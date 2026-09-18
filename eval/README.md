# Évaluation

## Jeu de test **figé** (à créer en M0)
~100 pages **jamais vues** à l'entraînement → `data/test_set/`. Ne jamais y
puiser pour entraîner. C'est la référence unique pour comparer les itérations.

## Métriques
- **CER** (character error rate) — principal ; **WER** secondaire (`jiwer`).
- **CER sensible aux diacritiques** — variante si la politique les inclut.
- **Matrice de confusion par glyphe** — cible les faiblesses de la police.
- **Police** : correction du shaping (HarfBuzz), overlay rendu-vs-original.
- **Bout-en-bout** : % pages propres après post-correction, temps/page, **taux
  d'intervention humaine** (doit baisser à chaque tour).

## Garde anti-régression
Utiliser **eval-gate** de Soup (`/docs/eval-gate`, `/docs/eval-design`) : ne
promouvoir une nouvelle itération que si le CER s'améliore sur le jeu figé.

Rapports générés → `eval/reports/` (gitignoré).
