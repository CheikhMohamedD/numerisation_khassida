#!/usr/bin/env python3
"""
Génère un rapport HTML autonome (images intégrées en base64) pour VISUALISER
l'état du projet : stats, overlay de segmentation, lignes page 1 (gold vs OCR
baseline + CER), exemplaires de glyphes, vérification du shaping de la police v0.

Sortie : report.html (à la racine) — ouvrir dans un navigateur.

Usage : python scripts/make_report.py
"""
import base64
import glob
import io
import json
from pathlib import Path

import cv2
import jiwer
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
import sys
sys.path.insert(0, str(ROOT / "scripts"))
from normalize import normalize_text, strip_diacritics  # noqa: E402

LINES = ROOT / "data" / "lines" / "khassida"
OUT = ROOT / "report.html"


def b64(img: Image.Image, w=None):
    if w and img.width > w:
        img = img.resize((w, round(img.height * w / img.width)))
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="JPEG", quality=80)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def load_jsonl(p):
    p = Path(p)
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def seg_overlay():
    page = ROOT / "data" / "images" / "khassida" / "page-01.png"
    if not page.exists():
        return None
    img = Image.open(page).convert("RGB")
    d = ImageDraw.Draw(img)
    man = [m for m in load_jsonl(LINES / "manifest.jsonl") if m["page"] == 1]
    for m in man:
        x0, y0, x1, y1 = m["bbox"]
        d.rectangle([x0, y0, x1, y1], outline=(200, 30, 30), width=6)
    return b64(img, 700)


def exemplar_sheet(n=40):
    fs = sorted(glob.glob(str(ROOT / "font/glyph_exemplars/paws/page-01_*.png")))[:n]
    if not fs:
        return None
    ims = [Image.open(f).convert("RGB") for f in fs]
    ims = [im.resize((round(im.width * 90 / im.height), 90)) for im in ims]
    per = 8
    rows = [ims[i:i + per] for i in range(0, len(ims), per)]
    W = max(sum(im.width + 6 for im in r) for r in rows)
    H = len(rows) * 96
    sheet = Image.new("RGB", (W, H), (245, 244, 238))
    y = 0
    for r in rows:
        x = 0
        for im in r:
            sheet.paste(im, (x, y)); x += im.width + 6
        y += 96
    return b64(sheet, 900)


def font_shaping():
    ttf = ROOT / "font" / "build" / "khassida-scaffold-v0.ttf"
    if not ttf.exists():
        return []
    import uharfbuzz as hb
    from fontTools.ttLib import TTFont
    order = TTFont(str(ttf)).getGlyphOrder()
    font = hb.Font(hb.Face(hb.Blob.from_file_path(str(ttf))))
    res = []
    for t in ["بببب", "با", "الله", "سمس", "دد"]:
        buf = hb.Buffer(); buf.add_str(t); buf.guess_segment_properties()
        hb.shape(font, buf, {})
        res.append((t, "  ".join(order[i.codepoint] for i in buf.glyph_infos)))
    return res


def main():
    manifest = load_jsonl(LINES / "manifest.jsonl")
    verses = load_jsonl(ROOT / "data/reference_text/verses.jsonl")
    gold = {r["path"]: r["text"] for r in load_jsonl(ROOT / "data/test_set/gold.jsonl")}
    ocr = {r["path"]: r["text"] for r in load_jsonl(LINES / "ocr.jsonl")}
    exemplars = load_jsonl(ROOT / "font/glyph_exemplars/manifest.jsonl")

    # CER global sur gold
    common = [p for p in gold if p in ocr]
    cer_raw = jiwer.cer([normalize_text(gold[p]) for p in common],
                        [normalize_text(ocr[p]) for p in common]) if common else None
    cer_bare = jiwer.cer([strip_diacritics(gold[p]) for p in common],
                         [strip_diacritics(ocr[p]) for p in common]) if common else None

    # lignes page 1
    rows = []
    for m in [m for m in manifest if m["page"] == 1]:
        crop = Image.open(LINES / m["path"])
        g = gold.get(m["path"], "")
        o = ocr.get(m["path"], "")
        c = jiwer.cer([strip_diacritics(g)], [strip_diacritics(o)]) if g else None
        rows.append((b64(crop, 620), g, o, c))

    st = f"""
    <div class=grid>
      <div class=stat><b>{len({m['page'] for m in manifest})}</b><span>pages khassida</span></div>
      <div class=stat><b>{len(manifest)}</b><span>lignes segmentées</span></div>
      <div class=stat><b>{len(verses)}</b><span>vers de référence</span></div>
      <div class=stat><b>{len(exemplars)}</b><span>exemplaires de glyphes</span></div>
      <div class=stat><b>{cer_bare*100:.1f}%</b><span>CER baseline (rasm)</span></div>
    </div>""" if cer_bare is not None else ""

    line_rows = "".join(
        f"<tr><td class=img><img src='{im}'></td>"
        f"<td class=ar dir=rtl>{g}</td>"
        f"<td class=ar dir=rtl>{o or '<i>—</i>'}</td>"
        f"<td class=cer>{('%.0f%%'%(c*100)) if c is not None else ''}</td></tr>"
        for im, g, o, c in rows)

    ex = exemplar_sheet()
    seg = seg_overlay()
    shaping = "".join(f"<tr><td class=ar dir=rtl>{t}</td><td class=mono>{r}</td></tr>"
                      for t, r in font_shaping())

    html = f"""<!doctype html><html lang=fr><head><meta charset=utf-8>
<title>Numérisation Khassida — état</title>
<style>
 body{{font-family:-apple-system,system-ui,sans-serif;max-width:1000px;margin:0 auto;
   padding:24px;color:#1c1c1c;background:#f7f4ed}}
 h1{{font-size:26px}} h2{{margin-top:34px;border-bottom:2px solid #1c1c1c;padding-bottom:4px}}
 .grid{{display:flex;gap:12px;flex-wrap:wrap}}
 .stat{{background:#fff;border:1px solid #eceae4;border-radius:12px;padding:14px 18px;text-align:center}}
 .stat b{{display:block;font-size:24px}} .stat span{{font-size:12px;color:#5f5f5d}}
 table{{border-collapse:collapse;width:100%;margin-top:12px;background:#fff}}
 td,th{{border:1px solid #eceae4;padding:8px;vertical-align:middle}}
 .img img{{max-width:620px;display:block}}
 .ar{{font-size:22px;line-height:1.8}} .cer{{font-weight:700;text-align:center}}
 .mono{{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:#3b3b3b}}
 img{{border:1px solid #eceae4;border-radius:6px}}
 .cap{{color:#5f5f5d;font-size:13px;margin:4px 0 10px}}
</style></head><body>
<h1>Numérisation des Khassida — état visuel</h1>
<p class=cap>Corpus parallèle (classique ↔ calligraphie). Jalons M0–M4. Rapport auto-généré.</p>
{st}

<h2>1 · Segmentation en lignes (page 1)</h2>
<p class=cap>Chaque cadre rouge = une ligne détectée (profil de projection).</p>
{f"<img src='{seg}'>" if seg else "<i>page indisponible</i>"}

<h2>2 · Lignes page 1 — gold vs OCR baseline</h2>
<p class=cap>Colonnes : image · vérité terrain (gold) · OCR Tesseract (baseline) · CER (rasm).</p>
<table><tr><th>Ligne</th><th>Gold</th><th>OCR baseline</th><th>CER</th></tr>{line_rows}</table>

<h2>3 · Exemplaires de glyphes (page 1)</h2>
<p class=cap>Composantes connexes = tracés réels à la graisse d'origine (matière pour la police).</p>
{f"<img src='{ex}'>" if ex else "<i>exemplaires non générés</i>"}

<h2>4 · Police v0 — vérification du shaping (HarfBuzz)</h2>
<p class=cap>La bonne forme contextuelle est choisie selon la position (glyphes placeholder).</p>
<table><tr><th>Texte</th><th>Glyphes sélectionnés</th></tr>{shaping}</table>
</body></html>"""

    OUT.write_text(html, encoding="utf-8")
    print(f"Rapport → {OUT}")
    print("Ouvre-le avec :  open report.html")


if __name__ == "__main__":
    main()
