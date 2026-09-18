# Segmentation (Phase A)

Layout + découpage en **lignes**, ordre de lecture **RTL**.

- Outil : **Kraken** (+ **eScriptorium** pour l'annotation assistée).
- Entrée : `data/images/**/*.png` (pages prétraitées).
- Sortie : `data/lines/` (une image par ligne) + ALTO/PAGE-XML (coordonnées).

Étapes :
1. Détection des baselines et régions (modèle de segmentation Kraken).
2. Extraction des lignes → `data/lines/<page>/line_XXXX.png`.
3. Vérifier l'ordre RTL et la couverture (pas de ligne manquante).

Les lignes découpées alimentent l'annotation (`data/ground_truth/`) et l'OCR.
