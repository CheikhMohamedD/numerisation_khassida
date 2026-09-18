# Journal de travail — M2 & M3

Exécution autonome des jalons **M2** (texte de référence + segmentation +
alignement) et **M3** (police brouillon v0). Tout est reproductible par scripts.

Environnement : `./.venv` (Python 3), Tesseract 5.5.3 (`ara`), Poppler,
OpenCV, fontTools, uharfbuzz. Voir `requirements.txt`.

---

## M2 — Données par corpus parallèle ✅ (pipeline fonctionnel, qualité brouillon)

### M2.1 Texte de référence (OCR du classique)
- **Script** : `ocr/ocr_classique.py` (Tesseract `ara`, psm 6) + `scripts/normalize.py`.
- **Constat** : la couche texte du PDF classique est cassée (mojibake, pas de
  ToUnicode) → OCR de l'image, qui est propre.
- **Sortie** : `data/reference_text/classique.txt` + `verses.jsonl`
  (**23 pages → 268 vers** arabes normalisés, diacritiques conservés).
- **Qualité** : brouillon (erreurs OCR type lettres fusionnées/manquantes) mais
  contenu fidèle ; sera raffiné dans la boucle. À corriger en priorité via
  active learning.
- **Commande** : `./.venv/bin/python ocr/ocr_classique.py`

### M2.2 Segmentation en lignes de la khassida
- **Script** : `segmentation/segment_lines.py` (profil de projection OpenCV).
- **Réglage** : `smooth=9, thresh_ratio=0.18, min_height=30` (calé pour éviter la
  fusion de 2 rangées dans la calligraphie épaisse). Ces valeurs sont les défauts.
- **Sortie** : `data/lines/khassida/page-XX/line-YYYY.png` + `manifest.jsonl`
  (**32 pages → 352 lignes**, ~11/page). Vérifié visuellement : 1 crop = 1 rangée.
- **Limite** : la projection reste heuristique ; pour la production, **Kraken**
  (baselines) fera mieux sur les lignes qui se chevauchent.
- **Commande** : `./.venv/bin/python segmentation/segment_lines.py`

### M2.3 Alignement vers ↔ lignes
- **Script** : `scripts/align.py`.
  - Défaut **proportionnel** (provisoire) car le texte de la khassida n'existe pas
    encore (c'est la cible OCR) → 352 paires, toutes `needs_review: true`.
  - Mode **Needleman-Wunsch** (`--khassida-ocr FILE`) : dès qu'un 1ᵉʳ OCR des
    lignes khassida existe, alignement global par similarité de texte.
- **Sortie** : `data/alignment/pairs.jsonl`
  (`{line_id, line_path, ref_verse_id, ref_text, method, needs_review}`).
- **Note** : 268 vers vs 352 lignes → mapping non 1:1 (granularité de mise en
  page différente). L'alignement fin nécessitera soit l'OCR khassida (M4), soit
  un calage manuel d'ancres. Le draft donne un point de départ.
- **Commande** : `./.venv/bin/python scripts/align.py`

---

## M3 — Police brouillon v0 ✅ (squelette de shaping validé ; contours placeholder)

### M3.1 Extraction d'exemplaires de glyphes
- **Script** : `font/extract_glyph_exemplars.py` (composantes connexes OpenCV).
- **Sortie** : `font/glyph_exemplars/paws/` + `marks/` + `manifest.jsonl`
  (**352 lignes → 7971 PAWs + 564 diacritiques**). Ce sont de vrais tracés de la
  calligraphie **à la graisse d'origine** — matière première pour la vectorisation.
- **Précision** : les composantes sont des **PAWs** (morceaux de mots), pas des
  lettres isolées (l'arabe est cursif). L'étiquetage par lettre viendra de
  l'alignement/OCR. `font/glyph_exemplars/{paws,marks}/` sont **gitignorés**
  (166 Mo, régénérables) ; seul le manifest est suivi.
- **Commande** : `./.venv/bin/python font/extract_glyph_exemplars.py`

### M3.2 Squelette de police (shaping arabe)
- **Script** : `font/build_font_scaffold.py` (fontTools + feaLib).
- **Sortie** : `font/build/khassida-scaffold-v0.ttf` (**155 glyphes**) + `features.fea`.
- **Contenu** : 28+ lettres arabes, leurs **formes contextuelles**
  (isol/init/medi/fina) et les features OpenType `isol/init/medi/fina`. Contours =
  **placeholders** (rectangles à ergots de jointure) à remplacer par les tracés
  vectorisés des exemplaires, **en conservant la graisse**.
- **Vérification HarfBuzz** (le shaping choisit la bonne forme selon le contexte) :
  - `بببب` → beh.init · medi · medi · fina ✅
  - `با` → beh.init · alef.fina ✅
  - `الله` → alef.isol · lam.init · lam.medi · heh.fina ✅
  - `دد` → dal.isol · dal.isol ✅ (dal ne se lie pas à gauche)
- **Intérêt** : valider **le pipeline de shaping** (le plus normatif) avant de
  dessiner les glyphes. `.ttf/.otf` gitignorés (régénérables).
- **Commande** : `./.venv/bin/python font/build_font_scaffold.py`

---

## M4 — OCR v1 & CER de référence ✅ (baseline établie ; boucle câblée)

### M4.1 Jeu de test figé + vérité terrain
- **Gold** : `data/test_set/gold.jsonl` — **10 lignes de la page 1** transcrites
  à la main en arabe vocalisé (isti'ādha + basmala + ṣalawāt), vérifiées via le
  crop calligraphique **et** le parallèle classique. À **étendre** ensuite à des
  pages plus variées.

### M4.2 Évaluation CER/WER
- **Script** : `eval/cer.py` (jiwer). Rapporte **CER brut** (diacritiques inclus)
  et **CER sans diacritiques** (rasm), + WER, par ligne et agrégé.
- **Correctif** : la plage de diacritiques englobait par erreur les lettres de
  base (0621–064A) ; corrigé et centralisé dans `scripts/normalize.py`
  (`strip_diacritics`, marques seules : 0610–061A, 064B–065F, 0670, 06D6–06ED).

### M4.3 OCR baseline (Tesseract `ara`) + CER de référence
- **Script** : `ocr/ocr_khassida_baseline.py` → `data/lines/khassida/ocr.jsonl`
  (352 lignes). Tesseract générique sur la calligraphie warsh = **hors
  distribution**, volontairement faible.
- **CER de référence (à battre)** : **79,2 % brut · 76,6 % rasm · WER 113,7 %**
  (rapport : `eval/reports/cer_ocr.json`). Certaines lignes vides (Tesseract
  abandonne) ; la ligne 7 tombe à 39 % (capte « وسلم … بارك »).

### M4.4 Boucle d'alignement fermée
- `scripts/align.py --khassida-ocr data/lines/khassida/ocr.jsonl` → mode
  **Needleman-Wunsch** : 268 paires, mais **0 confiante** (score max 0,47,
  moyenne 0,22).
- **Diagnostic honnête** : l'alignement est borné par la qualité des **deux**
  OCR (khassida bruité **et** référence classique bruitée). La boucle est prête ;
  il faut d'abord **nettoyer la référence** (le classique est de l'imprimé
  propre → gros gain facile) puis **entraîner un vrai OCR khassida**.

### Ce que M4 établit
- Une **cible chiffrée** : tout modèle entraîné doit passer **sous 76,6 % CER**.
- Un **harnais d'évaluation** reproductible (test figé + CER).
- La **boucle d'alignement** opérationnelle, prête à s'améliorer avec de
  meilleurs OCR.

### Non fait (assumé, nécessite compute/labels)
- Entraînement neuronal (Kraken/TrOCR ou VLM Soup) pour **battre** la baseline :
  nécessite des labels fiables (référence nettoyée + alignement confiant) et du
  GPU. C'est l'objet de M5.
- Génération synthétique : nécessite soit la police v0 **avec vrais tracés**,
  soit une police arabe tierce (Amiri) + rendu avec *shaping* (libraqm) —
  reporté pour éviter un rendu arabe incorrect.

---

## État des jalons

- [x] **M2** — texte de référence (268 vers), segmentation (352 lignes),
  alignement provisoire (352 paires). *Pipeline OK ; qualité à raffiner.*
- [~] **M3** — exemplaires (8535) + squelette de police v0 avec shaping validé.
  *Reste : vectoriser les exemplaires pour remplacer les placeholders.*
- [x] **M4** — jeu de test figé (10 lignes gold), harnais CER, **CER de
  référence 76,6 % (rasm)**, boucle d'alignement fermée (NW). *Reste (M5) :
  nettoyer la référence + entraîner un OCR pour battre la baseline.*

## Limites assumées (honnêteté)
- OCR classique = **brouillon** (à corriger, surtout aux endroits critiques).
- Segmentation = **heuristique** (Kraken recommandé pour la production).
- Alignement = **provisoire proportionnel** (le vrai alignement suit l'OCR khassida M4).
- Police v0 = **contours placeholder** (le shaping est réel ; les formes ne le sont pas encore).

## Prochaines actions (M4 et raffinements)
1. **Corriger** un échantillon du texte de référence (active learning) pour un
   seed propre.
2. **OCR khassida v1** (Kraken/TrOCR sur les paires, ou VLM Soup) → produit
   `data/lines/khassida/ocr.jsonl`.
3. Relancer `align.py --khassida-ocr …` → alignement Needleman-Wunsch réel.
4. **Vectoriser** les exemplaires (Potrace) et remplacer les placeholders de la
   police, lettre × forme, à la même graisse ; contrôler par overlay.
5. Boucle bootstrapping (police → synthétique → OCR → exemplaires → police).
