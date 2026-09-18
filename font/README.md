# Reconstruction de la police (Phase D)

Reconstruire la calligraphie des Khassida en fonte numérique **TTF/OTF** avec le
*shaping* arabe correct. Sert aussi à **générer des données synthétiques** (boucle).

## Sous-dossiers
- `glyph_exemplars/` — occurrences réelles par **lettre × forme** (isolée/initiale/
  médiane/finale) et ligatures, extraites des scans (aidé par l'OCR).
- `sources/` — sources éditables **versionnées** : `.sfd` (FontForge) ou `.ufo`.
- `build/` — binaires générés (`.ttf/.otf`), **gitignorés**.

## Étapes (cf. plan §6)
1. **Collecte** d'exemplaires (clustering visuel des glyphes).
2. **Vectorisation** raster→SVG (Potrace/autotrace) → nettoyage FontForge.
3. **Construction** : mapping **Unicode base** + tables OpenType de shaping :
   `init` `medi` `fina` `isol`, `liga`/`rlig`, `ccmp`, `mark`/`mkmk`, sens RTL.
4. **Vérification** du rendu avec HarfBuzz :
   ```bash
   hb-shape build/khassida.ttf "بسم الله الرحمن الرحيم"
   ```
   Contrôler que les formes contextuelles et ligatures se déclenchent.

## Outils
FontForge (scriptable Python), fontTools, uharfbuzz. (Optionnel : génération ML de
glyphes manquants — DeepVecFont/diffusion — à **valider manuellement**.)
