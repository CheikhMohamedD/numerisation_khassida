# Guide de transcription (jalon M0)

Pour l'annotation du seed (200–500 lignes) dans **eScriptorium**. Objectif :
des transcriptions **cohérentes** entre annotateurs, conformes à la
[politique Unicode](unicode-policy.md).

## Principes

- Transcrire **ce qui est écrit**, ligne par ligne, dans l'ordre **RTL**.
- Une **ligne image** ↔ une **ligne texte** (pas de fusion de lignes).
- Conserver la graphie source (alif/hamza/tāʾ marbūṭa **non** normalisés).
- Diacritiques : suivre la décision de la politique Unicode (inclure/exclure) —
  et s'y tenir pour **tout** le seed.
- Ne pas « corriger » le texte : pas d'ajout de mots, pas d'orthographe moderne.

## Cas particuliers

| Cas | Règle |
|---|---|
| Mot coupé en fin de ligne | transcrire tel quel sur la ligne où il apparaît |
| Rature / surcharge | transcrire la version finale lisible ; noter en commentaire si ambigu |
| Illisible | marquer par un placeholder convenu (ex. `⟨?⟩`) et signaler |
| Enluminure / ornement | ignorer (pas de texte) |
| Titre / rubrique en couleur | transcrire comme texte normal |
| Note marginale | région séparée si le layout la distingue |

## Qualité

- Double-transcrire un **sous-ensemble** (~10 %) pour mesurer l'accord
  inter-annotateur (et affiner ce guide).
- Passer chaque transcription par `scripts/normalize.py` avant de l'enregistrer
  comme vérité terrain.
