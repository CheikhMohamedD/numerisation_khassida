#!/usr/bin/env python3
"""
M4 — évaluation OCR : CER / WER sur le jeu de test figé.

Compare les prédictions d'un OCR aux transcriptions gold (data/test_set/gold.jsonl).
Rapporte deux métriques, conformément à la politique (diacritiques inclus) :
- **CER brut** (diacritiques compris)
- **CER sans diacritiques** (qualité du rasm seul)

Entrées :
    data/test_set/gold.jsonl            ({path, text})
    <predictions>.jsonl                 ({path, text})  (déf: data/lines/khassida/ocr.jsonl)
Sortie :
    eval/reports/cer_<pred>.json + tableau console.

Usage :
    python eval/cer.py [--pred data/lines/khassida/ocr.jsonl]
"""
import argparse
import json
import sys
from pathlib import Path

import jiwer

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from normalize import normalize_text, strip_diacritics as strip_diac  # noqa: E402

GOLD = ROOT / "data" / "test_set" / "gold.jsonl"


def load(p):
    return {json.loads(l)["path"]: json.loads(l)["text"]
            for l in Path(p).read_text(encoding="utf-8").splitlines() if l.strip()}


def cer(ref, hyp):
    ref = [r for r in ref]
    return jiwer.cer(ref, hyp)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pred", default=str(ROOT / "data/lines/khassida/ocr.jsonl"))
    args = ap.parse_args()

    gold = load(GOLD)
    pred = load(args.pred)
    common = [p for p in gold if p in pred]
    if not common:
        print("Aucune ligne commune gold/pred.", file=sys.stderr)
        return

    refs = [normalize_text(gold[p]) for p in common]
    hyps = [normalize_text(pred[p]) for p in common]
    refs_bare = [strip_diac(gold[p]) for p in common]
    hyps_bare = [strip_diac(pred[p]) for p in common]

    cer_raw = jiwer.cer(refs, hyps)
    wer_raw = jiwer.wer(refs, hyps)
    cer_bare = jiwer.cer(refs_bare, hyps_bare)

    print(f"Jeu de test : {len(common)} lignes")
    print(f"  CER brut (diacritiques inclus) : {cer_raw*100:.1f} %")
    print(f"  CER sans diacritiques (rasm)   : {cer_bare*100:.1f} %")
    print(f"  WER brut                        : {wer_raw*100:.1f} %")
    print("\n  Par ligne (CER sans diacritiques) :")
    for p in common:
        c = jiwer.cer([strip_diac(gold[p])], [strip_diac(pred[p])])
        print(f"    {p}: {c*100:5.1f} %   pred='{pred[p][:40]}'")

    rep = {"pred": args.pred, "n_lines": len(common),
           "cer_raw": cer_raw, "cer_bare": cer_bare, "wer_raw": wer_raw}
    out = ROOT / "eval" / "reports" / f"cer_{Path(args.pred).stem}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  → {out}")


if __name__ == "__main__":
    main()
