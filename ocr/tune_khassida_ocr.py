#!/usr/bin/env python3
"""
M5 — tente d'améliorer l'OCR de la KHASSIDA (calligraphie) par prétraitement,
mesuré contre le gold `data/test_set/gold.jsonl` (10 lignes page 1).

Tesseract n'a pas de modèle pour cette calligraphie : l'objectif n'est pas de
la « résoudre » mais de voir si un prétraitement réduit assez le CER pour
rendre l'alignement exploitable (et donc générer des labels).

Usage : python ocr/tune_khassida_ocr.py
"""
import json
import sys
from pathlib import Path

import cv2
import jiwer
import numpy as np
import pytesseract
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from normalize import normalize_text, strip_diacritics  # noqa: E402

LINES = ROOT / "data" / "lines" / "khassida"
GOLD = ROOT / "data" / "test_set" / "gold.jsonl"


def pp_raw(g):
    return g


def pp_otsu(g):
    _, b = cv2.threshold(cv2.GaussianBlur(g, (3, 3), 0), 0, 255,
                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return b


def pp_otsu_up(g):
    b = pp_otsu(g)
    return cv2.resize(b, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)


def pp_down(g):
    # la calligraphie est très épaisse : réduire peut aider Tesseract
    return cv2.resize(g, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)


def pp_otsu_thin(g):
    b = pp_otsu(g)
    # amincir les traits (erode sur encre noire = dilate du blanc)
    return cv2.dilate(b, np.ones((3, 3), np.uint8), iterations=1)


def pp_clahe(g):
    return cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(g)


PREPROC = {"raw": pp_raw, "otsu": pp_otsu, "otsu+up": pp_otsu_up,
           "down0.6": pp_down, "otsu+thin": pp_otsu_thin, "clahe": pp_clahe}
PSMS = [7, 6, 13]


def main():
    gold = {json.loads(l)["path"]: json.loads(l)["text"]
            for l in GOLD.read_text(encoding="utf-8").splitlines() if l.strip()}

    results = []
    for pname, fn in PREPROC.items():
        for psm in PSMS:
            refs, hyps = [], []
            for path, gtext in gold.items():
                gray = cv2.cvtColor(cv2.imread(str(LINES / path)), cv2.COLOR_BGR2GRAY)
                txt = pytesseract.image_to_string(
                    Image.fromarray(fn(gray)), lang="ara",
                    config=f"--oem 1 --psm {psm}")
                hyps.append(strip_diacritics(" ".join(normalize_text(txt).split())))
                refs.append(strip_diacritics(gtext))
            cer = jiwer.cer(refs, hyps)
            empty = sum(1 for h in hyps if not h.strip())
            results.append((cer, pname, psm, empty))
            print(f"  {pname:11} psm={psm:<3} CER={cer*100:5.1f}%  vides={empty}/10")

    results.sort()
    print("\n=== Classement ===")
    for cer, pname, psm, empty in results[:5]:
        print(f"  {cer*100:5.1f}%  {pname} psm={psm} (vides={empty})")
    print(f"\nBaseline actuelle (raw psm=7) : 76.6 %")
    print(f"Meilleur ici : {results[0][1]} psm={results[0][2]} → {results[0][0]*100:.1f} %")


if __name__ == "__main__":
    main()
