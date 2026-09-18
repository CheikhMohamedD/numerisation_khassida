#!/usr/bin/env python3
"""
Phase A — rasterise les PDF des Khassida en images (400 DPI par défaut).

Entrée : data/raw_pdfs/*.pdf
Sortie : data/images/<nom_pdf>/page_0001.png ...

Nécessite Poppler (brew install poppler) + `pip install pdf2image`.

Usage:
    python preprocessing/pdf_to_images.py [--dpi 400] [--fmt png]
"""
import argparse
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = HERE / "data" / "raw_pdfs"
OUT = HERE / "data" / "images"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dpi", type=int, default=400)
    ap.add_argument("--fmt", default="png")
    args = ap.parse_args()

    from pdf2image import convert_from_path

    pdfs = sorted(RAW.glob("*.pdf"))
    if not pdfs:
        print(f"Aucun PDF dans {RAW}. Dépose tes Khassida puis relance.")
        return

    for pdf in pdfs:
        dst = OUT / pdf.stem
        dst.mkdir(parents=True, exist_ok=True)
        print(f"[{pdf.name}] rasterisation à {args.dpi} DPI ...")
        pages = convert_from_path(str(pdf), dpi=args.dpi)
        for i, img in enumerate(pages, 1):
            img.save(dst / f"page_{i:04d}.{args.fmt}")
        print(f"  -> {len(pages)} pages dans {dst}")


if __name__ == "__main__":
    main()
