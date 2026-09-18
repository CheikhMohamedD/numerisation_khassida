# Plan d'entraînement IA — Numérisation de PDF arabes à police non normalisée

> Objectif : transformer des PDF arabes (essentiellement des pages **image/scan**)
> en **texte Unicode fiable**, apprendre à reconnaître une **police arabe non
> normalisée**, puis **reconstruire cette police** (TTF/OTF) pour accélérer la
> numérisation des documents suivants.
>
> Ce plan s'appuie sur **Soup CLI** (toolkit de post-training / fine-tuning,
> Apache-2.0, pensé pour petits GPU) pour tout le volet modèles. Voir la doc
> scrapée dans [`soup-docs.md`](soup-docs.md).

---

## 0. Décomposition du problème

Ton projet contient en réalité **trois sous-problèmes** couplés, qu'il faut
traiter dans une **boucle qui se renforce** (bootstrapping) :

1. **OCR / HTR** — lire l'image d'une page arabe → texte Unicode.
2. **Reconnaissance de la police** — identifier et regrouper les glyphes propres
   à cette typographie non standard (formes contextuelles, ligatures, diacritiques).
3. **Reconstruction de la police** — produire une fonte numérique (TTF/OTF) avec
   le *shaping* arabe correct, qui sert ensuite à **générer des données
   synthétiques** pour ré-entraîner l'OCR → cercle vertueux.

Le cœur stratégique du projet est cette **boucle** :

```
police (brouillon) ─► rendu de texte synthétique étiqueté ─► entraînement OCR
        ▲                                                          │
        │                                                          ▼
   raffinage police ◄── exemplaires de glyphes réels ◄── OCR de nouvelles pages
```

Chaque tour améliore les deux artefacts (OCR **et** police). C'est ce qui rend le
projet réaliste malgré l'absence de police normalisée et de données annotées.

---

## 1. Spécificités de l'arabe (contraintes de conception)

À intégrer dès le départ, car elles conditionnent chaque brique :

- **Écriture cursive** : chaque lettre a jusqu'à **4 formes contextuelles**
  (isolée / initiale / médiane / finale). L'OCR doit apprendre le texte, pas des
  glyphes isolés → travailler au **niveau ligne**, pas caractère.
- **Ligatures** obligatoires (lām-alif …) et calligraphiques → glyphes composites.
- **Diacritiques (ḥarakāt)** souvent optionnels : décider tôt si on les
  transcrit ou non (deux modèles/têtes possibles).
- **Sens RTL** + allongement *kashida* → segmentation de ligne et ordre de
  lecture spécifiques.
- **Normalisation Unicode** : cible en **lettres de base (NFC)**, pas en
  *presentation forms* (U+FExx) ; le *shaping* est du ressort de la police, pas du
  texte. Fixer une politique de normalisation (alif variants, tāʾ marbūṭa,
  hamza, chiffres arabes/hindi) **avant** d'annoter.

---

## 2. Stack & outils recommandés

| Besoin | Outil open-source | Rôle |
|---|---|---|
| PDF → images | `pdftoppm` / `pdf2image` (Poppler) | Rasteriser à 300–600 DPI |
| Prétraitement | OpenCV, `scikit-image`, ScanTailor | Binarisation, deskew, débruitage, dewarp |
| Analyse de mise en page + segmentation ligne | **Kraken** / eScriptorium | Baselines, régions, ordre RTL, HTR historique |
| Annotation ground-truth | **eScriptorium** ou Label Studio | Transcription ligne-à-ligne, RTL |
| OCR ligne (voie spécialisée) | **Kraken**, **Calamari**, **PaddleOCR**, **TrOCR** | CRNN+CTC ou transformer OCR |
| OCR / lecture (voie VLM) | **Soup** `modality: vision` (Qwen2-VL, LLaMA-3.2-Vision) | Lecture page/ligne robuste, QLoRA 4-bit |
| Post-correction linguistique | **Soup** SFT + DPO/RLVR (LLM arabe) | Corriger erreurs, restaurer diacritiques |
| Reconstruction de police | **FontForge** (scriptable Python), **fontTools**, Potrace/autotrace | Vectorisation, mapping Unicode, features OpenType |
| Vérification du shaping | **HarfBuzz** (`hb-shape`), `uharfbuzz` | Contrôler init/medi/fina/isol, `liga`, `mark` |
| Évaluation | `jiwer` (CER/WER), Soup **eval-gate** | Métriques + garde anti-régression |
| Livraison | `hocr-tools`/OCRmyPDF (couche texte), Soup **serving** | PDF cherchable, API |

---

## 3. Phase A — Données & prétraitement (fondations)

**A1. Numériser & rasteriser.** `pdftoppm -r 400 doc.pdf page` → PNG. Garder le
DPI constant. Inventorier : nb de pages, homogénéité de la police, présence de
diacritiques, complexité de mise en page (colonnes, notes, tableaux).

**A2. Nettoyage image.** Binarisation (Sauvola/adaptive), deskew, débruitage,
dewarp. Pipeline reproductible (script versionné).

**A3. Analyse de mise en page.** Kraken/eScriptorium : détection des **baselines**
et régions, **segmentation en lignes**, ordre de lecture **RTL**. Sortie : une
image par ligne + coordonnées (ALTO/PAGE-XML).

**A4. Politique de texte.** Figer la normalisation Unicode cible (cf. §1) et un
**guide de transcription** (ce qu'on inclut/ignore : diacritiques, ponctuation,
chiffres). C'est le contrat qui garantit la cohérence des annotations.

---

## 4. Phase B — Amorçage des données (le vrai goulot d'étranglement)

Sans police normalisée ni corpus annoté, on crée les données par **deux sources
complémentaires** :

**B1. Seed manuel (vérité terrain).** Transcrire à la main **200–500 lignes**
représentatives dans eScriptorium (RTL, ligne-à-ligne). C'est peu, mais suffisant
pour amorcer un premier OCR et surtout pour **évaluer**.

**B2. Données synthétiques (le multiplicateur).** Dès qu'on a un **brouillon de
police** (Phase D, même imparfait), rendre de grands corpus de texte arabe
(Wikipédia ar, corpus classiques du domaine visé) avec cette police, en variant
taille, interligne, fond, bruit, légères distorsions → **milliers de lignes
étiquetées gratuitement**. C'est ici que police et OCR se renforcent.

> Dans Soup : formats et outils de données → [`/docs/data-formats`],
> [`/docs/data-tools`], augmentation → [`/docs/data-augment`],
> [`/docs/data-forge`], mélange/curriculum → [`/docs/data-mix`],
> ingénierie → [`/docs/data-engineering-pro`]. `soup data inspect` donne des
> statistiques image pour les datasets vision.

**B3. Active learning.** À chaque itération, faire tourner l'OCR courant sur des
pages non vues, remonter les lignes à **faible confiance / fort désaccord**, les
faire corriger en priorité → l'annotation humaine se concentre là où elle paie.

---

## 5. Phase C — Modèle OCR (deux voies, complémentaires)

### Voie 1 — Reconnaisseur de ligne spécialisé (à privilégier au départ)
CRNN+CTC (**Kraken**/**Calamari**) ou **TrOCR** fine-tuné sur les lignes de la
Phase B. Avantages : **frugal en données et en VRAM**, éprouvé sur l'arabe et les
documents historiques, s'intègre à eScriptorium. C'est le **moteur OCR principal**.

### Voie 2 — VLM via Soup (robustesse & contexte)
Fine-tuner un **modèle vision-langage** (Qwen2-VL, LLaMA-3.2-Vision) avec Soup pour
lire une ligne/page → texte arabe. Le modèle exploite des **priors linguistiques
arabes** (utile pour les diacritiques, les ligatures ambiguës, les pages
dégradées). QLoRA 4-bit → accessible sur petit GPU.

Config Soup (format LLaVA, un exemple = une image de ligne + transcription) :

```yaml
base: Qwen/Qwen2-VL-7B-Instruct
task: sft
modality: vision
data:
  train: ./data/ocr_lines.jsonl     # format llava, <image> + texte cible
  format: llava
  image_dir: ./data/lines
  val_split: 0.1
training:
  epochs: 3
  lr: 1e-5
  quantization: 4bit
  lora: { r: 64, alpha: 16 }
```

```json
{"image": "line_00042.png", "conversations": [
  {"from": "human", "value": "<image>\nTranscris fidèlement le texte arabe."},
  {"from": "gpt", "value": "نص عربي مكتوب بخط غير معياري"}]}
```

> Soup vision : [`/docs/multimodal`], [`/docs/modality-ii`]. Qualité LoRA →
> [`/docs/lora-quality`] ; quantization → [`/docs/quant-menu`] ; petit GPU →
> [`/docs/free-gpu-tier`], [`/docs/training-speed-memory`], [`/docs/multi-gpu`].

**Recommandation** : Voie 1 comme moteur (rapide à itérer), Voie 2 comme
**secours sur pages difficiles** + base de la post-correction. On peut ensuite
**distiller** le VLM vers un modèle plus léger.

---

## 6. Phase D — Reconstruction de la police (font engineering)

C'est le volet le plus normatif (règles OpenType/HarfBuzz), en partie manuel.

**D1. Collecte d'exemplaires.** À partir des scans nettoyés et de la segmentation,
regrouper (clustering visuel) les occurrences de chaque **lettre × forme
contextuelle** et des ligatures. L'OCR aide à étiqueter automatiquement ces
exemplaires (d'où la boucle).

**D2. Vectorisation.** Débruiter → raster→SVG (Potrace/autotrace) → nettoyage des
contours dans **FontForge** (scriptable en Python via `fontforge`/`fontTools`).
Un glyphe = moyenne/consolidation de plusieurs exemplaires.

**D3. Construction de la fonte.** Mapping **Unicode base** + tables **OpenType de
shaping arabe** :
- `init` / `medi` / `fina` / `isol` (formes contextuelles),
- `liga` / `rlig` (ligatures), `ccmp` (décomposition/recomposition),
- `mark` / `mkmk` (positionnement des diacritiques), sens **RTL**.
Vérifier le rendu réel avec **HarfBuzz** (`hb-shape`, `uharfbuzz`) sur des chaînes
test couvrant toutes les jointures.

**D4. (Optionnel) ML pour glyphes manquants.** Pour compléter des glyphes rares,
des approches type **DeepVecFont / diffusion de glyphes** peuvent proposer des
contours, à valider manuellement. À garder en option — ne pas bloquer le projet
dessus.

**Livrable** : une **fonte TTF/OTF** qui (a) rend correctement l'arabe et (b)
sert de générateur de données synthétiques (retour en Phase B).

---

## 7. Phase E — Post-correction linguistique (LLM arabe, via Soup)

L'OCR produit du texte bruité. Un **LLM arabe** le corrige :
- **SFT** sur paires `(texte OCR bruité → texte propre)` — les paires sont
  générées gratuitement en dégradant du texte propre, ou via les erreurs réelles
  de l'OCR.
- **Restauration des diacritiques** comme tâche séparée si besoin.
- **DPO / RLVR** avec une **récompense vérifiable** (correspondance dictionnaire,
  cohérence morphologique, score de langue) pour préférer les corrections
  valides sans hallucination.

> Soup : [`/docs/rlvr`] (récompenses vérifiables), [`/docs/reward-verifier`],
> [`/docs/online-dpo`], [`/docs/trace-to-preference`], [`/docs/data-augment`].

---

## 8. Phase F — La boucle de bootstrapping (le moteur du projet)

Itération type (à répéter jusqu'à convergence du CER) :

1. Police courante → **rendu synthétique** massif (Phase B2).
2. Synthétique **+ seed réel** → (ré)entraîner l'OCR (Phase C).
3. OCR sur de **nouvelles pages** → texte + nouveaux **exemplaires de glyphes**.
4. Lignes à faible confiance → **correction humaine** (active learning, B3).
5. Nouveaux exemplaires → **raffiner la police** (Phase D).
6. **Eval-gate** : ne promouvoir la nouvelle itération que si le CER s'améliore
   sur un jeu de test **figé**.

> Garde anti-régression et conception d'évals dans Soup :
> [`/docs/eval-design`], [`/docs/eval-gate`], [`/docs/eval-depth`],
> diagnostic → [`/docs/fine-tune-doctor`], [`/docs/diagnose`], [`/docs/advise`].
> Reproductibilité → [`/docs/seeds-and-reproducibility`], registre →
> [`/docs/registry`].

---

## 9. Évaluation

- **OCR** : **CER** (character error rate) principal, WER secondaire, **CER
  sensible aux diacritiques** en variante. Matrice de confusion par glyphe pour
  cibler les faiblesses de la police.
- **Police** : correction du *shaping* (tests HarfBuzz), **overlay
  rendu-vs-original** (IoU des contours), couverture des formes contextuelles.
- **Bout-en-bout** : % de pages « propres » après post-correction ; temps par
  page ; taux d'intervention humaine (doit **baisser** à chaque itération).
- **Jeu de test figé** dès le départ (pages jamais vues à l'entraînement).

---

## 10. Livraison / industrialisation

Pipeline final :

```
PDF ─► images (400 DPI) ─► prétraitement ─► layout+lignes (Kraken)
    ─► OCR (Kraken/TrOCR ; VLM en secours) ─► post-correction LLM
    ─► texte + ALTO/hOCR ─► PDF cherchable (couche texte) / export
```

- **Export & service** : [`/docs/export`], [`/docs/export-to-gguf-ollama`]
  (inférence locale via Ollama), serveur [`/docs/serving`], intégration
  [`/docs/mcp-server`].
- **Reproductibilité & versionnage** des datasets, modèles et de la police
  (chaque itération = version taguée).

---

## 11. Matériel

Soup est conçu pour **petits GPU** (whisper-tiny/base et QLoRA 4-bit tournent sur
4 Go). Réaliste :
- **Démarrage** : 1 GPU 8–16 Go (QLoRA VLM 4-bit, reconnaisseur de ligne).
- **Montée en charge** : multi-GPU ([`/docs/multi-gpu`],
  [`/docs/multi-gpu-deepspeed`]) ou GPU loués ([`/docs/borrowed-hardware`],
  [`/docs/free-gpu-tier`]).
- La **vectorisation de police** et le prétraitement tournent sur CPU.

---

## 12. Feuille de route (jalons)

| Jalon | Contenu | Sortie vérifiable |
|---|---|---|
| **M0** | Cadrage : politique Unicode, guide de transcription, jeu de test figé | Doc de spec + 100 pages test |
| **M1** | Prétraitement + segmentation ligne opérationnels | Lignes propres RTL, ALTO |
| **M2** | Seed 200–500 lignes annotées | Ground-truth + baseline CER |
| **M3** | Police brouillon v0 (lettres + formes principales) | TTF v0 + shaping HarfBuzz OK |
| **M4** | OCR v1 (synthétique + seed) | CER mesuré sur test figé |
| **M5** | Boucle bootstrapping (2–3 tours) + active learning | CER en baisse, moins d'humain |
| **M6** | Post-correction LLM (SFT, puis DPO/RLVR) | Gain CER après correction |
| **M7** | Police v1 complète (ligatures, diacritiques) | Round-trip rendu≈original |
| **M8** | Pipeline bout-en-bout + PDF cherchable + service | Débit pages/h, doc reproductible |

---

## 13. Risques & parades

- **Zéro donnée au départ** → synthétique par la police + active learning ;
  n'attendre ni gros corpus ni annotation massive.
- **Police non normalisée** → travailler **ligne** (pas glyphe) pour l'OCR ; la
  police se reconstruit **progressivement** via la boucle.
- **Shaping arabe correct** = expertise OpenType/HarfBuzz → prévoir du temps
  dédié Phase D ; tester tôt et souvent avec `hb-shape`.
- **Diacritiques** → décider tôt (inclure/exclure) ; éventuellement une **tête
  séparée** de restauration.
- **Régressions entre itérations** → **eval-gate** systématique sur test figé.
- **Sur-ingénierie ML de la police** → garder D4 (génération ML de glyphes) en
  option, ne pas en dépendre.

---

## 14. Où Soup intervient précisément (récapitulatif)

| Étape du projet | Pages Soup (dans `soup-docs.md`) |
|---|---|
| Démarrage & config | `/docs/getting-started`, `/docs/configuration`, `/docs/advise` |
| Données (formats, augmentation, mélange) | `/docs/data-formats`, `/docs/data-tools`, `/docs/data-augment`, `/docs/data-forge`, `/docs/data-mix`, `/docs/data-engineering-pro` |
| OCR vision (VLM) | `/docs/multimodal`, `/docs/modality-ii` |
| Qualité / frugalité | `/docs/lora-quality`, `/docs/quant-menu`, `/docs/training-speed-memory`, `/docs/multi-gpu`, `/docs/free-gpu-tier` |
| Post-correction (préférence/récompense) | `/docs/rlvr`, `/docs/reward-verifier`, `/docs/online-dpo`, `/docs/trace-to-preference` |
| Évaluation & garde | `/docs/eval-design`, `/docs/eval-gate`, `/docs/eval-depth`, `/docs/fine-tune-doctor`, `/docs/diagnose` |
| Repro & registre | `/docs/seeds-and-reproducibility`, `/docs/registry` |
| Export & service | `/docs/export`, `/docs/export-to-gguf-ollama`, `/docs/serving`, `/docs/mcp-server` |

> Note d'honnêteté : Soup couvre **l'entraînement des modèles** (OCR-VLM,
> post-correction LLM, évaluation, service). Le **prétraitement image**, la
> **segmentation de ligne** (Kraken/eScriptorium) et la **fabrication de la
> police** (FontForge/HarfBuzz) sont des briques **hors Soup** à intégrer autour.

---

## 15. Prochaine action concrète

1. Convertir un échantillon de PDF en images 400 DPI et **mesurer** la difficulté
   (homogénéité police, diacritiques, mise en page).
2. Figer la **politique Unicode** + **guide de transcription** + **jeu de test**.
3. Monter eScriptorium et annoter les **premières 200 lignes** (seed + baseline).
4. En parallèle, tracer les **lettres de base** de la police dans FontForge → TTF v0.
5. Premier tour de boucle : synthétique v0 → OCR v1 → CER de référence.
