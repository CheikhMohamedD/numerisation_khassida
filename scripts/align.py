#!/usr/bin/env python3
"""
M2 — alignement de séquence : texte de RÉFÉRENCE (vers du classique) ↔ LIGNES
calligraphiques de la khassida. Produit des paires (image de ligne ↔ texte) pour
l'entraînement OCR et l'étiquetage des glyphes, sans transcription manuelle.

Deux modes :
- **proportionnel (défaut)** : le texte de la khassida n'existe pas encore
  (c'est la cible OCR). On mappe chaque ligne à un vers par position
  proportionnelle → alignement PROVISOIRE, marqué `needs_review: true`.
- **needleman-wunsch (`--khassida-ocr FILE`)** : dès qu'un premier OCR des lignes
  khassida existe, on aligne par similarité de texte (global, monotone).

Entrées :
    data/reference_text/verses.jsonl      (vers de référence)
    data/lines/khassida/manifest.jsonl    (lignes khassida)
Sortie :
    data/alignment/pairs.jsonl
      {line_id, line_path, ref_verse_id, ref_text, method, score, needs_review}

Usage :
    python scripts/align.py
    python scripts/align.py --khassida-ocr data/lines/khassida/ocr.jsonl
"""
import argparse
import json
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from normalize import strip_diacritics as bare  # noqa: E402

REF = ROOT / "data" / "reference_text" / "verses.jsonl"
LINES = ROOT / "data" / "lines" / "khassida" / "manifest.jsonl"
OUT = ROOT / "data" / "alignment" / "pairs.jsonl"


def load_jsonl(p):
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def proportional(verses, lines):
    n, m = len(verses), len(lines)
    pairs = []
    for i, ln in enumerate(lines):
        j = min(n - 1, round(i * (n - 1) / max(1, m - 1)))
        v = verses[j]
        pairs.append({
            "line_id": ln["line_id"], "line_path": ln["path"],
            "ref_verse_id": v["id"], "ref_text": v["text"],
            "method": "proportional_draft", "score": None, "needs_review": True,
        })
    return pairs


def needleman_wunsch(verses, lines, ocr_by_line, gap=-0.4):
    """Alignement global monotone lignes↔vers par similarité de texte."""
    n, m = len(lines), len(verses)
    sim = lambda a, b: SequenceMatcher(None, a, b).ratio()
    ref_bare = [bare(v["text"]) for v in verses]
    line_bare = [bare(ocr_by_line.get(l["line_id"], "")) for l in lines]

    # DP
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = D[i - 1][0] + gap
    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] + gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = D[i - 1][j - 1] + sim(line_bare[i - 1], ref_bare[j - 1])
            D[i][j] = max(match, D[i - 1][j] + gap, D[i][j - 1] + gap)
    # backtrack
    pairs, i, j = [], n, m
    while i > 0 and j > 0:
        s = sim(line_bare[i - 1], ref_bare[j - 1])
        if D[i][j] == D[i - 1][j - 1] + s:
            v, ln = verses[j - 1], lines[i - 1]
            pairs.append({
                "line_id": ln["line_id"], "line_path": ln["path"],
                "ref_verse_id": v["id"], "ref_text": v["text"],
                "method": "needleman_wunsch", "score": round(s, 3),
                "needs_review": s < 0.55,
            })
            i, j = i - 1, j - 1
        elif D[i][j] == D[i - 1][j] + gap:
            i -= 1
        else:
            j -= 1
    return list(reversed(pairs))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--khassida-ocr", default="", help="JSONL {line_id,text} d'un OCR khassida")
    args = ap.parse_args()

    verses = load_jsonl(REF)
    lines = load_jsonl(LINES)
    OUT.parent.mkdir(parents=True, exist_ok=True)

    if args.khassida_ocr:
        ocr = {r["line_id"]: r["text"] for r in load_jsonl(Path(args.khassida_ocr))}
        pairs = needleman_wunsch(verses, lines, ocr)
        method = "needleman_wunsch"
    else:
        pairs = proportional(verses, lines)
        method = "proportional_draft"

    with OUT.open("w", encoding="utf-8") as f:
        for p in pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    review = sum(1 for p in pairs if p["needs_review"])
    print(f"Alignement [{method}] : {len(pairs)} paires "
          f"({len(verses)} vers, {len(lines)} lignes), {review} à revoir.")
    print(f"  → {OUT}")


if __name__ == "__main__":
    main()
