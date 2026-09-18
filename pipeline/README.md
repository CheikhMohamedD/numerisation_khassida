# Pipeline bout-en-bout (Phase F)

Chaîne finale, une fois les briques prêtes :

```
PDF ─► images (400 DPI) ─► prétraitement ─► layout + lignes (Kraken)
    ─► OCR (Kraken/TrOCR ; VLM Soup en secours) ─► post-correction LLM
    ─► texte + ALTO/hOCR ─► PDF cherchable (couche texte) / export
```

- Couche texte / PDF cherchable : `hocr-tools`, OCRmyPDF.
- Service / inférence locale : Soup `/docs/serving`, `/docs/export-to-gguf-ollama`,
  `/docs/mcp-server`.
- **Reproductibilité** : seeds (`/docs/seeds-and-reproducibility`), registre
  (`/docs/registry`) ; chaque itération = version taguée (datasets, modèles, police).

## La boucle de bootstrapping (le moteur)
1. Police courante → rendu synthétique (`data/synthetic/`).
2. Synthétique + seed → (ré)entraîner l'OCR.
3. OCR sur nouvelles pages → texte + nouveaux exemplaires de glyphes.
4. Lignes à faible confiance → correction humaine (active learning).
5. Nouveaux exemplaires → raffiner la police.
6. **eval-gate** : promouvoir seulement si le CER baisse.
