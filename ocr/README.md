# OCR (Phase C)

Lecture **ligne → texte arabe**. Deux voies complémentaires (cf. plan §5).

## Voie 1 — reconnaisseur de ligne spécialisé (à privilégier au départ)
CRNN+CTC (**Kraken**/**Calamari**) ou **TrOCR**. Frugal en données/VRAM, éprouvé
sur l'arabe historique. C'est le **moteur principal**.

## Voie 2 — VLM via Soup (robustesse & contexte)
Fine-tune d'un modèle vision-langage (Qwen2-VL, LLaMA-3.2-Vision) en QLoRA 4-bit.
Config prête : [`configs/soup-vision-ocr.yaml`](configs/soup-vision-ocr.yaml).

```bash
pip install "soup-cli[vision]"
soup train -c ocr/configs/soup-vision-ocr.yaml
```

## Données attendues
- Entraînement : `data/ground_truth/` (seed réel) + `data/synthetic/` (rendu police).
- Format VLM : JSONL LLaVA (`<image>` + transcription), voir la config.

## Sorties
- Modèle → `ocr/out/` (gitignoré) ; export GGUF/Ollama possible (doc Soup `/docs/export-to-gguf-ollama`).
- Prédictions → à évaluer dans `eval/` (CER sur jeu figé).
