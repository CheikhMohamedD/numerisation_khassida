# Stratégie corpus parallèle (raffinement majeur du plan)

On dispose de **deux PDF du même Khassida** (*Wakāna ḥaqqan ʿalaynā…*) :

| Fichier | Contenu | Couche texte | Rôle |
|---|---|---|---|
| `Wakaana_haqan_haleyna_Arabe-classique.pdf` | Naskh imprimé, **vocalisé**, 23 p. | présente mais **encodage cassé** (mojibake, pas de ToUnicode) | **texte de référence** |
| `Wakaana_haqan_haleyna_arabe-khassida.pdf` | Calligraphie **warsh/maghribi épaisse**, 32 p. | quasi vide | **cible OCR + police** |

C'est un **corpus parallèle** : même texte, deux typographies, **même ordre de
vers**. Cela remplace en grande partie la transcription manuelle du seed (M2) et
accélère toute la boucle.

## Constat vérifié
- Page 1 des deux = même ouverture (isti'ādha + basmala + prière). Contenu aligné.
- Pagination différente (23 vs 32) car la calligraphie est plus grande → **aligner
  au niveau vers/hémistiche**, pas page.
- Le texte vocalisé du classique confirme : **diacritiques à INCLURE** dans la
  politique Unicode.
- La couche texte du classique est **inexploitable** (encodage custom) → le texte
  de référence s'obtient par **OCR du classique** (facile : imprimé propre).

## Pipeline de données (remplace/renforce la Phase B)

```
classique.pdf ─OCR arabe standard─► texte de référence (vocalisé)  → data/reference_text/
                                              │
khassida.pdf ─segmentation ligne─► lignes calligraphiques          → data/lines/khassida/
                                              │
                         ALIGNEMENT vers-à-vers (ordre monotone)    → data/alignment/
                                              │
                 ┌────────────────────────────┴───────────────────────────┐
                 ▼                                                          ▼
   paires (image_ligne_khassida, texte)                   exemplaires de glyphes étiquetés
        = données OCR SANS transcription manuelle              = matière pour la police
```

### 1. Texte de référence (`data/reference_text/`)
OCR du **classique** (naskh imprimé propre) avec un OCR arabe standard
(Tesseract `ara`, ou un VLM). Vérification humaine légère seulement. Sortie :
texte vocalisé, découpé en **vers/hémistiches**, normalisé (voir
[unicode-policy](unicode-policy.md)).

### 2. Segmentation de la khassida (`data/lines/khassida/`)
Kraken : lignes calligraphiques dans l'ordre RTL.

### 3. Alignement (`data/alignment/`)
Aligner la **séquence de vers** de référence avec la **séquence de lignes**
khassida (alignement monotone type Needleman-Wunsch/DTW sur l'ordre). Comme le
contenu et l'ordre sont identiques, l'alignement est surtout un **calage de
séquence** ; contrôle humain sur les zones ambiguës. Sortie : paires
`(image_ligne_khassida.png, texte_vers)`.

### 4. Double exploitation
- **OCR** : les paires alimentent l'entraînement (voie Kraken/TrOCR + VLM Soup)
  **sans transcription manuelle** — le seed devient quasi gratuit.
- **Police** : connaissant le texte de chaque ligne, on **localise chaque
  caractère × forme** dans la calligraphie → exemplaires étiquetés pour
  reconstituer chaque glyphe **fidèlement, à la même graisse** (voir Phase D).

## Impact sur la police (Phase D)
Puisqu'on connaît le texte, on sait **quel glyphe** correspond à chaque tracé.
On collecte, par lettre × forme (isolée/initiale/médiane/finale) et par ligature,
des exemplaires réels de la calligraphie épaisse → on vectorise en conservant la
**graisse** d'origine → fonte TTF/OTF fidèle. La cohérence de graisse se contrôle
en superposant le rendu de la police reconstruite sur les tracés d'origine.

## Conséquences sur les jalons
- **M2** n'est plus « transcrire 200–500 lignes à la main » mais « **OCR du
  classique + alignement** » (transcription manuelle réduite à la vérification).
- Le **jeu de test figé** reste nécessaire : réserver quelques pages de la
  khassida **non alignées** pour mesurer le CER honnêtement.

## Prochaines actions
1. OCR du classique → `data/reference_text/` (Tesseract `ara` ou VLM), puis
   normalisation + découpe en vers.
2. Segmentation Kraken de la khassida → `data/lines/khassida/`.
3. Script d'alignement séquence vers ↔ lignes → `data/alignment/pairs.jsonl`.
4. Contrôle humain d'un échantillon d'alignement (qualité).
