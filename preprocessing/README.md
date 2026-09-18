# Prétraitement image (Phase A)

Préparer les pages avant segmentation/OCR.

1. **Rasterisation** : `python preprocessing/pdf_to_images.py --dpi 400`
   (`data/raw_pdfs/*.pdf` → `data/images/<pdf>/page_XXXX.png`).
2. **Nettoyage** (à ajouter, OpenCV/scikit-image) : binarisation (Sauvola),
   deskew, débruitage, dewarp. Pipeline **reproductible** et versionné.

Sortie : pages propres → `segmentation/` (Kraken).

> Poppler requis pour la rasterisation : `brew install poppler`.
