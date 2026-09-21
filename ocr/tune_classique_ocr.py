#!/usr/bin/env python3
"""
M5 — optimise l'OCR du CLASSIQUE (texte de référence) de façon MESURÉE.

Balaie des variantes de prétraitement × PSM Tesseract, calcule le CER contre le
gold `data/test_set/gold_classique.jsonl` (page 1), et affiche le classement.
Le but : fiabiliser la référence, car elle plafonne l'alignement (donc les
labels d'entraînement).

Usage : python ocr/tune_classique_ocr.py
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
from normalize import normalize_text, is_arabic_line, strip_diacritics  # noqa: E402

PAGE = ROOT / "data" / "images" / "classique" / "page-01.png"
GOLD = ROOT / "data" / "test_set" / "gold_classique.jsonl"


# --- variantes de prétraitement ---------------------------------------------

def pp_raw(g):
    return g


def pp_otsu(g):
    _, b = cv2.threshold(cv2.GaussianBlur(g, (3, 3), 0), 0, 255,
                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return b


def pp_sauvola(g):
    # approximation Sauvola via seuillage adaptatif gaussien
    return cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 41, 12)


def pp_upscale(g):
    return cv2.resize(g, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)


def pp_otsu_denoise(g):
    b = pp_otsu(g)
    return cv2.medianBlur(b, 3)


PREPROC = {"raw": pp_raw, "otsu": pp_otsu, "sauvola": pp_sauvola,
           "upscale": pp_upscale, "otsu+denoise": pp_otsu_denoise}
PSMS = [4, 6]


def ocr_lines(img_arr, psm):
    txt = pytesseract.image_to_string(Image.fromarray(img_arr), lang="ara",
                                      config=f"--oem 1 --psm {psm}")
    return [l for l in normalize_text(txt).split("\n") if is_arabic_line(l)]


def score(pred_lines, gold_lines):
    """CER (rasm) en alignant les n premières lignes communes."""
    n = min(len(pred_lines), len(gold_lines))
    if n == 0:
        return 1.0, 0
    refs = [strip_diacritics(g) for g in gold_lines[:n]]
    hyps = [strip_diacritics(p) for p in pred_lines[:n]]
    return jiwer.cer(refs, hyps), n


def main():
    gold = [json.loads(l)["text"] for l in GOLD.read_text(encoding="utf-8").splitlines() if l.strip()]
    gray = cv2.cvtColor(cv2.imread(str(PAGE)), cv2.COLOR_BGR2GRAY)

    results = []
    for pname, fn in PREPROC.items():
        arr = fn(gray)
        for psm in PSMS:
            lines = ocr_lines(arr, psm)
            cer, n = score(lines, gold)
            results.append((cer, pname, psm, len(lines), n))
            print(f"  {pname:13} psm={psm}  CER={cer*100:5.1f}%  "
                  f"lignes={len(lines)} (comparées={n})")

    results.sort()
    print("\n=== Classement (meilleur CER rasm) ===")
    for cer, pname, psm, nl, n in results[:5]:
        print(f"  {cer*100:5.1f}%  {pname} psm={psm}  ({nl} lignes)")
    best = results[0]
    print(f"\nMeilleure config : preproc={best[1]} psm={best[2]} → CER {best[0]*100:.1f}%")


if __name__ == "__main__":
    main()
