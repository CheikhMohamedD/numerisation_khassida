# Numérisation des Khassida — OCR arabe & reconstruction de police

Numériser les **Khassida** (qaṣāʾid de Cheikh Ahmadou Bamba) : des PDF arabes
essentiellement **image/scan**, écrits dans une **calligraphie non normalisée**.
Objectif : produire du **texte Unicode fiable**, apprendre à reconnaître cette
typographie, puis **reconstruire une police** (TTF/OTF) qui accélère la
numérisation des documents suivants.

Le plan complet : [`docs/plan-numerisation-arabe.md`](docs/plan-numerisation-arabe.md).
Référence de l'outil d'entraînement (Soup CLI) : [`docs/soup-docs.md`](docs/soup-docs.md).

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
| `data/lines/` | A/B | Images de ligne découpées | — |
| `data/ground_truth/` | B | Transcriptions manuelles (seed 200–500 lignes) | — |
| `data/synthetic/` | B | Lignes rendues avec la police (boucle) | police → lignes étiquetées |
| `ocr/` | C | Entraînement OCR (Kraken/TrOCR **et** VLM Soup) | lignes → texte |
| `postcorrection/` | E | LLM arabe de correction (SFT/DPO/RLVR via Soup) | texte bruité → propre |
| `font/` | D | Reconstruction police (FontForge/HarfBuzz) | glyphes → TTF/OTF |
| `eval/` | — | Jeu de test figé, métriques (CER), rapports | — |
| `pipeline/` | F | Chaîne bout-en-bout PDF → texte/PDF cherchable | — |
| `scripts/` | — | Utilitaires transverses | — |

## Où en est-on — jalons

- [ ] **M0** Cadrage : politique Unicode + guide de transcription + jeu de test figé
- [ ] **M1** Prétraitement + segmentation ligne opérationnels
- [ ] **M2** Seed 200–500 lignes annotées (+ baseline CER)
- [ ] **M3** Police brouillon v0 (lettres + formes principales)
- [ ] **M4** OCR v1 (synthétique + seed) — CER de référence
- [ ] **M5** Boucle bootstrapping (2–3 tours) + active learning
- [ ] **M6** Post-correction LLM (SFT puis DPO/RLVR)
- [ ] **M7** Police v1 complète (ligatures, diacritiques)
- [ ] **M8** Pipeline bout-en-bout + PDF cherchable + service

## Démarrer (actions M0)

1. Déposer un échantillon de PDF dans `data/raw_pdfs/`.
2. Rasteriser : `python preprocessing/pdf_to_images.py` (400 DPI) → `data/images/`.
3. Figer la **politique Unicode** ([`docs/unicode-policy.md`](docs/unicode-policy.md))
   et le **guide de transcription** ([`docs/transcription-guide.md`](docs/transcription-guide.md)).
4. Choisir ~100 pages jamais vues pour `data/test_set/` (jeu figé).
5. Monter eScriptorium et annoter les **200 premières lignes** → `data/ground_truth/`.

## Environnement

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

> Note : Soup couvre **l'entraînement des modèles** (OCR-VLM, post-correction,
> éval, service). Le prétraitement image, la segmentation de ligne
> (Kraken/eScriptorium) et la **fabrication de police** (FontForge/HarfBuzz) sont
> des briques à intégrer **autour** de Soup — voir chaque sous-dossier.
