# Post-correction linguistique (Phase E)

Corriger le texte OCR bruité avec un **LLM arabe**, via Soup.

- **SFT** sur paires `(texte OCR → texte propre)` (paires réelles + dégradations
  synthétiques de texte propre).
- **Restauration des diacritiques** en tâche séparée si la politique Unicode les inclut.
- **DPO / RLVR** avec **récompense vérifiable** (dictionnaire, morphologie, score
  de langue) pour préférer les corrections valides sans hallucination.

Doc Soup : `/docs/rlvr`, `/docs/reward-verifier`, `/docs/online-dpo`,
`/docs/trace-to-preference`, `/docs/data-augment`.

Sortie : modèle → `postcorrection/out/` (gitignoré). Gain mesuré en **CER après
correction** dans `eval/`.
