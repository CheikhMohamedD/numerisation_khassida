# Numérisation des Khassida — OCR arabe & reconstruction de police

Numériser les **Khassida** (qaṣāʾid de Cheikh Ahmadou Bamba) : des PDF arabes
essentiellement **image/scan**, écrits dans une **calligraphie non normalisée**.
Objectif : produire du **texte Unicode fiable**, apprendre à reconnaître cette
typographie, puis **reconstruire une police** (TTF/OTF) qui accélère la
numérisation des documents suivants.

Le plan complet : [`docs/plan-numerisation-arabe.md`](docs/plan-numerisation-arabe.md).
Référence de l'outil d'entraînement (Soup CLI) : [`docs/soup-docs.md`](docs/soup-docs.md).

> **Atout majeur — corpus parallèle.** On a **deux PDF du même Khassida** : une
> version **classique** (naskh imprimé vocalisé) et la version **calligraphique**
> à numériser. La classique fournit le **texte de référence** ; on l'aligne
> vers-à-vers sur la calligraphie → données d'entraînement **et** exemplaires de
> glyphes étiquetés, **sans transcription manuelle**. Détails :
> [`docs/parallel-corpus-strategy.md`](docs/parallel-corpus-strategy.md).

## Idée directrice : la boucle de bootstrapping

```
police (brouillon) ─► rendu synthétique étiqueté ─► entraînement OCR
        ▲                                                 │
        │                                                 ▼
   raffinage police ◄── exemplaires de glyphes ◄── OCR de nouvelles pages
```

Police et OCR se renforcent à chaque itération — c'est ce qui rend le projet
faisable sans corpus annoté ni police existante.

## Organisation du dépôt (alignée sur les phases du plan)

| Dossier | Phase | Rôle | Entrée → Sortie |
|---|---|---|---|
| `docs/` | — | Plan, doc Soup, guides (Unicode, transcription) | — |
| `data/raw_pdfs/` | A | PDF sources des Khassida | — |
| `data/images/` | A | Pages rasterisées 400 DPI | PDF → PNG |
| `preprocessing/` | A | Binarisation, deskew, débruitage, dewarp | images → images propres |
| `segmentation/` | A | Layout + lignes (Kraken/eScriptorium), ordre RTL | pages → lignes + ALTO |
| `data/lines/` | A/B | Images de ligne découpées (classique + khassida) | — |
| `data/reference_text/` | B | Texte de référence = **OCR du classique** (vocalisé) | classique → texte |
| `data/alignment/` | B | Paires (ligne khassida ↔ texte) par alignement vers-à-vers | → `pairs.jsonl` |
| `data/ground_truth/` | B | Vérifications/corrections manuelles (léger) | — |
| `data/synthetic/` | B | Lignes rendues avec la police (boucle) | police → lignes étiquetées |
| `ocr/` | C | Entraînement OCR (Kraken/TrOCR **et** VLM Soup) | lignes → texte |
| `postcorrection/` | E | LLM arabe de correction (SFT/DPO/RLVR via Soup) | texte bruité → propre |
| `font/` | D | Reconstruction police (FontForge/HarfBuzz) | glyphes → TTF/OTF |
| `eval/` | — | Jeu de test figé, métriques (CER), rapports | — |
| `pipeline/` | F | Chaîne bout-en-bout PDF → texte/PDF cherchable | — |
| `scripts/` | — | Utilitaires transverses | — |

## Où en est-on — jalons

- [x] **M0** Cadrage : PDF déposés + rasterisés (23+32 p.), politique Unicode (diacritiques inclus), stratégie corpus parallèle
- [ ] **M1** Prétraitement + segmentation ligne (classique & khassida)
- [ ] **M2** Texte de référence (OCR du classique) + **alignement** vers ↔ lignes → paires (remplace la transcription manuelle)
- [ ] **M3** Police brouillon v0 (lettres + formes principales)
- [ ] **M4** OCR v1 (synthétique + seed) — CER de référence
- [ ] **M5** Boucle bootstrapping (2–3 tours) + active learning
- [ ] **M6** Post-correction LLM (SFT puis DPO/RLVR)
- [ ] **M7** Police v1 complète (ligatures, diacritiques)
- [ ] **M8** Pipeline bout-en-bout + PDF cherchable + service

## Démarrer — prochaines actions (M1 → M2)

M0 fait : 2 PDF déposés et **rasterisés 400 DPI** (`data/images/classique` 23 p.,
`data/images/khassida` 32 p.), politique Unicode fixée (diacritiques inclus),
stratégie corpus parallèle documentée.

Suite :
1. **OCR du classique** (naskh imprimé propre) → `data/reference_text/`
   (Tesseract `ara` ou VLM), normaliser + découper en **vers**.
2. **Segmentation** Kraken de la khassida → `data/lines/khassida/` (ordre RTL).
3. **Alignement** vers ↔ lignes → `data/alignment/pairs.jsonl`
   (paires image de ligne ↔ texte, sans transcription manuelle).
4. Réserver quelques pages khassida **non alignées** pour `data/test_set/` (CER honnête).
5. Contrôle humain d'un échantillon d'alignement.

## Environnement

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

> Note : Soup couvre **l'entraînement des modèles** (OCR-VLM, post-correction,
> éval, service). Le prétraitement image, la segmentation de ligne
> (Kraken/eScriptorium) et la **fabrication de police** (FontForge/HarfBuzz) sont
> des briques à intégrer **autour** de Soup — voir chaque sous-dossier.
