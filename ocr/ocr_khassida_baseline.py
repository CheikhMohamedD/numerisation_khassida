#!/usr/bin/env python3
"""
M4 — OCR BASELINE de la khassida avec Tesseract `ara` (modèle générique).

La calligraphie warsh épaisse est hors distribution pour Tesseract → résultat
volontairement faible : c'est le **point de référence (CER baseline) à battre**
par un modèle entraîné (Kraken/TrOCR ou VLM Soup). Sert aussi à amorcer
l'alignement Needleman-Wunsch (scripts/align.py --khassida-ocr).

Entrée : data/lines/khassida/manifest.jsonl (+ crops)
Sortie : data/lines/khassida/ocr.jsonl  ({line_id, path, text})

Usage : python ocr/ocr_khassida_baseline.py [--psm 7] [--limit N]
"""
import argparse
import json
import sys
from pathlib import Path

import cv2
import pytesseract
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from normalize import normalize_text  # noqa: E402

LINES = ROOT / "data" / "lines" / "khassida"


def preprocess(path, scale):
    """Sous-échantillonnage : la calligraphie est très épaisse, la réduire aide
    nettement Tesseract. Meilleure config mesurée (gold 10 lignes) :
    scale=0.6 + psm 13 → CER rasm 55.9 % (vs 76.6 % en raw/psm 7), 0 ligne vide.
    Voir ocr/tune_khassida_ocr.py."""
    gray = cv2.cvtColor(cv2.imread(str(path)), cv2.COLOR_BGR2GRAY)
    if scale and scale != 1.0:
        gray = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    return Image.fromarray(gray)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lang", default="ara")
    ap.add_argument("--psm", type=int, default=13, help="13 = ligne brute (meilleur ici)")
    ap.add_argument("--scale", type=float, default=0.6, help="Sous-échantillonnage")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    manifest = [json.loads(l) for l in (LINES / "manifest.jsonl").read_text(
        encoding="utf-8").splitlines() if l.strip()]
    if args.limit:
        manifest = manifest[: args.limit]

    out = LINES / "ocr.jsonl"
    cfg = f"--oem 1 --psm {args.psm}"
    with out.open("w", encoding="utf-8") as f:
        for i, m in enumerate(manifest, 1):
            img = preprocess(LINES / m["path"], args.scale)
            txt = normalize_text(pytesseract.image_to_string(img, lang=args.lang, config=cfg))
            txt = " ".join(txt.split())  # ligne unique
            f.write(json.dumps({"line_id": m["line_id"], "path": m["path"],
                                "text": txt}, ensure_ascii=False) + "\n")
            if i % 50 == 0:
                print(f"  {i}/{len(manifest)}")
    print(f"{len(manifest)} lignes OCR → {out}")


if __name__ == "__main__":
    main()
