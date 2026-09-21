#!/usr/bin/env python3
"""
Prépare le jeu d'entraînement OCR-VLM au format **Soup / LLaVA**, à partir des
paires (image de ligne ↔ texte) VÉRIFIÉES : le gold du jeu de test figé + les
paires d'alignement confiantes (needs_review=false).

C'est le fichier que consomme `soup train -c ocr/configs/soup-vision-ocr.yaml`.
Tant qu'on n'a pas assez de lignes fiables, l'entraînement n'est pas déclenché
(voir la jauge du rapport). Cible indicative : ~200 lignes.

Sortie : data/ocr_lines_train.jsonl
    {"image": "page-01/line-0001.png",
     "conversations": [{"from":"human","value":"<image>\\nTranscris..."},
                       {"from":"gpt","value":"<texte>"}]}

Usage : python ocr/build_soup_dataset.py [--target 200]
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GOLD = ROOT / "data" / "test_set" / "gold.jsonl"
PAIRS = ROOT / "data" / "alignment" / "pairs.jsonl"
OUT = ROOT / "data" / "ocr_lines_train.jsonl"
PROMPT = "<image>\nTranscris fidèlement le texte arabe de cette ligne."


def load_jsonl(p):
    p = Path(p)
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.exists() else []


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", type=int, default=200)
    args = ap.parse_args()

    rows, seen = [], set()
    # 1) gold vérifié (source la plus fiable)
    for g in load_jsonl(GOLD):
        if g["path"] not in seen:
            seen.add(g["path"]); rows.append((g["path"], g["text"], "gold"))
    # 2) alignement fiable : ancres + paires validées en revue ; on exclut les
    #    lignes rejetées (illisibles ou mal segmentées).
    for p in load_jsonl(PAIRS):
        if p.get("rejected"):
            continue
        if not p.get("needs_review", True) and p["line_path"] not in seen:
            seen.add(p["line_path"]); rows.append((p["line_path"], p["ref_text"], "align"))

    with OUT.open("w", encoding="utf-8") as f:
        for path, text, _ in rows:
            f.write(json.dumps({
                "image": path,
                "conversations": [
                    {"from": "human", "value": PROMPT},
                    {"from": "gpt", "value": text},
                ]}, ensure_ascii=False) + "\n")

    n = len(rows)
    ng = sum(1 for _, _, s in rows if s == "gold")
    print(f"Jeu d'entraînement Soup : {n} lignes ({ng} gold + {n-ng} alignées) → {OUT}")
    print(f"image_dir attendu : data/lines/khassida  (cf. ocr/configs/soup-vision-ocr.yaml)")
    if n >= args.target:
        print(f"✅ ≥ {args.target} lignes : prêt à déclencher\n"
              f"   soup train -c ocr/configs/soup-vision-ocr.yaml   # pip install \"soup-cli[vision]\"")
    else:
        print(f"⛔ {n}/{args.target} lignes fiables — enrichir d'abord (gold étendu / "
              f"alignement confiant via un meilleur OCR) avant de lancer Soup.")


if __name__ == "__main__":
    main()
