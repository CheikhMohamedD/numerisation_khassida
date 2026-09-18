#!/usr/bin/env python3
"""
M3 — extraction d'EXEMPLAIRES DE GLYPHES depuis les lignes de la khassida.

Chaque composante connexe de l'encre ≈ un PAW (piece of Arabic word) ou une
lettre isolée : ce sont les tracés réels de la calligraphie épaisse, matière
première pour vectoriser et reconstituer chaque caractère à la même graisse.

Les diacritiques (petits points/marques) sont détectés par taille et rangés à
part (dossier `marks/`), car ils se traiteront comme `mark`/`mkmk` dans la police.

Entrée : data/lines/khassida/page-*/line-*.png
Sortie :
    font/glyph_exemplars/paws/<line>__cNN.png     (tracés principaux)
    font/glyph_exemplars/marks/<line>__cNN.png    (diacritiques présumés)
    font/glyph_exemplars/manifest.jsonl

Usage :
    python font/extract_glyph_exemplars.py [--min-area 400] [--pad 6]
"""
import argparse
import json
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
LINES = ROOT / "data" / "lines" / "khassida"
OUT = ROOT / "font" / "glyph_exemplars"


def binarize(gray):
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, bw = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return bw


def extract(path, min_area, pad, mark_max_area):
    img = cv2.imread(str(path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bw = binarize(gray)
    # ferme les micro-trous pour des composantes propres
    bw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    n, _, stats, _ = cv2.connectedComponentsWithStats(bw, connectivity=8)
    H, W = gray.shape
    out = []
    for i in range(1, n):
        x, y, w, h, area = stats[i]
        if area < 15:  # bruit
            continue
        kind = "marks" if area < mark_max_area and h < H * 0.33 else "paws"
        if kind == "paws" and area < min_area:
            continue
        x0, y0 = max(0, x - pad), max(0, y - pad)
        x1, y1 = min(W, x + w + pad), min(H, y + h + pad)
        out.append((kind, img[y0:y1, x0:x1], (int(x0), int(y0), int(x1), int(y1)), int(area)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--min-area", type=int, default=500, help="Aire min d'un PAW (px)")
    ap.add_argument("--mark-max-area", type=int, default=350, help="Aire max d'un diacritique")
    ap.add_argument("--pad", type=int, default=6)
    args = ap.parse_args()

    (OUT / "paws").mkdir(parents=True, exist_ok=True)
    (OUT / "marks").mkdir(parents=True, exist_ok=True)
    lines = sorted(LINES.glob("page-*/line-*.png"))
    manifest = []
    counts = {"paws": 0, "marks": 0}
    for lp in lines:
        tag = f"{lp.parent.name}_{lp.stem}"
        comps = extract(lp, args.min_area, args.pad, args.mark_max_area)
        for k, (kind, crop, bbox, area) in enumerate(comps, 1):
            rel = f"{kind}/{tag}__c{k:02d}.png"
            cv2.imwrite(str(OUT / rel), crop)
            manifest.append({"src_line": str(lp.relative_to(LINES)), "kind": kind,
                             "path": rel, "bbox": bbox, "area": area})
            counts[kind] += 1

    with (OUT / "manifest.jsonl").open("w", encoding="utf-8") as f:
        for m in manifest:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(f"{len(lines)} lignes → {counts['paws']} PAWs + {counts['marks']} diacritiques.")
    print(f"  → {OUT}")


if __name__ == "__main__":
    main()
