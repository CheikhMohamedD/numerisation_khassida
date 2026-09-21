#!/usr/bin/env python3
"""
Réinjecte les décisions de l'interface de revue (review.json) dans le pipeline.

- status `ok`        → la paire devient FIABLE (`needs_review: false`), avec le
                       texte corrigé s'il a été édité (`method: reviewed`).
- status `rejected`  → la paire est marquée inutilisable (`rejected: true`) et
                       exclue du jeu d'entraînement (ligne illisible ou mal
                       segmentée).

Met à jour `data/alignment/pairs.jsonl` puis reconstruit le jeu Soup.

Usage :
    python scripts/apply_review.py ~/Downloads/review.json
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAIRS = ROOT / "data" / "alignment" / "pairs.jsonl"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("review", help="Chemin du review.json exporté")
    ap.add_argument("--no-rebuild", action="store_true",
                    help="Ne pas relancer build_soup_dataset.py")
    args = ap.parse_args()

    rev_path = Path(args.review).expanduser()
    if not rev_path.exists():
        print(f"Introuvable : {rev_path}", file=sys.stderr)
        sys.exit(1)

    decisions = {r["path"]: r for r in json.loads(rev_path.read_text(encoding="utf-8"))}
    pairs = [json.loads(l) for l in PAIRS.read_text(encoding="utf-8").splitlines() if l.strip()]

    n_ok = n_rej = n_corr = 0
    for p in pairs:
        d = decisions.get(p["line_path"])
        if not d:
            continue
        if d["status"] == "ok":
            if d.get("corrected") and d["text"] != p["ref_text"]:
                p["ref_text"] = d["text"]
                n_corr += 1
            p["needs_review"] = False
            p["method"] = "reviewed"
            p.pop("rejected", None)
            n_ok += 1
        elif d["status"] == "rejected":
            p["rejected"] = True
            p["needs_review"] = True
            n_rej += 1

    with PAIRS.open("w", encoding="utf-8") as f:
        for p in pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    reliable = sum(1 for p in pairs if not p.get("needs_review", True)
                   and not p.get("rejected"))
    print(f"Revue appliquée : {n_ok} validées ({n_corr} corrigées), {n_rej} rejetées.")
    print(f"Paires fiables au total : {reliable} / {len(pairs)}")

    if not args.no_rebuild:
        print("\nReconstruction du jeu d'entraînement Soup :")
        subprocess.run([sys.executable, str(ROOT / "ocr" / "build_soup_dataset.py")],
                       check=False)


if __name__ == "__main__":
    main()
