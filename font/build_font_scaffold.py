#!/usr/bin/env python3
"""
M3 — squelette de police v0 (« brouillon ») pour la khassida.

Construit une fonte TTF **structurellement complète** : les 28+ lettres arabes,
leurs FORMES CONTEXTUELLES (isolée/initiale/médiane/finale) et les features
OpenType `isol/init/medi/fina` qui les sélectionnent selon le contexte. Les
contours sont des PLACEHOLDERS (rectangles avec ergots de liaison indiquant le
sens de jointure) — à remplacer par les tracés vectorisés des exemplaires
(`font/glyph_exemplars/`) en conservant la graisse d'origine.

L'intérêt du v0 : valider tout le pipeline de *shaping* arabe (le plus normatif)
avant de dessiner les glyphes. On prouve avec HarfBuzz que la bonne forme est
choisie selon la position.

Sortie : font/build/khassida-scaffold-v0.ttf  (+ features.fea)
Vérif   : shaping HarfBuzz imprimé en fin d'exécution.

Usage : python font/build_font_scaffold.py
"""
from pathlib import Path

from fontTools.fontBuilder import FontBuilder
from fontTools.feaLib.builder import addOpenTypeFeatures
from fontTools.pens.ttGlyphPen import TTGlyphPen

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "font" / "build"
TTF = BUILD / "khassida-scaffold-v0.ttf"
FEA = BUILD / "features.fea"

# (codepoint, nom, jointure)  jointure: D=dual (4 formes), R=right (isol+fina),
# U=non-joignant (isol seul)
LETTERS = [
    (0x0621, "hamza", "U"), (0x0623, "alefHamzaAbove", "R"),
    (0x0625, "alefHamzaBelow", "R"), (0x0627, "alef", "R"),
    (0x0622, "alefMadda", "R"), (0x0624, "wawHamza", "R"),
    (0x0626, "yehHamza", "D"), (0x0628, "beh", "D"), (0x0629, "tehMarbuta", "R"),
    (0x062A, "teh", "D"), (0x062B, "theh", "D"), (0x062C, "jeem", "D"),
    (0x062D, "hah", "D"), (0x062E, "khah", "D"), (0x062F, "dal", "R"),
    (0x0630, "thal", "R"), (0x0631, "reh", "R"), (0x0632, "zain", "R"),
    (0x0633, "seen", "D"), (0x0634, "sheen", "D"), (0x0635, "sad", "D"),
    (0x0636, "dad", "D"), (0x0637, "tah", "D"), (0x0638, "zah", "D"),
    (0x0639, "ain", "D"), (0x063A, "ghain", "D"), (0x0641, "feh", "D"),
    (0x0642, "qaf", "D"), (0x0643, "kaf", "D"), (0x0644, "lam", "D"),
    (0x0645, "meem", "D"), (0x0646, "noon", "D"), (0x0647, "heh", "D"),
    (0x0648, "waw", "R"), (0x0649, "alefMaksura", "R"), (0x064A, "yeh", "D"),
]

FORMS = {"D": ["isol", "init", "medi", "fina"],
         "R": ["isol", "fina"], "U": ["isol"]}

ADV = 700
STUB = 90


def draw(pen, join_left, join_right):
    """Corps rectangulaire + ergots de liaison (RTL : droite=prev, gauche=next)."""
    # corps
    pen.moveTo((120, 0)); pen.lineTo((120, 620)); pen.lineTo((580, 620))
    pen.lineTo((580, 0)); pen.closePath()
    if join_right:  # connexion à la lettre précédente (à droite)
        pen.moveTo((580, 0)); pen.lineTo((580, 140))
        pen.lineTo((580 + STUB, 140)); pen.lineTo((580 + STUB, 0)); pen.closePath()
    if join_left:  # connexion à la lettre suivante (à gauche)
        pen.moveTo((120 - STUB, 0)); pen.lineTo((120 - STUB, 140))
        pen.lineTo((120, 140)); pen.lineTo((120, 0)); pen.closePath()


def glyph_for_form(form):
    pen = TTGlyphPen(None)
    draw(pen, join_right=form in ("medi", "fina"),
              join_left=form in ("medi", "init"))
    return pen.glyph()


def build():
    BUILD.mkdir(parents=True, exist_ok=True)
    glyph_order = [".notdef", "space"]
    glyphs, metrics, cmap = {}, {}, {}

    # .notdef + space
    glyphs[".notdef"] = glyph_for_form("isol")
    glyphs["space"] = TTGlyphPen(None).glyph()
    metrics[".notdef"] = (ADV, 0); metrics["space"] = (ADV, 0)
    cmap[0x20] = "space"

    fea_feats = {f: [] for f in ("isol", "init", "medi", "fina")}
    for cp, name, join in LETTERS:
        cmap[cp] = name                       # glyphe nominal (mappé Unicode)
        glyphs[name] = glyph_for_form("isol")
        metrics[name] = (ADV, 0)
        glyph_order.append(name)
        for form in FORMS[join]:
            gname = f"{name}.{form}"
            glyphs[gname] = glyph_for_form(form)
            metrics[gname] = (ADV, 0)
            glyph_order.append(gname)
            fea_feats[form].append((name, gname))

    fb = FontBuilder(unitsPerEm=1000, isTTF=True)
    fb.setupGlyphOrder(glyph_order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupNameTable({
        "familyName": "Khassida Scaffold v0",
        "styleName": "Regular",
        "psName": "KhassidaScaffold-v0",
    })
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, usWinAscent=800, usWinDescent=200)
    fb.setupPost()

    # Features OpenType : chaque forme = substitution simple nominal -> variante.
    lines = ["languagesystem DFLT dflt;", "languagesystem arab dflt;", ""]
    for form, subs in fea_feats.items():
        if not subs:
            continue
        lines.append(f"feature {form} {{")
        for nominal, gname in subs:
            lines.append(f"    sub {nominal} by {gname};")
        lines.append(f"}} {form};")
        lines.append("")
    FEA.write_text("\n".join(lines), encoding="utf-8")
    addOpenTypeFeatures(fb.font, str(FEA))

    fb.save(str(TTF))
    print(f"Fonte v0 : {len(glyph_order)} glyphes → {TTF}")
    return TTF


def verify(ttf):
    import uharfbuzz as hb
    blob = hb.Blob.from_file_path(str(ttf))
    face = hb.Face(blob); font = hb.Font(face)
    gname = {v: k for k, v in {i: n for i, n in enumerate(
        __import__("fontTools").ttLib.TTFont(str(ttf)).getGlyphOrder())}.items()}
    order = __import__("fontTools").ttLib.TTFont(str(ttf)).getGlyphOrder()

    tests = ["بببب", "با", "الله", "سمس", "دد"]
    print("\n=== Vérification shaping (HarfBuzz) ===")
    for t in tests:
        buf = hb.Buffer(); buf.add_str(t); buf.guess_segment_properties()
        hb.shape(font, buf, {})
        names = [order[i.codepoint] for i in buf.glyph_infos]
        print(f"  {t}  →  {'  '.join(names)}")


if __name__ == "__main__":
    verify(build())
