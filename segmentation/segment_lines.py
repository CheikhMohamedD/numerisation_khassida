#!/usr/bin/env python3
"""
M2 — segmentation en LIGNES de la khassida calligraphique (profil de projection).

Approche : binarisation (Otsu, encre=blanc), profil horizontal d'encre lissé,
découpe aux vallées (bandes sans encre) → une image par ligne, dans l'ordre
haut→bas. Pré-traitement léger (niveaux de gris + flou) pour la calligraphie
épaisse sur papier verdâtre.

Entrée : data/images/khassida/page-*.png
Sortie :
    data/lines/khassida/page-XX/line-YYYY.png
    data/lines/khassida/manifest.jsonl   ({"line_id","page","index","path","bbox"})

Usage :
    python segmentation/segment_lines.py [--min-height 40] [--pad 10]
"""
import argparse
import json
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "data" / "images" / "khassida"
OUT_DIR = ROOT / "data" / "lines" / "khassida"


def binarize(gray):
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Encre sombre -> premier plan blanc via THRESH_BINARY_INV + Otsu
    _, bw = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return bw


def find_line_bands(bw, min_height, smooth, thresh_ratio):
    proj = bw.sum(axis=1).astype(np.float64) / 255.0  # encre par ligne (px)
    if smooth > 1:
        k = np.ones(smooth) / smooth
        proj = np.convolve(proj, k, mode="same")
    thr = proj.max() * thresh_ratio
    on = proj > thr
    bands, start = [], None
    for i, v in enumerate(on):
        if v and start is None:
            start = i
        elif not v and start is not None:
            if i - start >= min_height:
                bands.append((start, i))
            start = None
    if start is not None and len(on) - start >= min_height:
        bands.append((start, len(on)))
    return bands


def segment_page(path, min_height, pad, smooth, thresh_ratio):
    img = cv2.imread(str(path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bw = binarize(gray)
    bands = find_line_bands(bw, min_height, smooth, thresh_ratio)
    H, W = gray.shape
    crops = []
    for (y0, y1) in bands:
        y0p, y1p = max(0, y0 - pad), min(H, y1 + pad)
        # bornes horizontales sur la bande (retirer marges vides)
        band_ink = bw[y0p:y1p].sum(axis=0)
        xs = np.where(band_ink > 0)[0]
        x0, x1 = (int(xs[0]), int(xs[-1] + 1)) if len(xs) else (0, W)
        x0p, x1p = max(0, x0 - pad), min(W, x1 + pad)
        crops.append((img[y0p:y1p, x0p:x1p], (int(x0p), int(y0p), int(x1p), int(y1p))))
    return crops


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    # Défauts calés sur la khassida (calligraphie warsh épaisse, ~11 lignes/page).
    ap.add_argument("--min-height", type=int, default=30)
    ap.add_argument("--pad", type=int, default=12)
    ap.add_argument("--smooth", type=int, default=9)
    ap.add_argument("--thresh-ratio", type=float, default=0.18)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pages = sorted(IMG_DIR.glob("page-*.png"))
    manifest = []
    lid = 0
    for p in pages:
        page_no = int(p.stem.split("-")[-1])
        crops = segment_page(p, args.min_height, args.pad, args.smooth, args.thresh_ratio)
        pdir = OUT_DIR / f"page-{page_no:02d}"
        pdir.mkdir(parents=True, exist_ok=True)
        for idx, (crop, bbox) in enumerate(crops, 1):
            lid += 1
            rel = f"page-{page_no:02d}/line-{idx:04d}.png"
            cv2.imwrite(str(OUT_DIR / rel), crop)
            manifest.append({"line_id": lid, "page": page_no, "index": idx,
                             "path": rel, "bbox": bbox})
        print(f"  page {page_no:02d}: {len(crops)} lignes")

    with (OUT_DIR / "manifest.jsonl").open("w", encoding="utf-8") as f:
        for m in manifest:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(f"\n{len(pages)} pages → {lid} lignes. Manifest: {OUT_DIR/'manifest.jsonl'}")


if __name__ == "__main__":
    main()
