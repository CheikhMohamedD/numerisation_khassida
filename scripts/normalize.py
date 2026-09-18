#!/usr/bin/env python3
"""
Normalisation Unicode du texte arabe, conforme à docs/unicode-policy.md.

Politique retenue :
- NFC
- diacritiques (ḥarakāt) CONSERVÉS (le corpus est vocalisé)
- kashida U+0640 RETIRÉ (allongement purement typographique)
- graphie source conservée (pas de normalisation alif/hamza/tāʾ marbūṭa)
- espaces uniformisés, trim par ligne, presentation forms décomposées vers base

Usage :
    python scripts/normalize.py < in.txt > out.txt
    from normalize import normalize_text
"""
import re
import sys
import unicodedata

TATWEEL = "ـ"  # kashida
# Zero-width et marques de direction à retirer
ZERO_WIDTH = dict.fromkeys(map(ord, "​‌‍‎‏﻿"), None)


def normalize_text(text: str) -> str:
    # 1) Décompose les presentation forms (FB50–FEFF) vers lettres de base, puis NFC.
    text = unicodedata.normalize("NFKC", text)
    text = unicodedata.normalize("NFC", text)
    # 2) Retire kashida + caractères zero-width / marques directionnelles.
    text = text.replace(TATWEEL, "")
    text = text.translate(ZERO_WIDTH)
    # 3) Espaces : tabs -> espace, espaces multiples -> un seul, trim par ligne.
    out_lines = []
    for line in text.split("\n"):
        line = line.replace("\t", " ")
        line = re.sub(r"[  ]{2,}", " ", line).strip()
        out_lines.append(line)
    # 4) Supprime les lignes vides en excès (max une vide consécutive).
    text = "\n".join(out_lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n")
    return text


ARABIC_CHAR = re.compile(r"[؀-ۿ]")


def is_arabic_line(line: str, min_ratio: float = 0.3) -> bool:
    """Vrai si la ligne contient une proportion suffisante de caractères arabes."""
    stripped = re.sub(r"\s", "", line)
    if not stripped:
        return False
    ar = sum(1 for c in stripped if ARABIC_CHAR.match(c))
    return ar / len(stripped) >= min_ratio


if __name__ == "__main__":
    sys.stdout.write(normalize_text(sys.stdin.read()))
