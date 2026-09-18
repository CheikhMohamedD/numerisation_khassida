# Politique Unicode (à figer — jalon M0)

Cible de transcription : **lettres de base, normalisation NFC**. Le *shaping*
(formes contextuelles, ligatures) est du ressort de la **police**, jamais du
texte. On n'utilise **pas** les *presentation forms* (U+FB50–FEFF).

> Ce fichier est un **contrat** : toute annotation et toute sortie OCR doivent le
> respecter, sinon les métriques (CER) et l'entraînement deviennent incohérents.

## Décisions à trancher (cocher/compléter)

| Sujet | Décision | Notes |
|---|---|---|
| Normalisation | `NFC` | à appliquer systématiquement |
| Diacritiques (ḥarakāt) | ✅ **INCLURE** | confirmé : le classique et la khassida sont **entièrement vocalisés** |
| Alif variants | unifier ? (أ إ آ ا) | conserver la forme écrite, ne pas normaliser à `ا` |
| Hamza | positions (ء ئ ؤ إ أ) | conserver la graphie source |
| Tāʾ marbūṭa vs hāʾ | ة vs ه | conserver la graphie source |
| Chiffres | arabes-orientaux (٠١٢…) vs latins | choisir selon la source |
| Ponctuation | ، ؛ ؟ … | conserver l'unicode arabe |
| Kashida (ـ, U+0640) | ⬜ garder / ⬜ retirer | c'est un allongement **typographique** → plutôt retirer du texte |
| Signes coraniques / marques | liste à établir | spécifiques aux Khassida |

## Règles de normalisation appliquées (à implémenter dans `scripts/normalize.py`)

1. `unicodedata.normalize("NFC", texte)`
2. Retirer le kashida U+0640 (si décision = retirer).
3. Uniformiser espaces (une seule espace, pas de tab), trim par ligne.
4. **Ne pas** convertir en presentation forms.
5. (optionnel) Journaliser les caractères hors liste blanche pour revue.
