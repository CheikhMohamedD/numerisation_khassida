#!/usr/bin/env python3
"""
M2 — OCR du PDF classique (naskh imprimé vocalisé) pour produire le TEXTE DE
RÉFÉRENCE. Le classique a une couche texte cassée (mojibake) ; on OCR donc
l'image, qui est propre. Sortie : texte normalisé + découpe en vers (abyāt).

Entrée : data/images/classique/page-*.png
Sortie :
    data/reference_text/classique.txt         (texte normalisé complet)
    data/reference_text/verses.jsonl          ({"id","page","text"} par vers)

Nécessite : tesseract (+ langue `ara`), pytesseract.

Usage :
    python ocr/ocr_classique.py [--psm 6]
"""
import argparse
import json
import sys
from pathlib import Path

import pytesseract
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from normalize import normalize_text, is_arabic_line  # noqa: E402

IMG_DIR = ROOT / "data" / "images" / "classique"
OUT_DIR = ROOT / "data" / "reference_text"


def ocr_page(path: Path, lang: str, psm: int) -> str:
    img = Image.open(path)
    cfg = f"--oem 1 --psm {psm}"
    txt = pytesseract.image_to_string(img, lang=lang, config=cfg)
    return normalize_text(txt)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lang", default="ara")
    ap.add_argument("--psm", type=int, default=6, help="Tesseract page seg mode")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pages = sorted(IMG_DIR.glob("page-*.png"))
    if not pages:
        print(f"Aucune image dans {IMG_DIR}", file=sys.stderr)
        return

    full = []
    verses = []
    vid = 0
    for p in pages:
        page_no = int(p.stem.split("-")[-1])
        text = ocr_page(p, args.lang, args.psm)
        full.append(f"# page {page_no}\n{text}")
        for line in text.split("\n"):
            line = line.strip()
            if is_arabic_line(line):
                vid += 1
                verses.append({"id": vid, "page": page_no, "text": line})
        print(f"  page {page_no:02d}: {len([l for l in text.splitlines() if l.strip()])} lignes")

    (OUT_DIR / "classique.txt").write_text("\n\n".join(full), encoding="utf-8")
    with (OUT_DIR / "verses.jsonl").open("w", encoding="utf-8") as f:
        for v in verses:
            f.write(json.dumps(v, ensure_ascii=False) + "\n")

    print(f"\n{len(pages)} pages OCR → {len(verses)} vers (lignes arabes).")
    print(f"  {OUT_DIR/'classique.txt'}")
    print(f"  {OUT_DIR/'verses.jsonl'}")


if __name__ == "__main__":
    main()
