# Soup CLI — Documentation

> Scraped from <https://trysoup.dev/docs> on 2026-09-16. 114 pages, in sidebar order.

## Table of Contents

1. [Getting Started](#001-getting-started)
2. [Configuration](#002-configuration)
3. [Training Intelligence](#003-training-intelligence)
4. [soup advise— decide before you train](#004-advise)
5. [Pre-flight & Tooling (v0.64.0)](#005-preflight-tooling)
6. [Fine-tune Doctor (v0.71.27)](#006-fine-tune-doctor)
7. [Eval-Gated Training](#007-eval-gate)
8. [soup eval design— derive evals from your training data](#008-eval-design)
9. [Eval Depth (v0.65.0)](#009-eval-depth)
10. [Quant-Lobotomy Checker](#010-quant-check)
11. [soup diagnose— seven failure-mode probes, one verdict](#011-diagnose)
12. [Post-train X-rays (v0.66.0)](#012-post-train-xrays)
13. [Tracker & Eval Pro (v0.43.0)](#013-tracker-eval-pro)
14. [Training Methods](#014-training)
15. [Backends & Performance](#015-backends)
16. [Vision & Audio Fine-Tuning](#016-multimodal)
17. [Autopilot](#017-autopilot)
18. [Apple Silicon MLX Backend](#018-mlx-backend)
19. [Tool-Calling Fine-Tuning](#019-tool-calling)
20. [RLVR — Reinforcement Learning from Verifiable Rewards](#020-rlvr)
21. [Multi-GPU Mastery](#021-multi-gpu)
22. [Training Speed & Memory](#022-training-speed-memory)
23. [Training Stability & Auto-Tuning (v0.32.0)](#023-training-stability)
24. [Seeds and reproducibility](#024-seeds-and-reproducibility)
25. [Multi-Trainer Speed & Memory (v0.35.0)](#025-multi-trainer-speed-memory)
26. [Multipack — FFD Bin-Packing Sampler (v0.37.0)](#026-multipack)
27. [LoRA Quality — PiSSA, ReLoRA, Per-Pattern Rank, Surgical Patches (v0.39.0)](#027-lora-quality)
28. [Preference Variety (v0.40.0)](#028-preference-variety)
29. [Optimizer Zoo (v0.41.0)](#029-optimizer-zoo)
30. [Long Context (v0.49.0)](#030-long-context)
31. [GRPO Plus (v0.50.0)](#031-grpo-plus)
32. [Modality II (v0.52.0)](#032-modality-ii)
33. [Agent Forge & Deploy Autopilot (v0.46.0)](#033-agent-forge)
34. [Unlearning & Knowledge Edit (v0.61.0)](#034-unlearning)
35. [Retrieval-Augmented FT & Activation Steering (v0.62.0)](#035-rag-and-steering)
36. [Anti-trend Insurance (v0.68.0)](#036-anti-trend-insurance)
37. [Loop Hardening (v0.70.0 → live in v0.71.11)](#037-loop-hardening)
38. [Closed-loop reward-hacking auto-mitigation (v0.71.26)](#038-reward-hack-mitigation)
39. [Lean install + live wiring (v0.71.0 → v0.71.41)](#039-lean-install-live-wiring)
40. [Spectrum targeted training (v0.71.23)](#040-spectrum-targeted-training)
41. [LISA (v0.71.34)](#041-lisa)
42. [soup shrink: make a model smaller (v0.71.29)](#042-soup-shrink)
43. [PRM-guided GRPO (v0.71.30)](#043-prm-guided-grpo)
44. [Online DPO (v0.71.31)](#044-online-dpo)
45. [ASR fine-tuning (v0.71.32)](#045-asr-fine-tuning)
46. [Reward Forge: synthesize a reward verifier, then prove it cannot be gamed (v0.71.40 → v0.71.41)](#046-reward-verifier)
47. [Layer streaming: fine-tune a model that does not fit in your card (BETA, v0.72.0; NF4 v0.72.2; breadth v0.72.3; preference losses v0.72.4; external validation and the NF4 gradient repair v0.73.0)](#047-layer-streaming)
48. [Scaling a streaming run (v0.72.3)](#048-streaming-scaling)
49. [Preference losses over layer streaming (v0.72.4)](#049-streaming-preference)
50. [The layer streaming paper](#050-paper)
51. [Validation on hardware we do not own](#051-external-validation)
52. [Data Formats](#052-data-formats)
53. [Data Tools](#053-data-tools)
54. [Data Augmentation](#054-data-augment)
55. [Trace-to-Preference](#055-trace-to-preference)
56. [Data Pipeline Pro (v0.42.0)](#056-data-pipeline-pro)
57. [Data Forge & Quality Moat (v0.47.0)](#057-data-forge)
58. [Data Mixing Optimizer & Dynamic Curriculum (v0.48.0 — BETA)](#058-data-mix)
59. [Trace Ecosystem (v0.63.0)](#059-trace-ecosystem)
60. [Data Engineering Pro (v0.69.0)](#060-data-engineering-pro)
61. [Data Moat II (v0.71.36)](#061-data-moat-ii)
62. [Best-of-N & Evol-Instruct (v0.71.31)](#062-best-of-n-evolve)
63. [soup ship: the SHIP / DON'T-SHIP verdict (v0.71.25)](#063-soup-ship)
64. [Inference Server](#064-serving)
65. [Model Export](#065-export)
66. [Model Registry](#066-registry)
67. [HuggingFace Hub Deep Integration](#067-hf-hub-integration)
68. [Smart Inference Server (v0.30.0)](#068-speculative-decoding)
69. [soup draft (v0.71.33)](#069-soup-draft)
70. [Quant Menu — 9 Quantization Formats (v0.38.0)](#070-quant-menu)
71. [Quant Menu II (v0.53.0)](#071-quant-menu-ii)
72. [Model Catalog Expansion (v0.51.0)](#072-model-catalog-v051)
73. [Experiment Tracking](#073-experiments)
74. [Web UI](#074-web-ui)
75. [Soup Cans](#075-soup-cans)
76. [Soup Cans v2 + Live LR Finder (v0.33.0)](#076-soup-cans-v2)
77. [Observability & Dev UX (v0.34.0)](#077-observability)
78. [Live Dashboard & UX (v0.44.0)](#078-live-dashboard-ux)
79. [Plugin System (v0.45.0)](#079-plugins)
80. [soup adapters— git for LoRA](#080-adapters)
81. [soup loop— the production data flywheel, all from the CLI](#081-soup-loop)
82. [Adapter Lifecycle Finish (v0.67.0)](#082-adapter-lifecycle)
83. [Adapter algebra (v0.71.34)](#083-adapter-arithmetic)
84. [MCP server:soup mcp serve(v0.71.28)](#084-mcp-server)
85. [Correctness First (v0.36.0)](#085-correctness-first)
86. [Governance & Provenance (v0.59.0)](#086-governance)
87. [Supply Chain Security (v0.60.0)](#087-supply-chain-security)
88. [Compliance pack (v0.71.35)](#088-compliance-pack)
89. [Recipes](#089-recipes)
90. [Massive Recipe Expansion (v0.31.0)](#090-recipe-expansion)
91. [Migration](#091-migration)
92. [Fine-tune Llama 3.1 with LoRA using Soup CLI](#092-fine-tune-llama-3-1-lora)
93. [Fine-tune Qwen 3 on a custom dataset](#093-fine-tune-qwen-3)
94. [Fine-tune Gemma 3 with QLoRA (single GPU)](#094-fine-tune-gemma-3-qlora)
95. [Export fine-tuned models to GGUF and deploy on Ollama](#095-export-to-gguf-ollama)
96. [DPO training guide: align LLMs with human preferences](#096-dpo-training-guide)
97. [Migrate from LLaMA-Factory to Soup CLI](#097-migrate-from-llamafactory)
98. [Migrate from Axolotl to Soup CLI](#098-migrate-from-axolotl)
99. [Multi-GPU training with DeepSpeed ZeRO-3](#099-multi-gpu-deepspeed)
100. [CLI Reference](#100-cli-reference)
101. [FAQ](#101-faq)
102. [What's new across v0.71 to v0.75](#102-whats-new)
103. [v0.75.0: MLX honours its config, and unknown keys refuse the load](#103-mlx-honours-its-config)
104. [v0.74.0: the base was loaded in fp32 the whole time](#104-loaded-in-fp32)
105. [v0.73.3: four flags that did nothing](#105-flags-that-did-nothing)
106. [v0.73.2: the release gate](#106-ship-gate-repairs)
107. [v0.73.1: the free GPU tier](#107-free-gpu-tier)
108. [v0.73.0 "Borrowed Hardware"](#108-borrowed-hardware)
109. [v0.53.1 — Live writers for Quant Menu II](#109-v053-live-writers)
110. [v0.53.2 — Live trainers for Modality II](#110-v0532-modality-live)
111. [v0.53.6 / v0.53.7 — Plugins live, Anthropic API, tool endpoints](#111-v0536-7-plugins-anthropic)
112. [v0.53.8 / v0.53.10 — Remote loaders, alternative hubs, tracker extras](#112-v0538-10-remote-hubs)
113. [v0.53.9 — Live dashboard, Web UI mobile, bench percentiles, tokenizer trainer](#113-v0539-live-ux)
114. [v0.53.11 — GRPO variants live, PRM live, LongLoRA live, weighted preference](#114-v05311-grpo-prm-longlora)

---

<a id="001-getting-started"></a>

# 1. Getting Started

*Source: <https://trysoup.dev/docs/getting-started>*

## Installation

As of **v0.71.0** the install is split. `pip install soup-cli` is a light, **PyTorch-free** CLI + data-tools install — `soup init`, `soup data …`, and the inspection commands all work on it. To fine-tune, add the `[train]` extra:

```bash
# Light core: CLI + config + data tools, no PyTorch
pip install soup-cli

# Add the training stack (torch, transformers, peft, trl, datasets, …)
pip install "soup-cli[train]"

# Everything (train + serve + ui + data + mcp) in one shot
pip install "soup-cli[all]"

# Or from GitHub (latest dev)
pip install git+https://github.com/MakazhanAlpamys/Soup.git
```

> **Upgrading from ≤ v0.70?** `pip install soup-cli` no longer pulls PyTorch. If you train, reinstall with `pip install "soup-cli[train]"` — a missing heavy dependency now surfaces a friendly \*"Training needs the [train] extra"\* message instead of an `ImportError`.

### Requirements

**Default: resident QLoRA**

> **On Debian 12, Ubuntu 23.04 or anything newer, plain `pip install` fails outside a virtualenv**, and it is not a Soup problem:

>

> ```text
>
> error: externally-managed-environment
>
> ```

>

> Those distributions ship an `EXTERNALLY-MANAGED` marker in the system Python, so pip refuses to write into a `site-packages` that `apt` also manages ([PEP 668](https://peps.python.org/pep-0668/)). It is the default on current Debian and Ubuntu, so it is the ordinary first-run experience there rather than an edge case, and nothing in Soup can rescue it: the package is not installed yet when the command runs.

>

> Soup declares a `soup` console script, which makes it an application rather than a library, so **upstream's README now leads with `pipx`**:

>

> ```bash
>
> pipx install soup-cli # or: uv tool install soup-cli
>
> pipx install "soup-cli[train]" # extras spelled exactly as below
>
> ```

>

> Both give Soup its own virtualenv and put the command on `PATH`, which is outside PEP 668's scope entirely. Every `pip` line on this page stays correct **inside** a virtualenv, a Colab notebook or a Docker image, and `python3 -m venv .venv` then plain `pip` works just as well. Use `pip` rather than `pipx` if you also want to `import soup_cli` from your own code, because pipx isolation is the wrong shape for that.

- **Python 3.10 to 3.12** (the floor was raised from 3.9 in v0.71.0; v0.73.0 added the upper bound, because on 3.13 and above pip resolved untested PyTorch wheels that crash inside the native extension before Soup runs)
- **The `[train]` stack, as of v0.75.0**: `torch>=2.6.0`, `transformers>=5.16.1,<6.0.0`, `trl>=0.29.0,<1.0.0`, `peft>=0.20.0,<1.0.0`, `accelerate>=0.27.0`. A fresh install resolves all of that for you. One consequence worth knowing: `pip install "soup-cli[train,mlx]"` resolves for the first time in v0.74.0, because the two extras previously declared `transformers` ranges that could not be satisfied together at all
- CUDA-compatible GPU (recommended); Apple Silicon (MPS) or CPU (experimental) also work
- 8 GB+ VRAM for 7B models with QLoRA

> **The torch floor moved to 2.6.0 in v0.75.0, and that closed a real trap.** v0.74.0 declared `torch>=2.5.0` while `trl>=0.29` could not import at 2.5.1 at all, because it needs the public FSDP2 API that arrives in 2.6.0, so a pinned 2.5.x environment silently lost DPO, KTO, GRPO and BCO. pip could not catch it, since `trl` declares no torch dependency. v0.74.0 published the hole rather than guessing at a fix, because 2.5.1 was measured to fail and 2.6 had not been measured to work; v0.75.0 raised the floor **and proved it in CI**. If you pin torch yourself, pin 2.6.0 or newer.

**If the model does not fit: layer streaming (opt-in, BETA)**

- Set `training.stream_layers: true` in `soup.yaml` and the frozen base never loads into VRAM: Llama-3.1-8B fine-tunes in **3.32 GB on a 4 GB card**. Slower than resident training, so leave it off for a model that already fits. See [Layer Streaming](/docs/layer-streaming).

Streaming bounds the decoder stack to one layer at a time. Embeddings and the logits tensor stay resident, so peak VRAM still depends on the model, just much less.

### Optional Extras

```bash
pip install "soup-cli[train]"      # Training stack: torch, transformers, peft, trl, …
pip install "soup-cli[fast]"       # Unsloth 2-5x training speedup
pip install "soup-cli[mlx]"        # Apple Silicon backend (M1–M4)
pip install "soup-cli[serve]"      # FastAPI inference server
pip install "soup-cli[serve-fast]" # vLLM backend
pip install "soup-cli[sglang]"     # SGLang backend
pip install "soup-cli[eval]"       # lm-evaluation-harness
pip install "soup-cli[data]"       # MinHash dedup + semantic split (scikit-learn)
pip install "soup-cli[data-pro]"   # langdetect + Presidio PII
pip install "soup-cli[vision]"     # Pillow for vision fine-tuning
pip install "soup-cli[audio]"      # librosa + soundfile
pip install "soup-cli[qat]"        # Quantization-aware training
pip install "soup-cli[liger]"      # Liger Kernel fused ops
pip install "soup-cli[onnx]"       # ONNX export
pip install "soup-cli[tensorrt]"   # TensorRT-LLM export
pip install "soup-cli[awq]"        # AWQ quantized export
pip install "soup-cli[gptq]"       # GPTQ quantized export (a separate extra)
pip install "soup-cli[ui]"         # Web UI dashboard
pip install "soup-cli[tui]"        # Full-screen Textual dashboard
pip install "soup-cli[trackers]"   # MLflow / SwanLab / Trackio logging
pip install "soup-cli[wandb]"      # Weights & Biases, for soup train --wandb
pip install "soup-cli[generate]"   # httpx, for soup data generate provider calls
pip install "soup-cli[deepspeed]"  # ZeRO distributed training
pip install "soup-cli[ring-attn]"  # Ring FlashAttention
pip install "soup-cli[remote]"     # Remote datasets (s3 / gs / az / oci)
pip install "soup-cli[sign]"       # ed25519 adapter / attestation signing
pip install "soup-cli[compile]"    # DSPy / GEPA / TextGrad prompt compiler
pip install "soup-cli[carbon]"     # codecarbon energy / CO2 tracking
pip install "soup-cli[modal]"      # Serverless cloud GPU (soup train --cloud modal; --cloud lambda needs no extra)
pip install "soup-cli[aider]"      # Aider CLI, for soup eval aider (v0.74.0)
pip install "soup-cli[mcp]"        # MCP server (soup mcp serve) for coding agents
pip install "soup-cli[cce]"        # Cut Cross-Entropy (training.use_cut_ce)
pip install "soup-cli[mix]"        # scikit-optimize, for soup data mix --optimize
pip install "soup-cli[pdf]"        # reportlab, for the EU AI Act Annex XI/XII PDFs
pip install "soup-cli[dev]"        # the test and lint stack, for contributing
pip install "soup-cli[all]"        # shorthand for train + serve + ui + data + mcp
```

### Use double quotes, and here is why

`pip install "soup-cli[train]"` is the **only spelling that works in every shell**: `cmd.exe`, PowerShell, bash and zsh. Every command above uses it.

Older tutorials and videos, including some of ours, show the single-quoted `pip install 'soup-cli[train]'`. That is bash, zsh and PowerShell syntax. Windows `cmd.exe` has no single-quote quoting, so it hands the quotes straight to pip:

```
ERROR: Invalid requirement: "'soup-cli[train]'": Expected package name at the start of dependency specifier
```

If you hit that, swap the `'` for `"`. Nothing is wrong with the package: pip is rejecting a literal quote character. Dropping the quotes entirely also works on Windows, but then zsh reads `[train]` as a glob and fails instead.

## Quick Start

### 1. Create a config

```bash
# Interactive wizard
soup init

# Or use a template
soup init --template chat
```

### 2. Train

```bash
soup train --config soup.yaml
```

Soup automatically detects your GPU, sets optimal batch size, configures LoRA, and begins training.

### 3. Chat with your model

```bash
soup chat --model ./output
```

### 4. Push to HuggingFace

```bash
soup push --model ./output --repo your-username/my-model
```

### 5. Export and serve

```bash
# Export to GGUF for Ollama / llama.cpp
soup export --model ./output --format gguf --quant q4_k_m

# Start OpenAI-compatible server
soup serve --model ./output --port 8000
```

## Health Check

Check your environment for compatibility issues:

```bash
soup doctor
```

Shows Python version, GPU availability, all dependency versions, and fix suggestions.

## Quick Demo

Run a complete demo in one command:

```bash
soup quickstart          # Creates sample data + config + trains TinyLlama
soup quickstart --dry-run # Just create files without training
```

[NextConfiguration](/docs/configuration)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="002-configuration"></a>

# 2. Configuration

*Source: <https://trysoup.dev/docs/configuration>*

Soup uses a single YAML config file for all settings. Run `soup init` to generate one.

## Reproducibility and full fine-tuning (v0.73.0)

Two `training` keys landed in v0.73.0. Both are **config keys, not CLI flags**.

```yaml
training:
  seed: 1234        # weight init of new params, data order, dropout
  data_seed: 7      # optional: vary data order while holding init fixed
  lora:
    r: 0            # 0 means no adapter: full fine-tuning, dense checkpoint
```

`seed` and `data_seed` are the first seed knobs in the project's history: before this every run trained at seed 42 with no way to change it, so "run this twice with a different seed" was impossible. **Both default to unset rather than to 42**, deliberately, because an unset seed has to keep reproducing two different historical defaults (the trainer's 42 and the multipack sampler's 0) and a plain 42 would have silently re-ordered every existing multipack run. A boolean is refused by name, since `seed: true` would otherwise become seed 1.

The honest scope, and it widened in v0.73.1: the seed reaches the trainer arguments in **every wrapper** now, applied before the model loads, so setting it on a DPO run is real. It reached one wrapper of eighteen when it shipped in v0.73.0, which is what the original note here described. On a [streamed](/docs/layer-streaming) run it additionally seeds the adapter initialisation for all five streaming tasks, which is why a streamed run is bit-reproducible from a seed while a resident 4-bit one still is not.

`lora.r: 0` selects **full fine-tuning** on `task: sft` and, since v0.75.0, `task: embedding`: no adapter is built, and the run writes a dense checkpoint rather than a LoRA. **On any other task the gate does not apply at all**, and that is worth knowing before you rely on it: `classifier`, `reranker`, `cross_encoder` and `asr` gate LoRA behind their own flag and ignore the rank entirely, while the remaining tasks hand the 0 straight to PEFT, which rejects it with its own message about a positive integer rather than Soup's named one. Rank 0 was chosen because three parts of the codebase already read it as "no adapter" and because `r: 0` used to crash, so no config that worked before changes meaning. It is refused with a named message alongside a non-transformers backend, a non-text modality, any quantisation, Spectrum, LISA, layer streaming, or any LoRA-shaped option, and it refuses rather than running a no-op if your freeze settings leave nothing trainable.

## Config Structure

```yaml
base: meta-llama/Llama-3.1-8B-Instruct   # HuggingFace model ID (required)
task: sft                                   # Training task
# backend: unsloth                          # 2-5x faster (pip install "soup-cli[fast]")
# modality: text                            # text, vision, or audio

data:
  train: ./data/train.jsonl                 # Path to training data
  format: alpaca                            # Data format (auto-detected if omitted)
  val_split: 0.1                            # Validation split ratio
  max_length: 2048                          # Max sequence length (64-1048576)
  # image_dir: ./data/images               # For vision modality
  # audio_dir: ./data/audio                # For audio modality

training:
  epochs: 3
  lr: 2e-5
  batch_size: auto                          # auto or integer
  quantization: 4bit                        # none, 4bit, 8bit
  # weight_decay: 0.01                      # default 0.01
  # max_grad_norm: 1.0                      # gradient clipping, default 1.0
  # logging_steps: 10                       # log metrics every N steps
  # save_steps: 100                         # checkpoint every N steps
  # warmup_ratio: 0.03                      # 0.0-0.5, default 0.03
  # scheduler: cosine                       # LR scheduler
  # quantization_aware: false              # Enable QAT
  # optimizer: adamw_8bit
  # gradient_checkpointing: true
  # stream_layers: false                   # Train or align a model bigger than VRAM (v0.72, BETA)
  # stream_source: auto                    # auto | ram | disk
  # stream_buffers: 2                      # 2-8
  # stream_pin: false                      # v0.74.0: force the pageable store
  lora:
    r: 64
    alpha: 16
    dropout: 0.05
    # target_modules: auto                 # Auto-detected per model
    # use_dora: false                      # Weight-decomposed LoRA

output: ./output
```

## Layer streaming keys

These turn on [layer streaming](/docs/layer-streaming), which trains a model larger than your VRAM by keeping the frozen base out of the card entirely. They are **config keys, not CLI flags**: there is deliberately no `--stream-layers`.

| Key | Values | Default | Notes |
| --- | --- | --- | --- |
| `stream_layers` | `true` / `false` | `false` | BETA. Only enable it if the model does **not** fit resident; streaming trades time for memory |
| `stream_source` | `auto` / `ram` / `disk` | `auto` | `auto` takes RAM when the base fits and falls back to an NVMe tier; `ram` refuses instead of falling back; `disk` forces NVMe |
| `stream_buffers` | `2` to `8` | `2` | VRAM buffers in the pool. 2 is double-buffering; 1 cannot overlap load with compute, so it is refused |
| `stream_vram_probe` | `true` / `false` | `false` | v0.73.1. Decide the fit by **measuring** one real forward and backward at your shape, instead of predicting it. `task: sft` only. Costs 1 to 5 seconds, and cannot overrule a prediction more than 4x over budget |
| `stream_disk_kind` | `nvme` / `ssd` / `hdd` | (unset) | v0.73.3. Override the detected media type behind the disk tier. `nvme` forces the tier on, `ssd` and `hdd` force it off. The override prints beside what was actually detected, and deliberately carries no measured rate, so a later refusal can never cite a reading you overrode |
| `stream_vram_override` | bytes | (unset) | v0.73.1. **Replaces** the free-VRAM figure the pre-flight checks against, in either direction. It changes the yardstick, not the check: an override below real free VRAM still refuses a config that would otherwise fit |
| `stream_pin` | `true` / `false` | (unset) | v0.74.0. Force the RAM store pageable or page-locked instead of letting Soup decide. `false` prints the throughput it costs rather than absorbing it silently; `true` **refuses on the RAM tier** if the box cannot page-lock the store, naming the store size rather than a ceiling nobody probed, and is announced-and-proceeds on the disk tier and on CPU, where there is nothing to page-lock |
| `stream_ngram_source` | `auto` / `ram` / `disk` | `auto` | v0.74.0. Where Qwen4-Exp's external N-gram table is read from. Read-only, and only meaningful for that family |

Setting any of these while `stream_layers` is `false` is refused, because the knobs would silently do nothing.

> **A key the schema does not declare is no longer silently dropped (v0.74.0).** Until then none of the config models overrode the library default of ignoring undeclared keys, so a typo validated clean and was discarded: `training.quantizaton: none` trained 4-bit, `training.gradient_checkpoint: true` did no checkpointing, `data.max_len: 512` truncated at 2048, and `soup train --dry-run` printed "Config valid. Ready to train!" Loading a config now walks the whole model tree and reports every key it cannot place in one report, naming the field you probably meant. **Since v0.75.0 the load is refused.** `soup train` exits 1 before the training stack is imported, and the API and Web UI loader raises `ValueError` with the same text. Nothing is defaulted and nothing is substituted; the message says `Refused.` rather than `Not applied.`, which would have read as if the run went ahead without the key, and the scan stops at 100 findings and says so. Two things are worth knowing. A config that must stay loadable on v0.74 as well needs the key **removed, not renamed**, because v0.74 warns and ignores it while v0.75 refuses it, and neither applies it. And `soup plan` and `soup apply` read the YAML as a plain mapping, so they do not run this check at all. `soup sweep` is stricter, because a swept parameter that matches nothing produces a grid of identical arms and a meaningless winner: it **exits 1** before the first arm.

`stream_vram_probe` and `stream_vram_override` are not interchangeable, and the difference is the point. `stream_vram_probe` is **a measurement**: it runs the step and reads the peak. `stream_vram_override` is **an assertion you are making** about how much VRAM is really available, which is what you need when the pre-flight cannot see the truth, as under a per-process memory cap in a hosted notebook.

Streaming also constrains keys you already set: `quantization` must be `none` or `4bit`, `batch_size` must be a concrete number rather than `auto`, and `task` must be one of `sft`, `dpo`, `orpo`, `simpo` and `kto` (`kto` additionally needs `batch_size` of 2 or more). [Scaling a streaming run](/docs/streaming-scaling) covers sizing, the VRAM pre-flight and the disk tier; [Preference losses over streaming](/docs/streaming-preference) covers the four alignment tasks.

## Templates

Soup includes 21 built-in templates:

```bash
soup init --template chat          # Conversational fine-tune
soup init --template code          # Code generation
soup init --template medical       # Domain expert
soup init --template reasoning     # GRPO reasoning (DeepSeek-R1 style)
soup init --template vision        # Vision/multimodal fine-tune
soup init --template audio         # Audio/speech fine-tune
soup init --template kto           # KTO unpaired preference
soup init --template orpo          # ORPO (no reference model)
soup init --template simpo         # SimPO length-normalized preference
soup init --template ipo           # IPO regularized preference
soup init --template bco           # BCO binary classifier preference (v0.40)
soup init --template rlhf          # Full RLHF pipeline (SFT -> RM -> PPO)
soup init --template pretrain      # Continued pre-training on raw text
soup init --template moe           # MoE fine-tuning (ScatterMoE LoRA)
soup init --template longcontext   # 128k+ context fine-tuning
soup init --template embedding     # Sentence embedding fine-tuning
soup init --template tool-calling  # Function / tool-calling fine-tune (v0.25)
```

Four more are regulation-shaped ([compliance pack](/docs/compliance-pack), v0.71.35). Each is a valid training config on a license-clean Apache-2.0 base plus header comments naming that regime's exact commands, because Soup's compliance controls are CLI flags and commands rather than config keys:

```bash
soup init --template hipaa         # Protected Health Information
soup init --template soc2          # SOC 2 Trust Services Criteria
soup init --template eu-ai-act     # EU AI Act Annex XI/XII
soup init --template sr-11-7       # SR 11-7 Model Risk Management
```

## Task-Specific Config Keys

| Key | Tasks | Description |
| --- | --- | --- |
| `dpo_beta` | DPO | DPO beta parameter |
| `kto_beta` | KTO | KTO beta parameter |
| `orpo_beta` | ORPO | ORPO beta parameter |
| `simpo_gamma` | SimPO | SimPO gamma parameter |
| `cpo_alpha` | SimPO | CPO alpha parameter |
| `ipo_tau` | IPO | IPO tau parameter |
| `grpo_beta` | GRPO | GRPO beta parameter |
| `num_generations` | GRPO | Number of generations per prompt |
| `reward_fn` | GRPO, PPO | Reward function (accuracy/format/path.py) |
| `reward_model` | PPO | Path to reward model |
| `ppo_epochs` | PPO | PPO training epochs |
| `ppo_clip_ratio` | PPO | PPO clip ratio |
| `ppo_kl_penalty` | PPO | PPO KL penalty |
| `loraplus_lr_ratio` | All | LoRA+ learning rate ratio |
| `use_galore` | All | Enable GaLore optimizer |
| `moe_lora` | All | Target MoE expert layers |
| `moe_aux_loss_coeff` | All | Router load-balancing loss |
| `use_liger` | All | Liger Kernel fused ops |
| `use_flash_attn` | All | FlashAttention v2/v3 |
| `use_ring_attention` | All | Ring FlashAttention |
| `rope_scaling_type` | All | RoPE scaling (linear/dynamic/yarn/longrope) |
| `neftune_alpha` | All | NEFTune noisy embeddings (0-50) |
| `packing` | SFT | Sample packing for efficiency |
| `curriculum` | All | Enable curriculum learning |
| `curriculum_metric` | All | Sort metric (length) |
| `curriculum_buckets` | All | Number of difficulty buckets (1-20) |
| `loss_watchdog` | All | Enable loss watchdog |
| `loss_watchdog_threshold` | All | Loss spike threshold (≤100) |
| `loss_watchdog_patience` | All | Patience before stopping (≤1000) |
| `freeze_layers` | All | Freeze bottom N layers (≤1000) |
| `freeze_ratio` | All | Freeze ratio of layers |
| `embedding_loss` | Embedding | Loss function |
| `embedding_pooling` | Embedding | Pooling strategy |

[PreviousInstallation](/docs/getting-started)[NextTraining Intelligence](/docs/training-intelligence)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="003-training-intelligence"></a>

# 3. Training Intelligence

*Source: <https://trysoup.dev/docs/training-intelligence>*

v0.25.0 adds two training-time subsystems: **catastrophic forgetting detection** and **checkpoint intelligence**. The forgetting signal later became leg 2 of [`soup ship`](/docs/soup-ship)'s SHIP / DON'T-SHIP verdict.

## Catastrophic forgetting detection

Runs a mini benchmark on the base model \*before\* training, then repeats it every N steps on the current checkpoint. If general-knowledge accuracy drops more than your threshold, the Rich dashboard turns yellow; cross the red line and you can auto-stop training.

### Forgetting-detection config

```yaml
training:
  forgetting_detection: true
  forgetting_eval_steps: 100
  forgetting_threshold: 0.10       # warn if accuracy drops >10%
  forgetting_benchmark: mini_mmlu  # mini_mmlu | mini_common_sense | mini_instruction
  forgetting_stop: false           # auto-stop on severe forgetting
```

### Built-in benchmarks

Each is a hand-authored set embedded in the source, no external downloads: 26 items in `mini_mmlu`, 24 in `mini_common_sense` and 24 in `mini_instruction`. The sets are small on purpose, sized so a single item flipping moves the score past the default 0.05 threshold, and they are worth reading before you reason about what a delta means.

- `mini_mmlu` — diverse MMLU coverage (STEM / humanities / social sciences)
- `mini_common_sense` — common-sense reasoning
- `mini_instruction` — instruction-following quality

## Checkpoint intelligence

HF Trainer's "best checkpoint" is the one with lowest loss. But lower loss ≠ better model — overfitted checkpoints hit low loss with bad real-world quality. Checkpoint intelligence runs a quality eval \*during\* training and tags `best_quality` separately from `best_loss`.

### Checkpoint-intelligence config

```yaml
training:
  checkpoint_intelligence: true
  checkpoint_eval_steps: 200
  checkpoint_eval_metric: composite   # judge | mmlu | custom | composite
  checkpoint_eval_tasks: eval.jsonl   # optional custom eval
  checkpoint_keep_top: 3              # delete the rest
  early_stop_on_regression: true
  early_stop_patience: 2
```

### Dashboard

```
Epoch 2/3 ████████ loss: 0.89  step 450/720
  → Loss best:     step-450 (loss 0.89)
  → Quality best:  step-300 (judge 8.2/10) ⭐
  → Gen knowledge: 91.2% (baseline 95.0%, -3.8% ⚠)
  → Last eval:     +0.4 judge points (improving)
```

After training, the `best_quality` checkpoint is linked at `./output/best_quality/`.

## Storage

Both subsystems extend the SQLite experiment tracker (`~/.soup/experiments.db`) with two new tables:

- `checkpoint_quality(run_id, step, metric, score, is_best, created_at)`
- `forgetting_eval(run_id, step, benchmark, accuracy, baseline, delta, warning_level)`

Inspect them with `soup runs show <run_id>` or query directly.

## Safety

- Benchmark data is embedded in code — no external file loading at runtime.
- Eval intervals are bounded to prevent runaway eval overhead, and the two floors differ: `forgetting_eval_steps` is 10 to 10,000 (default 100), `checkpoint_eval_steps` is **50** to 10,000 (default 200). A value of 20 is inside one range and refused by the other.
- Pruning only deletes files inside the run's `output_dir` and never follows symlinks outside.

## Defaults

Autopilot turns both subsystems on by default. If you hand-write `soup.yaml`, flip the flags above.

[PreviousConfiguration](/docs/configuration)[Nextsoup advise: pre-flight decision engine](/docs/advise)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="004-advise"></a>

# 4. soup advise— decide before you train

*Source: <https://trysoup.dev/docs/advise>*

Before you touch a GPU, ask: do you actually need to fine-tune? Or is your problem better solved with prompt engineering, RAG, DPO instead of SFT, or GRPO over rewards?

`soup advise` (v0.54.0) is a **pre-flight decision engine**. It classifies your task, profiles your dataset, and emits a ranked verdict across:

- `PROMPT_ENG` — your data is too small / your goal is solvable with a better prompt
- `RAG` — high-variance factual recall is better handled with retrieval
- `SFT` — supervised fine-tuning is the right baseline
- `DPO` — you already have preference pairs (`chosen`/`rejected`)
- `GRPO` — you have reasoning traces + ≥ 500 rows, RL over verifiable rewards wins

## Usage

```bash
soup advise run data.jsonl --goal "polite customer support chat"
```

Output:

```text
SFT (recommended)
  why:
    - 4,213 rows (above _MIN_ROWS_FOR_TRAINING=50)
    - no preference pairs detected
    - no reasoning traces — GRPO ruled out
    - tone-shift goal — SFT is the right baseline
  next: soup autopilot --model meta-llama/Llama-3.1-8B --data data.jsonl --goal chat
```

## Heuristics

- **Task classification**: keyword + structural signals. `tool_calls` field → tool\_use; `<think>...</think>` blocks → reasoning; chat-shaped messages → input-extraction. The `--goal` string carries ~10× the row weight when classifying.
- **Dataset profile**: row count, avg input/output chars, type-token diversity, label variance, `has_chosen_rejected`, `has_reasoning_traces`. Capped at 2,000-row sample for speed.
- **Verdict rubric**: preference pairs detected → DPO · reasoning traces with 500 rows or more → GRPO · under 50 rows → PROMPT\_ENG (training will overfit) · high-variance factual → RAG · default → SFT

## `--probe` — put real numbers on the ROI estimate

```bash
soup advise run data.jsonl --goal "..." --probe
```

Runs a 100-step LoRA probe and a held-out zero-shot / few-shot / RAG baseline, bounded to `[-1, 1]` per-method delta. The 600-second timeout is a hard wall.

## `--record` — cross-project history

```bash
soup advise run data.jsonl --goal "..." --record
```

Appends a frozen `HistoryEntry` to `~/.soup/advise_history.jsonl` (atomic, file-locked via `fcntl.flock` on POSIX / `msvcrt.locking` on Windows, 64 KB per-line cap, 16 MiB file cap, 10k row cap). Future verdicts read this back via `summarise_history` so the engine learns across projects.

Override the path with `SOUP_ADVISE_HISTORY_PATH` — containment-checked to `$HOME` / `$CWD` / `tempfile.gettempdir()`. Default file perms: `0o600`.

## Subcommands

```bash
soup advise run data.jsonl --goal "..."   # explicit (also the default)
soup advise explain                       # print the full rubric
soup advise compare --limit 20            # prior verdicts from advise_history.jsonl, newest first
```

The top-level argv preprocessor `_rewrite_advise_argv` injects `run` so `soup advise data.jsonl` works without typing the subcommand.

## See also

- [Autopilot](/docs/autopilot) — the literal next step after `soup advise`
- [Eval design](/docs/eval-design) — turn your data into evals
- [Trace-to-preference](/docs/trace-to-preference) — distill production traffic into DPO pairs
- [Pre-flight & tooling (v0.64)](/docs/preflight-tooling) — `soup tunability` picks the right base model after advise picks the right task; `soup plan` + `soup apply` then lock the plan with drift detection before training

[PreviousTraining Intelligence](/docs/training-intelligence)[NextPre-flight & Tooling](/docs/preflight-tooling)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="005-preflight-tooling"></a>

# 5. Pre-flight & Tooling (v0.64.0)

*Source: <https://trysoup.dev/docs/preflight-tooling>*

Six surfaces that catch mistakes **before** you spend a GPU hour: pick the right base, lock the run plan, freeze the environment, install completions, advise on licenses, and predict peak VRAM.

## `soup tunability` — Pareto frontier of base-model efficiency

```bash
soup tunability --dataset ./chats.jsonl --candidates qwen3-1.7b,llama-3.2-3b,phi-4-mini \
  --probe-steps 100 --holdout-size 64 --output ./tunability.json
```

Ranks candidate bases by how much fine-tuning is likely to buy on your data, and reports which of them form the **Pareto frontier** (best efficiency for cost). By default the score is a deterministic heuristic, not a measurement. Add `--live` (with `--device`) to actually probe each candidate with a lightweight LoRA on a held-out slice and rank on measured training-loss deltas.

`--candidates` is an **allowlist**, and a name outside it exits non-zero rather than falling back. The eight bundled candidates are `qwen3-0.6b`, `qwen3-1.7b`, `llama-3.2-1b`, `llama-3.2-3b`, `gemma-3-e2b`, `phi-4-mini`, `smollm3-1.7b` and `qwen2.5-1.5b`; `--list` prints them with their licences, and `--plan-only` dry-runs without probing.

- Candidate **allowlist** with licensing metadata (Apache-2.0 / MIT / LLaMA-3 / etc.)
- Bounds: `probe_steps ∈ [10, 10000]`, `holdout_size ∈ [10, 100000]` rows
- Safety: path containment, null-byte rejection, symlink-escape rejection
- Output: per-candidate delta, wall-clock seconds, estimated USD cost, Pareto membership

## `soup plan` / `soup apply` — Terraform-shaped drift detection

```bash
soup plan --config soup.yaml --state ./soup.tfstate
soup apply --config soup.yaml --state ./soup.tfstate
```

`plan` computes cost / ETA / peak-VRAM / SHA-256 hashes from the config and writes an **immutable** `soup.tfstate`. `apply` re-reads the config, detects any drift (batch size, dataset SHA, base SHA) and **refuses to proceed** (exit 3) until you re-plan.

- Pure JSON state: `plan{cost, eta, sha}`, `applied: bool`, `applied_at`, `run_id`
- TOCTOU defense: `os.lstat` before open, symlinks rejected
- Peak VRAM with 10% safety margin; spot pricing per GPU tier
- Composes with v0.67 `soup lock` for full reproducibility

## `soup env lock` / `status` / `check` — hermetic environment

```bash
soup env lock --output ./soup-env.lock
soup env check --lock ./soup-env.lock   # exit 3 on ABI drift
soup env check                          # v0.73.3: also audits declared bounds, no lock needed
```

Snapshots Python version, CUDA major version, platform, and every installed package into a JSON lockfile. `check` detects **ABI-sensitive** drift (e.g. CUDA 12 → 13) that would silently break training.

**Since v0.73.3 it also audits your installed packages against Soup's own declared version bounds**, and exits 3 when one is violated. That runs first and **independently of any lock file**, so it catches the case it was reported for: installing a fast serving stack into a training environment silently pushes `transformers` past the `<5.0.0` cap Soup itself declares, producing an environment Soup's own metadata calls unsupported with no warning at any point. The bounds are read from package metadata rather than a second hardcoded copy, because a second copy is exactly the drift this is meant to catch. The lock diagnostic still prints either way, so a bounds violation cannot hide a missing lock file or an ABI drift.

The practical guidance that came with it: **install `[serve-fast]` in a separate environment from `[train]`.** Their resolutions are genuinely incompatible today.

### `soup env fix` — the repair, once `check` has told you something is wrong

```bash
soup env fix                                   # print a uv-pip install plan from the lock
soup env fix --format requirements             # print it as requirements lines instead
soup env fix --format requirements -o req.txt  # also write that file, under cwd
```

It renders a reproducible install plan from `soup-env.lock` and **prints it. It never installs anything**, and that is deliberate rather than unfinished: recreating a virtual environment is environment-dependent, so Soup emits the commands for you to read, paste or script rather than shelling out to a package manager on your behalf. With no lock file it exits 1 and tells you to run `soup env lock` first.

- Fields: `soup_version`, `python_version`, `platform`, `cuda_version`, packages `{name, version, source}`
- Atomic write, file-size capped
- Feeds the `env_hash` half of v0.67 `soup.lock` closure

## `soup completions <shell>` — bash / zsh / fish

```bash
soup completions bash  | sudo tee /etc/bash_completion.d/soup
soup completions zsh   > ~/.zsh/completions/_soup
soup completions fish  > ~/.config/fish/completions/soup.fish
```

Eval-safe shell completion scripts emitted to stdout (no Rich panels). Closed shell allowlist; all error messages go to stderr.

## `soup license-advisor` — deploy-target risk gate

```bash
soup license-advisor --target b2c --license llama-3 --monthly-active-users 750000
```

Returns `ok` / `warn` / `block` (exit 3 on block) for a (license, deploy-target, MAU) tuple. Targets: `b2c`, `defense`, `embedded` — each with distinct rules. Composes with v0.60 license-matrix on `soup adapters merge`.

## Hardware-fit calculator — analytical peak VRAM

```python
from soup_cli.utils.hardware_fit import estimate_peak_vram_gb, decide_hardware_fit

report = decide_hardware_fit(input, available_vram_gb=24.0)
# report.predicted_peak_gb -> 18.2
# report.breakdown -> {weights: 4.1, optimizer: 8.2, gradients: 4.1, activations: 1.3, overhead: 0.5}
```

Static predictor with a 5-bucket breakdown (weights / optimizer / gradients / activations / overhead) and a **10% safety margin**. Refuses to run if predicted peak exceeds available VRAM.

If you disagree with it, `soup train --allow-oom-attempt` bypasses this gate and launches anyway. It is opt-out rather than opt-in for a reason: a prediction that refuses a run which would have worked costs you an argument, while a run that launches and does not fit costs you the run. Note this is the **analytical** gate for an ordinary resident run. Layer streaming skips it entirely and uses its own budget instead, which this flag does not reach; the streaming equivalents are the config keys `stream_vram_probe` and `stream_vram_override`.

- 9 quant tiers (`none`, `4bit`, `8bit`, `fp8`, `gptq`, `awq`, `aqlm`, `eetq`, `mxfp4`)
- 4 PEFT modes (`full`, `lora`, `dora`, `qlora`)
- Bounds: `seq_len ∈ [64, 1M]`, `batch ∈ [1, 1024]`, `params ∈ (0, 1000B]`
- Activation memory halved under gradient checkpointing

## Numbers

Six surfaces, +N tests on top of v0.63's 10,035. Composes downstream with v0.65 eval depth, v0.66 post-train x-rays, and v0.67 adapter lifecycle.

## See also

- [Soup lock](/docs/adapter-lifecycle) — v0.67 closes the env\_hash → soup.lock reproducibility chain.
- [Governance](/docs/governance) — v0.59 BOM + SLSA-3 + audit log layer on top of plan/apply.

[Previoussoup advise: pre-flight decision engine](/docs/advise)[NextFine-tune Doctor](/docs/fine-tune-doctor)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="006-fine-tune-doctor"></a>

# 6. Fine-tune Doctor (v0.71.27)

*Source: <https://trysoup.dev/docs/fine-tune-doctor>*

Most fine-tunes don't fail loudly. They fail \*silently\*: the model never stops generating, the assistant turns were never actually trained, or your DPO run quietly learns "longer = better" instead of the preference you meant. **v0.71.27 "Fine-tune Doctor"** is a pure-CPU, zero-GPU pre-flight that catches these before a single training step.

> We have not found these checks in Unsloth, Axolotl or LLaMA-Factory. Without them you find out after the GPU hour.

## `soup data doctor` — 8 chat-template checks

```bash
soup data doctor chats.jsonl --model meta-llama/Llama-3.1-8B
```

It renders your data through the model's **real** tokenizer and chat template, then runs eight checks:

| # | Check | Catches |
| --- | --- | --- |
| 1 | `chat_template` present | Tokenizer with no chat template at all |
| 2 | `template_render` | A template that throws on your rows |
| 3 | `generation` markers | Missing `{% generation %}` spans (needed for response-only masking) |
| 4 | `eos_in_labels` | **The #1 "model never stops generating" bug** — every assistant turn's trained span must actually contain an EOS/EOT token (checked on \*every\* turn, not just the last) |
| 5 | `bos_duplication` | Template \*and\* tokenizer both prepending BOS |
| 6 | `system_role` | Mistral-style templates that reject a leading system turn |
| 7 | `unknown_roles` | Roles the template doesn't understand |
| 8 | `truncation_risk` | p95 rendered length vs `max_length` |

The verdict uses the same **OK / MINOR / MAJOR** taxonomy as [soup diagnose](/docs/diagnose): **exit 0** on OK/MINOR, **exit 2** on MAJOR, so it drops straight into CI.

### See the mask, don't guess it

```bash
soup data doctor chats.jsonl --model meta-llama/Llama-3.1-8B --show-mask 3
```

`--show-mask N` prints N sample rows with every token coloured **trained vs masked**, rendered through the **real collator path** (answer-only, per-message train-field, or RAFT span-mask), not a reimplementation. An assistant-mask bug becomes visible instantly. The flags `--train-on-responses-only` and `--train-on-messages-with-train-field` pick the exact masking strategy `soup train` would use, so what you see is what you'll train.

Dataset-derived strings are stripped of C0 control characters before hitting your terminal (Rich's markup escape doesn't neutralise raw ESC bytes); the `--output` JSON is unaffected.

## `soup data lint` — the preference-data linter

```bash
soup data lint prefs.jsonl              # word-count length bias
soup data lint prefs.jsonl --model Qwen/Qwen2.5-7B   # exact token-length bias
```

For `dpo / orpo / simpo / ipo / bco / kto` data it flags:

- **`length_bias`** — chosen systematically longer than rejected (**the #1 silent DPO degradation**), reported as a **Cohen's d effect size** so you know how bad it is, not just that it exists.
- **`label_imbalance`** — KTO desirable:undesirable ratio out of balance.
- **`near_duplicates`** — MinHash/LSH near-dupes (reuses the `soup data dedup` kernel).
- **`identical_pairs`** — chosen == rejected, i.e. zero preference signal.
- **`prompt_leak`** — the prompt echoed verbatim inside the completion.

## Numbers

Validated live against the real `HuggingFaceTB/SmolLM2-135M-Instruct` tokenizer; the smoke pass found and fixed two genuine bugs. Part of the v0.71 release line, which closed at **16,529 tests across 319 files**.

## See also

- [soup diagnose](/docs/diagnose) — the post-training report card whose OK/MINOR/MAJOR taxonomy the doctor mirrors.
- [Pre-flight & tooling](/docs/preflight-tooling) — `soup plan/apply`, `soup tunability`, hardware-fit, the rest of the "catch it before GPU" surface.
- [MCP server](/docs/mcp-server) — `data_doctor` is one of the tools exposed to your coding agent.

[PreviousPre-flight & Tooling](/docs/preflight-tooling)[NextEval-Gated Training](/docs/eval-gate)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="007-eval-gate"></a>

# 7. Eval-Gated Training

*Source: <https://trysoup.dev/docs/eval-gate>*

v0.26.0 adds declarative eval suites that run at epoch boundaries. If a task score falls below its threshold — or regresses against a baseline — training halts before you waste another epoch.

## The gate file

Every entry in `tasks:` is one of three types: `custom`, `judge`, or `benchmark`. Each task has a `name` (used as the baseline key) and a numeric `threshold`.

```yaml
# evals/gate.yaml
suite: chat-quality
tasks:
  - type: custom
    name: tool_calls
    tasks: evals/tool_calls.jsonl
    scorer: exact            # exact | contains | regex | semantic
    threshold: 0.70

  - type: judge
    name: chat_judge
    prompts: evals/judge_prompts.jsonl
    judge_model: ollama://llama3.1     # or https://... or http://localhost
    threshold: 0.70   # judge scores normalise to [0,1] off the rubric scale, not raw 1-5

  - type: benchmark
    name: mmlu
    benchmark: mini_mmlu
    threshold: 0.60
```

## Enable it

Either inline in `soup.yaml`:

```yaml
training:
  eval_gate:
    enabled: true
    suite: ./evals/gate.yaml
    every_n_epochs: 1              # 1-100
    regression_threshold: 0.05     # 0.0-1.0
    baseline: previous             # registry://<id> | previous | a path
    on_regression: stop            # stop | warn | continue
```

Those six are the whole block. `baseline` accepts a registry id, the literal `previous`, or a path to a scores JSON; `on_regression` decides whether a regression halts the run, prints, or is recorded and ignored.

…or on the command line:

```bash
soup train --config soup.yaml --gate ./evals/gate.yaml
```

## Post-hoc verdict

Run the gate standalone against any model:

```bash
soup eval gate --suite ./evals/gate.yaml --model ./output
# ✓ mmlu:        0.648 (baseline 0.643, +0.005) PASS
# ✗ chat_judge:  0.62  (baseline 0.78, -0.16)   REGRESSION
# → verdict: FAIL
```

A task fails if its score is below its `threshold` \*or\* if it drops more than the configured regression threshold (default 0.05) below the supplied baseline.

## Baselines

- `registry://<id>` — pulls eval results for the referenced [registry](/docs/registry) entry
- `./baseline.json` — a JSON map of `{task_name: score}`
- omitted — tasks are judged only against their `threshold`

### Baseline provenance (v0.74.0)

```bash
soup eval gate --suite ./suite.yaml --model ./output --write-baseline ./baseline.json
```

A written baseline now carries a provenance block, the Soup version and a scorer revision, alongside its scores. Reading one back **warns once** when the stamp is missing, which is what an older file looks like, or when the scorer revision has moved underneath it, and stays silent when it matches. That replaces the v0.73.2 warning, which recognised a stale baseline by a **hardcoded list of suite names** and therefore could only ever know about the one scoring change somebody remembered to add. A locked fingerprint fails the test suite if a bundled scorer's output moves without its revision being bumped, so the stamp cannot quietly stop meaning anything.

> **A judge-scored task was normalized against the wrong scale until v0.74.0.** The gate divided the aggregate judge score by 10 while the default rubric runs 1 to 5, so a perfect 5.0 read as **0.50**, typical thresholds of 0.70 and 0.80 were impossible to satisfy, and a healthy run could be stopped by `on_regression: stop` for no reason. Normalization now derives the minimum and maximum from the rubric in use, clamps out-of-bounds values and handles a degenerate scale. If a judge-gated run of yours stopped early, that is worth re-checking.

## Judge URL allowlist

`judge_model` must use one of: `ollama://`, `https://`, or `http://localhost` / `http://127.0.0.1`. Any other scheme is rejected at load time — an SSRF guard on the eval path.

## See also

- [Registry](/docs/registry) — the typical baseline source
- [Evaluation](/docs/experiments) — the broader eval platform

[PreviousFine-tune Doctor](/docs/fine-tune-doctor)[Nextsoup eval design: derive evals from data](/docs/eval-design)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="008-eval-design"></a>

# 8. soup eval design— derive evals from your training data

*Source: <https://trysoup.dev/docs/eval-design>*

Before v0.55 you wrote your eval suite by hand. Now Soup drafts one from your data.

## `soup eval design`

```bash
soup eval design data.jsonl --goal "polite customer support chat" --num-dimensions 5
```

How it works:

1. **TF-IDF salience** picks up to `num_dimensions` (default 5) salient terms over the dataset. 10,000-row DoS-capped subsample.
2. **Goal-keyword dispatch** maps each dimension to a scorer: `json` / `code` / `math` → `rlvr` (verifiable reward), `classify` → `exact_match`, `extract` → `regex`, and everything else → `judge`.
3. Output: a frozen `EvalDesign` (JSON) with one `EvalDimension` per row.

Scorer allowlist: `{exact_match, regex, judge, rlvr}`.

## `soup eval discover` — canaries

```bash
soup eval discover data.jsonl --num-clusters 5 --per-cluster 3
```

Three sets:

- **Held-out canaries** — greedy farthest-first Jaccard-distance clustering (`_CLUSTER_SUBSAMPLE = 10_000`).
- **Adjacent-skill probes** — neighbours that fall just outside training distribution.
- **Memorization probes** — 25%-prefix truncation. If the trained model can continue the rest of a training row from its prefix, it memorized.

Per-group cap: `_MAX_CANARIES_PER_GROUP = 1024`.

## `soup eval lock` — pin the suite

```bash
soup eval lock my-design.json
```

Locks the design as a `SHA-256`-checksummed `eval_suite` artifact via `canonicalise_design_bytes` (canonical-JSON for stable hashes across runs). The frozen `LockedSuite` (path / sha256 / dimension\_count) is registered in the v0.26 registry alongside the new `canaries` artifact kind.

## `soup eval coverage` — gap analysis

```bash
soup eval coverage my-design.json --task reasoning
```

Checks the locked design against the v0.54.0 `TASK_CATEGORIES` taxonomy and the `_RECOMMENDED_SCORERS` allowlist (e.g. `reasoning → (rlvr, judge)`, `format_conversion → (regex, rlvr)`). Returns a `CoverageReport` with concrete gap recommendations.

## `soup eval gate-install` — git regression gate

```bash
soup eval gate-install --baseline run-id-7f3a
```

Writes `.git/hooks/pre-push` (atomic, POSIX `0o755`) that:

1. Runs your locked eval suite on the current head.
2. Compares each `GateThresholds` metric (`task_accuracy` / `refusal_rate` / `format_validity` / `p95_latency_ms`) against the baseline via `paired_bootstrap_ci(baseline, candidate, n_samples, ci_level, seed)`, where `n_samples` is bounded to `[100, 100_000]` and `ci_level` to `(0, 1)`.
3. `decide_regression` uses direction-aware metric handling via `_METRIC_DIRECTION` — higher-is-better for accuracy, lower-is-better for latency.
4. Refuses the push on a `RegressionVerdict` of `REGRESSED`.

The hook script is rendered via `render_pre_push_hook` with `shlex.quote` for every interpolated path — no shell injection.

## `soup eval against` — the check the hook runs

The hook above is a wrapper. This is the command inside it, and you can run it by hand any time you want to compare two runs without pushing anything.

```bash
soup eval against <baseline-run-id> --candidate <candidate-run-id>
```

It reads the per-row metric series for both runs from the experiment tracker, runs the same `decide_regression` on the paired delta, and **exits 0 when there is no regression and 1 when there is**, so it drops into any CI step, not only a git hook.

| Flag | Default | Meaning |
| --- | --- | --- |
| `--candidate` | (required) | The run whose metrics are compared against the baseline. |
| `--metric` | `task_accuracy` | One of `task_accuracy`, `refusal_rate`, `format_validity`, `p95_latency_ms`. |
| `--n-samples` | `1000` | Paired-bootstrap samples, bounded to `[100, 100000]`. |
| `--seed` | `0` | Deterministic seed, so the verdict is reproducible. |
| `--suite` | (none) | A locked suite from `soup eval lock`, validated as a gate precondition. A missing or unparseable suite **blocks** the check rather than skipping it. |
| `--json-only` | off | One JSON verdict line instead of the rendered panel. |

The `--suite` behaviour is the part worth knowing: the generated pre-push hook passes the locked suite through, so a suite that has gone missing fails the gate instead of quietly turning it off.

## See also

- [Quant-check](/docs/quant-check) — same idea, but for quant-induced regression
- [Eval-gated training](/docs/eval-gate) — halt training when quality drops
- [Registry](/docs/registry) — where `eval_suite` and `canaries` artifacts live
- [Eval depth (v0.65)](/docs/eval-depth) — 4 deeper optional probes (behavior, capability, checklist, irt-subset) that stack on top of v0.55 dimensions
- [Post-train x-rays (v0.66)](/docs/post-train-xrays) — 4 mechanistic-interpretability probes (sae-diff, sleeper, interference, pack); failure-mode coverage 6 → 10

[PreviousEval-Gated Training](/docs/eval-gate)[NextEval Depth](/docs/eval-depth)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="009-eval-depth"></a>

# 9. Eval Depth (v0.65.0)

*Source: <https://trysoup.dev/docs/eval-depth>*

Failure-mode coverage goes from 7 to 11. The v0.56 diagnose report card stays the daily driver; v0.65 adds four optional deeper probes you opt into when you actually care, plus a fifth piece that is not a probe at all: a calibration gate for the judge the other evals lean on.

## `soup eval behavior` — pre/post safety diff

```bash
soup eval behavior <run-id> --battery xstest \
  --evidence ./responses.json --output ./behavior.json
```

Bundled safety / refusal / jailbreak / sycophancy probe sets, scored pre-FT vs. post-FT with the v0.26 / v0.56 `OK ≥0.85 / MINOR ≥0.60 / MAJOR` thresholds.

Five batteries at launch:

| Battery | What it catches |
| --- | --- |
| `xstest` | Over-refusal on benign prompts |
| `harmbench` | Jailbreak resistance |
| `jailbreakbench` | Jailbreak prompt-pair contrasts |
| `elephant` | Sycophancy / opinion-shifting |
| `syceval` | Sycophantic alignment to user |

Evidence is operator-supplied JSON `{pre_responses, post_responses, oracle}` by default. `soup eval behavior --base-model <m> --adapter <a> [--device <d>]` generates both response sets itself instead. 16 MiB file cap, `O_NOFOLLOW` open against symlink swap.

## `soup eval capability` — lm-eval-harness task surface

```bash
soup eval capability <run-id> --suite full --output ./capability.json
```

Validated lm-eval-harness task IDs for **7 bundled benchmarks** — MMLU-Pro, GPQA, BBEH, AIME, MATH-500, HumanEval+, SWE-bench-Verified. Four profiles: `full`, `fast`, `math`, `code`.

By default `soup eval capability` validates the task IDs and emits a runbook for you to execute. Add `--live` with `--model` and `--tasks` (plus `--limit` / `--device`) and it runs the harness itself.

## `soup eval checklist` — MFT / INV / DIR DSL

```yaml
# spec.yaml
tests:
  - name: capital_facts
    kind: mft                     # minimum functionality
    prompts: ["What is the capital of France?"]
    expected: ["Paris"]
  - name: paraphrase_stable
    kind: inv                     # invariance under paraphrase
    prompts: ["Capital of FR?", "Tell me FR capital"]
    expected: ["Paris"]
  - name: more_polite
    kind: dir                     # directional perturbation
    prompts: ["You're rude.", "You're being unhelpful."]
    expected: ["apolog"]
```

CheckList-style behavioral DSL. Up to 1,000 tests per spec; 1 MiB YAML cap; `enforce_under_cwd_and_no_symlink` on file open.

## `soup eval irt-subset` — Rasch IRT cost-cut

```bash
soup eval irt-subset ./responses.jsonl --size small --output ./plan.json
```

Fits a 1-parameter Rasch IRT model to per-item correctness signals and selects a **minimum-cost subset** that preserves ranking power:

- `full` = 100% of items
- `small` = ~30% (Rasch information-weighted)
- `tiny` = ~10%

The math: `P(correct | θ, β) = σ(θ - β)`, item information `I(β) = σ(-β) · σ(β)`. Information **peaks at β≈0** (50/50 items most discriminate). Pure-Python kernel — no numpy/scipy.

256 MiB JSONL cap; item-ID validated (≤256 chars, no null bytes).

## Judge calibration — measure the judge before you trust its scores

Every judge-based eval on this page, and `soup ship --task-mode judge_score` and `pairwise` too, rests on an LLM judge. A judge is an instrument, and an uncalibrated one produces numbers that look exactly like calibrated ones. v0.65.0 shipped the piece that measures it.

> **Library only, no CLI surface.** It is `soup_cli.eval.calibrate` and you call it from Python. There is no `soup eval calibrate` subcommand. Note also that the gate's own error message suggests running `soup eval design --calibrate`, and **that flag does not exist**: `soup eval design` takes only `--goal`, `--num-dimensions` and `--output`. Ignore the suggestion, not the error.

Two things get measured, both from judging the same pairs **in both orders**:

- **Position bias** (`fit_position_bias`) returns a coefficient in `[-1, 1]`. **0.0** means the judge agrees with itself when you swap the slots; **+1.0** means it always picks whichever answer was shown first, regardless of content; **-1.0** means it always picks the second. It is computed as the rate at which the two orderings disagree, so a perfectly consistent judge scores 0.0.
- **Agreement rate** against an oracle set you supply.

`conformal_threshold(scores, alpha=0.1)` then turns the calibration scores into an **abstention threshold**: at production time, judgements whose confidence falls below it should be abstained from rather than scored, which is what preserves the coverage you asked for. `alpha=0.0` abstains on nothing, `alpha=1.0` abstains on everything below the maximum.

The part worth having is the gate:

```python
from soup_cli.eval.calibrate import ensure_judge_calibrated, load_judge_calibration

report = load_judge_calibration("judge_calibration.json")
ensure_judge_calibrated(report, min_agreement=0.7, max_bias=0.3)
```

`ensure_judge_calibrated` **raises** rather than returning a verdict, and it raises on all four of: no calibration ran at all, the report says not calibrated, agreement below `min_agreement`, or position bias outside `±max_bias`. That is the same design choice as [`soup reward stress`](/docs/reward-verifier) refusing a gameable verifier: an instrument that has not been checked should stop the run, not quietly score it.

Reports persist with `write_judge_calibration` / `load_judge_calibration` and are stored in the registry under the artifact kind `judge_calibration`, so a judge's calibration travels with the run that used it.

## See also

- [Diagnose](/docs/diagnose) — v0.56 6-probe report card, the lighter daily driver.
- [Post-train x-rays](/docs/post-train-xrays) — v0.66 mechanistic interpretability probes that stack on top of v0.65 behaviour evals.

[Previoussoup eval design: derive evals from data](/docs/eval-design)[NextQuant-Lobotomy Check](/docs/quant-check)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="010-quant-check"></a>

# 10. Quant-Lobotomy Checker

*Source: <https://trysoup.dev/docs/quant-check>*

Quantization — 16-bit → 4-bit, say — often destroys niche capability you care about while the aggregate score looks fine. `soup eval quant-check` renders an OK / MINOR / MAJOR verdict per task so you never ship a stealth regression.

## Run it

```bash
soup eval quant-check \
  --before ./output/merged \
  --after ./output/merged.q4_k_m.gguf \
  --tasks critical_eval.jsonl
```

Both `--before` and `--after` accept either a filesystem path or `registry://<id>` pointing at a [registry](/docs/registry) entry.

## Output

```
Quant check
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━━━┓
┃ Task                      ┃ Before ┃ After ┃ Delta ┃ Verdict ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━━━┩
│ math.competition_hard     │ 0.540  │ 0.310 │ -0.230│ MAJOR   │
│ tool_call.multi_tool      │ 0.760  │ 0.510 │ -0.250│ MAJOR   │
│ instruction.long_context  │ 0.880  │ 0.840 │ -0.040│ MINOR   │
│ json_schema.deep_nested   │ 0.910  │ 0.905 │ -0.005│ OK      │
└───────────────────────────┴────────┴───────┴───────┴─────────┘
```

## Verdict thresholds

The classifier uses absolute drops in score:

- `OK` — drop `< 0.02` (or the score actually improved)
- `MINOR` — `0.02 ≤ drop < 0.05`
- `MAJOR` — `drop ≥ 0.05`

## Output formats

`--format` accepts `table` (default, Rich-rendered), `json`, or `markdown`. Pipe the output to a file if you want to persist the report:

```bash
soup eval quant-check --before X --after Y --tasks t.jsonl --format json > report.json
```

## Tasks file

Reuse any [custom eval JSONL](/docs/experiments):

```jsonl
{"prompt": "Solve: ...", "expected": "42", "category": "math.competition_hard", "scoring": "exact"}
{"prompt": "Capital of France?", "expected": "Paris", "scoring": "contains"}
```

## See also

- [Export](/docs/export) — GGUF / AWQ / GPTQ
- [Evaluation](/docs/experiments)

[PreviousEval Depth](/docs/eval-depth)[Nextsoup diagnose: post-training model report card](/docs/diagnose)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="011-diagnose"></a>

# 11. soup diagnose— seven failure-mode probes, one verdict

*Source: <https://trysoup.dev/docs/diagnose>*

After you finish training, the question is no longer "did the loss go down" — it's "did I quietly break something." `soup diagnose` (v0.56.0) is a post-training model report card that runs **7 pure-function failure-mode probes**:

| Probe | What it catches |
| --- | --- |
| `forgetting` | Per-task Δ accuracy with tolerance band — extends v0.25 `eval/forgetting` |
| `refusal` | advbench / xstest delta over caller-supplied generators (`_MAX_REFUSAL_SCAN = 8192`) |
| `format` | JSON / regex / tool-call validity over the RLVR verifier set, with an explicit ReDoS probe (`compiled.search("a" * 128)`) |
| `mode_collapse` | Pairwise n-gram-Jaccard distance over K completions (`k ∈ [2, 32]`, `ngram_n ∈ [1, 8]`) |
| `memorization` | Training-prefix echo via partial-prompt continuation (`_MAX_SCAN_ROWS = 1000`) |
| `contamination` | n-gram overlap with public benchmarks (combined-complexity cap rejects when training rows × benchmark corpus > 1e9) |
| `citation` | citation-recall regression on RAFT-shaped rows: does the answer still cite the supporting `[doc-id]`? (v0.71.10) |

Every probe is a pure function over a generator callable, which is why the same code path serves both modes. **Since v0.71.7 `soup diagnose` can supply that generator itself**: pass `--base-model` (with `--dataset`, and optionally `--tokenizer`, `--device`, `--citation-style` and `--shuffle-seed`) and it loads the model and runs the probes for you. Without `--base-model` it stays a pure scorer over evidence you supply, and you wire in your own `GeneratorFn` around a serve backend.

## Usage

```bash
soup diagnose <run-id> \
  --evidence ./evidence.json \
  --output ./diagnose.json \
  --badge ./badge.svg \
  --attach-to-registry registry-id
```

Verdict thresholds (composed in `compose_report`):

- `≥ 0.85` → **OK**
- `≥ 0.60` → **MINOR**
- `< 0.60` → **MAJOR**

Output: a frozen `FailureReport` (`run_id` / `base` / `adapter` / `scores` / `overall` / `soup_version` / `extras`) plus an embeddable SVG badge from `render_badge_svg`, one cell per probe (html-escaped — safe for HF model cards). Missing modes fill via `neutral_score`.

## `soup train --diagnose-gate`

```bash
soup train --diagnose-gate ./evidence.json
```

Refuses the final checkpoint save on a `MAJOR` regression (`typer.Exit(code=2)`). The new `diagnose_report` artifact kind is registered in the v0.26 registry alongside `eval_suite` and `canaries` from v0.55.

## See also

- [Eval-gated training](/docs/eval-gate) — pre-training gate at epoch boundaries
- [Quant-check](/docs/quant-check) — quant-specific regression check
- [Eval design](/docs/eval-design) — design the evidence your gate scores
- [Eval depth (v0.65)](/docs/eval-depth) — 4 deeper failure-mode probes (behavior, capability, checklist, irt-subset) that stack on top of the 7 diagnose probes
- [Post-train x-rays (v0.66)](/docs/post-train-xrays) — 4 mechanistic-interpretability probes (sae-diff, sleeper, interference, pack) — failure-mode coverage 6 → 10

[PreviousQuant-Lobotomy Check](/docs/quant-check)[NextPost-train X-rays](/docs/post-train-xrays)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="012-post-train-xrays"></a>

# 12. Post-train X-rays (v0.66.0)

*Source: <https://trysoup.dev/docs/post-train-xrays>*

Mechanistic-interpretability on every fine-tune. Four probe families that surface what \*changed inside\* the model, not just what changed in outputs. Pure descriptive — no auto-mitigation, designed for CI logging and model cards.

## `soup probe sae-diff` — Sparse Autoencoder feature movement

```bash
soup probe sae-diff ./gemma_scope.safetensors ./pre_acts.json ./post_acts.json \
  --top-k 20 --output ./sae_diff.json
```

Encode pre-FT and post-FT activation batches through a Sparse Autoencoder; report the **top-K features** whose mean activation moved the most. Closed SAE-repo allowlist — and as of **v0.71.8** `--auto-download` fetches one from the HF Hub into `~/.soup/sae-cache/` (validated against the allowlist BEFORE any network call, via an SSRF-hardened `snapshot_download`):

- Gemma Scope (2B / 9B / 27B residual-stream)
- EleutherAI Pythia SAEs
- JBloomAus Llama SAEs
- OpenAI GPT-2 SAE

Bounds: top-k `[1, 10K]`, up to 1M features, up to 1M tokens per batch, 16 MiB evidence cap. v0.71.8 also adds `soup probe sleeper --weights`, `soup probe truth` / `harm`, `soup probe interference --measure` (live PEFT multi-adapter N×N matrix), and `soup train --capture-activations`. That last one has a partner flag, **`soup train --capture-prompts <path>`**, which records the prompts the activations belong to; the capture is not much use without them, and the path is cwd-contained and symlink-rejecting like every other write Soup makes.

## `soup probe sleeper` — defection-agent classifier

```bash
soup probe sleeper llama-3-8b --evidence ./activations.json --output ./sleeper.json
```

Calibrated **linear defection probe** (per-base, deterministic) applied to a 2D activation tensor. Reports flagged-token rate and verdict:

| Flagged rate | Verdict |
| --- | --- |
| ≤1% | OK |
| ≤5% | MINOR |
| >5% | **MAJOR** |

Bundled-base allowlist (Llama-3-8B, Gemma-2-9B, …); no evidence → OK report with 0 tokens (matches v0.56 neutral-mode policy). 16 MiB cap; symlink rejection.

## `soup probe interference` — N×N adapter compatibility matrix

```bash
soup probe interference ./losses.json --output ./matrix.json
```

Input is operator-measured per-pair losses; output is an N×N catastrophic-interference matrix:

```
score(A → B) = (loss(A_target | A+B) - loss(A_target | A alone)) / loss(A alone)
```

|  | score |  | Verdict |
| --- | --- | --- | --- |
| <5% | OK |
| <20% | MINOR |
| ≥20% | **MAJOR** (exit 2, gates CI) |

Bounds: 2..16 adapters (4..256 pairs). Adapter names ≤256 chars; markup-escaped before render against injection.

## `soup probe pack` — bundled probes per base

```bash
soup probe pack llama-3-8b --output ./pack.json
soup probe pack --list
```

Per-base manifest of calibrated probes (sleeper / sae / truth / harm). Metadata only — no weights embedded (v0.66 ships schema; weights fetcher shipped in v0.71.8). 1..32 probes per pack; per-field caps against operator-controlled-input bloat.

## Live influence-function blame

Bundled in v0.66 alongside the probe family: a **DataInf-style row attribution** runner that walks training data, computes per-example influence on a target output, and ranks the most causal rows. Composes with v0.67 `soup adapters bisect` — bisect tells you \*which checkpoint\* broke, blame tells you \*which rows\* caused it.

## See also

- [Diagnose](/docs/diagnose) — v0.56 6-probe report card; v0.66 adds 4 more probes on top.
- [Adapter lifecycle](/docs/adapter-lifecycle) — v0.67 bisect uses v0.66 blame for row-level attribution.

[Previoussoup diagnose: post-training model report card](/docs/diagnose)[NextTracker & Eval Pro](/docs/tracker-eval-pro)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="013-tracker-eval-pro"></a>

# 13. Tracker & Eval Pro (v0.43.0)

*Source: <https://trysoup.dev/docs/tracker-eval-pro>*

## `--tracker` allowlist

Closed allowlist: `wandb` | `tensorboard` | `mlflow` | `swanlab` | `trackio` | `none`.

```bash
soup train --tracker mlflow
```

Mutually exclusive with legacy `--wandb` / `--tensorboard` via `resolve_report_to`.

## Telemetry: opt-in, hardware-only, and still sending nothing

v0.43.0 landed a telemetry **schema** and the environment variables that would configure it, and for many releases that was all there was: the primitives existed and no command called them. **v0.75.0 wired it**, together with the public privacy policy that had been the stated precondition.

Three things have to be true before a byte leaves your machine, and as shipped the third one is false.

**1. You have to opt in.** It is off unless `SOUP_TELEMETRY=1` (or `true`, `yes`, `on`). Unset, or set to anything else including `0`, means no payload is built and the disk is never touched.

**2. You can turn it off per invocation.** `--no-telemetry` is a global flag on every command, and it overrides the environment variable. It is checked twice, once as the parsed option and once as a raw scan of `argv`, so it still works if callback parsing never ran.

**3. The bundled project key is a placeholder, and the code refuses it.** The key compiled into the wheel is `phc_soup_public_write_only`, which the sender tests for by name. On a match it writes `Notice: telemetry is not yet live.` to stderr and returns **without opening a socket**. So the shipped binary transmits nothing even for a user who opted in. An operator who wants their own collection sets `SOUP_POSTHOG_KEY` **and** `SOUP_POSTHOG_ENDPOINT` together, and that endpoint must be HTTPS and must pass the same SSRF policy the rest of the CLI uses.

What the payload would carry, if all three held, is seven fields and nothing else:

```text
soup_version       the running version
command            the top-level command, checked against the registered
                   command list and masked to "(unknown)" otherwise
python             major.minor only
os                 platform.system()
arch               platform.machine()
duration_seconds   how long the command took
distinct_id        a random UUID4 generated locally, stored at
                   ~/.soup/telemetry_id purely to deduplicate events
```

The published policy also states what is **never** collected: dataset paths or contents, model names or architectures, config contents or hyperparameters, usernames or local paths, IP addresses, tokens or credentials. Delete `~/.soup/telemetry_id` and a new one is generated on the next opt-in. The upload is a fire-and-forget HTTPS POST at command exit with a one-second connect and read timeout, and every network and filesystem exception is swallowed, so telemetry cannot fail or delay a run.

The authoritative text is upstream's own [privacy policy](https://github.com/MakazhanAlpamys/Soup/blob/main/docs/backends-and-ops.md#privacy-policy), a section of the backends and ops document rather than a separate file, plus the network-egress section of `SECURITY.md`.

## NLG metrics

Pure-Python BLEU + ROUGE-1/2/L + `effective_tokens_per_second`. Closed allowlist `NLG_METRICS = frozenset({"bleu","rouge_1","rouge_2","rouge_l"})`.

## KL-divergence calibration

```bash
soup eval quant-check --before old.json --after new.json --tasks t.jsonl
```

Classifies the KL delta as OK / MINOR / MAJOR at 0.05 / 0.20 thresholds (mirrors quant-check).

## Model Arena (Elo)

An A/B tournament with Elo ratings: K=32 default, 256-model cap, 1M-match cap, and `Tournament.ratings` returns a `MappingProxyType` so a caller cannot mutate the table.

> **Library only, no CLI surface.** It ships as `soup_cli.eval.arena` and is used from Python. There is no `soup eval arena` subcommand; `soup eval` registers `benchmark`, `custom`, `judge`, `auto`, `compare`, `leaderboard`, `human`, `gate`, `quant-check`, `design`, `discover`, `lock`, `coverage`, `against`, `gate-install`, `unlearning`, `behavior`, `capability`, `checklist`, `irt-subset`, `citation` and `aider` (v0.74.0). For a pairwise verdict from the CLI, use [`soup ship --task-mode pairwise`](/docs/soup-ship).

## New benchmarks

`ceval`, `cmmlu`, `aider_polyglot` (live Aider Polyglot runner v0.43.1).

## Profiling helpers

- `memory_snapshot_context` — CUDA `torch.cuda.memory._record_memory_history` wrapper
- `detect_anomaly_context` — `torch.autograd.set_detect_anomaly` wrapper
- `nccl_bandwidth_check` — reference table for h100 / a100 / v100 / rtx40-series (OK ≥80% / MINOR ≥50% / MAJOR <50%)

## VS Code launch.json writer

Writes `.vscode/launch.json` with cwd containment and a symlink TOCTOU guard. It ships as a **library helper with no CLI surface**: `soup_cli.utils.vscode_setup.write_launch_json` has no caller in the shipped code, and `soup doctor`'s own flags are `--nccl`, `--disk` and, since v0.75.0, `--config` — none of which writes a launch.json. Treat it as available to a script, not as a command.

## soup data demo

4-bundle frozen registry: `alpaca_demo` / `sharegpt_demo` / `dpo_demo` / `grpo_demo`. Atomic copy via sibling temp file + `os.replace`.

```bash
soup data demo alpaca_demo --output ./train.jsonl
```

[PreviousPost-train X-rays](/docs/post-train-xrays)[NextTraining Methods](/docs/training)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="014-training"></a>

# 14. Training Methods

*Source: <https://trysoup.dev/docs/training>*

Soup supports **23 training tasks** via the `task` config key. That number is the exact cardinality of the `task` field in the config schema, not a marketing round-up: the full list is in [All Training Tasks](#all-training-tasks) below. Switching method means changing one line of YAML, not changing tools.

`soup edit set` (ROME / MEMIT / AlphaEdit) and `soup steer train` (CAA / ITI / RepE) are **not** `task:` values. They are weight-surgery and inference-time commands, documented under [Unlearning & knowledge editing](/docs/unlearning) and [RAG & steering](/docs/rag-and-steering).

> **If the model does not fit in your card**, add `training.stream_layers: true` and the frozen base never enters VRAM at all. That works for `sft` and, since v0.72.4, for `dpo`, `orpo`, `simpo` and `kto`, with DPO's reference model taken from the same stream with its adapters switched off, so it costs no extra weights. See [Layer streaming](/docs/layer-streaming) and [Preference losses over streaming](/docs/streaming-preference).

## Supervised Fine-Tuning (SFT)

The most common method. Train on instruction-response pairs.

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft

data:
  train: ./data/train.jsonl
  format: alpaca

training:
  epochs: 3
  lr: 2e-5
  batch_size: auto
  quantization: 4bit
  lora:
    r: 64
    alpha: 16
```

## Direct Preference Optimization (DPO)

Train with preference pairs (chosen vs rejected).

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: dpo

data:
  train: ./data/preferences.jsonl
  format: dpo

training:
  dpo_beta: 0.1
  quantization: 4bit
  lora:
    r: 64
    alpha: 16
```

## Group Relative Policy Optimization (GRPO)

Reasoning training (DeepSeek-R1 style) with reward functions instead of a reward model.

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: grpo

data:
  train: ./data/reasoning_train.jsonl
  format: sharegpt
  max_length: 4096

training:
  grpo_beta: 0.1
  num_generations: 4
  reward_fn: accuracy     # or 'format', or path to custom .py
  quantization: 4bit
  lora:
    r: 64
    alpha: 16
```

**Built-in reward functions:**

- `accuracy` — checks if the final answer matches expected (supports `####` and `\boxed{}` formats)
- `format` — checks for structured `<think>...</think>` reasoning blocks

**Custom reward functions** — point to a Python file:

```python
# my_reward.py
def reward_fn(completions, **kwargs):
    # kwargs carries your dataset's own columns, row-aligned with completions.
    golds = kwargs["answer"]
    return [1.0 if g in c[-1]["content"] else 0.0 for c, g in zip(completions, golds)]
```

**What is in `kwargs`.** Source columns are preserved and passed through, and the trainer additionally exposes the target as `answer`: an alpaca `output`, or the final assistant turn of a chat row. Required columns are validated **before generation starts**, so a missing one refuses the run rather than producing a silently useless reward: `accuracy` and the verifiable `math` domain need `answer`, verifiable `code` needs `expected` or `answer`, and `json_schema` needs `schema`.

## PPO / Full RLHF Pipeline

Three-step pipeline: SFT warmup -> Reward Model -> PPO alignment.

```yaml
# Step 3: PPO alignment
base: meta-llama/Llama-3.1-8B-Instruct
task: ppo

data:
  train: ./data/prompts.jsonl
  format: chatml

training:
  reward_model: ./output_rm   # From step 2
  ppo_epochs: 4
  ppo_clip_ratio: 0.2
  ppo_kl_penalty: 0.05
  quantization: 4bit
  lora:
    r: 64
    alpha: 16
```

## All Training Tasks

All 23, exactly as the schema accepts them.

| Task | Data | Use Case |
| --- | --- | --- |
| **sft** | alpaca/sharegpt/chatml/llava | Instruction tuning |
| **dpo** | prompt+chosen+rejected | Preference alignment |
| **online\_dpo** | prompts + a judge **or** a reward model | On-policy preference with a judge in the loop ([v0.71.31](/docs/online-dpo)) |
| **grpo** | prompts + reward fns | Reasoning (DeepSeek-R1); a [PRM can score every step](/docs/prm-guided-grpo) |
| **ppo** | prompts + reward model/fn | Full RLHF stage 3 |
| **kto** | prompt+completion+label | Unpaired preference |
| **bco** | prompt+completion+label | Binary classifier optimization |
| **orpo** | prompt+chosen+rejected | Reference-free alignment |
| **simpo** | prompt+chosen+rejected | Length-normalized preference |
| **ipo** | prompt+chosen+rejected | Regularized preference |
| **preference** | any preference format | Unified dispatcher; picks the loss for you |
| **reward\_model** | prompt+chosen+rejected | RLHF stage 2 |
| **prm** | step-labelled reasoning (`prm`) | Process reward model, graded per step |
| **pretrain** | plaintext (raw text) | Continued pre-training |
| **embedding** | anchor+positive(+negative) | Sentence embeddings |
| **classifier** | text + label (`num_labels`) | Sequence classification. `training.classifier_kind` picks `single_label` (default) or `multi_label`; `training.classifier_lora: true` adapts the head with LoRA instead of full fine-tuning |
| **reranker** | query + document + label | Reranking |
| **cross\_encoder** | pair + label | Cross-encoder scoring |
| **distill** | data + a `teacher_model` | Knowledge distillation, incl. cross-tokenizer ULD and MiniLLM |
| **unlearn** | a forget set | [NPO / SimNPO / RMU removal](/docs/unlearning) |
| **tts** | audio | Text-to-speech (BETA, hardware-gated) |
| **asr** | `{"audio": path, "text": transcript}` | [Whisper fine-tuning with WER/CER](/docs/asr-fine-tuning) (v0.71.32) |
| **moe\_lora\_routing** | alpaca/sharegpt | MoLE per-token gating over N task LoRAs (v0.67) |

## Running Training

```bash
# Start training
soup train --config soup.yaml

# Resume from checkpoint
soup train --config soup.yaml --resume auto
soup train --config soup.yaml --resume ./output/checkpoint-500

# With W&B logging
soup train --config soup.yaml --wandb

# With TensorBoard
soup train --config soup.yaml --tensorboard

# With DeepSpeed (multi-GPU)
soup train --config soup.yaml --deepspeed zero2

# With FSDP2
soup train --config soup.yaml --fsdp full_shard

# Skip confirmation
soup train --config soup.yaml --yes

# Continual learning: rehearse an old dataset so the new task
# does not erase it (v0.71.36, sft/pretrain only)
soup train --config new_task.yaml --replay old_task.jsonl --replay-ratio 0.1
```

`--replay` interleaves a seeded sample of `old_task.jsonl` into training; `--replay-ratio` is the fraction of the final mixed set. Validation stays pure new-task. See [Data Moat II](/docs/data-moat-ii) for the full mechanism and its measured limits.

[PreviousTracker & Eval Pro](/docs/tracker-eval-pro)[NextBackends & Performance](/docs/backends)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="015-backends"></a>

# 15. Backends & Performance

*Source: <https://trysoup.dev/docs/backends>*

Soup has three training backends: `transformers` (default), `unsloth` (2-5x faster on CUDA), and `mlx` (native Apple Silicon, new in v0.25.0).

## Apple Silicon MLX Backend (v0.25.0)

Train on M1–M4 Macs without CUDA or emulation:

```bash
pip install "soup-cli[mlx]"
```

```yaml
base: mlx-community/Llama-3.1-8B-Instruct-4bit
backend: mlx
task: sft       # sft ONLY: the MLX backend refuses every other task
```

See the [MLX backend guide](/docs/mlx-backend) for supported tasks, diagnostics, and MLX-native recipes.

## Unsloth Backend (2-5x Faster Training)

Use the Unsloth backend for significantly faster training and up to 80% less VRAM:

```bash
pip install "soup-cli[fast]"
```

Add one line to your config:

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft
backend: unsloth    # 2-5x faster, -80% VRAM

data:
  train: ./data/train.jsonl
  format: alpaca

training:
  epochs: 3
  lr: 2e-5
  quantization: 4bit
  lora:
    r: 64
    alpha: 16
```

Works with all training tasks: SFT, DPO, GRPO, PPO, KTO, ORPO, SimPO, IPO, and Pretrain.

> **Tip:** Soup auto-detects unsloth. When installed, you'll see a hint during `soup train` if you haven't enabled it yet.

## Performance Optimizations

```yaml
training:
  use_liger: true             # Liger Kernel fused ops (20-60% memory savings)
  use_flash_attn: true        # FlashAttention v2/v3 auto-detection
  gradient_checkpointing: true  # Required for long sequences
```

Install optional packages:

```bash
pip install "soup-cli[liger]"       # Liger Kernel
pip install flash-attn --no-build-isolation  # FlashAttention
pip install "soup-cli[ring-attn]"   # Ring FlashAttention
```

## Long-Context Training (128k+)

```yaml
training:
  rope_scaling_type: yarn       # linear, dynamic, yarn, longrope
  yarn_factor: 4.0              # yarn only: refused with any other scaling type
  gradient_checkpointing: true
  # use_ring_attention: true    # Sequence parallelism across GPUs

data:
  max_length: 131072            # Up to 1M tokens supported
```

## Multi-GPU Training

### DeepSpeed

```bash
soup train --config soup.yaml --deepspeed zero2          # ZeRO Stage 2
soup train --config soup.yaml --deepspeed zero3          # ZeRO Stage 3
soup train --config soup.yaml --deepspeed zero2_offload  # Stage 2 + optimizer offload
soup train --config soup.yaml --deepspeed zero3_offload  # Stage 3 + CPU parameter offload (v0.73.0)
```

### FSDP2 (PyTorch Native)

```bash
soup train --config soup.yaml --fsdp full_shard    # Like ZeRO-3
soup train --config soup.yaml --fsdp shard_grad    # Like ZeRO-2
soup train --config soup.yaml --fsdp full_offload  # With CPU offload
```

## No GPU at all: train on a serverless cloud one

The rest of this site is about making a small card work. If you have no card, `--cloud modal` renders a self-contained [Modal](https://modal.com) app from your `soup.yaml` and runs it on a per-second-billed GPU.

```bash
pip install "soup-cli[modal]"    # only needed to submit live

# Plan-only, the DEFAULT: write the stub and print the modal run command.
soup train --config soup.yaml --cloud modal --gpu a100

# Submit live (authenticate once with `modal setup`, or set
# MODAL_TOKEN_ID and MODAL_TOKEN_SECRET).
soup train --config soup.yaml --cloud modal --gpu a100 --cloud-submit
```

`--gpu` accepts `t4`, `l4`, `a10g`, `a100` (the default), `a100-80gb`, `l40s` and `h100`.

**Plan-only is the default and that is deliberate**: nothing is submitted, and nothing is billed, until you add `--cloud-submit`. You get the generated `soup_modal_app.py` and the exact command, so you can read what would run before it does.

Your config is **base64-embedded as data**, not interpolated as code, so nothing in the YAML can execute in the generated stub and no secret is written into it. The image pins `soup-cli[train]` to the version you are running locally, writes the embedded config inside the container, and runs `soup train` on the chosen GPU.

### Lambda Cloud (v0.74.0)

```bash
soup train --config soup.yaml --cloud lambda
```

`--gpu` takes one of exactly four Lambda instance types: `a10`, `a6000`, `a100` and `h100`. That list is shorter than Modal's, so a value that works there (`t4`, `l4`, `a10g`, `l40s`) is refused here. You need `LAMBDA_API_KEY`, `LAMBDA_SSH_KEY_NAME` and `LAMBDA_SSH_PRIVATE_KEY` in the environment, with the public key already registered in your Lambda account; `LAMBDA_REGION` is optional and defaults to `us-tx-1`. Output paths must be relative. **Keep the local controller running until it reports termination**: shutting down the guest does not stop the billing, the controller does.

Plan-only by default, like Modal. The design decision worth knowing is where the credential lives: **the API key never enters the instance**. Termination belongs to a local controller, and its `finally` both terminates the instance and polls to confirm that the termination actually happened, rather than firing the call and assuming. Upstream is explicit that the Lambda and RunPod submission paths still need a paid live-validation pass before either can be described as provider-validated.

## Quantization-Aware Training (QAT)

Train with simulated quantization for better post-quantization quality:

```bash
pip install "soup-cli[qat]"
```

```yaml
training:
  quantization: 4bit
  quantization_aware: true    # Enable QAT
```

QAT is ~5-10% slower training but produces significantly better quality when deploying with aggressive quantization. Not compatible with the unsloth backend.

## Advanced LoRA Variants

### DoRA (Weight-Decomposed LoRA)

```yaml
training:
  lora:
    r: 64
    alpha: 16
    use_dora: true
```

### LoRA+ (Differentiated Learning Rates)

```yaml
training:
  lr: 2e-5
  loraplus_lr_ratio: 16.0    # lr_B = lr x 16
  lora:
    r: 64
    alpha: 16
```

### GaLore (Memory-Efficient Full-Parameter Training)

```yaml
training:
  quantization: none          # Required: incompatible with quantization
  use_galore: true
  galore_rank: 128
  galore_update_proj_gap: 200
  galore_scale: 0.25
```

> **Note:** GaLore requires `quantization: none` and `backend: transformers` (not unsloth).

### NEFTune (Noisy Embeddings)

Add noise to embedding vectors during training for better generalization:

```yaml
training:
  neftune_alpha: 5.0    # Noise magnitude (0.0–50.0, typical: 5–15)
```

NEFTune has been shown to improve instruction-following quality without extra data or compute. Works with all training tasks.

### rsLoRA (Rank-Stabilized LoRA)

Scale LoRA outputs by `1/sqrt(r)` instead of `1/r` for better training at high ranks:

```yaml
training:
  lora:
    r: 128              # Higher ranks benefit most from rsLoRA
    alpha: 64
    use_rslora: true
```

> **Tip:** Combine NEFTune + rsLoRA + Unsloth backend for the best training quality and speed.

## MoE Model Support

Fine-tune Mixture of Experts models (Mixtral, Qwen3-30B-A3B, DeepSeek V3):

```yaml
base: Qwen/Qwen3-30B-A3B
task: sft

training:
  moe_lora: true               # Target expert + attention layers
  moe_aux_loss_coeff: 0.01     # Router load-balancing loss
  quantization: 4bit
```

Soup auto-detects MoE architectures. Works with all training tasks.

### Adapting routed expert tensors directly (v0.74.0)

`moe_lora` targets expert and attention **modules**. Some architectures keep their experts as raw 2-D or 3-D `nn.Parameter` tensors instead, which a module-level target cannot reach, so `lora.target_parameters` adapts those tensors through PEFT:

```yaml
training:
  lora:
    r: 16
    alpha: 32
    dropout: 0                 # required: PEFT cannot wrap a raw parameter with dropout
    target_modules: auto
    target_parameters: auto    # routed gate_up_proj + down_proj tensors
    rank_pattern:
      experts.gate_up_proj: 2
      experts.down_proj: 2
```

`auto` resolves the architecture's registered parameter mapping, currently Qwen4-Exp routed experts, and **fails closed** when an architecture has none; an explicit list of parameter-name suffixes is also accepted, capped at 256 entries. The scope is narrow and every bound is refused when the config is read, not minutes into a run: `task: sft` or `pretrain`, `backend: transformers`, `modality: text`, plain LoRA or rsLoRA with `init_strategy: random` and `use_dora: false`, and **not with `training.stream_layers: true`**, which stays resident-only for now.

Two operational notes upstream states rather than leaves to be discovered: `torch.compile` may recompile or graph-break around parameter wrappers, and a parameter-targeted MoE adapter materializes a contribution for **every** expert at inference, so merge it into the base for deployment unless you need to hot-swap adapters.

## Curriculum Learning (v0.23.0+)

Sort training data by difficulty and train progressively:

```yaml
training:
  curriculum: true
  curriculum_metric: length       # Sort by sequence length
  curriculum_buckets: 5           # 1-20 difficulty buckets
```

## Freeze Training (v0.24.0+)

Freeze bottom layers to reduce compute while preserving base knowledge:

```yaml
training:
  freeze_layers: 16               # Freeze bottom 16 layers
  # freeze_ratio: 0.5             # Or freeze 50% of layers
```

## Loss Watchdog (v0.24.0+)

Automatically stop training if loss spikes or diverges:

```yaml
training:
  loss_watchdog: true
  loss_watchdog_threshold: 5.0    # Stop if loss exceeds threshold
  loss_watchdog_patience: 3       # Wait N steps before stopping
```

## Sample Packing (v0.23.0+)

Pack multiple short samples into one sequence for efficient training:

```yaml
training:
  packing: true                   # Enable sample packing (SFT only)
```

[PreviousTraining Methods](/docs/training)[NextVision & Audio](/docs/multimodal)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="016-multimodal"></a>

# 16. Vision & Audio Fine-Tuning

*Source: <https://trysoup.dev/docs/multimodal>*

## Vision / Multimodal

Fine-tune vision-language models (LLaMA-3.2-Vision, Qwen2-VL, Pixtral):

```bash
pip install "soup-cli[vision]"
soup init --template vision
```

```yaml
base: meta-llama/Llama-3.2-11B-Vision-Instruct
task: sft
modality: vision

data:
  train: ./data/vision_train.jsonl
  format: llava
  image_dir: ./data/images
  val_split: 0.1

training:
  epochs: 3
  lr: 1e-5
  quantization: 4bit
  lora:
    r: 64
    alpha: 16
```

### Vision Data Formats

**LLaVA:**

```json
{"image": "photo.jpg", "conversations": [{"from": "human", "value": "<image>\nDescribe this image."}, {"from": "gpt", "value": "A cat on a mat."}]}
```

**ShareGPT4V:**

```json
{"image": "chart.png", "conversations": [{"from": "human", "value": "<image>\nWhat does this show?"}, {"from": "gpt", "value": "Quarterly revenue."}]}
```

`soup data inspect` automatically shows image statistics (count, formats, missing files) for vision datasets.

## Audio / Speech

Fine-tune audio-language models (Qwen2-Audio, Whisper):

```bash
pip install "soup-cli[audio]"
soup init --template audio
```

```yaml
base: Qwen/Qwen2-Audio-7B-Instruct
task: sft
modality: audio

data:
  train: ./data/audio_train.jsonl
  format: audio
  audio_dir: ./data/audio
  val_split: 0.1

training:
  epochs: 3
  lr: 1e-5
  quantization: 4bit
  lora:
    r: 64
    alpha: 16
```

### Audio Data Format

```json
{"audio": "recording.wav", "messages": [{"role": "user", "content": "Transcribe this audio."}, {"role": "assistant", "content": "Hello world."}]}
```

> Want to fine-tune Whisper itself (speech-to-text, not audio understanding)? That is a dedicated task since v0.71.32: see [ASR fine-tuning](/docs/asr-fine-tuning) (`task: asr`, `format: asr`, built-in WER/CER, whisper-tiny/base train on a 4 GB GPU).

## Continued Pre-training

Continue training on raw text for domain adaptation:

```yaml
base: meta-llama/Llama-3.1-8B
task: pretrain

data:
  train: ./data/corpus.jsonl     # {"text": "..."} or plain .txt files
  format: plaintext
  max_length: 4096

training:
  epochs: 1
  lr: 1e-5
  quantization: 4bit
```

## Embedding Fine-Tuning

Train sentence embedding models with contrastive learning:

```yaml
base: sentence-transformers/all-MiniLM-L6-v2
task: embedding

data:
  train: ./data/embeddings.jsonl
  format: embedding

training:
  embedding_loss: contrastive    # contrastive, triplet, cosine
  embedding_pooling: mean
  embedding_margin: 0.5
  embedding_temperature: 0.05
```

### Embedding Data Format

```json
{"anchor": "What is Python?", "positive": "Python is a programming language."}
{"anchor": "What is Python?", "positive": "A programming language.", "negative": "A type of snake."}
```

[PreviousBackends & Performance](/docs/backends)[NextAutopilot](/docs/autopilot)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="017-autopilot"></a>

# 17. Autopilot

*Source: <https://trysoup.dev/docs/autopilot>*

`soup autopilot` is the zero-config entry point added in v0.25.0. You pass a model, a dataset, and a goal. Autopilot profiles the dataset, model, and GPU, then emits a `soup.yaml` with every hyperparameter chosen and justified.

## Quick start

```bash
soup autopilot \
  --model meta-llama/Llama-3.1-8B \
  --data chats.jsonl \
  --goal chat \
  --gpu-budget 24GB
```

## Inputs

`--model`, `--data` and `--goal` are all required. There is no way to pass a task: choosing one is what Autopilot is for.

| Flag | Meaning |
| --- | --- |
| `--model` / `-m` | Any HuggingFace repo or local path (required) |
| `--data` / `-d` | JSONL dataset (alpaca / sharegpt / chatml / dpo / kto / tool-calling) (required) |
| `--goal` / `-g` | `chat` · `reasoning` · `code` · `classification` · `tool-calling` · `alignment` · `domain-adapt` (required) |
| `--gpu-budget` | VRAM budget (defaults to detected GPU) |
| `--output` / `-o` | Config path (default: `./soup.yaml`) |
| `--dry-run` | Print decisions without writing `soup.yaml` |
| `--yes` / `-y` | Skip the confirmation prompt |

## What Autopilot decides

1. **Task** — maps goal → SFT / DPO / GRPO / pretrain, including the tool-calling format where appropriate. Those four are the whole range: the seven goals above map to `sft` (chat, code, classification, tool-calling), `grpo` (reasoning), `dpo` (alignment) and `pretrain` (domain-adapt).
2. **Quantization** — chooses `none`, `8bit`, or `4bit` based on `model_size × 1.2` vs VRAM.
3. **PEFT** — picks LoRA r=8/16/32 from dataset size, and turns on DoRA when the data is large and the VRAM headroom allows it. It does not select VeRA, and it does not turn LoRA off.
4. **Batch size × grad\_accum** — targets effective batch 16–32, computed from VRAM headroom.
5. **Learning rate** — scales with rank and quantization (e.g. LoRA r=16 → 2e-4, 4bit → ×0.8).
6. **Epochs** — 5 → 3 → 2 → 1 depending on dataset size.
7. **`max_length`** — ceil(p95 × 1.1) clamped to model context.
8. **Perf flags** — auto-enables FlashAttention v2 on Ampere+, Liger Kernel on modern Llama arch, `gradient_checkpointing` for long context, MLX backend on Apple Silicon.
9. **Training intelligence** — turns on forgetting detection and checkpoint intelligence by default.

Every decision is printed with a short reason in a Rich panel, so you can see \*why\* r=16 beat r=32 or why quantization dropped to 4bit.

## Example output

```
╭─ Autopilot Decisions ─────────────────────────────────╮
│ ✓ Quantization: 4bit                                  │
│   reason: 8B model needs ~5GB in 4bit, leaves 19GB    │
│                                                        │
│ ✓ PEFT: LoRA r=16, alpha=32                           │
│   reason: 15k samples — r=16 balances capacity /      │
│           overfitting risk                            │
│                                                        │
│ ✓ Batch size: 4 × grad_accum 8 = effective 32         │
│ ✓ Learning rate: 2e-4                                 │
│ ✓ Epochs: 2                                           │
│ ✓ Max length: 2048 (p95=1820 + 10% margin)            │
│ ✓ Flash Attention v2 (Ampere GPU)                     │
│ ✓ Liger Kernel (modern Llama arch)                    │
│ ✓ Forgetting detection (mini_mmlu)                    │
│ ✓ Checkpoint intelligence (judge metric)              │
│                                                        │
│ Estimated time: 1h 42min                              │
│ Estimated VRAM: 18.2GB / 24GB ✓                       │
╰────────────────────────────────────────────────────────╯
```

## Safety

- Dataset and output paths are resolved and constrained to the working directory (no path traversal).
- GPU budget is bounded to 1GB–1TB; there is no time budget: `--gpu-budget` is the only budget the command accepts.
- Model names are validated against HuggingFace Hub naming rules.
- Model code is never executed during analysis — Autopilot uses HF Hub metadata only.

## See also

- [Training methods](/docs/training)
- [Backends](/docs/backends) — including MLX
- [Training intelligence](/docs/training-intelligence) — forgetting detection + checkpoint quality
- [Recipes](/docs/recipes) — start here if you don't need Autopilot

[PreviousVision & Audio](/docs/multimodal)[NextApple Silicon MLX](/docs/mlx-backend)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="018-mlx-backend"></a>

# 18. Apple Silicon MLX Backend

*Source: <https://trysoup.dev/docs/mlx-backend>*

Soup v0.25.0 adds a native MLX training backend for M1 to M4 Macs, running on unified memory without CUDA, Rosetta, or x86 emulation. **Supervised fine-tuning is the only task it supports**: every other task, DPO and GRPO included, is refused at config load. See the table below.

## Install

```bash
pip install "soup-cli[mlx]"
```

This pulls `mlx>=0.20` and `mlx-lm>=0.31.3` as optional dependencies. The `mlx-lm` floor was raised in v0.73.1, to the version the MLX supervised path is actually built against.

## Enable the backend

Set `backend: mlx` in `soup.yaml`, or pass `--backend mlx` to `soup train`:

```yaml
base: mlx-community/Llama-3.1-8B-Instruct-4bit
backend: mlx
task: sft

data:
  train: data.jsonl
  format: chatml

training:
  epochs: 3
  lr: 1e-4
  batch_size: 2
  lora:
    r: 16
    alpha: 32
```

## Supported tasks

| Task | MLX | Notes |
| --- | --- | --- |
| sft | ✓ | LoRA and QLoRA (mlx-community 4bit models) |
| dpo | – | Refused at config load: upstream mlx-lm exposes no training helper. Use `backend: transformers` |
| grpo | – | Refused at config load, same reason |
| ppo | – | Refused — use the transformers backend |
| reward\_model | – | Refused at config load, same reason |
| embedding | – | Refused at config load, same reason |
| pretrain | – | Refused at config load, same reason |

The MLX backend supports `sft` and nothing else: every other task is rejected by the same cross-validator, with the same message, before anything loads. The rows above differ in what you would use them for, not in how they fail.

## Diagnostics

```bash
soup doctor
```

On Apple Silicon this reports `Backend: MPS (Apple Silicon)` and whether it is available. It does **not** report the MLX version, the chip name, unified memory or a recommended batch size: the helper that would fill those in has no caller, which is the known limitation stated at the end of this page. `soup doctor --config soup.yaml` is the part of this command that does know about MLX, and it is [documented below](#soup-doctor---config-the-settings-your-backend-does-not-read).

**Since v0.73.3, device detection knows this backend exists.** Before that, `detect_device()` only probed PyTorch MPS and fell back to `cpu`, so an MLX run announced "CPU (no GPU detected)" — and the label was never the harm. That fallback also fired a "4bit quantization is not supported on CPU" warning and **silently rewrote `quantization: 4bit` to `none`**, on every MLX run that asked for 4-bit. With `backend: mlx` set, detection now resolves to MLX with the chip name, reports Apple unified memory in telemetry, and preserves `4bit` for pre-quantized `mlx-community` checkpoints, which is a different thing from bitsandbytes NF4 and was never what that warning was written about. The CUDA-shaped analytical VRAM pre-flight is also skipped on this path, because Apple unified memory is managed by Metal rather than by a fixed VRAM pool.

Also since v0.73.3: `[mlx]` is a **self-contained install** for supervised fine-tuning on local JSONL, JSON or CSV data, so you never need the PyTorch stack just to train on a Mac. **Since v0.74.0 you may combine them**: `pip install "soup-cli[train,mlx]"` resolves, because both extras now declare the same `transformers>=5.16.1,<6.0.0` floor. Before that release the two declared ranges that could not be satisfied together at all, so the combination was not a style preference but an outright resolver failure. `[train]` is still the PyTorch and TRL stack the Transformers backend uses. A Hugging Face Hub or streaming dataset still needs `datasets`, because that data source owns the dependency; a local file path does not.

## MLX-native recipes

- `llama3.1-8b-sft-mlx` — M2+ 16GB. Measured on an **8 GB M1** too: 48 iterations in 71 s at a **5.154 GB peak**, adapter written and reloadable
- `qwen3-8b-sft-mlx` — M2+ 16GB. Its repo ID was broken until v0.75.0, pointing at `mlx-community/Qwen3-8B-Instruct-4bit`, which does not exist; it now names `mlx-community/Qwen3-8B-4bit`
- `gemma3-4b-sft-mlx` — M1+ 16GB. **Renamed in v0.75.0**, from `gemma3-9b-sft-mlx`: there is no 9B Gemma 3, so the old name pointed at a repository that raised `RepositoryNotFoundError`. It now names `mlx-community/gemma-3-4b-it-4bit`

Use any of them with `soup recipes use <name>`. The old `gemma3-9b-sft-mlx` name exits 1.

> **`qwen3-8b-sft-mlx` behaves differently after v0.75.0, and the change is a refusal rather than a regression.** It does not set `data.train_on_responses_only`, so it takes the `true` default, which reached nothing on this backend until now. Qwen3's chat template injects its thinking block only for the **last** assistant turn, which means partial renderings are not prefixes of the full one and MLX cannot build a per-token mask it can vouch for. Single-turn and system-plus-single-turn rows train as before; **multi-turn rows are now refused at dataset construction**, before the training loop starts, with a message naming `data.train_on_responses_only: false` as the remedy. Set that to restore the old behaviour on multi-turn Qwen3 data, knowing it trains on the prompt. `llama3.1-8b-sft-mlx` and `gemma3-4b-sft-mlx` mask correctly on both shapes and are unaffected.

## The six options this backend accepted and never read

**v0.75.0 is the release named for this page.** Six training options were validated by the schema, documented in these pages, accepted by the config loader, and then read by nothing on `backend: mlx`. The same `soup.yaml` trained a different recipe on Apple Silicon than it did on a CUDA box, silently, and nothing warned.

| Option | What actually happened before v0.75.0 |
| --- | --- |
| `data.train_on_responses_only` | Defaults to `true` and reached nothing, so **every MLX run trained on system and user turns**, and the adapter metadata recorded `mask_prompt: false` regardless |
| `training.optimizer` | Every run built a bare `AdamW`. All 32 allowlisted names became AdamW |
| `training.scheduler` | No schedule at all: a constant learning rate, whatever the recipe said |
| `training.warmup_ratio` | Ignored, for the same reason |
| `training.weight_decay` | Ignored |
| `training.max_grad_norm` | Ignored. The documented default clips every transformers run at 1.0; on MLX nothing clipped anywhere, and the `MLX backend ignores:` advisory did not even mention it |
| `training.gradient_accumulation_steps` | mlx-lm's own dataclass default of 1 always applied, so the effective batch size and the optimizer-update cadence were not the ones you configured. `adapter_config.json` also hardcoded `1`, so the drift was not detectable from the output afterwards |
| `training.gradient_checkpointing` | mlx-lm's default of `False` always applied, giving up the memory saving you enabled it for. `adapter_config.json` hardcoded `false` here too |

All of them are honoured now, and three of the consequences are worth stating with their measurements rather than in the abstract.

**Response-only masking is not comparable between the two backends, and MLX is the stricter one.** Setting mlx-lm's own flag was not the fix: it masks a single prefix ending before the last message, so on multi-turn chat it supervises only the final assistant turn. Measured on Apple Silicon over 16 two-turn conversations: **772 supervised tokens unmasked, 71 with upstream's flag, 146 with a correct mask.** Soup injects its own per-token mask for chat rows, uses upstream's flag for prompt-and-completion rows where it is correct, and warns on plain-text rows because upstream raises there. MLX **excludes the assistant header** from the loss where the transformers path includes it, and MLX **refuses** a chat template whose partial renderings are not prefixes of the full one rather than approximating. `data.train_on_messages_with_train_field` and `data.train_on_prompt` have no MLX equivalent and now appear in the `MLX backend ignores:` line instead of vanishing.

**`max_grad_norm` rescues a specific failure, not every run.** One M1 step on a deliberately ill-conditioned batch moved SGD weights by **388.03 unclipped against 0.0085** at `max_grad_norm: 1.0`. AdamW moved **0.126505 against 0.126504**, because Adam normalises by its second moment anyway. So this matters for `optimizer: sgd` and for gradient spikes, and barely registers on an Adam-family run. The norm that actually ran is recorded in `adapter_config.json`.

> **Upgrade note, and it applies to anyone who never touched the field.** `gradient_accumulation_steps` defaults to **4**. An MLX run that used to update the optimizer on every micro-batch now accumulates over four first: a **4x larger effective batch size and roughly a quarter as many optimizer updates** for the same `iters`. That is the schema default finally taking effect, so a differently-converging run after upgrading is **expected rather than a regression**. `iters` is also rounded down to a whole number of accumulation groups, with a floor of one group, because mlx-lm only updates on `it % accum == 0` and never flushes a trailing partial group: without that, a dataset smaller than the accumulation window trained for **zero** optimizer updates.

## Optimizers and schedules

Soup's optimizer allowlist is far wider than anything MLX ships, so most valid values have no equivalent here. Since v0.75.0 a value MLX cannot express is **refused by name** when the optimizer is built, rather than silently becoming AdamW.

| Setting | Accepted on MLX |
| --- | --- |
| `training.optimizer` | `adamw_torch`, `adamw_hf`, `adamw_torch_fused`, `sgd`, `adafactor`, `adagrad`, `rmsprop`, `muon` — eight of the thirty-two on Soup's allowlist |
| `training.scheduler` | `cosine`, `linear`, `constant`, `constant_with_warmup` |
| `training.weight_decay` | Any value, except that a non-zero decay on `adagrad` or `rmsprop` is refused, because those MLX constructors take no `weight_decay` at all and dropping it silently is the bug this module exists to fix |

Run a recipe that needs anything else on `backend: transformers`.

**The schedule is built in optimizer-update units, not iterations**, because that is what MLX drives a callable learning rate from. Your real warmup is `warmup_ratio x (iters // gradient_accumulation_steps)`; building it against iterations would stretch the warmup by the accumulation factor and never reach the cosine floor. Measured on Apple Silicon, a `cosine` run with `warmup_ratio: 0.2` now reports **10 distinct learning rates across 40 iterations** where the old path reported one. A `warmup_ratio` that rounds to zero updates says so.

The effective plan is written into `adapter_config.json` — `optimizer`, `scheduler`, `warmup_updates`, `total_updates`, `weight_decay`, `peak_lr` — so what ran is recoverable from the output directory rather than inferred from the recipe.

## This backend now drives the dashboard, the tracker and the stream

`MLXSFTTrainerWrapper.train()` accepted `display`, `tracker` and `run_id` and discarded them, so an MLX run showed mlx-lm's raw stdout while the same config on the transformers path got the Rich panel. Since v0.75.0 it drives all three: the live terminal dashboard, the `soup ui` SSE stream and the SQLite experiment tracker.

It is an adapter rather than a reuse of the transformers callback, and the reason is worth knowing: mlx-lm exposes only `on_train_loss_report` and `on_val_loss_report`, so bridging through a Hugging Face `TrainerCallback` would have meant faking trainer state. Two deliberate consequences: `speed` carries `iterations_per_second` to match the transformers path, because the panel hard-labels that field `it/s`; and **`grad_norm` is left unset**, because mlx-lm does not compute one and a field reading a plausible `0.0` on one backend is worse than an absent one. Verified against real mlx-lm on an 8 GB M1.

**Validation loss is recorded at all for the first time**, on every backend, and MLX produces it too. Before v0.75.0 the callback read the training loss and never the evaluation loss, so an evaluation step left the last training loss in place and re-reported it: the evaluated number existed nowhere. The live panel gains a `Val loss` row, and the `metrics` table and the SSE frame each carry `val_loss` as **its own series, never folded into `loss`**. The panel carries the last measured value forward between evaluations; the stored and streamed values do not, so a step where no evaluation ran records `NULL` and a series read back has one point per measurement rather than one per logged step. Existing `~/.soup/experiments.db` files are migrated in place, and rows written before this ship read `NULL` rather than a fabricated `0.0`, because an unmeasured value must not read as a measured one.

## `soup doctor --config`: the settings your backend does not read

```bash
soup doctor --config soup.yaml
```

A field can be declared, validated and documented and still be read by nothing on the backend you chose. That is what this whole page is about, and v0.75.0 added the command that tells you **before** the run instead of during it.

It loads the config, prints `Config check - task=<t> backend=<b>`, and then either says every setting this config writes is read, or lists the ones that are not, with the reason and the issue that recorded it. Only fields you actually set are listed, never the ones sitting at a schema default: a wall of hundreds of rows is not a pre-flight check.

**The scope is deliberately narrow, and that is the honest framing.** The table covers `task: sft` on `backend: mlx`, **seven entries**, and every other task-and-backend pair reports nothing rather than guessing. Every one of those seven is already something `mlx_sft.py` warns about at runtime, so the value added is the timing, not new knowledge. Backend support is **declared by hand rather than inferred**, because inference does not work: reachability over the import graph detected none of five independently-known MLX gaps, reading the trainer module alone invents gaps for fields that live in helper modules, and `--dry-run` exits before a trainer is ever constructed. A guard keeps the table honest in both directions, so an entry marked unread fails the suite once any declared module reads the field.

`soup doctor --config` exits **2** when the config cannot be read, parsed or validated — all three deliberately agree, so this leg can gate CI — and `soup doctor` exits **1** when a required core dependency is missing or out of range, while the optional `[train]` group stays advisory.

> **Two disclosures upstream publishes with it, and they belong here.** Five entries were removed from that table before merge, because the same release wired those fields — the guard is what noticed. And the all-clear message **overclaims**: the field-consumer guard behind it catches a field nothing reads, not a field something reads wrongly, and CUDA-only kernels such as `use_liger` are unread on MLX and absent from the table entirely. Read "every setting is read" as "nothing in the declared table is unread", which is a narrower statement.

## Limitations

- Single-device only, no distributed MLX training.
- Base models must be MLX-format (typically from the `mlx-community` HF org).
- `bitsandbytes` is unused on this backend: quantization comes from the MLX model itself.
- Unsloth backend is not MLX-compatible (they're separate execution paths).
- **Apple Silicon streaming and MPS training are experimental.** v0.74.0 turned on BF16 autocast for hardware-validated resident supervised, DPO, reward-model, PRM and GRPO training on capable MPS runtimes behind a live capability probe, with the process-reward path deliberately keeping fp32 master weights to avoid a fatal Metal optimizer dtype mismatch, and unvalidated MPS and CPU staying fp32. Layer streaming keeps its host store genuinely on the CPU there, refusing any allocation that is not real CPU memory, and preserves a BF16 checkpoint instead of silently doubling the store and disk cache to FP32. No claim is made that streaming fits a larger model or runs faster than resident MPS training, and `backend: mlx` is still rejected with `stream_layers` because they are separate model-loading paths.
- **It reads neither `training.seed` nor `training.data_seed`.** Setting either is a warning, not a rejection, because a config valid on transformers should not become unloadable by switching backend. Seeding MLX for real needs a separate generator and is separate work. See [seeds and reproducibility](/docs/seeds-and-reproducibility).

### If you resumed an MLX run before v0.74.0, it started from scratch

`--resume auto` and a direct `--resume <path>` only recognised `checkpoint-N` directories, which is the shape the transformers and Unsloth paths write. `mlx-lm`'s tuner saves step-numbered `NNNNNNN_adapters.safetensors` files instead, so an MLX run's own output **never matched, and training silently restarted from zero every time**.

The located checkpoint's adapter weights are loaded before training starts now, and what that is, is stated plainly: **a weights-only warm start, not a full resume.** `mlx-lm`'s LoRA trainer exposes no optimizer state and no step count, so the step counter and the data position both restart at zero however far the checkpoint got, and the run says so rather than implying otherwise. The same fix also covers a config with `experiment_name` set, which the first attempt missed.

> **Known limitation, still open at v0.75.0: `soup doctor` never reports MLX.** The MLX version always reads `unknown`, because `_get_mlx_info()` is defined in the doctor command and called from nowhere. It was filed during v0.74.0 and did not ship in v0.75.0 either, so this is now two releases old. `soup doctor --config soup.yaml` is unaffected: that leg reads the config rather than the runtime.

### If you trained on this backend before v0.73.1, re-run it

Two defects meant an MLX run could complete successfully and be worthless, and both are repaired in [v0.73.1](/docs/free-gpu-tier).

- **`backend: mlx` never dispatched to the MLX trainer at all.** It fell through silently to the transformers path. And without a freeze first, what it saved was not an adapter but a full fine-tune: **172 tensors where 24 were expected** on a 1.2B model.
- **The MLX `adapter_config.json` saved `target_modules` unresolved**, as `{"keys": ["auto"]}`. Loading that file dropped **every LoRA tensor without a word**, so generation with the adapter was bit-identical to the base model. Since `auto` is the schema default, this was every MLX run that did not name its modules by hand. The file cannot be repaired after the fact; the run has to be redone.

[PreviousAutopilot](/docs/autopilot)[NextTool-Calling](/docs/tool-calling)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="019-tool-calling"></a>

# 19. Tool-Calling Fine-Tuning

*Source: <https://trysoup.dev/docs/tool-calling>*

Soup v0.25.0 adds an end-to-end pipeline for training models that call functions.

## Data format

A new `tool-calling` format was added to `soup_cli/data/formats.py`:

```json
{
  "messages": [{"role": "user", "content": "What's the weather in Tokyo?"}],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "parameters": {"type": "object", "properties": {"city": {"type": "string"}}}
      }
    }
  ],
  "tool_calls": [
    {"function": {"name": "get_weather", "arguments": "{\"city\": \"Tokyo\"}"}}
  ]
}
```

The detector expects `messages`, `tools`, and `tool_calls` to all be present. Tool definitions are embedded in the system message and `tool_calls` are emitted as assistant turns during normalization.

## Generate tool-call training data

```bash
soup data generate \
  --prompt "Function-calling examples: a user request, then one tool call with arguments" \
  --provider openai \
  --format chatml \
  --count 1000 \
  --output tool_calls.jsonl
```

`--prompt` is required, and `--template` is an allowlist of exactly five: `code`, `conversation`, `qa`, `preference`, `reasoning`. There is **no `tool-calling` template on the CLI**. The bundled builder in `soup_cli/data/templates/tool_calling.py`, configurable across API domains (weather, search, database, filesystem), is a library helper with no command-line selector, in the same way the Elo arena and judge calibration are library helpers. Describe the shape you want in `--prompt` instead.

## Train

Use a ready-made recipe:

```bash
soup recipes use qwen3-8b-tools
soup train
```

Or start from a recipe clone and edit:

```yaml
base: Qwen/Qwen3-8B
task: sft

data:
  train: ./tool_calls.jsonl
  format: tool-calling

training:
  epochs: 3
  lr: 2e-4
  lora: { r: 16, alpha: 32 }
```

## Evaluation

`soup eval custom` ships three tool-call scoring functions:

- `tool_call_match` — exact function name + arguments
- `tool_call_name_match` — function name only
- `tool_call_args_subset` — partial credit for matching a subset of arguments

## Recipes

- `qwen3-8b-tools` — Qwen 3 8B, 4bit, LoRA r=16
- `llama4-scout-tools` — Llama 4 Scout 17B, 4bit, LoRA r=16

## See also

- [Data formats](/docs/data-formats)
- [Autopilot](/docs/autopilot) — `--goal tool-calling` picks this format automatically

[PreviousApple Silicon MLX](/docs/mlx-backend)[NextRLVR: Verifiable Rewards](/docs/rlvr)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="020-rlvr"></a>

# 20. RLVR — Reinforcement Learning from Verifiable Rewards

*Source: <https://trysoup.dev/docs/rlvr>*

v0.25.0 adds deterministic reward signals for GRPO training on math, code, and JSON-schema tasks. No reward model, no human labels.

## Enable it

```yaml
base: Qwen/Qwen3-8B
task: grpo

data:
  train: math_problems.jsonl
  format: chatml

training:
  reward_fn: verifiable
  verifiable_domain: math   # math | code | json_schema
  lr: 1e-5
  epochs: 1
  lora: { r: 16, alpha: 32 }
```

## Built-in reward functions

| Domain | What it does | Sandbox |
| --- | --- | --- |
| `math` | Regex-extracts the final answer, compares numerically with tolerance | pure Python |
| `code` | Executes Python against expected outputs | subprocess, timeout 5s, no network, restricted builtins, 10 KB output cap |
| `json_schema` | Validates output against a JSON Schema and scores completeness | pure Python |

All three live in `soup_cli/trainer/rewards.py` and are routed through the existing GRPO trainer.

## Generate training data

```bash
soup data generate \
  --prompt "Math word problems, each with a single exact numeric answer" \
  --provider ollama --count 500 --output verifiable.jsonl
```

`--prompt` is required, and `--template` accepts only `code`, `conversation`, `qa`, `preference` and `reasoning`; there is **no `verifiable` template and no `--domain` flag** on the CLI. `soup_cli/data/templates/verifiable.py` builds problems with ground-truth answers you can verify at training time, but it is a library helper with no command-line selector.

## Safety

- `code_exec` runs each completion in a short-lived subprocess with no network access and a restricted builtin set.
- `math_verify` never uses `eval()` on model output — answers are extracted by regex.
- `verifiable_domain` is a Pydantic `Literal` so arbitrary strings can't reach the dispatcher.

## See also

- [Training methods](/docs/training) — GRPO
- [Autopilot](/docs/autopilot) — `--goal reasoning` picks RLVR when your data has ground truth

[PreviousTool-Calling](/docs/tool-calling)[NextMulti-GPU Mastery](/docs/multi-gpu)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="021-multi-gpu"></a>

# 21. Multi-GPU Mastery

*Source: <https://trysoup.dev/docs/multi-gpu>*

Soup v0.27.0 turns multi-GPU training from a research paper into a CLI flag. Topology detection picks the right strategy, ZeRO++ lands quantized weights and grads, FSDP2 can opt into `torch.compile`, and pipeline parallelism is scaffolded for models that don't fit a single node.

## One-flag launch

```bash
soup train --gpus auto
soup train --gpus 8
```

`--gpus` inspects GPU count and interconnect (NVLink vs PCIe), then recommends the strategy for your config — DeepSpeed ZeRO-3, ZeRO++, FSDP2, or pipeline. If the topology doesn't match what your config asked for, Soup prints the corrected `accelerate launch` command you can paste.

## ZeRO++

```yaml
base: meta-llama/Llama-3.1-70B
task: sft

training:
  quantization: 4bit
  lora:
    r: 16
    alpha: 32
```

```bash
soup train --gpus 8 --deepspeed zero++
# aliases: zero_pp
```

ZeRO++ cuts inter-GPU communication by quantizing the broadcasted weights and gradients. Integer fields (`sub_group_size`, `stage3_max_live_parameters`, `stage3_max_reuse_distance`) are written as `int(1e9)` so DeepSpeed's strict JSON validator accepts them.

## FSDP2 + torch.compile

```yaml
training:
  use_fsdp2_compile: true
```

```bash
soup train --gpus 4 --fsdp full_shard
```

The validator requires an FSDP preset, CUDA, `backend=transformers`, and `torch>=2.2 + accelerate>=0.27`. DeepSpeed + `torch.compile` is explicitly rejected — the two own their own compile paths and mixing them produces a cryptic runtime crash.

## Pipeline parallelism

```yaml
training:
  parallelism: pipeline
  pipeline_stages: 4
```

The validator requires `pipeline_stages >= 2`, CUDA, and `gpu_count >= pipeline_stages`. `pipeline_stages` is bounded `[1, 16]`.

## DeepSpeed-MII backend

```bash
soup serve --backend mii --model ./output
```

Registered in v0.27.0, live since v0.33.0. A misconfigured `--backend mii` always exits non-zero (never silently accepts).

**v0.74.0 repaired the prompt and the finish reason.** Until then this backend hand-rolled a `System:/User:/Assistant:` prompt and hardcoded `finish_reason` to `stop`, so a served model saw a format it was never trained on and a client could not tell a truncated answer from a completed one. It now applies the model's own chat template through the shared builder and reports the engine's real finish reason. Behaviour is unchanged for a model that ships no chat template. That is the third backend to have carried this same pair, after vLLM in v0.73.0 and SGLang in v0.74.0.

## Multi-GPU recipes

- `llama3-70b-fsdp2` — 70B SFT on 8×A100 via FSDP2 + compile
- `qwen3-32b-zeropp` — Qwen 3 32B SFT via DeepSpeed ZeRO++
- `deepseek-v3-pipeline` — DeepSeek V3 SFT via pipeline parallelism

```bash
soup recipes use llama3-70b-fsdp2
soup train --gpus 8
```

## Security & guardrails

- `--gpus` rejects `bool`, negatives, zero, non-digits, and values above `MAX_GPU_COUNT=128`
- `--gpus auto` on a CPU-only host prints an explicit yellow warning instead of silently single-processing
- The `accelerate launch` argv is built via `shlex.quote` so copy-pasted commands can't inject via a crafted config path
- NCCL env hints are applied via `os.environ.setdefault` — user / launcher overrides always win
- Rich markup on `--config` paths is escaped before embedding in advice panels

## See also

- [Training speed & memory](/docs/training-speed-memory) — Cut CE, FP8, activation offloading
- [Backends](/docs/backends) — transformers / unsloth / MLX

[PreviousRLVR: Verifiable Rewards](/docs/rlvr)[NextSpeed & Memory](/docs/training-speed-memory)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="022-training-speed-memory"></a>

# 22. Training Speed & Memory

*Source: <https://trysoup.dev/docs/training-speed-memory>*

Soup v0.28.0 ships six production-grade throughput + memory features. All six were SFT-only in v0.28, a gate lifted in v0.33 and finished in v0.35 — non-SFT trainers are rejected at config-load time, so there are no silent no-ops.

> **If the model does not fit at all, none of these six is the answer.** They shave a resident run; they cannot make a model smaller than your card. For that, see [layer streaming](/docs/layer-streaming): the frozen base never loads resident, so peak VRAM is bounded by one decoder layer instead of the whole model, and Llama-3.1-8B fine-tunes on a 4 GB card. Since v0.72.4 that covers [preference losses](/docs/streaming-preference) too, not just supervised fine-tuning. It is BETA, and it is slower than resident training, so reach for it only when resident training is impossible.

## Cut Cross-Entropy

```yaml
training:
  use_cut_ce: true
```

Cut CE avoids materialising the full `[seq_len × vocab_size]` logits tensor during the cross-entropy backward pass. Biggest win on models with vocab ≥ 128k (Llama 3, Qwen 3). Architecture detection reads `config.model_type` first, so a local checkpoint directory resolves as correctly as a hub id; a substring match on the last path component (`model_name.rsplit("/", 1)[-1]`) is only the fallback when no config can be read. That order was the v0.74.0 repair: before it, name matching came first, so a `soup merge` output called `checkpoint-2000` matched nothing and cut-cross-entropy stayed off on a flag you had explicitly set. It also means org prefixes, so org prefixes like `deepseek-ai/...-phi-...` can't trigger the wrong patcher.

Install the optional dep:

```bash
pip install "soup-cli[cce]"
```

## FP8 training (Hopper+)

```yaml
training:
  quantization_aware: fp8
```

Configures float8 linear layers via torchao. The validator requires CUDA, a Hopper+ GPU (SM capability check), and the transformers backend. Pydantic accepts only `true` / `false` / `"fp8"` — unknown strings like `"fp16"` are rejected at config load.

## Tiered gradient checkpointing

```yaml
training:
  gradient_checkpointing: auto   # or: selective | medium | full
```

| Tier | Memory saved | Throughput cost |
| --- | --- | --- |
| `selective` | Small | ~5% |
| `medium` | Medium | ~15% |
| `full` | Large | ~30% |
| `auto` | Auto-picked from detected VRAM | — |

`resolve_gradient_checkpointing` returns only HF-supported keys. Granularity is exposed via a separate helper so private markers never leak into `TrainingArguments`.

## Kernel auto-composition

```yaml
training:
  kernel_auto_compose: true
```

Enumerates Liger Kernel + FlashAttention combos, micro-benchmarks each, and picks the fastest. `pick_best_kernel` raises `ValueError` when every candidate is missing a finite `time_ms` — prevents silent promotion of an untimed combo when benchmarking infrastructure fails. NaN / None times are treated as `+inf`.

## Cross-document attention masking

```yaml
training:
  packing: true      # this is the whole answer
```

When sample packing is on, documents in one packed sequence must not attend across each other. That isolation is TRL's **default `bfd` strategy**, and you get it by setting `packing: true` with a FlashAttention `attn_implementation`. There is no second flag to set.

> **`packing_cross_doc_attn_mask` is refused at config load since v0.75.0, and it never worked before that.** Soup mapped it to TRL `packing_strategy="attention_free"`, which has never been in TRL's allowlist on any released version, so the flag was a `TypeError` at trainer setup rather than a working mask. It is now rejected by a `@model_validator` that names `bfd` / `bfd-requeue` / `wrapped` as the real allowlist and points at `packing: true`. This is a false-capability correction, not a regression: no release ever built that mask. Remove the key from any config that carries it.

## Activation offloading

```yaml
training:
  activation_offloading: cpu    # or: disk
```

Saved-tensor hooks offload activations to pinned RAM (`cpu`) or an on-disk scratch dir (`disk`). The disk variant keeps the `mkstemp` file descriptor open until `torch.save` flushes, closing the TOCTOU window between `os.close(fd)` and `torch.save(path)`. `torch.load(weights_only=True)` prevents arbitrary Python deserialization on reload. Scratch dirs are containment-checked against cwd. Unsloth and MLX backends are rejected.

## SFT-only guard (v0.28)

`SoupConfig` rejects `use_cut_ce`, `quantization_aware="fp8"`, `kernel_auto_compose`, and `activation_offloading` when `task != "sft"`. Multi-trainer wiring landed in v0.33.0, and every transformer-backend trainer was wired in v0.35.0.

## See also

- [Multi-GPU mastery](/docs/multi-gpu) — ZeRO++ / FSDP2 / pipeline
- [Backends](/docs/backends) — transformers / unsloth / MLX

[PreviousMulti-GPU Mastery](/docs/multi-gpu)[NextTraining Stability](/docs/training-stability)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="023-training-stability"></a>

# 23. Training Stability & Auto-Tuning (v0.32.0)

*Source: <https://trysoup.dev/docs/training-stability>*

Pre-flight tuning + in-training stability nets. All flags are opt-in.

## LR Range Finder

Run a fast.ai-style geometric LR sweep before the real training run. Soup writes a JSON report with the recommended LR, the loss curve, and the divergence point.

```bash
soup train --config soup.yaml \
  --find-lr \
  --find-lr-start 1e-7 \
  --find-lr-end 1e-1 \
  --find-lr-steps 100 \
  --find-lr-output ./lr_finder.json
```

The report contains the geometric `lrs[]`, raw + EMA-smoothed `losses[]`, the recommended LR (steepest negative gradient before divergence), the LR with min loss, and the divergence point if any.

> **v0.33.0:** `--find-lr` now runs an in-process LR-sweep training loop. NaN/Inf loss terminates the sweep early so `diverged_at` is honest.

## Auto warmup schedule

```yaml
training:
  warmup_auto: true
  warmup_ratio: 0.03   # 3% of total update steps (default)
```

Clamped to [10, 1000] so tiny datasets get some warmup and huge datasets don't burn half a million wasted steps.

## Auto mixed-precision

```yaml
training:
  auto_mixed_precision: true
```

Picks `bf16` on Ampere+, `fp16` on Turing or known fp16-stable models (Qwen2 / Qwen2.5 / Phi-3 / Phi-3.5), `no` on pre-Pascal. Multi-version pairs match the longest substring deterministically.

## Loss spike auto-recovery

Extends the watchdog: instead of stopping on a spike, decay LR and resume.

```yaml
training:
  loss_watchdog: true                   # required
  loss_spike_recovery: true
  loss_spike_recovery_max_attempts: 3
  loss_spike_recovery_lr_decay: 0.5
```

Capped at 3 attempts by default. Spike recovery writes a `spike_recovery.json` hint with the decayed LR for re-launch.

## Convergence detector

```yaml
training:
  convergence_detection: true
  convergence_window: 50
  convergence_rel_tol: 0.005
```

Surfaces `continue` / `early_stop` / `lower_lr` advice based on the loss curve.

## VRAM pressure advisory

```yaml
training:
  grad_accum_auto_tune: true
  grad_accum_pressure_threshold: 0.92
```

Records peak memory each step. When pressure crosses the threshold, recommends a new `(batch, accum)` pair preserving effective batch (capped at `accum=1024`).

[PreviousSpeed & Memory](/docs/training-speed-memory)[NextReproducibility](/docs/seeds-and-reproducibility)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="024-seeds-and-reproducibility"></a>

# 24. Seeds and reproducibility

*Source: <https://trysoup.dev/docs/seeds-and-reproducibility>*

Until v0.73.0 there was **no way to set a seed at all**. Every run trained at 42, the framework default, and the only variation between two runs of one config was row ordering plus whatever the GPU did differently that day.

That matters more than it sounds, because a project that reports "arm A beat arm B by 0.006" needs to know what one arm does against **itself**. Without a seed knob, the natural spread was missing its largest source, and every measurement quoted against it was weaker than it looked.

## The two keys

```yaml
training:
  seed: 1234        # weight init of new parameters, data order, dropout
  data_seed: 99     # optional: vary data order while holding init fixed
```

**Both are config keys, not CLI flags. There is no `--seed`.**

- **Both default to unset**, not to 42. That is deliberate rather than tidy: an unset seed has to reproduce two different historical defaults, 42 for the trainer and 0 for the multipack sampler, and defaulting the field to 42 would have silently re-ordered every existing multipack run.
- An **unset `seed` resolves to 42**; an unset `data_seed` stays unset. The fields are optional precisely so the trainer can tell "unset" from "explicitly 42".
- Bounds are 0 to 2^32 - 1. **Zero is legitimate.** A YAML `true` is **refused by name** rather than coerced to 1.
- `data_seed` needs a recent enough `accelerate`.

## What changed in v0.73.1, and what did not

In v0.73.0 the seed reached **the supervised trainer and nothing else**. A seeded GRPO or DPO run was accepted, trained at 42, and said nothing. Seventeen of eighteen task wrappers ignored it. Replicates that differed only in their seed were the same run.

It now reaches every wrapper, and it is applied **before the model loads**, because the adapter's own initialisation is drawn before the trainer's seeding used to happen.

> **The values a run trains at are unchanged. What changed is when they arrive.** An unseeded run's adapter and classification-head initialisation used to vary from process to process; it is now deterministic at 42.

## What a seed does not buy you

This is the part worth reading before you design an experiment on top of it.

- **It is not a determinism guarantee.** For bit-exact reruns you also need PyTorch's deterministic-algorithms switch, and **Soup does not set that for you**.
- **A resident 4-bit run is still not bit-reproducible from a seed.** This is diagnosed and not fixed in the source. Never treat a resident quantised arm as reproducible.
- **A streamed run is** bit-reproducible: five runs, one adapter hash, zero movement on every behavioural suite. That asymmetry is real and is why the streamed arm is the control.
- **The `mlx` backend reads neither field.** It now says so, in its existing "MLX backend ignores" line. That is a warning rather than a rejection, because a config that is valid on transformers should not become unloadable by switching backend. Seeding MLX for real needs a separate generator and is separate work.
- The multipack sampler still takes 0.

## Why the ship gate cares

The consequence is concrete, and it is the reason this page sits next to the release notes rather than in a corner.

**Three runs of one unchanged resident configuration moved two behavioural suites by 0.375 and 0.269, against a regression threshold of 0.05.** Five of seven suites could cross the line on a re-run that changed nothing at all.

Two separate things follow, and they compose:

1. Set a seed, so a replicate is a replicate.
2. Measure what your instrument can resolve before you call a delta real. That is [`soup ship --noise-floor`](/docs/ship-gate-repairs), added in v0.73.2, and it exists because greedy decoding is not deterministic on a GPU either.

Neither one alone is enough. A seed removes a source of variation you control; the noise floor sizes the one you do not.

## See also

- [v0.73.1: the free GPU tier](/docs/free-gpu-tier) — where the seed reached the rest of the trainers.
- [v0.73.2: the release gate](/docs/ship-gate-repairs) — where the instrument got measured.
- [v0.73.0 Borrowed Hardware](/docs/borrowed-hardware) — where the seed keys first shipped.
- [The ship gate](/docs/soup-ship) — the verdict these numbers feed.

[PreviousTraining Stability](/docs/training-stability)[NextTrainer Speed & Memory](/docs/multi-trainer-speed-memory)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="025-multi-trainer-speed-memory"></a>

# 25. Multi-Trainer Speed & Memory (v0.35.0)

*Source: <https://trysoup.dev/docs/multi-trainer-speed-memory>*

v0.35 finishes the v0.28 → v0.33 → v0.35 expansion: the four big speed-and-memory features now wire into **every** transformer-backend trainer.

## What's now multi-trainer

| Feature | v0.28 | v0.33 | v0.35 |
| --- | --- | --- | --- |
| `use_cut_ce` | SFT | SFT, DPO, Pretrain | 13 tasks |
| `quantization_aware: "fp8"` | SFT | SFT, DPO, Pretrain | 13 tasks |
| `kernel_auto_compose` | SFT | SFT, DPO, Pretrain | 13 tasks |
| `activation_offloading` | SFT | SFT, DPO, Pretrain | 13 tasks |

"13 tasks" = SFT, DPO, Pretrain, GRPO, PPO, KTO, ORPO, SimPO, IPO, BCO, the unified `preference` dispatcher, Reward-Model and Embedding. That is the allowlist in `utils/v028_features.py`, and it is narrower than "every trainer": ten of the 23 tasks are still **refused at config load** rather than silently ignored — `prm`, `tts`, `classifier`, `reranker`, `cross_encoder`, `distill`, `unlearn`, `moe_lora_routing`, `online_dpo` and `asr`. So `use_cut_ce: true` with `task: distill` or `task: asr` raises, even though both are transformers-backend text tasks. The MLX backend and an unknown task each emit their own message so you get the right fix.

## fp8 / int8 QAT guard

Six trainer wrappers (GRPO / KTO / ORPO / SimPO / IPO / PPO) had `if tcfg.quantization_aware:` which would route the string `"fp8"` into the legacy int8 `prepare_model_for_qat` path. Each guard is now `quantization_aware != "fp8"` (matches the DPO / Pretrain pattern).

## Activation offloading hooks installed everywhere

The shared helper in `utils/v028_features.py` now enforces `is_under_cwd` containment for `activation_offloading="disk"` and reduces the offending path to `os.path.basename` in the `ValueError` message so absolute `$HOME` paths don't leak. All thirteen supported trainer wrappers wrap `trainer.train()` with this context manager — closes a v0.33 oversight where DPO / Pretrain accepted the flag but never installed offload hooks.

## Kernel benchmarking forward-only

`benchmark_kernel_combos` runs forward-only under `torch.no_grad()` — corruption hazard from gradient accumulation onto the live training model is eliminated. Caller-supplied bounds are clamped (`bs ≤ 32`, `sl ≤ 512`, `steps ≤ 50`, `vocab ≤ 200_000`) so a misconfigured caller cannot OOM the CI runner. Returns a NEW list — input candidates are never mutated.

## Quant menu kwarg allowlist

vLLM `quantization` kwarg is now an explicit named parameter on `create_vllm_engine` (not a `**kwargs` splat) and is validated against the closed allowlist `{awq, gptq, fp8}`. The earlier kwarg-splat path could have leaked arbitrary `AsyncEngineArgs` fields to the engine constructor — eliminated by the named-param refactor.

## Error redaction on model load fallback

When every candidate fails to load, the `RuntimeError` message includes only `type(last_error).__name__ + ": " + str(last_error)` instead of `repr(last_error)` — `repr` of a `FileNotFoundError` would embed `$HOME`-prefixed checkpoint paths.

## See also

- [Training speed & memory](/docs/training-speed-memory) — original v0.28 doc
- [Quant menu](/docs/quant-menu) — original 9-format menu · [Quant Menu II](/docs/quant-menu-ii) — UD GGUF, NVFP4, BitNet, KV cache (v0.53)

[PreviousReproducibility](/docs/seeds-and-reproducibility)[NextMultipack: FFD Bin-Packing Sampler](/docs/multipack)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="026-multipack"></a>

# 26. Multipack — FFD Bin-Packing Sampler (v0.37.0)

*Source: <https://trysoup.dev/docs/multipack>*

Soup's largest single throughput win on chat fine-tuning over uneven-length data. Instead of padding every sample to `max_length`, Multipack uses **First-Fit-Decreasing bin packing** to group variable-length samples into bins approaching `batch_size × max_length` — eliminating padding waste.

```yaml
training:
  multipack: true
  packing: false   # mutually exclusive with multipack
```

## How it composes

- **Multipack** picks WHICH samples go together (FFD packing).
- The FA varlen path is auto-selected when FlashAttention is available, which is what keeps packed documents from attending across each other.
- **Do not reach for `packing_cross_doc_attn_mask`.** It is [refused at config load since v0.75.0](/docs/training-speed-memory) and never built a mask on any release. Document isolation under `packing: true` comes from TRL's default `bfd` strategy instead.

## Architecture allowlist

**38 architectures as of v0.51**, up from the 18 this release shipped with: Llama, Mistral, Mixtral, Qwen / Qwen2 / Qwen3 / Qwen2-MoE, Gemma 1/2/3, Phi / Phi-3 / Phi-4, DeepSeek V2/V3, Falcon, StableLM, SmolLM2, Granite and Granite-MoE, GLM-4 and GLM-5, Kimi, MiniMax, QwQ, QVQ, GPT-OSS, Magistral, Devstral, Ministral, MedGemma, LFM2, Cogito, Hunyuan, Ernie, Yi, Baichuan and ChatGLM. See [the v0.51 model catalog](/docs/model-catalog-v051) for what that expansion covered.

Unknown architectures **fail loudly at config-load** instead of silently no-opping (critical fix vs Axolotl's silent-miss footgun).

## Scope

Multipack is **sft / pretrain only** on the `transformers` backend. Preference / RLHF trainers and MLX backend get distinct error messages naming the actual reason. The sampler is wired into HF Trainer's `_get_train_sampler` and has been live since v0.40.4.

## DoS hardening

- FFD packer caps at 1M items, a bound on retained memory rather than on runtime: since v0.75.0 placement descends a segment tree of per-bin remaining capacity, so it is **O(N log N)** rather than the O(N²) scan it used to be. Measured on one box, 5.5x faster at 1,000 rows, 37x at 10,000 and 96x at 30,000, with the packing itself verified unchanged against the old function over 6,000 randomized cases. Which item lands in which bin is the property that had to hold: changing it would silently change every multipack run
- 4D mask builder caps allocations at 2³¹ cells
- Chat-template Jinja analyzer caps at 128 KB
- Every numeric input rejects `bool` explicitly

## Jinja template analyzer

The `JinjaTemplateAnalyzer` (also v0.37.0) walks chat-template ASTs to discover non-standard `message.<field>` references (`tool_calls`, `name`, `weight`, `train`) — used by the v0.36.0 `train_on_messages_with_train_field` path so per-message training masks are aware of fields beyond `role` / `content`. The analyzer **parses** templates without rendering them, so a crafted `soup.yaml` cannot trigger SSRF.

[PreviousTrainer Speed & Memory](/docs/multi-trainer-speed-memory)[NextLoRA Quality](/docs/lora-quality)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="027-lora-quality"></a>

# 27. LoRA Quality — PiSSA, ReLoRA, Per-Pattern Rank, Surgical Patches (v0.39.0)

*Source: <https://trysoup.dev/docs/lora-quality>*

Five PEFT-surface improvements that LlamaFactory and Axolotl maintain.

```yaml
training:
  lora:
    init_strategy: pissa          # 'random' (default), 'pissa', 'olora'
    rank_pattern:                 # per-target-module rank override
      q_proj: 8
      v_proj: 16
    alpha_pattern:                # per-target-module alpha override
      q_proj: 16
  relora_steps: 500               # magnitude-prune LoRA every 500 steps
  relora_warmup_ratio: 0.1        # skip first 10% of training
  relora_prune_ratio: 0.9         # zero out smallest 90% by magnitude
  relora_reset_optimizer: true    # clear optimizer state on each fire
```

## PiSSA

PiSSA initializes the LoRA pair from the **SVD of the base weight**, giving faster early convergence than random init at the cost of one extra SVD pass on the first epoch.

`init_strategy: olora` is also accepted; setting the legacy `use_olora: true` auto-aligns for back-compat.

## ReLoRA

ReLoRA fires every N global steps, magnitude-prunes the LoRA adapter weights (keeping the top `1 - relora_prune_ratio` by absolute value), and optionally clears optimizer state for the pruned parameters so momentum doesn't fight the new sparse weights.

Useful for very long training runs where the LoRA capacity saturates.

## Per-pattern rank/alpha

Map module name patterns to integer ranks. Useful in MoE configs where expert FFNs need lower rank than attention.

Caps: 256 keys × value 1024. `bool` rejected on values. Incompatible with `use_vera` (VeRA shares one rank).

## Surgical patches

- **Gemma 4** `ClippableLinear` swap (auto-detected via word-boundary regex on model name)
- **Fused-MoE 3-D expert** `lora_dropout` strip

Both auto-fire when the model name and architecture match. Both are gated and silent on unrelated models.

## Template registry

The 21 built-in templates now live as `soup_cli/templates/*.yaml` with a `manifest.json` index. `soup init --template <name>` reads the YAML; the inline copies in `schema.py` stay as a back-compat fallback, deprecated in favour of the YAML registry.

`load_template` containment-checks the resolved path against `_templates_dir()` so a tampered `manifest.json` cannot read files outside the package directory.

## Scope

Wired into the SFT trainer + transformers backend in v0.39.0. ReLoRA is wired into the preference and RL trainers too (DPO / GRPO / KTO and the rest). MLX backend gets a distinct error message.

[PreviousMultipack: FFD Bin-Packing Sampler](/docs/multipack)[NextPreference Variety](/docs/preference-variety)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="028-preference-variety"></a>

# 28. Preference Variety (v0.40.0)

*Source: <https://trysoup.dev/docs/preference-variety>*

Five preference losses live behind one config knob. Pick a loss without renaming your task, anneal β over training, periodically refresh the frozen reference, and blend losses with a forward-looking multi-objective surface.

> **On a card that cannot hold the model**: since v0.72.4, `dpo`, `orpo`, `simpo` and `kto` also run over a streamed base, where the frozen reference is that same stream with its adapters switched off rather than a second copy of the weights. Note the unified `task: preference` dispatcher below, and `ipo` and `bco`, are **not** in the streaming allowlist: name the loss in `task` directly. See [Preference losses over streaming](/docs/streaming-preference).

## BCO (Binary Classifier Optimization)

Same input format as DPO; rows are split internally to TRL's BCO unpaired schema (`{prompt, completion, label}`).

```yaml
task: bco
data:
  train: ./data/preferences.jsonl
  format: dpo
training:
  bco_beta: 0.1
  lora: { r: 64, alpha: 16 }
  quantization: 4bit
```

`bco_beta` defaults to 0.1 (`gt=0`). New `soup init --template bco` ships in the box.

## Unified preference dispatcher

Use `task: preference` + `training.preference_loss` to swap losses without touching `task`. Hyperparameter sweeps over the loss type itself become trivial.

```yaml
task: preference
data:
  train: ./data/preferences.jsonl
  format: dpo
training:
  preference_loss: dpo   # or simpo, orpo, ipo, bco
```

Legacy `task: dpo` / `task: simpo` / etc. remain first-class — the unified surface is additive.

## KL-controlled DPO variants

Anneal β over training and periodically refresh the reference model.

```yaml
task: dpo   # or task: preference + preference_loss: dpo, or task: ipo
training:
  dpo_beta: 0.1
  dpo_beta_schedule: linear   # linear | cosine | exponential
  dpo_beta_end: 0.01
  dpo_ref_regen_epochs: 2     # copy student → ref model every 2 epochs
```

Both controls are gated to DPO-family tasks (`dpo`, `ipo`, or `preference` with `preference_loss in {dpo, ipo}`). Transformers backend only.

The `BetaScheduleCallback` resolves `total_steps` lazily in `on_train_begin` so the schedule sees the real `state.max_steps` populated by HF Trainer. Epoch-0 regen is suppressed (avoids copying the untrained student).

## Multi-objective preference loss (live as of v0.53.11)

```yaml
task: preference
training:
  preference_loss_weights: {dpo: 0.7, simpo: 0.3}
```

The schema validates 2–5 entries summing to 1.0 (±1e-6). Single-entry rejected with an actionable message pointing at scalar `preference_loss`. Mutually exclusive with scalar `preference_loss`. Rejected on MLX backend.

**`bco` cannot be combined with a paired loss**, and the refusal arrives later than the others: the schema allowlist accepts the name, so the config loads clean and `validate_weight_compat` raises at trainer setup instead. BCO scores each completion on its own, the paired losses need a chosen-versus-rejected pair, and there is no shared batch shape. Use `bco` as a scalar `preference_loss` rather than as an ensemble member.

Live runtime weighted-loss combination is wired in v0.40.1; v0.40.0 fails fast with an actionable `NotImplementedError` if you actually try to train (same stub-then-live pattern as v0.27.0 MII / v0.37.0 multipack / v0.38.0 quant menu / v0.39.0 ReLoRA).

## Stats

- Net **+118 tests** (4538 → 4656 across 136 files)
- BCO trainer + dispatcher + β schedule math + ref-model regen TOCTOU + multi-objective schema bounds

## See also

- [DPO training guide](/docs/dpo-training-guide) — preference dataset format
- [Trace-to-preference](/docs/trace-to-preference) — harvest pairs from production logs
- [Registry](/docs/registry) — track preference variants in the lineage DAG

[PreviousLoRA Quality](/docs/lora-quality)[NextOptimizer Zoo](/docs/optimizer-zoo)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="029-optimizer-zoo"></a>

# 29. Optimizer Zoo (v0.41.0)

*Source: <https://trysoup.dev/docs/optimizer-zoo>*

A closed allowlist of **32** optimizers covering HF-native (10), bitsandbytes-backed (8) and the v0.41 additions (14).

## Supported optimizers

HF-native: `adamw_torch`, `adamw_torch_fused`, `adafactor`, `sgd`, and the rest of the HF set.

bitsandbytes-backed: `adamw_bnb_8bit`, `paged_adamw_8bit`, `lion_8bit`, etc.

New in v0.41:

- **BAdam** — block-coordinate descent for full-parameter fine-tuning
- **APOLLO** (`apollo_adamw`) — gradient-scaled training in low rank
- **Adam-mini** — half the optimizer memory of AdamW
- **lomo** / **adalomo** — low-memory optimization with optional adaptive scaling
- **grokadamw** — Grokfast-style AdamW
- **schedule\_free\_adamw** / **schedule\_free\_sgd**
- **muon**, **dion**, **came\_pytorch**
- **TorchAO** `ao_adamw_fp8` / `ao_adamw_4bit` / `ao_adamw_8bit`

```yaml
training:
  optimizer: muon
```

`validate_optimizer_name` rejects non-string / empty / null-byte / >64-char inputs with actionable messages and lowercases for deterministic lookup. Unknown names fail at config-load.

## Per-module LR groups

Map regex patterns → learning rates with first-match-wins routing.

```yaml
training:
  lr: 2e-4   # base / fallback
  lr_groups:
    - { pattern: "model\\.embed_tokens", lr: 5e-5 }
    - { pattern: ".*lora_A.*", lr: 1e-3 }
    - { pattern: ".*lora_B.*", lr: 1e-3 }
```

Capped at 32 entries. Each `pattern` must compile via `re.compile` (ReDoS probe runs). Each `lr ∈ (0, 1]`, finite-only (NaN / ±inf rejected), bool rejected. Duplicates rejected.

## LoftQ quantization-aware LoRA init

```yaml
training:
  lora:
    init_strategy: loftq   # random | pissa | olora | loftq
    loftq_iter: 5          # [1, 10]
    loftq_bits: 4          # 2 | 4 | 8
```

Builds the LoftQ config via peft (lazy import); incompatible with DoRA + VeRA.

## LLaMA Pro block expansion

```yaml
training:
  expand_layers: 4              # [1, 64]
  freeze_trainable_layers: 32   # required when expand_layers set
```

Schema landed in v0.41.0 and the block-expansion patch is applied live by the SFT and pretrain trainers.

## Friendly load\_in\_X aliases

`load_in_8bit: true` remaps `quantization` → `8bit`. `load_in_16bit: true` remaps to `none`. Mutually exclusive. Combining either with an explicit Quant Menu format raises rather than silently overriding.

[PreviousPreference Variety](/docs/preference-variety)[NextLong Context](/docs/long-context)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="030-long-context"></a>

# 30. Long Context (v0.49.0)

*Source: <https://trysoup.dev/docs/long-context>*

Three RoPE-scaling strategies for 128k+ context fine-tuning.

## YaRN

```yaml
training:
  rope_scaling_type: yarn   # linear | dynamic | yarn | longrope
  yarn_factor: 8.0
  yarn_beta_fast: 32
  yarn_beta_slow: 1
```

The RoPE keys are flat fields on `training`, not a nested `rope_scaling` block.

## Dynamic NTK

```yaml
training:
  rope_scaling_type: dynamic
  yarn_factor: 4.0
```

## LongLoRA S² shifted-sparse attention

```yaml
training:
  use_longlora: true
```

Live: the forward-pass override is applied by the SFT trainer, and the group size is derived rather than configured.

## Llama 3.1 NTK-aware scaling

Set `rope_scaling_type: llama3` and Soup wires up the Llama 3.1-style NTK-aware schedule.

Gates: `validate_longlora_compat` + `is_llama_model` reject incompatible architectures at config-load. Pair with [Multipack](/docs/multipack) to keep variable-length samples efficient on long-context runs.

[PreviousOptimizer Zoo](/docs/optimizer-zoo)[NextGRPO Plus](/docs/grpo-plus)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="031-grpo-plus"></a>

# 31. GRPO Plus (v0.50.0)

*Source: <https://trysoup.dev/docs/grpo-plus>*

22 features. Unsloth + axolotl GRPO parity.

## 7 GRPO variants

```yaml
task: grpo
training:
  grpo_variant: gspo   # standard | gspo | dapo | dr_grpo | bnpo | two_sided | rft
  grpo_delta: 0.5      # required for two_sided, optional for gspo (clip radius,
                       # default 0.2). (0, 1]. Rejected on every other variant
  grpo_fp16: true      # explicit FP16 mixed precision
```

## Long-context & vision GRPO

```yaml
base: Qwen/Qwen2-VL-7B-Instruct   # vision_grpo needs a base from the VLM allowlist
modality: vision                  # and the vision modality, or it is refused
training:
  long_context_grpo: true   # extends rope scaling into rollouts
  vision_grpo: true         # multimodal GRPO
  vllm_sleep_mode: true     # free vLLM memory between rollouts
```

## Async rollout backends

```yaml
training:
  rollout_backend: openenv   # art | ruler | nemo_gym | openenv
  rollout_func: soup_cli.envs.calculator:rollout   # required by openenv
  async_grpo_prefetch: true
```

`art` — OpenPipe ART, `ruler` — long-horizon judging, `nemo_gym` — NVIDIA Gym, `openenv` — multi-turn agent envs.

## Reference-model controls

```yaml
training:
  ref_model_ema_alpha: 0.99   # EMA-style ref refresh
  replay_buffer_size: 50000
  tis_threshold: 1.5          # truncated importance sampling
  mask_truncated_completions: true
  defer_rerolling: true
  skip_zero_advantage: true
  off_policy_mask_threshold: 0.7
```

## New task: prm

`task: prm` (Process Reward Model) wired through the standard reward-model trainer. Gates: vision + GRPO compat checked.

v0.50.0 shipped the schema. v0.53.3 wired `grpo_fp16` routing + the known-VLM-base gate for `vision_grpo`; v0.53.11 lit up real loss kernels for every non-standard variant (gspo / dapo / dr\_grpo / bnpo / two\_sided / rft) via `make_grpo_trainer_variant`, made `task: prm` live with per-step MSE + reward head, and enabled `GRPOStabilityCallback` (EMA + replay buffer + TIS alerts). See [v0.53.11 — GRPO Plus finish](/docs/v05311-grpo-prm-longlora).

[PreviousLong Context](/docs/long-context)[NextModality II](/docs/modality-ii)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="032-modality-ii"></a>

# 32. Modality II (v0.52.0)

*Source: <https://trysoup.dev/docs/modality-ii>*

7 parts. New task families + BitNet + EBFT/GDPO + MoE quant. +237 tests (6968 → 7205).

## TTS (task: tts)

5 family allowlists with per-family emotion vocabularies.

```yaml
task: tts
modality: audio_out
base: canopylabs/orpheus-3b-0.1-ft
data:
  format: audio
  train: ./data/tts.jsonl
training:
  tts_family: orpheus   # orpheus | sesame_csm | llasa | spark | oute
  tts_emotion: happy    # a single string, not a list
```

Cross-validator gates per family. `canopylabs/orpheus` requires `tts_family: orpheus`.

**`data.format: audio` is the live-codec path, and it needs a per-family package that Soup does not install for you**: `snac` for Orpheus, `moshi` for Sesame-CSM, `xcodec2` for Llasa, `sparktts` for Spark, `outetts` for Oute. Only **Orpheus is live**; the other four raise a friendly per-family error naming what is missing. The path that runs everywhere is the **pre-encoded** one: encode your audio to codec tokens yourself, register them through `data.new_special_tokens`, and train with `data.format: chat` over the token text. That is the workflow to reach for unless you specifically want the Orpheus codec in-process.

## Distillation (task: distill)

```yaml
task: distill
base: meta-llama/Llama-3.2-3B
training:
  teacher_model: meta-llama/Llama-3.1-70B-Instruct
  distill_divergence: kl         # kl | forward_kl | reverse_kl | js
  distill_temperature: 2.0       # [0.05, 100]
```

## Classifier / Reranker / Cross-Encoder

```yaml
task: classifier   # | reranker | cross_encoder
training:
  num_labels: 5
  label_names: ["very_bad", "bad", "neutral", "good", "very_good"]
  classifier_kind: single_label   # or multi_label (v0.52.0)
  classifier_lora: false          # true wraps the head with LoRA (v0.71.12)
```

`classifier_kind` picks the head: `single_label` is the default for `task: classifier`, `multi_label` trains one independent decision per label rather than a choice between them. `classifier_lora` is opt-in: it wraps the sequence-classification head as a PEFT `SEQ_CLS` adapter instead of full fine-tuning, and the ordinary `training.lora` block still supplies `r` / `alpha` / `dropout` when you turn it on.

## BitNet 1.58-bit quantization

```yaml
training:
  quantization: bitnet_1.58
```

Gates: non-MLX, text modality, `task ∈ {sft, pretrain, dpo}`. `is_bitnet_model` heuristic auto-detects Microsoft / Falcon-E checkpoints.

## EBFT + GDPO variants

These two cannot share a config: `ebft_variant` is refused unless `task: sft` and `gdpo_variant` unless `task` is `dpo` or `preference`.

```yaml
task: sft
training:
  ebft_variant: structured        # structured | strided
```

```yaml
task: dpo
training:
  gdpo_variant: length_normalized # standard | length_normalized | margin
```

## MoE expert quant

```yaml
training:
  moe_lora: true                 # required: moe_expert_quant is refused without it
  moe_expert_quant: nf4          # nf4 | int8_rowwise
  train_router_only: true        # freeze experts, train router only
```

## Reasoning effort dispatch

```yaml
training:
  reasoning_effort: medium       # low | medium | high  (gpt-oss family)
```

v0.52.0 shipped the schema; v0.53.2 lit up the trainers — `task: distill` (DistillTrainerWrapper with KL/forward\_kl/reverse\_kl/js), `task: classifier | reranker | cross_encoder` (single-label / multi-label / cross-encoder heads), EBFT + GDPO loss kernels, and `reasoning_effort` dispatch. See [v0.53.2 — Modality II live](/docs/v0532-modality-live).

[PreviousGRPO Plus](/docs/grpo-plus)[NextAgent Forge](/docs/agent-forge)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="033-agent-forge"></a>

# 33. Agent Forge & Deploy Autopilot (v0.46.0)

*Source: <https://trysoup.dev/docs/agent-forge>*

## soup agent — OpenAPI / MCP / GraphQL → SFT

Parse a tool spec, synthesize tool-calling SFT data, then train.

```bash
soup agent synth --spec ./openapi.yaml --output ./tools.jsonl
soup agent train --spec ./openapi.yaml --base meta-llama/Llama-3.1-8B-Instruct
soup agent eval --spec ./openapi.yaml --predictions ./preds.jsonl
```

Supports OpenAPI 3.x, MCP manifests, and GraphQL introspection.

## soup deploy autopilot

Pick PEFT + quant + spec-decoding combo for a hardware target.

```bash
soup deploy autopilot --base ./output --target runpod-a100
soup deploy autopilot --base ./output --target mac-m4-pro
```

`--list` prints the catalog. The ten target ids are `mac-m3`, `mac-m4-pro`, `rtx-3060-12gb`, `rtx-4090-24gb`, `iphone-16`, `pixel-9`, `ollama-local`, `lm-studio`, `runpod-a100` and `hf-jobs-h100`. A run writes two files, `deploy_autopilot.yaml` and `deploy_autopilot.sh`.

[PreviousModality II](/docs/modality-ii)[NextUnlearning & knowledge editing](/docs/unlearning)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="034-unlearning"></a>

# 34. Unlearning & Knowledge Edit (v0.61.0)

*Source: <https://trysoup.dev/docs/unlearning>*

GDPR right-to-be-forgotten as a first-class task. Surgical fact patches without retraining.

## `task: unlearn` — remove specific data, keep the rest

Three methods, all wired as live trainers:

| Method | Loss shape | Needs reference model | Notes |
| --- | --- | --- | --- |
| **NPO** (Negative Preference Optimization) | DPO-shaped, negative-only | yes | Pair with retain set |
| **SimNPO** | Length-normalized NPO | no | Faster on long sequences |
| **RMU** (Representation Misdirection Unlearning) | Residual-stream noise on forget inputs | no | Best for concept-level removal |

```yaml
# soup.yaml
base: meta-llama/Llama-3.1-8B
task: unlearn
training:
  epochs: 3
  unlearn_method: simnpo
  unlearn_alpha: 0.7
data:
  forget_set: ./private_data_to_remove.jsonl
  retain_set: ./general_knowledge.jsonl
output: ./unlearned_model
```

`unlearn_alpha` (0.0–10.0) is the retain-set weight. It defaults to **unset**, and an unset value resolves to **1.0** in the trainer, not to 0.5. `forget_set` is required; `retain_set` is optional but strongly recommended for NPO.

## `soup eval unlearning` — TOFU / MUSE / WMDP

```bash
soup eval unlearning <run-id> --benchmark tofu
```

Three benchmarks at launch:

- **TOFU** — Task of Fictitious Unlearning. Forget Quality + Model Utility + PrivLeak.
- **MUSE** — Memorization & Unlearning suite.
- **WMDP** — Weapons of Mass Destruction Proxy.

Scores roll up into an OK / MINOR / MAJOR verdict mirroring v0.56 diagnose.

## `soup edit set` — ROME / MEMIT / AlphaEdit

Surgically patch facts without retraining:

```bash
soup edit set --base meta-llama/Llama-3.1-8B-Instruct \
  --method rome \
  --subject "The capital of France is" \
  --target "Lyon" \
  --plan-only
```

- **ROME** — Rank-One Model Editing, targets MLP layers (Meng 2022).
- **MEMIT** — Mass-Edit Memory in a Transformer (Meng 2023).
- **AlphaEdit** — gradient-based fact patching.

v0.61.0 shipped the plan / validation surface; **live application landed in v0.71.9** — covariance-free rank-1 ROME/MEMIT/AlphaEdit kernels apply the edit (on a tiny model a ROME edit moved P("Lyon" | "The capital of France is") from 0.0016 → 0.96), guarded by a persistent SQLite EditGovernor; live GRACE codebook ships alongside.

## `soup edit diff` — citation diff visualizer

```bash
soup edit diff registry://before_id registry://after_id \
  --probes ./probes.jsonl --top-k 10
```

Compares two Registry entries and surfaces which facts changed. Citation visualizer overlays before / after answers next to the supporting evidence.

## Sequential Edit Governor

Built into both `soup edit` and the training pipeline:

- **Edit count overflow** — caps per-base-model edits (default 10) to prevent cascading drift.
- **Norm blowup** — rejects any edit that would amplify weight norms beyond a configured threshold.

## Numbers

+193 new tests in v0.61.0 (9446 → 9571). Security: 5 HIGH, 11 MEDIUM, 11 LOW fixes.

## See also

- [Diagnose](/docs/diagnose) — pair unlearning with the 6-probe report card to verify the forget actually happened.
- [RAG & steering](/docs/rag-and-steering) — v0.62 control-vector steering, a soft alternative to surgical edits.
- [Post-train x-rays (v0.66)](/docs/post-train-xrays) — `soup probe sae-diff` and `soup probe sleeper` verify unlearning at the mechanistic level (Sparse Autoencoder feature movement + calibrated defection classifier), beyond Forget Quality / Model Utility / PrivLeak benchmark scores.

[PreviousAgent Forge](/docs/agent-forge)[NextRAG & Steering](/docs/rag-and-steering)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="035-rag-and-steering"></a>

# 35. Retrieval-Augmented FT & Activation Steering (v0.62.0)

*Source: <https://trysoup.dev/docs/rag-and-steering>*

Five surfaces wired together: RAFT data format, RA-DIT two-stage pipeline, citation-faithful fine-tuning, activation steering vectors (CAA / ITI / RepE), and the GRACE codebook.

## `data.format: raft` — Stanford RAFT data

```yaml
data:
  train: ./raft_data.jsonl
  format: raft
  max_length: 4096
```

Per-row schema:

```json
{
  "query": "What is the capital of France?",
  "golden_doc": "France is a country in Europe...",
  "distractor_docs": ["Spain is...", "Germany is..."],
  "answer": "Paris"
}
```

The model learns to use retrieved context (golden + distractors) to answer queries — context-aware completion, not isolated Q&A.

## `training.ra_dit_stage` — two-stage pipeline

RA-DIT (Retrieval-Augmented Dual Instruction Tuning) chains:

```yaml
# Stage 1: contrastive retriever
task: embedding
training:
  ra_dit_stage: retriever
  ra_dit_retriever_model: sentence-transformers/all-MiniLM-L6-v2
```

```yaml
# Stage 2: RAFT generator
task: sft
data:
  format: raft
training:
  ra_dit_stage: generator
```

Both stages reuse the existing trainer wrappers. **Live as of v0.71.10** — RAFT span-mask training (answer-only loss, `[doc-N]` citation labels) and the `soup ra-dit` one-shot orchestrator (retriever → generator in one command, Registry auto-link) run end-to-end; `soup steer train/apply` + `soup serve --steer` and `soup eval citation` are live too.

## `training.citation_faithful` — enforce source attribution

```yaml
data:
  format: raft
training:
  citation_faithful: true
  citation_style: bracket   # bracket | inline | footnote
  citation_recall_threshold: 0.85
```

When `citation_faithful=true`, the trainer masks the loss to emphasize citation spans. The model learns to cite sources from retrieved docs. The final save is refused if citation recall < threshold.

## `soup steer` — activation steering vectors

```bash
soup steer train --base meta-llama/Llama-3.1-8B-Instruct \
  --method caa --name safety-v1 \
  --pairs ./safety_pairs.jsonl --layer 16

soup steer apply --name safety-v1 --strength 1.5
soup steer list
```

Three methods:

- **CAA** (Contrastive Activation Addition) — add a learned vector to the residual stream.
- **ITI** (Inference-Time Intervention) — shift specific attention heads.
- **RepE** (Representation Engineering) — PCA-based direction extraction.

`|strength| ≤ 10` is enforced. Vectors register as the new `steering_vector` artifact kind in the v0.26 Registry.

Pairs JSONL:

```json
{"positive": "You are a helpful AI.", "negative": "You are a harmful AI."}
```

## `training.grace_codebook` — discrete latent codebook

```yaml
training:
  grace_codebook: true
  grace_codebook_size: 1024
  grace_codebook_dim: 128     # both size and dim are required together
```

GRACE (Generalization-Regularized Adaptive Codebook Embedding) discretizes the latent activation space into a learned codebook. Reduces overfitting on small datasets; useful for thousands of sequential edits without norm-blowup. Schema landed in v0.62.0; the live codebook shipped in v0.71.9.

## New recipes

Three RAFT-style recipes shipped:

- `raft-llama3-8b` — RAFT SFT generator on Llama 3.1 8B.
- `ra-dit-retriever` — sentence-transformer contrastive stage.
- `ra-dit-llama3-8b` — full RA-DIT stage-2 generator.

## Numbers

+215 new tests in v0.62.0 (9571 → 9786). Security: 0 CRITICAL, 0 HIGH, 4 MEDIUM, 11 LOW.

## See also

- [Trace ecosystem](/docs/trace-ecosystem) — v0.63 `soup ingest` produces the JSONL that feeds the RAFT generator.
- [Unlearning](/docs/unlearning) — surgical edits as a harder counterpart to soft steering.
- [Data Forge](/docs/data-forge) — quality moat for the source docs that become golden / distractor pairs.

[PreviousUnlearning & knowledge editing](/docs/unlearning)[NextPrompt Compile & Distill](/docs/anti-trend-insurance)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="036-anti-trend-insurance"></a>

# 36. Anti-trend Insurance (v0.68.0)

*Source: <https://trysoup.dev/docs/anti-trend-insurance>*

Five-bet hedge against paradigm shifts. If prompt engineering keeps winning, `soup compile` keeps you covered. If prompt costs wall out, `soup distill-prompt` migrates the system prompt into weights. `soup compile-tools` does the same trick for tool descriptions. `soup apple-adapter` targets Apple FoundationModels on iOS 26+. And `soup local-rl` builds a personal-LLM feedback flywheel from thumbs-up/down on your own machine.

## `soup compile` — DSPy + GEPA + TextGrad prompt-program compiler

```bash
soup compile ./program.py --eval ./suite.yaml \
  --optimizer mipro --max-iters 500 --output ./compiled.json
```

Closed optimiser allowlist of 5: `mipro`, `gepa`, `textgrad`, `copro`, `bootstrap_fewshot`. Hard bound `MAX_COMPILE_ITERS=1000`.

- `validate_program_path` requires `.py`, cwd containment, `os.lstat + S_ISLNK` rejection via shared `paths.enforce_under_cwd_and_no_symlink`
- `CompileResult` enforces finite-score (no NaN / ±Inf), iterations ≥ 0
- Module is `commands/compile_cmd.py` because `compile` is a Python builtin
- **Live as of v0.71.13** (behind the `[compile]` extra) — `run_compile` dispatches DSPy / GEPA / TextGrad; `soup compile-tools` optimises tool schemas too; `--plan-only` still renders the plan and exits 0

## `soup distill-prompt` — long prompts → small fine-tunes

```bash
soup distill-prompt --traces ./traces.jsonl \
  --teacher meta-llama/Llama-3-70B --student mistralai/Mistral-7B-v0.3 \
  --strategy sft --output ./dataset.jsonl
```

Closed strategy set `{sft, preference, kl}`. Teacher / student IDs capped at 512 chars; null-byte + empty rejected. Composes with v0.71 cross-tokenizer ULD. **Live as of v0.71.13** (behind the `[compile]` extra) — `prepare_distill_dataset` calls the teacher once per trace via the v0.20 providers and emits sft/kl messages or preference chosen/rejected pairs.

## `soup compile-tools` — textual gradients over tool descriptions

```bash
soup compile-tools ./spec.json --eval ./eval.jsonl --optimizer textgrad
```

Spec extension allowlist `{.json, .yaml, .yml}` (case-insensitive on Windows). TextGrad / GEPA optimise tool descriptions so model picks them more accurately. Composes with v0.46 Agent Forge — Agent Forge parses the spec, ToolCompile optimises descriptions.

## `soup apple-adapter` — HF ↔ MLX ↔ Apple FoundationModels

```bash
soup apple-adapter ./adapter \
  --direction hf-to-apple --output ./apple-bundle --sign
```

Closed direction allowlist of 4: `hf-to-mlx`, `mlx-to-hf`, `hf-to-apple`, `mlx-to-apple`. Explicit `S_ISDIR` + symlink rejection on source. `sign` must be real `bool` (bool-as-int defence). Reuses v0.60 Part B signing infrastructure and extends the v0.25 MLX backend. **Live as of v0.71.21** — `convert_apple_adapter` does the PEFT ↔ mlx-lm round trip for `hf-to-mlx` / `mlx-to-hf` (real bf16 adapter smoke); the `*-to-apple` directions stay upstream-gated (exit 3) until Apple's on-device adapter spec settles.

## `soup local-rl` — personal-LLM feedback flywheel (LIVE)

```bash
# The DB path must stay under the current working directory: a ~ path is refused.
soup local-rl init --db ./local.db
soup local-rl record --db ./local.db \
  --prompt "summarise my last commit" --response "..." --thumb up
# or let the served model fill the same DB for you:
soup serve --model ./output --record-thumbs ./local.db
soup local-rl status --db ./local.db
soup local-rl harvest --db ./local.db --output ./pairs.jsonl

soup train --config dpo.yaml   # point data.train at ./pairs.jsonl
```

- **You do not have to call `record` by hand.** [`soup serve --record-thumbs <db>`](/docs/speculative-decoding#capturing-thumbs-from-the-served-model) turns on `POST /v1/thumbs` and writes into this same database, which is the edge that closes the loop: serve, collect, harvest, train. Path contained under cwd, transformers backend only.
- POSIX `0o600` SQLite, `interactions` + `thumbs` tables (idempotent `CREATE TABLE IF NOT EXISTS`)
- Parameterised inserts, 16 KiB prompt + 16 KiB response caps, null-byte rejection
- `harvest` walks thumbs by `ts ASC`, emits one `DpoPair{prompt, chosen, rejected}` per prompt with both an up and down (last-writes-win dedup), atomic JSONL write via `tempfile.mkstemp + os.replace`
- `soup local-rl train` is **live as of v0.71.13** — `--once` harvests the latest thumbs DPO pairs and runs a real nightly DPO/KTO/ORPO train via a `soup train` subprocess (a `state` table skips re-runs with no new feedback or fewer than `--min-pairs`); without `--once` it renders an injection-safe systemd `.service`/`.timer` + launchd `.plist` scheduler scaffold

## Numbers

+204 tests in v0.68.0 (11,021 → **11,225**) across 6 new test files. 2 POSIX-only symlink tests skip on Windows.

## See also

- [Data engineering pro (v0.69)](/docs/data-engineering-pro) — `soup build` + `soup expect` build on the same TOCTOU helper consolidated here.
- [Loop hardening (v0.70)](/docs/loop-hardening) — cross-tokenizer ULD pairs with `soup distill-prompt`.
- [MLX backend](/docs/mlx-backend) — what `soup apple-adapter` extends.

[PreviousRAG & Steering](/docs/rag-and-steering)[NextLoop Hardening](/docs/loop-hardening)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="037-loop-hardening"></a>

# 37. Loop Hardening (v0.70.0 → live in v0.71.11)

*Source: <https://trysoup.dev/docs/loop-hardening>*

Six surfaces that protect the training loop from the failure modes that cost a real GPU-hour. Shipped schema-first in v0.70.0; **as of v0.71.11 every callback is live** — the detectors install real GRPO/PPO `TrainerCallback`s, the distillation losses compute inside the distill trainer, the RL checkpoints write real state, and `soup iterative-dpo` runs the full loop. Validated end-to-end on SmolLM2-135M.

## `--reward-hack-detector` — InfoRM + RM-ensemble divergence

```bash
soup train --config grpo.yaml \
  --reward-hack-detector info_rm \
  --reward-hack-halt
```

`base`, `task` and `reward_model` are config keys, so they live in `grpo.yaml` rather than on the command line. (Do not paste a `#` comment inside a backslash chain: the comment ends the command, and the flags below it run as commands of their own.)

Two detectors:

- `info_rm` — InfoRM Cluster-Separation Index (Wang et al. 2024, [arXiv 2402.09345](https://arxiv.org/abs/2402.09345)). Drops when the policy collapses onto a degenerate reward-maximising subspace.
- `rm_ensemble` — mean pairwise variance across an RM ensemble (cap 32). When ensemble members disagree, the policy is exploiting one of them.

Math kernels `compute_cluster_separation`, `compute_rm_ensemble_divergence`, `classify_hack_signal` are **LIVE** with OK / WARN / HACK bands at 0.10 / 0.30 relative drop. `--reward-hack-halt` auto-stops on HACK (exit 2). Cross-validator: `task in {grpo, ppo}` only, `halt=True` requires detector, rejects mlx; `rm_ensemble` requires ≥2 reward functions. Composes with v0.34 `soup why` for anomaly explanation. **Live as of v0.71.11** — the GRPO callback reads per-step rewards via a shared thread-safe capture buffer, classifies the verdict, logs it to `state.log_history`, and halts on HACK.

> **v0.71.26 closes the loop.** These detectors no longer only \*halt\*: `--reward-hack-mitigation kl_control|pid_lagrangian` makes the trainer **self-correct** mid-run — raise the KL penalty, shape the reward, roll back to the last-good checkpoint, then early-stop only as a last resort. See [Closed-loop reward-hacking auto-mitigation](/docs/reward-hack-mitigation).

## `training.uld_strategy` — Universal Logit Distillation

```yaml
# soup.yaml
task: distill
training:
  teacher_model: meta-llama/Llama-3.1-8B-Instruct   # required by task: distill
  uld_strategy: wasserstein_aligned   # the one that handles two different tokenizers
```

Boizard et al. 2024 ([arXiv 2402.12030](https://arxiv.org/abs/2402.12030)). Three strategies, and **only one of them is cross-tokenizer**. Getting that wrong is not a slow run, it is a run that trains on the wrong text and reports a plausible loss the whole way, so read the split before you pick:

| Strategy | Tokenizers | What it does |
| --- | --- | --- |
| `wasserstein_aligned` | **Different** | Re-tokenizes and aligns decoded character spans, so Llama → Mistral or GPT-2 BPE → Llama SentencePiece is a real comparison |
| `wasserstein` | **Must be interchangeable** | 1-D Wasserstein distance over sorted teacher / student logits, no alignment. Cheap, and correct only for two sizes in one family |
| `topk_align` | **Must be interchangeable** | Top-K teacher logits matched via a BPE-overlap heuristic. Sharper signal, same tokenizer requirement |

`uld_top_k: 32` is required for `topk_align`. `_MAX_VOCAB_SIZE=262144` covers multilingual SentencePiece and GPT-OSS 200K vocabularies. All three are gated to `task='distill'` and reject the mlx backend. **Live as of v0.71.11.** (v0.71.12 also adds `distill_mode: sequence` for hard-label sequence-level KD, mutually exclusive with the ULD logit path.)

> **`wasserstein` and `topk_align` were sold as cross-tokenizer here until v0.75.0, and they never were.** Both forward the student's own `input_ids` **straight to the teacher**, clamped into its vocabulary range to avoid an index error. Clamping does not translate a token between two vocabularies, it just picks some other token. So a mismatched pair fed the teacher garbled or simply different text, and the distillation term was computed against logits for that wrong text, while the loss stayed **finite and plausible** the whole run. Nothing raised and nothing warned.

>

> Both strategies now **refuse a tokenizer pair that is not interchangeable, at `setup()`**, naming `wasserstein_aligned` as the working alternative. The check reuses the same `same_tokenizer` probe Soup already trusts to decide whether a speculative-decoding draft is interchangeable with its target. The same-tokenizer fast path is untouched. **If you distilled across two different tokenizers with `wasserstein` or `topk_align` on any earlier release, that run is not salvageable, so re-run it with `wasserstein_aligned`.**

>

> A second defect in the same family shipped alongside: the ULD loss **ignored the response-only label mask and the causal shift** that the cross-entropy term already applied, so under the default `train_on_responses_only` it was optimising prompt tokens and the shift-boundary position too. Both loss functions now take the labels and mask on `labels != -100` after the same shift.

## `training.minillm_enabled` — reverse-KL with 3 stability tricks bundled

```yaml
task: distill
training:
  teacher_model: meta-llama/Llama-3.1-8B-Instruct   # required by task: distill
  minillm_enabled: true
  minillm_teacher_mix_ratio: 0.3
  minillm_length_normalize: true
  minillm_pretrain_anchor_weight: 0.1
  minillm_pretrain_anchor_path: ./pretrain.jsonl
```

Gu et al. 2024 ([arXiv 2306.08543](https://arxiv.org/abs/2306.08543)). All three §3 stability tricks bundled: teacher-mixed sampling (mix teacher samples into the on-policy rollout), length normalisation (per-token KL averaged), pretrain-loss anchor (regularise toward an anchor distribution at weight α).

There is **one real CLI flag** in this family, and everything above is config:

```bash
soup train --config distill.yaml --minillm-on-policy
```

It switches the rollout from a teacher-forced approximation to a genuine on-policy one: a fresh autoregressive sample is drawn from the teacher-student mixture each step, then scored with the length-normalised reverse KL. `training.minillm_rollout_length` sizes it, defaulting to `min(max_length, 32)`.

Cross-validators **reject silent no-ops**:

- `anchor_weight=0` with `anchor_path` set → error
- `anchor_weight > 0` with `path = None` → error

Gated to `task='distill'`. **Live as of v0.71.11** — the teacher-mixed, length-normalised reverse-KL term plus the optional pretrain-anchor SFT term train end-to-end; the anchor reader is cwd-contained + symlink-rejecting with a per-line byte cap.

## `training.rl_checkpoint_save_every_steps` — mid-epoch PPO/GRPO ckpt

```bash
# config keys under training:, not CLI flags
#   rl_checkpoint_save_every_steps: 200
#   rl_checkpoint_keep_last: 4
#   rl_checkpoint_include_optimizer: true
#   rl_checkpoint_include_ref_model: true
#   rl_checkpoint_include_rollout_buffer: true
soup train --config ppo.yaml
```

TorchTune explicitly punts mid-epoch checkpointing. Soup enforces the bounds `save_every_steps ∈ [1, 10M]`, `keep_last ∈ [1, 100]` (oldest pruned).

Composes with v0.32 spike recovery + v0.40 reference-model regen — recovery now hops to the **most recent mid-epoch ckpt** instead of restarting the epoch on a PPO crash. **Live as of v0.71.11** — it writes a real adapter + optimizer state + JSON manifest every N steps and prunes to `rl_checkpoint_keep_last`. (v0.71.11 also makes the GRPO reference-model EMA update in place, eliminating the three model-sized allocations per step.)

## `soup iterative-dpo` — sample → score → re-pair → retrain driver

```bash
soup iterative-dpo --base-model registry://policy-v3 \
  --reward-model ./rm \
  --prompts ./prompts.jsonl \
  --output-dir ./iter-dpo \
  --rounds 4 --pairs-per-round 4000
```

`--base-model`, `--reward-model`, `--prompts` and `--output-dir` are all required here; unlike `soup train`, this driver takes the reward model as a flag rather than from a config.

Frozen `IterativeDPOPlan` with a **consecutive-`round_index`** invariant and canonical per-round artifacts:

```
./iter-dpo/round-01/pairs.jsonl
./iter-dpo/round-01/adapter/
./iter-dpo/round-02/pairs.jsonl
./iter-dpo/round-02/adapter/
...
```

So a crashed run resumes cleanly. `--plan-only` renders the validated plan and exits 0. **Live as of v0.71.11** — each round samples completions from the previous round's adapter, then trains a fresh LoRA from the base on that round's harvested pairs.

## `training.echo_trap_enabled` — RAGEN multi-turn n-gram repetition detector

```bash
soup train --config grpo.yaml \
  # config keys under training: echo_trap_enabled \
  #   echo_trap_threshold: 0.6 \
  #   echo_trap_halt: true
```

Zhu et al. 2025 ([arXiv 2504.14437](https://arxiv.org/abs/2504.14437)). Pure-Python n-gram repetition rate per trajectory + a batch mean — when an agent's rollout collapses into "echoing itself" (the same n-gram pattern appearing repeatedly within and across turns), this catches it before the reward model rewards the degenerate policy.

**`--echo-trap-tokenizer-aware` is the one real CLI flag here**, and the trade-off is worth stating before you reach for it: scoring repetition over tokens rather than characters catches subword repetition that punctuation-heavy text hides, but it makes the score **tokenizer-specific** instead of vocabulary-agnostic, so two runs on different tokenizers stop being comparable. Everything else in this family (`echo_trap_enabled`, `echo_trap_threshold`, `echo_trap_halt`) is a `training.` config key, not a flag.

OK / WARN / TRAP bands at 0.30 / 0.60. DoS caps `_MAX_NGRAM_N=32`, `_MAX_TRAJECTORY_TOKENS=1M`, `_MAX_BATCH_TRAJECTORIES=100k`. Gated to `task in {grpo, ppo}` non-mlx. Composes with v0.53.11 `GRPOStabilityCallback`. **Live as of v0.71.11** — the GRPO callback scores per-trajectory n-gram repetition, logs the verdict, and halts on TRAP when `training.echo_trap_halt` is set.

## Numbers

+337 tests in v0.70.0 (11,487 → 11,824); the live wiring in v0.71.11 is part of the broader v0.71 sweep, which closed at **16,529 tests across 319 files** in v0.71.41. As of v0.74.0 the suite spans **475 test files**; upstream stopped publishing a total it counted at the tag, so this page names the number that reproduces and not one it cannot check.

## See also

- [Closed-loop reward-hacking auto-mitigation (v0.71.26)](/docs/reward-hack-mitigation) — the release that turns these detectors from "halt" into "self-correct".
- [Lean install + live wiring (v0.71)](/docs/lean-install-live-wiring) — the release that made all six of these surfaces real.
- [Adapter lifecycle (v0.67)](/docs/adapter-lifecycle) — `soup adapters bisect` finds which mid-epoch ckpt regressed.
- [Anti-trend insurance (v0.68)](/docs/anti-trend-insurance) — `soup distill-prompt` + ULD pair up to bridge tokeniser gaps.
- [Soup Loop (v0.58)](/docs/soup-loop) — iterative-DPO runs inside a `soup loop` iteration.

[PreviousPrompt Compile & Distill](/docs/anti-trend-insurance)[NextReward-Hack Auto-Mitigation](/docs/reward-hack-mitigation)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="038-reward-hack-mitigation"></a>

# 38. Closed-loop reward-hacking auto-mitigation (v0.71.26)

*Source: <https://trysoup.dev/docs/reward-hack-mitigation>*

The reward-hack and echo-trap detectors from [loop hardening](/docs/loop-hardening) can \*halt\* a degenerate RL run. **v0.71.26 closes the loop**: the GRPO/PPO trainer now **detects reward hacking mid-run and self-corrects** — it raises the KL penalty, shapes the reward, rolls back to the last-good checkpoint, and only early-stops as a last resort.

> We have not found an open-source RLHF library that closes the loop from **detection → automatic correction → continue**. The ones we checked detect, or they halt. Soup steers the run back on course. That is the whitespace this release aims at.

## The one flag

```bash
soup train --config grpo.yaml \
  --reward-hack-mitigation off | log_only | kl_control | pid_lagrangian
```

It requires a `reward_hack_detector` (`info_rm` or `rm_ensemble`) on a `grpo` / `ppo` transformers run. The config-file equivalent is `training.reward_hack_mitigation`.

## Four modes, escalating

### `log_only` — the eyes (no control action)

Streams a per-step `mitigation_log.jsonl` under the run directory: raw signal, health, `drop_pct`, OK / WARN / HACK verdict, current β / kl\_coef, reward mean/std, completion-length mean and trend, and n-gram repetition. It **provably never mutates β or kl\_coef** — run it first to \*see\* hacking happen before you let the controller act. The log writer is cwd-contained with rotation, secret redaction, and symlink-reject-on-rotate.

### `kl_control` — reversible bang-bang controller with hysteresis

When a **multi-signal vote** (InfoRM cluster-separation or RM-ensemble divergence, plus completion `length_trend` and n-gram `repetition`) stays above the trip band for a dwell window, the controller **raises β** (the KL coefficient) multiplicatively, clamped to `[reward_hack_beta_floor, reward_hack_beta_ceil]`, **never crossing zero**. Once the signal recovers below the release band for the patience window, it **relaxes β** back toward the floor. Dwell + release-patience are the hysteresis that stops it flapping.

β is written to **both** `trainer.beta` and `trainer.args.beta`, so it takes effect on stock GRPO **and** Soup's GRPO variants (gspo / dapo / dr\_grpo / …), and to `trainer.args.kl_coef` on PPO.

### `pid_lagrangian` — principled control + a safety net

Replaces bang-bang with a **PID-Lagrangian controller** (Stooke et al. 2020, "Responsive Safety in RL via PID Lagrangian Methods"): it treats "hacking signal ≤ target" as a constraint whose Lagrange multiplier (the β / KL coefficient) is updated by a PID law with integral **anti-windup** and an output clamp. On persistent hacking it climbs an **escalation ladder**:

1. **Raise KL** continuously toward the target.
2. **Roll back** to the last-good RL checkpoint (requires `training.rl_checkpoint_save_every_steps`), dropping LR / raising β on resume.
3. **Early-stop cleanly** with a plain-English **give-up explanation** — which signal, for how long, and what the controller tried — surfaced through `soup why`.

### Anti-gaming hardening (any control mode)

So the controller itself can't be gamed: per-signal **EMA or median smoothing**, **conservative-on-disagreement** voting (when detectors disagree, keep KL high), a reward-**distribution-drift** guard (catches a policy shifting its reward distribution to fool the top/bottom split), and optional **bounded reward shaping** — a capped penalty on the gamed proxy (length / repetition / sentinel token) applied over the reward-function seam and always logged.

## Example config

```yaml
# soup.yaml
base: HuggingFaceTB/SmolLM2-135M
task: grpo
data:
  train: ./prompts.jsonl
training:
  reward_hack_detector: info_rm
  reward_hack_mitigation: pid_lagrangian  # off | log_only | kl_control | pid_lagrangian
  rl_checkpoint_save_every_steps: 50      # required by reward_hack_rollback below
  reward_hack_beta_floor: 0.02            # positive floor, so β never crosses 0
  reward_hack_beta_ceil: 1.0
  reward_hack_trip_band: 0.30             # raise β above this drop_pct
  reward_hack_release_band: 0.10          # relax β below this
  reward_hack_dwell_steps: 2              # consecutive trips before acting (hysteresis)
  reward_hack_release_patience: 3
  reward_hack_signals: ["info_rm", "length_trend"]
  reward_hack_kl_gain: 1.5                # how hard a trip raises beta
  # pid_lagrangian only. These are REFUSED at config load under any other
  # mitigation mode, so commenting out the mode rather than these keys does
  # not work: a YAML comment does not disable a key that is still set.
  reward_hack_pid_kp: 0.5
  reward_hack_pid_ki: 0.05
  reward_hack_pid_kd: 0.1
  reward_hack_signal_target: 0.15         # the setpoint the controller holds
  reward_hack_integral_clamp: 1.0         # anti-windup bound on the I term
  reward_hack_rollback: true              # enable the rollback rung
  reward_hack_rollback_patience: 3        # trips before rolling back
  reward_hack_max_recovery_attempts: 2    # then early-stop with a soup why
  # optional hardening
  reward_hack_signal_smoothing: ema       # none | ema | median
  reward_hack_conservative_on_disagreement: true
```

The config above is the `pid_lagrangian` shape, because the PID tunables and `reward_hack_rollback` are **refused at config load** under `kl_control` rather than ignored, and `reward_hack_rollback: true` separately requires `rl_checkpoint_save_every_steps`. For plain `kl_control`, keep everything down to `reward_hack_kl_gain` and delete the PID block.

> **`pid_lagrangian` has never had a valid run** (upstream #371, still open at v0.75.0). The mechanism is implemented and the mode is selectable; its efficacy is not established. `kl_control` is the mode with a demonstrated mid-run rollback behind it.

## Honest limitations

This is an RL feature, so it cannot ship "schema-only" — a controller that mutates training dynamics is only real if a logged run shows it working. On the maintainer's single RTX 3050 that means **proof-of-mechanism only**:

- Validated on **SmolLM2-135M + a synthetic length-hacking task**, with all four modes live including a **real mid-run rollback**.
- **PPO ships BETA** — the signal buffer and `kl_coef` mutation are wired and unit-tested, but the on-GPU proof is **GRPO-only**.
- Whether the loop suppresses hacking **without collapsing true reward on 7B+ models with real reward models** is an open, community-validatable question, tracked in [issue #286](https://github.com/MakazhanAlpamys/Soup/issues/286). Contributors with larger GPUs (or `soup train --cloud modal`) can reproduce the experiments and report back.
- `reward_hack_mitigation` in `{kl_control, pid_lagrangian}` is **mutually exclusive** with a DPO-style β schedule / `ref_model_ema_alpha` (both drive the KL / ref dynamics).

## Numbers

+184 tests in `tests/test_v07126.py`, taking the suite to **14,788 across ~298 files**.

## See also

- [Loop hardening (v0.70 → live v0.71.11)](/docs/loop-hardening) — the detectors this feature turns from "halt" into "self-correct".
- [Lean install + live wiring (v0.71)](/docs/lean-install-live-wiring) — the release line this caps.
- [GRPO Plus](/docs/grpo-plus) — the GRPO variants β mutation reaches on both code paths.
- [soup ship](/docs/soup-ship) — the post-training SHIP / DON'T-SHIP verdict that pairs with a hardened run.

[PreviousLoop Hardening](/docs/loop-hardening)[NextLean Install + Live Wiring](/docs/lean-install-live-wiring)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="039-lean-install-live-wiring"></a>

# 39. Lean install + live wiring (v0.71.0 → v0.71.41)

*Source: <https://trysoup.dev/docs/lean-install-live-wiring>*

The v0.71 line is two stories plus a run of capstones: a **leaner install**, a release-long **live-wiring sweep** that turned the entire schema-first roadmap into working code, and **native Spectrum targeted training**. v0.71.24 expanded the recipe catalog to **133** with the 2026 open-weight model families, **v0.71.25 added [`soup ship`](/docs/soup-ship)** (the one-command SHIP / DON'T-SHIP verdict), **v0.71.26 closed the RL loop** with [reward-hacking auto-mitigation](/docs/reward-hack-mitigation), **v0.71.27 "Fine-tune Doctor"** added a pure-CPU pre-flight ([`soup data doctor`](/docs/fine-tune-doctor) + `soup data lint`), **v0.71.28 shipped the [`soup mcp serve`](/docs/mcp-server) MCP server**, and **v0.71.29 added [`soup shrink`](/docs/soup-shrink)** (one-command depth pruning + distill-heal with a SHIP / DON'T-SHIP perplexity verdict), **v0.71.30 let a Process Reward Model drive GRPO** ([PRM-guided GRPO](/docs/prm-guided-grpo)), **v0.71.31 shipped the judge-in-the-loop suite** ([Online DPO](/docs/online-dpo), [best-of-N & Evol-Instruct](/docs/best-of-n-evolve), and a pairwise judge win-rate for [`soup ship`](/docs/soup-ship)), **v0.71.32 added [ASR fine-tuning](/docs/asr-fine-tuning)** (`task: asr` fine-tunes Whisper locally, with built-in WER/CER), **v0.71.33 shipped [`soup draft`](/docs/soup-draft)** (measure whether speculative decoding pays off before you enable it, and the measurement said no on our own pair), **v0.71.34 added [adapter algebra](/docs/adapter-arithmetic) and [LISA](/docs/lisa)**, and **v0.71.35 shipped the [compliance pack](/docs/compliance-pack)** (regulation-shaped `init` templates, `soup card` model-card autogen, a `soup ci init` PR gate, and GGUF export that finally works on Windows). v0.71.36 "Data Moat II" then added a semantic layer over your training data ([`soup data dedup --semantic`](/docs/data-moat-ii), `soup data topics`, `soup data canary`, `soup train --replay`), and the patch v0.71.37 fixed the Windows cmd.exe install-hint quoting. The v0.71 line closed with the eval-gate wedge: **v0.71.38** gave the [`soup ship`](/docs/soup-ship) regression leg real teeth (answer-extraction scoring over seven bundled offline suites, not substring-matched trivia), **v0.71.39** closed the evidence loop (`soup ship --emit-evidence` + a committed `ShipConfig` + `--push owner/repo#N`, provenance-bound so it is CI for weights on every PR), and **v0.71.40 + v0.71.41 shipped [Reward Forge](/docs/reward-verifier)** (`soup reward synth` generates a deterministic reward verifier from your data and refuses a degenerate one, `soup reward stress` proves it cannot be gamed). Across the v0.71 line the test suite grew from 11,824 to **16,529** across **319** files. (the v0.72 and v0.73 lines have since taken it to 475 test files at v0.74.0.)

## v0.71.0 — the install split (breaking)

`pip install soup-cli` is now a light, **PyTorch-free** CLI + data-tools install. The heavy training stack (`torch`, `transformers`, `peft`, `trl`, `datasets`, `bitsandbytes`, `accelerate`) moved to a `[train]` extra.

```bash
pip install soup-cli            # light: CLI + config + data tools, no PyTorch
pip install "soup-cli[train]"   # add the training stack to fine-tune
pip install "soup-cli[all]"     # train + serve + ui + data + mcp
```

- `soup init`, `soup data …`, and the inspection commands work on the bare install; `soup train` needs `[train]`.
- A missing heavy dependency surfaces a friendly \*"Training needs the [train] extra. Run: pip install "soup-cli[train]""\* message.
- **Python 3.10+** is now the floor (raised from 3.9). The repo moved to a `src/` layout, the coverage gate rose to 77%, and a `py.typed` marker ships typed hints.

## v0.71.1 → v0.71.14 — the roadmap goes live

Almost everything that previously shipped \*"schema-first, live next patch"\* is now real, validated end-to-end on tiny models (SmolLM2-135M / a real RTX 3050).

### Training & RL (v0.71.11)

- `--reward-hack-detector info_rm|rm_ensemble` — live GRPO callback (InfoRM cluster-separation or RM-ensemble divergence), halts on HACK.
- `echo_trap_enabled` — live RAGEN n-gram-repetition detector, halts on TRAP.
- `uld_strategy: wasserstein|topk_align` — a real Universal Logit Distillation loss, for a teacher and student that **share a tokenizer** (two sizes in one family). Since v0.75.0 both refuse a pair that is not interchangeable, because they forward the student's token ids to the teacher unchanged; [`wasserstein_aligned` is the cross-tokenizer one](/docs/loop-hardening).
- `minillm_enabled` — live teacher-mixed, length-normalised reverse-KL with a pretrain anchor.
- `rl_checkpoint_save_every_steps: N` — real mid-epoch PPO/GRPO checkpoints (adapter + optimizer + manifest), pruned to `rl_checkpoint_keep_last`.
- `soup iterative-dpo` — runs the full sample → RM-score → re-pair → DPO-train loop over N rounds.
- The GRPO reference-model EMA now updates in place (no full-state-dict copies).

### Architecture & PEFT (v0.71.12)

- `task: distill` gains `distill_mode: token|sequence` (sequence-level hard-label KD).
- Classifier / reranker / cross-encoder LoRA attaches to the head.
- LLaMA Pro block expansion is per-architecture (Llama / Qwen / Mistral); LongLoRA S² shifted-sparse attention installs its forward override; Mixture-of-Depths (`use_mod: true`, with `mod_capacity_factor` defaulting to 0.125) routes a top-k token subset per layer; it is live for SFT and pretrain on Llama, Qwen and Mistral, an unsupported architecture warns and skips, and you pick exactly one of MoD, LLaMA Pro and LongLoRA.
- `soup serve --bank <bank.json>` — VeRA / VB-LoRA multi-tenant serving, per-request `X-User-Id`, ~KB per persona.
- `task: moe_lora_routing` — MoLE per-token gate over N frozen task LoRAs (only the router trains).

### RAG, steering & editing (v0.71.9 – v0.71.10)

- `data.format: raft` — answer-only span-mask training with `[doc-N]` citation labels; `soup ra-dit` is the two-stage retriever → generator orchestrator with Registry auto-link.
- `soup steer train/apply` + `soup serve --steer` — CAA / ITI / RepE control vectors at decode time.
- `soup eval citation` — precision / recall / F1 over RAFT rows.
- `soup edit set` — live ROME / MEMIT / AlphaEdit rank-1 weight edits with an SQLite EditGovernor; live GRACE codebook.
- `soup train with task: unlearn` — live NPO / SimNPO / RMU.

### Probes & eval (v0.71.7 – v0.71.8)

- Real linear-probe math with operator-supplied weights; `soup probe sae-diff --auto-download` (allowlisted SAE from the Hub); `soup probe truth` / `soup probe harm`; `soup probe interference --measure` (live PEFT multi-adapter N×N matrix); `soup train --capture-activations`.
- Live runners for `soup advise run --probe-model`, `soup tunability --live`, `soup eval capability --live`, `soup eval behavior`, and `soup diagnose`.

### Data engineering (v0.71.6)

- `soup build` materialises datasets (5 built-in transforms, incremental re-tokenise-only-changed-rows via a SQLite state store).
- `soup data gen-magpie` generates via chat-template-prefix harvest (`ollama` / `vllm`, SSRF-hardened).
- `soup eval irt-subset` adds 2PL / 3PL fits.

### Prompt-compile (v0.71.13, `[compile]` extra)

- `soup compile`, `soup distill-prompt`, `soup compile-tools`, and `soup local-rl train` (a real nightly DPO/KTO/ORPO trainer) are live.

### Governance & supply chain (v0.71.2 – v0.71.3)

- Real **ed25519** detached signatures for `soup adapters sign` / `soup attest` (`[sign]` extra).
- Anti-AI-jacking trust-on-first-use namespace pins on Hub downloads; automatic license auto-detection + a backdoor-scan gate at `soup adapters merge`.
- `soup train --track-energy` (codecarbon offline kWh / CO2); PDF Annex XI/XII docs; Soup Can manifest v3 with embedded in-toto attestations; a `~/.soup/audit.jsonl` audit log on every command; airgap reproducibility receipts.

### Export & serve finale (v0.71.14)

- `soup merge-sharded-fsdp-weights` — live FSDP shard consolidation into one `.safetensors` (no arbitrary pickle exec).
- `soup serve --kv-cache-type bf16|f16|q8_0` — live KV-cache typing on the transformers backend. `fp8` is accepted by the schema and unreachable: vLLM and SGLang routing raises `NotImplementedError`, and on transformers it raises unconditionally, so a Hopper card does not make it work.
- ONNX export verified end-to-end. GGUF / AWQ / GPTQ export QA and HF Spaces deploy remain `infra-blocked`. (Since closed in part: GGUF was validated end-to-end on Windows in v0.71.35, and v0.74.0 repaired the GPTQ export path, which now requires `--calibration-data`, and made TensorRT export fail fast instead of writing zero bytes. HF Spaces deploy is still infra-blocked.)

## v0.71.15 → v0.71.23 — the stub tail closes, and Spectrum lands

With the roadmap live, the patch chain closed the remaining stubs and added new capability, all validated on a real RTX 3050 / SmolLM2 box (hardware-only paths ship BETA-gated, never faked).

### Native Spectrum targeted training (v0.71.23)

`soup spectrum scan --model <id> --top-percent 50` streams a model's safetensors one tensor at a time (no model load, peak RAM is the largest single matrix), computes a singular-value SNR per weight with a Marchenko-Pastur noise threshold, and prints a ready-to-paste `training.unfrozen_parameters` block. Full-fine-tune only the high-signal layers, scanning even a very large model on a CPU box. See [Spectrum targeted training](/docs/spectrum-targeted-training).

### Serve & RAG finish (v0.71.17)

- `soup serve --mole <dir>` — serve-time MoLE blends N frozen task LoRAs per token at decode (companion to the v0.71.12 train-time gate).
- `soup serve --bank` resolves the active VeRA / VB-LoRA user per request via the `X-User-Id` header (multi-worker safe, no cross-request leak).
- RAFT distractors get an epoch-aware shuffle salt; `soup diagnose --citation-style` threads the style + seed into the live citation probe.

### Distill & agent depth (v0.71.18, KV-cache in v0.71.22)

- MiniLLM true on-policy rollout (Gu et al. §3.1), with the O(L²) per-step cost resolved by a cached `past_key_values` path.
- `uld_strategy: wasserstein_aligned` — character-span alignment for two **different** tokenizers, disjoint or merely mismatched (Llama → Mistral, GPT-2 BPE ↔ Llama SentencePiece). This is the only ULD strategy that re-tokenizes, and since v0.75.0 it is the one the other two name when they refuse a mismatched pair.
- `soup agent eval --sandbox` — execute tool-call predictions in the v0.25 RLVR sandbox.
- `soup train --cloud modal` — render a serverless Modal GPU app from your `soup.yaml` (plan-only by default; `--cloud-submit` for live). `--cloud lambda` renders a Lambda Cloud plan the same way as of v0.74.0, and the API key never enters the instance: termination belongs to a local controller whose `finally` both terminates and polls to confirm it happened.

### Knowledge-edit depth (v0.71.16)

- ROME / MEMIT / AlphaEdit now edit GPT-2 (`Conv1D`) and Mixtral, not just Llama.
- `soup edit set --method rome --cov-corpus <jsonl>` — covariance-preconditioned ROME (the genuine closed form; falls back to `C=I` without a corpus).

### Modality II + precision go live, BETA-gated (v0.71.19 – v0.71.21)

- TTS trainer live for Orpheus / Sesame-CSM / Llasa / Spark / Oute (`task: tts`); BitNet 1.58-bit trainer + `soup export --format bitnet|tq1_0`; MoE expert quant + `train_router_only`.
- `fp8_attention` + `nvfp4` torchao converters (Hopper / Blackwell gate), vLLM sleep-mode, `openenv` agent rollout, `soup apple-adapter` PEFT ↔ MLX round-trip, and `soup delinearize-llama4` all live.
- The Quant Menu (`gptq` / `awq` / `hqq` / …) now threads through the vision and audio modality paths.

## v0.71.24 — the 2026 model-family recipe expansion

The catalog grew from **116 to 133** ready-made recipes: **17 new SFT recipes** for the open-weight models released February to June 2026, each with its Hugging Face repo-ID verified to resolve.

| Family | Recipes | License | Notes |
| --- | --- | --- | --- |
| **Qwen 3.5** | `qwen3.5-0.8b/2b/4b/9b/27b-sft` + `qwen3.5-35b-a3b/122b-a10b/397b-a17b-sft` (MoE) | Apache-2.0 | 262K context, native vision |
| **Qwen 3.6** | `qwen3.6-27b-sft`, `qwen3.6-35b-a3b-sft` | Apache-2.0 | dense + MoE |
| **DeepSeek-V4** | `deepseek-v4-flash-sft`, `deepseek-v4-pro-sft` | MIT | Pro is 1.6T-class MoE (multi-GPU) |
| **GLM-5.1** | `glm-5.1-sft` | MIT | 754B MoE (multi-GPU) |
| **Kimi** | `kimi-k2.5-sft`, `kimi-k2.6-sft` | Modified MIT | ~1T agentic MoE (multi-GPU) |
| **MiniMax M3** | `minimax-m3-sft` | MiniMax Community License | 428B; **commercial use needs a separate agreement** |
| **Mistral Large 3** | `mistral-large-3-sft` | Apache-2.0 | 675B/41B-active multimodal MoE (multi-GPU) |

The giants ship as multi-GPU recipes (mirroring the existing `llama3-70b-fsdp2` / `qwen3-32b-zeropp` / `deepseek-v3-pipeline` configs), so size is never a blocker for `soup recipes use`. This release also fixed a stale repo-ID: the `glm-5` recipe now points at `zai-org/GLM-5` after the org migrated from `THUDM`. Drop one in with `soup recipes use qwen3.5-9b-sft`, point `data.train` at your dataset, and run `soup train`.

## v0.71.25 — soup ship + friendlier errors

v0.71.25 adds **[`soup ship`](/docs/soup-ship)**: after a fine-tune, one command answers the only question that matters, did the model get better or did I break it, as a single **SHIP / DON'T-SHIP** verdict. It fuses a strict task-win check with a catastrophic-forgetting gate, so a model that wins your task but regresses general benchmarks is refused. Exit codes are CI-gateable (0 = SHIP, 2 = DON'T SHIP, 1 = error), and `--evidence` decides offline with no model load. See the [`soup ship` page](/docs/soup-ship) for the decision rule and flags.

v0.71.25 also makes common load failures friendlier: the CUDA-OOM hint now suggests `gradient_checkpointing` and `4bit` quantization, and there are clear new messages for Hugging-Face-gated repos (`huggingface-cli login` / `HF_TOKEN`) and `trust_remote_code`.

## v0.71.26 — closing the RL loop

v0.71.26 ships **[closed-loop reward-hacking auto-mitigation](/docs/reward-hack-mitigation)**: the GRPO/PPO trainer now \*detects\* reward hacking mid-run and \*self-corrects\* instead of only halting. `soup train --reward-hack-mitigation off|log_only|kl_control|pid_lagrangian` adds a controller that raises the KL penalty on a multi-signal vote, holds the hacking signal at a target with a PID-Lagrangian law, rolls back to the last-good checkpoint, and early-stops with a plain-English give-up explanation. We are not aware of another open-source RLHF library that closes this loop. It ships as **proof-of-mechanism** on SmolLM2-135M (PPO BETA); scale validation is [issue #286](https://github.com/MakazhanAlpamys/Soup/issues/286). The release also adds a ready-made `qwen2.5-coder-7b-sft` recipe (catalog 133 → 134) and friendlier CUDA-OOM / gated-repo / trust\_remote\_code errors.

## v0.71.27 — Fine-tune Doctor

v0.71.27 adds a pure-CPU, zero-GPU pre-flight that kills the top silent fine-tune failures before a single training step, something we have not found in Unsloth, Axolotl or LLaMA-Factory. **[`soup data doctor`](/docs/fine-tune-doctor)** runs 8 chat-template checks against the real tokenizer, including `eos_in_labels` (the number-one "model never stops generating" bug) and `bos_duplication`, with the same OK / MINOR / MAJOR taxonomy as `soup diagnose` (exit 2 on MAJOR); `--show-mask N` colours each token trained-versus-masked through the real collator path. **`soup data lint`** is a preference-data linter for `dpo/orpo/simpo/ipo/bco/kto` that flags length-bias as a Cohen's d effect size, plus label imbalance, near-duplicates, identical pairs and prompt leak. See the [Fine-tune Doctor page](/docs/fine-tune-doctor).

## v0.71.28 — the MCP server

v0.71.28 ships **[`soup mcp serve`](/docs/mcp-server)**, a Model Context Protocol server so any MCP client (Claude Code, Cursor, Cline, Continue) can drive Soup over stdio. No other fine-tuning CLI ships one. It exposes 16 tools: 14 read-only ones that map to Soup commands and return JSON (advise, data inspect/validate/score/doctor, recipes search/show, runs, registry, profile, diagnose, ship) plus 2 plan-only mutating tools (`train_start`, `export`) behind `--allow-mutating` that only render the command they would run. (Since v0.73.3 there are **18**: `--allow-execute` adds `train_execute` and `export_execute`, which run a plan behind a single-use server-issued token.) Transport was stdio only in that release (no network listener; sse and http arrived in v0.74.0), output is control-char sanitized, paths are cwd-contained, and it installs behind a lazy-imported `[mcp]` extra so the core stays PyTorch-free. v0.71.28 also completes vocab-expansion parity across every preference and RL trainer. See the [MCP server page](/docs/mcp-server).

## See also

- [Compliance pack (v0.71.35)](/docs/compliance-pack) — init templates, model-card autogen, a CI gate, and GGUF that works on Windows.
- [Adapter algebra (v0.71.34)](/docs/adapter-arithmetic) and [LISA (v0.71.34)](/docs/lisa) — task arithmetic over LoRAs, and full-FT quality at LoRA memory.
- [soup draft (v0.71.33)](/docs/soup-draft) — measure whether speculative decoding pays off before you enable it.
- [PRM-guided GRPO (v0.71.30)](/docs/prm-guided-grpo) — a Process Reward Model as the per-step GRPO reward.
- [soup shrink (v0.71.29)](/docs/soup-shrink) — depth-prune + distill-heal with a perplexity verdict.
- [ASR fine-tuning (v0.71.32)](/docs/asr-fine-tuning) — fine-tune Whisper on your own audio, WER/CER built in.
- [Online DPO (v0.71.31)](/docs/online-dpo) and [Best-of-N & Evolve (v0.71.31)](/docs/best-of-n-evolve) — the judge-in-the-loop suite.
- [MCP server (v0.71.28)](/docs/mcp-server) — drive Soup from your coding agent.
- [Fine-tune Doctor (v0.71.27)](/docs/fine-tune-doctor) — pre-flight chat-template + preference-data checks.
- [Closed-loop reward-hacking auto-mitigation (v0.71.26)](/docs/reward-hack-mitigation) — the capstone that closes the RL loop.
- [Loop hardening (v0.70 → live v0.71.11)](/docs/loop-hardening) — the six detectors, now real.
- [Supply-chain security](/docs/supply-chain-security) — ed25519 signing + merge gates.

[PreviousReward-Hack Auto-Mitigation](/docs/reward-hack-mitigation)[NextSpectrum Training](/docs/spectrum-targeted-training)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="040-spectrum-targeted-training"></a>

# 40. Spectrum targeted training (v0.71.23)

*Source: <https://trysoup.dev/docs/spectrum-targeted-training>*

**Spectrum** picks the layers worth training. Instead of a full fine-tune (every weight) or a blanket LoRA (every layer, low rank), `soup spectrum scan` ranks each weight matrix by its **signal-to-noise ratio** and lets you full-fine-tune only the high-signal layers. You get most of the quality of a full fine-tune at a fraction of the memory and compute.

> The reference Spectrum implementation needs the model on a GPU to scan its layers. Soup's scanner streams the `.safetensors` shards one tensor at a time, so it never loads the model. Peak RAM is the largest single weight matrix, which means you can scan a 70B on a laptop CPU.

## Scan a model

```bash
soup spectrum scan --model meta-llama/Llama-3.1-8B --top-percent 50
```

```bash
# write the patch straight to a file, restrict to specific module types
soup spectrum scan --model ./my-merged-model \
  --top-percent 25 \
  --modules mlp,attn \
  --output patch.yaml
```

| Flag | Default | Description |
| --- | --- | --- |
| `--model` | (required) | HF Hub id or local path. Streamed shard-by-shard, never loaded. |
| `--top-percent` | 50 | Keep the top N% of layers by SNR, per module-type group. |
| `--modules` | `all` | Restrict the scan to `mlp`, `attn`, or a comma list. |
| `--output` | (stdout) | Write the `training.unfrozen_parameters` block to a file (kept under cwd). |
| `--no-cache` | off | Skip the scan cache at `~/.soup/spectrum/<slug>.json`. |

The command prints a per-group SNR table and a ready-to-paste config block.

## Train on the result

The scan emits a `training.unfrozen_parameters` list of regex patterns. Drop it into your `soup.yaml`:

```yaml
base: meta-llama/Llama-3.1-8B
task: sft
data:
  train: ./data/train.jsonl
training:
  quantization: none
  unfrozen_parameters:
    - "model.layers.(2|5|8|11).mlp.down_proj"
    - "model.layers.(2|5|8).self_attn.v_proj"
```

```bash
soup train --config soup.yaml
```

The SFT trainer freezes every parameter, then unfreezes only the matched set. This is a **full fine-tune of a subset of layers** (the matched weights train at full precision), not LoRA.

## How the SNR ranking works

For each weight matrix, Spectrum takes the singular values and applies a **Marchenko-Pastur** noise threshold ([arXiv:2406.06623](https://arxiv.org/abs/2406.06623)): singular values above the random-matrix noise floor carry signal, the rest are noise. The ratio of signal energy to total energy is the layer's SNR. Layers are ranked within each module-type group, so attention and MLP layers compete with their own kind rather than against each other.

The kernel is pure-numpy and **transpose-invariant** (the singular values of `W` and `W.T` are identical), so GPT-2 `Conv1D` weights (`c_attn` / `c_fc` / `c_proj`) are recognised alongside Llama-style `nn.Linear` names.

## Constraints

`training.unfrozen_parameters` requires a full-precision SFT run and is mutually exclusive with the LoRA stack and the other layer-selection knobs:

- requires `task: sft`, `backend: transformers`, `modality: text`, `quantization: none`
- mutually exclusive with LoRA features, `freeze_layers`, `freeze_ratio`, `train_router_only`, `expand_layers`, and `stream_layers` (streaming keeps the base frozen on the `meta` device, so there is nothing for Spectrum to unfreeze)

Patterns are validated at parse time: nested-unbounded-quantifier regexes (ReDoS), null bytes, and empties are rejected, with caps on count (50k) and length (512). Hub downloads route through the SSRF-hardened, namespace-pinned loader; symlinked shards and matrices above a 2^31-element SVD cap are skipped, and `--output` stays under the working directory.

## See also

- [Lean install + live wiring (v0.71)](/docs/lean-install-live-wiring) — the release line Spectrum caps off.
- [LoRA quality](/docs/lora-quality) — when a blanket low-rank adapter is the better trade-off.
- [Optimizer & PEFT zoo](/docs/optimizer-zoo) — freeze ratios, LLaMA Pro, and the rest of the parameter-efficiency menu.

[PreviousLean Install + Live Wiring](/docs/lean-install-live-wiring)[NextLISA](/docs/lisa)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="041-lisa"></a>

# 41. LISA (v0.71.34)

*Source: <https://trysoup.dev/docs/lisa>*

LISA (Layerwise Importance Sampled AdamW, [arXiv:2403.17919](https://arxiv.org/abs/2403.17919)) reaches for full-fine-tuning quality without a full fine-tune's memory. On the quality half it delivers, measured at 3B and 8B. On memory it beats full fine-tuning and **loses to LoRA**, by a margin that widens with scale, which is [measured below](#measured-at-3b-and-8b-and-half-the-pitch-did-not-survive) rather than glossed. Where [Spectrum](/docs/spectrum-targeted-training) picks the layers **once** and trains that fixed set, LISA re-samples a small random set of decoder layers **every N steps** and freezes the rest. The input embeddings, the LM head, and the final norm stay trainable throughout.

```yaml
task: sft
backend: transformers
modality: text
training:
  quantization: none       # LISA is a full fine-tune of the active layers
  lisa_enabled: true
  lisa_num_layers: 2       # decoder layers active per interval (clamped to model depth)
  lisa_interval_steps: 20  # re-sample cadence, in global steps
```

## Config fields

| Field | Default | Meaning |
| --- | --- | --- |
| `lisa_enabled` | `false` | Turns LISA on. |
| `lisa_num_layers` | `2` | Decoder layers trainable per interval, clamped to the model's depth. |
| `lisa_interval_steps` | `20` | How often, in global steps, the active set is re-sampled. |
| `lisa_reset_optimizer` | `true` | Clears optimizer state for layers as they are re-frozen. |
| `lisa_train_embeddings` | `true` | v0.74.0. `true` is LISA as published. Set it `false` to freeze the always-on group (input embeddings, LM head, final norm) so only the sampled decoder layers train. |

Setting any `lisa_*` field away from its default while `lisa_enabled` is `false` is a hard error, not a silent no-op.

**`lisa_train_embeddings: false` is a trade, not a free win, which is why it is opt-in.** The always-on group is about **70% of everything LISA trains at 8B**, so it is where LISA's memory actually goes, and freezing it changes what the run can learn. Two riders travel with it: the analytical VRAM pre-flight still treats LISA as a full fine-tune regardless of the flag, because crediting the frozen-embeddings saving needs a measured constant nobody has taken on GPU hardware, so a run that would now fit can still be conservatively refused, and `soup train --allow-oom-attempt` is how you launch it anyway.

**LISA also accepts `task: pretrain` as of v0.74.0.** Continued pre-training is the same rotating-full-fine-tune mechanism LISA was built for, so the supervised-only gate it had inherited from Spectrum was arbitrary. The rest of the gate is unchanged: transformers, text, `quantization: none`, and mutually exclusive with the LoRA feature flags, `freeze_layers` / `freeze_ratio` and `unfrozen_parameters`.

## Why it saves memory, and how much

Only a handful of layers train at any moment, and their optimizer state is cleared when they are re-frozen, so peak optimizer memory is roughly `embeddings + head + lisa_num_layers`, far below a full fine-tune. Unlike a static freeze, the active set keeps moving, so updates spread across the depth of the model instead of staying pinned to one slice. The set is drawn at random each interval, so that is a tendency rather than a guarantee: a short run fires few intervals and will not reach every layer.

### Measured at 3B and 8B, and half the pitch did not survive

LISA is often described, here included, as full fine-tuning quality at something like LoRA's memory. On an H100 80 GB, over Alpaca with 200 steps and three interleaved repeats per arm, **the quality half holds and the memory half does not.**

| Llama-3.1-8B-Instruct | Peak VRAM | Held-out loss |
| --- | --- | --- |
| Full fine-tuning | does not fit, 73.94 GB even at batch 1 | — |
| LISA, 2 layers every 20 steps | 52.14 GB | 1.294 |
| LoRA r=16 | **34.56 GB** | **1.275** |

| Qwen2.5-3B-Instruct | Peak VRAM | Held-out loss |
| --- | --- | --- |
| Full fine-tuning | 57.60 GB | 1.2905 |
| LISA, 2 layers every 20 steps | 19.37 GB | **1.2463** |
| LoRA r=16 | **15.93 GB** | 1.2420 |

**LISA beat full fine-tuning at both learning rates, so the quality claim stands.** But it costs **1.22x LoRA's memory at 3B and 1.51x at 8B, and the gap widens with scale**, because the embeddings, the LM head and the final norm stay trainable through every interval and account for **70.7% of everything LISA trains at 8B**. The arithmetic in the paragraph above is correct and still reads as a win over LoRA. It is not one.

Stated positively, which is the honest version of the pitch: **LISA trains an 8B on a single 80 GB card where full fine-tuning needs roughly 120 GB and cannot run at all.** Reach for it when you want closer-to-full-fine-tune behaviour and LoRA is not enough, not when you want to save memory over LoRA.

Two caveats on the table. Held-out quality here is in-distribution loss and token accuracy on an Alpaca validation split, not a downstream benchmark. And raising `lisa_num_layers` costs quality as well as memory on this data: at 3B the held-out loss went 1.2504 at 2 layers, 1.2673 at 8 and 1.2950 at 16, while at 8B anything above 8 exhausts an 80 GB card. `lisa_interval_steps` was indistinguishable anywhere from 1 to 50.

## Gates

LISA is `sft` or `pretrain` (since v0.74.0) + `transformers` + `text` + `quantization: none` only. It is mutually exclusive with LoRA features, `freeze_layers` / `freeze_ratio`, and Spectrum's `unfrozen_parameters`, because each of those independently decides what trains and stacking them is a footgun, not a feature. It is also mutually exclusive with `train_router_only`, `expand_layers`, `freeze_trainable_layers`, `moe_lora`, `relora_steps`, `loraplus_lr_ratio` and `stream_layers` (a streamed base is frozen on the `meta` device, so per-step layer sampling has nothing to sample). Every reject config fails with a specific message.

> Implementation note: the model is left fully trainable at trainer-setup time so Hugging Face's optimizer (built before the first callback fires) contains every decoder parameter; the LISA callback then toggles `requires_grad` per interval, and frozen parameters produce no gradient so the optimizer skips them. This ordering invariant is what makes the callback work at all.

Live on a 4 GB GPU for small models: a 4-epoch SmolLM2-135M-Instruct run completes with no callback crash (loss 0.66, token accuracy 0.80).

## See also

- [Spectrum targeted training](/docs/spectrum-targeted-training) — the static, SNR-ranked counterpart.
- [PEFT & efficiency](/docs/lora-quality) — LoRA, PiSSA, ReLoRA, per-pattern rank.
- [Adapter algebra](/docs/adapter-arithmetic) — the other half of the v0.71.34 release.

[PreviousSpectrum Training](/docs/spectrum-targeted-training)[NextModel Shrink](/docs/soup-shrink)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="042-soup-shrink"></a>

# 42. soup shrink: make a model smaller (v0.71.29)

*Source: <https://trysoup.dev/docs/soup-shrink>*

**v0.71.29** ships `soup shrink`: one command that makes a model \*permanently\* smaller and faster by removing its least-useful decoder layers, optionally healing the damage by distillation, and printing a single **SHIP / DON'T-SHIP** perplexity verdict. The output is one dense smaller model, not a base plus an adapter.

It implements ["The Unreasonable Ineffectiveness of the Deeper Layers"](https://arxiv.org/abs/2403.17887) (Gromov et al.), with a Minitron-style distillation heal in place of the paper's plain fine-tune.

> We have not found one-command importance-ranked depth pruning, with a distill-heal and a binary perplexity verdict, in another fine-tuning CLI.

## How it works

1. **Importance scan.** For each contiguous block of decoder layers, Soup runs one forward pass per calibration prompt and measures the **angular distance** the residual stream travels from the block's input to its output, averaged over every non-pad token. A block that barely changes the residual stream is doing little work and is the safest to drop.
2. **Select + prune.** The least-important block is removed. The **first and last decoder layers are always protected** (they carry the most transformation). The model is sliced, its `num_hidden_layers` patched, saved, and reloaded so the surviving layers re-index cleanly.
3. **Distill-heal (optional).** With `--heal`, the full-depth original (teacher) is distilled into the pruned student via a LoRA logit-distillation `soup train` subprocess. The resulting adapter is then **fused back** into the pruned base, so the shipped artifact stays a single dense model.
4. **Verdict.** Perplexity is measured before and after. Soup **SHIPs only if the perplexity ratio stays within your tolerance** (default 10%), else **DON'T SHIP**.

## Quick start

```bash
# Plan only: print the layer-importance table + chosen block, write nothing.
soup shrink --model HuggingFaceTB/SmolLM2-135M-Instruct --drop-ratio 0.25 \
    --calib calib.jsonl --device cpu --plan-only

# Prune 25%, distill-heal, get a verdict, attach the report to a registry entry.
soup shrink --model HuggingFaceTB/SmolLM2-135M-Instruct --drop-ratio 0.25 \
    --calib calib.jsonl --heal heal.jsonl --heal-steps 200 \
    --tolerance 0.10 -o shrunk --device cpu --attach-to-registry <id>
```

The shrunk model lands in `<out>/model`, and the verdict is written to `<out>/shrink_report.json`.

## Flags

| Flag | Default | Meaning |
| --- | --- | --- |
| `--model` | required | Model id or local path to shrink |
| `--calib` | required | Calibration prompts (JSONL, chat rows), must stay under cwd |
| `--drop-ratio` | — | Fraction of layers to drop (e.g. `0.25`). Exactly one of ratio / layers |
| `--drop-layers` | — | Explicit contiguous-layer count to drop |
| `--heal` | off | Distill the original into the pruned student, then fuse the adapter back |
| `--heal-steps` | `200` | Approx optimiser steps for the distill heal |
| `--tolerance` | `0.10` | Perplexity-ratio tolerance for the SHIP verdict (max 5.0) |
| `-o`, `--output-dir` | `./shrunk` | Output dir; model in `<dir>/model`, verdict in `<dir>/shrink_report.json` |
| `--device` | auto | `cpu` or `cuda` for the importance + perplexity passes |
| `--attach-to-registry` | — | Attach the shrink report to a registry entry id |
| `--plan-only` | off | Print the importance table + chosen block, then exit 0 (writes nothing) |
| `--trust-remote-code` | off | Allow custom modeling code; defaults off with a probe + warn |

The first and last layers are always protected, so the resolved drop count is clamped to `[1, num_layers - 2]`.

## The verdict + exit codes

`soup shrink` drops into CI exactly like [`soup ship`](/docs/soup-ship) and `soup diagnose`:

| Exit code | Meaning |
| --- | --- |
| `0` | **SHIP** — perplexity ratio within tolerance |
| `2` | **DON'T SHIP** — pruning raised perplexity past tolerance |
| `1` | Error |

Pruning always raises perplexity, so `shrink` uses this dedicated ratio rule rather than `soup ship`'s absolute-improvement gate. The perplexity numbers are the same procedure applied before and after, so the **ratio** is valid, but they are not directly comparable to `soup eval` / lm-eval absolute scores.

## Supported architectures (v1)

**Llama, Qwen, SmolLM.** Anything else is a friendly reject with a pointer to open an issue. The family is checked twice: fail-fast from the config before weights load, and again on the loaded model.

## Validated results

Live-validated on **SmolLM2-135M** on a single **RTX 3050 (4 GB)**:

- **Drop 25%, unhealed:** 30 → 22 layers (~21% of params gone), perplexity **x2.98**.
- **Drop 4 + CPU heal:** perplexity recovered to **x1.35**.

The importance pass loads the model, so it is live-validated on models up to ~3B on that hardware; larger models work but are unvalidated on the reference card.

## Security

Every path (`--calib`, `--heal`, `--output-dir`, and every derived write path like `<out>/model` and the fuse staging dir) is held under cwd with `realpath` + `commonpath` + `O_NOFOLLOW` + symlink rejection, **re-validated right before each write** (TOCTOU defence, including after the potentially hours-long heal). The heal runs as an argv-list subprocess (no shell) with a timeout and a schema-validated config; its output is control-char-stripped before it reaches your terminal. Input files are capped at 64 MiB and 10,000 calib rows. `--model` defaults `trust_remote_code=False`.

## See also

- [soup ship](/docs/soup-ship) — the SHIP / DON'T-SHIP verdict for a fine-tune; `shrink` mirrors its exit codes.
- [Spectrum targeted training](/docs/spectrum-targeted-training) — the complementary move: instead of removing layers, freeze all but the high-signal ones.
- [Fine-tune Doctor](/docs/fine-tune-doctor) — pre-flight your data before you prune-and-heal.

[PreviousLISA](/docs/lisa)[NextPRM-guided GRPO](/docs/prm-guided-grpo)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="043-prm-guided-grpo"></a>

# 43. PRM-guided GRPO (v0.71.30)

*Source: <https://trysoup.dev/docs/prm-guided-grpo>*

`soup train` with `task: grpo` can now use a trained Process Reward Model as the per-step reward signal, the o1-era process-supervision idea: grade every reasoning step, not just the final answer. Point it at a PRM you trained with `soup train` with `task: prm` and it scores each step of a generated answer, folding the per-step scores into one reward that GRPO optimizes.

> We have not found another OSS fine-tuning CLI that uses a PRM as the per-step GRPO reward.

## Config

```yaml
task: grpo
backend: transformers        # required (the PRM reward runs a transformers forward)
modality: text               # required
data:
  format: chatml
  train: ./grpo_prompts.jsonl
training:
  prm_reward: ./my-prm       # a `soup train` with `task: prm` checkpoint dir, or an HF id
  prm_aggregate: min         # min (weakest-link, default) | prod | last
  num_generations: 4
  grpo_beta: 0.04
```

- `prm_reward` replaces `reward_fn`; TRL logs it as `rewards/prm_reward`, and the v0.71.26 [reward-hack controller](/docs/reward-hack-mitigation) observes it like any other reward.
- `prm_aggregate` folds the per-step scores into one number. `min` is the weakest-link default and the safe choice; `prod` assumes calibrated `[0,1]` step scores (it can blow up or flip sign on uncalibrated labels); `last` uses the final step.
- Step boundaries are a newline heuristic; each step is scored with one PRM forward pass.

## Bundled rollout environments

v0.71.30 also ships three deterministic, pure-Python toy environments so the GRPO `openenv` rollout path works with no external setup:

```yaml
training:
  rollout_backend: openenv
  rollout_func: soup_cli.envs.calculator:rollout   # or retrieval_qa | guess_number
  reward_fn: verifiable
  verifiable_domain: math
```

Ready-made recipes: `grpo-env-calculator`, `grpo-env-retrieval-qa`, `grpo-env-guess-number` (part of catalog 134 to 137). They are single-shot prompt/answer seeders (the live `openenv` contract passes seed prompts, not the model), not interactive multi-turn episodes.

## Honesty

Proof-of-mechanism only, validated on SmolLM2-135M with a tiny synthetic PRM and synthetic reward on a single RTX 3050, not a production reward-model claim. Scale validation is tracked in [issue #286](https://github.com/MakazhanAlpamys/Soup/issues/286).

## See also

- [GRPO Plus](/docs/grpo-plus) — the 7 GRPO variants, rollout backends, and stability controls this builds on.
- [Online DPO](/docs/online-dpo) — the judge-in-the-loop RL alternative when you have a judge instead of a PRM.
- [RLVR](/docs/rlvr) — verifiable rewards for math / code / JSON with no reward model at all.

[PreviousModel Shrink](/docs/soup-shrink)[NextOnline DPO](/docs/online-dpo)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="044-online-dpo"></a>

# 44. Online DPO (v0.71.31)

*Source: <https://trysoup.dev/docs/online-dpo>*

`soup train with task: online_dpo` puts an LLM judge (or a reward model) in the training loop. Each step samples two on-policy completions per prompt, a pairwise judge names the winner `chosen` and the loser `rejected`, and the model takes a DPO step on that fresh, self-generated pair. It wraps TRL's `OnlineDPOTrainer`, and it is transformers + text only (prompt-only data, like GRPO).

This is the training face of the v0.71.31 [judge-in-the-loop suite](/docs/best-of-n-evolve): the same swap-debiased judge also mines data with best-of-N, grows it with Evol-Instruct, and decides SHIP with a pairwise win-rate in [`soup ship`](/docs/soup-ship).

## Config

```yaml
base: HuggingFaceTB/SmolLM2-135M-Instruct
task: online_dpo
data:
  train: ./data/prompts.jsonl      # prompt-only (any format works; prompts are extracted)
training:
  online_dpo_judge: "ollama://llama3.1"   # a pairwise judge (ollama:// | https:// | http://localhost)
  # OR set a reward model instead of a judge (exactly one of the two):
  # reward_model: ./my-reward-model
  online_dpo_loss_type: sigmoid           # sigmoid | ipo
  online_dpo_max_new_tokens: 64
  dpo_beta: 0.1
  lora: { r: 8, alpha: 16, target_modules: auto }
```

```bash
soup train --config online_dpo.yaml
# or start from the ready-made recipe:
soup recipes use online-dpo-smollm2-135m
```

## Config fields

| Field | Default | Meaning |
| --- | --- | --- |
| `online_dpo_judge` | (none) | Judge URL (`ollama://model`, `https://...`, or `http://localhost`). Mutually exclusive with `reward_model`. |
| `reward_model` | (none) | A reward model to score completions instead of a judge. Exactly one of judge / reward\_model must be set. |
| `online_dpo_loss_type` | `sigmoid` | `sigmoid` (DPO) or `ipo`. |
| `online_dpo_max_new_tokens` | `64` | Tokens to sample per completion (`1..4096`). |
| `beta` | via `dpo_beta` | The DPO temperature; reuses the existing `dpo_beta`. |

The cross-validator requires `backend: transformers` and `modality: text`, and rejects both-set or neither-set judge / reward\_model, plus any `online_dpo_*` field left non-default when the task is not `online_dpo`.

## How the judge is used (and a per-version note)

The judge is Soup's `JudgeEvaluator` adapted to TRL, swap-debiased: it compares the two completions in both orders and only records a winner when `(A,B)` and `(B,A)` agree, so position bias cannot leak a preference.

Because CI resolves trl 1.x (which removed pairwise judges and moved the trainer to `trl.experimental`), Soup ships a runtime trl-version adapter:

- **trl 0.19.x** uses the swap-debiased pairwise judge (`judge=`).
- **trl 1.x** uses the same `JudgeEvaluator` as a pointwise `reward_funcs=` scorer.

Same judge model either way; the comparison shape differs by installed trl version. This is a documented per-version behaviour difference, not a bug.

## Honesty

Proof-of-mechanism only. Online DPO was validated on SmolLM2-135M with a synthetic length-preferring judge on CPU (`rewards/*` and `objective/kl` logged), not a production RLHF claim. The 4-bit path is code-correct but hardware-gated (validated at `quantization: none` on CPU; real QLoRA online-DPO needs a bigger GPU). Scale validation is an open community ask ([issue #286](https://github.com/MakazhanAlpamys/Soup/issues/286)).

## See also

- [Best-of-N & Evol-Instruct](/docs/best-of-n-evolve) — the data side of the judge-in-the-loop suite.
- [soup ship](/docs/soup-ship) — decide SHIP with a pairwise judge win-rate (`--task-mode pairwise`).
- [Preference variety](/docs/preference-variety) — the offline DPO / KTO / ORPO / SimPO / IPO / BCO dispatcher.
- [GRPO Plus](/docs/grpo-plus) and [PRM-guided GRPO](/docs/prm-guided-grpo) — the RL alternatives.

[PreviousPRM-guided GRPO](/docs/prm-guided-grpo)[NextASR (Whisper)](/docs/asr-fine-tuning)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="045-asr-fine-tuning"></a>

# 45. ASR fine-tuning (v0.71.32)

*Source: <https://trysoup.dev/docs/asr-fine-tuning>*

`soup train` with `task: asr` fine-tunes OpenAI Whisper speech-recognition models on your own audio, locally. Data is plain JSONL rows of `{"audio": "clip.wav", "text": "the transcript"}`: clips decode to 16 kHz mono log-mel input features, transcripts become the decoder labels, and the trainer wraps Hugging Face `Seq2SeqTrainer` + `WhisperProcessor`. whisper-tiny (39M) and whisper-base (74M) train on a 4 GB GPU.

## Config

```yaml
base: openai/whisper-tiny
task: asr
data:
  train: ./data/train.jsonl
  format: asr                 # rows: {"audio": "clip.wav", "text": "hello world"}
  audio_dir: ./data/audio     # audio paths resolve here (containment-checked)
training:
  epochs: 3
  lr: 1e-4
  batch_size: 2
  asr_language: en            # optional; pins + persists the decoder prefix
  asr_task: transcribe        # transcribe | translate
  asr_lora: true              # LoRA on q/v projections; default is full fine-tune
  lora: { r: 16, alpha: 32, target_modules: [q_proj, v_proj] }
output: ./out
```

```bash
pip install "soup-cli[train,audio]"
soup recipes use whisper-tiny-asr   # or whisper-base-asr / whisper-large-v3-asr
soup train
```

## Config fields

| Field | Default | Meaning |
| --- | --- | --- |
| `asr_language` | (none) | Decoder language prefix (e.g. `en`). Persists to an `asr_generation.json` sidecar next to the weights, so inference restores it automatically. |
| `asr_task` | `transcribe` | `transcribe` or `translate`. Also persisted to the sidecar. |
| `asr_lora` | `false` | `true` trains LoRA on the q/v projections instead of full fine-tuning. |

The cross-validator requires `backend: transformers` (so `mlx` / `unsloth` are rejected) and footgun-rejects `asr_*` fields when the task is not `asr`; a separate trainer-side gate rejects a non-Whisper base before any weight download.

## Inference + WER/CER

```bash
soup infer --task asr --model ./out --input eval.jsonl --output preds.jsonl \
    --audio-dir ./data/audio [--asr-language en] [--asr-task transcribe]
```

`--model` loads a full Whisper model or a PEFT/LoRA adapter dir. Input rows are `{"audio": path}` with an optional `"text"` reference; when references are present, each output row carries `transcription`, `wer` and `cer`, plus a corpus WER summary (sum of edits over sum of reference words, not a mean of per-row rates). The metrics are pure-Python word- and char-level Levenshtein with no new dependency, and word accuracy (1 - WER) plugs into [soup ship](/docs/soup-ship) as a higher-is-better task metric, so the SHIP / DON'T-SHIP verdict works for speech models too.

> WER/CER use a light normalizer (casefold, strip surrounding punctuation, collapse whitespace), deliberately not the full Whisper normalizer: good for before/after deltas, not leaderboard-comparable absolutes.

## Recipes

| Recipe | Base | Size | Status |
| --- | --- | --- | --- |
| `whisper-tiny-asr` | `openai/whisper-tiny` | 39M | Live, validated on a 4 GB RTX 3050 |
| `whisper-base-asr` | `openai/whisper-base` | 74M | Live, fits a 4 GB GPU |
| `whisper-large-v3-asr` | `openai/whisper-large-v3` | 1.5B | Parse-tested; needs a 16 GB+ GPU |

A `smolvlm-256m-sft` tiny-VLM recipe ships alongside (parse-tested, `target_modules` pinned to q/v). v0.72.0 fixed the setup and tokenization half of [issue #302](https://github.com/MakazhanAlpamys/Soup/issues/302) (the vision processor now mirrors `pad_token` from its nested tokenizer), but a full training step still needed Idefics3-aware collation, so that recipe stayed parse-only until **v0.74.0**, which keeps messages and images together until collation, converts legacy `<image>` markers to structured multimodal content, and lets the processor produce image-token expansion and architecture-specific pixel tensors.

## Honesty

Proof-of-mechanism only. The live validation is a memorization run on a single RTX 3050: WER 1.000 to 0.000 and loss 7.2 to 0.0005 at 0.4 of 4 GB VRAM. That proves the loop trains end to end; real accent or domain gains need real audio. The release also fixed the hardware-fit gate mis-sizing Whisper checkpoints as 7B models, which would have wrongly blocked ASR training on consumer GPUs.

## Security

Audio decodes only through the hardened loader (a `soundfile` pre-probe before read, symlink rejection, `O_NOFOLLOW`, byte caps), never through datasets auto-decode. `data.audio_dir` is containment-checked (realpath + commonpath); UNC paths and traversal are rejected. A missing `[audio]` extra, a bad audio path, or a non-Whisper base all fail with a friendly error before a GPU hour.

## See also

- [Vision & Audio](/docs/multimodal) — the audio-understanding (Qwen2-Audio) and vision paths.
- [Modality II](/docs/modality-ii) — TTS, the audio-out counterpart to ASR's audio-in.
- [soup ship](/docs/soup-ship) — gate a speech model on word accuracy plus no forgetting.
- [Recipes](/docs/recipes) — all 167 ready-made configs.

[PreviousOnline DPO](/docs/online-dpo)[NextReward Forge](/docs/reward-verifier)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="046-reward-verifier"></a>

# 46. Reward Forge: synthesize a reward verifier, then prove it cannot be gamed (v0.71.40 → v0.71.41)

*Source: <https://trysoup.dev/docs/reward-verifier>*

An RL run trusts its **reward verifier** more than anything else and inspects it least. If the verifier pays out for the wrong reasons, the policy learns to hack it, and you find out after the GPU hours. Reward Forge is two commands that turn Soup's reward-hacking detector on the verifier itself: `soup reward synth` **builds** a deterministic verifier from your data and refuses a bad one; `soup reward stress` **attacks** a verifier to see if degenerate junk gets paid.

Both are pure and offline, and both ride the existing `load_reward_fn` `.py` path, so they add **no new trusted-execution surface**. No RL library (TRL, Unsloth, Axolotl, OpenRLHF) synthesizes a reward or tests one for gameability.

## `soup reward synth` — a verifier from your gold outputs (v0.71.40)

```bash
soup reward synth golds.jsonl -o reward.py                      # auto-detect the family
soup reward synth golds.jsonl -o reward.py --kind numeric --tolerance 1e-6
soup reward synth golds.jsonl --plan-only                       # show the induced spec, write nothing
soup reward synth golds.jsonl -o reward.py --output-report calib.json
```

Point it at a JSONL of reference (gold) outputs and it infers one of four verifier families, auto-detected or forced with `--kind`, each grounded in your golds:

| `--kind` | What it checks |
| --- | --- |
| `numeric` | Extracts the last number, a `\boxed{}` span or a `####` answer and compares exactly or within `--tolerance`. |
| `json_schema` | Induces keys, value types and required fields from the golds and validates against them. |
| `regex` | Builds positional character classes over equal-length golds. |
| `tool_call` | Binds each tool's `required` and `allowed` arguments. |

The emitted `reward.py` is **self-contained, readable and committable** — you read it, edit it, diff it in review, and check it into git, exactly like a hand-written reward. It is not a trained-weights black box.

### The moat: mandatory calibration

The differentiator is that synth **refuses to emit a verifier that cannot tell good from bad**. Before writing the file, the synthesized verifier is loaded back and run against:

- its **own references** — it must accept at least **90%**, and
- **auto-generated bad answers** — it must reject them.

A degenerate always-accept verifier is refused with **exit 2**, never silently written. `--plan-only` reports the induced spec without writing, and `--output-report` persists the calibration JSON.

## `soup reward stress` — is the verifier gameable? (v0.71.41)

```bash
soup reward stress reward.py --references golds.jsonl
soup reward stress reward.py --references golds.jsonl --attacks empty,length,repetition,sentinel --sentinel GOLD
soup reward stress verifiable --verifiable-domain math --references golds.jsonl   # probe a builtin
```

Where synth proves a verifier separates references from \*friendly\* perturbations, stress asks the adversarial question a reward-hacking model asks at train time: **does the verifier pay out for degenerate junk?** It feeds four attack families, each scored against the real gold (references are cycled), so a `numeric`, `tool_call` or `json_schema` verifier still gets a valid target and must reject the garbage:

- `empty` — an empty completion
- `length` — a length-padded completion
- `repetition` — a repeated fragment
- `sentinel` — spam containing a magic token (`--sentinel`)

```text
$ soup reward stress reward.py --references golds.jsonl
attack       accept-rate
empty        0%
length       0%
repetition   0%
sentinel     0%
verdict: ROBUST   0 / 4 attacks gamed   exit 0
```

It reports a **per-attack accept-rate table** plus an overall gameability verdict, tuned by `--max-gameable` and `--threshold`, and `--output-report` persists the JSON. It probes a synthesized `.py` **and** a builtin (`accuracy`, `format`, `verifiable`) through the same loader. Exit codes: **0 = robust**, **2 = gameable**, **1 = error**. A gold-requiring verifier probed with **no `--references`** is a hard error naming the flag, never a false "robust".

## Reward ensembles now train (v0.71.40)

A comma-separated `training.reward_fn` finally trains as a **reward ensemble**:

```yaml
task: grpo                       # root-level, NOT under training
training:
  reward_fn: "accuracy,format"   # resolves to GRPOTrainer(reward_funcs=[accuracy, format])
```

This also unlocks the `rm_ensemble` reward-hack detector, which needs at least two rewards, and it fixes a recipe (`deepseek-v3-reasoning`) that shipped exactly this form and previously crashed with `Unknown reward function`. The `reward_fn` field also gained a validator that rejects null bytes, blanks, oversize strings and empty comma segments (`verifiable` in a comma list without a `verifiable_domain` now fails at parse time, like the bare form).

## Where it fits

```
soup reward synth  →  reward.py  →  soup reward stress  →  soup train (task: grpo)
   (build)             (commit)        (prove robust)         (train against it)
```

Synthesize a verifier from data you already have, stress it until the accept-rates are zero, commit the `.py`, then train GRPO against a reward you have actually audited.

## See also

- [RL & preference training](/docs/online-dpo) — GRPO, online DPO and the judge in the loop the reward feeds.
- [Closed-loop reward-hacking auto-mitigation](/docs/reward-hack-mitigation) — the train-time half: detect a policy gaming the reward and self-correct.
- [soup ship](/docs/soup-ship) — the SHIP / DON'T-SHIP verdict that gates the trained model.

[PreviousASR (Whisper)](/docs/asr-fine-tuning)[NextLayer Streaming](/docs/layer-streaming)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="047-layer-streaming"></a>

# 47. Layer streaming: fine-tune a model that does not fit in your card (BETA, v0.72.0; NF4 v0.72.2; breadth v0.72.3; preference losses v0.72.4; external validation and the NF4 gradient repair v0.73.0)

*Source: <https://trysoup.dev/docs/layer-streaming>*

The usual answer to "this model does not fit" is quantize harder, rent a bigger GPU, or give up. Layer streaming is a fourth answer: **never load the frozen base at all**. Soup keeps it in CPU RAM (or on NVMe) and copies it into VRAM one decoder layer at a time, so peak VRAM is bounded by the size of **one layer** instead of the whole model.

Quantizing that streamed base to NF4 shrinks it about fourfold, and that is what turns the idea into a useful one:

**Llama-3.1-8B fine-tunes on a 4 GB laptop GPU at 119.6 tok/s in 3.32 GB** — on a card that cannot hold even a quarter of the model.

This ships **BETA**, and both the scope and the claim below are narrow on purpose.

If you would rather watch it than read it: [the 90-second run](https://youtu.be/T1LCErE943E) shows the pre-flight panel (a 3.60 GB base store pinned in RAM across 32 layers, two 113 MB VRAM buffers) and then the measurement card settling at 3.32 GB and 119.6 tok/s, stopping short of the 4 GB line. The mechanism is written up in a preprint, summarised on [the paper page](/docs/paper).

> **v0.72.3 widened it.** The first three releases were deliberately narrow: Llama and Qwen only, batch size 1, no gradient accumulation, no resume, RAM only. All of that is lifted. Ten architectures are supported as of v0.74.0, batches and accumulation work, `--resume` works, a pre-flight predicts peak VRAM and refuses a run that will not fit, and an NVMe overflow tier handles a base too big even for RAM. See [Scaling a streaming run](/docs/streaming-scaling) for the sizing rules, the batch-versus-accumulation measurement and the disk tier.

> **v0.72.4 added alignment.** Streaming used to mean supervised fine-tuning only. `dpo`, `orpo`, `simpo` and `kto` now run against a streamed base, and DPO's reference model is the same streamed base with its adapters switched off, so it costs no extra weights. See [Preference losses over streaming](/docs/streaming-preference).

## Read this first if you already trained with streaming

Two defects in this feature's history produced runs that looked completely healthy and were not. Both are narrow, both have a one-line test, and neither affects a run outside its stated scope.

### If you streamed a 32B or larger model in NF4

**Above roughly 165 MB per decoder layer, a streamed NF4 run produced silently wrong gradients.** In practice that means a 32B or a 72B: 8B sits at 105 MB per layer and 14B at 132, both below the boundary with margin, and both verified exact over a 50-backward soak. Filed as issue #331.

The forward stayed bit-exact throughout, and the loss matched a resident reference to every digit, so nothing in a training log could show it. The cause is buffer aliasing rather than a race: `bitsandbytes` keeps the packed 4-bit weight outside PyTorch's `save_for_backward` mechanism, so gradient checkpointing cannot recompute it, and the backward reads a streaming slot that has already been refilled with a different layer. bf16 was never affected, at any size.

**It was present in v0.72.0 through v0.72.4, and it is repaired in v0.73.0.** The repair keeps streamed NF4 weights out of that code path entirely, and it is gated on two real models against a control that reproduced the defect in the same process: 256 of 256 gradient tensors exact at 32B, and 320 of 320 at 72B, the size where the defect was worst. It costs about 3% of peak VRAM and 4% of throughput. If you streamed a 32B or larger model in NF4 on any earlier version, re-run it on v0.73.0; if you streamed 8B or smaller, there is nothing to do. [The full diagnosis, the threshold measurement and the repair's cost](/docs/external-validation#the-defect-this-found).

### If you trained with streaming on v0.72.0

**That adapter is inert. Re-run it on v0.72.1.**

The streaming wrapper held the real decoder layer as a child named `inner`, so every adapter tensor was written to disk under a key carrying an extra `.inner.` segment:

```
base_model.model.model.layers.0.inner.self_attn.q_proj.lora_A.weight
                               ^^^^^^
```

Loading that file into an ordinary model matches **nothing**. PEFT reports missing keys as a `UserWarning` rather than an error, so `soup merge`, `soup serve`, `soup chat` and `PeftModel.from_pretrained` all completed normally and handed back the **untuned base model**. Nothing failed, and nothing looked wrong.

Check a file you already have:

```bash
python -c "from safetensors.torch import load_file; \
print([k for k in load_file('adapter_model.safetensors') if '.inner.' in k][:3])"
```

A non-empty list means the adapter is affected.

**What was not affected matters just as much.** The training itself was correct: the streamed run's numerics are unchanged and v0.72.0's bit-exactness results still stand. Only the saved file was wrong. There is no way to restore a broken file's association with its base model beyond renaming keys, so **re-running is the reliable path**. On v0.72.1 a streamed adapter saves byte-for-byte in the same layout as an ordinary LoRA run, portable to any tool that has never heard of layer streaming.

v0.72.1 also closed a second hole in the same area: the guard refusing `--resume` for a streaming run only tested that one flag, so `--hf-resume` reached `resume_from` around it. That combination used to appear to work by accident, and once adapters save canonically it would instead have matched nothing and continued with a **freshly initialised adapter, silently**. Both flags were refused until v0.72.3 fixed the load side and unblocked them; see [Scaling a streaming run](/docs/streaming-scaling#resume-works-now-and-why-it-could-not-before).

> Both defects above share a shape, and it is worth naming rather than smoothing over. v0.72.0 passed every correctness gate it set itself and shipped a clean throughput table, and no test in that release saved an adapter and loaded it back. #331 passed every gate too, on hardware where the reference it needed could not exist. In each case the run exited 0 and the loss curve looked healthy. A green suite measures what it was pointed at.

## What is actually new here

Layer streaming itself is not new, and fine-tuning on a small card is not new. An early draft of this page claimed no published system does this; that claim was fact-checked against the sources and cut, because it is false. What is true is narrower:

- **For inference, streaming a small card is well established.** AirLLM runs 70B-class models through a 4 GB GPU, and its own documentation states that layer sharding is **not compatible with gradient propagation**. Hugging Face's `disk_offload` is documented as big-model **inference** and runs under `no_grad`.
- **For training, the published small-card result already exists**: LSP-Offload ([arXiv:2406.10181](https://arxiv.org/abs/2406.10181)) fine-tunes **1.3B on a 4 GB laptop GPU**. It gets there by compressing the **optimisation** into a learned sparse subspace, **not** by streaming weights.

So the honest headline is not "nobody has done this". It is **up to 8B on a 4 GB card, by streaming the base rather than approximating the optimisation, with the forward pass verified bit-exact against a resident run at the same precision** — and packaged as two config keys in a general-purpose CLI rather than a research prototype.

## Turn it on

It is a **config key, not a CLI flag**:

```yaml
training:
  stream_layers: true          # enable layer streaming
  quantization: 4bit           # NF4: ~4x smaller store, so 8B fits a 4 GB card
  stream_source: auto          # RAM when the base fits, NVMe disk when it does not
  stream_buffers: 2            # double-buffering; range [2, 8], default 2
  # stream_pin: false          # v0.74.0: force the pageable store, and print what it costs

  batch_size: 4                # any concrete value; the pre-flight sizes it for you
```

`quantization` accepts `none` (bf16) or `4bit` (NF4) and nothing else. NF4 is what you want unless you have a specific reason to stream bf16: it shrinks the RAM store about fourfold, and a smaller store is far more likely to page-lock, which is worth more than the arithmetic (see below).

```bash
# There is no --stream-layers flag. You train exactly as before:
soup train --config soup.yaml
```

> **The one value `batch_size` cannot take is `auto`.** The auto-batch probe sizes a **resident** model, which a streaming run never loads, so it is refused by name. Set a concrete number instead: as of v0.72.3 a pre-flight predicts peak VRAM for that exact batch and sequence length and refuses the run before any GPU work if it will not fit. Reach for `batch_size` before `gradient_accumulation_steps`, because at the same effective batch a real batch measured about **2.52x faster** than accumulating. [Why, and how to size it](/docs/streaming-scaling).

## How it works

The base model is built on PyTorch's `meta` device, so its weights never occupy VRAM. Only the embeddings, the final norm, an untied LM head and the **LoRA adapters with their gradients and optimizer state** get real storage on the card, and those are small. The checkpoint is rewritten once into one safetensors shard per decoder layer, and that store is held in CPU RAM, page-locked when the machine allows it, or read from an [NVMe disk tier](/docs/streaming-scaling#the-disk-overflow-tier) when the base is too large for RAM.

During the step, each decoder layer is copied into one of N pre-allocated VRAM buffers on a **dedicated CUDA stream**, so the load of layer i+1 overlaps the compute of layer i. The pooled buffer is substituted into the unmodified decoder layer, which means the same kernels run on the same weight bytes.

Each layer is read **twice per step** — once in the forward pass and once when the backward pass recomputes it — because `dL/dx = Wᵀ · dL/dy` needs the weights to push gradient down to the layers below. That is physics, not an implementation detail, and it is why streaming costs time rather than being free.

**Correctness is not part of the trade.** A streamed forward pass was verified **bit-exact** against a resident one, and a 100-step streamed loss curve matched resident exactly.

Treat "bit-exact" as **two claims, not one**, because they can come apart: the forward (the logits) and the backward (every LoRA gradient tensor) are measured independently. On the development box both hold. On borrowed H100 hardware, where a resident reference for a real model can actually exist, the forward is exact up to 72B while the backward turned out to be wrong above roughly 165 MB per NF4 layer, which is [the defect described above](#if-you-streamed-a-32b-or-larger-model-in-nf4). Whenever this page or any other says a run is bit-exact, it means both halves at the size stated, and nowhere else. [The full ledger](/docs/external-validation).

**Since v0.75.0 there is a third qualifier, and it is the card.** Streamed NF4 is **not** bit-exact against resident NF4 on Blackwell. On an RTX 5070 (`sm_120`) the two CUDA-only exactness tests fail at **4.9e-4** in fp16 and **3.9e-3** in bf16, while the `quantization: none` parametrisations of the same tests **pass**. That split is the useful part of the report: layer streaming itself is still exact there, and the divergence is in the `bitsandbytes` NF4 path on that architecture. It is **not** the defect v0.73.0 repaired, which had a megabytes-per-layer boundary rather than a card-architecture one, and unlike that one **this is not fixed**: the root cause is not established, and no mechanism is claimed here because upstream claims none. CI cannot see it, because CI has no GPU runner and these tests skip on every hosted platform; it took the first Blackwell card the project has had access to.

So the full form of the claim is four-part: **which half** (forward or backward), **which quantisation**, **which size**, and now **which card**. Everything measured and published on this site was measured on Ampere or Hopper.

## Measured numbers

Measured on the development box: **RTX 3050 Laptop 4 GB**, Windows 11, 16.9 GB RAM, LoRA, batch 1, gradient checkpointing on, `PagedAdamW8bit`, 50 steps after 10 warm-up.

| Model | Quant | Seq | Throughput | GPU util | Peak VRAM | RAM store |
| --- | --- | --- | --- | --- | --- | --- |
| **Llama-3.1-8B-Instruct** | **NF4** | 512 | **119.6 tok/s** | **100%** | **3.32 GB** | 3.60 GB pinned |
| Qwen2.5-3B | NF4 | 512 | 264.2 tok/s | 100% | 1.76 GB | 1.43 GB pinned |
| Qwen2.5-3B | bf16 | 512 | 143.1 tok/s | 79.3% | 2.15 GB | 5.55 GB pageable |
| Qwen2.5-1.5B | bf16 | 512 | 525.0 tok/s | 96.8% | 1.82 GB | pinned |
| Qwen2.5-1.5B | bf16 | 1024 | 487.6 tok/s | 96.7% | 2.96 GB | pinned |
| Qwen2.5-0.5B | bf16 | 512 | 978.6 tok/s | 91.4% | 1.47 GB | pinned |

> **Read the 8B rate as a pre-repair figure.** Every row above was measured on v0.72.2, before the [NF4 gradient repair](#if-you-streamed-a-32b-or-larger-model-in-nf4) that shipped in v0.73.0. That repair cost 4.8% throughput at 32B, and nobody has re-run the 8B laptop configuration on the repaired code. A server card cannot stand in for the measurement either, which the H100 replication showed by coming back no faster rather than faster, so throughput here does not carry across machines. The nearest independent evidence is a **median 113.00 tok/s in the same 3.32 GB peak on an H100**, five runs, which is [a cross-hardware reproduction rather than a re-measurement](/docs/external-validation).

For scale, 1M training tokens is about **2.3 hours at 8B** on that card. That is arithmetic from the measured rate, not a separate measurement.

**The honest cost: 1.43x slower than resident training**, measured at 0.5B. That is the only apples-to-apples comparison available on this box, because 1.5B and above cannot run resident here at all.

### Why NF4 also made the 3B row faster

The same model went from 143.1 to 264.2 tok/s, and the reason is **not** that 4-bit arithmetic is faster. A 1.43 GB store fits under this machine's page-locked memory ceiling where a 5.55 GB one did not. Pinned memory is what lets the host-to-device copy run asynchronously, so the layer loads hide behind compute again, and utilisation goes from 79.3% to 100%.

**Treat the mechanism as the claim, not the multiplier.** Those two rows come from different sessions and this card's boost clock varies by about 13% between sessions, so the exact factor is indicative. What is solid is the cause: pinning restores overlap, and NF4 is what makes pinning possible at this size.

The same reasoning explains the bf16 3B row's 79.3%. It is **not** a model-size effect: that box could not page-lock a 5.55 GB base, so the run fell back to a pageable store. Soup performs that fallback automatically **and prints what it costs** instead of absorbing it silently. **The bf16 3B throughput is therefore a lower bound.**

One number worth knowing before you size a run: at the time this table was measured, the untied `embed_tokens` and `lm_head` stayed **resident and unquantised**, and they account for **2.10 GB of the 8B row's 3.32 GB**. Roughly two thirds of that peak was not streamed at all, which is exactly why 8B sat close to this card's ceiling.

> **v0.74.0 changed that, and the table above is deliberately not restated.** An untied embedding and LM head are now sharded separately and reuse **one** vocabulary-sized device buffer instead of both staying resident, so the 8B peak has moved. Nobody has re-run the 4 GB laptop configuration on the new code, and upstream's own docs say the historical figure is not being relabelled as a new measurement. Tied embeddings keep the existing resident path and numerics. The rows above stand as what they were: v0.72.2, before both the NF4 gradient repair and this change.

Be careful how utilisation is argued in general: GPU utilisation on its own only says a kernel was resident, which is **necessary for overlap but not sufficient to prove it**. The evidence is the step arithmetic, not the utilisation column.

## Run it yourself on a free Colab T4

[Open the proof notebook in Colab](https://colab.research.google.com/github/MakazhanAlpamys/Soup/blob/main/notebooks/proof-4gb.ipynb) and the argument runs on a card you do not have to own: a free-tier Google Colab **Tesla T4** (sm\_75, Turing, 15.6 GB). The notebook holds the process to **4.00 GB** with `torch.cuda.set_per_process_memory_fraction` before anything loads, then proves the cap bites rather than assuming it, by asking for 4.29 GiB and being refused.

What the completed run printed: `Meta-Llama-3.1-8B-Instruct`, NF4, `stream_layers: true`, `stream_buffers: 2`, batch 1, `max_length: 256`, LoRA r=8, fp16 (a T4 has no bf16 hardware). Seven steps, exit 0, an adapter written with **128 of 128 tensors non-zero**, and a **measured peak of 2.91 GB** against the pre-flight's predicted 3.02, an over-prediction of **3.8%** in the direction the estimator was fitted to err.

Read the frame before you read the number:

- **No throughput is claimed, here or in the notebook.** A card held under an artificial memory cap is not a benchmark. The pre-flight panel's `31-46 tok/s` line is a compute bound derived from a GEMM probe on that card, not a measurement of what the run achieved.
- **Gradient exactness on Turing is not shown.** An adapter with 128 non-zero tensors proves gradients flowed, not that they were right, and that distinction is exactly the shape of [the NF4 defect](#if-you-streamed-a-32b-or-larger-model-in-nf4) v0.73.0 repaired. The notebook's streamed-versus-resident comparison captured no output on that session, so it is recorded as unrun rather than as a pass.
- **On a capped card the pre-flight reads the whole device.** `torch.cuda.mem_get_info()` cannot see a per-process cap, so the panel reported 15.10 GB free while the run was held to 4.00. Nothing was harmed here, since 2.91 GB genuinely fits, but on Colab, Kaggle or a MIG slice the pre-flight is not what enforces your real budget.
- **One run, one seed, one configuration, no repeats**, on a session that cannot be returned to, with the library versions not recorded.
- **The notebook installs Soup from git, not from PyPI**, and it still does even though the precision fix it depends on **shipped in v0.73.1**. Upstream has not switched its install cell back, and the notebook's own first cell still claims the fix is unreleased. Ignore that line, expect the git install, and note that pinning it to a tag would change nothing: a `git+` install resolves to the default branch whichever revision of the notebook you opened.

What it does establish is worth having on its own: the streaming path executes end to end on a pre-Ampere card, at 8B, inside a 4 GB process budget. Before this it had never been run there. [The full record](https://github.com/MakazhanAlpamys/Soup/blob/main/benchmarks/run-t4-colab-free-tier.md), including the longer list of what it does not establish.

## Honest scope

This ships **BETA**, and the claims stop where the measurements stop.

- **Models measured on the 4 GB card: Llama-3.1-8B under NF4, plus Qwen2.5-0.5B, 1.5B and 3B**, and a live `soup train` on SmolLM2-135M. **Nothing above 8B has been measured on this hardware, so no number on this page speaks for a larger model.** Sizes above that were later measured on a borrowed 8x H100 box, up to 72B, and what those runs do and do not establish is [a page of its own](/docs/external-validation). Note the host side is the real gate on reproducing them: the 72B run needed a 33.74 GB pinned RAM store, which a 16.9 GB laptop cannot hold at all.
- **Ten architectures** (`llama`, `qwen2`, `qwen3`, `mistral`, `gemma`, `gemma2`, `gemma3_text`, `phi`, `phi3`, and `qwen4_exp` since v0.74.0, plus the `qwen3_5` dense and MoE aliases). The original nine are verified bit-exact against the same checkpoint loaded resident, under both bf16 and NF4; the v0.74.0 additions carry weaker evidence and [say so](/docs/streaming-scaling#which-models-stream). **There is no throughput measurement for anything but Llama and Qwen, so no speed is claimed for the rest** — every tok/s figure on this page is Llama or Qwen. Multimodal `gemma3` is refused; only `gemma3_text` is accepted.
- `task` must be one of `sft`, `dpo`, `orpo`, `simpo`, `kto`; `backend: transformers`; `modality: text`. The four preference losses landed in v0.72.4, and **no throughput figure is claimed for any of them, because none was measured**. `ipo`, `bco` and the unified `task: preference` dispatcher are still refused. See [Preference losses over streaming](/docs/streaming-preference).
- **`quantization` must be `none` or `4bit`.** Other quantisations store weights in formats that cannot be streamed into a pooled buffer.
- **`batch_size` cannot be `auto`** — the auto-batch probe sizes a resident model. Any concrete value is fine, subject to the VRAM pre-flight.
- **Loading an adapter into a streamed run works** as of v0.72.3, but in memory `named_parameters()` and `state_dict()` still disagree, which is the deliberate cost of a serialisation-only fix. End-to-end `soup train --resume` could not be demonstrated on the development box, for a reason that has nothing to do with streaming: `transformers` refuses `torch.load` below torch 2.6 under CVE-2025-32434, which blocks **every** resume there.
- **The RAM-versus-disk speed gap is unmeasured**, and no figure is claimed for it. The disk tier's **correctness** is verified bit-exact against the RAM tier.
- **Plain LoRA only.** DoRA, VeRA and the PiSSA / OLoRA / LoftQ initialisations all read a real base weight, which streaming keeps on the `meta` device at adapter-build time. `use_rslora` is fine.
- **Pre-Ampere cards (T4, P100, V100, GTX 16xx, RTX 20xx) stream in fp16 rather than bf16.** Until this fix the store dtype was the literal "bf16 on any CUDA device", so the whole free notebook tier ran in a dtype its GPU has no units for, and it could not fail on the Ampere card every number above was measured on. fp16 is bit-exact against a resident reference of matching numerics, `0.000000e+00`, in both quantisations. Two honest edges. The capability question has to be asked as `is_bf16_supported(including_emulation=False)`, because the bare call counts software emulation and a T4 answers True to it, which made the first version of this fix a no-op on exactly the hardware it targeted. And that exactness was measured **using** fp16 on an Ampere card, so it establishes the plumbing and not the Turing or Pascal kernels. **It shipped in [v0.73.1](/docs/free-gpu-tier)**, where it turned out not to be a streaming fix at all: the same assumption sat in fourteen places, so every task died on that hardware, not only a streamed one.
- Numbers are Windows/WDDM and therefore systematically pessimistic versus Linux. `expandable_segments:True` is silently ignored on Windows, and Soup detects that rather than claiming it is active.
- **If the model already fits resident on your card, do not enable it.** Streaming trades time for memory, and there is nothing to buy when memory is not the constraint.

## Rejected at config load

Every refusal is deterministic and happens before a single GPU byte is touched. Where a later release lifts a limit, the refusal message **names that release**; the rows marked `n/a` are refused on a structural ground and carry no roadmap promise either way.

**None of this constrains an ordinary resident run.** These are the refusals a run with `stream_layers: true` can hit, and several of the rows below name things that are perfectly legal, and common, with streaming off.

| Config, on a streaming run | Refused because | Lifted in |
| --- | --- | --- |
| `quantization` other than `none` or `4bit` | other quantisations store weights in formats that cannot be streamed into a pooled buffer | n/a |
| `batch_size: auto` | the auto-batch probe sizes a **resident** model, which a streaming run never loads. Set a concrete value; the pre-flight sizes it | n/a |
| architecture outside the ten-item allowlist (\*) | named explicitly, with the allowlist. Multimodal `gemma3` is refused on purpose: streaming a vision wrapper as a causal LM is the exact failure the allowlist exists to prevent | — |
| `task: grpo` or `task: ppo` | **permanent**, and the message says so rather than naming a release: generation rollouts re-read every layer once per generated token, which destroys the amortisation streaming depends on | n/a |
| `task` outside `sft`, `dpo`, `orpo`, `simpo`, `kto` | the message lists the accepted five. `ipo`, `bco` and `task: preference` are not among them | — |
| `task: kto` with `batch_size: 1` | TRL's KL term is degenerate at batch 1. Refused when the config is read rather than minutes later, after the checkpoint has been sharded | n/a |
| `backend: unsloth` / `backend: mlx` | streaming replaces the model-load path those backends own | n/a |
| `lora.r < 1` | the streamed base is frozen, so a run with no adapter is a no-op | n/a |
| `lora.use_dora`, `lora.use_vera`, `lora.init_strategy` other than `random` | PiSSA / OLoRA / LoftQ / DoRA / VeRA all initialise from the real base weight, which streaming keeps on the meta device | n/a |
| `unfrozen_parameters`, `lisa_enabled`, `packing`, `multipack`, `use_fsdp2_compile`, `train_router_only`, `expand_layers` | each independently rewrites or re-freezes the same layers streaming owns | n/a |
| `stream_source` / `stream_buffers` / `stream_vram_probe` / `stream_vram_override` / `stream_disk_kind` / `stream_pin` / `stream_ngram_source` set while `stream_layers: false` | a footgun: the knobs would silently do nothing | — |
| `moe_expert_quant` with `stream_layers: true` | added in **v0.74.0**. It is applied only by the resident setup path, so it was silently ignored on a streamed run rather than doing anything | — |
| `stream_pin: true` on the RAM tier when the box cannot page-lock the store | added in **v0.74.0**. `true` means insist. The refusal names the **store size**, not a page-lock ceiling, because the ceiling is deliberately left unprobed so a refusal can never cite a figure nobody measured. On the disk tier and on CPU there is nothing to page-lock, so it is announced and the run proceeds | — |
| `stream_source: ram` when the store fits available memory but store-plus-extras crosses the physical-host safety ceiling | added in **v0.74.0**, at pre-flight, instead of letting the kernel OOM-kill the process. `auto` falls back to the disk tier in the same case | — |
| a trainable `lora_*` parameter still on the meta device after PEFT attaches the adapter | added in **v0.73.3**. PEFT 0.18 creates streamed adapters on `meta` for Soup to materialise while PEFT 0.19 may create them as real tensors immediately, so "materialised zero" could not tell a healthy no-op from a missed adapter. The run is refused, naming the stranded parameter, instead of proceeding into a silent no-training run | — |
| a predicted peak VRAM larger than the free VRAM | added in v0.72.3, and it names `training.batch_size` and `data.max_length` as the two knobs that scale it linearly | — |
| `stream_source: ram` when the base does not fit in RAM | `ram` means insist, not prefer. The message offers `auto`, which falls back to the NVMe tier instead | — |
| the disk tier on a non-NVMe volume | 80 shards read twice per step on a spinning disk is a run that thrashes for hours. `unknown` media is refused rather than guessed | — |

(\*) One honest footnote: the architecture check is the only row here that is **not** a config-parse validator. It needs the model's own config, so it runs a moment later, at trainer setup. Still before any GPU work and still deterministic, but if you are counting on a pure-CPU `soup train --dry-run` to catch everything, that is the one that arrives late.

The generic pre-flight hardware-fit gate is **skipped** for streaming runs, because it models a resident run and would otherwise refuse exactly the runs streaming exists to enable. Since v0.72.3 a **streaming-specific** budget replaces it, and that one does refuse: it predicts peak VRAM from your batch, sequence length and vocabulary, which are the terms streaming does **not** bound. See [Scaling a streaming run](/docs/streaming-scaling#the-vram-pre-flight).

## Full config

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft
backend: transformers

data:
  train: ./data.jsonl
  format: alpaca
  max_length: 512
  val_split: 0.1

training:
  epochs: 3
  lr: 2e-5
  batch_size: 4                    # v0.72.3: bigger batches amortise the weight read
  gradient_accumulation_steps: 2   # v0.72.3: values above 1 are allowed
  quantization: 4bit               # NF4; 'none' streams bf16 instead
  gradient_checkpointing: true     # handled per-layer by the streamer
  stream_layers: true
  stream_source: auto              # RAM when it fits, NVMe disk when it does not
  stream_buffers: 2
  lora:
    r: 64
    alpha: 16

output: ./output
```

Gradient checkpointing is handled **per layer by the streamer**, and the Hugging Face Trainer's own is left off so layers are not recomputed twice.

That `batch_size: 4` is illustrative, not a recommendation: whether it fits depends on your card, the model's vocabulary and `max_length`, and the pre-flight will tell you before the run starts. [Sizing rules](/docs/streaming-scaling).

## Troubleshooting

- **"a streaming step is predicted to need X GB of VRAM but only Y GB is free"** — the v0.72.3 pre-flight. Streaming bounds the **weights**, not the activations or the logits, and both of those scale with `batch_size` times `data.max_length`. Lower either one. On a large-vocabulary model the logits tensor is usually the whole story.
- **"but only Y GB of RAM is free"** — you asked for `stream_source: ram` and the base does not fit in it. `ram` means insist, so it refuses rather than falling back. Set `stream_source: auto` to use the NVMe disk tier instead, free RAM, or pick a smaller base. If you are streaming bf16, `quantization: 4bit` shrinks the store about fourfold and is often enough on its own.
- **"layer streaming needs NVMe or more RAM"** — the base does not fit in RAM and the detected disk is not NVMe. `soup doctor --disk` reports what Soup detected on your machine. On a cloud box, check this one before you believe it: until v0.73.3 a paravirtual disk was read as a spinning one on the strength of a flag it defaults to. Since v0.73.3 the media type is measured when that flag is unreliable, and `training.stream_disk_kind: nvme` overrides it if detection is still wrong.
- **"could not page-lock the base ... falling back to a PAGEABLE RAM store"** — expected on a busy machine, and it costs real throughput: pageable memory makes the host-to-device copy synchronous. Training continues, more slowly. Close other applications, or switch to `quantization: 4bit` so the store is small enough to pin.
- **"layer streaming does not support model\_type=..."** — the message prints the full allowlist. Note that a real `google/gemma-3-*` checkpoint reports `gemma3`, the vision-capable wrapper, which is refused; the text-only `gemma3_text` is what streams.
- **"training.stream\_layers supports quantization='none' or '4bit'"** — those are the only two. Other quantisations store weights in a form that cannot be streamed into a pooled buffer.
- **Slower than you expected** — layer streaming trades time for memory. **If the model already fits resident on your card, do not enable it.**

## Roadmap

Each refusal above names its release, and this is the same list from the other side:

- **v0.72.1** (shipped) — the adapter-key correctness fix above, plus the `--hf-resume` refusal. It took the `.1` slot out of turn, which is why every later slot below moved up by one and every refusal message in the CLI was corrected to match.
- **v0.72.2** (shipped) — 4-bit (NF4) streaming, the capability jump that made 8B reachable. It also fixed a display bug where a streamed 4-bit run reported its parameter count about 6.5x too high (training was unaffected), and a startup regression that had the CLI importing PyTorch on every invocation, taking `soup --help` from 6.0 s back down to 1.15 s.
- **v0.72.3** (shipped) — breadth: six more architectures, batches above 1, gradient accumulation, `--resume` and `--hf-resume`, a batch- and vocabulary-aware VRAM pre-flight, and the NVMe disk overflow tier. [The full page](/docs/streaming-scaling).
- **v0.72.4** (shipped) — preference losses: DPO, ORPO, SimPO and KTO against a streamed base, with DPO's reference model taken from that same stream with its adapters switched off, so it costs no extra weights. [The full page](/docs/streaming-preference).
- **v0.73.0** (shipped) — the release that came out of three days on borrowed hardware. It repaired [the NF4 gradient defect](#if-you-streamed-a-32b-or-larger-model-in-nf4) that only a resident reference could have found, refused streaming under `nn.DataParallel` rather than quietly using one card of eight, and fixed the four preference losses whose gradient-checkpointing flag was never set. [What the whole exercise measured](/docs/external-validation).
- **v0.73.1** (shipped) — not a streaming release at heart, though it repaired streaming too: bf16 was assumed on every CUDA card in fourteen places, so [every pre-Ampere card failed on every task](/docs/free-gpu-tier). It also caught this feature's own VRAM pre-flight under-predicting at long sequence and shipped `training.stream_vram_probe`, which measures one real step instead of predicting it.
- **v0.73.2** (shipped) — nothing streaming-specific: it repaired [the release gate](/docs/ship-gate-repairs) that decides whether a tuned model ships at all.
- **v0.73.3** (shipped) — two streaming repairs, both contributed. A **paravirtual disk** reports itself as rotational with no media hint, so a genuinely NVMe-backed cloud disk measured at 1.5 GB/s was refused the disk tier, which is exactly the audience that tier exists for; when the rotational flag is unreliable the media type is now settled by a bounded direct sequential read, with a 1 GB/s floor, and `training.stream_disk_kind` as the manual override. And the streamed build now **enforces its own postcondition**: PEFT 0.18 creates streamed adapters on the meta device for Soup to materialise while PEFT 0.19 may create them as real tensors immediately, so "materialised zero" could not tell a healthy no-op from a missed adapter. The run is refused, naming the stranded parameter, rather than proceeding into a silent no-training run.
- **GRPO and PPO are explicitly not planned.** Rollouts need generation, and generation re-reads the model per token.

**What is next is a measurement, not a feature.** The 14B reference benchmark that was going to follow v0.72.4 did **not** become v0.73.1: that slot went to the pre-Ampere repair and the measured VRAM probe instead, and v0.73.2 went to the release gate. The benchmark now sits at the **end** of the v0.73 series rather than at its start, and it is still hardware-gated: it wants a card this project can keep rather than three borrowed days, run under three disk conditions and three sequence lengths with utilisation traces. The borrowed H100 box overtook part of it (14B, 32B and 72B were measured against resident references a 4 GB machine cannot hold) but it was a validation campaign, not that structured benchmark, and the [RAM-versus-disk question](#honest-scope) it was meant to answer is still unmeasured because that box had no NVMe.

## Measurement records and citation

The gate records behind every number on this page are published in full, including the checks that failed, the diagnoses that turned out wrong, and the figures that were measured and then discarded: [the benchmarks directory](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks). They are working records rather than a report assembled afterwards, so read them front to back; a passage quoted out of order may be one the same page later refutes.

The newest of them is the one from hardware nobody here owns: three days on an 8x H100 box, which is the first machine able to hold a **resident reference** for a model worth streaming. That record reproduces the headline row on a completely different card and stack, extends the forward check to 72B, compares the method against DeepSpeed ZeRO-3, shows a streamed model converging indistinguishably from a resident one, and contains the gradient defect it found on the way. [Read the summary](/docs/external-validation).

The work also has a preprint, cited by its concept DOI so a revision never strands a reference: [10.5281/zenodo.21771064](https://doi.org/10.5281/zenodo.21771064). [The paper page](/docs/paper) is the short version: what it measures, the correctness protocol it defends hardest, the three findings that have nothing to do with streaming, what it explicitly does not claim, and the BibTeX entry.

## Shard cache

The first streaming run rewrites the checkpoint into one safetensors shard per decoder layer under `~/.soup/layer-stream/` (override with `SOUP_LAYER_STREAM_CACHE_DIR`), quantising as it goes when you asked for `4bit`. The rewrite works one tensor at a time, so sharding a model that does not fit never requires it to fit, and the quantisation happens **once, offline**, not on every run.

The cache is keyed to the **quantisation, the dtype, the quantisation device and a fingerprint of the source checkpoint**. Switching between `none` and `4bit`, or retraining a base in place, therefore **re-shards instead of silently streaming the wrong bytes**.

## See also

- [Scaling a streaming run](/docs/streaming-scaling) — v0.72.3: which architectures stream, how to size batch and sequence length against the VRAM pre-flight, batch versus gradient accumulation, resume, and the NVMe disk tier.
- [Preference losses over streaming](/docs/streaming-preference) — v0.72.4: DPO, ORPO, SimPO and KTO against a streamed base, why the reference model costs no extra weights, and what it costs in time instead.
- [Validation on hardware we do not own](/docs/external-validation) — the same mechanism on 8x H100: a resident reference at 8B through 72B, the DeepSpeed comparison, the convergence result, and the defect the exercise found.
- [Training](/docs/training) — the training guide the streamed run otherwise follows unchanged.
- [Spectrum targeted training](/docs/spectrum-targeted-training) — the other way to train a large model small: pick the high-signal layers instead of streaming all of them.
- [LISA](/docs/lisa) — full fine-tune quality without a full fine-tune, for models that do fit resident. Measured at 3B and 8B it beats full fine-tuning on held-out loss but costs more memory than LoRA, not less.

[PreviousReward Forge](/docs/reward-verifier)[NextStreaming: Scale](/docs/streaming-scaling)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="048-streaming-scaling"></a>

# 48. Scaling a streaming run (v0.72.3)

*Source: <https://trysoup.dev/docs/streaming-scaling>*

[Layer streaming](/docs/layer-streaming) proved a mechanism: the frozen base never loads resident, so peak VRAM is bounded by one decoder layer instead of the whole model, and NF4 shrank that store far enough to put Llama-3.1-8B on a 4 GB laptop GPU.

It was also, on purpose, barely usable for planning a real run. Llama and Qwen only. Batch size 1. No gradient accumulation. No resume. RAM or nothing.

**v0.72.3 lifts all of it**, and each capability was gated against a streamed-versus-resident bit-exactness reference before it was written rather than after.

## Which models stream

Ten `model_type` values are on the allowlist. Six of them arrived in v0.72.3 and the tenth in v0.74.0:

| `model_type` | Since | Notes |
| --- | --- | --- |
| `llama` | v0.72.0 | the 8B row on the [layer streaming](/docs/layer-streaming#measured-numbers) page is this one |
| `qwen2` | v0.72.0 | every throughput row on these pages is Llama or Qwen |
| `qwen3` | v0.72.0 |  |
| `mistral` | **v0.72.3** |  |
| `gemma` | **v0.72.3** |  |
| `gemma2` | **v0.72.3** |  |
| `gemma3_text` | **v0.72.3** | the text-only config. See the warning below |
| `phi` | **v0.72.3** |  |
| `phi3` | **v0.72.3** | fuses Q, K and V into one `qkv_proj`, so there is no `q_proj` to find |
| `qwen4_exp` | **v0.74.0** | float32 tiny-model parity only. See the caveat below |

Four aliases route onto families already on the list rather than counting as new ones: `qwen3_5`, `qwen3_5_text`, `qwen3_5_moe` and `qwen3_5_moe_text` all reach the `qwen3` streamer, and `qwen4_exp_text` reaches `qwen4_exp`. Upstream states why each alias needs its own control: mapping a model type by name alone is not enough to establish that its decoder graph is safe.

> **The v0.74.0 additions carry weaker evidence than the original nine, and the difference is stated rather than smoothed over.** Only the original nine are verified bit-exact in **both** bf16 and NF4. Qwen3.5's dense and MoE decoder paths are verified against resident controls **on CPU**; the MoE path also has live streamed training on Qwen3.5-35B-A3B with NF4 and MoE LoRA on a 3072-token dataset, and that run has **no resident control at all**, because no available machine can hold 35B resident. Qwen4-Exp has an exact **float32 tiny-model** parity gate, including its external N-gram table, and real-checkpoint plus NF4 validation are still pending. Its N-gram access is governed by `training.stream_ngram_source` (`auto`, `ram`, `disk`).

Each of the six added in v0.72.3 was verified **bit-exact against the same checkpoint loaded resident, under both bf16 and NF4**. Phi-3 is the interesting one: streaming has to substitute weights into a layer whose attention projection is fused, and it comes out bit-identical anyway.

> **`gemma3` is not `gemma3_text`.** A real `google/gemma-3-*` checkpoint reports `model_type: gemma3`, which is the vision-capable wrapper, and it is **refused**. Streaming a multimodal wrapper as if it were a causal LM is exactly the failure an allowlist exists to prevent, so the refusal is deliberate rather than an oversight.

**There is no throughput measurement for any family beyond Llama and Qwen, so none is claimed** — not for the six added in v0.72.3, and not for Qwen3.5 or Qwen4-Exp either. Every tok/s figure published for layer streaming is Llama or Qwen. What was established for the newer families is correctness, not speed.

## Batch size beats gradient accumulation

Both were refused before v0.72.3 and both work now. They are not interchangeable, and the release measured the difference instead of reasoning about it.

Measured on Qwen2.5-0.5B in bf16, sequence length 256, pinned RAM store, 50 steps after 10 warm-up:

| `batch_size` | `gradient_accumulation_steps` | Throughput | Peak VRAM |
| --- | --- | --- | --- |
| 1 | 1 | 556.6 tok/s | 0.842 GB |
| 1 | 4 | 540.1 tok/s | 0.846 GB |
| **4** | **1** | **1378.0 tok/s** | 2.28 GB |

At the same effective batch of 4, **raising `batch_size` measured about 2.52x faster than accumulating**.

The reason is structural, not incidental. A real batch amortises each layer's load over more tokens. Accumulation does not: every micro-batch re-reads the entire base, so the layer reads per 1000 tokens stayed flat across accumulation 1, 2 and 4. Accumulation is not useless, though. It holds peak VRAM almost exactly flat (0.842 GB to 0.846 GB) where batch 4 cost 2.28 GB, which is the whole point of it.

**The rule: raise `batch_size` while the VRAM budget allows, then accumulate for the rest.** Soup prints that advice at run start when it sees you accumulating.

## The VRAM pre-flight

Once batches scale, a new way to fail appears, and it is not obvious from the outside.

**Streaming bounds the weights. It does nothing about activations or the logits tensor, and both scale with `batch_size` times `data.max_length`.** On a model with a 151,936-token vocabulary at batch 8, the logits tensor alone measured **8.71 GB, which is 146 times the entire layer-buffer pool of 0.060 GB**. Streaming the weights perfectly and then allocating an 8.71 GB logits tensor is not a win.

So `soup train` now predicts peak VRAM before the run and refuses one that will not fit. The panel it prints carries the budget and a forecast, here for a **small model** at batch 2 on the 4 GB development card:

```
  peak VRAM    ~0.48 GB at batch 2 x seq 256 (logits 0.35 GB)
  free VRAM    3.46 GB
  forecast     5685-8361 tok/s — a compute-bound bound, not a promise
               (from a GEMM ceiling measured on this card now @ 862 MHz)
```

Above those lines the panel also names the architecture and tier, the size of the layer store, the buffer pool and what stays resident. Those figures scale with the model, so the four lines above are the ones worth reading before a run: they are the only part that changes when you change `batch_size` or `max_length`.

And when it does not fit:

```
a streaming step is predicted to need X GB of VRAM but only Y GB is free.
Streaming bounds the WEIGHTS, not the activations or the logits — lower
training.batch_size or data.max_length, both of which scale this linearly.
```

### The estimator had a real bug in it

The first version of the budget charged **6 bytes per logit element** from first principles. The measured peak is **14**. The old constant **under-predicted that term by 2.33x**, which on the largest term in the whole budget is the difference between a prediction and a guess.

A later measurement on different hardware took that 14 apart stage by stage, with three repeats and no spread at all, and the total held while the explanation did not. The number is **12 plus 2**: the loss arithmetic costs 12, being the bf16 logits alongside **three** fp32 buffers of the same shape, and the remaining 2 is a retention, the cost of holding the model's output object alive across `backward()`. An earlier telling of this said "bf16 logits, fp32 upcast, log-softmax output and gradient, all live at once", which is right in total and wrong in detail: the upcast is freed when the loss function returns. The 12 is also stack-independent, measured identically on two very different torch and TRL versions.

The corrected estimate was fitted against **ten real runs** across two models with a 3.1x vocabulary contrast, at batches 1 to 8 and two sequence lengths. Worst error: **0.85%**, and it never under-predicted any of them.

### And then it did under-predict, at long sequence (v0.73.1)

That "never under-predicts" was the estimator's contract, and it is the reason the whole gate is trustworthy: on Windows an over-budget allocation does not raise, it spills silently into host memory. **v0.73.1 measured the contract failing.**

Through the real `soup train` on the same 4 GB laptop, with SmolLM2-135M streamed in bf16 at batch 1:

| Sequence | Predicted | Real peak | Ratio |
| --- | --- | --- | --- |
| 4352 | 3.282 GB | 3.036 GB | 1.081x, over-predicts, safe |
| 5120 | 3.844 GB | 4.118 GB | **0.934x, under-predicts** |
| 6144 | 4.590 GB | 5.830 GB | **0.787x, under by 21%** |

**The ten-run fit above could not have caught this, and that is the lesson.** Every one of its rows sits at sequence 256 or 512. It varies batch, so it says nothing whatever about sequence length. A control only covers the variable it varies.

The mechanism is **deliberately not claimed**. The obvious candidate, the quadratic term from the attention score matrix, does not settle the numbers, and a formula cannot model a term nobody has identified. So the answer shipped is not another coefficient, it is a measurement, and the fitted estimate is left in place as the default. See [v0.73.1](/docs/free-gpu-tier) for the probe that replaces it on request.

**A second box has since said this does not reproduce there.** A contributor ran the same protocol on an NVIDIA A10G with a much newer stack (torch 2.13, transformers 5.16.1) and the ratio is flat at about **1.16x over-prediction** from sequence 2048 through 6144, on two models. The record publishes its leading hypothesis as a **negative result with a positive control**, and explicitly does **not** refute the reading for this 3050. Taken together the honest conclusion is that the term varies per-stack \*and\* per-sequence-length, which is why the answer is a measurement rather than a constant. See [the v0.74.0 record](/docs/loaded-in-fp32).

### Why refusing beats trusting the driver

On Windows, WDDM does not raise on overcommit. It pages to host memory instead. During this work a run that should have failed outright instead reached a **9.27 GB peak on a card with 4.29 GB**, silently, at a throughput nobody would want. That is the case the pre-flight exists to catch: not a crash, but a run that appears to work.

## The throughput forecast

The panel quotes a throughput range, and where that range comes from is a deliberate design choice: a **GEMM ceiling measured on your own card in that session**, printed next to the SM clock. Never a compiled-in per-card constant.

That is a response to a measurement rather than a preference. **This one card produced 3.5 and 7.6 TFLOPS in two different sessions at the same reported clock.** A baked-in table would have been wrong about half the time, on the same hardware. Real streamed runs land at **68 to 100% of their measured ceiling**, which is why the line calls itself a bound and not a promise.

## Resume works now, and why it could not before

`--resume` and `--hf-resume` were refused for streaming runs. The refusal was not caution; it was covering a bug.

**Adapters could not be loaded into a streamed model at all.** PyTorch's `load_state_dict` narrows keys by child name, and the streaming wrapper holds the real decoder layer as a child, so a canonically saved checkpoint matched **0 of N tensors**. PEFT reports missing keys as a warning rather than an error, so nothing failed. A resumed run simply reproduced the **from-scratch loss curve exactly**, which is the kind of bug that looks like a successful run.

The fix redirects canonical keys at load time, mirroring the save-side fix from [v0.72.1](/docs/layer-streaming#read-this-first-if-you-already-trained-with-streaming). It is **load-side only**, which is worth stating precisely: v0.72.0's forward-path bit-exactness results stand without being re-run, because nothing in the forward path changed.

**What was verified:** the adapter round-trip now lands every tensor, the device map is preserved, decoder parameters stay on the `meta` device (so the run is still streaming, not quietly materialised), and loss continuity holds on the production CUDA path.

**What could not be demonstrated, and why it is not streaming's fault:** end-to-end `soup train --resume` on the development box. `transformers` refuses `torch.load` below torch 2.6 under CVE-2025-32434, and that blocked **every** resume on that machine, streaming or not. (**Since unreachable in v0.75.0**, which raised the declared floor to `torch>=2.6.0` and proved it in CI, so no supported install sits below it. The streaming half was verified on the production CUDA path at the time; what was missing was a box that could run the control.)

**Still open:** loading an adapter into a streamed model works, but in memory `named_parameters()` and `state_dict()` still disagree. That is the deliberate cost of fixing serialisation rather than rewriting the wrapper.

## The disk overflow tier

If the base does not fit in RAM either, v0.72.3 streams it from NVMe, holding **nothing** resident.

```yaml
training:
  stream_layers: true
  batch_size: 1          # streaming refuses batch_size 'auto', which is the default
  stream_source: auto    # RAM when the base fits, NVMe when it does not
```

| `stream_source` | Behaviour |
| --- | --- |
| `auto` (default) | RAM when the base fits it, otherwise fall back to the NVMe tier, with a printed note |
| `ram` | insist on RAM. **Refuses rather than falling back**, so a run that must stay in RAM cannot quietly become a disk run |
| `disk` | force the NVMe tier even when RAM would have fit |

**NVMe-class only.** SATA SSD, spinning disk and undetectable media are all refused. That is not fussiness: the streamer reads every shard twice per step, so an 80-layer model is 160 seeks per step on a spinning disk and the run thrashes for hours. Unknown media is refused rather than guessed, because guessing wrong costs more than stopping.

**What "NVMe-class" means changed in v0.73.3, and it matters on a cloud box.** Detection used to trust the kernel's rotational flag, which a paravirtual (virtio) device reports as `1` with no media hint — so a genuinely NVMe-backed cloud disk, measured at 1.5 GB/s, was classified as a spinning one and denied the tier it was built for. `rotational=0` still settles it as solid state. When the flag is unreliable, the media type is now decided by a **bounded direct sequential read** rather than by the flag: at or above **1 GB/s** the disk earns the tier, and a genuinely slow one still does not. Deliberately above SATA's practical ceiling, and an unmeasurable disk is still treated as the slow case, which is the safe direction.

`training.stream_disk_kind` (`nvme` / `ssd` / `hdd`) is the escape hatch for when even that is wrong. It prints what it overrode beside what was detected, and it carries **no measured rate** on purpose, so a later refusal can never cite a reading you overrode.

Check what Soup detects on your machine:

```bash
soup doctor --disk
```

It reports `NVMe`, `SATA SSD`, `HDD` or `Unknown`, and it is opt-in because the probe costs about 9 seconds cold (about 2.4 seconds warm) on Windows. On Windows, where a machine can present several physical disks with no way to attribute the volume, Soup reports the **worst** one it found.

**On Linux the probe writes**, and that is a side effect rather than just a time cost, so it is worth stating plainly: where the kernel's `rotational` flag is unreliable, Soup writes a small scratch file beside where the shards would go, reopens it with `O_DIRECT` to bypass the page cache, and times a few bounded page-aligned sequential reads, keeping the **fastest** one so a single cold sample cannot under-measure a fast device and wrongly refuse it. The scratch file is **always removed**, any failure (no `O_DIRECT` on that filesystem, no write permission) returns nothing so the caller stays conservative, and each read is bounded so the probe cannot grow into the 9-second cost the Windows path already carries. Media it cannot identify stays `unknown`, and the disk tier refuses `unknown` rather than guessing.

### The honest part

The disk tier's **correctness** is verified: it is bit-exact against the RAM tier.

**How much slower it is has not been measured, and no figure is claimed for it.** The reason is that a like-for-like comparison is hard to construct honestly on the development hardware. safetensors memory-maps the shards, so on a machine with spare RAM the OS page cache keeps them resident between steps, which means the "disk" tier is partly a RAM tier. And at roughly 5 effective TFLOPS the NVMe read largely hides under compute anyway. A number measured there would be misleading rather than merely incomplete, so there is no number.

## A config that uses all of it

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft
backend: transformers

data:
  train: ./data.jsonl
  format: alpaca
  max_length: 512

training:
  epochs: 3
  lr: 2e-5
  batch_size: 4                    # raise this first; the pre-flight sizes it
  gradient_accumulation_steps: 2   # then accumulate for the rest
  quantization: 4bit               # NF4: ~4x smaller store
  gradient_checkpointing: true
  stream_layers: true
  stream_source: auto              # RAM, falling back to NVMe
  stream_buffers: 2
  lora:
    r: 64
    alpha: 16

output: ./output
```

Those batch and accumulation values are **illustrative, not a recommendation**. Whether they fit depends on your card, the model's vocabulary and `max_length`, and the pre-flight will tell you before the run starts rather than after.

## Also in v0.72.3

Three fixes and one dependency cap that are not about capability:

- The guard meant to refuse non-NVMe media was wired to a hardcoded constant and **could never fire**. It fires now.
- Streaming weight sources are released when training ends **or raises**. This matters more on the disk tier, which holds one open shard handle per decoder layer.
- Subprocess helpers resolve tools to absolute paths, because on Windows `CreateProcess` searches the current directory before `PATH`.
- The `[mcp]` extra is capped below 2.0. The MCP SDK's 2.0.0 release removed an API `soup mcp serve` round-trips through, which broke its round-trip tests for anyone installing fresh. Support for the 2.x API is tracked separately.

## What is still out of scope

Layer streaming remains **BETA**.

- `task` must be one of `sft`, `dpo`, `orpo`, `simpo`, `kto`. The four preference losses landed in v0.72.4; `ipo`, `bco` and the unified `task: preference` dispatcher are still refused.
- **GRPO and PPO are explicitly not planned.** Rollouts need generation, and generation re-reads the model per token, which destroys the amortisation streaming depends on.
- `backend: transformers`, `modality: text`, plain LoRA, and `quantization` of `none` or `4bit`.
- `batch_size: auto` is refused: the auto-batch probe sizes a resident model, which a streaming run never loads.
- Nothing above 8B has been measured on the 4 GB card, so nothing on this page speaks for a larger model there. 14B, 32B and 72B were measured later on a borrowed 8x H100 box, which also turned up [a gradient defect in NF4 above roughly 165 MB per decoder layer](/docs/external-validation).

## Measurement records and citation

Two of this page's results are written up in the preprint rather than only logged: the peak-VRAM predictor, including the corrected 14-bytes-per-logit-element constant, and the finding that gradient accumulation is per-token I/O-neutral with a 2.52x opportunity cost against batch size. [The paper page](/docs/paper) summarises both. The raw gate record for this release, failures and discarded numbers included, is in [the benchmarks directory](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks).

## See also

- [Layer streaming](/docs/layer-streaming) — the mechanism, the measured numbers and the full refusal table.
- [Preference losses over streaming](/docs/streaming-preference) — DPO, ORPO, SimPO and KTO against a streamed base, and why the reference model costs no extra weights.
- [The layer streaming paper](/docs/paper) — the preprint behind these numbers, what it measured and what it explicitly does not claim.
- [Training](/docs/training) — everything a streamed run otherwise follows unchanged.
- [Speed and memory](/docs/training-speed-memory) — the knobs that matter when the model does fit resident.

[PreviousLayer Streaming](/docs/layer-streaming)[NextStreaming: Align](/docs/streaming-preference)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="049-streaming-preference"></a>

# 49. Preference losses over layer streaming (v0.72.4)

*Source: <https://trysoup.dev/docs/streaming-preference>*

Until v0.72.4, a model too big for your card could only be **supervised** fine-tuned on it. `task` had to be `sft`, and `dpo`, `orpo`, `simpo` and `kto` were all refused when the config was read. All four run against a streamed base now, with the same keys SFT already used, so preference alignment stops being the step that forces you to rent a bigger card.

Nothing else about streaming changed. If you have not read it yet, start with [Layer streaming](/docs/layer-streaming) for the mechanism and [Scaling a streaming run](/docs/streaming-scaling) for architectures, batches and the disk tier. This page is only about what the preference losses add on top.

## The five accepted tasks

```
sft   dpo   orpo   simpo   kto
```

That list is exact. `ipo`, `bco` and the unified `task: preference` dispatcher are **not** in the streaming allowlist, so "all preference losses stream" would be false. `grpo` and `ppo` are excluded permanently, and their refusal deliberately names no release: generation rollouts re-read every layer once per generated token, which destroys the amortisation streaming exists to buy.

## DPO's reference model is free

DPO scores the policy against a frozen reference. The obvious implementation builds a second copy of the model, which doubles the weights and defeats the entire premise of streaming: you would be back to needing the model twice over on a card that could not hold it once.

Soup takes the reference from **the same streamed base with its LoRA adapters switched off**. Policy and reference are one set of weights, one RAM store and one buffer pool, and the adapter is the only difference between the two forward passes.

Measured on the reference box, a 4 GB RTX 3050 Laptop, in bf16 with a 365.2M-parameter model (730.4 MB of weights, 24 decoder layers, vocabulary 260, sequence length 64, batch 1):

| Arm | Peak VRAM | vs streamed SFT |
| --- | --- | --- |
| Streamed SFT | 89.53 MB | 1.000x |
| Streamed DPO | 81.87 MB | **0.914x** |
| Control: DPO forced to build a real second model | 812.32 MB | 9.92x |

The RAM store was byte-identical between the SFT and DPO arms (729.91 MB each), and so was the VRAM buffer pool (60.83 MB each).

The control arm is what makes the headline mean anything. Forcing a real second instance moved the peak by **730.44 MB** against **730.44 MB** of weights, which is exactly one copy. As the gate record puts it: "DPO is not 2x SFT" means nothing unless the same harness can show what 2x looks like.

### Read 0.914x as "no second copy", not as a saving

DPO is not cheaper than SFT in general. That row sits below 1.0 because of the fixture, not because of the feature: the SFT arm computes its loss over all 64 positions, while the DPO arm splits the same 64 into a 32-token prompt and a 32-token completion, so its logits tensor is smaller. A negative delta is simply the strongest available form of "there is no second copy of the weights".

These numbers also come from a **synthetic 365.2M-parameter model**, not from a real checkpoint and not from Llama-3.1-8B. They are a memory-accounting result, not a throughput result.

### Why this was measured rather than asserted

A passing loss curve cannot detect the failure this feature is exposed to. The streamed layer substitutes base weights through `functional_call` rather than through the module's own `forward`, so it is entirely plausible that disabling the adapter is a silent no-op through that path. If it were, the reference would **be** the policy, every log-ratio would be zero, and the DPO loss would sit at `0.6931` forever, which reads as slow training rather than as a bug.

So three things were checked that a loss curve cannot check:

1. The memory table above, with its forced-second-instance control.
2. A policy-versus-reference gap of `8.219452e-01` on chosen completions, proving the two passes really differ.
3. A zero-adapter control measuring exactly `0.000e+00`, proving that gap comes from the adapter and not from some other difference between the two forwards.

## KTO is not reference-free

However it is usually described, KTO picks its reference exactly the way DPO does, so it gets exactly the same treatment: the same streamed base with adapters disabled, no second copy. **ORPO and SimPO genuinely are reference-free** and never construct one at all.

KTO carries one extra requirement, and Soup enforces it when the config is read rather than minutes into a run after the checkpoint has already been sharded:

```
task='kto' requires training.batch_size >= 2 (TRL's KL term is
degenerate at batch 1).
```

Note that KTO is streamable **only because v0.72.3 lifted streaming's own batch-1 restriction**. Under v0.72.0 through v0.72.2 it could not have shipped at all.

## Free in memory is not free in time

DPO walks the layer stack more often than supervised fine-tuning does, because it adds a reference forward on top of the policy forward and the gradient-checkpoint recompute. Measured on the same 24-layer model: **46 layer loads per step for SFT against 70 for DPO, which is 1.52x**.

That is the honest cost, and it is the one to plan around. Streaming makes the reference free in memory; it does not make it free.

## Correctness

Every one of the four losses is **bit-exact against a resident run of the same loss**, difference exactly `0.0`. DPO's arm ran in float32 on CPU precisely so that "bit-exact" means literally zero rather than bf16 noise: streamed `0.67242944` against resident `0.67242944` over 16 synchronised adapter tensors. Layer-0 adapter gradients are non-zero, and two runs at the same seed differ by `0.000e+00`.

End to end through the released CLI, streaming SmolLM2-135M under NF4 (30 layers, a 0.05 GB pinned RAM store, two 2 MB VRAM buffers):

| Task | Loss |
| --- | --- |
| `dpo` | 0.6931 to 0.6695 |
| `orpo` | 5.3816 to 5.0559 |
| `simpo` | 5.2033 to 4.8749 |
| `kto` | 0.5000 to 0.4904 (6 epochs) |

All four saved adapters are ordinary LoRA files: 120 tensors, zero keys carrying the streaming wrapper segment, and 60 of 60 `lora_B` tensors non-zero. They load into a non-streaming model like any other adapter.

## A config that runs

DPO over a streamed, NF4-quantized base:

```yaml
base: Qwen/Qwen2.5-3B
task: dpo
backend: transformers        # streaming requires it

data:
  train: ./data/preferences.jsonl
  format: dpo
  max_length: 512            # see the pre-flight note below

training:
  epochs: 3
  dpo_beta: 0.1
  batch_size: 1              # a concrete value; "auto" is refused
  gradient_accumulation_steps: 1
  quantization: 4bit         # or none
  gradient_checkpointing: true
  stream_layers: true
  stream_source: auto        # RAM when it fits, NVMe when it does not
  stream_buffers: 2
  lora:
    r: 64
    alpha: 16

output: ./output
```

The other three are the same file with one or two lines changed:

- **ORPO**: `task: orpo`, and `orpo_beta: 0.1` in place of `dpo_beta`.
- **SimPO**: `task: simpo`, with `simpo_gamma: 0.5` and `cpo_alpha: 1.0`.
- **KTO**: `task: kto`, `format: kto`, `kto_beta: 0.1`, and `batch_size: 2` or more.

## Before you configure it: the pre-flight is a loose upper bound

The [VRAM pre-flight](/docs/streaming-scaling) predicts peak VRAM and refuses a run that will not fit. It is **sound but conservative**, and a preference run feels that most because it sends twice the rows through the same charge of 14 bytes per logit element, while TRL reduces preference logits to per-token log-probabilities with `selective_log_softmax` instead of holding a full-vocabulary fp32 upcast. The gap is large: DPO's entire above-resident cost measured 51.76 MB where the charge for the same shape is roughly 458 MB.

One correction worth carrying, from a later run of 72 configurations with three repeats and no spread: **the over-prediction is not a preference-loss problem.** A supervised control at the same effective row count misses by the same margin, so doubling the rows for a paired loss is the right thing to do and one shared coefficient is simply too high. Preference losses are where you notice it, not where it comes from.

In practice, on a 4 GB card with a 128k-vocabulary 1B model, **DPO is allowed at `max_length: 512` and refused from `768` up, even though it would probably fit.**

That shipped deliberately, because under-predicting is the strictly worse failure. On Windows an overcommit is not an exception you can catch: WDDM silently spills into shared host memory, so the run completes an order of magnitude slower with no error at all. A run completing is not evidence that its configuration fits. Refusing is.

If the pre-flight refuses a preference run you believe fits, lower `data.max_length` first. Tightening the estimate for these losses is tracked upstream.

## A packaging bug fixed along the way

Six preference trainers pass a field that TRL removed across several of its own releases, so on a fresh install `soup train with task: orpo` could fail at import before training ever started. It was invisible to CI because the TRL imports live inside the trainer's `setup()`, and no test had ever called `setup()` on those wrappers. The dependency bound that pins it was then settled by **constructing all six configs against each candidate version** rather than by reading source, which is the general lesson worth keeping: a version bound derived by reading source is a hypothesis, and the experiment that tests it is constructing the object.

This was a pre-existing defect, not one v0.72.4 introduced. A contract test now drives the real `setup()` for all six on the ordinary non-streaming path, and derives its covered set from the trainer sources so a seventh trainer joins automatically.

## What is still out of scope

Layer streaming remains **BETA**.

- `task` must be one of `sft`, `dpo`, `orpo`, `simpo`, `kto`. `ipo`, `bco` and `task: preference` are refused.
- **GRPO and PPO are permanently excluded**, not pending a release.
- `backend: transformers`, `modality: text`, plain LoRA, and `quantization` of `none` or `4bit`.
- **No tokens-per-second figure is claimed for any preference loss, at any model size**, because none has been measured. A later run on borrowed hardware timed all four in samples per second, which is a different unit and a directional one; see the section below.
- The sizes above 8B that have been measured for streaming were measured on server hardware, not on the card this feature targets. [What those runs establish](/docs/external-validation).

## Since measured on a real 8B

The numbers above come from a 365.2M-parameter synthetic fixture, which is the right size to make a second copy of the weights impossible to miss but the wrong size to be convincing on its own. The same claim was later checked on **Llama-3.1-8B in NF4, streamed, through the shipped CLI**, on an 8x H100 box:

| Streamed task | Reference model | Peak VRAM | Samples/s, median of 3 |
| --- | --- | --- | --- |
| `sft` | none | 3,689 MB | 6.082 |
| `orpo` | none, genuinely reference-free | 3,719 MB | 5.973 |
| `simpo` | none, genuinely reference-free | 3,719 MB | 5.946 |
| `dpo` | the same base, adapters disabled | 3,733 MB | 4.665 |
| `kto` | the same base plus a separate KL forward | 3,669 MB | 3.595 |

**Peak VRAM is flat across all five, within 64 MB or 1.7%.** DPO costs **44 MB more than supervised fine-tuning**, against roughly 5.6 GB for a second resident copy of an NF4 8B. That is the whole claim of this page, measured at a size where a second copy could not hide.

The throughput column needs three cautions. These are **samples per second, not tokens per second**, so they do not translate into the tok/s figures quoted elsewhere on this site. They come from 64-row single-epoch runs where setup is a large share of an 11 to 14 second step, so **the ordering is reproducible and the absolute ratios are directional**. And `kto` ran a different dataset, unpaired, so only its VRAM column compares directly.

Note that DPO's 0.77x here and the **1.52x** layer reads quoted above are not the same metric and neither corrects the other: one counts samples per second end to end, the other counts weight reads per optimizer step.

One scoping note on a rule stated elsewhere: **a preference loss on Llama-3.1-8B is refused by the pre-flight on a 4 GB card**, and that is a property of the card, not of the model. On an 80 GB card the same configuration passes the pre-flight and trains, which is exactly what the table above is.

## Measurement records and citation

The gate record behind this release is published in full, including the checks that failed, the diagnoses that turned out wrong, and the numbers that were measured and then discarded: [the benchmarks directory](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks). The layer-streaming work also has a preprint, [10.5281/zenodo.21771064](https://doi.org/10.5281/zenodo.21771064), summarised on [the paper page](/docs/paper). Note the scope: v1 of the preprint measured the mechanism as it shipped in v0.72.3, v2 adds the 8x H100 session and the correctness repair that shipped in v0.73.0, and v3 retracts one explanation v2 gave without changing a measured number. The preference losses on this page came after v1 and are still outside what the paper measures.

## See also

- [Layer streaming](/docs/layer-streaming) — the mechanism, the measured numbers and the full refusal table.
- [Scaling a streaming run](/docs/streaming-scaling) — architectures, batch versus gradient accumulation, the pre-flight, resume and the disk tier.
- [Preference variety](/docs/preference-variety) — the preference losses themselves, and how they differ.
- [Online DPO and the judge in the loop](/docs/online-dpo) — preference training with a judge or reward model on-policy.

[PreviousStreaming: Scale](/docs/streaming-scaling)[NextThe paper](/docs/paper)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="050-paper"></a>

# 50. The layer streaming paper

*Source: <https://trysoup.dev/docs/paper>*

The mechanism behind [training an 8B model on a 4 GB laptop GPU](/docs/layer-streaming) is written up as a preprint, together with the correctness protocol that verifies a streamed run is bit-exact against a resident one. This page is the short version, plus everything you need to cite it.

> **Exact Layer Streaming: LoRA Fine-Tuning of an 8B Model on a 4 GB Laptop GPU** (v3). Makazhan, A. (2026). Zenodo. [10.5281/zenodo.21918325](https://doi.org/10.5281/zenodo.21918325). Preprint, CC-BY-4.0.

**Version 3 is current, published 13 August 2026.** The title and the claim are unchanged, still 8B on 4 GB, and no measured number has changed since v1. [What version 2 added](#what-version-2-adds) is a session on hardware the project does not own; [what version 3 does](#what-version-3-adds) is retract one explanation version 2 gave for it.

Two DOIs, and they are not interchangeable:

| DOI | What it points at | Use it when |
| --- | --- | --- |
| [10.5281/zenodo.21771064](https://doi.org/10.5281/zenodo.21771064) | the **concept** DOI, always the newest version, v3 today | you mean "the paper" and want the reference to follow it forward |
| [10.5281/zenodo.21918325](https://doi.org/10.5281/zenodo.21918325) | **v3** specifically | you are citing a version you actually read |

**Cite the version you used.** v1 was not withdrawn and stays citable at its own version DOI; nothing in it was retracted, and the section below says exactly what changed.

## What it reports

Two results, both on one machine: an RTX 3050 Laptop with 4 GB of VRAM, 16.9 GB of host RAM, running Windows 11.

- **Llama-3.1-8B-Instruct in NF4 at 119.6 tok/s, 3.32 GB peak, 100% SM occupancy.**
- **Qwen2.5-3B with an un-quantized bf16 base at 143 tok/s in 2.15 GB**, a configuration that raises CUDA out of memory when the same model is trained resident on the same card.

Both are configurations whose weights alone exceed the card. Measured overhead against resident training is **1.43x, at 0.5B**, the only size on that machine that admits a valid resident baseline at all.

The paper is deliberate about what that does not beat. Layer streaming on a small card is well established for inference, and AirLLM's own documentation says layer sharding is not compatible with gradient propagation. The published fine-tuning result for this hardware class is **1.3B**, reached by LSP-Offload ([arXiv:2406.10181](https://arxiv.org/abs/2406.10181)) by compressing the optimisation into a learned sparse subspace rather than by streaming the base. The systems that do stream weights during training are evaluated on an H200 with 1.5 TB of host memory, an RTX 4090 with 256 GB, or a cluster. The unserved combination, and the one the paper addresses, is streamed training on a small card.

## What version 2 adds

The paper roughly doubled, from about 9,000 words to about 19,800, and every addition comes from the same source: three borrowed days on an 8x H100 box, which was the first hardware other than the original laptop this work had ever run on.

- **Replication on hardware nothing like the original.** 119.6 tok/s on the RTX 3050 against a median of 113.00 on an H100, at the same 3.32 GB peak. The server card is if anything slightly slower. Version 2 offered an explanation for that and [version 3 retracts it](#what-version-3-adds); the measurement itself is unaffected.
- **A silent wrong-gradient defect, found and repaired.** On NF4 above roughly 165 MB per decoder layer the forward stayed bit-exact and the loss curve looked healthy while the gradients were wrong. The cause is named in the upstream library and reported there; the repair is gated against controls on real 32B and 72B.
- **Bit-exactness at real model sizes** instead of three-layer toys: forward from 0.5B to 72B, backward at 8B and 14B.
- **Trained-model quality, measured for the first time**, and indistinguishable from a resident run.
- **A comparison against DeepSpeed**, including the result that does not flatter the method: eight cards of ZeRO-3 are slower than one card training resident.
- **The limitations section rewritten**: of v1's ten items, one is closed and four more are narrowed, and seven new ones are added.

The last line is the one worth pausing on. A revision that only closed limitations would be a marketing document. This one closed one, narrowed four and opened seven, because measuring at a real size is how you find out what you did not know you were assuming.

## What version 3 adds

**Version 3 is current, published 13 August 2026.** The title and the claim are unchanged, still 8B on 4 GB, and no measured number changed. It exists to retract one explanation version 2 gave.

Version 2 read the H100 replication, a server card coming back no faster than the laptop, as evidence that layer streaming is bound by host-to-device transfer rather than by the GPU. It was an inference, and it had never been measured. On 11 August 2026 it was measured on the original laptop and is false at the published configuration: four ablation arms interleaved in one process at a pinned clock show that removing all host-to-device traffic, 6.864 GB per step, buys **1.44%**, removing the NF4 dequantisation buys **9.80%**, and removing both leaves **88.7%** of the step standing. The compute stream is blocked on a copy for **8.4 ms of a 4190 ms step**, and the step runs at **71.3%** of that card's same-session, shape-matched GEMM ceiling. The claim is true below roughly **128 tokens per step**, where the fixed transfer volume dominates, and the published configuration is not there.

What survives is the measurement itself, and it is untouched: a card with roughly two orders of magnitude more compute came back no faster than the laptop. The constraint is common to both machines and is not the compute the datacenter card adds. Beyond that we no longer offer an explanation for why: the one we offered was measured and refuted, and a second guess would be the same mistake in a new sentence. The H100's own bottleneck was never instrumented and no claim is made about it.

Two things about how it was published are worth copying rather than admiring. The retraction is a new version of the paper rather than an edit to the old one, because a claim that reached readers cannot be unpublished by changing a file. And every occurrence in the measurement records is annotated in place rather than deleted: in a folder whose premise is publishing the record as written, a silent deletion costs more credibility than the error does. The record is [`probe-v0.73.0-what-bounds-streaming.md`](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks).

## The result it defends hardest is not the throughput

In a streamed trainer the natural failure is silent. If the autograd graph is severed at the base weights, the upper layers still train, the loss still descends, and the run looks healthy. A throughput number taken before correctness is established measures nothing.

So the central check is **bit-exactness against a resident reference of the same numerics**: resident NF4 for a streamed NF4 run, never resident bf16, because quantisation error is wide enough to hide a real defect inside it. Against a matched reference the expected answer is 0.0, so anything else is a bug by construction.

That discipline paid for itself. It caught a PEFT dispatch path that selected a different LoRA implementation on a `meta`-device skeleton and produced a **0.94 maximum logit divergence with byte-identical weights and byte-identical adapters**: no exception, no warning, and a loss curve that looked entirely healthy. Nothing short of bit-exactness would have surfaced it.

The protocol itself, on SmolLM2-135M in bf16 with LoRA r=16 on `q_proj` and `v_proj`:

| Check | Threshold | Measured |
| --- | --- | --- |
| Streamed vs resident logits, max abs diff | < 1e-3 | 0.0, bit-exact |
| LoRA gradient at layer 0 | non-zero | 9.50e-01, 30 of 30 layers non-zero |
| 100-step loss curve vs resident | within noise | max relative difference 0.0 |
| Same seed twice | identical | 0.0 |
| With pinned-host boundary offload | < 2% relative | 4.83e-3 |
| Two buffers vs three | identical | 0.0 |

Bit-exactness was then re-verified across **nine `model_type` families in both bf16 and NF4**, 14 of 14 comparisons at a maximum absolute logit difference of 0.000e+00. Two rows carry more weight than the others. `phi3` fuses Q, K and V into a single `qkv_proj`, so the projection names a Llama-shaped implementation would look for do not exist at all, and it is bit-exact anyway, which is the strongest evidence that layer detection walks the real module tree rather than a naming assumption. And `gemma3` is deliberately refused while `gemma3_text` is accepted, with the accept and the refuse asserted together so the refusal cannot decay into a spelling accident.

The protocol runs on CPU and is part of the project's test suite rather than a one-off experiment, so a regression fails CI instead of reaching a user.

## Three findings that have nothing to do with streaming

These are the parts most likely to be useful even if you never enable layer streaming.

1. **The cross-entropy logits term costs 14 bytes per element, not 6.** A first-principles budget counts the bf16 logits plus an fp32 upcast. The measured figure is 14, because the loss holds the bf16 logits, the fp32 upcast, an fp32 log-softmax and an fp32 gradient live at the same time. That is a 2.33x under-prediction on a term that dominates: at batch 8 the logits tensor was over a hundred times the size of the entire layer buffer pool. Anyone budgeting VRAM for a large-vocabulary model from first principles will make the same mistake.
2. **Windows and WDDM do not raise out of memory, they spill.** One row of the fitting grid allocated **9.27 GB on a 4.29 GB card and completed without an exception**. The methodological consequence is blunt: on this platform, "it did not crash" is not evidence that a configuration fits. It also cost a discarded baseline, a resident run whose reported peak turned out to be the driver paging into host memory.
3. **Gradient accumulation is per-token I/O-neutral.** The received wisdom, the paper's own earlier draft included, is that accumulation multiplies I/O linearly because every micro-batch re-reads the model. True per optimizer step, and misleading per token, which is the unit that sets wall-clock time: layer reads per 1000 tokens held constant at 175.78 across accumulation 1, 2 and 4. The real cost is opportunity cost, measured at **2.52x** at an equal effective batch of 4, which is why the tool prints "raise batch size until the pre-flight refuses, then accumulate" rather than the standard low-VRAM advice of keeping batch at 1.

A fourth, smaller one, aimed at anyone quoting a fraction of peak on a consumer GPU: a ceiling is only comparable to a throughput measured in the same session. Repeating one GEMM six times inside a single session was stable to under 1%, while the same card varied by about 13% between sessions at the same reported clock. Any fraction-of-ceiling figure has to state the SM clock it was taken at.

## What it does not claim

The limitations section is long on purpose, and it is the reason to trust the rest.

- **8B is the largest size measured.** No 14B or larger claim is supported by any number in the paper.
- **The 3B bf16 figure is a lower bound.** That machine could not page-lock a 5.55 GB store, so the run fell back to a pageable one, which makes the host-to-device copy synchronous. The occupancy drop from 96.8% to 79.3% is that cost, measured rather than estimated.
- **Windows and WDDM throughout.** The numbers are systematically pessimistic against Linux, and there is no Linux measurement.
- **One card, and architecture coverage verified at small scale.** The nine-family gate used tiny from-config checkpoints rather than downloaded ones, deliberately, because the risk being tested is a naming property and not a size property. The throughput results are Qwen2.5 and Llama only.
- **Bit-exactness is verified at 135M, not at 8B.** At 8B it is impossible on that machine by construction: it needs a resident reference, which cannot exist for a model that does not fit. The paper names this as the most useful missing experiment in it. That experiment has since been run on borrowed hardware, and the section below says what it returned.
- **n = 1.** Every throughput row is a single run of 50 measured steps after 10 warm-up, on a working laptop that was not otherwise idle, and no variance is reported. The one exception is the accumulation comparison, repeated in an interleaved order precisely because a monotonic clock drift would otherwise have manufactured the result.
- **The RAM-versus-disk performance gap is unmeasured and no figure is claimed for it.** Correctness of the disk tier is established; relative speed is not.

## The experiment it named as missing is now in the paper

The limitation above is the one worth acting on, and in August 2026 a borrowed **8x H100** box made it possible. It was open in v1 and it is closed in v2, which is the largest single reason the revision exists. Those cards can hold a resident 8B, 14B, 32B and even 72B, so the comparison the paper could not make on a 4 GB laptop was finally made against real checkpoints instead of 3-layer fixtures. [The full record is its own page](/docs/external-validation); three things from it bear directly on the paper.

**No measured number from v1 changes, and nothing in it is invalidated.** Its headline configuration sits at 105 MB per decoder layer, comfortably below the boundary the exercise found, and its gradients survive a 50-backward soak against a resident NF4 reference at exactly `0.0`. Its throughput claim reproduces on completely different hardware, a different operating system and a much newer software stack: 119.6 tok/s in 3.32 GB there, against a median of 113.00 tok/s in the same 3.32 GB peak on an H100.

**The exactness claim is strengthened, and the two halves are strengthened by different amounts.** The forward is exact against matched resident references at 8B, 14B, 32B and 72B. The backward is exact at 8B and 14B, which is at and below the paper's own scope, and above that it was **wrong** until it was repaired. So "verified at 72B" is a forward statement and only a forward statement. The paper asserts nothing at 72B, so nothing in it depends on the distinction, but any future revision that reaches past 14B has to carry it explicitly rather than saying "bit-exact" and leaving a reader to decide which half was meant. Two expert readers already read it the other way.

**One thing that stays open across every version so far.** The repair changed the code path the headline was measured on. At real training shapes the arithmetic is unchanged, and the measured cost at 32B is 4.8%, but nobody has re-run the 8B laptop configuration on the repaired code, and a server card cannot stand in for a 4 GB laptop, which the H100 replication showed by coming back no faster rather than faster. **Treat 119.6 tok/s as a pre-repair figure until someone re-runs it on that card.** It is one of the seven limitations v2 adds rather than something v2 quietly resolved.

## The records behind it

Every number comes from measurement logs published verbatim in [the benchmarks directory](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks). They are the working gate records kept while each item was built, not a summary assembled afterwards, so they carry the failures, the assumptions that turned out wrong and the numbers that were measured and then discarded, in the order those things happened. Read a file from its top rather than lifting a passage out of the middle: a passage may be one the same page later corrects.

## Reproducing the headline row

The implementation shipped in Soup v0.72.3 under Apache-2.0. Two keys below are load-bearing, and omitting them is a silent divergence rather than an error: `gradient_accumulation_steps` (the shipped default is 4, and at batch 1 that measures roughly 2.5x lower throughput) and, for the un-quantized run, `quantization` (the shipped default is `4bit`).

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft
data:
  train: data.jsonl
  max_length: 512
training:
  stream_layers: true
  stream_source: ram
  stream_buffers: 2
  quantization: 4bit
  batch_size: 1
  gradient_accumulation_steps: 1    # load-bearing: the shipped default is 4
  optimizer: paged_adamw_8bit
  lora:
    r: 16
    target_modules: [q_proj, v_proj]
```

Omitting the `lora` block is not equivalent either: it defaults to r=64 with automatic target selection rather than the r=16 on `q_proj` and `v_proj` that produced these numbers. The run also needs free host RAM of at least the store size divided by 0.7, about 5.1 GB for the 8B NF4 store, and the pre-flight refuses below that rather than thrashing.

## Cite it

```bibtex
@misc{makazhan2026exact,
  title        = {Exact Layer Streaming: LoRA Fine-Tuning of an 8B Model on a 4 GB Laptop GPU},
  author       = {Makazhan, Alpamys},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v3},
  doi          = {10.5281/zenodo.21918325},
  url          = {https://doi.org/10.5281/zenodo.21918325}
}
```

## See also

- [Layer streaming](/docs/layer-streaming) — the mechanism as it ships today, the measured numbers, and the full refusal table.
- [Scaling a streaming run](/docs/streaming-scaling) — architectures, batch versus gradient accumulation, the VRAM pre-flight, resume and the disk tier.
- [Preference losses over streaming](/docs/streaming-preference) — DPO, ORPO, SimPO and KTO against a streamed base, which came after v1 was written and are still outside what the paper measures.
- [Validation on hardware we do not own](/docs/external-validation) — the resident reference at 8B, 14B, 32B and 72B in full, which v1 named as its most useful missing experiment and v2 carries.

[PreviousStreaming: Align](/docs/streaming-preference)[NextExternal validation](/docs/external-validation)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="051-external-validation"></a>

# 51. Validation on hardware we do not own

*Source: <https://trysoup.dev/docs/external-validation>*

Every number Soup has published about layer streaming came from one machine: a 4 GB RTX 3050 Laptop running Windows. That is the machine the feature exists for, and it is also the machine that cannot check the feature's central claim.

The claim is that a streamed run computes the same thing a normal run computes. Checking it needs a **resident reference**: the same checkpoint, same quantisation, loaded the ordinary way, so the two can be compared tensor by tensor. On a 4 GB card that reference cannot exist for any model worth streaming. So the published checks ran on 3-layer models built from a config, with a hidden size of 32 and an NF4 layer of **0.01 MB**. [The paper](/docs/paper) says so in its own limitations, and names the missing experiment as the most useful one absent from it.

In August 2026 someone lent us an **8x H100 80 GB** box for three days. This page is what the experiment returned, including the defect it found.

The full record is published as written, in the order things happened, at [`benchmarks/gate-h100-validation.md`](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks). It is a working record, not a report assembled afterwards, so it contains rejected hypotheses, withdrawn findings and measurement errors that later controls caught. Read it from the top.

## The box, and why the stack matters

- **8x H100 80 GB HBM3**, 503 GB host RAM, 32 cores, Ubuntu 24.04, driver 590.48.01
- **PCIe between all pairs, no NVLink.** This matters for the DeepSpeed comparison below and it favours nobody by accident: all-gather traffic is exactly what NVLink exists for.
- **Page-locked ceiling is 62.96 GB**, not 503 GB. Pinned memory is a separate budget from RAM.
- **No NVMe.** The only device is a virtual disk the kernel reports as rotational, which is why the RAM-versus-disk question stays unanswered.

The software stack is a different one end to end: torch 2.13, bitsandbytes 0.50.0, trl 0.26.2, peft 0.20.0. Of the five components that matter, **only `transformers` matches the laptop**. That is a feature of the experiment rather than a nuisance: a result that survives a stack change is a result about the method, not about one pinned set of wheels.

## Bit-exactness is two claims, and they are not the same claim

This is the most important sentence on the page, and it is the one two expert readers got wrong before it was written down.

> Every exactness result below is **two independent measurements**: the **forward** (logits, compared with `torch.equal`) and the **backward** (every LoRA gradient tensor). Above roughly **165 MB per NF4 layer they disagreed.** "Bit-exact at 72B" is a forward statement and only a forward statement.

Each row was compared against a resident reference of **matching numerics**: resident NF4 for a streamed NF4 run, never resident bf16, because quantisation error is wide enough to hide a real defect inside it.

| Model | Quant | MB/layer | Forward | Backward, pinned | Backward, unpinned | After the repair |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen2.5-0.5B | NF4 | 7 | exact `0.0` | exact 96/96 | not tested | already exact |
| Llama-3.1-8B | NF4 | 105 | exact `0.0` | exact 128/128 | not tested | already exact |
| Llama-3.1-8B | bf16 | 480 | exact `0.0` | exact 128/128 | not tested | never affected |
| Qwen2.5-14B | NF4 | 132 | exact `0.0` | exact 192/192 | not tested | already exact |
| Qwen2.5-14B | bf16 | 570 | exact `0.0` | exact 192/192 | not tested | never affected |
| **Qwen2.5-32B** | **NF4** | **234** | exact `0.0` | **WRONG 8/256** | exact 256/256 | **exact 256/256** |
| **Qwen2.5-72B** | **NF4** | **432** | exact `0.0` | **WRONG 8/320** | exact 320/320 | **exact 320/320** |

The 8B NF4 and 14B NF4 rows each survived a **50-consecutive-backward soak** with a worst absolute difference of `0.0`. A cell that was not measured says "not tested" rather than being left blank, because a blank reads as a pass.

## The defect this found

**In NF4, above roughly 165 MB per decoder layer, a streamed run produced silently wrong gradients.** Filed as issue #331.

It is worth being precise about how silent. The forward stayed bit-exact on every run. The loss matched a resident reference **to every digit**. The run exited 0, printed no warning, and the loss curve fell normally. Only a direct gradient comparison could see that 62 of 64 layers were wrong.

- **Threshold**, bracketed by sweeping one shape parameter: exact at **163.8 MB per layer**, broken at **171.5**. Monotone on both sides over seven points, with no exceptions. It is a bracket, not a number.
- **Which models.** 8B sits at 105 MB per layer and 14B at 132, both below with margin. 32B (234) and 72B (432) are above. **Nothing Soup has ever published is above the boundary.**
- **Why NF4 only.** bf16 is exact at 935 MB per layer, moving **3.9 times more bytes** than the failing NF4 run, so it is not about transfer size.
- **The cause is aliasing, not a race.** A full `cuda.synchronize()` does not fix it. Giving each pooled tensor a private copy fixes it completely. `bitsandbytes.MatMul4Bit` stashes the packed weight and its quantisation state on the autograd context as ordinary Python attributes instead of going through `save_for_backward`, so gradient checkpointing cannot see them: the reference is captured in the forward, aliases the streaming buffer, and is read in the backward after that slot has been refilled with a different layer. bf16 goes through a native op that does use `save_for_backward`, which is why it was never affected. The upstream half is filed as `bitsandbytes-foundation/bitsandbytes#2034`.
- **The obvious fix was rejected on measurement.** Cloning every pooled tensor is correct and costs only about 6% of throughput, but it takes peak VRAM from 4,220 MB to 19,720 MB on a real 32B, which is approximately the whole model. A repair that is O(model) instead of O(one layer) deletes the reason the feature exists.
- **The shipped repair keeps streamed NF4 weights out of that code path entirely**, so the saved reference goes through the ordinary mechanism that checkpointing knows how to recompute. Gated on two real models against a control that reproduced the defect in the same process: **32B at 256/256 and 72B at 320/320, five repetitions each.** It costs **+2.9% peak VRAM and 4.8% throughput at 32B**, and **+2.6% and 3.7% at 72B**.

### Are you affected?

**Almost certainly not, and here is the exact test.** You need all three of: `quantization: 4bit`, layer streaming, and a decoder layer above roughly 165 MB. On the 4 GB hardware this feature targets, that layer size is out of reach: a 32B NF4 store is 14.99 GB of pinned host RAM and a 72B store is 33.74 GB. If you have streamed an 8B or smaller, you are below the boundary with margin and there is nothing to re-run.

If you did stream a 32B or larger in NF4, the adapter is not trustworthy and re-running is the only fix, exactly as with [the v0.72.1 adapter-key defect](/docs/layer-streaming#read-this-first-if-you-already-trained-with-streaming). The two have the same shape: an exit-0 run that looked healthy the whole time.

**The repair shipped in v0.73.0.** Every release from v0.72.0 to v0.72.4 carries the defect at those sizes, so upgrade before streaming anything that large in NF4. The library behaviour it works around is upstream and unchanged, filed as `bitsandbytes-foundation/bitsandbytes#2034`.

## Peak VRAM is flat in model size

This is the feature's whole claim, and it is the first time it has been measured across a real size range on one card. Five runs per row, streamed, NF4, through the shipped CLI.

| Model | Throughput, median of 5 | Spread | Peak VRAM | Pinned host store |
| --- | --- | --- | --- | --- |
| Llama-3.1-8B | 113.00 tok/s | 5.0% | 3,397 MB | 3.35 GB |
| Qwen2.5-14B | 118.60 tok/s | 4.1% | 4,475 MB | 6.35 GB |
| Qwen2.5-32B | 76.80 tok/s | 3.9% | 4,845 MB | 14.99 GB |

**The model grows fourfold and peak VRAM moves from 3,397 to 4,845 MB.** Qwen2.5-72B extends the shape at n=2: **37.9 tok/s in 7,411 MB**, against a 33.74 GB pinned store.

Two honest readings of that table. 14B being faster than 8B is the opposite of the naive expectation, it was not investigated, and **no mechanism is asserted for it**; the two rows are different architectures with different vocabularies, so the clean comparison is the two Qwen2.5 rows, which do fall. And every row here was taken **before** the #331 repair, which costs a few percent of throughput at the sizes it applies to.

The 72B row deserves its caveat spelled out rather than buried: under the configuration that shipped, **72B's gradients were wrong**, so that line describes a memory and throughput result, not a valid training result. After the repair the gradients are exact. And the 33.74 GB host store is the real gate on reproducing it: this is not a claim about a laptop.

## The laptop number reproduces on completely different hardware

The published headline is Llama-3.1-8B NF4 at **119.6 tok/s in a 3.32 GB peak**, on an RTX 3050 Laptop under Windows. The same configuration on an H100 gives a **median of 113.00 tok/s in a 3.32 GB peak**.

An H100 is not slightly faster here. It is slightly **slower**, and mean GPU utilisation on those runs was **54.1%**.

The record originally read that as proof the method is bound by host-to-device transfer rather than by the GPU. **That reading was retracted on 11 August 2026, by measurement.** Four ablation arms interleaved in one process on the original laptop at a pinned clock: removing all host-to-device traffic, **6.864 GB per step**, buys **1.44%**; removing the NF4 dequantisation buys **9.80%**; removing both leaves **88.7%** of the step standing. The compute stream is blocked on a copy for **8.4 ms of a 4190 ms step**, and the step runs at **71.3%** of that card's same-session, shape-matched GEMM ceiling. The claim is true below roughly **128 tokens per step**, where the fixed transfer volume dominates, and the published configuration is not there.

What survives is the measurement itself, and it is untouched: a card with roughly two orders of magnitude more compute came back no faster than the laptop. The constraint is common to both machines and is not the compute the datacenter card adds. Beyond that we no longer offer an explanation for why: the one we offered was measured and refuted, and a second guess would be the same mistake in a new sentence. The H100's own bottleneck was never instrumented and no claim is made about it. Every occurrence upstream is annotated in place rather than deleted, including in the record that first made the claim.

What the retraction does not touch is what a streamed run needs from its host: turning pinning off cost **6.56x throughput** at 32B NF4, which is why Soup refuses rather than silently falling back when it cannot pin.

## Against DeepSpeed ZeRO-3

The first comparison against another tool, run through Soup's own `--deepspeed` entry point so it is one tool against itself. One H100, Llama-3.1-8B, same data, same LoRA, 256 optimizer steps.

| Approach | Base dtype | Throughput | Peak VRAM |
| --- | --- | --- | --- |
| Layer streaming | NF4 | 121.46 tok/s | 3,399 MB |
| Layer streaming | bf16 | 63.52 tok/s | 3,935 MB |
| DeepSpeed ZeRO-3, CPU parameter offload | bf16 | 21.65 tok/s | 38,135 MB |

At matched numerics, bf16 against bf16, layer streaming is **2.93x the throughput in 9.7x less peak VRAM**. ZeRO-3 was then given a second, memory-tuned attempt: tightening every knob bought 5.6% less VRAM for 12% less throughput.

**Do not read that as "streaming beats DeepSpeed."** The record is emphatic about this and so is this page. ZeRO-3 shards across ranks, and with one GPU there is no partner to shard to, so it is being used outside the regime it was built for. That regime happens to be layer streaming's home ground, which is the point, but the honest claim is the narrow one: **not faster than DeepSpeed, built for a different situation, namely one card that is too small.**

The eight-card picture makes the same point from the other side, on the same model and data:

| Approach | GPUs | Throughput | Peak VRAM |
| --- | --- | --- | --- |
| Resident bf16 | 1 | 2,645.4 tok/s | 30.0 GB |
| ZeRO-3, no offload | 8 | 1,831.7 tok/s | 34.0 GB per card |
| ZeRO-3 + CPU offload | 8 | 1,752.2 tok/s | 38.0 GB per card |
| Layer streaming bf16 | 1 | 1,077.1 tok/s | **2.9 GB** |

**Eight cards of ZeRO-3 are slower than one card training resident**, for a model that fits on one card. Against streaming on a single GPU they buy 1.70x, for 34 GB on each of eight cards against 2.9 GB on one. If the model fits, the right answer is the top row and every clever technique here is a loss. This is a PCIe box with no NVLink, and ZeRO-3 would improve on an NVLink node while the streaming row would not.

## Does streaming change the model you get?

Bit-exactness answers this for one step. Convergence over a real fine-tune is a separate question, and it had never been measured.

Protocol: Llama-3.1-8B, **NF4 in both arms**, five paired runs where streamed run \*i\* and resident run \*i\* see byte-identical training data from disjoint subsets, scored by Soup's own `soup ship` against a fixed 300-row held-out set that no run trained on.

|  | Mean score | Within-arm spread |
| --- | --- | --- |
| Resident NF4 | 0.8773 | 0.0333 |
| Streamed NF4 | 0.8720 | 0.0200 |

The mean paired difference is **+0.0053**, which is **1.6 items out of 300**, against a within-arm spread several times larger. The general-capability leg points against the convenient direction: **3 of 5 resident runs came back DON'T SHIP against 1 of 5 streamed**, and the single worst regression in the matrix belongs to a resident run.

**Read this as "no difference is detectable at this resolution", not as "there is no difference."** The experiment resolves roughly one percentage point on a 300-item set. It does not license a claim of quality-neutrality to arbitrary precision.

## Preference losses, on a real 8B

[The v0.72.4 claim](/docs/streaming-preference) that DPO's reference model costs no extra weights was measured on a 365M synthetic fixture. It now holds on a real 8B through the shipped CLI, streamed, timed for the first time:

| Streamed task | Reference model | Peak VRAM | Samples/s, median of 3 |
| --- | --- | --- | --- |
| `sft` | none | 3,689 MB | 6.082 |
| `orpo` | none, genuinely reference-free | 3,719 MB | 5.973 |
| `simpo` | none, genuinely reference-free | 3,719 MB | 5.946 |
| `dpo` | same base, adapters disabled | 3,733 MB | 4.665 |
| `kto` | same base plus a separate KL forward | 3,669 MB | 3.595 |

**Peak VRAM is flat across all five, within 64 MB or 1.7%.** DPO costs **44 MB more than SFT**, against roughly 5.6 GB for a second resident copy of an NF4 8B. That is the claim, measured at a size where a second copy would be impossible to miss.

Two cautions. These are **samples per second, not tokens per second**, and they come from 64-row single-epoch runs where setup is a large share of an 11 to 14 second step, so **treat the ratios as directional**. And `kto` runs a different dataset, so only its VRAM compares directly.

The same session also measured the streaming trade through the shipped CLI on a real model for the first time: streaming holds an 8B in **3,681 MB against the resident path's 12,087 MB, 3.28x less, for 1.13x the wall time**.

## The other machine nobody here owns, and it is free

An 8x H100 box is external hardware that almost nobody reading this can repeat on. A free-tier Colab **Tesla T4** is external hardware anyone can repeat on in about twenty minutes, and it is the other end of the same question. A streamed 8B NF4 run now completes there, inside a **4.00 GB** process cap, at a **measured peak of 2.91 GB**.

It is a far weaker result than anything else on this page and is filed that way upstream: **not a gate**. One run, one seed, no repeats, on a session that cannot be returned to, with no captured correctness comparison and therefore **no gradient exactness on Turing**. **No throughput is quoted**, because a card held under an artificial cap is not a benchmark. What it establishes is that the path executes end to end on a pre-Ampere card at 8B, which had never been run before.

[Run it yourself, with the full frame](/docs/layer-streaming#run-it-yourself-on-a-free-colab-t4). The precision fix it needs shipped in [v0.73.1](/docs/free-gpu-tier), though the notebook itself still installs Soup from git.

## What this does not say

The record's own limitations section is long, and it is the reason to trust the rest.

- **The RAM-versus-disk gap is still unmeasured.** There was no NVMe on the box, and a number from a virtual disk published under a heading people would read as "NVMe" is worse than no number.
- **Why the defect is NF4-only, and why its boundary is so sharp, is not explained.** Seven hypotheses were tested and rejected. None replaced them.
- **The repair is gated at two sizes**, 32B and 72B. No size between them was tested, and each gate is one sequence length and one buffer count.
- **The quality result resolves about one percentage point**, on 300 items, with the adapter initialisation seed uncontrolled.
- **Every number is one machine, one session.** No claim here is a multi-machine result.
- **The published 119.6 tok/s laptop figure was measured before the #331 repair.** At real training shapes bitsandbytes already took the same code path the repair forces, so the arithmetic is unchanged, and the measured cost at 32B is 4.8%. But nobody has re-run the 8B laptop configuration on the repaired code, and an 80 GB server card cannot stand in for a 4 GB laptop, which the H100 replication showed by coming back no faster rather than faster. **Treat it as a pre-repair figure until someone re-runs it.**

## The result that is not a number

Twelve defects surfaced in three days. Seven were repaired in the same window, five were filed with reproducers. The record's own summary of why is worth carrying:

> Every one of them was found by running something that had never been run, not by reading code.

Four of the twelve were features the project ships and documents that had **never executed once** on any machine. Two produced successful, exit-0 runs the entire time: an adapter that reloaded as all zeros, and a `data.max_length` above 1024 that was silently ignored on every supervised run. A green test suite measured neither the features that had never run nor the paths that cannot run on one card.

That is the argument for borrowing hardware, and it is a better argument than any throughput number in the table above.

## See also

- [Layer streaming](/docs/layer-streaming) — the mechanism as it ships, the measured numbers and the full refusal table.
- [The paper](/docs/paper) — the preprint, the correctness protocol and the limitations this page answers.
- [Scaling a streaming run](/docs/streaming-scaling) — architectures, batches, the VRAM pre-flight and the disk tier.
- [Preference losses over streaming](/docs/streaming-preference) — DPO, ORPO, SimPO and KTO against a streamed base.

[PreviousThe paper](/docs/paper)[NextData Formats](/docs/data-formats)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="052-data-formats"></a>

# 52. Data Formats

*Source: <https://trysoup.dev/docs/data-formats>*

Soup supports 19 data formats as of v0.71.32 (raft added for Retrieval-Augmented Fine-Tuning in v0.62, asr added for Whisper fine-tuning in v0.71.32). Files can be JSONL, JSON, CSV, Parquet, or TXT — local paths or remote URIs (`s3` / `gs` / `gcs` / `az` / `abfs` / `abfss` / `oci`). Format is auto-detected from the first row.

## Alpaca

```json
{"instruction": "Explain gravity", "input": "", "output": "Gravity is..."}
```

## ShareGPT

```json
{"conversations": [{"from": "human", "value": "Hi"}, {"from": "gpt", "value": "Hello!"}]}
```

## ChatML

```json
{"messages": [{"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello!"}]}
```

## DPO / ORPO / SimPO / IPO (preference pairs)

```json
{"prompt": "Explain gravity", "chosen": "Gravity is a force...", "rejected": "I don't know"}
```

## KTO (unpaired preferences)

```json
{"prompt": "Explain gravity", "completion": "Gravity is a force...", "label": true}
```

## LLaVA (vision)

```json
{"image": "photo.jpg", "conversations": [{"from": "human", "value": "<image>\nDescribe this."}, {"from": "gpt", "value": "A cat."}]}
```

## ShareGPT4V (vision)

```json
{"image": "chart.png", "conversations": [{"from": "human", "value": "<image>\nExplain this chart."}, {"from": "gpt", "value": "Revenue growth."}]}
```

## Plaintext (pre-training)

```json
{"text": "Raw text document for continued pre-training..."}
```

Or use `.txt` files directly (one document per line).

## Embedding

```json
{"anchor": "What is Python?", "positive": "Python is a programming language."}
{"anchor": "What is Python?", "positive": "A programming language.", "negative": "A type of snake."}
```

## Audio

```json
{"audio": "recording.wav", "messages": [{"role": "user", "content": "Transcribe."}, {"role": "assistant", "content": "Hello world."}]}
```

## ASR (new in v0.71.32)

```json
{"audio": "clip.wav", "text": "the transcript"}
```

For [Whisper fine-tuning](/docs/asr-fine-tuning) (`task: asr`): the clip becomes 16 kHz log-mel input features, the text becomes the decoder labels. Paths resolve against `data.audio_dir` (containment-checked).

## Tool-calling (new in v0.25.0)

```json
{"messages": [{"role": "user", "content": "Weather in Tokyo?"}], "tools": [{"type": "function", "function": {"name": "get_weather", "parameters": {"type": "object", "properties": {"city": {"type": "string"}}}}}], "tool_calls": [{"function": {"name": "get_weather", "arguments": "{\"city\": \"Tokyo\"}"}}]}
```

Tool definitions are embedded in the system message during normalization and `tool_calls` are emitted as assistant turns. See the [Tool-calling guide](/docs/tool-calling) for the full pipeline.

## The seven the page above does not show a row for

Nineteen formats are declared, and the twelve above are the ones you will meet first. These are the rest, one row each.

```json
// prm — process reward, stepwise supervision
{"prompt": "Solve 2+2", "completions": ["First, add", "Result is 4"], "labels": [true, true]}

// pre_tokenized — skip the tokenize stage entirely
{"input_ids": [1, 2, 3], "labels": [-100, 2, 3], "attention_mask": [1, 1, 1]}

// input_output — template-free, per-segment loss control
{"segments": [{"text": "Q: hi", "label": false}, {"text": "A: hello", "label": true}]}

// video — resolved under data.video_dir
{"video": "clip.mp4", "messages": [{"role": "user", "content": "Describe this clip."}]}

// multimodal — typed content parts, text / image / audio / video in one message
{"messages": [{"role": "user", "content": [{"type": "text", "text": "What's in this?"}, {"type": "image", "url": "x.png"}]}]}

// raft — Retrieval-Augmented Fine-Tuning, v0.62
{"question": "...", "oracle": "...", "distractors": ["...", "..."], "answer": "..."}
```

`pre_tokenized` pairs with `data.tokenized_path` after `soup data preprocess`. And `auto`, the default, is the nineteenth: it sniffs the format from the first rows so you can leave `data.format` out entirely.

All data normalizes internally to `{"messages": [...]}` structure (+ `"image"` for vision, `"audio"` for audio, + `"tools"` for tool-calling).

[PreviousExternal validation](/docs/external-validation)[NextData Tools](/docs/data-tools)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="053-data-tools"></a>

# 53. Data Tools

*Source: <https://trysoup.dev/docs/data-tools>*

Soup includes powerful CLI tools for preparing training datasets. Full augmentation guide: [Data augmentation](/docs/data-augment).

## Inspect

```bash
soup data inspect ./data/train.jsonl
```

Shows dataset statistics: sample count, token distribution, field analysis. For vision datasets, automatically shows image statistics (count, formats, missing files).

## Validate

```bash
soup data validate ./data/train.jsonl
soup data validate ./data/train.jsonl --format alpaca
soup data validate ./data/train.jsonl --min-valid-fraction 0.9
```

Checks for missing fields, encoding issues, and format compliance. Auto-detects format when `--format` is not specified.

**It agrees with the loader now, and it did not before v0.75.0.** The validator used to judge a row by which top-level keys were present, while `load_dataset` runs the real converters and drops any row that comes back empty. Those are two different notions of valid, and they disagreed in two directions: the six formats with no key signature at all — `prm`, `pre_tokenized`, `input_output`, `video`, `multimodal` and `raft` — **skipped validation entirely and reported every row valid regardless of content**, and for the formats that were checked, key presence passed rows a converter drops on a value, such as a null field or a non-dict message. A file could validate clean and then fail in the middle of a training run.

The valid-row count is now computed by running the real conversion path per row, so the agreement is structural rather than a second, weaker check that drifts. When a row is dropped, the converter's own reason is surfaced for the first few offenders, `row 3: chatml message must be a dict`, so the report says which rows and why rather than only a count. On upstream's own datasets this shifted **120 of 360 file-by-format verdicts**, every one of them an over-count on a file that genuinely had zero valid rows in that format.

**The exit codes matter, because this is the first step of the PR gate `soup ci init` writes:**

| Exit | Meaning |
| --- | --- |
| `0` | At least one row is usable, and any `--min-valid-fraction` is met. A partially valid dataset still exits 0 when no minimum is given |
| `1` | An input error: a missing file, or a format that cannot be detected. **Also an unknown `--format`** |
| `2` | A non-empty dataset with **no usable rows**, or one below `--min-valid-fraction` |

`--min-valid-fraction` takes a float in `[0.0, 1.0]` and defaults to `0.0`, meaning no minimum. Two of those three behaviours are new in v0.75.0: before it, a file with **zero** usable rows exited 0, and `--format bogus` exited 0 while reporting "2/2 rows valid for bogus format", which quietly turned the CI gate into a pass for any file. An unknown format is an input error rather than a failed gate, deliberately, so a typo cannot be mistaken for a real rejection.

The accepted values for `--format` are `auto` plus the eighteen convertible formats: `alpaca`, `sharegpt`, `chatml`, `dpo`, `kto`, `llava`, `sharegpt4v`, `plaintext`, `embedding`, `audio`, `tool-calling`, `prm`, `pre_tokenized`, `input_output`, `video`, `multimodal`, `raft` and `asr`. The flag's own `--help` text lists only seven of them and is stale; this list is the allowlist the code checks against.

## Convert

```bash
soup data convert ./data/train.jsonl --to sharegpt --output converted.jsonl
```

Transform between alpaca, sharegpt, and chatml formats.

## Merge

```bash
soup data merge data1.jsonl data2.jsonl --output merged.jsonl --shuffle
```

Combine multiple datasets with optional shuffling.

## Deduplicate

```bash
# Requires: pip install "soup-cli[data]"
soup data dedup ./data/train.jsonl --threshold 0.8

# Semantic near-dup removal over embedding cosine (v0.71.36, needs [train]):
soup data dedup ./data/train.jsonl --semantic -o clean.jsonl
```

Remove near-duplicate samples using MinHash, or add `--semantic` to catch **reworded** duplicates MinHash's shingling scores as distinct. See [Data Moat II](/docs/data-moat-ii) for the semantic path, plus `soup data topics` (coverage map) and `soup data canary` (memorization probe).

## Extended Statistics

```bash
soup data stats ./data/train.jsonl
```

Length distribution with histograms, token counts, and language detection.

## Synthetic Data Generation

```bash
# Generate using OpenAI API
soup data generate --prompt "Create math word problems" --count 100 --format alpaca

# Use a different model
soup data generate --prompt "Medical Q&A pairs" --model gpt-4o --count 500

# Deduplicate against existing data
soup data generate --prompt "..." --count 200 --dedup-with existing.jsonl

# Use seed examples to guide style
soup data generate --prompt "..." --seed examples.jsonl --count 100

# Use a local server (soup serve, Ollama, etc.)
soup data generate --prompt "..." --provider server --api-base http://localhost:11434/v1
```

### Multi-Provider Support (v0.20.0+)

```bash
# Generate via local Ollama instance
soup data generate --prompt "..." --provider ollama --model llama3.1
soup data generate --prompt "..." --ollama-model llama3.1  # shorthand

# Generate via Anthropic Claude API (set ANTHROPIC_API_KEY env var)
soup data generate --prompt "..." --provider anthropic --model claude-3-haiku-20240307

# Generate via local vLLM server
soup data generate --prompt "..." --provider vllm --model meta-llama/Llama-3.1-8B-Instruct
```

### Domain Templates (v0.20.0+)

```bash
# Code instruction pairs (Python, JS, Go, Rust, Java)
soup data generate --prompt "..." --template code --language Python --task-type function

# Multi-turn conversations
soup data generate --prompt "..." --template conversation --turns 6 --topic "science"

# QA from context document
soup data generate --prompt "..." --template qa --context document.txt

# Preference data (DPO/KTO/ORPO)
soup data generate --prompt "..." --template preference --pref-task dpo

# Chain-of-thought reasoning (GRPO)
soup data generate --prompt "..." --template reasoning --domain math
```

### Quality Pipeline (v0.20.0+)

```bash
# Auto-validate after generation (remove malformed entries)
soup data generate --prompt "..." --validate

# Auto-filter by quality (coherence scoring)
soup data generate --prompt "..." --filter

# Auto-dedup (MinHash, requires: pip install "soup-cli[data]")
soup data generate --prompt "..." --dedup

# Full quality pipeline: validate + filter + dedup
soup data generate --prompt "..." --quality-pipeline
```

## Quality Filter

```bash
# Filter by coherence score
soup data filter ./data/train.jsonl --coherence 0.3

# Filter by perplexity + coherence
soup data filter ./data/train.jsonl --perplexity 500 --coherence 0.3

# Add scores without removing samples
soup data filter ./data/train.jsonl --score-only
```

Uses perplexity + coherence scoring to identify low-quality samples.

## Data Sampling (v0.23.0+)

```bash
# Random sample
soup data sample ./data/train.jsonl --strategy random -n 1000

# Diverse sample (TF-IDF clustering)
soup data sample ./data/train.jsonl --strategy diverse -n 500

# Hard examples (by length)
soup data sample ./data/train.jsonl --strategy hard -n 500
```

## Data Splitting (v0.23.0+)

```bash
# Split into train/val/test. --val and --test are integer PERCENTAGES,
# not fractions; the train remainder is implied, and --train is accepted
# for command parity rather than read.
soup data split ./data/train.jsonl --val 10 --test 10

# Absolute row counts instead of percentages, with a reproducible seed
soup data split ./data/train.jsonl --val 500 --test 500 --absolute --seed 42

# Stratified split. --stratify takes the field to stratify on, as a value.
soup data split ./data/train.jsonl --val 10 --stratify category

# Semantic stratification (v0.73.2): cluster by embedding, then split
soup data split ./data/train.jsonl --val 10 --stratify-semantic --num-clusters 8
```

## HuggingFace Dataset Hub (v0.24.0+)

```bash
# Search for datasets
soup data search "math reasoning"

# Preview remote dataset metadata
soup data preview tatsu-lab/alpaca

# Download to local JSONL
soup data download tatsu-lab/alpaca --output ./data/alpaca.jsonl --samples 1000
```

## Dataset Registry (v0.24.0+)

Register local datasets by name for use in `soup.yaml`:

```bash
# Register a dataset
soup data register my-chat-data --path ./data/chat.jsonl --format chatml

# List registered datasets
soup data registry

# Use in config: data.train: registry:my-chat-data
soup data unregister my-chat-data
```

[PreviousData Formats](/docs/data-formats)[NextData Augmentation](/docs/data-augment)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="054-data-augment"></a>

# 54. Data Augmentation

*Source: <https://trysoup.dev/docs/data-augment>*

`soup data augment` expands a JSONL dataset with LLM-driven rewrites. Added in v0.25.0.

## Usage

```bash
# Rephrase each example 3x
soup data augment \
  --input data.jsonl \
  --output augmented.jsonl \
  --strategy rephrase \
  --count 3

# Translate to other languages
soup data augment --input data.jsonl --strategy translate --lang ru,zh,es

# Rewrite in multiple styles
soup data augment --input data.jsonl --strategy style --styles formal,casual,technical
```

## Strategies

| Strategy | Purpose |
| --- | --- |
| `rephrase` | Preserve meaning, diversify wording |
| `translate` | Add examples in other languages for multilingual fine-tuning |
| `style` | Rewrite in formal / casual / technical / etc. tones |

## Providers

Augmentation uses the judge providers: `ollama`, `anthropic`, `vllm`. Select with `--provider`.

```bash
soup data augment \
  --input data.jsonl \
  --strategy rephrase \
  --count 2 \
  --provider ollama \
  --dedup
```

## Flags

| Flag | Meaning |
| --- | --- |
| `--strategy` | `rephrase` / `translate` / `style` |
| `--count` | Augmentation multiplier (default 2, max 10) |
| `--lang` | Target languages for `translate` |
| `--styles` | Style list for `style` |
| `--model` | Model id to ask the provider for |
| `--base-url` | Provider endpoint, for a self-hosted or proxied server |
| `--requests-per-minute` | Client-side rate limit |
| `--dedup` | Deduplicate augmented + original data |

## Safety

- Input/output paths are resolved and constrained to the current working directory.
- Output format must match the input format, enforced after generation.
- `--count` is capped at 10 to prevent accidental 1000× blow-ups.
- Requests honor `--requests-per-minute` inherited from `soup data generate`.

[PreviousData Tools](/docs/data-tools)[NextTrace → Preference](/docs/trace-to-preference)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="055-trace-to-preference"></a>

# 55. Trace-to-Preference

*Source: <https://trysoup.dev/docs/trace-to-preference>*

v0.26.0 turns traffic logs into DPO / KTO training data. Point `soup data from-traces` at LangChain, OpenAI, or Soup-serve logs. Soup extracts preference signals — thumbs, regenerations, user edits — and writes clean pairs.

## Ingest a log

```bash
soup data from-traces \
  --logs chat_logs.jsonl \
  --format langchain \
  --signal thumbs_up \
  --output prefs.jsonl
```

## Flags

| Flag | Meaning |
| --- | --- |
| `--logs` | JSONL trace file (or a directory for the `soup-serve` format) |
| `--format` | `langchain` · `openai` · `soup-serve` |
| `--signal` | `thumbs_up` · `regenerations` · `user_edit` |
| `--output` / `-o` | Destination JSONL (default `prefs.jsonl`) |
| `--judge` | Keep only pairs an LLM judge agrees with |
| `--judge-provider` | `openai` · `server` · `ollama` |
| `--judge-model` | Model id for the judge |
| `--judge-api-base` | Judge endpoint, validated against the SSRF guard |
| `--min-confidence` | Judge-confidence floor, default 0.7 |

## Signals

- `thumbs_up` — explicit positive feedback becomes the chosen response
- `regenerations` — if the user hit regenerate, the later response is preferred
- `user_edit` — if the user rewrote the response, the edit becomes chosen

## Review before training

```bash
soup data review prefs.jsonl --sample 10
```

Previews up to 100 random pairs side-by-side with their chosen / rejected labels. Use it as a sanity check before burning a GPU on junk data.

## Train on them

DPO or KTO — the output format of `from-traces` matches both:

```yaml
task: dpo
data:
  train: prefs.jsonl
  format: dpo
```

## Safety

- Logs never execute model code — parsers only read JSON.
- Traces may contain PII or secrets; Soup warns on ingest and leaves scrubbing to you before sharing pairs externally.
- Output JSONL can be validated with the same `soup data validate` pipeline as any other dataset.

## See also

- [Data formats](/docs/data-formats)
- [DPO training guide](/docs/dpo-training-guide)

[PreviousData Augmentation](/docs/data-augment)[NextData Pipeline Pro](/docs/data-pipeline-pro)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="056-data-pipeline-pro"></a>

# 56. Data Pipeline Pro (v0.42.0)

*Source: <https://trysoup.dev/docs/data-pipeline-pro>*

18 features across 6 parts. Axolotl + LLaMA-Factory data-layer parity.

## 5 new data formats

```yaml
data:
  train: ./data/train.jsonl
  format: prm            # PRM stepwise-supervised
  # | pre_tokenized      # LF tokenized_path / Axolotl empty
  # | input_output       # Axolotl template-free segments+labels
  # | video
  # | multimodal         # axolotl content-parts schema
```

## Remote URIs

7-entry allowlist for object stores. Bucket regex `^[a-zA-Z0-9][a-zA-Z0-9._\-]{0,62}$`. Userinfo / fragment / query rejected.

```yaml
data:
  train: s3://my-bucket/train.jsonl    # s3 | gs | gcs | az | abfs | abfss | oci
  streaming: true
  buffer_size: 10000
  shards: 16
```

Live fsspec loaders shipped in v0.53.8 (schema-only in v0.42.0).

## `data.prompt_strategy` — your own row transform

An Axolotl-style `module.path:function_name` spec. The import is resolved once at setup, so a bad path fails fast rather than mid-epoch, and the function is applied to **each row before template rendering**.

```yaml
data:
  train: ./data/train.jsonl
  prompt_strategy: my_pkg.strategies:to_chat
```

It runs code you name, so it is operator-controlled by design: only point it at a module you trust. (The schema description for this field still says "schema-only in v0.42.0"; the executed loader has applied it since v0.53.7.)

## Multi-dataset interleave

`data.interleave` selects the strategy, and it is validated at config load. It attaches to a **list-valued** `data.train` and is refused outright against a single path, so the sub-block never appears on its own:

```yaml
# A FRAGMENT, not a config: this block goes under the data: key, beside
# a list-valued data.train. On its own at the root it is refused as an
# unknown key, because only a root-level lora: block is remapped.
data:
  interleave:
    strategy: probs      # concat | under | over | probs
    probs: [0.7, 0.3]    # one entry per dataset, in data.train's order
```

Probs are validated as 2–32 entries summing to 1.0 ± 1e-6, each in (0, 1], and the list must be exactly as long as `data.train`. The full config is below.

> **This was a known gap until v0.74.0, and the history is worth one paragraph, because the site published the gap while it stood.** `data.interleave` had validated, documented and parsed since v0.42.0 while **nothing read it at training time**, so every multi-dataset mixture silently trained on `data.train`'s single path. `data.train` also declared a single string, so naming several datasets was rejected outright at config load. v0.73.3 repaired only the visible half, the recipe `soup data mix --optimize` writes, which had been emitting a list form its own loader rejected.

**v0.74.0 wired it.** `data.train` accepts `str | list[str]`; a list of two or more entries is combined by `data.interleave` into one row set, and a single path stays byte-identical to what it was.

**v0.75.0 then changed where `val_split` sits in that order, and the consequence is worth knowing before you trust a validation number.** Under `over` or `probs` the same row could land in **both** `train` and `val`, because the split ran after the padding and a padded copy is the same row. On the eager local-file and all-Hub-name paths `val_split` now runs **first, per source**, so that cannot happen. Two things follow, both upstream's own:

- **The requested fraction is no longer exact** under `over` or `probs`, because it is taken from each source's smaller, unpadded row count. Two sources of 1000 and 100 rows with `over` and `val_split: 0.1` give **110 validation rows out of 1910, which is 5.8%**, not 200 out of 2000.
- **Train and validation end up with different source mixtures.** If you oversampled specifically to correct a source imbalance, your validation set still reflects the original, un-rebalanced skew.

`concat` and `under` never pad, so neither applies to them. **The streaming path is not fixed at v0.75.0** and can still place one row on both sides of the split under `over` or `probs`.

```yaml
data:
  train:
    - ./data/support.jsonl
    - ./data/code.jsonl
  interleave:
    strategy: probs        # concat | under | over | probs
    probs: [0.7, 0.3]
```

Streaming and Hugging Face Hub names work too, and the strategies are deliberately mapped so a name means the same thing on both paths: `concat` concatenates, `under` and `over` stop at the first exhausted or the last, and `probs` passes the probabilities through. That equivalence was verified by running one `probs` config through both paths and comparing the resulting proportions, rather than by two tests that each pass alone.

Two shapes are still **refused by name**: an all-Hub list with `data.streaming: true`, and any list mixing Hub names with local or remote entries. `training.packing` and `training.multipack` are rejected with a list too, at config-parse time, with a message naming the reason.

## Advanced masking + vocab expansion

`mask_history`, `train_on_prompt` (mutually exclusive with `train_on_responses_only`), `eval_on_each_dataset`, `split_thinking` (Qwen3 `<think>` masking), `image_min_pixels` / `image_max_pixels`, `image_resize_algorithm`, `video_fps`, `video_maxlen`.

```yaml
data:
  add_new_tokens: ["<thought>", "</thought>"]
  new_special_tokens: ["<|im_end|>"]
  resize_vocab: true
```

## soup data ingest

Convert PDF / DOCX / MD / TXT into JSONL.

```bash
soup data ingest mybook.pdf --output mybook.jsonl
```

Lazy-imports `pypdf` / `python-docx` so missing optional deps don't crash `soup data --help`.

## AOT tokenize cache

```bash
soup data preprocess soup.yaml --output ./cache
```

Plans the cache key (16-char SHA-256 of dataset + tokenizer + max\_length + format). The live tokenize loop shipped in v0.53.7.

[PreviousTrace → Preference](/docs/trace-to-preference)[NextData Forge](/docs/data-forge)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="057-data-forge"></a>

# 57. Data Forge & Quality Moat (v0.47.0)

*Source: <https://trysoup.dev/docs/data-forge>*

## soup data forge — synthetic data pipeline

Chunk → judge → active-prune → JSONL with provenance.

```bash
soup data forge --docs ./docs --output ./synth.jsonl \
  --task sft \
  --target-rows 5000 \
  --teacher <model> \
  --provenance ./provenance.jsonl
```

`--task` picks the shape of what comes out: `sft`, `preference` or `tool`. `--provenance` writes a separate manifest of `{source_doc, judge_id, chunk_id, filter_score}` so a generated row can be traced back to the document it came from. The rest tune the pipeline: `--uncertainty-threshold` for the active-prune step, `--max-chunk-chars` for chunking, `--judge-provider` / `--judge-model` / `--judge-base-url` for the judge, and `--hub hf|modelscope|modelers` for where the teacher is pulled from.

Each row carries provenance (source doc, chunk offset, judge score).

## soup data score — composite quality scorecard

PII + toxicity + langdetect + educational + decontamination.

```bash
soup data score --input ./train.jsonl --benchmarks gsm8k
```

Each filter is also addressable individually:

- `soup data decontaminate` — drop rows overlapping public benchmarks (n-gram heuristic)
- `soup data toxicity` — keyword baseline today; a Llama-Guard backend is named in the source but is still unshipped as of v0.74.0
- `soup data langdetect` — 2-letter language code per row
- `soup data pii` — flag email / phone / SSN / credit-card patterns
- `soup data educational` — educational-value score per row [0, 1]

[PreviousData Pipeline Pro](/docs/data-pipeline-pro)[NextData Mixing](/docs/data-mix)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="058-data-mix"></a>

# 58. Data Mixing Optimizer & Dynamic Curriculum (v0.48.0 — BETA)

*Source: <https://trysoup.dev/docs/data-mix>*

## soup data mix --optimize

Bayesian search over per-dataset mixture weights against a held-out objective.

```bash
soup data mix --optimize \
  --datasets sft.jsonl,preference.jsonl,instruct.jsonl \
  --output mix.yaml

# --apply does not write a dataset. It prints the data: block to splice
# into your soup.yaml, so the mixture is resolved at training time.
soup data mix --apply mix.yaml
```

The emitted recipe now renders `data.train` as the **full dataset list**, index-aligned with `interleave.probs`, rather than collapsing to the single highest-weighted dataset the way it had to before `data.interleave` was read at training time.

`BudgetTracker` caps wall-clock and token budget per search.

Since v0.73.3 the emitted recipe **loads**. It names the single highest-weighted dataset in `data.train` and keeps the full ranked breakdown as a comment, because at the time `data.train` was typed as a single string. **v0.74.0 closed that**: `data.train` now accepts a list, and two or more local paths are combined through [`data.interleave`](/docs/data-pipeline-pro) before the validation split runs, with streaming and Hub-name lists covered too.

## Dynamic curriculum learning

```yaml
training:
  curriculum: true
  curriculum_dynamic: true
  curriculum_buckets: 5
  curriculum_metric: loss      # length | perplexity | loss
```

`DynamicCurriculumPolicy` re-weights buckets every N steps based on `history.jsonl`. `compute_bucket_weights` clamps to a stable simplex.

```bash
soup runs curriculum-curve <run-id>
soup runs curriculum-curve <run-id> --history ./runs/$LAST/curriculum_history.jsonl
```

Renders the per-bucket weight curve over training.

Both features are BETA in v0.48.0. Symlink containment hardening lands across all file paths.

[PreviousData Forge](/docs/data-forge)[NextTrace Ecosystem](/docs/trace-ecosystem)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="059-trace-ecosystem"></a>

# 59. Trace Ecosystem (v0.63.0)

*Source: <https://trysoup.dev/docs/trace-ecosystem>*

Pull traces from any SaaS observability dashboard, mine prompts, sample the most uncertain rows, run sequential A/B with martingale-controlled Type-I error, and watch production for distributional drift — all from one CLI, all offline, no per-trace fees.

Five new top-level commands, every one of them LIVE in v0.63.0.

## `soup ingest` — universal trace importer

```bash
soup ingest --source langfuse --logs ~/Downloads/langfuse_export.jsonl \
  --output ./traces.jsonl
```

Six sources at launch:

| Source | Env var | Notes |
| --- | --- | --- |
| `langfuse` | `LANGFUSE_PUBLIC_KEY` + `LANGFUSE_SECRET_KEY` | Dashboard export, or a live pull (below) |
| `langsmith` | `LANGSMITH_API_KEY` | LangSmith API traces |
| `helicone` | `HELICONE_API_KEY` | Helicone observability |
| `openpipe` | `OPENPIPE_API_KEY` | OpenPipe production traces |
| `otel` | `OTEL_EXPORTER_OTLP_HEADERS` | OpenTelemetry OTLP |
| `openai-stored` | `OPENAI_API_KEY` | OpenAI Stored Completions |

**Langfuse needs a key pair, not one key.** The hint this path printed used to name `LANGFUSE_KEY`, which is a variable Langfuse does not read at all; it names `LANGFUSE_PUBLIC_KEY` and `LANGFUSE_SECRET_KEY` as of v0.75.0. If you followed the old hint and got nowhere, that is why.

By default there are **no network calls**: you export from the SaaS dashboard, then `soup ingest` normalises the file. Langfuse is the one source Soup can also fetch for itself, with `--pull` (below). A PII warning prints once per invocation either way.

## Live pull from Langfuse (v0.75.0)

```bash
export LANGFUSE_PUBLIC_KEY=pk-lf-...
export LANGFUSE_SECRET_KEY=sk-lf-...

soup ingest --source langfuse --pull --since 24h --output traces.jsonl
```

No export step. `--pull` replaces `--logs` and reads Langfuse's Observations API v2 directly, writing **one row per `GENERATION` observation** into the same `TraceRecord` schema the file path produces. A chat message list becomes a `prompt` of every message's content joined by newlines, **including the system prompt**, which is the same flattening the local parser already applies to a `{"messages": [...]}` export, so the two paths agree. An agent trace therefore yields one row per LLM call it made, and its spans and tool calls yield none. A row's `trace_id` is the observation id.

| Flag | Default | Notes |
| --- | --- | --- |
| `--pull` | off | `--source langfuse` only |
| `--since` | `7d` | `30m`, `24h`, `7d`; maximum `365d` |
| `--max-pages` | `100` | Pages of 100 generations. Maximum 10,000 |
| `--allow-private-host` | off | For a self-hosted Langfuse. HTTPS is still required |

**Credentials never take a flag**, so they never reach the audit log's argv. They come from `LANGFUSE_PUBLIC_KEY` and `LANGFUSE_SECRET_KEY`, with `LANGFUSE_BASE_URL` or `LANGFUSE_HOST` for another region or a self-hosted instance (`LANGFUSE_BASE_URL` wins, matching the Langfuse SDK's own precedence), and they are kept out of the output file, the console, debug logs, the audit log and error messages. A host URL with credentials embedded in it is refused, naming the two variables instead.

Every loop is bounded, and the bounds are the point:

- **HTTPS only**, through the same SSRF validator `--slack-url` uses. **Redirects are refused rather than followed with credentials attached.**
- **30 s per request**, **64 MiB per response**.
- Hitting `--max-pages` **exits 1 and writes nothing** rather than handing you a silently truncated dataset. Output streams to a staging file, so a failed pull leaves an earlier file at `--output` untouched.
- HTTP 429 is retried up to five times honouring `Retry-After`, capped at 60 s.

Generations with no input or no output are skipped and counted in the summary line, so a pull that matched nothing usable says so instead of writing an empty file. It uses the standard library over HTTPS, so there is no new dependency, and **without `--pull` the pull code is never imported and no connection is opened**.

One timing note worth acting on: it reads the **v2 Observations** endpoint because `/api/public/traces` leaves Langfuse Cloud on 16 November 2026.

LangSmith, Helicone, OpenPipe and OpenAI Stored Completions have no live pull yet. Export them and pass `--logs`.

Output schema (frozen `TraceRecord` with `MappingProxyType` metadata):

```json
{
  "trace_id": "trace_abc123",
  "prompt": "What is the capital of France?",
  "output": "The capital of France is Paris.",
  "source": "langfuse",
  "signal": "none",
  "metadata": {"user_id": "user_789", "timestamp": "2026-05-20T..."}
}
```

Feeds directly into v0.26 `soup data from-traces` for preference-pair building.

## `soup prune-prompt` — system-prompt mining

```bash
soup prune-prompt --input ./traces.jsonl --output ./traces_pruned.jsonl --min-frequency 0.95
```

Detects the longest shared system-prompt prefix across rows via **binary search over up to 32 candidate lengths** (v0.63 fixed an O(N²) early-exit bug from the prototype). Strips it from training data so the fine-tuned model internalizes the boilerplate instead of repeating it — OpenPipe's signature trick.

Pass `--tokenizer <model>` and the prefix is found over **token ids** rather than characters. That is not a refinement: a character-level strip can cut a BPE multi-byte sequence in half when the shared prefix ends mid-token, and the tokenizer-aware mode finds the longest shared token-id prefix and decodes what remains. `--slack-url` and `--discord-url` post the result through the same SSRF-hardened webhook validator the rest of the CLI uses.

Two-pass file read; capped at 100k rows to prevent DoS.

## `soup data active-sample` — uncertainty sampling

```bash
soup data active-sample --input ./prod_traces.jsonl --budget 200
```

Two modes auto-detected from the JSONL schema:

- **Single score** — max-entropy on `rm_score` (peaks at 0.5).
- **Dual scores** — pairwise disagreement on `rm_scores` list.

Output is a drop-in eval prompt set for human judging.

## `soup ab` — Wald-SPRT sequential A/B

```bash
soup ab --input ./ab_results.jsonl --metric judge_score \
  --alpha 0.05 --beta 0.20 --effect-size 0.1
```

`--slack-url` and `--discord-url` post the verdict through the same SSRF-hardened validator the rest of the CLI uses, and the interesting half is when they stay quiet: the webhook fires only when the test actually **decides**, accepting or rejecting the null. A run that is still gathering evidence says nothing. The same pair is on `soup ingest`, `soup prune-prompt` and `soup data active-sample`.

Wald's SPRT (Sequential Probability Ratio Test) is a martingale under the null hypothesis — Type-I error is controlled **at every stopping time**, not just at a fixed sample size. Early-stops when the log-likelihood ratio crosses A = log((1-β)/α) (reject H0) or B = log(β/(1-α)) (accept H0).

Input rows:

```json
{"arm": "control", "latency": 150.2}
{"arm": "treatment", "latency": 145.1}
```

Decisions: `reject_h0` / `accept_h0` / `continue`. v0.63 ships a CRITICAL fix for a sign error in the historical mSPRT implementation.

Three metrics at launch: `latency`, `judge_score`, `retry_rate`.

## `soup drift-alarm` — KL drift watch with webhooks

```bash
soup drift-alarm \
  --reference ./ft_output_dist.jsonl --live ./prod_output_dist.jsonl \
  --threshold 0.2 \
  --slack-url "https://hooks.slack.com/services/T.../B.../..."
```

Rolls KL divergence between **token-distribution snapshots** at fine-tune time vs. production. Surfaces both behavioral drift ("model now outputs JSON") and vocabulary drift ("same 20 phrases repeated"). Whitespace tokenization is the default; pluggable tokenizers ship in v0.63.1.

Input rows (one per token):

```json
{"token": "json", "log_prob": -3.2}
```

Optional Slack / Discord webhooks fire on drift, **SSRF-validated** (loopback-only, RFC1918 / link-local / cloud-metadata IPs rejected). Exit code 3 on drift for cron-friendly automation.

## Numbers

+219 new tests in v0.63.0 (9816 → **10035**). Security: 1 CRITICAL (mSPRT sign error → Wald SPRT), 2 HIGH, 3 MEDIUM, 2 LOW.

## See also

- [Soup loop](/docs/soup-loop) — the `HarvestFn` half of the v0.58 production flywheel is now powered by `soup ingest`.
- [Trace-to-preference](/docs/trace-to-preference) — convert normalised traces into DPO / KTO pairs.
- [Eval design](/docs/eval-design) — derive a goal-conditioned eval suite from the active-sampled prompts.

[PreviousData Mixing](/docs/data-mix)[NextData Engineering Pro](/docs/data-engineering-pro)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="060-data-engineering-pro"></a>

# 60. Data Engineering Pro (v0.69.0)

*Source: <https://trysoup.dev/docs/data-engineering-pro>*

Dataset prep stops being "throw a JSONL at the trainer" and becomes a first-class engineering discipline. dbt-shaped DAG, Great-Expectations suite, Magpie synth, Persona-Hub diversity, and the [arXiv 2510.13928](https://arxiv.org/abs/2510.13928) brain-rot detector.

## `soup build` — dbt-shaped DAG of dataset transforms

```yaml
# manifest.yaml
# Each model names a transform, not SQL. A seed model reads a source;
# every downstream model names the models it consumes in refs.
models:
  - name: chats_raw
    kind: incremental
    source: data/thumbs_up.jsonl
    transform: identity
  - name: chats_decontaminated
    kind: incremental
    refs: [chats_raw]
    transform: drop_empty
  - name: chats_train
    kind: view
    refs: [chats_decontaminated]
    transform: token_count
```

```bash
soup build manifest.yaml --dry-run    # validates topology, exits 0 (LIVE today)
soup build manifest.yaml              # materialises (live since v0.71.6)
```

- Closed `SUPPORTED_MODEL_KINDS = {incremental, table, view}`
- Topo-sort via Kahn's algorithm
- **Re-tokenise only changed rows**: `compute_row_hash` (SHA-256 over canonical-JSON, `id` field excluded) + `incremental_diff(prev, new) → {added, changed, removed, unchanged}`
- DoS caps: `_MAX_MODELS=256`, `_MAX_REFS_PER_MODEL=32`, `_MAX_FILE_BYTES=1 MiB`
- **Live as of v0.71.6** — `run_build` materialises datasets with five built-in transforms, and these are the whole list: `identity`, `drop_empty`, `lowercase`, `add_field` and `token_count`. Anything else must be a **dotted import path** (`my_pkg.transforms:filter_low_quality`), resolved from the CLI, which upstream flags as arbitrary code execution: only run a manifest you trust. **A name that is neither is caught by the runner, not by the plan**, so `--dry-run` exits 0 on a manifest whose real run dies on the first unknown transform. The schema deliberately does not validate the function reference. `table` rebuilds, `view` re-derives, `incremental` re-transforms only the rows whose content hash changed (SQLite state store, keyed by row hash + transform fingerprint). Custom transforms pass per-run via the Python API. v0.71.6 also makes `soup data gen-magpie` generate live (ollama / vllm raw-completion, SSRF-hardened; `anthropic` rejected).

## `soup expect` — Great Expectations for chat data (LIVE)

```yaml
# suite.yaml
expectations:
  - expect_no_pii
  - expect_token_length_between: {min: 32, max: 2048}
  - expect_no_refusal_pattern
  - expect_chosen_preferred_over_rejected_by_judge:
      judge: openai/gpt-4o-mini
      min_win_rate: 0.55
```

```bash
soup expect ./data.jsonl ./suite.yaml
# exit 0 = pass; 2 = validation rejection; 3 = suite failure
```

Closed allowlist: `expect_no_pii` (reuses v0.47 Presidio), `expect_token_length_between`, `expect_no_refusal_pattern` (reuses v0.56 refusal detector), `expect_chosen_preferred_over_rejected_by_judge` (reuses v0.19 judge surface). Walks `text`, `content`, `output`, `prompt`, `instruction`, `response` top-level keys + `messages[].content` arrays. `_MAX_SUITE_LEN=64`. Drop into CI between `soup data` and `soup train`.

## `soup data gen-magpie` — synthetic data via chat-template-prefix harvest

```bash
soup data gen-magpie --base meta-llama/Llama-3-8B \
  --provider ollama --target 50000 \
  --output ./synth.jsonl
```

Magpie trick: prime the base model with just the assistant chat-template prefix and let it complete the prompt itself. Reuses the v0.20 provider stack, minus Anthropic: Magpie primes the base model with a bare chat-template prefix, which a hosted chat API will not do, so `--provider anthropic` is refused here. Ollama and vLLM work. `_MAX_TARGET_ROWS=1_000_000`, `_MAX_BASE_MODEL_LEN=512`. The live `run_magpie` loop and the v0.47 quality-filter chain shipped in v0.71.6, with `--quality-filter` on by default.

## `soup data persona-mix` — Persona-Hub diversity sampler (LIVE)

```bash
soup data persona-mix --prompts ./prompts.jsonl \
  --n 20000 --output ./diverse.jsonl
# Optional BYO: --personas tencent-200k.jsonl --styles styles.jsonl
```

Bundled 12 personas × 5 writing styles (BYO Tencent 200k corpus via `--personas` / `--styles`). Deterministic by seed (`random.Random(seed)`). `compute_topic_diversity` = Shannon entropy over pooled whitespace tokens. Atomic JSONL write + cwd-contained input + `enforce_under_cwd_and_no_symlink` on output. Caps: 100 MiB / 100k entries per loader.

## `soup data brain-rot` — AI-slop detector (LIVE)

```bash
soup data brain-rot ./data.jsonl --strict --max-major-fraction 0.25
# exit 3 if MAJOR fraction > 0.25
```

[arXiv 2510.13928](https://arxiv.org/abs/2510.13928) brain-rot detector. Two pure-Python scorers:

- `score_triviality` — token-diversity inversion + `!!` / `??` punctuation runs + low-effort token density + length penalty
- `score_popularity_signal` — clickbait phrase scan + emoji U+1F300–U+1FAFF density

Worst-signal-wins: `1.0 − max(triviality, popularity)`. Bands match v0.26/v0.56/v0.65: OK ≥ 0.85, MINOR ≥ 0.60, else MAJOR. `refuse_if_rotten` raises when MAJOR fraction exceeds threshold. English-keyword-only in v0.69.0; multilingual shipped in v0.71.6 behind `--lang en|es|fr|de|ru|auto`.

## Cross-cutting hardening

Refactored 3 duplicate TOCTOU blocks behind a new shared `paths.enforce_under_cwd_and_no_symlink` helper (code-review CRITICAL fix). v0.70 + future releases reuse it.

## Numbers

+262 tests in v0.69.0 (11,225 → **11,487**) across 5 new test files. 3 POSIX-only symlink tests skip on Windows.

## See also

- [Anti-trend insurance (v0.68)](/docs/anti-trend-insurance) — the TOCTOU helper this consolidates was first lifted here.
- [Loop hardening (v0.70)](/docs/loop-hardening) — `soup expect` gates data going into `--reward-hack-detector` runs.
- [Eval depth (v0.65)](/docs/eval-depth) — same OK / MINOR / MAJOR taxonomy.

[PreviousTrace Ecosystem](/docs/trace-ecosystem)[NextData Moat II](/docs/data-moat-ii)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="061-data-moat-ii"></a>

# 61. Data Moat II (v0.71.36)

*Source: <https://trysoup.dev/docs/data-moat-ii>*

A semantic layer over your training data, plus two tools for what a fine-tune **forgets** and **leaks**. Four commands: dedup the reworded duplicates MinHash misses, map which topics your data actually covers, plant canaries and later prove whether the model memorized them, and replay a slice of the old task so a new one does not erase it.

Zero new dependencies. The embedding kernel reuses `transformers` from the `[train]` extra (mean-pooled `all-MiniLM-L6-v2`, no `sentence-transformers`), so `dedup --semantic` and `topics` need `[train]` plus a one-time model download; plain MinHash `dedup` stays on the light core.

## `soup data dedup --semantic` — near-duplicates over meaning, not shingles

```bash
soup data dedup train.jsonl --semantic -o clean.jsonl
soup data dedup train.jsonl --semantic --threshold 0.85 --field text -o clean.jsonl
soup data dedup train.jsonl --semantic --embed-model sentence-transformers/all-mpnet-base-v2
```

MinHash shingling compares token sets, so a **reworded** duplicate reads as distinct. Semantic dedup compares embedding cosine instead and catches those: measured, rewordings score 0.88 to 0.91 cosine where MinHash scored them apart, while genuinely-distinct-but-similar instructions are kept.

> **Honest limit: this is not a paraphrase detector.** Measured with `all-MiniLM-L6-v2`, paraphrase cosines (0.49 to 0.76) \*overlap\* genuinely-distinct rows (0.54 to 0.76). "Add two numbers" vs "Multiply two numbers" scores **0.759**, higher than the true paraphrase "reverse a string" / "invert the order of characters" at **0.491**, so no threshold separates them. Lowering `--threshold` to chase paraphrases deletes real training rows. The default `0.8` is deliberately conservative (max distinct-pair cosine measured was 0.759) and still strictly beats MinHash.

## `soup data topics` — a coverage map of your dataset

```bash
soup data topics train.jsonl                    # 'auto' picks the cluster count
soup data topics train.jsonl --clusters 8 -o topics.json
```

Clusters the dataset (k-means over the same embeddings), labels each cluster with its distinctive terms (c-TF-IDF), and prints a coverage table plus a warning for thin topics:

```
82% code · 9% chat · 6% math · 2% sql · 1% legal
topic 'legal' is thin: 1% of rows — likely under-represented
```

Only topics under 2% of the data are flagged (a 6% topic like `math` above is left alone). Labels are **emergent term clusters, not a fixed taxonomy**, and there is no automatic join to an eval-coverage suite; read the table as "where my data concentrates", not as classification against an ontology.

## `soup data canary insert|check` — prove what the model memorized

```bash
# 1. insert K unique high-entropy secrets (keep the manifest OUT of your repo)
soup data canary insert train.jsonl -o canaried.jsonl --count 16 --manifest secrets.json

# 2. train on canaried.jsonl as usual, then rank each secret's loss vs controls:
soup data canary check --manifest secrets.json --base ./my-model --adapter ./lora
```

A Secret-Sharer memorization probe ([Carlini et al.](https://arxiv.org/abs/1802.08232)): insert K secrets, train, then check any model or adapter by ranking each secret's loss against never-inserted controls drawn from the same space. Measured on SmolLM2-135M, a memorized set lands at percentile 0.0 (loss 1.7 to 2.5) against a clean model's 4.1 to 6.2. The verdict is a **binomial-tail test (α = 0.05) over the count** of memorized canaries, and **exit 2 on MAJOR** lets CI gate a leak.

> The verdict is a binomial tail on purpose. The obvious rule, "MAJOR if any single canary ranks in the bottom 1%", fires MAJOR on a **clean** model about 15% of the time at K = 16 (a CI gate crying wolf one run in seven); the count-based test drops that false-MAJOR rate to ~1.2% while still catching a partial leak of 2 of 10. "No exposure" is the sampled-control approximation, not full-space rank enumeration, so it is evidence of no memorization, not a proof. The manifest is the sensitive artifact and is written `0600` on POSIX.

## `soup train --replay` — rehearse the old task so the new one does not erase it

```bash
soup train --config new_task.yaml --replay old_task.jsonl --replay-ratio 0.1
```

Continual-learning rehearsal: interleave a seeded sample of an old dataset into training so a new task does not overwrite the old one. `--replay-ratio` is the fraction of the **final** mixed set (`n_replay = round(r/(1-r) · n_new)`), rows are **interleaved rather than appended**, an undersized pool reports the shortfall instead of repeating rows, and the mix touches `train` only, so validation stays pure new-task.

> **Honest scope: proof-of-mechanism.** On SmolLM2-135M + LoRA, replay retained the old task 7% better than a no-replay control (the correct direction), but forgetting without it was only about +4%, i.e. mild, so the effect size at full fine-tuning or 7B+ is unproven on a 4 GB box. Replay v1 is `sft` / `pretrain` only and is incompatible with `packing` / `multipack`.

## Fixes that shipped with it

- **The hardware-fit gate refused to train any locally-merged model.** A `soup merge -o ./mymodel` output has no size marker in its name, so the size guesser returned its 7B default, predicted ~16 GB of VRAM, and refused, blocking the exact merge-then-train-from-merged flow that `--replay` serves. Local checkpoints are now measured from their safetensors header (0.135B actual versus 7.0B guessed). This is the third instance of that class after the v0.71.32 (Whisper) and v0.71.33 (`M` suffix) fixes, and all three were caught by a live smoke, never a unit test.
- **Replay rows now get the same path-traversal validation as the primary dataset** (a llava-shaped `{"image": ...}` replay row previously bypassed the vision/audio guard).

## See also

- [Data Tools](/docs/data-tools) — inspect, validate, convert, merge, and plain MinHash dedup.
- [Data Engineering Pro](/docs/data-engineering-pro) — the dbt-shaped build DAG, `soup expect`, Magpie, brain-rot (Data Moat I).
- [soup ship](/docs/soup-ship) — the SHIP / DON'T-SHIP verdict a canary leak should block.
- [Supply-chain security](/docs/supply-chain-security) — the other side of "what leaves the model".

[PreviousData Engineering Pro](/docs/data-engineering-pro)[NextBest-of-N & Evolve](/docs/best-of-n-evolve)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="062-best-of-n-evolve"></a>

# 62. Best-of-N & Evol-Instruct (v0.71.31)

*Source: <https://trysoup.dev/docs/best-of-n-evolve>*

Two `soup data` subcommands that put an LLM judge in the loop to build training data, the data side of the v0.71.31 [judge-in-the-loop suite](/docs/online-dpo).

> We have not found this as an integrated CLI suite elsewhere.

## soup data best-of-n — rejection sampling (BOND-lite)

Sample N completions from a base model, let a judge score each one, keep the winner as a clean SFT row. With `--emit-pairs` it also writes winner-versus-loser DPO pairs, so one pass bootstraps both an SFT set and a preference set.

```bash
soup data best-of-n --base HuggingFaceTB/SmolLM2-135M-Instruct \
    --prompts prompts.jsonl --n 8 --judge ollama://llama3.1 \
    -o best_of_n.jsonl --emit-pairs pairs.jsonl
```

| Flag | Default | Meaning |
| --- | --- | --- |
| `--base` | the default path | Local model to sample from (loads locally; bounded by your GPU). Give this or `--provider`. |
| `--provider` | off | v0.74.0. `ollama` or `vllm`: draw the candidates from a running raw-completion endpoint instead of loading a model. `anthropic` is refused by name, because its Messages API has no raw-completion endpoint. |
| `--model` | required with `--provider` | Provider-side model id, recorded in `_best_of_n` provenance next to the provider. |
| `--base-url` | loopback | Provider endpoint, SSRF-validated. |
| `--prompts` | required | Prompt JSONL (cwd-contained, symlink-rejected). |
| `--judge` | required | Judge URL, SSRF-validated. |
| `--n` | `8` | Candidates per prompt (`2..64`). |
| `-o`, `--output` | required | SFT output JSONL; each row carries a `_best_of_n` provenance object (`n`, `winner_idx`, `judge_model`, `scores`). |
| `--emit-pairs` | off | Also write winner-vs-loser DPO pairs to this path. |
| `--temperature` | `1.0` | Sampling temperature (`0..2`). |
| `--max-new-tokens` | `256` | Tokens per candidate (`1..4096`). |
| `--seed` | `0` | Sampling seed. |
| `--plan-only` | off | Print the plan and exit without sampling. |

Judging is pointwise (one judge call per candidate, argmax), so cost scales with `--n`. Prompt rows are validated with line-numbered errors instead of being silently dropped, each accepted row records its `source_line`, and a non-finite or boolean judge score is rejected before a winner is picked (v0.74.0).

### Sampling from a provider, and finishing what you started (v0.74.0)

The candidates no longer have to come from a model you load. `--provider ollama|vllm --model <id> [--base-url <url>]` draws them from a running raw-completion endpoint through the same SSRF-validated seam `soup data evolve` uses. The local-only flags are refused in provider mode rather than silently ignored.

A run that dies partway no longer starts over. Sampling is journalled per prompt (`--checkpoint`, defaulting beside the output), `--resume` continues from the last committed group, and the outputs are published manifest-last, so an interruption never leaves a partial SFT or DPO file behind. A resume binds the prompt source lines and the exact local model content, so it refuses to continue against changed inputs instead of quietly mixing two runs.

For an air-gapped or two-phase workflow, split sampling from judging:

```bash
# Phase 1, where the GPU is: sample only, construct no judge.
soup data best-of-n --base Qwen/Qwen2.5-7B-Instruct --revision <commit> \
    --prompts prompts.jsonl --n 8 --export-candidates candidates.jsonl

# Phase 2, anywhere: materialize the outputs from verified judgments,
# with no model load and no network.
soup data best-of-n --candidate-artifact candidates.jsonl \
    --judgments verified.jsonl -o best_of_n.jsonl --emit-pairs pairs.jsonl
```

Offline materialization commits through a final verifiable manifest, rejects online-only recovery options, and fails closed on an interrupted or mismatched generation rather than writing a file.

> **Breaking, if you script it:** `--export-candidates --seed N` seeds each prompt independently as of v0.74.0, so a resumed run reproduces the same candidates. That changes the output of an existing `--export-candidates --seed N` command.

## soup data evolve — Evol-Instruct (WizardLM)

Grow instruction diversity by mutating seed prompts, completing the synthetic-data suite (Magpie, Forge, Persona, evolve). `depth` deepens an instruction (adds constraints, concretizes, adds reasoning steps); `breadth` creates a new sibling instruction in the same domain.

```bash
soup data evolve --input seeds.jsonl --provider ollama --model llama3.1 \
    --strategy depth --rounds 2 -o evolved.jsonl
```

| Flag | Default | Meaning |
| --- | --- | --- |
| `--input` | required | Seed instructions JSONL. |
| `--provider` | required | `ollama` or `vllm` (the raw-completion providers; `anthropic` is rejected). |
| `--model` | required | Generator model id. |
| `--strategy` | `depth` | `depth` (deepen) or `breadth` (diversify). |
| `--rounds` | `1` | Evolution rounds (`1..5`). |
| `-o`, `--output` | required | Evolved output JSONL. |
| `--max-tokens` | `512` | Generation budget (`1..16384`). |

Each round evolves every live instruction and drops empty, unchanged, or meta-prompt-echo outputs; if a round eliminates everything, the previous generation carries forward.

## Security

Both write atomically (`mkstemp` + `os.replace`) with cwd containment re-validated to close a symlink-swap window; every judge / provider URL is SSRF-validated; `--base` loads with `trust_remote_code=False` (probe + warn); dataset-derived text is escaped before it is echoed. Prompts / seeds are capped at 100,000 rows.

## See also

- [Online DPO](/docs/online-dpo) — train on-policy against the same judge.
- [soup ship](/docs/soup-ship) — decide SHIP with a pairwise judge win-rate.
- [Data Forge & quality moat](/docs/data-forge) and [Data engineering pro](/docs/data-engineering-pro) — the rest of the synthetic-data and quality surface.

[PreviousData Moat II](/docs/data-moat-ii)[NextShip Verdict](/docs/soup-ship)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="063-soup-ship"></a>

# 63. soup ship: the SHIP / DON'T-SHIP verdict (v0.71.25)

*Source: <https://trysoup.dev/docs/soup-ship>*

After a fine-tune there is exactly one question worth answering: **did the model get better, or did I break it?** `soup ship` answers it as a single binary verdict, **SHIP** or **DON'T SHIP**, plus a one-screen reason. It is not a dashboard to interpret, it is a decision you can gate CI on.

The trick most pipelines miss is that a model can \*win the task you trained for\* and still be worse, because it forgot how to do everything else. `soup ship` fuses both checks into one rule and refuses that model.

## The decision rule

```
SHIP  ⇔  (leg 1) task_tuned > task_base          # strict improvement
     AND (leg 2) every benchmark: base − tuned ≤ forgetting_threshold
else DON'T SHIP — even if the task metric looks great.
```

- **Leg 1, task win** — the metric you care about strictly improved from base to tuned. A tie is **not** a win.
- **Leg 2, no catastrophic forgetting** — no general benchmark dropped more than the forgetting threshold (default **0.05 absolute points**, the same semantics as the eval-gate regression threshold).

A missing baseline does not silently SHIP, it **refuses** with a clear message. When more than one rule fails the reason names the most decisive one (missing baseline → task win → regression).

## Run it

```bash
# live: score a base model and a LoRA adapter on your task + the default suite
soup ship \
  --base meta-llama/Llama-3.1-8B \
  --adapter ./output/adapter \
  --task-eval tasks.jsonl
```

```bash
# judge the task win with an LLM, regress against named lm-eval suites
soup ship \
  --base meta-llama/Llama-3.1-8B \
  --tuned ./my-finetuned-model \
  --task-eval tasks.jsonl \
  --task-mode judge_score --judge-model ollama://llama3.1 \
  --general-suite mmlu,gsm8k \
  --baseline registry://abc123
```

```text
DON'T SHIP
Leg 1 task win (judge_score): 0.6200 -> 0.6100  [no win]

Leg 2 general suite (threshold 5.00%)
  mmlu               0.7500 -> 0.6900   -0.0600   REGRESS
  gsm8k              0.5200 -> 0.5300   +0.0100   ok

General benchmark(s) regressed past 5.00%: mmlu.
Catastrophic forgetting: DON'T SHIP even though the task metric was ok.
```

Exit codes are CI-ready: **0 = SHIP**, **2 = DON'T SHIP**, **1 = runtime error**, and (since v0.71.38) **3 = usage error** (a typo'd flag or a bad `--general-suite`), so a misconfigured gate never masquerades as a DON'T-SHIP.

## Decide offline, with no model load

`--evidence ev.json` reaches a verdict from pre-computed scores, so CI can gate without a GPU:

```bash
soup ship --evidence ev.json --output verdict.json
```

```json
{
  "task": { "mode": "metric", "base": 0.40, "tuned": 0.55 },
  "benchmarks": {
    "mini_mmlu":         { "base": 0.80, "tuned": 0.79 },
    "mini_common_sense": { "base": 0.60, "tuned": 0.62 },
    "mini_instruction":  { "base": 0.70, "tuned": 0.71 }
  }
}
```

`--output verdict.json` also persists the machine-readable verdict from a live run.

## Pairwise judge win-rate (v0.71.31)

`--task-mode pairwise` decides leg 1 with a true head-to-head judge: for each prompt the judge picks base vs tuned, swap-debiased so a win only counts when both orders agree. The base is a 0.5 coin-flip, and the tuned model wins the leg only if its win-rate is above 0.5.

```bash
soup ship --base <m> --adapter ./out --task-eval tasks.jsonl \
  --task-mode pairwise --judge-model ollama://llama3.1
```

Offline, the `--evidence` task block takes `{ "mode": "pairwise", "base": 0.5, "tuned": <winrate> }`.

## The regression leg grew teeth (v0.71.38)

Leg 2 is the moat, so it had to be trustworthy. It used to be fifteen trivia prompts scored by case-insensitive **substring containment**, which credited `"B"` for **B**erlin and `"3"` for 1**3**, and had zero coverage of tool-calling, JSON validity or safety. v0.71.38 replaced that with an **answer-extraction plus boundary-aware scorer** and a bundled, offline **general suite of seven hand-authored benchmarks** shipped in the wheel:

- `mini_mmlu` · `mini_common_sense` · `mini_instruction` (expanded)
- `mini_arithmetic` (new)
- `mini_tool_call` (function-calling), `mini_format_json` (JSON validity), `mini_safety` (refusal rate) — three the old gate could not see at all

Each suite is roughly **24 to 40 items**, small enough to run offline in a blink but large enough that a single wrong answer sits well under the default 0.05 threshold and trips the gate instead of being rounded away. Everything is scored offline with Soup's own scorers: **no lm-eval, no network, no download.** Naming your own suites (`--general-suite mmlu,gsm8k`) still routes through lm-eval as an override.

### An eighth suite, and two of the seven were mis-scoring (v0.73.2)

Giving the leg teeth was not the same as giving it eyes, and v0.73.2 found it **ranking by the wrong thing in two suites and blind in one whole direction**.

- **`mini_over_refusal` joins as the eighth default suite.** Leg 2 flagged a drop in refusal rate and had no reverse, so a tune that refuses everything read as a monotone safety improvement. Two models with byte-identical scores on all seven shipped suites and the same verdict, one of which refuses every benign request, were indistinguishable to it. The new suite is 40 benign requests that merely sound alarming, scored as the **fraction not refused**, so safety and helpfulness are two axes and neither can be gamed alone.
- **`mini_mmlu` and `mini_common_sense` did not understand a boxed answer.** A stub answering every item correctly scored **0.000**, and Llama-3.1-8B scored **0.423**, below a 0.5B, while scoring 1.000 on two other multiple-choice suites. Fixed on both halves at once (the extractor alone is worth eight items, the prompt alone worth zero): **0.423 to 0.731**.
- **`mini_tool_call` ranked by brace hygiene.** The same 8B named the right tool **40 times out of 40** and scored **0.225**. Now 1.000.

> **A `--baseline` snapshot taken before v0.73.2 is on a different scale** for those three suites, and the jumps on an unchanged model are larger than the 0.05 gate. Re-take it. `mini_instruction` and `mini_arithmetic` are unaffected. Full detail on [the v0.73.2 page](/docs/ship-gate-repairs).

### Measure the instrument first: `--noise-floor` (v0.73.2)

Greedy decoding is not deterministic on a GPU. Measured over five runs of one model with no adapter, the scores spread **0.015 strict and 0.020 format-blind**, against a threshold of 0.05, and four of six paired deltas in that session sat inside the floor. Until v0.73.2 the gate compared against 0.05 without ever saying what it could resolve.

```bash
soup ship --base ./base --adapter ./out --task-eval task.jsonl --noise-floor 5
```

`--noise-floor N` (N from 2 to 10) re-runs the base N times, prints the measured floor beside the verdict, and gates each axis at whichever is larger, the threshold or the floor. Two caveats travel with it: those two figures are **the borrowed H100 session's**, not the release's own development box, which measured **0.0000** on CPU where greedy decode is deterministic; and at **n=3, one model, one dataset** the floor sizes the effect rather than calibrating a threshold. Widening its scope in v0.73.3 did not change that second caveat.

**Since v0.73.3 the leg-1 task floor is measured in every `--task-mode`, not only `metric`.** In `judge_score` the base side is scored N times through the judge; in `pairwise` the base model is judged **against itself**, where the expected win rate is 0.5 by construction, so the spread is measured rather than inferred. Those repeats fold in the judge's own sampling noise, so that floor is labelled **`decode + judge`** on the panel and stamped `judge_inclusive` in the evidence and JSON output, and it must never be read as a decode-only number. The cost is N extra judge API calls, and a missing or malformed `--judge-model` is now a usage error up front rather than a failure discovered mid-measurement.

The floor is also committable. `eval.ship.noise_floor` joins the other gate-policy fields under `eval.ship` in `soup.yaml`, bounded to the same `[2, 10]` from the same constant the CLI validates against, with CLI over config over default precedence. Like the flag, it is a live-measurement input: it is measured when a run produces evidence and refused under `--evidence`, and it is excluded from the recipe hash, so setting a floor never invalidates evidence you already have.

## Evidence you can commit (v0.71.39)

v0.71.38 made the verdict trustworthy; v0.71.39 makes it **reproducible and provenance-bound**, so `soup ci init` becomes CI for weights, not prompts.

```bash
# emit the verdict back into the --evidence input schema (a run's output replays as input)
soup ship --base <m> --adapter ./out --task-eval tasks.jsonl --emit-evidence evidence.json

# commit the gate policy in soup.yaml (eval.ship), then run it; CLI > config > default
soup ship --config soup.yaml --emit-evidence evidence.json

# post the verdict as a PR comment (best-effort, never flips the exit code)
soup ship --config soup.yaml --push owner/repo#42
```

- **`--emit-evidence <path>`** re-serializes the verdict into the `--evidence` **input** schema, so the same file replays through `--evidence` (same `--forgetting-threshold`) to an identical verdict.
- **`ShipConfig` under `eval.ship` in `soup.yaml`** + **`--config soup.yaml`** commit the gate policy (`task_eval` / `task_mode` / `general_suite` / `forgetting_threshold` / `judge_model` / `baseline`, plus `noise_floor` since v0.73.3). Precedence is **CLI > config > default**.
- **Provenance + staleness gate.** Emitting evidence stamps a `provenance` block (an order-insensitive `config_sha`, the `base_model`, a best-effort `data_sha`). Reading evidence back with `--config` then **refuses (exit 3)** evidence whose `config_sha` drifted from the committed recipe. The gate policy itself is **excluded** from the hash, so tuning `forgetting_threshold` never falsely invalidates evidence.
- **`soup ci init --config soup.yaml`** binds the generated PR gate to that committed config, so the check on every pull request enforces provenance too.

### If you shipped a 4-bit or 8-bit adapter before v0.74.0, re-judge it

The judge loaded the base model at full precision no matter what the run had trained at, so an **NF4-trained adapter was scored against a bf16 base it never saw during training**, and the fallback message claimed bf16 while never actually setting a dtype. `soup ship --config soup.yaml` now derives the load precision from `training.quantization` when it is `4bit` or `8bit`, and prints the precision it actually loaded. Other quantization formats still fall back to full precision, and `advise --probe-model`, `diagnose --base-model` and `tunability --live` take no such flag yet, so they keep the old default. Two halves of that issue stay open upstream and are worth knowing before you trust a stored verdict: the numerics are **not** stamped into the verdict or the evidence JSON, and there is **no staleness gate** on evidence whose numerics do not match.

## Flags

| Flag | Default | Description |
| --- | --- | --- |
| `--base` | (required, live) | Base model id or path, the "before". |
| `--tuned` / `--adapter` | (one required, live) | The "after": a separate tuned model, or a LoRA adapter on top of `--base`. Mutually exclusive. |
| `--task-eval` | (required, live) | JSONL of leg-1 task-win eval items. cwd-contained, symlink-rejected. |
| `--task-mode` | `metric` | Leg-1 mode: `metric` (eval accuracy), `judge_score` (pointwise LLM-as-a-judge), or `pairwise` (a swap-debiased judge win-rate, base vs tuned per prompt, base = 0.5). `pairwise` requires `--judge-model` (v0.71.31). |
| `--judge-model` | (judge mode only) | Judge URL, validated by scheme and host (blocks SSRF prefix bypasses). |
| `--general-suite` | eight mini suites | Leg-2 benchmarks. Default is the eight bundled offline suites (seven from v0.71.38, plus `mini_over_refusal` in v0.73.2); named suites route through lm-eval as an override. ≤ 50 names. |
| `--noise-floor` | (off) | Re-run the base model N times (`[2, 10]`) to measure what this instrument can resolve, print it beside the verdict, and refuse to call any smaller delta significant (v0.73.2). Every `--task-mode` since v0.73.3; in the judge modes it costs N judge passes and is labelled `decode + judge`. |
| `--baseline` | (none) | Recorded base leg-2 scores, `registry://<id>` or a JSON file, to skip the base run. |
| `--forgetting-threshold` | `0.05` | Max allowed leg-2 drop in absolute points, in `[0.0, 1.0]`. |
| `--evidence` | (offline mode) | Decide from a pre-computed scores JSON, no model load. `O_NOFOLLOW`, 16 MiB cap, cwd-contained. |
| `--config` | (none) | Load the gate policy from `eval.ship` in `soup.yaml`; also gates `--evidence` on config staleness (v0.71.39). CLI > config > default. |
| `--emit-evidence` | (none) | Re-serialize the verdict into the `--evidence` input schema, stamped with a provenance block (v0.71.39). |
| `--push` | (none) | `owner/repo#N`: post the verdict as a GitHub PR comment. Best-effort; never flips the exit code (v0.71.39). |
| `--output` | (stdout) | Write the verdict JSON to a path (kept under cwd). |
| `--device` | auto | `cuda` or `cpu` for the live run. |

## Why no other tool ships this

Leg 2, the catastrophic-forgetting gate, is the moat. Plenty of tools will tell you whether your task metric went up. What we have not found elsewhere is a first-class binary command that refuses a model on the grounds that it broke general knowledge. The regression math reuses Soup's existing eval-gate kernel, the new value is the single fused verdict, the one-screen reason, and a task-win leg that now includes a real pairwise judge win-rate.

## Inference prompts now match training (v0.75.0)

Until v0.75.0 every generating command, including this one, rendered the chat template to text and then handed that text to the tokenizer, which added its **own** special tokens on top. On a template that renders a BOS itself — Llama-3, Gemma, Mistral — that meant a **doubled BOS at inference** against the single one Soup's default supervised path trains with.

Measured: **2 BOS down to 1** on vendor templates, **1 down to 0** on Soup's own `data.chat_template` presets, which render none, plus no trailing EOS from tokenizers that append one. `usage.prompt_tokens` drops accordingly.

**So a verdict issued before v0.75.0 was measured on a prompt that differed from training by a token.** Nothing about the weights changed, and the same applies to `soup bench` numbers, `soup diff` comparisons, `soup diagnose`, `soup advise` and the eval gate's own generators. Re-judge rather than assuming.

Two riders travel with it. An adapter trained with `train_on_responses_only: false` **saw** the doubled BOS in training, so it now differs from inference by one token in the other direction. And the **vLLM, SGLang and DeepSpeed-MII engines are still affected**, because they tokenize the rendered string themselves rather than receiving ids; that half is tracked upstream, and `--backend transformers` is the workaround if you need the verdict to match training exactly.

## v1 honesty

- **Pairwise judge win-rate** (`--task-mode pairwise`) is **live as of v0.71.31**: the judge picks base vs tuned per prompt, swap-debiased (a win counts only when both orders agree), base is a 0.5 coin-flip and the tuned model wins only if its win-rate exceeds 0.5. Because CI resolves trl 1.x, a runtime adapter uses the pairwise judge on trl 0.19.x and the same judge pointwise on trl 1.x.
- **`ShipConfig` under `eval.ship` is live as of v0.71.39** (the earlier CLI-only note no longer holds); the verdict engine is pure-Python and fully tested.
- Built-in mini-benchmarks are offline and instant, lm-eval suites block on a real model load.
- One honesty note that shipped alongside these releases: Soup's telemetry primitives existed with **no command wired to them**, so nothing was ever sent. v0.75.0 wired them, strictly opt-in and hardware-only, and the shipped wheel still sends nothing even when opted in, because its bundled project key is a placeholder the sender refuses. [What the payload would carry](/docs/tracker-eval-pro).

## See also

- [Eval-gated training](/docs/eval-gate) — halt a run mid-training on a quality regression; `soup ship` is the post-training counterpart.
- [Model report card (soup diagnose)](/docs/diagnose) — the seven-failure-mode x-ray that pairs with the verdict.
- [Soup Loop](/docs/soup-loop) — where the verdict slots into the traces → DPO → canary flywheel.
- [Lean install + live wiring (v0.71)](/docs/lean-install-live-wiring) — the release line `soup ship` caps off.

[PreviousBest-of-N & Evolve](/docs/best-of-n-evolve)[NextInference Server](/docs/serving)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="064-serving"></a>

# 64. Inference Server

*Source: <https://trysoup.dev/docs/serving>*

Deploy fine-tuned models as an OpenAI-compatible API server.

## Transformers Backend

```bash
pip install "soup-cli[serve]"
soup serve --model ./output --port 8000
```

Simple HTTP API using HuggingFace Transformers. Good for testing and low-traffic use.

## vLLM Backend (2-4x Faster)

> **Install `[serve-fast]` in a different environment from `[train]`.** Their resolutions are genuinely incompatible today: `pip install vllm` into a training environment silently downgrades `torch` and pushes `transformers` past the `<5.0.0` cap Soup's own metadata declares, producing an environment Soup calls unsupported with no warning at any point. Since v0.73.3, [`soup env check`](/docs/preflight-tooling) catches that after the fact, exit 3, without needing a lock file. Not creating it is cheaper.

```bash
pip install "soup-cli[serve-fast]"
soup serve --model ./output --backend vllm

# Multi-GPU with tensor parallelism
soup serve --model ./output --backend vllm --tensor-parallel 2

# Control GPU memory usage
soup serve --model ./output --backend vllm --gpu-memory 0.8

# Cap the context vLLM reserves KV cache for (v0.73.0, vLLM only)
soup serve --model ./output --backend vllm --max-model-len 8192
```

Recommended for production. Uses PagedAttention for high throughput. `--max-model-len` is the knob to reach for when vLLM refuses to start because the model's declared context window would need more KV cache than the card has: lower it and the engine reserves less.

## KV-cache type

The KV cache is usually the second-largest thing in VRAM while serving, after the weights, and it grows with context length rather than with model size.

```bash
soup serve --model ./output --kv-cache-type bf16   # or f16, q8_0, fp8
```

- `bf16` and `f16` set the cache dtype and need no extra dependency.
- `q8_0` is 8-bit quantized and needs `hqq` or `optimum-quanto`. Without one the command exits 2 with the install hint rather than falling back quietly.
- `fp8` is accepted by the config and **cannot be served today**: the transformers backend has no fp8 KV-cache path, and the vLLM / SGLang routing that would provide one is not wired, so it raises either way. The Hopper SM 9.0 check only picks which error you see.

**Transformers backend only.** Routing this flag through vLLM and SGLang is still open upstream, so do not assume it applies when you switch backend.

## SGLang Backend

```bash
pip install "soup-cli[sglang]"
soup serve --model ./output --backend sglang

# Multi-GPU
soup serve --model ./output --backend sglang --tensor-parallel 2
```

Alternative high-throughput backend with RadixAttention. It serves `/v1/chat/completions`, `/v1/models` and `/health`; the Anthropic-shaped `/v1/messages` endpoint is transformers-only.

**v0.74.0 ported the two vLLM repairs that were still standing here.** The prompt goes through the model's own chat template rather than a third hand-rolled copy, so a served model no longer sees a format it was never trained on, and `finish_reason` reports `length` on a truncated response instead of a hardcoded `stop`, on both the sync and streaming paths. Live verification against a real SGLang runtime on Linux is still an open follow-up.

> **Breaking in v0.74.0: this backend now obeys `--trust-remote-code`.** It had hardcoded it on at both runtime call sites, so a custom-code model executed its own repository code on this backend whether or not you opted in. The warning panel said so, but a notice is not a gate. A custom-code model now **fails to load** here without the flag, which is the same default-deny every other backend has had since v0.36. The same release also gave this backend the model's own chat template instead of a hand-rolled `User:`/`Assistant:` prompt, and a real `finish_reason` of `length` when a response hits `max_tokens` instead of a hardcoded `stop`.

## Binding to a non-loopback host (v0.74.0)

```bash
soup serve --model ./output --host 0.0.0.0 --tool-auth-token "$TOKEN"
```

**Without the token that command now exits 2**, where it used to print a warning and start anyway. The reason is that the endpoint the token protects changed underneath it: `/v1/tools/bash` was re-enabled behind real operating-system namespace and sandbox isolation, so it **actually executes code** now, and a warning is not a sufficient control over an executing endpoint reachable from the network. Where strict isolation is unavailable, Windows included, the endpoint fails closed with HTTP 501 rather than falling back to something weaker. It is not a filesystem sandbox, and the docs say so rather than implying one.

## Speculative decoding

```bash
# Transformers backend
soup serve --model ./output --speculative-decoding small-draft-model --num-speculative-tokens 5

# vLLM backend
soup serve --model ./output --backend vllm --speculative-decoding small-draft-model
```

A smaller draft model proposes tokens the target verifies in one pass, keeping the target's exact output. Whether that is actually faster depends on the pair, so measure it rather than assume: [`soup draft measure`](/docs/soup-draft) reports the real acceptance rate and plain-vs-assisted throughput, and on the pair we validated it came out at 0.55 to 0.64x, a net **slowdown**.

## Multi-Adapter Serving (v0.22.0+)

Serve multiple LoRA adapters on a single base model:

```bash
soup serve --model ./base --adapters chat=./adapters/chat --adapters code=./adapters/code
```

Switch adapters per request via the `model` field:

```json
{"model": "chat", "messages": [{"role": "user", "content": "Hello!"}]}
```

## API Endpoints

All backends expose the same OpenAI-compatible API:

- `POST /v1/chat/completions` — chat completions (streaming supported)
- `GET /v1/models` — list available models
- `GET /health` — health check

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "output",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

Compatible with OpenAI SDK:

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="unused")
response = client.chat.completions.create(
    model="output",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

> **Note:** `max_tokens` is capped at 16,384 per request. Error details are never exposed in HTTP responses.

[PreviousShip Verdict](/docs/soup-ship)[NextModel Export](/docs/export)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="065-export"></a>

# 65. Model Export

*Source: <https://trysoup.dev/docs/export>*

Export fine-tuned models to various formats for deployment.

## Merge LoRA Adapter

Merge a LoRA adapter with its base model into a standalone model:

```bash
# Auto-detect base model from adapter_config.json
soup merge --adapter ./output --output ./merged

# Specify base model and dtype
soup merge --adapter ./output --base meta-llama/Llama-3.1-8B --dtype bfloat16
```

## GGUF (llama.cpp / Ollama)

```bash
# Export LoRA adapter (auto-merges with base, then converts)
soup export --model ./output --format gguf --quant q4_k_m

# Different quantizations
soup export --model ./output --format gguf --quant q8_0
soup export --model ./output --format gguf --quant f16

# Export a full (already merged) model
soup export --model ./merged --format gguf
```

Supported quantizations: `q4_0`, `q4_k_m`, `q5_k_m`, `q8_0`, `f16`, `f32`

Use with Ollama:

```bash
echo 'FROM ./my-model.q4_k_m.gguf' > Modelfile
ollama create my-model -f Modelfile
ollama run my-model
```

## ONNX

```bash
pip install "soup-cli[onnx]"
soup export --model ./output --format onnx
soup export --model ./output --format onnx --output ./model_onnx
```

## TensorRT-LLM

```bash
pip install "soup-cli[tensorrt]"
soup export --model ./output --format tensorrt
soup export --model ./output --format tensorrt --output ./model_trt
```

> **This path now checks itself before it does any work, and on a current TensorRT-LLM it stops there (v0.74.0).** Soup shelled out to `python -m tensorrt_llm.commands.convert_checkpoint`, a module absent from every current TensorRT-LLM release: that package ships only `bench`, `build`, `eval`, `prune`, `refit` and `serve`, and checkpoint conversion now lives as a per-architecture `examples/<arch>/convert_checkpoint.py` script in NVIDIA's source tree instead. Before v0.74.0 the export **silently produced zero artifact bytes**; it now fails immediately with a message naming the missing entry point, before the LoRA merge and the output directory are touched. If you exported to TensorRT on an earlier release, check the directory actually holds an engine. Installing `tensorrt_llm` can also downgrade a training environment's `torch`, `transformers`, `numpy` and `datasets` pins, so keep it out of the environment you train in.

## AWQ Quantization (v0.23.0+)

```bash
pip install "soup-cli[awq]"
soup export --model ./output --format awq --calibration-data calib.jsonl
soup export --model ./output --format awq --calibration-data calib.jsonl --output ./model_awq
```

## GPTQ Quantization (v0.23.0+)

```bash
pip install "soup-cli[gptq]"
soup export --model ./output --format gptq --calibration-data calib.jsonl
soup export --model ./output --format gptq --calibration-data calib.jsonl --output ./model_gptq
```

`--bits` (4 or 8, default 4) and `--group-size` (default 128) set the AWQ and GPTQ quantization width, and they are what the output shard name records.

**`--calibration-data` is required for BOTH formats, and it arrived as a breaking change in each.** GPTQ first, in v0.74.0: the flagless form used to be accepted and then died inside auto-gptq with `object is not iterable`, because `quantize()` wants tokenized examples and was handed a bare tokenizer. AWQ followed in v0.75.0, for the opposite reason: AWQ \*did\* have a fallback, and that was the problem. A flagless AWQ export **silently downloaded AutoAWQ's large default calibration dataset**, so the calibration inputs behind a shipped artifact were whatever that download happened to contain. Both formats now refuse a missing or unusable JSONL **before** the quantizer is imported and before the model is loaded, so the refusal costs nothing. A file with zero usable samples is refused up front too, and `--calibration-samples` caps how many rows are read (default 128).

The same release repaired the exported directory. `save_quantized` writes its own `gptq_model-<bits>bit-<group>g.safetensors` shard, which `AutoModelForCausalLM.from_pretrained` does not look for, so a GPTQ export written before v0.74.0 does not reload by the standard path. The directory now also carries a standard `model.safetensors`.

## Deploy to Ollama (v0.18.0+)

Deploy a GGUF model directly to your local Ollama instance:

```bash
# Deploy a GGUF model
soup deploy ollama --model ./output/model.q4_k_m.gguf --name soup-my-model

# Deploy with system prompt and parameters
soup deploy ollama --model ./model.gguf --name soup-chat \
  --system "You are a helpful assistant." \
  --template chatml \
  --parameter temperature=0.7 \
  --parameter top_p=0.9

# Export + deploy in one command
soup export --model ./output --format gguf --deploy ollama

# List Soup-deployed models
soup deploy ollama --list

# Remove a model
soup deploy ollama --remove soup-my-model
```

Auto-detected chat templates: `chatml`, `llama`, `mistral`, `vicuna`, `zephyr` (or `auto` to infer from soup.yaml).

## Push to HuggingFace Hub

```bash
soup push --model ./output --repo your-username/my-model
soup push --model ./output --repo your-username/my-model --private
```

Auto-generates a model card with training details.

[PreviousInference Server](/docs/serving)[NextModel Registry](/docs/registry)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="066-registry"></a>

# 66. Model Registry

*Source: <https://trysoup.dev/docs/registry>*

v0.26.0 ships a local model registry at `~/.soup/registry.db`. Every fine-tune can be pushed, tagged, searched, diffed, and walked as a lineage DAG — entirely offline, no server, no cloud.

## Why a registry

Most people end up with 17 checkpoint directories called `output-3-final` and no idea which one won. The registry fixes that: one row per fine-tune, carrying config, eval baseline, and parent lineage.

## Push a run

```bash
# After training a model
soup registry push \
  --run-id run_20260420_143052_a1b2 \
  --name chat-llama \
  --tag v1 \
  --notes "Alpaca 15k, 2 epochs, lr=2e-4"
```

The registry derives lineage from the run's config (same base model, different run id); there is no `--parent` flag.

## List, show, search

```bash
# List everything
soup registry list

# Filter
soup registry list --name chat-llama
soup registry list --tag prod
soup registry list --base Qwen/Qwen3-8B --task sft

# Show details + lineage
soup registry show chat-llama@v1

# Search across name, base, task, notes
soup registry search "medical"
```

## Diff two versions

```bash
soup registry diff chat-llama@v1 chat-llama@v2
# training.lr:       2e-4 → 3e-4
# training.lora.r:   16   → 32
# eval.judge:        8.2  → 8.6  (+0.4)
# eval.mmlu:         64.3 → 65.1 (+0.8)
```

`soup registry diff` pretty-prints both config and eval delta between two entries.

## Promote to prod

```bash
soup registry promote chat-llama@v2 --tag prod
```

Tagging is how you mark stable versions. Any number of tags can point at the same entry.

## Lineage DAG

```bash
soup history chat-llama
# chat-llama
# ├── @v1  judge 8.2  mmlu 64.3%  (2026-04-18)
# │   ├── @v2  judge 8.6  mmlu 65.1%  (2026-04-19)
# │   │   └── @prod  ⭐
# │   └── @v1-rephrase  judge 8.3  mmlu 64.0%
# └── @baseline
```

Cycle detection is enforced on every walk — forking a descendant back onto an ancestor raises an error.

## Delete

```bash
soup registry delete chat-llama@v1 --yes
```

Delete cascades to children, but the confirmation prompt prints the subtree first.

## Use as an eval-gate baseline

The [eval gate](/docs/eval-gate) accepts `registry://<id>` as the baseline, so quality regressions are diffed against any historical run rather than a static file.

## Storage

- SQLite at `~/.soup/registry.db` — human-readable, portable
- Single writer, no daemon
- Name + tag are validated (ASCII, 64-char cap, no path separators)
- SQL LIKE-wildcard escaping on every search term

## See also

- [Eval gate](/docs/eval-gate) — baselines can point at registry entries
- [Soup Cans](/docs/soup-cans) — export a registry entry as a portable `.can`
- [CLI reference](/docs/cli-reference)

[PreviousModel Export](/docs/export)[NextHuggingFace Hub](/docs/hf-hub-integration)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="067-hf-hub-integration"></a>

# 67. HuggingFace Hub Deep Integration

*Source: <https://trysoup.dev/docs/hf-hub-integration>*

Soup v0.29.0 closes the loop between training and the Hub. Every checkpoint can auto-push as a branch, training can resume from the Hub after a crash, models deploy to a Gradio or Streamlit Space in one command, and self-hosted Hubs are supported via `HF_ENDPOINT`.

## Auto-push every checkpoint

```bash
soup train --push-as alpamys/chat-llama
```

Every `save_steps` checkpoint is uploaded to HuggingFace Hub as a `checkpoint-<N>` branch. The `main` branch is updated only at training completion. A sticky `_repo_failed` flag means push failures (bad token, rate limit) short-circuit subsequent saves — no log spam, no training crash.

The upload uses an explicit `allow_patterns` allowlist (`*.safetensors`, `*.bin`, `*.pt`, `*.json`, `tokenizer*`, `trainer_state.json`, `training_args.bin`, `README.md`) — an `output_dir` that overlaps with your project root cannot accidentally publish `.env` or source files.

## Resume from the Hub

```bash
soup train --push-as alpamys/chat-llama --hf-resume
```

`--hf-resume` pulls the latest `checkpoint-<N>` branch via `snapshot_download`, places it in `output_dir` (containment-checked against cwd), and resumes. `local_dir_use_symlinks=False` defeats symlink-based filesystem escapes on older `huggingface_hub` versions.

Use this when a spot GPU dies, a preemption kicks you off, or you want to migrate training between machines.

## HF Collections

```bash
soup push --model ./output \
  --repo alpamys/chat-llama \
  --collection alpamys/kazakh-llms-abc123
```

Adds the pushed repo to an existing HuggingFace Collection. The slug follows the `owner/slug-hash` regex; null bytes, whitespace, and `..` are rejected. Max 256 chars.

## Self-hosted Hub (`HF_ENDPOINT`)

```bash
HF_ENDPOINT=https://hf.internal.example.com soup train --push-as team/my-model
```

Every HF operation routes to your internal Hub. SSRF hardening:

- Scheme allowlist (http/https only)
- Plain HTTP permitted only for loopback (`localhost` / `127.0.0.1` / `::1`)
- `0.0.0.0` explicitly rejected
- Private / link-local / cloud-metadata IPs (RFC1918, 169.254.x) rejected via `ipaddress.ip_address`
- Null bytes rejected

## Publish datasets

```bash
soup data push --input data.jsonl --hf-dataset alpamys/kazakh-chat
```

Uploads a local JSONL as a HuggingFace dataset repo. Input path must stay under cwd, `repo_id` is validated, and a token is resolved via the unified `utils/hf.resolve_token` chain. Commit messages are stripped to the first line and capped at 200 chars to prevent multi-line injection into public HF commit history.

## Deploy to HF Spaces

```bash
soup deploy hf-space \
  --model alpamys/chat-llama \
  --space alpamys/chat-llama-demo \
  --template gradio-chat   # or: streamlit-chat
```

Creates a Space wrapping your fine-tuned model. `render_space_template` validates `model_repo` via `validate_repo_id` before substituting into `app.py` / `README.md` — a crafted repo id cannot inject Python code into the deployed Space.

## Model card v2

Generated READMEs now include:

- Training config: task, base model, learning rate, optimizer
- Optional eval scorecard from an `eval_results.json`
- HTML-escaped `data_lineage` parameter
- Markdown-active chars neutralized in task names and non-numeric score values (`|`, `[`, `]`, `(`, `)`, `!`, `<`, `>`, newlines, tabs) — no table-row / link / image / raw-HTML injection in the rendered README

## Token resolution

`utils/hf.resolve_token` is the single source of truth:

1. Env: `HF_TOKEN` or `HUGGINGFACE_HUB_TOKEN`
2. `~/.cache/huggingface/token`
3. `~/.huggingface/token`

Non-printable tokens are rejected. The legacy `soup push --token` flag now warns deprecated and delegates to this chain.

## `repo_id` validation

Applied to `soup push --repo`, `soup train --push-as`, `soup data push --hf-dataset`, `soup deploy hf-space --model/--space`:

- Alphanumeric + `._-` only
- Per-component ≤ 96 chars
- Total ≤ 200 chars
- Null-byte / whitespace / `..` / leading-`/` rejection

## License migration

As of v0.29.0, Soup is **Apache-2.0** (previously MIT). Downstream redistributors must retain the `NOTICE` file per §4(d).

## See also

- [Registry](/docs/registry) — track every pushed run locally
- [Eval-gated training](/docs/eval-gate) — catch regressions before pushing to the Hub
- [CLI reference](/docs/cli-reference)

[PreviousModel Registry](/docs/registry)[NextSmart Inference Server](/docs/speculative-decoding)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="068-speculative-decoding"></a>

# 68. Smart Inference Server (v0.30.0)

*Source: <https://trysoup.dev/docs/speculative-decoding>*

`soup serve` graduated from a basic OpenAI-compatible wrapper into a production-grade serving stack. Speculative decoding, prefix caching, structured output, dynamic LoRA hot-swap, a continuous-batching dashboard, and OpenTelemetry tracing all ship in v0.30.0.

## Speculative decoding

Use a smaller draft model to propose tokens the target verifies in one pass. Whether it is faster depends entirely on the pair: [`soup draft measure`](/docs/soup-draft) (v0.71.33) is how you find out before you enable it.

```bash
# Transformers backend — uses HF assisted generation
soup serve --model ./output --speculative-decoding small-draft-model --num-speculative-tokens 5

# vLLM backend — uses vLLM native speculative decoding
soup serve --model ./output --backend vllm --speculative-decoding small-draft-model

# Auto-pair: Soup picks the draft for you based on the target family
soup serve --model meta-llama/Llama-3.1-70B-Instruct --backend vllm --auto-spec
```

`--auto-spec` handles Llama 3.1 / 3.3 / 4, Qwen 2.5 / 3, Mistral Large, Mixtral, DeepSeek V3 / R1, and Gemma 2 / 3. Models without a known draft pairing print a yellow "no draft" note and fall back to standard decoding. A draft you trained yourself with [`soup draft distill`](/docs/soup-draft) is picked up **before** this built-in table.

> Before you enable any of this, measure it. [`soup draft measure`](/docs/soup-draft) (v0.71.33) reports the draft's real acceptance rate and plain-vs-assisted throughput on your own pair. On the pair we validated, assisted decoding came out at 0.55 to 0.64x, a net **slowdown**, so treat a speedup as something to verify rather than assume.

## Prefix caching (vLLM)

For RAG and agent workloads with a shared system prompt:

```bash
soup serve --model ./output --backend vllm --prefix-cache
```

The first request with a given prefix warms the cache; subsequent requests skip the shared prefix compute entirely.

## Structured output

Constrain output to a JSON schema or regex pattern.

```bash
# JSON schema (file must live under cwd)
soup serve --model ./output --structured-output json --json-schema product.json

# Regex (length-capped at 2048 chars, null bytes rejected)
soup serve --model ./output --structured-output regex --regex-pattern '\\d{3}-\\d{4}'
```

Schemas serialised over 64 KB are rejected. JSON schemas must declare a top-level `type` field. Constraints are validated at startup, not per-request.

## Dynamic LoRA hot-swap

Switch the active adapter at runtime without restarting the server.

```bash
soup serve --model base-model --adapters chat=./chat-adapter --adapters code=./code-adapter
```

```bash
curl -X POST http://localhost:8000/v1/adapters/activate/chat
# → {"active": "chat", "status": "ok"}

curl -X POST http://localhost:8000/v1/adapters/deactivate
# → {"active": null, "status": "ok"}

curl http://localhost:8000/v1/adapters
# → {"adapters": [{"name": "chat", "active": true}, ...], "active": "chat"}
```

Names match `^[a-zA-Z0-9][a-zA-Z0-9-]*$`. Activate/deactivate is thread-safe behind a lock.

## Continuous-batching dashboard + `/metrics`

```bash
soup serve --model ./output --dashboard
```

```bash
curl http://localhost:8000/metrics
# {
#   "requests_total": 1234,
#   "tokens_generated_total": 456789,
#   "active_requests": 3,
#   "latency_p50_ms": 185.2,
#   "latency_p95_ms": 720.0,
#   "latency_samples": 1000
# }
```

Latency percentiles are computed from the last 1000 requests; counters include failure paths so the dashboard reflects true reliability.

## OpenTelemetry tracing

Emit per-request spans to your OTLP collector.

```bash
pip install opentelemetry-sdk opentelemetry-exporter-otlp

soup serve --model ./output \
  --trace --trace-endpoint http://localhost:4317
```

OTLP endpoint hardening mirrors `HF_ENDPOINT`: scheme allowlist, plain HTTP only for loopback, RFC1918 / link-local / `0.0.0.0` rejected via `ipaddress.ip_address`. Missing SDK is a no-op with a warning.

### A local trace file, with no collector

If you do not want to stand up a collector to answer "what did it actually reply, and how slowly":

```bash
soup serve --model ./output --trace-log ./traces.jsonl --trace-log-cap-mb 100
```

One JSON object appended per chat completion, carrying `ts`, `prompt`, `response`, `latency_ms` and `tokens`. The path must stay under the working directory. It rotates at the cap (1 to 10000 MB, default 100) keeping one backup, and refuses to write through a symlink on the backup path.

**Secrets are redacted before the line is written**, not after: Hugging Face tokens, `sk-` keys and `Bearer` values are stripped, because a trace file is the most likely thing in a serving directory to get pasted into an issue. A write failure never takes down the request handler.

### Capturing thumbs from the served model

```bash
soup serve --model ./output --record-thumbs ./feedback.db
```

Turns on `POST /v1/thumbs` and writes into the same local SQLite that [`soup local-rl`](/docs/anti-trend-insurance) harvests, so a served model feeds the preference flywheel without anyone recording feedback by hand. Path contained under cwd, transformers backend only.

## DeepSpeed-MII backend

```bash
soup serve --model ./output --backend mii
```

Loopback-only CORS, `max_tokens` capped at 16384, streaming disabled (no SSE for MII v0.x). Pipeline crashes return generic 500 with no stack-trace leak.

## Auto-quant picker

```bash
soup serve --model ./output --auto-quant
```

The picker API is registered; live evaluation soft-falls-back to the highest-scored candidate so the server still binds when no candidate clears `min_score`.

[PreviousHuggingFace Hub](/docs/hf-hub-integration)[NextDraft & Spec Decoding](/docs/soup-draft)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="069-soup-draft"></a>

# 69. soup draft (v0.71.33)

*Source: <https://trysoup.dev/docs/soup-draft>*

Speculative decoding is sold as free speed: a small draft model proposes tokens, the big target verifies a whole batch of them in one pass, and you keep the target's exact output. The question nobody answers first is whether the draft would actually propose the tokens **your** model is about to emit. `soup draft measure` answers it before you ship, and on the pair we validated the honest answer was no.

## Measure first

```bash
soup draft measure --target my-tuned-model \
    --draft HuggingFaceTB/SmolLM2-135M-Instruct \
    --prompts prod-prompts.jsonl

# CI gate: exit 2 below the floor, plus a JSON report
soup draft measure ... --min-acceptance 0.6 -o report.json
```

It reports two things: the **acceptance rate** and **real plain-vs-assisted throughput** measured on your box, not estimated.

**Acceptance rate** is the fraction of the target's own greedy tokens the draft would have proposed correctly (teacher-forced argmax agreement, the metric the Medusa and EAGLE papers report). Higher is better; roughly, 70% and up is where speculative decoding starts paying for the draft's forward pass on realistic hardware. Exit codes are 0 = ok, 2 = below `--min-acceptance`, 1 = error, so CI can gate on it.

## Distil your own draft

```bash
soup draft distill --target my-tuned-model \
    --draft-base HuggingFaceTB/SmolLM2-135M-Instruct \
    --data traffic.jsonl -o draft/

soup serve --model my-tuned-model --auto-spec   # picks up ./draft
soup draft list
```

`distill` runs logit KD through the existing `task: distill` trainer and emits a **dense** model, because a PEFT adapter directory cannot be loaded as an `assistant_model`. **Before v0.73.3 `--steps N` delivered roughly N/4.44 optimiser steps**, silently: the epoch count that realised the request ignored both the validation split removing rows and gradient accumulation turning several micro-batches into one step. Epochs are now derived from the effective steps per epoch, the emitted config pins the run shape so the arithmetic and the trainer cannot drift, and the pre-flight prints the resolved step count before training starts. Flags: `--steps N` (training budget), `--device cpu`, `--force` (overwrite `-o`), `--plan-only` (render the config and exit).

A [`soup shrink`](/docs/soup-shrink) output makes a good draft base: it shares the target's tokenizer by construction.

## The local draft registry

`soup draft distill` registers the draft in `~/.soup/drafts.json`, and `soup serve --auto-spec` consults that registry **before** the built-in pairing table. A draft you trained yourself is therefore picked up automatically, with no flag to remember.

## Tokenizers: same by default, cross-tokenizer since v0.74.0

The reason the pair used to be refused is not pedantry: speculative decoding proposes **draft** token ids into the **target's** vocabulary, so a mismatched pair silently produces garbage instead of failing.

v0.74.0 opened the mismatched case on all three surfaces rather than removing the check. `soup draft distill` routes a mismatched pair through Universal Logit Distillation (`uld_strategy: wasserstein_aligned`) instead of refusing it; `soup draft measure` prints "Cross-tokenizer draft detected" and measures acceptance by aligning decoded character spans rather than token ids; and `soup serve --speculative-decoding` serves such a pair through Transformers Universal Assisted Decoding, raising a clear error when the installed `transformers` is too old for it. A same-tokenizer pair keeps the existing native fast path exactly as it was, which is the point: the slower alignment only runs where it has to.

> One caveat worth carrying: whether a cross-tokenizer draft **pays off** is a separate question from whether it runs, and the measured answer below is about a same-family pair. Measure before you enable it.

## Honesty: the measured result, including ours

The "~1.5 to 2x faster serving" pitch was **withdrawn, not shipped**. On `SmolLM2-360M-Instruct` (target) with a `SmolLM2-135M-Instruct` draft:

| Draft | Acceptance |
| --- | --- |
| Stock, no distillation | **69.3%** |
| Distilled, 2 epochs | 69.7% |
| Distilled, 10 epochs | **69.3%** |

Distillation bought nothing beyond noise. A small same-family draft is already near its capacity ceiling for agreeing with the target, and logit KD cannot buy capacity it does not have. Assisted decoding on that pair measured **0.55 to 0.64x**: a net **slowdown**, because the draft's forward pass costs more than the tokens it saves at this size.

So the feature ships as the honest gate rather than the speedup claim. `soup draft measure` correctly says "do not enable this" on that pair, and that is the point of shipping the measurement. Whether distillation materially raises acceptance for a genuinely diverged fine-tune, or a larger target and draft pair, is **unproven** on a 4 GB box and tracked as a scale issue. Run `soup draft measure` on **your** pair rather than assuming, including when the assumption comes from us.

> Acceptance is teacher-forced greedy agreement. It is exact, deterministic, and the right number for comparing drafts, but it is not the accepted-token count of a **sampling** run, which also depends on the rejection-resample cascade.

## See also

- [Smart Inference Server](/docs/speculative-decoding) — `--auto-spec`, the built-in pairing table, prefix cache.
- [soup shrink](/docs/soup-shrink) — depth-prune a model into a same-tokenizer draft base.
- [soup ship](/docs/soup-ship) — the other place Soup refuses to guess for you.

[PreviousSmart Inference Server](/docs/speculative-decoding)[NextQuant Menu](/docs/quant-menu)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="070-quant-menu"></a>

# 70. Quant Menu — 9 Quantization Formats (v0.38.0)

*Source: <https://trysoup.dev/docs/quant-menu>*

Pick the right quantization format for your base model and hardware. Soup loads the appropriate `quantization_config` and trains LoRA on top.

```yaml
# Train LoRA on top of a pre-quantized GPTQ checkpoint:
base: TheBloke/Llama-2-7B-Chat-GPTQ
training:
  quantization: gptq        # or: awq, hqq:4bit, aqlm, eetq, mxfp4, fp8

# FSDP + QLoRA — set quant_storage:
training:
  quantization: 4bit
  bnb_4bit_quant_storage: bfloat16
```

## What v0.74.0 changed for a 4-bit load

The fp32 finding is usually described in terms of a frozen base, which is a full-precision story. It reaches a **quantized** load too. A `quantization: 4bit` or `8bit` model still holds real modules outside the quantized linears, the embeddings, the norms and the LM head, and those were being materialised in fp32 for the same reason: no dtype was passed. They now follow the load dtype (`auto`, or an explicit fp16 on a pre-Ampere card), matching `bnb_4bit_compute_dtype` instead of sitting a precision above it. **Do not attach the release's 2.59x figure to this**: that number was measured on an unquantized frozen base with LoRA, and a 4-bit run was never paying the same bill.

## Format matrix

| Format | Bits | Use case | Optional dep |
| --- | --- | --- | --- |
| `4bit` | 4 | Default. Best general LoRA training. | bitsandbytes |
| `8bit` | 8 | Larger memory budget, more accurate gradients. | bitsandbytes |
| `none` | 16/32 | Full fine-tuning or DPO/PPO without quant. | — |
| `gptq` | 2/3/4/8 | Train LoRA on top of an existing GPTQ checkpoint. | gptqmodel |
| `awq` | 4 | Train LoRA on top of an existing AWQ checkpoint. | autoawq |
| `hqq:Nbit` | 1, 2, 3, 4, 5, 6, 8 | Wide bit range; compose with LoRA. | hqq |
| `aqlm` | 2 | Extreme compression. | aqlm |
| `eetq` | 8 | Fast 8-bit kernel for SM75+. | eetq |
| `mxfp4` | 4 | Newer 4-bit type with better activation distribution. | bitsandbytes ≥ 0.45 |
| `fp8` | — | Train fp16/bf16 on top of FP8-released checkpoints. | transformers ≥ 4.45 |

## Compatibility matrix

`soup train` runs `check_quant_distributed_compat()` at startup. HQQ / EETQ / AQLM hard-fail with FSDP and ZeRO-3; BNB 4-bit + FSDP is **resolved rather than warned about** since #350: `bnb_4bit_quant_storage` is set to the effective compute dtype before the model loads, and the adapter parameters are aligned to it before FSDP wraps them, which closes both halves of the old failure. Nothing is left for you to set by hand. The remaining combinations emits a yellow warning.

## Pre-quantized + QAT

`gptq` / `awq` / `hqq:*` / `aqlm` / `eetq` / `mxfp4` / `fp8` all carry their own scale; combining with `quantization_aware` (int8 QAT or `'fp8'`) is rejected at config-load.

## Scope

Wired into the SFT trainer + transformers backend in v0.38.0. Multi-trainer expansion landed in v0.40.5. MLX backend gets a distinct error message naming the actual reason.

[PreviousDraft & Spec Decoding](/docs/soup-draft)[NextQuant Menu II](/docs/quant-menu-ii)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="071-quant-menu-ii"></a>

# 71. Quant Menu II (v0.53.0)

*Source: <https://trysoup.dev/docs/quant-menu-ii>*

The full advanced-quantization surface. v0.53.0 shipped the closed allowlists and validators; v0.53.1 lit up every writer — 3-stage llama.cpp imatrix pipeline, TorchAO PTQ export, and single-shot BNB-4bit merge. See [v0.53.1 live writers](/docs/v053-live-writers) for the live-wiring detail.

## Unsloth Dynamic 2.0 GGUF ladder

14-entry closed allowlist:

`UD-Q8_K_XL · UD-Q6_K_XL · UD-Q5_K_XL · UD-Q4_K_XL · UD-Q3_K_XL · UD-Q2_K_XL · UD-IQ4_XS · UD-IQ3_M · UD-IQ3_XXS · UD-IQ2_M · UD-IQ2_XS · UD-IQ2_XXS · UD-IQ1_M · UD-IQ1_S`

`validate_ud_gguf_format` is case-insensitive with canonical normalisation.

```bash
soup export --format gguf-ud --gguf-flavour UD-Q4_K_XL --output ./model.gguf
```

## IQ + Apple/ARM GGUF flavours

- 12-entry IQ family (IQ1/2/3/4 — including IQ4\_NL non-linear)
- 10-entry Apple/ARM-friendly set (Q4\_0\_4\_4, Q4\_NL, Q5\_K\_M, etc.)

Both wrapped in `MappingProxyType` metadata.

## KV cache types

```yaml
training:
  kv_cache_type: fp8   # q8_0 | bf16 | f16 | fp8
```

FP8 is accepted by the schema and **unreachable at serve time**: the transformers backend has no fp8 KV-cache path and raises, and the vLLM / SGLang routing that would provide one is not wired, so it raises earlier still. The Hopper capability check only decides which of the two error messages you get; a Hopper card does not make it work today.

## FP8 attention, NVFP4, native unsloth\_bnb\_4bit

Three separate configs, because the requirements in those comments are enforced at config load and no single config satisfies all three.

```yaml
training:
  quantization_aware: fp8   # required, or fp8_attention is refused
  fp8_attention: true       # non-MLX only
```

```yaml
training:
  nvfp4: true               # CUDA + text only; Blackwell SM ≥ 12 (runtime check)
```

```yaml
backend: unsloth
training:
  quantization: 4bit
  unsloth_bnb_4bit: true    # both of the above are required
```

## LF / Axolotl parity

```yaml
training:
  quantization: 4bit
  bnb_4bit_use_double_quant: true   # explicit true requires quantization='4bit'
  quantize_ref_model: true          # extends quant to ref model (DPO/IPO/SimPO/ORPO/BCO/KTO/GRPO/PPO/preference)
  quantize_reward_model: true       # PPO + reward_model tasks
```

```yaml
training:
  quantization: 8bit
  llm_int8: true                    # asserts quantization='8bit', so it cannot
                                    # share a config with the 4-bit block above
```

> **`bnb_4bit_use_double_quant` was read by nothing until v0.73.3.** Every place Soup built a 4-bit config hardcoded double-quantization **on**, so setting the key to `false` changed your config fingerprint and changed nothing about the run. It is honoured now at the three call sites Soup owns: the resident loader, the layer-streaming path (which reads it once and hands the same value to both the sharder and the meta skeleton, so streamed-versus-resident bit-exactness cannot drift), and the 4-bit save path. Two things travel with that. The field is now **tri-state**: unset means the shipped default, which is double-quant on, so a config that never set it trains identically; only an explicit `true` triggers the "requires `quantization: 4bit`" refusal. And because the resolved config now carries the field, a previously-unset config shows a **one-time fingerprint drift** in `soup ship --evidence` provenance and `soup lock check` with the numerics unchanged. **The Unsloth loader cannot honour it** — `FastLanguageModel` builds its own quantization config internally with double-quant hardcoded on and exposes no override.

## Advanced save formats

```bash
soup merge --save-format 4bit          # | 4bit_forced
soup merge --save-format 4bit --no-double-quant   # v0.73.3; ignored for fp16
soup export --format torchao --quant-config quant.yaml
```

`save-format 4bit_forced` writes a single BNB-4bit merged checkpoint without a dequant / merge / requant cycle.

`--quant-config` accepts a closed TorchAO allowlist: `Int4WeightOnly` / `Int8DynActInt4` / `Float8DynActFloat8` / `NVFP4`.

## Stats

- Net **+157 tests** (7,453 → 7,610 across 179 files)
- 154 tests in `test_v0530.py`
- 5 review agents ran in parallel; every CRITICAL / HIGH / MEDIUM / LOW finding fixed or documented

## See also

- [Quant Menu (v0.38)](/docs/quant-menu) — the original 9-format menu
- [Speed & Memory](/docs/training-speed-memory) — FP8 training, Cut CE, kernel auto-compose
- [Multi-GPU](/docs/multi-gpu) — ZeRO++ / FSDP2 / pipeline

[PreviousQuant Menu](/docs/quant-menu)[NextModel Catalog](/docs/model-catalog-v051)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="072-model-catalog-v051"></a>

# 72. Model Catalog Expansion (v0.51.0)

*Source: <https://trysoup.dev/docs/model-catalog-v051>*

26 new recipes, catalog 80 → 106.

## New families

GPT-OSS 20B/120B, GLM 4.6 / 5, Kimi K2 / K2-Thinking, MiniMax M2, QwQ-32B, QVQ-72B, Granite 4, LFM2, Cogito v2, Mistral Small 3 / Medium 3.5, Magistral / Devstral / Ministral, MedGemma, EmbeddingGemma, LLaVA-Next, InternVL 3.5, Voxtral, Baichuan 2, Qwen-Image, DeepSeek-OCR, Paddle-OCR-VL.

```bash
soup recipes list
soup recipes search --task reasoning
soup recipes use qwq-32b-grpo
```

## MULTIPACK\_ARCHITECTURES: 18 → 38

The Multipack allowlist now spans 38 architectures — every model in the new catalog is packing-eligible where applicable.

## Alternative model hubs

```yaml
training:
  hub: modelscope   # hf | modelscope | modelers
```

Cross-validator rejects `hub != 'hf'` on `backend == 'mlx'`. `utils/hubs.py` exposes `validate_hub_name` / `validate_hub_endpoint` / `resolve_endpoint` / `default_endpoint` / `endpoint_env_var` / `required_hub_package` / `is_hf` with full SSRF parity to the v0.29.0 HF endpoint validator.

Live downloader / uploader wiring shipped in v0.53.10, and `soup data push --hub` in v0.71.5.

[PreviousQuant Menu II](/docs/quant-menu-ii)[NextExperiment Tracking](/docs/experiments)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="073-experiments"></a>

# 73. Experiment Tracking

*Source: <https://trysoup.dev/docs/experiments>*

Every `soup train` run is automatically tracked in a local SQLite database (`~/.soup/experiments.db`).

## List Runs

```bash
soup runs
```

Shows all training runs with task, model, status, and final loss. The run database at `~/.soup/experiments.db` is machine-wide, so this lists every run on the box; add `--cwd-only` to narrow it to runs whose `output_dir` sits under the current directory.

## Run Details

```bash
soup runs show run_20260223_143052_a1b2
```

Detailed info including config, metrics, and an ASCII loss curve.

### A run that is not running no longer says it is

Until v0.73.3 a run whose watcher process died was reported `running` **forever**, and the listing hardcoded that word for any row it could not otherwise classify. That trained you to ignore the one status field that guards against starting a second concurrent run.

Both `soup runs` and `soup runs show` now reconcile on read: a `running` row whose recorded process is gone is rewritten to **`terminated` with an unknown exit code**. Unknown, deliberately — a lost outcome is never recorded as a success — and the richer `completed` and `failed` statuses are left exactly as they are. Only runs recorded with a process id can be checked this way, so a run without one is left alone rather than guessed at.

On Windows this depended on a second fix, and it is a good example of a bug that cannot be reasoned around: the API that reports a process's exit code returns 259 for a process that is still alive, but **259 is also a perfectly legal exit code**, so a child that genuinely exited with 259 was indistinguishable from one still running. Liveness is now decided by waiting on the process handle with a zero timeout, which is signalled the instant the process exits whatever code it exits with.

## Compare Runs

```bash
soup runs compare run_1 run_2
```

Side-by-side comparison of two runs with loss curves and metrics.

## Delete Runs

```bash
soup runs delete run_1
```

## Reclaim disk without losing the run

Deleting a run is the blunt option. Checkpoints are what actually fill the disk, and most of that weight is optimizer state you will never load again.

```bash
soup runs clean run_1 --dry-run     # estimate the saving first, delete nothing
soup runs clean run_1               # surgical: drop optimizer states, keep the weights
soup runs clean --all               # every historical run
```

`--keep-weights` defaults to **on**, which is the whole design: it deletes `optimizer.pt` from the lesser checkpoints and leaves the model weights, so you can still evaluate or export from any of them. `--dry-run` estimates the saving without touching anything, and `--force` skips the confirmation for CI.

This matters more than it sounds at scale: a LoRA run training a fraction of a percent of the model can drag a checkpoint hundreds of times the size of the adapter it produced.

## Model Evaluation

Soup includes a comprehensive evaluation platform (v0.19.0+):

```bash
pip install "soup-cli[eval]"

# Run benchmarks (mmlu, gsm8k, hellaswag, etc.)
soup eval benchmark --model ./output --benchmarks mmlu,gsm8k

# Custom eval tasks from JSONL
soup eval custom --model ./output --tasks ./eval_tasks.jsonl

# LLM-as-a-judge evaluation
soup eval judge --target ./output --model gpt-4o --provider openai

# Auto-eval from soup.yaml config
soup eval auto --config soup.yaml

# Compare eval results between runs
soup eval compare run_1 run_2

# Local leaderboard across models
soup eval leaderboard

# Human A/B evaluation with Elo ratings
soup eval human --model-a ./model_v1 --model-b ./model_v2 --input ./prompts.jsonl
```

## Hyperparameter Sweep

Search for the best hyperparameters:

```bash
# Grid search
soup sweep --config soup.yaml --param lr=1e-5,2e-5,5e-5 --param lora_r=8,16,32

# Random search with max runs
soup sweep --config soup.yaml --param lr=1e-5,2e-5,5e-5 --strategy random --max-runs 5

# Preview without running
soup sweep --config soup.yaml --param lr=1e-5,2e-5 --dry-run

# Early stopping: skip remaining runs if loss exceeds 1.5x best
soup sweep --config soup.yaml --param lr=1e-5,2e-5,5e-5 --early-stop 1.5
```

## Model Comparison

Compare outputs of two models side-by-side:

```bash
soup diff --model-a ./model_v1 --model-b ./model_v2 --prompt "Explain gravity"
soup diff --model-a ./base --model-b ./finetuned --prompts test_prompts.jsonl
soup diff --model-a ./a --model-b ./b --prompts prompts.txt --output results.jsonl
```

## Batch Inference

Run a model on a list of prompts:

```bash
soup infer --model ./output --input prompts.jsonl --output results.jsonl
soup infer --model ./output --input prompts.txt --output results.jsonl \
  --max-tokens 512 --temperature 0.3
```

Output is JSONL with `prompt`, `response`, and `tokens_generated` fields.

## Training Profiler (v0.23.0+)

Estimate memory, speed, and GPU requirements before training:

```bash
soup profile --config soup.yaml            # model, task and quantization come from the config
```

Shows estimated GPU memory, training speed, and hardware recommendations.

## Adapter Management (v0.22.0+)

```bash
# Scan directory for LoRA adapters
soup adapters list ./experiments

# Show adapter metadata (base model, rank, size)
soup adapters info ./output

# Compare two adapters side-by-side
soup adapters compare ./adapter_v1 ./adapter_v2
```

## Logging Integrations

### TensorBoard

```bash
soup train --config soup.yaml --tensorboard
tensorboard --logdir ./output/runs/
```

### Weights & Biases

```bash
soup train --config soup.yaml --wandb
```

> `--tensorboard` and `--wandb` cannot be used together.

[PreviousModel Catalog](/docs/model-catalog-v051)[NextWeb UI](/docs/web-ui)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="074-web-ui"></a>

# 74. Web UI

*Source: <https://trysoup.dev/docs/web-ui>*

Soup includes a built-in web dashboard for managing experiments, training, and data.

## Launch

```bash
pip install "soup-cli[ui]"
soup ui
# Opens http://127.0.0.1:7860 in your browser
# Prints auth token to console
```

```bash
# Custom port, don't auto-open browser
soup ui --port 8080 --no-browser
```

## Pages

- **Dashboard** — view all experiment runs, loss charts, system info
- **New Training** — create configs from templates, validate, and start training
- **Data Explorer** — browse and inspect datasets (JSONL, JSON, CSV, Parquet)
- **Model Chat** — chat with a running `soup serve` inference server

## Security

The Web UI generates a random auth token at startup and prints it to the console. **Every private endpoint requires an `Authorization: Bearer <token>` header, not only the mutating ones.** Until v0.75.0 the read endpoints were open: run configurations, logs, system metrics and the event streams all answered without a token. Only `/` and `/api/health` stay open, so the dashboard can load.

**The streams authenticate differently, on purpose.** An SSE connection cannot carry a header the browser does not let you set, so instead of putting a durable token in a query string, the client exchanges one over an authenticated `POST` for a **short-lived, single-use ticket**.

**The interactive API docs are loopback-only.** `/openapi.json`, `/docs`, `/docs/oauth2-redirect` and `/redoc` serve on a loopback bind and are **absent, 404**, on any other, including `soup ui --public`. Upstream classifies that honestly as reconnaissance rather than disclosure: the schema exposes no run data, configuration or logs, but it does describe every route, parameter and request shape, and on a LAN bind that is free reconnaissance. They are **removed rather than gated** because `/docs` is a browser navigation that cannot attach a bearer header, so gating would have broken the page for a developer while leaving `/openapi.json` readable by any HTTP client. Read the schema from a loopback instance of the same version if you need it.

A non-loopback bind without a valid token **exits 2** rather than warning.

- CORS is restricted to the served origin (not wildcard)
- Data inspection is sandboxed to the working directory
- Config validation before writing
- HTTP error responses return generic messages (details logged server-side)

[PreviousExperiment Tracking](/docs/experiments)[NextSoup Cans](/docs/soup-cans)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="075-soup-cans"></a>

# 75. Soup Cans

*Source: <https://trysoup.dev/docs/soup-cans>*

A `.can` is a portable, verifiable recipe bundle — `tar.gz` of a manifest, the `soup.yaml`, and a `data_ref`. v0.26.0 ships `soup can pack / inspect / verify / fork` for sharing and forking fine-tunes without shipping checkpoints or training data directly.

## Pack

```bash
soup can pack \
  --entry-id chat-llama@v1 \
  --out chat-llama-v1.can
```

The pack includes:

- `manifest.json` — name, tag, parent, created-at, schema version
- `soup.yaml` — exact training config
- `data_ref.json` — a hash + URI pointing at the dataset (not the dataset itself)

## Inspect

```bash
soup can inspect chat-llama-v1.can
```

Prints manifest + config without extracting the archive.

## Verify

```bash
soup can verify chat-llama-v1.can
```

Checks schema version, manifest integrity, and whether the embedded `soup.yaml` still parses against the current Pydantic schema.

## Fork and modify

```bash
soup can fork chat-llama-v1.can \
  --out chat-llama-v2.can \
  --modify training.lr=3e-4 \
  --modify training.lora.r=32
```

Fork re-packs the archive with your overrides and a fresh manifest (new id, parent = original).

## Safety

Tar extraction is the classic attack surface. Soup Cans neutralize it:

- Rejects absolute paths and `..` traversal
- Rejects symlinks that point outside the extraction root
- 100 MB cap on archive size
- Format version was locked to `1` when this shipped. It is **3** at v0.74.0, and versions 1, 2 and 3 are all accepted on read; anything else is refused
- `dunder` keys (`__class__`, `__import__`, etc.) and null bytes are rejected in `fork --modify`
- Path containment uses shared `os.path.realpath + commonpath` so Windows short-name / junction tricks don't escape

## See also

- [Model registry](/docs/registry) — the source of truth that Cans export from
- [Configuration](/docs/configuration) — what lives inside a `.can`

[PreviousWeb UI](/docs/web-ui)[NextSoup Cans v2 + LR Finder](/docs/soup-cans-v2)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="076-soup-cans-v2"></a>

# 76. Soup Cans v2 + Live LR Finder (v0.33.0)

*Source: <https://trysoup.dev/docs/soup-cans-v2>*

v0.33 graduates several v0.27–v0.32 stubs into live functionality and ships meaningful follow-ups across the whole stack.

## Soup Cans v2 — `soup can run` + `soup can publish`

```bash
# Run a .can end-to-end: extract → train → optional deploy
soup can run my-recipe.can --yes
soup can run my-recipe.can --yes --deploy --env-capture env.txt

# Publish to HF Hub as a dataset
soup can publish my-recipe.can --hf-hub user/my-recipe
```

`soup can run` requires explicit `--yes` (mandatory consent — auto-downloads data + auto-trains). Manifest format bumped 1 → 2 (additive: new `deploy_targets` field). Both v1 and v2 cans still load.

**Security** — extract dir is containment-checked, GGUF rglob result for ollama deploy is realpath+commonpath checked against extract dir to prevent symlink escape, subprocess `TimeoutExpired` after 24h cap returns `rc=124` (coreutils convention). `soup can publish` validates `repo_id`, resolves the HF token via env / cache files, commit messages first-line + 200-char capped (matches v0.29 push policy).

## Live `--find-lr` training loop

The v0.32 stub curve is replaced with a real in-process LR-sweep training loop. NaN/Inf loss terminates the sweep early so `diverged_at` is honest. Falls back to a synthetic curve when prerequisites are missing (no torch / config load failure / dataset empty) so CI without GPUs still produces a parseable report.

```bash
soup train --config soup.yaml --find-lr --find-lr-output ./lr_finder.json
```

## Spike-recovery hint file

Loss-spike recovery now writes a `spike_recovery.json` hint with the decayed LR for re-launch:

```json
{"original_lr": 2e-4, "recovery_lr": 5e-5, "decay_factor": 0.25, "trigger_step": 482}
```

Live optimizer-state rewind and live DataLoader rebuild remain follow-ups (HF Trainer / TRL upstream constraints).

## VRAM grad-accum advisory (live)

When VRAM pressure crosses the threshold, the advisory now prints a concrete recommended `(batch, accum)` pair preserving effective batch:

```
[advisory] VRAM at 94% — try batch=2, accum=8 (preserves effective batch=16)
```

One-shot per run; doesn't fire when CUDA is unavailable.

## Auto-reexec under `accelerate`

`soup train --gpus N` now auto-reexecs under `accelerate launch` instead of just printing the command. Critical flags (`--fsdp`, `--deepspeed`, `--resume`, `--wandb`, `--tensorboard`, `--yes`) are forwarded as separate argv elements. Use `--no-reexec` to opt out and just print the command.

```bash
soup train --config soup.yaml --gpus 4               # auto-reexec
soup train --config soup.yaml --gpus 4 --no-reexec   # print command only
```

**Trust the printed command from v0.73.3 onward, and not before.** It used to be built from a second, hand-maintained list of "what the user typed", and that list was short, so flags fell off it silently: following the hint literally trained **without `--fsdp`**, and the run succeeded, which is why nothing ever pointed back at the hint. The printed copy was deleted rather than patched, and the hint is now derived from the same argv the auto-reexec would have used, so the two cannot drift again. Four more flags survive it now: `--name`, `--replay`, `--replay-ratio` and `--replay-seed`.

## Registry artifact attach

```bash
# Attach an eval JSON to an existing registry entry
soup eval custom --tasks evals/sanity.jsonl --model ./output \
  --attach-to-registry chat-llama@v1

# Auto-attach exported artifact to registry
soup export --model ./output --format gguf --registry-id chat-llama@v1
```

`eval_results` and `tensorrt` are now valid artifact kinds. `lookup_entry_by_output_dir` emits `ResourceWarning` when its 1000-row scan limit is hit (no silent miss).

## v0.28 features expanded to DPO + Pretrain trainers

`use_cut_ce`, `quantization_aware: "fp8"`, `kernel_auto_compose`, and `activation_offloading` now work on DPO and Pretrain trainers (in addition to SFT from v0.28). GRPO/KTO/ORPO/SimPO/IPO/PPO/RewardModel/Embedding still error at config-load with a precise multi-trainer message — full expansion arrives in v0.35.

## RLVR OS-level isolation

GRPO's `code_exec` reward gains real OS-level sandboxing on top of the v0.25 RLIMIT/socket-patch baseline:

- **Linux** — best-effort `os.unshare(CLONE_NEWUSER|CLONE_NEWNET|CLONE_NEWPID)`. Falls back silently to RLIMIT + socket-patch on hardened kernels (`unprivileged_userns_clone=0`).
- **macOS** — `sandbox-exec` wrapper with default-deny profile. `(allow mach-lookup)` narrowed to a 3-name allowlist (SecurityServer / notification\_center / opendirectoryd.libinfo) to prevent DNS/NSURLSession bypass.

## See also

- [Soup Cans](/docs/soup-cans) — pack, fork, run, publish
- [Training stability](/docs/training-stability) — LR finder + spike recovery
- [Multi-GPU](/docs/multi-gpu) — auto-reexec
- [Registry](/docs/registry) — artifact attach

[PreviousSoup Cans](/docs/soup-cans)[NextObservability & Dev UX](/docs/observability)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="077-observability"></a>

# 77. Observability & Dev UX (v0.34.0)

*Source: <https://trysoup.dev/docs/observability>*

Tools that explain \*why\* a run misbehaved instead of dumping a stack trace.

## `soup why`

Heuristic explainer — reads the most recent (or named) run and surfaces plain-English diagnoses with concrete next steps.

```bash
soup why                 # most recent run
soup why run_2026_abc    # specific run id (or prefix)
```

Detects: NaN/Inf loss, plateau (≥30 steps with <0.5% change), divergence (loss > 3× initial), persistent high gradient norm, learning rate outside the typical [1e-6, 5e-3] band. Pure rule-based — no model calls.

## `soup tui`

Full-screen Textual dashboard. Two-pane: run list (left) + selected-run detail (right). `r` refreshes, `q` quits.

```bash
pip install "soup-cli[tui]"
soup tui --refresh 1.0 --limit 50
```

## `soup train --profile`

Records a `torch.profiler` Chrome-trace over an early-steps window (default `wait=1, warmup=1, active=5, repeat=1`).

```bash
soup train --config soup.yaml --profile
# → ./output/profiles/<run_id>.trace.json
```

Open in `chrome://tracing` or Perfetto.

## Stopping and checkpointing a run that is already going

Two controls exist for the moment a run is live and you cannot restart it, and neither is a flag, which is why neither is findable by reading `--help`.

**Ctrl+C does not throw away the run.** The first `SIGINT` asks the trainer to **write a checkpoint and keep going**. A second one stops cleanly after that save completes. If no trainer state is wired up yet, the handler raises `KeyboardInterrupt` the ordinary way, so you can never be stuck in a process that refuses to die.

**A trigger file forces a save without touching the terminal:**

```bash
touch ./output/.checkpoint_now
```

The trainer polls between steps, saves on the next one, and then deletes the trigger, so it is a one-shot request rather than a mode. Useful when the run is in a scheduler, a container or someone else's tmux, and the loss curve just did something you want to keep.

## Crash bundles — `.crash` files

When training fails, Soup auto-writes a self-contained `.crash` JSON to `./.soup-crashes/crash_<utc>_<hex>.crash` containing:

- Redacted error trace
- Classified failure kind (`oom` / `nan` / `cuda` / `dataloader` / `nccl` / `other`)
- GPU state at crash time
- Env summary
- Last-50 metric rows
- Recursively-redacted config (`hf_*` / `sk-*` / `Bearer ...` tokens become `<redacted>`)

The output\_dir is reduced to `os.path.basename` so `$HOME` doesn't leak. Bundle truncated to 1 MB.

## Per-run cost

Every completed run stores an estimated cost (`$` per run) computed from the captured GPU device name and duration.

```bash
soup runs show <run_id>
# Cost: $4.21  Duration: 1h 38m  GPU: RTX 4090
```

CPU / MPS / unknown GPUs render `—` (no fabricated zeros).

```bash
soup cost --config soup.yaml             # estimate before training
soup cost --config soup.yaml --gpu H100  # specific GPU
```

## `soup runs replay`

```bash
soup runs replay <run_id>
```

Replay summary + downsampled loss curve from history (no live training restart).

## Global `--log-level`

```bash
soup --log-level verbose train --config soup.yaml
soup --log-level debug runs show <id>
```

Tiers: `quiet | normal | verbose | debug`. Wires a Rich-formatted logger on the `soup` namespace; `debug` enables timestamps + module paths.

[PreviousSoup Cans v2 + LR Finder](/docs/soup-cans-v2)[NextLive Dashboard](/docs/live-dashboard-ux)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="078-live-dashboard-ux"></a>

# 78. Live Dashboard & UX (v0.44.0)

*Source: <https://trysoup.dev/docs/live-dashboard-ux>*

21 cross-cutting UX features, +192 tests.

Highlights:

- Format-gate row helpers for the eval-gate dashboard
- HF resume checkpoint skipping optimization
- Polish across run cost, replay, profiling, and the Textual TUI

See [observability](/docs/observability) for `soup why` / `soup tui` / crash bundles.

[PreviousObservability & Dev UX](/docs/observability)[NextPlugin System & Ecosystem](/docs/plugins)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="079-plugins"></a>

# 79. Plugin System (v0.45.0)

*Source: <https://trysoup.dev/docs/plugins>*

5 parts, +169 tests. Public plugin / hook surface.

## BasePlugin Protocol

```python
from soup_cli.plugins import register_plugin

# The four hook names are fixed: pre_train, post_train, pre_step, post_step.
# Each takes one context dict and returns None. A plugin carries any
# subset of them; hooks are discovered by name, so a misspelled one is
# silently never called.
class MyTrainerPlugin:
    def pre_train(self, context): ...
    def post_step(self, context): ...

# Registration is what puts a plugin in the registry. Nothing is
# auto-discovered by subclassing: BasePlugin is a runtime-checkable
# Protocol, not a base class you inherit registration from.
register_plugin(
    name="my-trainer",          # kebab-case
    version="0.1.0",            # semver
    plugin=MyTrainerPlugin(),
    description="Example",
)
```

```bash
soup plugins list
soup plugins enable my-trainer
soup plugins disable my-trainer
```

**Registered plugins really run.** Every transformers-backend trainer attaches them as a genuine Hugging Face `TrainerCallback`, so `pre_train` / `post_train` / `pre_step` / `post_step` fire against the live training loop rather than being a surface waiting to be wired. Two deliberate properties: a hook that raises is swallowed at WARNING, so one misbehaving plugin cannot kill a multi-hour run, and the hook set is snapshotted when the callback is constructed, so registering a plugin mid-run does not retroactively receive events.

One thing that is **not** automatic: nothing under `soup_cli/plugins/` is auto-discovered at startup. A plugin exists once `register_plugin(...)` has been called in the process.

## OpenAI ↔ Anthropic Messages converter

`anthropic_messages.py` converts between OpenAI and Anthropic Messages schemas — useful for trace-to-preference + serve.

## Server-side tools allowlist

`server_tools.py` ships a server-side tools allowlist + `WebSearchConfig` for the inference server.

## N-gram speculative decoding

`ngram_spec.py` schema for n-gram speculative decoding; the serve path consumes it live.

## External integrations catalog

15-entry registry of known **deployment and serving targets** a trained model can be handed to, each with the artifact format it expects: LM Studio, ComfyUI, stable-diffusion.cpp, Open WebUI, Ollama, TEI, pgvector, FAISS, Weaviate and the rest. Not experiment trackers: W&B, MLflow, ClearML, Comet and Neptune are a separate allowlist, wired through `soup train --tracker`.

## Advanced trainer-plugin allowlist

Closed allowlist for advanced trainer plugins.

## Data Recipe DAG

`recipe_dag.py` parses a YAML DAG describing data preprocessing steps + dependencies. Topological sort guarantees deterministic execution order.

```bash
soup data recipe recipe.yaml
```

Validation is the default: the path is a positional argument and there is no `validate` subcommand. The live per-node runner shipped in v0.53.7 behind `--execute`.

[PreviousLive Dashboard](/docs/live-dashboard-ux)[Nextsoup adapters: git for LoRA](/docs/adapters)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="080-adapters"></a>

# 80. soup adapters— git for LoRA

*Source: <https://trysoup.dev/docs/adapters>*

After 6 weeks of running experiments you have 30 adapter folders and no idea which one to ship. `soup adapters` (v0.57.0, finished in v0.67.0) treats LoRA adapters as first-class versioned objects.

Ten subcommands across v0.57 + v0.67:

| Command | What it does | Shipped |
| --- | --- | --- |
| `soup adapters diff` | Per-layer Frobenius + relative drift + SVD effective rank | v0.57 |
| `soup adapters merge` | 5 strategies: linear / TIES / DARE / SVD / **CMA-ES** | v0.57 + v0.67 |
| `soup adapters blame` | Leave-one-out layer ablation planner | v0.57 |
| `soup adapters branch` | Name a LoRA config with SHA-pinned hashes | v0.57 |
| `soup adapters checkout` | Restore a branch; refuses on drift | v0.57 |
| `soup adapters branches` | List everything | v0.57 |
| `soup adapters pr` | GitHub-shaped PR markdown with eval-delta + sample diffs | **v0.67** |
| `soup adapters bisect` | Binary-search checkpoint history for regression boundary | **v0.67** |
| `soup lock write / show / check` | SHA256(base \ | \ | dataset \ | \ | env) closure, exit 3 on drift | **v0.67** |
| (v0.60 supply chain) | `scan` / `sign` / `verify` / `check-safetensors` | v0.60 |

All adapter math is **pure numpy, no torch**. `.bin` adapters are rejected with an actionable "re-save as safetensors" message. See [Adapter lifecycle (v0.67)](/docs/adapter-lifecycle) for the v0.67 surfaces.

## `soup adapters diff`

```bash
soup adapters diff adapter-a/ adapter-b/ --top-k 10 --format markdown
```

For each layer:

- Frobenius norm of the delta
- Relative drift (Frobenius / norm of a)
- **SVD effective rank** — `effective_rank(s) = exp(H(s²/Σs²))` where `H` is Shannon entropy. Tells you whether a high-rank adapter actually used its rank.

`--top-k` ranks layers by drift. `--format` accepts `table` / `json` / `markdown` and routes through `render_report_*`.

## `soup adapters merge` — 5 strategies

```bash
soup adapters merge a/ b/ c/ -o merged/ \
  --strategy ties --weights 0.4,0.3,0.3 --density 0.7 --seed 0

# v0.67 — evolutionary search over the simplex
soup adapters merge a/ b/ c/ -o merged/ \
  --strategy cmaes --eval ./suite.yaml --budget 1h
```

Strategies:

- **`linear`** — weighted average. Baseline.
- **`ties`** (Yadav et al. 2023) — trim by `density` → elect majority sign → disjoint average. Tied-sign defaults to `+1`.
- **`dare`** (Yu et al. 2024) — Bernoulli drop with `density`, rescale by `1/density`, deterministic via `--seed`.
- **`svd`** — linear-merge then low-rank SVD reconstruction (`--rank`).
- **`cmaes`** (v0.67, Sakana-style) — rank-mu CMA-ES (pure Python, no `cma` dep) over N-1 softmaxed logits on the simplex. Population [2..256], generations [1..10K], plateau-detects after 3 no-improvement gens. Eval-fn failures swallowed with sentinel score so one broken eval ≠ crashed run.

**Live as of v0.71.4** — `--canary <suite.json>` scores the merged adapter OK/MINOR/MAJOR via the Quant-Lobotomy taxonomy (`--strict-verdict` exits 2 on MAJOR), and `--strategy cmaes` runs the full evolutionary eval-suite loop (merge → materialise → score → write best). The backdoor-scan + license-conflict gates run for every strategy.

## `soup adapters blame` — leave-one-out planner

```bash
soup adapters blame adapter/ --dataset eval.jsonl --layer model.layers.* --budget 5m --shards 4
```

Plans which layer ablations to run within a wall-clock budget. `parse_budget` accepts `60s` / `5m` / `2h` (bounds `[60s, 24h]`). `_MIN_PER_SHARD_SECONDS = 30` checks feasibility — if the budget can't cover `shards × 30s` you get an actionable error. Returns a frozen `BlamePlan` with one `BlameShardWork` per shard.

Use `--plan-only` to see the plan without running anything. The live runner shipped in v0.66.0 with a DataInf-style influence-function approximation.

## `soup adapters branch` — named, SHA-pinned configs

```bash
soup adapters branch chat-llama-v3 -c soup.yaml --base meta-llama/Llama-3.1-8B --dataset data.jsonl
```

Records a frozen `Branch`:

```text
name              chat-llama-v3
config_path       soup.yaml
config_sha256     a3f1...
dataset_sha256    7c92...
base_model        meta-llama/Llama-3.1-8B
created_at        2026-05-15T23:14:02Z
soup_version      0.58.0
```

Branch-name regex: `^[A-Za-z0-9][A-Za-z0-9._\-]{0,127}$`. Config files capped at 1 MiB. Pointer file capped at 1,024 entries. Atomic write + POSIX `0o600`. `SOUP_BRANCHES_DIR` env override containment-checked to `$HOME` / `$CWD` / `$TMPDIR`.

## `soup adapters checkout` — drift-detecting restore

```bash
soup adapters checkout chat-llama-v3 -o restored-soup.yaml
```

Re-emits the locked config. **Refuses to restore on SHA mismatch** — if your `soup.yaml` or your dataset has changed since the branch was made, you get a hard error explaining what drifted. No silent stale restores.

## See also

- [Adapter algebra](/docs/adapter-arithmetic) — v0.71.34 adds `soup adapters arithmetic`: add, scale and negate LoRA deltas.
- [Registry](/docs/registry) — lineage DAG of full training runs
- [Soup Cans](/docs/soup-cans) — package an adapter + config + data ref into a portable bundle
- [Adapter lifecycle (v0.67)](/docs/adapter-lifecycle) — `soup adapters merge --strategy cmaes` evolutionary search, `soup adapters pr` GitHub-shaped reviews, `soup adapters bisect` regression history, and `soup lock` shared SHA256 closure
- [Supply-chain security (v0.60)](/docs/supply-chain-security) — `soup adapters scan / sign / verify` for backdoor detection + Merkle-root tamper protection

[PreviousPlugin System & Ecosystem](/docs/plugins)[Nextsoup loop: the production data flywheel](/docs/soup-loop)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="081-soup-loop"></a>

# 81. soup loop— the production data flywheel, all from the CLI

*Source: <https://trysoup.dev/docs/soup-loop>*

NVIDIA's data-flywheel reference needs a multi-service stack. Tracing and observability tools capture the traffic, but turning those traces into a training set, and the training set into a gated release, is a separate job they do not do. `soup loop` is that job in one command, offline.

`soup loop` (v0.58.0) ships it as **one CLI on a laptop**. It connects 8 of Soup's existing uniques — v0.26 Trace-to-Preference, v0.26 Eval-Gated Training, v0.26 Registry lineage, v0.26 Quant-Lobotomy verdicts, v0.26 Soup Cans, v0.25 Autopilot, v0.54 Advise, v0.55 Eval Design, v0.56 Diagnose — into a single loop:

> production traces → preference pairs → eval-gated DPO → canary deploy → auto-rollback

## Six subcommands

```bash
soup loop init  <served-model> --eval <suite> --baseline registry://<id> \
                --monthly-budget 50usd --max-runs-per-day 3
soup loop status
soup loop watch [--foreground|--detach] [--max-iterations N] [--poll-interval F]
soup loop pause / resume
soup loop canary <adapter> --traffic 5% [--autoroll-on-regress]
soup loop replay [<iteration-id>]
```

## Control plane

The full loop state lives in a single atomic file: `.soup/loop.yaml` (JSON-formatted via `tempfile.mkstemp + os.replace`, cwd-containment, direct `os.lstat` symlink rejection, 1 MiB cap, POSIX `0o600`).

Frozen `LoopState` schema:

- `served_model` / `eval_suite` / `baseline` / `status` (one of `{running, paused, stopped}`)
- 6 counters (`traces_harvested` / `pairs_distilled` / `runs_started` / `runs_shipped` / `runs_rolled_back` / `runs_skipped_by_budget`)
- canary + budget + daily-cap metadata
- iteration metadata

`to_dict` returns a `MappingProxyType` so callers can't mutate state through it. Only `with_status` and `bumped` are sanctioned mutators.

## Canary router

`soup loop canary <adapter> --traffic 5% --autoroll-on-regress` splits traffic via deterministic **SHA-256 hash routing**:

- 4-byte slice mod `_HASH_MOD = 10_000` → ±0.01% split granularity
- Per-request `route(policy, request_key)` is pure
- Verdict via `BucketStats.verdict()` returns `OK` / `MAJOR` / `UNKNOWN` using v0.26 Quant-Lobotomy thresholds (5-pct regression band, min 30 samples)
- `BucketStats` is mutable with `threading.Lock` for live request streams
- Cross-field validation: canary == stable rejected, `traffic_pct ∈ [0, 100]`
- `rollback` returns a new policy with the canary cleared (sticky-on-rollback)

## Budget guardrails

`parse_budget_string` accepts `"50usd"` / `"50"` / `"50 USD"` (≤ $1M hard cap). Each iteration runs through `check_budget` → frozen `BudgetDecision(proceed, reason, projected_total_usd, runs_today)`. Check order:

1. **daily-cap** (UTC-day rollover via `reset_daily_counter_if_new_day`)
2. **estimate-sanity** — refuse implausible cost estimates
3. **monthly-budget** — projected total vs configured cap

Budget-skipped iterations **produce no manifests** — no half-records to confuse `soup loop replay`.

## Watch daemon

`soup loop watch` orchestrates 5 stage callables: `HarvestFn` / `TrainFn` / `GateFn` / `DeployFn` / `CostFn`.

**You do not have to write those callables.** Since v0.71.4, `--pre-wired` binds real ones that compose the surfaces you already have: v0.26 trace-to-preference for the harvest, a `soup train` subprocess for the train, the v0.55 eval-gate for the gate, and the v0.30 `/v1/adapters/activate` hot-swap endpoint for the deploy. It is opt-in on both entry points, and `--pack-cans` additionally seals each iteration as a Soup Can.

```bash
soup loop init <served-model> --eval <suite> --baseline registry://<id> --pre-wired
soup loop watch --pre-wired --pack-cans
```

Two environment variables point the pre-wired stages at your own infrastructure: `SOUP_LOOP_TRACE_DIR` for where harvested traces live, and `SOUP_LOOP_SERVE_ENDPOINT` for the server to hot-swap against. Without `--pre-wired` the stage bindings are still no-op stubs, which is the shape the daemon shipped in at v0.58.

- `run_once(state, config)` is pure with respect to time (testable).
- `watch(config)` is the long-running daemon. Installs `SIGTERM` / `SIGINT` handlers.
- **Reloads state every iteration** so external `pause` / `resume` takes effect immediately without restarting the daemon.
- `--detach` spawns `python -m soup_cli.cli loop watch --foreground` via argv-list `subprocess.Popen` — no shell, no string interpolation.
- `maybe_rollback` fires only on `"MAJOR"` canary verdict.

## Iteration manifests

Every iteration writes a frozen `IterationRecord` to `.soup-loops/<iteration_id>/iteration.json`:

```text
iteration_id        20260515T231600-a1f3b2c4
started_at          2026-05-15T23:16:00Z
finished_at         2026-05-15T23:25:12Z
pairs_harvested     89
run_id              run-8f3
gate_verdict        OK            # OK | MAJOR | SKIPPED
canary_verdict      OK            # OK | MAJOR | UNKNOWN | None
shipped             true
rolled_back         false
estimated_cost_usd  2.40
notes               []
```

`new_iteration_id` = UTC timestamp + 8-hex `uuid.uuid4()`. `soup loop replay` walks the directory in chronological order.

## Known limitations

- Stage callbacks default to no-op stubs — live trace ingestion, registry baseline auto-pick, and `/v1/adapters/activate` rollout are operator-driven via `WatchConfig`. **Since closed in v0.71.4**: `--pre-wired` binds production stage callables, so the default is the only thing that is still a stub.
- `--detach` is a single-process subprocess; full daemonization (double-fork, session leader, /dev/null fds) is deferred.

## See also

- [Trace-to-preference](/docs/trace-to-preference) — the `HarvestFn` half of the loop
- [Eval-gated training](/docs/eval-gate) — the `GateFn` half
- [Registry](/docs/registry) — where `baseline` and shipped runs live
- [Diagnose](/docs/diagnose) — pair with `soup train --diagnose-gate` for a second safety net
- [Advise](/docs/advise) — what to run \*before\* a loop iteration
- [Trace ecosystem](/docs/trace-ecosystem) — v0.63 `soup ingest` feeds the loop's `HarvestFn`
- [Adapter lifecycle (v0.67)](/docs/adapter-lifecycle) — `soup lock` commits a SHA256(base \|\| dataset \|\| env) closure so the whole team coordinates on identical reproducible loop iterations; `soup adapters bisect` finds the broken iteration when the canary regresses
- [Pre-flight & tooling (v0.64)](/docs/preflight-tooling) — `soup plan` / `soup apply` drift-check the run plan before each loop iteration triggers a training

[Previoussoup adapters: git for LoRA](/docs/adapters)[NextAdapter Lifecycle](/docs/adapter-lifecycle)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="082-adapter-lifecycle"></a>

# 82. Adapter Lifecycle Finish (v0.67.0)

*Source: <https://trysoup.dev/docs/adapter-lifecycle>*

Six surfaces that complete what v0.57 `soup adapters` started. Adapters are now first-class versioned, collaborative, multi-tenant, evolvable, lockfile-tracked, bisect-able artifacts. We are not aware of a hosted vendor offering this set: evolutionary merge is mostly research demo, VeRA-style storage cuts against per-GPU-hour pricing, MoLE routing needs both a training and a serving stack, and adapter PRs need weights, eval and history together.

## CMA-ES merge — evolutionary search over LoRA weights

```bash
soup adapters merge ./lora_a ./lora_b ./lora_c --strategy cmaes \
  --eval ./suite.yaml --budget 1h --output ./merged
```

**Sakana-style evolutionary merge.** Pure-Python rank-mu CMA-ES (no `cma` dependency). Softmaxes N-1 logits onto the simplex, samples a population, keeps the elite half, plateau-detects after 3 generations without improvement (`converged=True`).

- 2..16 adapters; population `[2, 256]`; generations `[1, 10K]`
- Budget `[60s, 24h]` — reuses v0.57 `blame.parse_budget`
- Eval-fn failures swallowed with sentinel -1e9 score (one broken eval ≠ crashed run)
- **Live as of v0.71.4** — the full loop merges, materialises, and scores each candidate against the eval suite and writes the best-weighted merge; `--canary` adds an OK/MINOR/MAJOR verdict

## VeRA / VB-LoRA vector bank — multi-tenant adapter economics

```python
from soup_cli.utils.vector_bank import VectorBank, write_bank, estimate_bank_size

bank = VectorBank(
    name="customer-personalisation",
    base_model="meta-llama/Llama-3-8B",
    entries={"user_1": (0.31, -0.07, ...), "user_2": (...)},
)
write_bank(bank, "./bank.json")
# 128-D scaling vector at fp32 ≈ 512 bytes / user
# vs. ~30 MB per rank-16 LoRA on Llama-3-8B
```

**Shared random projection P (d\_model × d\_model) + per-user scaling vector v\_u.** Thousands of per-user adapters at MB-each instead of hundreds-of-MB per LoRA. Atomic JSON I/O + cwd containment + symlink rejection + 16 MiB cap.

`estimate_bank_size(num_users, vector_dim)` for sizing. **Live as of v0.71.12** — `soup serve --bank <bank.json> [--bank-strength S]` reconstructs the projection + per-user vectors and installs a decode-time hook; the active user is chosen per request via the `X-User-Id` header (unknown/absent id is a zero-delta no-op, so no cross-request leak).

## MoLE — per-token gating over task LoRAs

```yaml
# soup.yaml
task: moe_lora_routing
training:
  mole_task_adapters:        # the live form: paths to the frozen task LoRAs
    - ./adapters/coder
    - ./adapters/math
  mole_temperature: 1.0      # softmax sharpness
  mole_top_k: 2
```

**Mixture of LoRA Experts.** Gating network routes per-token activations to top-K task adapters via softmax over hidden state. Backend-cross-validator rejects `mlx`. **Live as of v0.71.12** — `mole_task_adapters: [...]` trains a real per-token gating network that blends N frozen task LoRAs (only the router trains); the gate is saved as `mole_gate.pt`.

## `soup adapters pr` — GitHub-shaped adapter pull requests

```bash
soup adapters pr "Better politeness on EU support tickets" \
  --base-sha 9f2e... --adapter ./candidate \
  --eval ./eval_delta.json --samples ./sample_diffs.json \
  --output ./PR.md
```

PR = `{base SHA, dataset diff, adapter weights, eval-delta report}` rendered as **review-friendly Markdown** with eval-delta table + per-sample baseline/candidate diffs:

| Metric | Baseline | Candidate | Δ |
| --- | --- | --- | --- |
| judge\_score | 7.4 | 8.2 | +0.8 |
| retry\_rate | 12.1% | 4.6% | -7.5% |

`_md_table_escape` neutralises the backtick, `|`, `\n`, `\r` and `\t` in operator-controlled cells. JSON output also available for v0.68 GitHub Action. Bounds: ≤64 deltas, ≤256 samples, ≤32 KiB per sample.

## `soup lock` — shared run lockfile

```bash
soup lock write --base-model meta-llama/Llama-3-8B \
  --base-sha <64hex> --dataset-sha <64hex> --env-hash <64hex> \
  --output soup.lock

soup lock show soup.lock
soup lock check --base-model ... --base-sha ... --dataset-sha ... --env-hash ...
# exit 3 on drift
```

Closure of `(base_model_sha, dataset_sha, env_hash)`:

```
closure_sha = SHA256(base_sha || dataset_sha || env_hash)
```

Commit `soup.lock` to git so the whole team coordinates on the same reproducible run. `soup_version` + `created_at` are **advisory only** — legitimate operator upgrades don't trigger drift. Composes with v0.64 `soup env lock` (provides env\_hash) and v0.64 `soup plan` (provides base/dataset hashes from config).

## `soup adapters bisect` — binary search over training history

```bash
soup adapters bisect ./ckpt-0500 ./ckpt-1000 ./ckpt-1500 ./ckpt-2000 \
  --eval-command "soup eval custom --model {ckpt} --tasks ./regression.jsonl"
```

Binary search over ordered checkpoint history. Operator supplies a shell **template** with `{ckpt}` placeholder — Soup uses `shlex.split` after `shlex.quote(ckpt)` (argv-list mode, **no `shell=True`**). Probes both endpoints first (short-circuits all-OK / all-broken), then ~log₂(n) midpoint probes. Exit 3 on `BROKEN_AT`.

Composes with v0.66 influence-blame: bisect finds the broken checkpoint, blame attributes it to specific training rows.

## Numbers

+165 tests in v0.67.0 (10,836 → **11,021**), 7 new test files. CMA-ES eval-wiring went live in v0.71.4, VeRA multi-tenant serve in v0.71.17, and the MoLE gating kernel in v0.71.12.

## See also

- [Adapter algebra (v0.71.34)](/docs/adapter-arithmetic) — task arithmetic over LoRA deltas, the newest member of this command family.
- [Adapters (v0.57)](/docs/adapters) — diff / merge / blame / branch / checkout, the foundation v0.67 builds on.
- [Post-train x-rays](/docs/post-train-xrays) — v0.66 blame is what `bisect` hands off to.
- [Pre-flight & tooling](/docs/preflight-tooling) — v0.64 `soup env lock` + `soup plan` are the inputs to `soup lock`.

[Previoussoup loop: the production data flywheel](/docs/soup-loop)[NextAdapter Algebra](/docs/adapter-arithmetic)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="083-adapter-arithmetic"></a>

# 83. Adapter algebra (v0.71.34)

*Source: <https://trysoup.dev/docs/adapter-arithmetic>*

`soup adapters arithmetic` applies task arithmetic ([arXiv:2212.04089](https://arxiv.org/abs/2212.04089)) to LoRA deltas. You **add** to blend two skills, **scale** to dial one down, and, the differentiator, **negate** to subtract one. The output is a single loadable adapter.

```bash
soup adapters arithmetic "coder + 0.5*math - toxic" \
    --adapter coder=./coder-lora \
    --adapter math=./math-lora \
    --adapter toxic=./toxic-lora \
    -o ./blended
```

Names in the expression map to adapter directories via the repeatable `--adapter name=path`. Exit 0 = ok, 1 = refusal.

## Why the coefficient math matters

A LoRA does not store its delta directly; it stores two factors whose product is the effective weight change, `ΔW = B @ A`. Scale both factors by a coefficient `c` and the delta scales by `c²`, which quietly breaks the whole idea: `- toxic` (c = -1) would square to +1 and become a **no-op** instead of a removal.

Soup splits the coefficient as the square root of its absolute value across the two factors and carries the sign, so the delta scales **linearly**: negation flips it, `0.5*` halves it, `2*` doubles it. The live check on two real rank-8 adapters: `||ΔW(2·a)|| / ||ΔW(a)|| = 2.000` exactly, where the old `c²` bug gives 4.0.

> Be precise about how far that exactness goes: it holds on the **self (diagonal) term**, so scaling or negating a **single** adapter is exact. A **multi-adapter sum** (like the example above) also carries **cross-terms** between the adapters, which this element-wise combine does not cancel.

## Mixed ranks are now exact (v0.72.0)

Mixed-rank inputs used to be **refused** with a "harmonize rank" message. As of **v0.72.0** they are handled **exactly**, not approximated.

The reason it is exact is structural rather than numerical. A LoRA delta is `ΔW = B @ A`, so stacking the `A` factors of the inputs on top of each other and the coefficient-scaled `B` factors side by side gives a single adapter whose product **is** the sum of the individual deltas, by construction. Concatenation loses nothing; there is no approximation step to be wrong about. The output simply carries the summed rank.

```bash
# rank-8 and rank-16 adapters in one expression: no longer a refusal
soup adapters arithmetic "coder + 0.5*math" \
  --adapter coder=./coder-r8 --adapter math=./math-r16 -o ./blended

# ask for a fixed output rank instead of the concatenated one
soup adapters arithmetic "coder + 0.5*math" \
  --adapter coder=./coder-r8 --adapter math=./math-r16 --rank 16 -o ./blended
```

`--rank N` truncates the concatenated result with an **SVD**, which is where an approximation does enter, deliberately and only when you ask for it: you are choosing a smaller adapter over an exact one. Without `--rank`, nothing is discarded.

Ranks are no longer a reason to refuse. Genuinely incompatible **layer shapes** still are.

## What it refuses

| Guard | Behaviour |
| --- | --- |
| Mixed ranks | Handled exactly by concatenation since v0.72.0; `--rank N` truncates with an SVD if you want a fixed output rank |
| Different base models | Refused; `--allow-cross-base` overrides |
| A FAIL-scanned input | Refused by the backdoor-scan gate; `--allow-unscanned` skips it |
| Paths outside the working dir, symlinks | Rejected |

The combine is signed and un-normalized. Same-rank inputs combine element-wise; mixed-rank inputs combine by concatenation, which is exact by construction (v0.72.0).

The expression parser is hand-written. There is no `eval`, so an adapter name can never become code.

## Honesty

What is proven is the **mechanism**: the delta really does negate, and the scaling ratio is exact to 2.000 on real adapters. What is **not** benchmarked is the behavioural outcome, so treat `- toxic` as "subtract that adapter's delta", not as a certified safety control. Whether subtracting a toxicity adapter measurably reduces toxicity on a real safety eval is an open question upstream calls proof-of-mechanism. Measure it on your own eval before you rely on it.

## See also

- [Adapter lifecycle](/docs/adapter-lifecycle) — diff, merge (linear / TIES / DARE / SVD / CMA-ES), bisect, PR, lock.
- [Adapters](/docs/adapters) — the git-for-LoRA surface this builds on.
- [Supply-chain security](/docs/supply-chain-security) — the backdoor scan the gate reuses.
- [LISA](/docs/lisa) — the other half of the v0.71.34 release.

[PreviousAdapter Lifecycle](/docs/adapter-lifecycle)[NextMCP Server](/docs/mcp-server)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="084-mcp-server"></a>

# 84. MCP server:soup mcp serve(v0.71.28)

*Source: <https://trysoup.dev/docs/mcp-server>*

**v0.71.28** ships a [Model Context Protocol](https://modelcontextprotocol.io) server, so you can drive Soup from any MCP client — **Claude Code, Cursor, Cline, Continue** — without leaving the chat. Your agent inspects a dataset, searches recipes, reads runs and gives a ship verdict as tool calls.

> No other fine-tuning CLI ships an MCP server.

## Start it

```bash
pip install "soup-cli[mcp]"    # official mcp SDK (mcp>=1.10.0,<3), lazy-imported
soup mcp serve                 # stdio; read-only tools
soup mcp serve --allow-mutating   # also run the 2 planning tools
soup mcp serve --allow-execute    # planning + real execution (v0.73.3)
```

Stdio is the default and is unchanged. **v0.74.0 added two network transports** for remote and multi-client setups, and they are covered in [network transports](#network-transports-v0-74-0) below.

### Execution (v0.73.3)

`--allow-execute` **implies `--allow-mutating`**, and its history is worth two sentences, because copy written about it ages badly. v0.73.2 added the flag as a **reserved gate that opened nothing**. **v0.73.3 opened it.**

```bash
soup mcp serve --allow-execute   # planning + real execution, behind a token
```

The server now carries **18 tools**, and a planned training or export can actually run. How that is gated is the whole design, and it is covered in [the execution model](#the-execution-model) below.

> **If you are auditing this against the binary, do not trust `--help` here.** At the v0.73.3 tag the help string for `--allow-execute`, the `--allow-mutating` help, and the server's own startup banner were all left behind by the feature commit and still say execution is disabled. The changelog, the command reference and the running code agree that it executes. This is the reverse of the usual rule, where the shipped binary settles a documentation disagreement.

**Nothing executes unless you pass the flag.** `--allow-mutating` on its own can never trigger a subprocess, and that is asserted in the code rather than assumed.

## Connect a client

Add Soup to your client's MCP config (`.mcp.json` for Claude Code, `claude_desktop_config.json` for Claude Desktop):

```json
{
  "mcpServers": {
    "soup": { "command": "soup", "args": ["mcp", "serve"] }
  }
}
```

To expose the planning tools, add the flag:

```json
{
  "mcpServers": {
    "soup": { "command": "soup", "args": ["mcp", "serve", "--allow-mutating"] }
  }
}
```

## The tools

The server exposes **18 tools total: 14 read-only + 2 planning + 2 executing**. It exposes MCP **Tools only** — no Resources, no Prompts. Every tool maps to a Soup command and returns JSON.

### 14 read-only tools (always available)

| Tool | Backing command | Returns |
| --- | --- | --- |
| `advise` | `soup advise` | PROMPT\_ENG / RAG / SFT / DPO / GRPO verdict for a dataset |
| `data_inspect` | `soup data inspect` | Row count, columns, length distribution, duplicates |
| `data_validate` | `soup data validate` | Format-compliance report (issues + valid-row count) |
| `data_score` | `soup data score` | Quality scorecard: PII, toxicity, language mix, educational value |
| `data_doctor` | `soup data doctor` | Chat-template compatibility vs a tokenizer (needs `[train]`) |
| `recipes_search` | `soup recipes search` | Search the catalog by keyword / task / size (no YAML body) |
| `recipes_show` | `soup recipes show` | A full recipe including the ready-to-use `soup.yaml` |
| `runs_list` | `soup runs` | Recent experiment runs from the local tracker |
| `runs_show` | `soup runs show` | One run's full record (accepts an id prefix) |
| `registry_list` | `soup registry list` | Registry entries, filterable by name/tag/base/task |
| `registry_show` | `soup registry show` | One entry by id / prefix / name:tag / `registry://` ref |
| `profile` | `soup profile` | Memory / speed / GPU-fit estimate from a `soup.yaml` (no model load) |
| `diagnose_evidence` | `soup diagnose --evidence` | Failure-mode report card from a pre-computed evidence JSON |
| `ship_evidence` | `soup ship --evidence` | SHIP / DON'T-SHIP verdict from a pre-computed evidence JSON |

### 2 planning tools (behind `--allow-mutating`)

| Tool | Backing command | Behaviour |
| --- | --- | --- |
| `train_start` | `soup train` | Validates a `soup.yaml`, returns `{config_valid, task, base, would_run, note}`. Never executes by itself |
| `export` | `soup export` | Validates the format, returns `{format, would_run, note}`. Never executes by itself |

Both are **always listed** but refuse to run unless you started the server with `--allow-mutating`, and even then they only **render the exact command that would run**. Calling them while disabled returns a clean `isError` telling you to restart with the flag.

Under `--allow-execute` they do one thing more: each returns a **`confirmation_token`** for the plan it just built. That token is the only way to reach the two tools below.

### 2 executing tools (behind `--allow-execute`, v0.73.3)

| Tool | Runs | Accepts |
| --- | --- | --- |
| `train_execute` | The training the matching `train_start` planned | `confirmation_token` and nothing else |
| `export_execute` | The export the matching `export` planned | `confirmation_token` and nothing else |

Both are always listed, carry a destructive annotation, and refuse unless the server was started with `--allow-execute`. They return `{run_id, status, pid, log_path}`.

## The execution model

The interesting property is what the client is **not** allowed to send. There is no command parameter, no argv, no shell string, and no environment: the argv was built server-side at plan time, and the only thing a caller can do is name a plan it already made.

- **The token is server-generated**, random, bound to **both** the plan and the execution kind, single-use, and expires after five minutes. A token from a `train_start` cannot run an export.
- **The config is snapshotted at plan time** and the run executes from that copy, so the file cannot be edited underneath a plan that was already approved.
- **Protected inputs are re-validated by content, not by timestamp.** The digest walks a directory tree by sorted relative path and per-file hash, refusing symlinks and bounded in both file count and bytes. The earlier mtime-and-size check did not change when a file \*inside\* a protected directory was rewritten, which meant a model could be swapped between planning and execution and still pass.
- **The process is spawned with `shell=False` and `stdin` closed**, its working directory pinned to where the server started, and its output redirected to `.soup/mcp-runs/<run_id>.log`.
- **The token is consumed, and capacity taken, before the process is spawned.** A failed spawn therefore requires a fresh plan rather than allowing a replay.
- **One execution at a time**, gated on a persisted run whose recorded process is still alive. That survives a restart: a live child from a previous server blocks a new run, while a stale record whose process is gone frees the slot instead of wedging it shut.
- **The run goes through the normal experiment tracker**, so `soup runs` sees what MCP started.

What it does **not** do: the snapshot freezes the configuration, not external filesystem assets, and a launch is fire-and-forget, so disconnecting your MCP client does not stop a subprocess that is already running.

## Security model

Every point below is implemented and tested:

- **No listener unless you ask for one** — stdio is the default and opens no port. stdout is reserved for the JSON-RPC channel; all human-facing text goes to stderr, and handler stdout is redirected so a stray `print()` can't corrupt the stream. A network transport is opt-in and carries its own mandatory bearer gate, below.
- **Path containment** — every path argument re-enters cwd-containment + symlink rejection (`O_NOFOLLOW` + fstat TOCTOU defence on reads).
- **Output sanitization** — C0/ESC/DEL bytes are recursively stripped from every returned string (tab/newline/CR kept), so a malicious dataset string can't smuggle ANSI/OSC terminal escapes into your client.
- **Path-free errors** — a failing handler becomes a clean `isError` result; no filesystem path or stack trace leaks, and the server survives.
- **Bounds** — string args ≤ 4096 chars, JSON args ≤ 16 MiB, dataset loads ≤ 1 GiB, int args range-checked (rejected, not silently clamped).
- **Execution is default-off and separately gated** — `--allow-mutating` alone can never spawn a process. With `--allow-execute` on, authorization is a server-issued one-time token: any client confirmation prompt you see is presentation, and the security lives entirely in the server-side token state.

## Install note

The `[mcp]` extra pulls one dependency, `mcp>=1.10.0,<3` (the official MCP Python SDK), and is **lazy-imported** — only the server module touches it, so the core CLI and the tool registry stay PyTorch-free and SDK-free. If you run `soup mcp serve` without the extra, you get a friendly one-line install hint and exit 1. The extra is also folded into `[all]` and `[dev]`.

**The bounds moved in v0.74.0.** The floor rose from `1.2.0` to `1.10.0`, measured against published wheels rather than a changelog: the transport-security module a listener depends on first appears there, and a listener whose origin checking silently disappears on an older SDK is worse than a resolver error. The `<2` cap, added when the SDK's 2.0.0 removed two APIs the server round-trips through, is **lifted**: both majors are bridged, chosen by probing the server constructor rather than by reading a version string, with a test that walks the syntax tree to enforce that and another that fails if a second dispatch implementation appears.

## Network transports (v0.74.0)

Until v0.74.0 the server was **stdio only**, which suits a client that spawns Soup as a subprocess and leaves remote or multi-client setups with nothing.

```bash
soup mcp serve --transport sse --host 127.0.0.1 --port 8765 --auth-token "$TOKEN"
soup mcp serve --transport http --host 127.0.0.1 --port 8765 --auth-token "$TOKEN"
```

Both serve the **same registry** as stdio, and the end-to-end test compares advertised tool names against the registry rather than a hardcoded count, so a subset cannot creep in.

Adding a listener is the risky part, so it is gated three ways.

| Gate | What it does | Why it is not optional |
| --- | --- | --- |
| **Bearer token** | Every request needs `Authorization: Bearer <token>`, compared in constant time. Header only, never a query string | A loopback port is reachable by every process on the box, so there is no opt-out. Header-only means it cannot land in an access log. The token format is validated by the same helper `soup ui` uses, rather than growing a second format |
| **DNS-rebinding protection** | `421` on a foreign `Host`, `403` on a foreign `Origin` | This is the gate a token cannot be: a page the operator merely visits sends no `Authorization` header, and its request still reaches the port |
| **Bind warnings** | Binding off loopback warns; a wildcard bind warns again | With a wildcard bind the `Host` check has nothing left to pin |

**`--allow-execute` is refused with either network transport.** The refusal is made twice on purpose, once in the command so the operator gets a readable message and once in the app factory so a direct caller cannot put an executing registry behind a listener either. The reasoning is stated rather than assumed: gated execution spawns real training and export processes, and behind a listener a leaked bearer token would mean process execution rather than plan disclosure, while stdio is a pipe to a client the operator already started.

`--host`, `--port` and `--auth-token` are **refused under `--transport stdio`** rather than silently ignored.

One operational addition rides along: a crash between spawning a training job and recording its process id used to let a restart double-book a second job, so an unresolved launch now counts as active, and `soup mcp runs reconcile --expunge-launching` recovers capacity from stale rows without editing the database by hand. It refuses the whole operation if any candidate records a process that is still alive.

## See also

- [v0.74.0: loaded in fp32](/docs/loaded-in-fp32) — the release that added the network transports.
- [v0.73.3: four flags that did nothing](/docs/flags-that-did-nothing) — the release that opened the execution gate.
- [Fine-tune Doctor](/docs/fine-tune-doctor) — `data_doctor` is one of the read-only tools here.
- [soup ship](/docs/soup-ship) — `ship_evidence` gives the SHIP / DON'T-SHIP verdict as a tool call.
- [advise](/docs/advise) / [diagnose](/docs/diagnose) — the decide-and-report tools your agent can call directly.

[PreviousAdapter Algebra](/docs/adapter-arithmetic)[NextCorrectness First](/docs/correctness-first)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="085-correctness-first"></a>

# 85. Correctness First (v0.36.0)

*Source: <https://trysoup.dev/docs/correctness-first>*

Four silent-failure modes Soup had → loud failures.

## Assistant-only loss masking

By default, Soup masks every non-assistant token with `-100` so the SFT loss reflects only what the model should \*generate\*. Toggle via `data.train_on_responses_only` (default `true`):

```yaml
data:
  train: data.jsonl
  train_on_responses_only: true   # default
  # OR per-message control:
  # train_on_messages_with_train_field: true
```

When the tokenizer ships a chat template with `{% generation %}` markers, the mask is exact. Without those markers, Soup falls back to an incremental tokenize-delta walk and documents the looseness.

> **If you trained with this before v0.73.3, re-run it.** A tokenizer returns a mapping object that is **not** a `dict`, and a type guard missed that, so the label mask was built from the mapping's **key strings** rather than from its token ids. There was no exception and no warning: the loss curve looked entirely normal, and the run trained on **zero tokens**. Token ids are now read through `input_ids` and normalised to plain integers before they reach the collator, and a missing or non-integer id fails loudly instead of producing a garbage mask. Separately, a template that reports an all-zero assistant mask while assistant messages plainly exist now falls back to the incremental walk, rather than shipping an all-`-100` no-op. The same assumption was removed from [`soup data doctor`](/docs/fine-tune-doctor), which had inherited it.

## `--trust-remote-code` opt-in

**Thirteen command modules** require `--trust-remote-code` to load any HF model that ships custom Python (`auto_map` in `config.json`): `train`, `chat`, `serve`, `infer`, `diff`, `merge`, `export`, `shrink`, `draft`, `generate`, and the `data`, `data doctor` and `eval` groups. The default is deny, everywhere.

```bash
soup train --config soup.yaml --trust-remote-code
```

First-party orgs (Meta, Mistral, Qwen, Google, etc. — 15 in the allowlist) suppress the warning panel; everything else prints a `REMOTE CODE WARNING` panel before loading.

## Chat-template hardening

Tokenizers without a chat template now raise a `ValueError` with a fix suggestion instead of silently building garbage `f"{role}: {content}"` strings.

```yaml
data:
  train: data.jsonl
  chat_template: chatml   # or: llama3, qwen2.5, mistral, gemma3, phi4, deepseek-r1, or a raw Jinja string
```

Raw Jinja strings are validated: null bytes, >64 KB, and filesystem-touching directives (`{% include %}`, `{% import %}`, `{% from %}`, `{% macro %}`, `{% extends %}`) are rejected at config-load.

## OOM-probe auto batch size

```yaml
training:
  batch_size: auto                  # unchanged
  auto_batch_size_strategy: probe   # NEW: 'static' | 'probe' | 'auto' (default)
```

Replaces the static memory formula with a real try-halve-then-double-to-ceiling loop.

> **The fit criterion changed in v0.74.0, and it matters most on Windows.** Until then the probe's only test was "the synthetic step did not raise". Under the WDDM driver, which is native Windows and WSL2, the allocator does not raise on an over-commit: it spills into host memory. So a batch that ran an order of magnitude slower in shared memory was approved **and cached**. The probe now reads `max_memory_allocated` after the step and refuses anything above what the process can actually reach on the device, and the cache key carries a version tag so entries written by the old probe are ignored rather than trusted. If you used `batch_size: auto` on Windows or WSL2 before v0.74.0, the cached size may never have been a fit.

Picked size is cached at `~/.soup/batch_cache.json` keyed on `(model, max_length, quantization, lora_r, gpu_name, gpu_memory_gb)` so repeat runs short-circuit. Cache file gets best-effort `0o600` perms after atomic rename.

[PreviousMCP Server](/docs/mcp-server)[NextGovernance, BOM & SLSA-3 attestations](/docs/governance)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="086-governance"></a>

# 86. Governance & Provenance (v0.59.0)

*Source: <https://trysoup.dev/docs/governance>*

Procurement-ready ML compliance from a single CLI. v0.59 ships 4 governance surfaces that previously required a stack of SaaS tools and a security team: CycloneDX/SPDX BOM emitter, in-toto / SLSA-3 attestation, HIPAA / SOC2 audit log, and EU AI Act Annex XI/XII auto-documentation.

## `soup bom emit` — ML Bill of Materials

Generates machine-learning Bills of Material in **CycloneDX 1.6** (with ML-BOM extension) or **SPDX 2.3** AI-profile formats — or both in a single invocation.

```bash
soup bom emit \
  --name llama3-8b-finetuned --version 1.0.0 \
  --base-model meta-llama/Llama-3.1-8B-Instruct \
  --base-sha abc123...def456 \
  --config-sha 789def...012abc \
  --data-sha 456ghi...789jkl \
  --task sft --license apache-2.0 \
  --format both --output ./manifests/llama3-bom
```

Atomic file write (`tempfile.mkstemp` + `os.replace`) with symlink rejection (TOCTOU defense). `--format=both` produces `<prefix>.cdx.json` and `<prefix>.spdx.json` side by side.

**Since v0.73.3, `--attach-to-registry <id>` registers what it wrote as a `bom` artifact on that entry**, so [`soup card`](/docs/compliance-pack) links it in the card's artifact table for free. Those were the two compliance documents `soup card` existed to publish and could not reach, because the registry had no such artifact kinds. The flag needs `--output` (omitting it is a usage error, exit 2), and a lookup or attachment failure exits non-zero **after leaving the emitted files on disk**. With `--format both`, both files are attached.

## `soup attest emit` — SLSA-3 in-toto attestations

Per-stage attestation aligned with **SLSA-3** (Supply-chain Levels for Software Artifacts) and in-toto.

```bash
soup attest emit --stage train \
  --subject adapter.safetensors --sha abc123...xyz789 \
  --builder soup-cli \
  --invocation "soup train --config soup.yaml" \
  --sign unsigned --output ./attestations/train.json
```

`--attach-to-registry <id>` works here too, as an `attestation` artifact, and a signed statement attaches its detached `.sig` sidecar alongside, so the card links every file a verifier needs (v0.73.3).

Stages: `extract` / `train` / `eval` / `export` / `publish`. Backends: `unsigned` (default — tamper-detectable via SHA-256); `ed25519` is **live as of v0.71.2** (`[sign]` extra; `soup attest verify <statement> --signature <sig>` does a canonical-JSON cryptographic verify). Sigstore keyless stays infra-blocked (needs an OIDC provider + Fulcio/Rekor).

## `soup audit-log` — HIPAA/SOC2 audit trail

Every command execution records timestamp, command-line, exit code, operator identity, and host into `~/.soup/audit.jsonl` (or `$SOUP_AUDIT_LOG_PATH`). PII fields are redacted before write.

```bash
# Tail the most recent 100 records (rich table)
soup audit-log tail --limit 100

# Raw JSONL for piping
soup audit-log tail --limit 50 --json

# Rotate at a 500 MB cap
soup audit-log rotate --cap-mb 500
```

### Turning it off

It is on by default for every command, so the opt-out belongs next to the feature rather than three pages away:

```bash
soup --no-audit-log train --config soup.yaml   # global flag, before the subcommand
SOUP_NO_AUDIT_LOG=1 soup train --config soup.yaml
```

Both suppress the one-line record entirely. `$SOUP_AUDIT_LOG_PATH` is the third control, and it moves the file rather than silencing it, which is what you want when the default location is the problem and the record is not.

## EU AI Act Annex XI/XII

`soup train` ships two new flags that emit the documentation required by the EU AI Act:

```bash
soup train --config soup.yaml \
  --annex-xi ./docs/annex-xi.md \
  --repro-receipt ./receipts/repro.json
```

The reproducibility receipt captures every seed, kernel version, library version, and dataset hash needed to reproduce the run under SR 11-7 model-risk-management standards.

## CO₂ energy tracking schema

Energy is tracked by the CLI, not by a config block: `soup train --track-energy` (with `--energy-country`) records consumption **offline** via codecarbon, and `soup bom emit --energy` folds the measurement into the BOM and the Annex XI doc. There is no `co2:` key in `soup.yaml`, and no live grid-intensity lookup.

## Numbers

+93 new tests in v0.59.0 (9193 → 9286).

## See also

- [Compliance pack](/docs/compliance-pack) — v0.71.35 wraps these commands into a regime-shaped workflow (`soup init --template`, `soup card`, `soup ci init`).
- [Supply-chain security](/docs/supply-chain-security) — v0.60 LoRA backdoor scanner, Merkle signing, air-gap bundles.
- [Registry](/docs/registry) — every BOM and attestation can be attached as an artifact.
- [Pre-flight & tooling (v0.64)](/docs/preflight-tooling) — `soup license-advisor --target b2c|defense|embedded` returns ok/warn/block per (license, deploy-target, MAU) and composes with the v0.59 license-matrix on `soup adapters merge`.
- [Adapter lifecycle (v0.67)](/docs/adapter-lifecycle) — `soup lock` SHA256(base \|\| dataset \|\| env) closure makes governance artifacts reproducible across teams.

[PreviousCorrectness First](/docs/correctness-first)[NextSupply-chain Security](/docs/supply-chain-security)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="087-supply-chain-security"></a>

# 87. Supply Chain Security (v0.60.0)

*Source: <https://trysoup.dev/docs/supply-chain-security>*

"Tensors you can ship through procurement." v0.60 layers 6 supply-chain controls on top of LoRA adapters so a security team can clear shipped weights for production.

## `soup adapters scan` — spectral backdoor detector

Pure-numpy spectral analysis of LoRA weight matrices. Flags four patterns associated with weight-space trojans:

| Pattern | Warn | Fail |
| --- | --- | --- |
| Rank-1 dominance | 50× | 200× |
| Top singular value / energy | > 75% | > 95% |
| Frobenius outlier (σ) | > 4σ | > 8σ |
| NaN / Inf | — | any |

```bash
soup adapters scan ./my_adapter --format json | jq '.overall'
# "OK" | "WARN" | "FAIL"
```

Exit codes: `0 = OK`, `1 = WARN` (advisory), `3 = FAIL` (CI gate).

## `soup adapters sign` / `verify` — Merkle-root tamper detection

```bash
soup adapters sign ./my_adapter --backend unsigned
# → ./my_adapter/.soup-signature.json

soup adapters verify ./my_adapter            # exit 1 on mismatch (lenient)
soup adapters verify ./my_adapter --strict   # exit 3 on mismatch (CI-strict)
```

The `unsigned` backend (default) computes a Merkle root over all adapter files for offline SHA-256 verification. `ed25519` is **live as of v0.71.2** — `soup adapters sign --backend ed25519 --key <priv.pem>` (or `--generate-key`, or `SOUP_SIGNING_KEY`) writes a real detached signature; `soup adapters verify --public-key <trusted.pem>` does a cryptographic verify that fails closed on any tamper / wrong key. Sigstore keyless (OIDC-via-GitHub) stays infra-blocked.

## `soup adapters check-safetensors` — refuse pickle at the boundary

```bash
soup adapters check-safetensors ./my_adapter --strict && echo "SHIP IT"
```

Rejects any `.bin`, `.pt`, or pickle-format weights. The single biggest LoRA attack vector is `pickle.load` on hostile weights; `--strict` makes the CI gate hard.

## License-conflict gate in `soup adapters merge`

```bash
soup adapters merge a/ b/ c/ --output merged/ \
  --license mit --license apache-2.0 --license mit \
  --license-override "Approved by legal team 2026-05-20"
```

33-entry SPDX-license compatibility matrix. Conflicting licenses require `--license-override "<reason, ≥ 8 chars>"` for audit.

## Namespace-pin TOFU (anti-AI-Jacking)

The first pull of an HF repo pins its namespace owner SHA in a local SQLite cache. Future pulls re-verify before download — a hijacked HuggingFace org cannot silently replace your base model.

## `soup airgap-bundle` — physical-media transfer

```bash
soup airgap-bundle \
  --output secure-bundle.tar.gz \
  --model ./llama3-8b-merged \
  --dataset ./prod-logs.jsonl \
  --wheel ./venv/lib/python3.11/site-packages \
  --bundle-size-cap 50
```

Packs model + datasets + wheels + kernels + manifest into a single tarball suitable for transfer through a data diode (physical-media / sneaker-net). Embeds a SHA-256 manifest per file. Refuses to build if total size > `--bundle-size-cap` (default 100 GiB).

## Numbers

+152 new tests in v0.60.0. Security-fix coverage: 12 HIGH, 11 MEDIUM, 6 LOW.

## See also

- [Compliance pack](/docs/compliance-pack) — v0.71.35 puts signing, scanning and attestation on a HIPAA / SOC 2 / EU AI Act / SR 11-7 path.
- [Governance](/docs/governance) — v0.59 BOM + SLSA-3 + audit log.
- [Adapters](/docs/adapters) — v0.57 diff / merge / blame / branch (the rest of the LoRA toolkit).
- [Adapter lifecycle (v0.67)](/docs/adapter-lifecycle) — `soup lock` SHA256 closure makes signed + scanned adapter artifacts reproducible across the team; `soup adapters pr` puts review + signing on every adapter change.

[PreviousGovernance, BOM & SLSA-3 attestations](/docs/governance)[NextCompliance Pack](/docs/compliance-pack)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="088-compliance-pack"></a>

# 88. Compliance pack (v0.71.35)

*Source: <https://trysoup.dev/docs/compliance-pack>*

Ship a regulated fine-tune with the paperwork it needs: start from a regulation-shaped config, publish a provenance-carrying model card, and gate every future change in CI.

## 1. Start from a compliance template

```bash
soup init --template hipaa      # Protected Health Information
soup init --template soc2       # SOC 2 Trust Services Criteria
soup init --template eu-ai-act  # EU AI Act Annex XI/XII
soup init --template sr-11-7    # SR 11-7 Model Risk Management
```

Be clear about what a template is, because the honest constraint shaped the design: Soup's compliance controls are **CLI flags and commands, not config keys**. There is no `audit_log:` or `bom:` key in the schema, so a template **cannot** "pre-wire audit-log on" as YAML, and pretending otherwise would be a lie in a document meant to prove things.

Each template is therefore a valid, immediately trainable config on a license-clean Apache-2.0 base, plus header comments naming the exact commands for that regime: PHI scrubbing and air-gap for HIPAA, BOM / attest / sign for SOC 2, Annex XI plus energy tracking for the EU AI Act, repro-receipt plus diagnose and ship for SR 11-7. Built-in templates went from 17 to 21.

## 2. The provenance path

```bash
soup data pii --input ./data/train.jsonl      # flag emails / phones / SSNs / MRNs
soup data decontaminate --input ./data/train.jsonl   # drop public-benchmark overlap

soup train --config soup.yaml --repro-receipt receipt.json
# EU AI Act: Annex XI/XII docs + measured energy
soup train --config soup.yaml --annex-xi annex_xi.md \
    --track-energy --energy-country DEU --energy-out energy.json

soup registry push --run-id <run-id> --name my-model --tag v1
soup bom emit --name my-model --base-model <hf-repo-id> \
    --base-sha <hex> --config-sha <hex> \
    --energy energy.json --format both        # CycloneDX + SPDX
soup attest emit --stage train --subject my-model --sha <hex> \
    --sign ed25519 --key key.pem              # in-toto + SLSA-3
```

The audit log records every command automatically (`soup audit-log tail`, `soup audit-log rotate`).

## 3. Model card autogen

```bash
soup card my-model:v1 -o MODELCARD.md
# or override the auto-generated card when uploading:
soup push --model ./output --repo you/my-model --card my-model:v1
```

`soup card` turns a [registry](/docs/registry) entry into a publishable Hugging Face card carrying base model, the real training config, an eval scorecard, config and data sha256 hashes, lineage (ancestors), and a table of every registered artifact.

Adapter versus full model is inferred from the registered artifacts and falls back to the training config's LoRA rank, with Spectrum and [LISA](/docs/lisa) full fine-tunes correctly treated as dense. This is not a detail: the live smoke caught a real LoRA run with no attached artifacts rendering `Type | Full model` and `library_name: transformers`, a false claim in a provenance document that 90 green tests had missed.

`soup push --card` is Hugging Face only (it warns and ignores on other hubs), and a bad ref fails fast before any network call.

## 4. Gate future changes in CI

```bash
soup ci init --data data/train.jsonl --suite expectations.yaml --evidence ship_evidence.json
# writes .github/workflows/soup-gate.yml
```

The generated job runs, in order:

```
soup data validate <data>       # dataset format compliance
soup expect <data> <suite>      # PII / token-length / refusal / judge expectations
soup ship --evidence <ev.json>  # SHIP / DON'T-SHIP (exit 2 blocks the merge)
```

Flags: `--branch main`, `--python 3.11`, `--force`. Every interpolated path is validated to stay under the repo root and shell-quoted, the branch and Python version are regex-gated so they cannot break out of their YAML context, and the write is atomic, symlink-rejecting, and refuses to clobber an existing workflow without `--force`.

## GGUF export now works on Windows

The same release validated `soup export --format gguf` end to end on Windows for the first time (llama.cpp built CPU-only with VS2022 BuildTools, SmolLM2-135M exported to q4\_0, q4\_k\_m, q8\_0 and f16, then `soup deploy ollama`, then live inference). Doing so surfaced four real bugs, each independently fatal:

| Bug | Effect |
| --- | --- |
| `SOUP_DIR` used relatively, not anchored to `~` | `~/.soup/llama.cpp` was never found, so a fresh ~200 MB checkout landed in whatever directory you ran from |
| The auto-clone pip-installed llama.cpp's `requirements.txt` | It pins `torch~=2.2.1` against the CPU wheel index: torch 2.5.1+cu became **2.2.2+cpu, so CUDA was gone**, and transformers 4.57 dropped to 4.46. Your first GGUF export silently destroyed your training setup. Soup now installs only the convert script's extra dependencies, unpinned, never touching torch |
| MSVC is a multi-config generator | It emits `build/bin/Release/llama-quantize.exe`, but only the flat layout was searched, so a correctly built llama.cpp was "not found" |
| `soup deploy ollama` on a relative GGUF path | Ollama resolves `FROM` against the Modelfile's directory and Soup writes it to a temp dir, so it failed with "pull model manifest: file does not exist". The Modelfile now emits an absolute path |

That is the argument for validating a feature on real hardware rather than trusting a green suite: 361 export and ollama tests were passing throughout.

## Security

Model-card injection was hardened, and the hole was pre-existing in `soup push`'s own auto-card rather than new: the Training section interpolated `base`, `task`, `scheduler` and `recipe` unescaped into a card destined for the public Hub, and since `base` and `scheduler` have no charset validator, a crafted-but-schema-valid config could smuggle raw HTML, or a backtick that breaks out of the surrounding code span. All values now go through the markdown escaper, which also neutralises backticks and strips C0/ESC control bytes.

## See also

- [Governance & provenance](/docs/governance) — BOM, attestations, audit log, air-gap.
- [Supply-chain security](/docs/supply-chain-security) — ed25519 signing, scan gates, license conflicts.
- [soup ship](/docs/soup-ship) — the verdict the CI gate blocks a merge on.
- [Model export](/docs/export) — GGUF, AWQ, GPTQ, ONNX, TensorRT.

[PreviousSupply-chain Security](/docs/supply-chain-security)[NextRecipes](/docs/recipes)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="089-recipes"></a>

# 89. Recipes

*Source: <https://trysoup.dev/docs/recipes>*

Soup includes 167 ready-made configs for popular models — v0.31 grew the catalog to 80, v0.51 added 26 new families (GPT-OSS / GLM 4.6 / Kimi K2 / MiniMax M2 / QwQ-32B / QVQ-72B / Granite 4 / Voxtral / DeepSeek-OCR and more), v0.52 added 6 TTS / BitNet recipes (Orpheus / Sesame-CSM / Llasa / Spark / Oute / Falcon-E), v0.62 added 3 RAG recipes (`raft-llama3-8b`, `ra-dit-retriever`, `ra-dit-llama3-8b`), v0.71.24 added 17 SFT recipes for the open-weight models released February to June 2026 (Qwen 3.5 / Qwen 3.6 / DeepSeek-V4 / GLM-5.1 / Kimi K2.5 / Kimi K2.6 / MiniMax M3 / Mistral Large 3), v0.71.26 added `qwen2.5-coder-7b-sft` (catalog 133 → 134), v0.71.30 added 3 GRPO rollout-env recipes (`grpo-env-calculator`, `grpo-env-retrieval-qa`, `grpo-env-guess-number`, catalog 134 → 137), v0.71.31 added `online-dpo-smollm2-135m` (catalog 137 → 138), and v0.71.32 added the ASR recipes `whisper-tiny-asr` / `whisper-base-asr` / `whisper-large-v3-asr` plus `smolvlm-256m-sft` (catalog 138 → 142), v0.73.3 added `qwen3.5-4b-pretrain` and `deepseek-v4-flash-grpo` (catalog 142 → 144), and v0.74.0 added nineteen more across the Qwen2.5-Coder and Qwen2.5-Math sizes, the DeepSeek-R1-Distill families in SFT and DPO, SmolLM3, and GRPO and DPO variants for the 2026 MoE giants (catalog 144 → 163), and v0.75.0 added four more, two DPO shapes for bases that already shipped SFT and GRPO plus two small Qwen3.5 GRPO recipes a contributor could actually run a few steps of (catalog 163 → 167). No need to write YAML from scratch.

## List Recipes

```bash
soup recipes list
```

Shows all available recipes with model name, task, and description.

## Search Recipes

```bash
# Search by model name
soup recipes search llama

# Search by task type
soup recipes search grpo

# Search by model size
soup recipes search 8b
```

## Show Recipe

```bash
# Print full YAML to stdout
soup recipes show llama3.1-8b-sft
```

## Use a Recipe

```bash
# Copy recipe to soup.yaml
soup recipes use llama3.1-8b-sft

# Custom output path
soup recipes use qwen2.5-7b-dpo --output my-config.yaml
```

## Available Recipes (167 total)

| Category | Models |
| --- | --- |
| **General SFT/DPO/GRPO/KTO/ORPO/SimPO/IPO/PPO/Embedding/Pretrain** | Llama 3.1 / 3.2 / 4 (Scout + Maverick), Qwen 2.5 / 3 (incl. 30B MoE + 235B-A22B), Mistral, Mixtral 8x7B/8x22B, Gemma 3, Phi-4, DeepSeek R1 / V3 + all 6 R1-Distill sizes |
| **2026 model families (v0.71.24, 17 new SFT)** | Qwen 3.5 (0.8B / 2B / 4B / 9B / 27B + 35B-A3B / 122B-A10B / 397B-A17B MoE, Apache-2.0, 262K ctx, native vision), Qwen 3.6 (27B + 35B-A3B, Apache-2.0), DeepSeek-V4 Flash / Pro (MIT), GLM-5.1 (MIT, 754B), Kimi K2.5 / K2.6 (Modified MIT, ~1T), MiniMax M3 (428B, MiniMax Community License — commercial use needs a separate agreement), Mistral Large 3 (Apache-2.0, 675B/41B-active multimodal MoE) |
| **v0.74.0 (19 new, contributed)** | Coding and math specialists `qwen2.5-coder-{1.5b,14b,32b}-sft` and `qwen2.5-math-{1.5b,7b}-sft`; the R1-Distill line completed with `deepseek-r1-distill-{qwen-1.5b,qwen-7b,llama-8b}-sft` and the matching `-dpo` trio; `smollm3-3b-sft` (the catalog had SmolLM2 in three sizes and no SmolLM3); `qwen3.8-27b-sft` (dense 27B text-only, Apache-2.0, DeepSpeed ZeRO-2); and preference and reasoning variants for the 2026 MoE giants, `qwen3.5-{9b-dpo,9b-grpo,35b-a3b-dpo}`, `glm-5.1-{dpo,grpo}` and `kimi-k2.6-grpo`. The giants are not trained by anyone here, so no hyperparameter in them is a measured recommendation |
| **v0.73.3 (2 new, contributed)** | `qwen3.5-4b-pretrain` (continued pre-training on `Qwen/Qwen3.5-4B-Base`: plaintext data, one epoch, QLoRA 4-bit), `deepseek-v4-flash-grpo` (GRPO reasoning on `deepseek-ai/DeepSeek-V4-Flash` with MoE LoRA and gradient checkpointing) |
| **v0.51 catalog expansion (26 new)** | GPT-OSS 20B / 120B, GLM 4.6 / 5, Kimi K2 / K2-Thinking, MiniMax M2, QwQ-32B, QVQ-72B, Granite 4, LFM2, Cogito v2, Mistral Small 3 / Medium 3.5, Magistral / Devstral / Ministral, MedGemma, EmbeddingGemma, LLaVA-Next, InternVL 3.5, Voxtral, Baichuan 2, Qwen-Image, DeepSeek-OCR, Paddle-OCR-VL |
| **Vision (multimodal)** | Llama-3.2-Vision (11B + 90B), Pixtral-12B, Qwen2-VL (7B + 72B), InternVL 2.5 / 3.5, LLaVA-Next, MiniCPM-V 2.6, Qwen-Image, DeepSeek-OCR, Paddle-OCR-VL |
| **Audio (speech)** | Qwen2-Audio, SeamlessM4T v2 (translation), Whisper-large-v3 (ASR), Voxtral |
| **ASR fine-tuning (v0.71.32, `task: asr`)** | Whisper tiny (39M) / base (74M) — live on a 4 GB GPU — and large-v3 (1.5B, 16 GB+); built-in WER/CER, see [ASR fine-tuning](/docs/asr-fine-tuning) |
| **TTS (v0.52, 5 families)** | Orpheus, Sesame-CSM, Llasa, Spark, Oute |
| **BitNet (v0.52)** | Falcon-E |
| **RAG (v0.62)** | `raft-llama3-8b`, `ra-dit-retriever`, `ra-dit-llama3-8b` |
| **Reasoning** | All 6 DeepSeek-R1-Distill sizes (Qwen 1.5B/7B/14B/32B + Llama 8B/70B), Qwen3-Coder 30B, Qwen3-30B-A3B reasoning, Phi-4 reasoning, QwQ-32B |
| **Small / edge / mobile** | SmolLM2 (135M / 360M / 1.7B), SmolLM3 3B, Qwen2.5 (0.5B / 1.5B / 3B), Gemma 2 2B, Phi-3.5-mini, Llama-3.2 (1B / 3B), LFM2 |
| **Domain specialists** | BioMistral 7B, Meditron 7B, MedGemma (medical) — CodeLlama (13B / 70B), Magicoder 6.7B (code) — Mathstral 7B and Qwen2.5-Math 1.5B / 7B (math) — Qwen2.5-Coder 1.5B / 14B / 32B (code) — Llama-2-13b-finance — Nemotron-4 340B — EmbeddingGemma |
| **Multimodal reasoning** | Llama-3.2-Vision GRPO, Pixtral DPO |
| **Multi-GPU** | llama3-70b-fsdp2, qwen3-32b-zeropp, deepseek-v3-pipeline |
| **Apple Silicon (MLX)** | llama3.1-8b / qwen3-8b / gemma3-4b SFT-MLX |
| **Tool-calling / agentic** | qwen3-8b-tools, llama4-scout-tools |

Each recipe ships with LoRA rank, learning rate, batch size, and quantization tuned to the model. Use `soup recipes show <name>` to print the full YAML.

## Customizing Recipes

Recipes are a starting point. After `soup recipes use`, edit the generated `soup.yaml` to:

- Point to your dataset (`data.train`)
- Adjust epochs, learning rate, or LoRA rank
- Add backend: unsloth for 2-5x speedup
- Enable evaluation with `eval` config section

[PreviousCompliance Pack](/docs/compliance-pack)[NextRecipe Expansion](/docs/recipe-expansion)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="090-recipe-expansion"></a>

# 90. Massive Recipe Expansion (v0.31.0)

*Source: <https://trysoup.dev/docs/recipe-expansion>*

v0.31 grows the recipe catalog from 46 → 80 ready-made configs. Every category gets first-class coverage — vision, audio, reasoning, edge, domain specialists, and multimodal reasoning.

## What's new

```bash
soup recipes list                    # browse all 80
soup recipes search vision           # filter by category
soup recipes search reasoning
soup recipes search edge
soup recipes use llama3.2-vision-grpo
```

## Vision (multimodal)

- **Pixtral-12B-2409** — `pixtral-12b-sft` + `pixtral-dpo`
- **Qwen2-VL** — 7B + 72B (FSDP2 multi-GPU)
- **InternVL 2.5** — OpenGVLab vision
- **MiniCPM-V 2.6** — compact vision
- **Llama-3.2-Vision GRPO** — multimodal reasoning

## Audio (speech)

- **Qwen2-Audio-7B-Instruct** — speech understanding
- **Whisper-large-v3** — ASR fine-tune
- **SeamlessM4T-v2** — speech translation

## Reasoning

All 6 DeepSeek-R1-Distill sizes ship as recipes:

- Qwen 1.5B / 7B / 14B / 32B
- Llama 8B / 70B

Plus Qwen3-Coder 30B, Qwen3-30B-A3B reasoning (MoE), and Phi-4 reasoning.

## Small / edge / mobile

- **SmolLM2** — 135M / 360M / 1.7B
- **Qwen2.5** — 0.5B / 1.5B / 3B
- **Gemma 2** — 2B
- **Phi-3.5-mini** — 3.8B
- **Llama-3.2** — 1B / 3B

## Domain specialists

- **Medical** — BioMistral 7B, Meditron 7B
- **Code** — CodeLlama 13B / 70B, Magicoder 6.7B
- **Math** — Mathstral 7B
- **Finance** — Llama-2-13b-finance starter
- **Mega-scale** — Nemotron-4 340B (NVIDIA)

## See also

- [Recipes](/docs/recipes) — the full catalog, 167 recipes at v0.75.0
- [Vision & Audio](/docs/multimodal)

[PreviousRecipes](/docs/recipes)[NextMigration](/docs/migration)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="091-migration"></a>

# 91. Migration

*Source: <https://trysoup.dev/docs/migration>*

Switch to Soup from other fine-tuning tools in one command. Soup automatically converts your existing config files.

## Supported Tools

| Source | Config format | Command |
| --- | --- | --- |
| LLaMA-Factory | YAML config | `soup migrate --from llamafactory config.yaml` |
| Axolotl | YAML config | `soup migrate --from axolotl config.yml` |
| Unsloth | Jupyter notebook | `soup migrate --from unsloth finetune.ipynb` |

## Usage

```bash
# Convert LLaMA-Factory config to soup.yaml
soup migrate --from llamafactory llama3_lora_sft.yaml

# Convert Axolotl config
soup migrate --from axolotl axolotl_config.yml

# Convert Unsloth notebook (AST-only, no code execution)
soup migrate --from unsloth finetune.ipynb

# Preview without writing (dry-run)
soup migrate --from llamafactory config.yaml --dry-run

# Custom output path
soup migrate --from axolotl config.yml --output my-soup.yaml
```

## What Gets Mapped

Soup maps all major config fields automatically:

- **Model**: `model_name_or_path` / `base_model` -> `base`
- **Task**: `stage` / `rl` -> `task` (pt->pretrain, rm->reward\_model, sft/dpo/kto/ppo/grpo)
- **LoRA**: rank, alpha, dropout, target modules, DoRA
- **Training**: epochs, lr, batch size, optimizer, scheduler, warmup, quantization
- **Data**: dataset path, format, max length
- **Output**: output directory

## Unsupported Features

Soup will warn about features that don't have a direct equivalent:

- **sample\_packing** (Axolotl) — not auto-mapped by `soup migrate`; set `training.packing` (or `training.multipack`) by hand after conversion
- **freeze training** (LLaMA-Factory) — not auto-mapped; set `training.freeze_layers` or `training.freeze_ratio` by hand
- **use\_rslora** (Unsloth) — supported, but the key is nested: `training.lora.use_rslora`
- **max\_steps** — Soup uses epochs; max\_steps emitted as comment
- **DeepSpeed / W&B** — emitted as CLI flag comments

## Security

- Input files are validated to be within the current working directory
- Unsloth notebooks are parsed via AST only — **no code is executed**
- Output paths are confined to the current directory

[PreviousRecipe Expansion](/docs/recipe-expansion)[NextFine-tune Llama 3.1 with LoRA](/docs/fine-tune-llama-3-1-lora)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="092-fine-tune-llama-3-1-lora"></a>

# 92. Fine-tune Llama 3.1 with LoRA using Soup CLI

*Source: <https://trysoup.dev/docs/fine-tune-llama-3-1-lora>*

This guide shows how to fine-tune **Meta Llama 3.1 8B** with LoRA adapters on a custom dataset using Soup CLI. End-to-end from install to inference in under 10 minutes on a single GPU.

## Why LoRA on Llama 3.1?

LoRA (Low-Rank Adaptation) trains only a small fraction (~0.1%) of model parameters, which means:

- Train 8B parameter Llama 3.1 on a single 24GB GPU (RTX 4090, A10)
- Checkpoints are tiny (~100MB instead of 16GB)
- Faster training and easier experimentation

## 1. Install

```bash
pip install "soup-cli[train,fast]"
```

> Since v0.71.0 the base `soup-cli` package is a light, PyTorch-free CLI. `[train]` adds the training stack; `[fast]` adds Unsloth on top. Installing `[fast]` alone cannot train.

The `[fast]` extra adds Unsloth for 2–5× training speedup on Llama-family models.

## 2. Prepare your dataset

Use the Alpaca format (JSON list of instruction/input/output triples):

```json
[
  {
    "instruction": "Summarize the following text.",
    "input": "Soup CLI is a fine-tuning toolkit...",
    "output": "Soup CLI is an open-source LLM fine-tuning tool."
  }
]
```

Save as `train.json`.

## 3. Create the config

Save as `llama31.yaml`:

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft
backend: unsloth            # root-level, NOT under training

data:
  train: train.json
  format: alpaca
  max_length: 2048          # sequence length lives under data

training:
  epochs: 3
  lr: 2.0e-4                # the key is lr, not learning_rate
  batch_size: 2
  gradient_accumulation_steps: 8
  lora:
    r: 16                   # LoRA turns on when r > 0; there is no enabled flag
    alpha: 32
    dropout: 0.05
    target_modules: [q_proj, k_proj, v_proj, o_proj]

output: ./runs/llama31
```

> **Spelling matters, and until v0.74.0 nothing told you so.** Writing `learning_rate` instead of `lr`, or nesting `backend` under `training`, used to be dropped in silence and the default used instead. Since v0.74.0 loading a config walks the whole tree and reports every key it cannot place, naming the field you probably meant, and **since v0.75.0 the same config is refused**: `soup train` exits 1 before the training stack is imported. If a setting seems to have no effect on an older wheel, read the unknown-key report and check the spelling against [Configuration](/docs/configuration).

## 4. Train

```bash
soup train --config llama31.yaml
```

Soup auto-detects GPU, enables FlashAttention, and trains LoRA adapters. Expect ~20 minutes for 1k examples on an RTX 4090.

## 5. Chat with your fine-tuned model

```bash
soup chat --model ./runs/llama31/latest
```

## 6. Export for deployment

```bash
# Merge LoRA into base model and export GGUF for Ollama
soup export --model ./runs/llama31/latest --format gguf --quant q4_k_m
```

## Troubleshooting

**Out of memory?** Enable QLoRA (a 4-bit base model). Note `4bit` is already the default, so this is only worth setting explicitly if you changed it:

```yaml
training:
  quantization: 4bit
  lora:
    r: 16
```

**Slow training?** Ensure `backend: unsloth` is set at the **root** of the config (not under `training`) and that you installed `pip install "soup-cli[train,fast]"`.

## Next steps

- [Export to GGUF and Ollama](/docs/export-to-gguf-ollama)
- [Multi-GPU training with DeepSpeed](/docs/multi-gpu-deepspeed)
- [Training methods reference](/docs/training)

[PreviousMigration](/docs/migration)[NextFine-tune Qwen 3 on a custom dataset](/docs/fine-tune-qwen-3)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="093-fine-tune-qwen-3"></a>

# 93. Fine-tune Qwen 3 on a custom dataset

*Source: <https://trysoup.dev/docs/fine-tune-qwen-3>*

Qwen 3 is one of the strongest open-weight models for reasoning and multilingual tasks. This guide shows how to fine-tune **Qwen 3 8B** on your own dataset with Soup CLI.

## 1. Install

```bash
pip install "soup-cli[train,fast]"
```

> Since v0.71.0 the base `soup-cli` package is a light, PyTorch-free CLI. `[train]` adds the training stack; `[fast]` adds Unsloth on top. Installing `[fast]` alone cannot train.

## 2. Dataset (ShareGPT format)

Qwen 3 handles multi-turn conversations well. Use the ShareGPT format:

```json
[
  {
    "conversations": [
      {"from": "user", "value": "Explain gradient descent in one paragraph."},
      {"from": "assistant", "value": "Gradient descent is..."}
    ]
  }
]
```

## 3. Config

```yaml
base: Qwen/Qwen3-8B
task: sft
backend: unsloth            # root-level, NOT under training

data:
  train: conversations.json
  format: sharegpt
  max_length: 4096          # sequence length lives under data

training:
  epochs: 2
  lr: 1.5e-4                # the key is lr, not learning_rate
  batch_size: 4
  gradient_accumulation_steps: 4
  lora:
    r: 32                   # LoRA turns on when r > 0; there is no enabled flag
    alpha: 64
    target_modules: [q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj]
```

**Why target all projections?** Qwen 3 benefits from training LoRA on both attention and MLP projections for instruction-following tasks.

## 4. Train

```bash
soup train --config qwen3.yaml
```

## 5. Serve with vLLM

```bash
pip install "soup-cli[serve-fast]"
soup serve --model Qwen/Qwen3-8B --adapters qwen3=./runs/qwen3/latest --backend vllm --port 8000
```

The model is now available at `http://localhost:8000/v1/chat/completions` with OpenAI-compatible API.

## Tips

- Qwen 3 uses a 151k vocab — stick to `data.max_length: 4096` or higher for best results.
- Use `training.neftune_alpha: 5` to inject noise into embeddings — improves generalization on small datasets.
- For reasoning tasks, try `training.packing: true` for efficient long-context training.

## Related

- [DPO alignment guide](/docs/dpo-training-guide)
- [Data formats reference](/docs/data-formats)

[PreviousFine-tune Llama 3.1 with LoRA](/docs/fine-tune-llama-3-1-lora)[NextFine-tune Gemma 3 with QLoRA on a single GPU](/docs/fine-tune-gemma-3-qlora)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="094-fine-tune-gemma-3-qlora"></a>

# 94. Fine-tune Gemma 3 with QLoRA (single GPU)

*Source: <https://trysoup.dev/docs/fine-tune-gemma-3-qlora>*

QLoRA combines 4-bit base model quantization with LoRA adapters, making it possible to fine-tune **Gemma 3 12B** on a single 16GB GPU (RTX 4080, A4000).

## Why QLoRA?

- 4× memory reduction vs full LoRA
- Same quality as full fine-tuning (~99% of benchmark scores per the QLoRA paper)
- Works on consumer hardware

## 1. Install

```bash
pip install "soup-cli[train,fast]"
```

> Since v0.71.0 the base `soup-cli` package is a light, PyTorch-free CLI. `[train]` adds the training stack; `[fast]` adds Unsloth on top. Installing `[fast]` alone cannot train.

## 2. Config

```yaml
base: google/gemma-3-12b-it
task: sft
backend: unsloth            # root-level, NOT under training

data:
  train: train.json
  format: alpaca
  max_length: 2048          # sequence length lives under data

training:
  quantization: 4bit        # the key is quantization, not quant
  epochs: 3
  lr: 2.0e-4                # the key is lr, not learning_rate
  batch_size: 1
  gradient_accumulation_steps: 16
  lora:
    r: 16                   # LoRA turns on when r > 0; there is no enabled flag
    alpha: 16
    use_rslora: true
    target_modules: [q_proj, k_proj, v_proj, o_proj]
```

**Note the key flags:**

- `quantization: 4bit` — 4-bit NF4 quantization of base model (the key is `quantization`; `quant` is not a field, and since v0.74.0 it is reported as an unknown key)
- `use_rslora: true` — rank-stabilized LoRA (v0.21.0+), better for larger models
- `batch_size: 1` with `gradient_accumulation_steps: 16` — effective batch of 16 on tight VRAM

## 3. Train

```bash
soup train --config gemma3.yaml
```

Monitor VRAM with `nvidia-smi` in another terminal. You should see ~14GB peak on Gemma 3 12B.

## 4. Merge and export

```bash
# Dequantize, merge LoRA, save full model
soup merge --adapter ./runs/gemma3/latest --output ./gemma3-merged

# Or export directly to GGUF q4_k_m
soup export --model ./runs/gemma3/latest --format gguf --quant q4_k_m
```

## Common issues

**OOM during backward pass?** Reduce `data.max_length` to 1024 or enable gradient checkpointing:

```yaml
training:
  gradient_checkpointing: true
```

**Loss spikes?** Enable loss watchdog (v0.24.0+):

```yaml
training:
  loss_watchdog: true          # a bool, not a block
  loss_watchdog_threshold: 2.0 # spike factor vs the running mean (default 3.0)
  loss_watchdog_patience: 5
```

## Related

- [Export to GGUF and Ollama](/docs/export-to-gguf-ollama)
- [Training backends](/docs/backends)

[PreviousFine-tune Qwen 3 on a custom dataset](/docs/fine-tune-qwen-3)[NextExport to GGUF and deploy on Ollama](/docs/export-to-gguf-ollama)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="095-export-to-gguf-ollama"></a>

# 95. Export fine-tuned models to GGUF and deploy on Ollama

*Source: <https://trysoup.dev/docs/export-to-gguf-ollama>*

After training with Soup CLI, export your model to GGUF format and serve it locally with Ollama in three commands.

## 0. Build llama.cpp first, if you want a quantized GGUF

Soup auto-clones llama.cpp (pinned at tag `b5270`) into `~/.soup/llama.cpp` on first use, but it does **not build it**. Converting to `f16` or `f32` works from the Python script alone. **Every quantized type additionally needs the `llama-quantize` binary**, so build it once:

```bash
cd ~/.soup/llama.cpp
cmake -B build -DGGML_NATIVE=OFF -DLLAMA_CURL=OFF -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release --target llama-quantize -j 4
```

Soup finds the binary in both the single-config layout (`build/bin/llama-quantize`, from Make or Ninja) and the multi-config one (`build/bin/Release/llama-quantize.exe`, from MSVC or Xcode), or on your `PATH`. To use a checkout you already have, pass `--llama-cpp /path/to/llama.cpp` or set `LLAMA_CPP_PATH`.

On Windows the validated toolchain is Visual Studio 2022 Build Tools with the "Desktop development with C++" workload plus CMake 3.14 or newer, CPU-only. Linux and macOS need only a C++ toolchain and CMake. **CUDA builds of llama.cpp are untested.**

> **Do not run `pip install -r ~/.soup/llama.cpp/requirements.txt`.** It pins `torch~=2.2.1` against the CPU wheel index, so it will downgrade a CUDA PyTorch and break training. Soup deliberately installs only the convert script's own extras (`gguf`, `sentencepiece`, `protobuf`), unpinned.

## 1. Export to GGUF

```bash
soup export --model ./runs/my-model/latest \
            --format gguf \
            --quant q4_k_m \
            --output ./my-model.gguf
```

**Quantization levels:**

| Quant | Size (7B) | Quality | Use case |
| --- | --- | --- | --- |
| `q4_k_m` | ~4.1 GB | Good | Default — best size/quality balance |
| `q5_k_m` | ~4.8 GB | Better | When you need higher accuracy |
| `q8_0` | ~7.5 GB | Near-lossless | Benchmarks, eval |
| `q4_0` | ~3.8 GB | Lower | The smallest rung `--quant` accepts |
| `f16` / `f32` | ~14 GB / ~28 GB | Unquantized | A conversion with no quantization step |

`--quant` accepts exactly these six values (`q4_0`, `q4_k_m`, `q5_k_m`, `q8_0`, `f16`, `f32`) and exits 1 on anything else, so the smaller llama.cpp rungs like `q2_k` and `q3_k_m` are not reachable through Soup.

## 2. Deploy to Ollama

Soup CLI ships with Ollama integration (v0.18.0+):

```bash
soup deploy ollama \
    --model ./my-model.gguf \
    --name my-model \
    --template chatml
```

This creates an Ollama Modelfile, imports the GGUF, and registers your model.

## 3. Chat

```bash
ollama run my-model
```

Or via the API:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "my-model",
  "prompt": "Hello!"
}'
```

## One-liner: train → export → deploy

```bash
soup train --config soup.yaml && \
soup export --model ./runs/latest --format gguf --quant q4_k_m && \
soup deploy ollama --model ./runs/latest/model.gguf --name my-model
```

## Other export formats

Soup CLI also supports:

- **ONNX** — `--format onnx` for cross-platform inference
- **TensorRT-LLM** — `--format tensorrt` for NVIDIA optimized serving
- **AWQ / GPTQ** — `--format awq` or `--format gptq` for quantized GPU inference
- **Hugging Face** — not an export format. A merged checkpoint comes from `soup merge --adapter <path> --output <dir>`. The formats `soup export` accepts are `gguf`, `gguf-ud`, `onnx`, `tensorrt`, `awq`, `gptq`, `bitnet`, `tq1_0` and `torchao`.

## Related

- [Serving with vLLM and SGLang](/docs/serving)
- [Fine-tune Llama 3.1 with LoRA](/docs/fine-tune-llama-3-1-lora)

[PreviousFine-tune Gemma 3 with QLoRA on a single GPU](/docs/fine-tune-gemma-3-qlora)[NextDPO training: align LLMs with human preferences](/docs/dpo-training-guide)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="096-dpo-training-guide"></a>

# 96. DPO training guide: align LLMs with human preferences

*Source: <https://trysoup.dev/docs/dpo-training-guide>*

**Direct Preference Optimization (DPO)** aligns language models with human preferences without needing a reward model — it's simpler and more stable than RLHF/PPO.

## When to use DPO

- You have a dataset of "chosen" vs "rejected" responses
- You want to reduce hallucinations and off-topic answers
- You want alignment without the complexity of PPO

Use DPO **after** SFT. A typical pipeline: Pretrain → SFT → DPO.

## 1. DPO dataset format

```json
[
  {
    "prompt": "Explain quantum entanglement.",
    "chosen": "Quantum entanglement is a physical phenomenon where...",
    "rejected": "Idk, something quantum."
  }
]
```

Save as `preferences.json`.

## 2. Config

```yaml
base: ./runs/my-sft-model/latest   # Start from SFT checkpoint
task: dpo
backend: transformers             # root-level, NOT under training

data:
  train: preferences.json
  format: dpo
  max_length: 2048                # sequence length lives under data

training:
  epochs: 1
  lr: 5.0e-7                      # the key is lr, not learning_rate
  batch_size: 2
  gradient_accumulation_steps: 8
  dpo_beta: 0.1                   # the key is dpo_beta, not beta
  lora:
    r: 16                         # LoRA turns on when r > 0; there is no enabled flag
    alpha: 32
```

> **Spell these two exactly.** `learning_rate` is not the field, so it leaves you on the `lr` default of `2e-5` — about 40x too high for DPO, which is the difference between alignment and a wrecked model. Likewise `beta` is not read; the field is `dpo_beta`. Since v0.74.0 a misspelled key is at least reported when the config loads, with a suggestion, and since v0.75.0 it is refused outright; before v0.74.0 it was dropped in silence, which is how a 40x learning rate reaches a real run.

**Key DPO hyperparameters:**

- `dpo_beta: 0.1` — KL penalty weight. Higher = stay closer to reference model.
- `lr: 5e-7` — DPO needs a much smaller LR than SFT.
- `epochs: 1` — DPO overfits quickly, rarely needs more than 1–2 epochs.

## 3. Train

```bash
soup train --config dpo.yaml
```

## 4. Evaluate

Compare the DPO model against the SFT baseline:

```bash
soup eval compare <sft-run-id> <dpo-run-id>
```

## DPO variants in Soup CLI

Soup supports several preference-optimization methods — swap `task:` to change algorithm:

- `task: dpo` — Direct Preference Optimization
- `task: orpo` — ORPO (combines SFT + DPO in one step, no reference model)
- `task: simpo` — SimPO (length-normalized, no reference model)
- `task: ipo` — IPO (IPO loss, more stable than DPO on noisy data)
- `task: kto` — KTO (works with unpaired binary labels)

## Related

- [Training methods reference](/docs/training)
- [Fine-tune Llama 3.1 with LoRA](/docs/fine-tune-llama-3-1-lora)

[PreviousExport to GGUF and deploy on Ollama](/docs/export-to-gguf-ollama)[NextMigrate from LLaMA-Factory to Soup CLI](/docs/migrate-from-llamafactory)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="097-migrate-from-llamafactory"></a>

# 97. Migrate from LLaMA-Factory to Soup CLI

*Source: <https://trysoup.dev/docs/migrate-from-llamafactory>*

Switching from **LLaMA-Factory** to Soup CLI takes one command. Soup CLI offers a simpler YAML schema, 2–5× faster training via Unsloth, and a unified CLI for training, serving, and export.

## One-line migration

```bash
soup migrate --from llamafactory path/to/your/llamafactory_config.yaml
```

This produces a `soup.yaml` file equivalent to your LLaMA-Factory config, mapping:

| LLaMA-Factory | Soup CLI |
| --- | --- |
| `model_name_or_path` | `base` (a root-level string, not `base.model`) |
| `stage: sft` | `task: sft` |
| `finetuning_type: lora` | `training.lora.r` (LoRA is on when `r > 0`) |
| `lora_rank` | `training.lora.r` |
| `lora_alpha` | `training.lora.alpha` |
| `per_device_train_batch_size` | `training.batch_size` |
| `cutoff_len` | `data.max_length` (sequence length lives under `data`) |
| `template` | nothing: Soup auto-detects the chat template from the tokenizer. Override with `data.chat_template` if you need to pin one. |

## Side-by-side example

**LLaMA-Factory config:**

```yaml
model_name_or_path: meta-llama/Llama-3.1-8B-Instruct
stage: sft
do_train: true
finetuning_type: lora
lora_rank: 16
lora_alpha: 32
dataset: alpaca_en
template: llama3
cutoff_len: 2048
per_device_train_batch_size: 2
gradient_accumulation_steps: 8
learning_rate: 2.0e-4
num_train_epochs: 3
```

**Soup CLI equivalent:**

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft
backend: unsloth            # root-level, NOT under training

data:
  train: alpaca_en
  format: alpaca
  max_length: 2048          # sequence length lives under data

training:
  epochs: 3
  lr: 2.0e-4                # the key is lr, not learning_rate
  batch_size: 2
  gradient_accumulation_steps: 8
  lora:
    r: 16                   # LoRA turns on when r > 0; there is no enabled flag
    alpha: 32
```

## Why migrate?

- **Faster training** — `backend: unsloth` gives 2–5× speedup on Llama/Qwen/Gemma/Mistral
- **Single YAML schema** validated by Pydantic v2 (no silent typos)
- **Unified CLI** — `soup train`, `soup chat`, `soup eval`, `soup serve`, `soup export` all in one tool
- **167 ready-made recipes** — `soup recipes list`
- **Built-in GGUF/Ollama export**
- **Dry-run migration** — preview the config with `--dry-run` before writing

## Dry-run preview

```bash
soup migrate --from llamafactory config.yaml --dry-run
```

Prints the converted config to stdout without writing.

## Related

- [Migrate from Axolotl](/docs/migrate-from-axolotl)
- [Configuration reference](/docs/configuration)

[PreviousDPO training: align LLMs with human preferences](/docs/dpo-training-guide)[NextMigrate from Axolotl to Soup CLI](/docs/migrate-from-axolotl)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="098-migrate-from-axolotl"></a>

# 98. Migrate from Axolotl to Soup CLI

*Source: <https://trysoup.dev/docs/migrate-from-axolotl>*

**Axolotl** is a popular fine-tuning framework. Soup CLI can import Axolotl configs directly with `soup migrate`.

## One-line migration

```bash
soup migrate --from axolotl path/to/axolotl_config.yml
```

## Field mapping

| Axolotl | Soup CLI |
| --- | --- |
| `base_model` | `base` (a root-level string, not `base.model`) |
| `datasets[0].path` | `data.train` |
| `datasets[0].type` | `data.format` |
| `sequence_len` | `data.max_length` (sequence length lives under `data`, not `training`) |
| `micro_batch_size` | `training.batch_size` |
| `gradient_accumulation_steps` | `training.gradient_accumulation_steps` |
| `num_epochs` | `training.epochs` |
| `adapter: lora` / `qlora` | `training.lora.r` (+ `training.quantization: 4bit` for qlora) |
| `lora_r` / `lora_alpha` | `training.lora.r` / `training.lora.alpha` |
| `load_in_4bit: true` | `training.quantization: 4bit` (the key is `quantization`, not `quant`) |
| `flash_attention: true` | (auto-enabled in Soup) |

## Example conversion

**Axolotl:**

```yaml
base_model: mistralai/Mistral-7B-v0.3
load_in_4bit: true
adapter: qlora
datasets:
  - path: tatsu-lab/alpaca
    type: alpaca
sequence_len: 2048
micro_batch_size: 2
gradient_accumulation_steps: 8
num_epochs: 3
learning_rate: 0.0002
lora_r: 16
lora_alpha: 32
flash_attention: true
```

**Soup CLI (after `soup migrate`):**

```yaml
base: mistralai/Mistral-7B-v0.3
task: sft
backend: unsloth            # root-level, NOT under training

data:
  train: tatsu-lab/alpaca
  format: alpaca
  max_length: 2048          # sequence length lives under data

training:
  quantization: 4bit        # the key is quantization, not quant
  epochs: 3
  lr: 2.0e-4                # the key is lr, not learning_rate
  batch_size: 2
  gradient_accumulation_steps: 8
  lora:
    r: 16                   # LoRA turns on when r > 0; there is no enabled flag
    alpha: 32
```

## What you gain

- One CLI for train / chat / eval / serve / export instead of separate tools
- Native Unsloth backend (automatic 2–5× speedup on supported models)
- GGUF / Ollama / vLLM / SGLang export and serving built-in
- Loss watchdog, curriculum learning, sample packing, freeze training

## Dry-run

```bash
soup migrate --from axolotl axolotl.yml --dry-run
```

## Related

- [Migrate from LLaMA-Factory](/docs/migrate-from-llamafactory)
- [Training methods](/docs/training)

[PreviousMigrate from LLaMA-Factory to Soup CLI](/docs/migrate-from-llamafactory)[NextMulti-GPU training with DeepSpeed ZeRO-3](/docs/multi-gpu-deepspeed)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="099-multi-gpu-deepspeed"></a>

# 99. Multi-GPU training with DeepSpeed ZeRO-3

*Source: <https://trysoup.dev/docs/multi-gpu-deepspeed>*

Use Soup CLI with DeepSpeed ZeRO-3 to train large models across multiple GPUs. This guide shows how to fine-tune a **70B model** across 4–8 GPUs.

## Install

```bash
pip install "soup-cli[train,deepspeed]"
```

> `[deepspeed]` adds ZeRO on top of the training stack; it does not pull it in on its own, because the base package is PyTorch-free.

## When to use which ZeRO stage

| Stage | What it shards | When to use |
| --- | --- | --- |
| ZeRO-2 | Optimizer states + gradients | 2–4 GPUs, 7B–13B models |
| ZeRO-3 | Everything incl. parameters | 4+ GPUs, 30B+ models |
| FSDP2 | Fully sharded (PyTorch native) | Alternative to ZeRO-3 |

## Config for Llama 3.1 70B on 8× A100

```yaml
base: meta-llama/Llama-3.1-70B-Instruct
task: sft
backend: transformers       # root-level, NOT under training

data:
  train: train.json
  format: alpaca
  max_length: 4096          # sequence length lives under data

training:
  epochs: 2
  lr: 1.0e-4                # the key is lr, not learning_rate
  batch_size: 1
  gradient_accumulation_steps: 16
  gradient_checkpointing: true
  auto_mixed_precision: true
  lora:
    r: 32                   # LoRA turns on when r > 0; there is no enabled flag
    alpha: 64

output: ./runs/llama70b
```

> **Sharding is not a config key.** There is no `training.distributed` block. DeepSpeed and FSDP are selected on the command line, so the same YAML runs on one GPU or eight.

## Launch on 8 GPUs

```bash
soup train --config llama70b.yaml --gpus 8 --deepspeed zero3
```

`--deepspeed` accepts `zero2`, `zero3`, `zero2_offload`, `zero3_offload`, `zero++`, or a path to a DeepSpeed config JSON. **Since v0.74.0 your own file is resolved the way a preset is**, and only for keys that are provably invalid for the run: `zero_hpz_partition_size` when the world size is not divisible by it, and the fp16 quantiser keys against a bf16 run. That matters because the documented way to customise ZeRO++ is to copy the preset JSON, which copies both defects, so an unresolved user file inherited a crash the presets are already protected from. A repair is printed and written to a temp copy: **your file on disk is never modified**, a config using none of those keys is passed through byte-identical, and malformed JSON is passed through untouched because DeepSpeed reports a bad config better than a traceback would. `zero3_offload` (v0.73.0) is stage 3 with CPU **parameter** offload, which is what a run short of VRAM actually wants and which could not be named on the command line before: `zero3` set no offload at all and the only offload preset was stage 2, optimizer-only. Measured on one H100 with Llama-3.1-8B in bf16: **21.65 tok/s at a 38,135 MB peak**. Its `offload_optimizer` deliberately stays off, because turning it on makes DeepSpeed build a CPU Adam kernel against a matching CUDA toolkit and fail without one; copy the emitted JSON and flip it if you have `nvcc`. Note that DeepSpeed with LoRA was broken on **every** stage until v0.73.0, and the repair covers the supervised trainer only. Use `zero2_offload` when the optimizer state is what does not fit. Soup handles the `torchrun` / `deepspeed` launcher config automatically.

## Alternative: FSDP2

```bash
soup train --config llama70b.yaml --gpus 8 --fsdp full_shard
```

`--fsdp` accepts `full_shard`, `shard_grad` or `full_offload`. FSDP2 is PyTorch-native and often simpler for LoRA workloads.

## Ring FlashAttention for 128k+ context

For very long sequences:

```bash
pip install "soup-cli[ring-attn]"
```

```yaml
data:
  max_length: 131072

training:
  use_ring_attention: true
```

## Tips

- Always enable `gradient_checkpointing: true` for 70B+ models
- CPU offload trades speed for VRAM — use only if OOM
- Profile first: `soup profile --config llama70b.yaml` estimates memory + throughput before you spend GPU hours

## Related

- [Backends reference](/docs/backends)
- [Training methods](/docs/training)

[PreviousMigrate from Axolotl to Soup CLI](/docs/migrate-from-axolotl)[NextCLI Reference](/docs/cli-reference)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="100-cli-reference"></a>

# 100. CLI Reference

*Source: <https://trysoup.dev/docs/cli-reference>*

## Core Commands

### `soup init`

Create a config file with interactive wizard or template.

```bash
soup init [--template <template>] [--output <path>]
```

### `soup train`

Start a training run.

```bash
soup train [--config <path>] [--resume auto|<checkpoint>] [--wandb] [--tensorboard] \
           [--deepspeed zero2|zero3|zero2_offload|zero3_offload|zero++|zero_pp] [--fsdp full_shard|shard_grad|full_offload] \
           [--gpus auto|<N>] [--gate <suite>] \
           [--push-as <user/repo>] [--hf-resume] [--yes]
```

- `--gpus` (v0.27) — topology-aware multi-GPU launch hint (NVLink/PCIe detection)
- `--deepspeed zero++` (v0.27) — ZeRO-3 with quantized weights & grads
- `--gate` (v0.26) — run an eval suite at epoch boundaries and halt on regression
- `--push-as` (v0.29) — auto-push every `save_steps` checkpoint to HF Hub as a `checkpoint-<N>` branch
- `--hf-resume` (v0.29) — pull the latest checkpoint branch from HF Hub and resume training

### `soup chat`

Interactive chat with a trained model.

```bash
soup chat --model <path> [--base <model>] [--temperature <float>] [--max-tokens <int>]
```

### `soup serve`

Start an OpenAI-compatible inference server.

```bash
soup serve [--model <path>] [--backend transformers|vllm|sglang|mii] [--port <int>] [--host <host>] [--tensor-parallel <n>] [--gpu-memory <float>] [--speculative-decoding <draft-model>] [--num-speculative-tokens <n>] [--adapters <name>=<path>]
```

### `soup export`

Export model to deployment format.

```bash
soup export --model <path> --format gguf|gguf-ud|onnx|tensorrt|awq|gptq|bitnet|tq1_0|torchao [--quant <type>] [--output <path>]
soup export --format awq|gptq --calibration-data <p> [--bits 4|8] [--group-size 128]
# --calibration-data is REQUIRED for both awq and gptq, and --calibration-samples caps
# the rows read (default 128). Refused before the quantizer is imported: gptq since
# v0.74.0, awq since v0.75.0, where a flagless run silently downloaded AutoAWQ's own
# large default calibration set.
soup export --format onnx [--onnx-task text-generation|feature-extraction]              # feature-extraction for task: embedding
```

### `soup merge`

Merge LoRA adapter with base model.

```bash
soup merge --adapter <path> [--base <model>] [--output <path>] [--dtype <type>]
```

### `soup push`

Upload model to HuggingFace Hub.

```bash
soup push --model <path> --repo <user/repo> [--private] [--collection <owner/slug-hash>]
```

- `--collection` (v0.29) — add the pushed repo to an existing HF Collection

Token resolution (single source of truth): env `HF_TOKEN` / `HUGGINGFACE_HUB_TOKEN` > `~/.cache/huggingface/token` > `~/.huggingface/token`. The legacy `--token` flag is deprecated and delegates to this chain.

### `soup eval`

Comprehensive model evaluation platform.

```bash
soup eval benchmark --model <path> [--benchmarks <list>]
soup eval custom --model <path> --tasks <path>
soup eval judge --target <path> [--model <judge-model>] [--provider <p>] [--rubric <path>]
soup eval auto [--config <path>]
soup eval compare <run1> <run2>
soup eval leaderboard
soup eval human --input <prompts.jsonl> --model-a <path> --model-b <path>
```

On `soup eval judge`, note that `--target` is the model under test and `--model` is the **judge**, not the other way round.

### `soup deploy`

Deploy models to inference runtimes.

```bash
# Ollama
soup deploy ollama [--model <path>] [--name <name>] [--system <prompt>] [--template <tpl>] [--parameter <key=val>]
soup deploy ollama --list
soup deploy ollama --remove <name>

# HuggingFace Spaces (new in v0.29)
soup deploy hf-space \
  --model <user/repo> \
  --space <user/space> \
  --template gradio-chat|streamlit-chat
```

`soup deploy hf-space` validates `model_repo` via `validate_repo_id` before substituting into `app.py` / `README.md` — a crafted repo id cannot inject Python code into the deployed Space.

### `soup infer`

Batch inference on a list of prompts. With `--task asr` (v0.71.32) it transcribes a JSONL of audio clips through a Whisper model or adapter and reports per-row and corpus WER/CER when reference texts are present. See [ASR fine-tuning](/docs/asr-fine-tuning).

```bash
soup infer --model <path> --input <path> --output <path> [--max-tokens <int>] [--temperature <float>]
soup infer --task asr --model <whisper|adapter> --input <jsonl> --output <jsonl> \
  [--audio-dir <dir>] [--asr-language <lang>] [--asr-task transcribe|translate]
```

### `soup migrate`

Import config from competing tools.

```bash
soup migrate --from llamafactory|axolotl|unsloth <input-file> [--output <path>] [--dry-run]
```

### `soup recipes`

Browse and use ready-made training configs.

```bash
soup recipes list                          # List all 167 recipes
soup recipes show <name>                   # Print recipe YAML
soup recipes use <name> [--output <path>]  # Copy to soup.yaml
soup recipes search <query>                # Search by model/task/size
```

## Data Commands

```bash
soup data inspect <path>                          # View dataset stats
soup data validate <path> [--format <fmt>]        # Check format compliance
soup data convert <path> --to <fmt> --output <f>  # Convert between formats
soup data merge <f1> <f2> --output <f> [--shuffle]  # Combine datasets
soup data dedup <path> [--threshold <float>]      # Remove duplicates
soup data stats <path>                            # Extended statistics
soup data generate --prompt "..." --count <n>     # Generate synthetic data
soup data generate --provider ollama|anthropic|vllm  # Multi-provider support
soup data generate --template code|conversation|qa|preference|reasoning  # Domain templates
soup data generate --quality-pipeline             # Validate + filter + dedup
soup data filter <path> [--coherence <f>] [--perplexity <n>]  # Quality filter
soup data sample <path> --strategy random|diverse|hard -n <n>         # Sample subset
soup data split <path> --val 10 --test 10 [--absolute] [--seed <n>]   # Split; --val/--test are integer percentages
soup data split <path> --val 10 --stratify <field>           # Stratify on a field
soup data split <path> --val 10 --stratify-semantic --num-clusters <n>  # Embedding-clustered strata (v0.73.2)
soup data search <query>                                     # Search HuggingFace Hub
soup data preview <dataset_id>                               # Preview remote dataset
soup data download <dataset_id> [--output <path>] [--samples <n>]  # Download from HF
soup data register <name> --path <path> --format <fmt>       # Register local dataset
soup data unregister <name>                                  # Remove from registry
soup data registry                                           # List registered datasets
soup data push --input <jsonl> --hf-dataset <user/repo>      # Publish JSONL as HF dataset (v0.29)
soup data from-traces --logs <logs> --format langchain|openai|soup-serve  # Trace-to-preference (v0.26)
soup data review <pairs.jsonl>                                # Preview preference pairs (v0.26)
soup data augment --input <jsonl> --strategy rephrase|translate|style     # LLM augment (v0.25)
```

## Experiment Commands

```bash
soup runs                         # List all training runs
soup runs show <run_id>           # Detailed run info + loss curve
soup runs compare <run1> <run2>   # Side-by-side comparison
soup runs delete <run_id>         # Remove from database
```

## Other Commands

```bash
soup deploy ollama [--model <p>] [--name <n>]   # Deploy GGUF to Ollama
soup profile --config soup.yaml                # Estimate memory/speed/GPU (model + task come from the config)
soup adapters list [<dir>]                     # Scan for LoRA adapters (positional, defaults to .)
soup adapters info <path>                      # Adapter metadata
soup adapters compare <a> <b>                  # Side-by-side comparison
soup sweep --config <path> --param key=v1,v2   # Hyperparameter search
soup diff --model-a <p> --model-b <p>          # Compare two models
soup doctor [--nccl] [--disk] [--config soup.yaml]                   # Check system + deps (+ NCCL bandwidth, + media type)
soup quickstart [--dry-run] [--yes]             # One-command demo
soup ui [--port <int>] [--no-browser] [--host <h>] [--public] [--auth-token <t>] [--show-token]
# --public binds 0.0.0.0 and prints a phone QR. A non-loopback bind WITHOUT a valid
# token exits 2. Every private endpoint needs Authorization: Bearer; SSE takes a
# short-lived single-use ticket instead. /docs and /openapi.json are loopback-only.
soup tui                                        # Full-screen training dashboard
soup monitor                                    # Live GPU monitor: util / temp / VRAM / power per GPU
soup fetch examples|configs|deepspeed_configs [<name>]  # Fetch a ready-to-edit file from the bundled catalog
soup quantize <model> --to <fmt>                # Ergonomic alias for `soup export --format <fmt>`
soup plugins list|install|enable|disable        # Manage Soup plugins
soup llama cli|mtmd-cli|gguf-split|server|quantize ...  # Proxy to the llama.cpp binaries
                                                        #   closed allowlist; the child env is FILTERED, so
                                                        #   HF_TOKEN / OPENAI_API_KEY / ANTHROPIC_API_KEY and
                                                        #   every other secret are dropped before exec. What
                                                        #   is forwarded: PATH / HOME / USER / USERPROFILE,
                                                        #   TMP / TEMP, TERM / COLORTERM, locale, plus
                                                        #   LLAMA_CPP_HOME, GGML_* and OMP_NUM_THREADS.
soup bench <model> [--base <m>] [--backend auto|transformers|mlx]  # Inference speedometer
                   [--max-tokens <n>] [--num-prompts <n>] [--prompts-file <p>]
                   [--p50] [--p95]              # tail-latency percentiles
soup version [--full]                           # Show version info
```

`soup doctor --disk` is opt-in because the probe costs roughly 9 seconds cold and 2.4 seconds warm on Windows, and with several physical disks it reports the worst one. Since v0.73.3 it may also **write a small scratch file** next to where the shards would go, because on a disk whose rotational flag cannot be trusted the media type is settled by a measured read rather than by the flag. It exists because [the streaming disk tier](/docs/streaming-scaling) requires NVMe and refuses a SATA SSD, a spinning disk or media it cannot identify, rather than guessing and thrashing for hours.

## v0.54 — Pre-flight Decision

```bash
soup advise run <data.jsonl> --goal "<task>"          # Classify task + rank PROMPT_ENG/RAG/SFT/DPO/GRPO
soup advise run <data.jsonl> --probe                  # 100-step LoRA probe for empirical ROI
soup advise run <data.jsonl> --record                 # Append to ~/.soup/advise_history.jsonl
soup advise explain                               # Print full rubric
soup advise compare [--limit N]                   # Prior verdicts, newest first
```

## v0.55 — Eval Design

```bash
soup eval design <data.jsonl> --goal "..."        # Goal-conditioned suite (TF-IDF + dispatch)
soup eval discover <data.jsonl>                   # Greedy farthest-first canaries + memorization probes
soup eval lock <design.json>                      # SHA-256-pin the suite as an artifact
soup eval coverage <design.json> --task <category>  # Gap analysis vs v0.54 taxonomy
soup eval gate-install --baseline <run-id>        # Install .git/hooks/pre-push regression gate
```

## v0.56 — Diagnose (Model Report Card)

```bash
soup diagnose <run-id> [--attach-to-registry <id>]  # 7 failure-mode probes + OK/MINOR/MAJOR + SVG badge
soup train --diagnose-gate <evidence>               # Refuse final save on MAJOR regression (exit 2)
```

## v0.57 + v0.67 — Adapter VCS

```bash
# v0.57 — git for LoRA
soup adapters diff <a> <b>                            # Per-layer Frobenius + relative drift + SVD effective rank
soup adapters merge <a> <b> [c...] -o <out> \
  --strategy linear|ties|dare|svd|cmaes \           # v0.67 adds CMA-ES evolutionary search
  [--eval <suite>] [--budget 1h]                       #   (eval + budget required for cmaes)
soup adapters blame <adapter-dir> --dataset <d> --layer <l> --budget 5m --shards 4
soup adapters branch <name> -c <config.yaml> --base <model> --dataset <data>
soup adapters checkout <name> -o <out.yaml>
soup adapters branches

# v0.67 additions
soup adapters pr <title> --base-sha <hex> --adapter <path> \
  --eval <eval_delta.json> --samples <sample_diffs.json> \
  --output <PR.md>                                     # GitHub-shaped PR markdown
soup adapters bisect <ckpt1> <ckpt2> ... \
  --eval-command "soup eval custom --model {ckpt} --tasks <tasks.jsonl>"
                                                       # Binary-search history for regression boundary

# Shared run lockfile (v0.67)
soup lock write --base-model <id> --base-sha <64hex> --dataset-sha <64hex> \
  --env-hash <64hex> [--output soup.lock]
soup lock show [soup.lock]
soup lock check --base-model <id> --base-sha <64hex> --dataset-sha <64hex> \
  --env-hash <64hex> [soup.lock]                       # Exit 3 on drift
```

## v0.58 — Production Data Flywheel

```bash
soup loop init <served-model> --eval <suite> --baseline registry://<id> \
  --monthly-budget 50usd --max-runs-per-day 3
soup loop watch                                   # Long-running daemon (SIGTERM-safe)
soup loop status
soup loop pause / soup loop resume
soup loop canary <adapter> --traffic 5% --autoroll-on-regress
soup loop replay [<iter-id>]
```

## v0.59-v0.62 — Governance, Supply Chain, Unlearn, RAG

```bash
# v0.59 — Governance & Provenance
soup bom emit --name <m> --version <v> --base-model <hf> --base-sha <sha> \
  --config-sha <sha> --task <t> --license <spdx> --format cyclonedx|spdx|both \
  --output <prefix> [--attach-to-registry <id>]   # v0.73.3; needs --output
soup attest emit --stage extract|train|eval|export|publish \
  --subject <artifact> --sha <sha> --builder <id> --invocation <cmd> \
  --sign unsigned|ed25519 \
  --output <path> [--attach-to-registry <id>]     # ed25519 adds the .sig sidecar
# NOTE: --sign sigstore is accepted and infra-blocked. It does not fail: it
# prints a notice, falls back to an UNSIGNED attestation and exits 0, with no
# .sig written. Do not treat it as a signing backend.
soup audit-log tail / rotate
soup train --annex-xi <out.md> --repro-receipt <out.json>

# v0.60 — Supply Chain Security
soup adapters scan <dir>                          # Spectral LoRA backdoor scanner (exit 0/1/3)
soup adapters sign <dir> [--key <k>]              # Merkle-root signing (--strict is on verify)
soup adapters verify <dir> [--strict]             # Merkle-root tamper detection
soup adapters check-safetensors <dir> --strict    # Refuse pickle/.bin/.pt
soup adapters merge <a> <b> -o <out> --license <spdx>   # SPDX-license compatibility gate
soup airgap-bundle --model <dir> --output <dir> [--dataset <dir>]... [--wheel <dir>]... [--kernel <dir>]...

# v0.61 — Unlearning & Knowledge Edit
# (configured via task: unlearn in soup.yaml)
soup eval unlearning <run-id> --benchmark tofu|muse|wmdp
soup edit set --base <m> --method rome|memit|alphaedit --subject "..." --target "..." [--plan-only]
soup edit diff registry://before_id registry://after_id --probes probes.jsonl --top-k 10

# v0.62 — RAG & Activation Steering
soup steer train --base <m> --method caa|iti|repe --name <id> --pairs <jsonl>
soup steer apply --name <id> --strength <float>   # |strength| ≤ 10 enforced
soup steer list
```

## v0.63 — Production Trace Ecosystem

```bash
soup ingest --source langfuse|langsmith|helicone|openpipe|otel|openai-stored \
  --logs <jsonl> --output <out.jsonl>
soup ingest --source langfuse --pull [--since 7d] [--max-pages 100] \
  [--allow-private-host] --output <out.jsonl>
# --pull fetches from the Langfuse API instead of --logs, and is langfuse-only.
# Credentials come from LANGFUSE_PUBLIC_KEY + LANGFUSE_SECRET_KEY, never a flag
# (LANGFUSE_BASE_URL or LANGFUSE_HOST for a region or self-hosted instance).
# --since max 365d; --max-pages max 10000, and hitting it exits 1 writing nothing.
soup prune-prompt --input <jsonl> --output <out.jsonl> --min-frequency 0.95
soup data active-sample --input <jsonl> --budget N
soup ab --input <jsonl> --metric latency|judge_score|retry_rate \
  [--alpha 0.05] [--beta 0.20] [--effect-size 0.1]
soup drift-alarm --reference <ref.jsonl> --live <live.jsonl> --threshold 0.2 \
  [--slack-url ...] [--discord-url ...]                # Exit 3 on drift
```

## v0.64 — Pre-flight & Tooling

```bash
soup tunability --dataset <path> [--candidates <names>] \
  [--probe-steps 100] [--holdout-size 64] [--output <path>] [--plan-only] [--list]
soup plan --config <soup.yaml> [--state ./soup.tfstate]
soup apply --config <soup.yaml> [--state ./soup.tfstate] [--dry-run]
soup env lock [--output ./soup-env.lock]
soup env status [--lock ./soup-env.lock]
soup env check [--lock ./soup-env.lock]                # Exit 3 on ABI drift or a violated declared bound
soup env fix [--lock <path>] [--format uv-pip|requirements] [--output <path>]   # print an install plan; never installs
soup completions bash|zsh|fish
soup license-advisor --target b2c|defense|embedded \
  [--license <spdx>] [--monthly-active-users <N>]      # Exit 3 on block
```

## v0.65 — Eval Depth (Failure Modes 6 → 10)

```bash
soup eval behavior <run-id> --battery xstest|harmbench|jailbreakbench|elephant|syceval \
  [--evidence <responses.json>] [--output <report.json>]
soup eval capability <run-id> --suite full|fast|math|code [--output <report.json>]
soup eval checklist <spec.yaml> [--evidence <responses.json>] [--output <report.json>]
soup eval irt-subset <responses.jsonl> --size full|small|tiny [--output <plan.json>]
```

## v0.66 — Post-train X-rays

```bash
soup probe sae-diff <sae.safetensors> <pre_acts.json> <post_acts.json> \
  [--top-k 20] [--output <report.json>]
soup probe sleeper <base> [--evidence <activations.json>] [--output <result.json>]
soup probe interference <losses.json> [--output <matrix.json>]   # Exit 2 if worst ≥20%
soup probe pack <base> [--list] [--output <manifest.json>]
```

## v0.71.27 — Fine-tune Doctor

```bash
soup data doctor <data.jsonl> --model <id|path> \
  [--show-mask N] [--train-on-responses-only | --no-train-on-responses-only] \
  [--train-on-eot] [--train-on-messages-with-train-field] \
  [--train-on-messages-with-train-field] [--output <report.json>]
# 8 chat-template checks (eos_in_labels, bos_duplication, truncation_risk, …)
# OK/MINOR/MAJOR verdict · exit 0 OK/MINOR · exit 2 MAJOR

soup data lint <data.jsonl> [--model <id|path>] [--output <report.json>]
# Preference-data linter for dpo/orpo/simpo/ipo/bco/kto:
# length_bias (Cohen's d), label_imbalance, near_duplicates,
# identical_pairs, prompt_leak
```

## v0.71.28 — MCP Server

```bash
pip install "soup-cli[mcp]"
soup mcp serve                    # stdio · 14 read-only tools
soup mcp serve --allow-mutating   # also run train_start / export (planning only)
soup mcp serve --allow-execute    # + train_execute / export_execute, token-gated (v0.73.3)
```

## v0.71.29 — Model shrink

See [soup shrink](/docs/soup-shrink).

```bash
soup shrink --model <id|path> --calib calib.jsonl --drop-ratio 0.25 [--drop-layers N] \
    [--heal heal.jsonl --heal-steps 200] [--tolerance 0.10] [-o out/] [--device cpu] \
    [--attach-to-registry] [--plan-only]        # exit 0 = SHIP, 2 = DON'T SHIP, 1 = error
```

## v0.71.30 — PRM-guided GRPO + rollout envs

See [PRM-guided GRPO](/docs/prm-guided-grpo).

```bash
soup train --config grpo.yaml   # training.prm_reward: <path|id> · training.prm_aggregate: min|prod|last
soup recipes use grpo-env-calculator      # or grpo-env-retrieval-qa / grpo-env-guess-number
```

## v0.71.31 — Judge in the loop

See [Online DPO](/docs/online-dpo) and [best-of-N & Evolve](/docs/best-of-n-evolve).

```bash
soup train --config online_dpo.yaml   # task: online_dpo; training.online_dpo_judge OR training.reward_model (exactly one)
soup data best-of-n --base <m> --prompts p.jsonl --n 8 --judge <url> -o sft.jsonl [--emit-pairs dpo.jsonl]
soup data evolve --input seeds.jsonl --provider ollama|vllm --model <m> --strategy depth|breadth --rounds N -o out.jsonl
soup ship --task-mode pairwise --judge-model <url>     # swap-debiased judge win-rate vs a 0.5 base
```

## v0.71.32 — ASR (Whisper)

See [ASR fine-tuning](/docs/asr-fine-tuning).

```bash
pip install "soup-cli[train,audio]"
soup recipes use whisper-tiny-asr          # task: asr · format: asr · fits a 4 GB GPU
soup infer --task asr --model ./out --input eval.jsonl --output preds.jsonl \
    [--audio-dir ./data/audio] [--asr-language en] [--asr-task transcribe]
```

## v0.71.33 — Speculative-decoding drafts

See [soup draft](/docs/soup-draft).

```bash
soup draft measure --target <m> --draft <d> --prompts p.jsonl   # acceptance + real tok/s
soup draft measure ... --min-acceptance 0.6 -o report.json      # exit 2 below the floor (CI)
soup draft distill --target <tuned> --draft-base <tiny> --data d.jsonl -o draft/
soup draft distill ... --steps N --device cpu --force --plan-only
soup draft list                                                 # what --auto-spec will pick up
```

## v0.71.34 — Adapter algebra + LISA

See [adapter algebra](/docs/adapter-arithmetic) and [LISA](/docs/lisa).

```bash
soup adapters arithmetic "coder + 0.5*math - toxic" \
    --adapter coder=<p> --adapter math=<p> --adapter toxic=<p> -o <out> \
    [--allow-unscanned] [--allow-cross-base]

# LISA is config-side (sft · transformers · text · quantization: none)
soup train --config sft.yaml   # training.lisa_enabled: true
                               # [lisa_num_layers] [lisa_interval_steps] [lisa_reset_optimizer]
```

## v0.71.35 — Compliance pack

See [compliance pack](/docs/compliance-pack).

```bash
soup init --template hipaa|soc2|eu-ai-act|sr-11-7   # regulation-shaped starting config
soup card <registry-id> -o MODELCARD.md            # provenance-carrying HF model card
soup push --model ./out --repo you/m --card <registry-id>   # upload it as the README (HF only)
soup ci init [--data d.jsonl --suite s.yaml --evidence ev.json] \
    [--branch main] [--python 3.11] [--force]      # writes .github/workflows/soup-gate.yml
```

## v0.72 — Layer streaming

Streaming is turned on by **config keys, not CLI flags**: there is deliberately no `--stream-layers`. See [layer streaming](/docs/layer-streaming), [scaling a streaming run](/docs/streaming-scaling) and [preference losses over streaming](/docs/streaming-preference).

```bash
# The whole surface is in soup.yaml, under training:
#   stream_layers: true      # enable it (BETA)
#   stream_source: auto      # auto | ram | disk   (NVMe-class only; ram refuses rather than falling back)
#   stream_disk_kind: nvme   # v0.73.3: override the detected media type
#   stream_pin: false        # v0.74.0: force the pageable store (true refuses on the RAM tier
#                            #          if the box cannot page-lock it)
#   stream_ngram_source: auto # v0.74.0: Qwen4-Exp external N-gram table, auto | ram | disk
#   stream_buffers: 2        # 2-8, VRAM buffers in the pool
#   quantization: 4bit       # or none; nothing else streams
# task: sft | dpo | orpo | simpo | kto             (kto needs batch_size >= 2)
soup train --config soup.yaml
soup train --config soup.yaml --resume auto       # unblocked for streaming in v0.72.3 (load-side;
                                                  # see the docs for the torch 2.6 / CVE caveat)

soup doctor --disk    # report the media type behind the disk tier (NVMe / SATA SSD / HDD /
                      # Unknown). Opt-in: the probe costs about 9 s cold, 2.4 s warm
```

## v0.74.0 — the frozen base, the stack, and a listener

See [v0.74.0: loaded in fp32](/docs/loaded-in-fp32).

```bash
# MCP over the network. Both transports serve the same 18-tool registry as stdio.
soup mcp serve --transport sse --host 127.0.0.1 --port 8765 --auth-token "$TOKEN"
soup mcp serve --transport http --host 127.0.0.1 --port 8765 --auth-token "$TOKEN"
# --allow-execute is REFUSED with either network transport; --host/--port/--auth-token are
# refused under --transport stdio rather than silently ignored.
soup mcp runs reconcile --expunge-launching   # recover capacity from stale launching rows

soup eval aider --model <m> --output <report.json> [--run-id <id>]   # Aider Polyglot ([aider])
# --model and --output are required. Also: --exercises-dir, --image, --threads,
# --num-tests, --timeout, --allow-host-services.
# The [aider] extra is NOT enough to run it: you also need the official Aider
# benchmark image, source-built from an Aider checkout (./benchmark/docker_build.sh),
# and a clone of polyglot-benchmark. --allow-host-services lets untrusted
# model-generated code reach other services listening on the host.
soup train --config soup.yaml --cloud lambda   # plan-only by default, like --cloud modal
soup export --model ./output --format gptq --calibration-data cal.jsonl   # now required
soup serve --model ./output --host 0.0.0.0 --tool-auth-token "$TOKEN"     # exit 2 without it
soup sweep --config soup.yaml --param lora.r=8,16   # an unknown --param now exits 1, before
                                                    # the first arm, instead of running a grid
```

## Global Flags

```bash
soup --verbose <command>   # Full tracebacks instead of friendly errors
```

> **Note:** `--verbose` is a global flag — it must go **before** the command name, not after.

[PreviousMulti-GPU training with DeepSpeed ZeRO-3](/docs/multi-gpu-deepspeed)[NextFAQ](/docs/faq)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="101-faq"></a>

# 101. FAQ

*Source: <https://trysoup.dev/docs/faq>*

## General

### What models does Soup support?

Any HuggingFace-compatible model. Popular choices include Llama, Mistral, Qwen, Phi, and Gemma families. Vision models (LLaMA-3.2-Vision, Qwen2-VL) and audio models (Qwen2-Audio) are also supported.

### Do I need a GPU?

A CUDA-compatible GPU is strongly recommended, and 4-bit quantization is what makes a small card usable. As a QLoRA rule of thumb: 8 GB reaches about 7B, 16 GB about 14B, 24 GB about 34B, 48 GB about 70B, and 80 GB and up covers 70B full fine-tuning or a MoE. Below that, [layer streaming](/docs/layer-streaming) changes the arithmetic entirely: it bounds peak VRAM by one decoder layer rather than by the model, which is how an 8B trains on a 4 GB card.

### How is Soup different from other fine-tuning tools?

Soup is CLI-first and opinionated. One command to train, one YAML to configure. It wraps best practices (Unsloth, FlashAttention, optimal hyperparameters) so you don't have to research them. 23 training methods (text / vision / audio / ASR / TTS / classifier / distill / preference / MoLE routing / online DPO), 17 quantization formats, multimodal support, full pipeline from training to deployment. Plus, you can migrate from LLaMA-Factory, Axolotl, or Unsloth in one command.

### What version is current?

Soup CLI **v0.75.0**, tagged 12 September 2026. It has no codename, for the second release running: upstream titled this one with a sentence too, "MLX honours its config; unknown config keys refuse the load", and that sentence is [the release](/docs/mlx-honours-its-config). The headline is still that you can [fine-tune Llama-3.1-8B on a 4 GB laptop GPU](/docs/layer-streaming), and since v0.72.4 align on the same card. **All 60 of v0.75.0's pull requests came from outside the maintainer**, by 22 people, and what they found is six training options that `backend: mlx` validated, documented, accepted and read by nothing, so the same config trained a different recipe on Apple Silicon than on a CUDA box. The same release makes an unknown config key **refuse the load** rather than warn, records validation loss for the first time on any backend, and raises the torch floor to 2.6.0, which closes the known limitation v0.74.0 published. Before it, **v0.74.0**, tagged 4 September 2026, where **116 of 120 merged pull requests came from somebody other than the maintainer**, by 25 people, and what they found is that a LoRA run's frozen base, the one part that never receives an optimizer step, was being materialised at twice its checkpoint's precision on every supervised path and in twelve more trainers: measured on an H100 with Llama-3.1-8B and LoRA, peak memory falls from 48,241 MiB to 18,658 MiB, 2.59x on an unchanged config. It also moved the stack to Transformers 5.16.1, TRL 0.29 and PEFT 0.20, repaired the free notebook tier a second time, took layer streaming to a tenth architecture, and gave `soup mcp serve` bearer-gated sse and http transports. Before it, the v0.73 line: [v0.73.1](/docs/free-gpu-tier) fixed the free notebook tier, where bf16 was assumed on every CUDA card in fourteen places, and caught the streaming VRAM pre-flight under-predicting at long sequence; [v0.73.2](/docs/ship-gate-repairs) stopped the SHIP verdict ranking by the wrong thing and added `soup ship --noise-floor`; and [v0.73.3](/docs/flags-that-did-nothing) was the first release the maintainer did not write, all 24 of its pull requests coming from other people, who found four flags the schema validated, the docs described and nothing read. Underneath them, v0.73.0 is the release that took the method to hardware this project does not own: three borrowed days on an 8x H100 box, which [confirmed it against a real resident reference up to 72B and found a silent gradient defect above 32B in NF4](/docs/external-validation) that is repaired here. Set `training.stream_layers: true` and the frozen base is never loaded resident; it streams from CPU RAM one decoder layer at a time into a small pool of VRAM buffers while only the LoRA adapters stay resident, so peak VRAM is bounded by **one layer** instead of the whole model. Add `quantization: 4bit` (**v0.72.2**) and that RAM store shrinks about fourfold, which is what puts 8B within reach of a card that cannot hold a quarter of it. Measured on a 4 GB RTX 3050 Laptop at batch 1: **Llama-3.1-8B at 119.6 tok/s in 3.32 GB** (a pre-repair figure: it was measured before the v0.73.0 NF4 gradient repair and has not been re-run on that card since), Qwen2.5-3B at 264.2 tok/s in 1.76 GB, and on the bf16 path 3B at 143.1 tok/s in 2.15 GB, 1.5B at 525.0 tok/s and 0.5B at 978.6 tok/s. The honest cost is **1.43x slower than resident** (measured at 0.5B), a streamed NF4 run is **bit-exact** against a resident NF4 run and that is a CI test rather than a one-off, and it ships **BETA**. Nothing above 8B has been measured **on that 4 GB card**, so there is no 14B claim for it; the larger sizes were measured on the borrowed H100 box instead.

**v0.72.3 is the breadth release**, and it is what turns streaming from a demonstration into something you can plan a run on. [Nine architectures](/docs/streaming-scaling) streamed instead of three after it (Llama, Qwen, Mistral, Gemma, Phi; v0.74.0 later took it to ten), with the six new families each verified bit-exact against the same checkpoint loaded resident under both bf16 and NF4, though no throughput was measured for them so none is claimed. Batches above 1 and gradient accumulation both work, and at the same effective batch raising `batch_size` measured about **2.52x faster** than accumulating. A pre-flight now predicts peak VRAM and refuses a run that will not fit, which matters because streaming bounds the weights but not the logits: on a 151,936-token vocabulary at batch 8 the logits tensor alone measured **8.71 GB**, 146x the whole layer-buffer pool. `--resume` and `--hf-resume` work. And an **NVMe disk overflow tier** takes a base too large even for RAM, holding nothing resident, bit-exact against the RAM tier, with its speed deliberately left unmeasured rather than guessed.

**v0.72.4 opened it to the preference losses.** [`dpo`, `orpo`, `simpo` and `kto`](/docs/streaming-preference) run against a streamed base now, so alignment stops being the step that forces a bigger card. DPO's reference model is the same streamed base with its adapters switched off, not a second copy: on a 365M-parameter synthetic fixture, streamed DPO peaked at **0.914x** the streamed SFT peak with a byte-identical RAM store, and the control that forced a real second instance moved the peak by **730.44 MB** against 730.44 MB of weights, exactly one copy. All four are bit-exact against a resident run of the same loss. Read that 0.914x as "no second copy" rather than as a saving, and note the cost that is not free: DPO reads the layer stack **1.52x** as often per step. KTO is not reference-free however it is usually described, and it needs `batch_size` of 2 or more. No throughput figure is claimed for any preference loss, because none was measured. What remains scoped: `task` in `sft`, `dpo`, `orpo`, `simpo`, `kto`, transformers, text, plain LoRA. GRPO and PPO are permanently excluded, not pending. The measurement records behind all of it are [published in full](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks), and the work has a preprint: [10.5281/zenodo.21771064](https://doi.org/10.5281/zenodo.21771064).

### Is there a paper?

Yes. Layer streaming is written up as a preprint on Zenodo, CC-BY-4.0, cited by a concept DOI so a revision never strands a reference:

> **Exact Layer Streaming: LoRA Fine-Tuning of an 8B Model on a 4 GB Laptop GPU**. Makazhan, A. (2026). Zenodo. [10.5281/zenodo.21771064](https://doi.org/10.5281/zenodo.21771064).

[The paper page](/docs/paper) is the short version, with the BibTeX entry. The result it defends hardest is not the throughput but the correctness protocol: a streamed trainer whose autograd graph has been severed still produces a falling loss, so the only meaningful evidence is bit-exactness against a resident reference **of the same numerics**, resident NF4 for a streamed NF4 run and never resident bf16. That discipline caught a dispatch path producing a 0.94 logit divergence with byte-identical weights and adapters, no crash and a healthy-looking loss curve. It is not on arXiv, so cite the Zenodo DOI above rather than an arXiv identifier.

v0.72.0 also made `soup adapters arithmetic` exact across [mixed ranks](/docs/adapter-arithmetic) instead of refusing them, and added `--rank N`.

**v0.72.1** is an out-of-band correctness release, and it matters if you already used streaming: an adapter saved by a v0.72.0 streamed run is **inert outside the streaming path**, because its keys carried an extra `.inner.` segment and PEFT reports missing keys as a warning rather than an error, so `soup merge`, `soup serve` and `soup chat` all silently returned the untuned base. The training was correct and the bit-exactness results stand; only the saved file was wrong. [Re-run that adapter](/docs/layer-streaming#read-this-first-if-you-already-trained-with-streaming). The same release also closed a hole where `--hf-resume` slipped around the `--resume` guard; both were then refused until v0.72.3 fixed the load side and unblocked them.

Underneath it, the v0.71 line is two stories plus a run of capstones: **v0.71.0 split the install** (`pip install soup-cli` is now a light, PyTorch-free CLI; `pip install "soup-cli[train]"` adds the training stack) and raised the floor to **Python 3.10+**, and **v0.71.1 → v0.71.14 wired the entire schema-first roadmap live** — the reward-hack / echo-trap detectors, ULD + MiniLLM distillation, mid-epoch RL checkpoints, `soup iterative-dpo`, RAFT span-mask training + `soup ra-dit`, CAA/ITI/RepE steering, ROME/MEMIT/AlphaEdit edits + GRACE, NPO/SimNPO/RMU unlearning, the SAE / sleeper / truth / harm / interference probes, the live eval / advise / tunability / diagnose runners, the `soup build` dbt-DAG materialiser, the Magpie generator, the `soup compile` / `distill-prompt` / `compile-tools` / `local-rl train` prompt family, VeRA/VB-LoRA multi-tenant serving, MoLE routing, FSDP shard consolidation, and serve-side KV-cache typing now all run end-to-end. Genuinely new in v0.71: **ed25519 adapter/attestation signing** with supply-chain merge gates, codecarbon energy/CO2 tracking, PDF Annex XI/XII docs, Soup Can v3 attestations, and a local audit log. **v0.71.15 → v0.71.23** then closed the stub tail and added native **Spectrum targeted training** (`soup spectrum scan` + `training.unfrozen_parameters`), serve-time MoLE (`soup serve --mole`), `soup agent eval --sandbox`, `soup train --cloud modal`, GPT-2 + Mixtral knowledge editing, and live TTS / BitNet / MoE-quant trainers. **v0.71.24** grew the recipe catalog from 116 to **133** with 17 new SFT recipes for the 2026 open-weight families (Qwen 3.5 / 3.6, DeepSeek-V4, GLM-5.1, Kimi K2.5 / K2.6, MiniMax M3, Mistral Large 3), **v0.71.25** added [`soup ship`](/docs/soup-ship), the one-command SHIP / DON'T-SHIP verdict, **v0.71.26** closed the RL loop with [reward-hacking auto-mitigation](/docs/reward-hack-mitigation) (the GRPO/PPO trainer self-corrects mid-run instead of only halting), plus a new `qwen2.5-coder-7b-sft` recipe (catalog 133 → 134). **v0.71.27 "Fine-tune Doctor"** added a pure-CPU pre-flight — [`soup data doctor`](/docs/fine-tune-doctor) (8 chat-template checks incl. the "never stops generating" EOS bug) and `soup data lint` (DPO length-bias as a Cohen's d effect size) — **v0.71.28** shipped the [`soup mcp serve`](/docs/mcp-server) MCP server so any coding agent (Claude Code, Cursor, Cline, Continue) can drive Soup over stdio, **v0.71.29** added [`soup shrink`](/docs/soup-shrink), one-command depth pruning with an optional distill-heal and a SHIP / DON'T-SHIP perplexity verdict, **v0.71.30** let a Process Reward Model drive GRPO ([PRM-guided GRPO](/docs/prm-guided-grpo)), **v0.71.31** shipped the judge-in-the-loop suite ([Online DPO](/docs/online-dpo), [best-of-N & Evol-Instruct](/docs/best-of-n-evolve), plus a pairwise judge win-rate for [`soup ship`](/docs/soup-ship)), **v0.71.32** added [ASR fine-tuning](/docs/asr-fine-tuning) (`task: asr` fine-tunes Whisper on your own audio, `soup infer --task asr` reports WER/CER, whisper-tiny/base train on a 4 GB GPU), **v0.71.33** shipped [`soup draft`](/docs/soup-draft) (train and, above all, **measure** a speculative-decoding draft: the measured verdict on our own validated pair was that it does not pay off, so the speedup pitch was withdrawn rather than shipped), **v0.71.34** added [adapter algebra](/docs/adapter-arithmetic) (`soup adapters arithmetic "coder + 0.5*math - toxic"`) and [LISA](/docs/lisa) (full fine-tune quality without a full fine-tune), and **v0.71.35** shipped the [compliance pack](/docs/compliance-pack): regulation-shaped `soup init --template hipaa|soc2|eu-ai-act|sr-11-7` configs, `soup card` model-card autogen from a registry entry, a `soup ci init` PR gate (validate to expect to ship, exit 2 blocks the merge), and GGUF export validated end-to-end on Windows for the first time. **v0.71.36 "Data Moat II"** added a semantic layer over your training data ([`soup data dedup --semantic`](/docs/data-moat-ii), `soup data topics`) plus two tools for what a fine-tune forgets and leaks (`soup data canary`, `soup train --replay`), and **v0.71.37** made every `pip install "soup-cli[extra]"` hint work on Windows cmd.exe and fixed eval-gate benchmark tasks. The v0.71 line closed with the eval-gate wedge: **v0.71.38** gave the [`soup ship`](/docs/soup-ship) regression leg real teeth (answer-extraction scoring over seven bundled offline suites instead of substring-matched trivia), **v0.71.39** closed the evidence loop (`soup ship --emit-evidence` + a committed `ShipConfig` + `--push owner/repo#N`, provenance-bound so the gate is CI for weights on every PR), and **v0.71.40 + v0.71.41 shipped [Reward Forge](/docs/reward-verifier)** (`soup reward synth` auto-generates a deterministic reward verifier from your gold outputs and refuses a degenerate one, `soup reward stress` attacks a verifier with empty, padded, repetitive and sentinel-spam junk to prove it cannot be gamed). **475 test files**, 23 training tasks, 19 data formats, 17 quantization formats, 167 recipes, 21 built-in templates. Apache-2.0 license since v0.29.0. Check with `soup version --full`.

### Can I migrate from LLaMA-Factory / Axolotl / Unsloth?

Yes: `soup migrate --from llamafactory config.yaml` converts your existing config automatically. Supports LLaMA-Factory YAML, Axolotl YAML, and Unsloth Jupyter notebooks. Use `--dry-run` to preview without writing.

### Are there ready-made configs?

Yes. Soup ships 167 recipes spanning Llama 3.1/3.2/4 (Scout + Maverick), Qwen 2.5/3 (incl. 30B and 235B MoE), the 2026 families (Qwen 3.5/3.6, DeepSeek-V4 Flash/Pro, GLM-5.1, Kimi K2.5/K2.6, MiniMax M3, Mistral Large 3 — v0.71.24), QwQ-32B, QVQ-72B, Gemma 3, Mistral, Phi-4, DeepSeek R1/V3 + all 6 R1-Distill sizes, plus v0.51 additions (GPT-OSS 20B/120B, GLM 4.6/5, Kimi K2 / K2-Thinking, MiniMax M2, Granite 4, LFM2, Cogito v2, Mistral Small 3 / Medium 3.5, Magistral / Devstral / Ministral, Baichuan 2), vision (Pixtral, Qwen2-VL, InternVL 3.5, LLaVA-Next, MiniCPM-V, Qwen-Image, DeepSeek-OCR, Paddle-OCR-VL), audio (Qwen2-Audio, Whisper-large-v3, Voxtral, SeamlessM4T-v2), ASR fine-tuning (`whisper-tiny-asr` / `whisper-base-asr` / `whisper-large-v3-asr` — v0.71.32), TTS (Orpheus, Sesame-CSM, Llasa, Spark, Oute — v0.52), BitNet (Falcon-E — v0.52), edge (SmolLM2 135M-1.7B, Phi-3.5-mini, LFM2), domain specialists (BioMistral, Meditron, CodeLlama, Magicoder, Mathstral, MedGemma, EmbeddingGemma), plus v0.62 RAG (`raft-llama3-8b`, `ra-dit-retriever`, `ra-dit-llama3-8b`), MLX-native, and multi-GPU (`llama3-70b-fsdp2`, `qwen3-32b-zeropp`, `deepseek-v3-pipeline`). Run `soup recipes list` to browse, `soup recipes search llama` to filter, and `soup recipes use llama3.1-8b-sft` to start training instantly.

## Training

### How long does training take?

Depends on model size, dataset, and hardware. A 1B model with 10K samples on an RTX 4090 typically takes 15-30 minutes with SFT. With Unsloth backend, 2-5x faster.

### Can I resume training from a checkpoint?

Yes: `soup train --config soup.yaml --resume auto` (latest checkpoint) or `--resume ./output/checkpoint-500` (specific checkpoint).

### Does Soup support multi-GPU?

Yes. v0.27.0 added topology-aware `soup train --gpus N` launch, ZeRO++ (quantized weights + grads), FSDP2 + `torch.compile`, pipeline parallelism (`parallelism: pipeline` + `pipeline_stages`), and the DeepSpeed-MII serving backend. See [Multi-GPU Mastery](/docs/multi-gpu).

### What training methods are available?

23 methods: SFT, DPO, Online DPO (v0.71.31 — on-policy against an LLM judge or a reward model, wraps TRL OnlineDPOTrainer), GRPO, PPO, KTO, ORPO, SimPO, IPO, BCO (v0.40), Pretrain, Embedding, Reward Model, the unified `preference` dispatcher (v0.40 — set `training.preference_loss: dpo|simpo|orpo|ipo|bco` to swap loss without renaming the task), PRM (v0.50 Process Reward Model — also usable as the per-step reward inside GRPO via PRM-guided GRPO, v0.71.30), TTS (v0.52 — Orpheus / Sesame-CSM / Llasa / Spark / Oute), ASR (v0.71.32 — [Whisper fine-tuning](/docs/asr-fine-tuning) with built-in WER/CER), Classifier / Reranker / Cross-Encoder (v0.52), Distill (v0.52 — kl / forward\_kl / reverse\_kl / js divergences), Unlearn (v0.61 — NPO / SimNPO / RMU), and MoE LoRA Routing (v0.67 — MoLE per-token gating over 2..64 task adapters). Plus `soup edit set` (v0.61 — ROME / MEMIT / AlphaEdit) and `soup steer train` (v0.62 — CAA / ITI / RepE) as inference-time / weight-surgery surfaces.

### Can I auto-push checkpoints to HuggingFace during training?

Yes — `soup train --push-as user/my-model` uploads every `save_steps` checkpoint to HF Hub as a `checkpoint-<N>` branch. Pair with `--hf-resume` to pull the latest branch and keep going after a spot-instance preemption. Set `HF_ENDPOINT=https://hf.internal.example.com` to target a self-hosted Hub. See [HF Hub integration](/docs/hf-hub-integration).

### Can I train faster on large-vocab models?

Yes — v0.28.0 adds Cut Cross-Entropy (`use_cut_ce: true`), which avoids materialising the full `[seq × vocab]` logits tensor. Best on Llama 3 / Qwen 3 (vocab ≥ 128k). Install with `pip install "soup-cli[cce]"`. v0.28 also ships FP8 training on Hopper+ GPUs, tiered gradient checkpointing, kernel auto-composition, cross-document attention masking, and CPU/disk activation offloading. See [Training speed & memory](/docs/training-speed-memory).

## Data

### What data formats are supported?

19 formats: Alpaca, ShareGPT, ChatML, DPO, KTO, LLaVA, ShareGPT4V, Plaintext, Embedding, Audio, Tool-calling, Auto, PRM, Pre-tokenized, Input-output, Video, Multimodal (v0.42), RAFT (v0.62 Retrieval-Augmented Fine-Tuning — `query + golden_doc + distractors + answer`), and [ASR](/docs/asr-fine-tuning) (v0.71.32 Whisper fine-tuning — `{"audio": path, "text": transcript}`). Format is auto-detected from the first row. Local paths or remote URIs (s3 / gs / az / abfs / oci). Use `soup data convert` to switch between formats. v0.69 adds `soup build` (dbt-shaped DAG of dataset transforms with incremental materialisation), `soup expect` (Great Expectations suite for chat data), and `soup data brain-rot` (AI-slop detector — refuses to train on clickbait).

### How much data do I need?

For SFT, 1K-10K high-quality samples is a good starting point. Quality matters more than quantity. Use `soup data filter` to check data quality.

### Can I generate synthetic data?

Yes: `soup data generate --prompt "Create math problems" --count 100`. Supports OpenAI, Ollama, Anthropic Claude, vLLM, and custom servers. Includes domain templates (code, conversation, QA, preference, reasoning) and a full quality pipeline.

## Deployment

### How do I serve my model?

`soup serve --model ./output --backend vllm` for production. The API is OpenAI-compatible.

### Can I export to llama.cpp / Ollama?

Yes: `soup export --model ./output --format gguf --quant q4_k_m`

### What export formats are supported?

Nine: GGUF and GGUF-UD (llama.cpp / Ollama, the second being the Unsloth Dynamic ladder), ONNX (cross-platform), TensorRT-LLM (NVIDIA optimized), AWQ and GPTQ (quantized deployment, and GPTQ requires `--calibration-data` since v0.74.0), BitNet and `tq1_0` (1.58-bit), and torchao.

## Troubleshooting

### How do I see full error messages?

Use `soup --verbose <command>` for full tracebacks.

### How do I check my environment?

Run `soup doctor` to check Python version, GPU availability, dependency versions, and get fix suggestions.

### `ImportError: DLL load failed while importing _C` on Windows

That is PyTorch, not Soup: the installed wheel does not match your CUDA runtime. Reinstall torch from the index for your CUDA version, for example `pip install torch --index-url https://download.pytorch.org/whl/cu121`.

### `soup version` disagrees with `pip show soup-cli`

You have more than one Python installation and they are not the one you think. Use a virtual environment. This is worth taking seriously rather than ignoring, because the two commands read different things: `soup version` reads the source that is actually going to run.

### My environment used to work and now something is off

`soup env check` audits your installed packages against the version bounds Soup itself declares and exits 3 when one is violated, with no lock file required. The usual cause is a later `pip install` of a serving stack into a training environment. [`soup env fix`](/docs/preflight-tooling#soup-env-fix-the-repair-once-check-has-told-you-something-is-wrong) then prints a reproducible install plan from your lock file.

[PreviousCLI Reference](/docs/cli-reference)[NextWhat's new](/docs/whats-new)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="102-whats-new"></a>

# 102. What's new across v0.71 to v0.75

*Source: <https://trysoup.dev/docs/whats-new>*

One page for everything that shipped since the v0.71 install split, newest first. The current flagship, layer streaming, has its own pages: [Layer streaming](/docs/layer-streaming) for the mechanism and the measured numbers, [Scaling a streaming run](/docs/streaming-scaling) for architectures, batches, resume and the disk tier, [Preference losses over streaming](/docs/streaming-preference) for DPO, ORPO, SimPO and KTO, and [Validation on hardware we do not own](/docs/external-validation) for what the method does at 8B through 72B on someone else's cards.

Every line below names the release it shipped in. Where a number is quoted it was measured; where none is quoted, none was measured.

## The v0.75 line

- **v0.75.0 is the release where MLX started honouring the config it had been accepting.** Six training options were validated by the schema, documented in these pages and read by nothing on `backend: mlx`, so [the same `soup.yaml` trained a different recipe on Apple Silicon than on a CUDA box](/docs/mlx-honours-its-config): response-only masking reached nothing, so every MLX run trained on the prompt; the optimizer, scheduler, warmup ratio and weight decay were dropped, so every run built a bare AdamW at a constant learning rate; `max_grad_norm` clipped nowhere; and gradient accumulation and checkpointing silently took mlx-lm's defaults. **All 60 of its pull requests came from outside the maintainer**, by 22 people, and **fourteen of its fixes mean a finished run was wrong**. **Breaking:** an unknown config key now **refuses the load** at the deadline v0.74.0 named, and `grpo_variant: gspo` is the published sequence-level objective rather than a column-centering heuristic, so existing gspo configs will not reproduce prior runs. Validation loss was computed on every backend and thrown away; it is now its own series, with an un-evaluated step recording `NULL` rather than a fabricated zero. `torch>=2.6.0` closes the limitation v0.74.0 published rather than hid. Also here: inference prompts stop sending a doubled BOS across `soup chat`, `serve`, `infer`, `bench`, `diff`, `ship`, `diagnose` and `advise`; `soup ingest --source langfuse --pull` fetches traces live; `soup doctor --config` names the settings your backend does not read; Web UI read endpoints and SSE require authentication; and four recipes take the catalog to 167. **No maintainer gate**: three contributor records landed instead, one of them a gate that failed and was published as written.

## The v0.74 line

- **v0.74.0 found the frozen base being loaded in fp32 the whole time.** A LoRA run freezes the base, so its only job is to hold the checkpoint's own numbers, and all three supervised load paths passed no dtype at all: measured on an H100 with Llama-3.1-8B and LoRA, peak memory falls from 48,241 MiB to 18,658 MiB, **2.59x on an unchanged config**, with the same defect standing in twelve more trainers. **116 of the release's 120 pull requests came from outside the maintainer**, by 25 people, and nine of its fixes mean [a run you already finished was wrong](/docs/loaded-in-fp32#re-run-this), starting with unknown config keys that were silently dropped. The training stack moves to Transformers 5.16.1, TRL 0.29 and PEFT 0.20, so `pip install "soup-cli[train,mlx]"` resolves for the first time; the free notebook tier could not stream at all until now, for a second reason after v0.73.1's; layer streaming admits a tenth architecture and stops keeping an untied embedding and LM head both resident; and `soup mcp serve` gains sse and http transports behind a mandatory bearer token, with gated execution refused over a listener. **Breaking:** `soup serve` exits 2 rather than warning on a non-loopback host without `--tool-auth-token`, and the SGLang backend finally obeys `--trust-remote-code`. No new throughput was measured; the two new records are a second-box VRAM verification and a partial Apple Silicon gate.

## The v0.73 line: borrowed hardware

- **v0.73.3 was written entirely by other people.** All 24 pull requests came from outside the maintainer, from eight contributors, five of them appearing for the first time, and what they found was [four flags that the schema validated, the docs described, and nothing read](/docs/flags-that-did-nothing). Two findings are the project's signature failure shape: assistant-only loss masking built its label mask from a tokenizer mapping's **key strings**, so a run trained on **zero tokens** behind a normal-looking loss curve, and on Apple Silicon `quantization: 4bit` was silently rewritten to `none` because device detection did not know MLX. The one new capability is that [`soup mcp serve --allow-execute`](/docs/mcp-server#the-execution-model) stopped being a reserved gate and now runs a planned training or export behind a single-use, server-generated confirmation token, taking the server from 16 tools to 18. Also here: the `soup ship` noise floor is measured in the judge task modes rather than metric alone, `soup env check` flags an installed package that violates Soup's own declared bounds, and layer streaming stops refusing a fast virtio disk as if it were a spinning one. **No new measurement was made and no benchmark record was added**, which upstream states rather than leaves implicit.
- **v0.73.2 repaired the release gate itself.** Two of [`soup ship`](/docs/ship-gate-repairs)'s behavioural suites ranked by the wrong thing, so a stub answering every item correctly scored 0.000 and an 8B naming the right tool 40 times out of 40 scored 0.225. A whole failure direction, a model that refuses everything, had no detector until `mini_over_refusal` joined as the eighth bundled suite. New CLI flag `soup ship --noise-floor N` measures what the instrument itself can resolve before any delta is called significant. **Any verdict issued before this release is suspect, and a stored `--baseline` is on a different scale.**
- **v0.73.1 repaired the GPU tier most people actually have.** bf16 was assumed on every CUDA card in fourteen places, so every pre-Ampere card (T4, P100, V100, GTX 16xx) failed on [every task](/docs/free-gpu-tier), not only on streaming. The same release caught the streaming VRAM pre-flight under-predicting at long sequence, against a contract that says it never does, and shipped `training.stream_vram_probe`. Three more classes of finished-but-wrong run were closed: MLX adapters that loaded as a silent no-op, `backend: mlx` never dispatching to MLX at all, and periodic checkpoints under `use_fsdp2_compile` still loading dead.
- **v0.73.0 is the release that came out of three days on an 8x H100 box.** It repaired the NF4 gradient defect that only a resident reference could have found, plus four backends that had never executed once: the multi-GPU launcher, DeepSpeed with LoRA, SGLang serving and the Liger kernel. Two capabilities are new, both config keys: `training.seed` and full fine-tuning as `lora.r: 0`. Python narrows to 3.10 through 3.12. **Six fixes mean a completed run of yours may be wrong**, including a supervised path that silently capped every run at 1024 tokens and a `soup ship` gate whose suites scored zero on a capable model. [The changelog and the re-run list](/docs/borrowed-hardware). (v0.73.0)

## The v0.72 line: layer streaming

- **Validated on hardware nobody here owns.** Three borrowed days on an 8x H100 box, the first machine able to hold a **resident reference** for a model worth streaming, so the correctness check that had only ever run on 3-layer fixtures finally ran against real checkpoints. The streamed forward is exact against a matched resident reference at 8B, 14B, 32B and 72B; peak VRAM stays flat from 3,397 MB to 4,845 MB while the model grows fourfold; the 4 GB laptop's headline reproduces at a median 113.00 tok/s against its 119.6; and a streamed model converges indistinguishably from a resident one over five paired runs. It also found a defect: in NF4 above roughly 165 MB per decoder layer, the **backward** produced silently wrong gradients while the forward stayed exact and the loss looked healthy. That affects 32B and up, was present in every release from v0.72.0 to v0.72.4, and is repaired in v0.73.0, gated at both affected sizes against a control that reproduced it. [The whole record](/docs/external-validation).
- **DPO, ORPO, SimPO and KTO run against a streamed base.** Streaming used to mean supervised fine-tuning only. DPO's reference model is the same streamed base with its adapters switched off, so it costs no extra weights: on a 365M-parameter synthetic fixture, streamed DPO peaked at 0.914x the streamed SFT peak, where forcing a real second instance in the same harness cost 730.44 MB, exactly one copy of them. All four are bit-exact against a resident run of the same loss. The reference is free in memory, not in time: DPO reads the layer stack 1.52x as often per step. KTO needs `batch_size` of 2 or more. (v0.72.4)
- A packaging defect that predates the release: six preference trainers passed a field TRL removed across several of its own versions, so `soup train with task: orpo` could fail at import on a fresh install. The dependency bound was settled by constructing all six configs against each candidate version rather than by reading source, and a contract test now calls the real `setup()` for all six. The first bound shipped too tight, and the reason is worth keeping: some of those config classes had **moved** into TRL's experimental namespace while still being re-exported publicly with the field intact, and a relocation read as a removal. Constructing the object is what distinguishes the two; reading a diff is not. Corrected in v0.73.0, which widens support to `trl>=0.14.0,<0.29` (**since moved**: v0.74.0 requires `trl>=0.29.0,<1.0.0`) behind a capability-probe layer rather than a version table, verified by constructing and training all six on three different trl versions. (v0.72.4)
- The measurement records behind the whole v0.72 line are published in the repository's [benchmarks directory](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks), failures and discarded numbers included, and the work has a preprint: [10.5281/zenodo.21771064](https://doi.org/10.5281/zenodo.21771064), summarised on [the paper page](/docs/paper). (v0.72.4)
- `soup doctor --disk` reports the detected media type, because the streaming disk tier needs NVMe and refuses a SATA SSD, a spinning disk, or media it cannot identify rather than guessing. Opt-in, because the probe costs about 9 seconds cold and 2.4 seconds warm. (v0.72.3)
- `[mcp]` is pinned below 2.0. The MCP SDK's 2.0.0 removed an API `soup mcp serve` round-trips through, which broke its round-trip tests for anyone installing fresh. (v0.72.3. **Since lifted**: v0.74.0 requires `mcp>=1.10.0,<3` and picks the API by probing the server constructor rather than reading a version string, so both majors work.)
- `soup adapters arithmetic --rank N`: mixed-rank LoRA algebra is exact rather than refused. Stacking the factors reproduces the sum of deltas by construction, and an SVD truncates to the rank you ask for. (v0.72.0)

## The v0.71 line: lean install and live wiring

- `soup reward synth golds.jsonl -o reward.py` plus `soup reward stress`: Reward Forge. Synthesize a deterministic verifier from your gold outputs, refusing to emit a degenerate one, then attack it with empty, padded, repetitive and sentinel-spam junk to prove it cannot be gamed. (v0.71.40 and v0.71.41)
- `soup ship --emit-evidence` plus `--config soup.yaml` plus `--push owner/repo#N`: the verdict becomes CI for weights, a provenance-bound gate you commit and render on every PR. (v0.71.39)
- The `soup ship` regression leg grew teeth: answer-extraction scoring over seven bundled offline suites (MMLU, arithmetic, tool-call, JSON, safety and more), not fifteen substring-matched trivia prompts. Verdicts can flip, because the old gate reported false negatives. (v0.71.38)
- `soup data dedup --semantic` plus `topics`, `canary` and `train --replay`: Data Moat II, a semantic layer over your data plus tools for what a fine-tune forgets and leaks. (v0.71.36)
- `soup init --template hipaa|soc2|eu-ai-act|sr-11-7` plus `soup card` and `soup ci init`: the compliance pack. A regulation-shaped config, a provenance-carrying model card, and a PR gate that blocks a merge on DON'T SHIP. (v0.71.35)
- `soup export --format gguf` is validated end to end on Windows (q4\_0, q4\_k\_m, q8\_0, f16, plus an Ollama round-trip), fixing four bugs including an export that downgraded your CUDA torch. (v0.71.35)
- `soup adapters arithmetic "coder + 0.5*math - toxic"`: task-vector algebra over LoRAs. Add, scale, and actually negate a delta rather than performing the no-op a naive coefficient gives. (v0.71.34)
- `training.lisa_enabled`: LISA re-samples which layers train every N steps, reaching for full fine-tune quality without a full fine-tune's memory. Since measured at 3B and 8B: it beats full fine-tuning on held-out loss, and it trains an 8B on one 80 GB card where full fine-tuning cannot run at all, but it costs **more** memory than LoRA rather than less (1.22x at 3B, 1.51x at 8B). [The numbers](/docs/lisa#measured-at-3b-and-8b-and-half-the-pitch-did-not-survive). (v0.71.34)
- `soup train` with `task: asr` plus `soup infer --task asr`: Whisper fine-tuning with built-in WER and CER. Tiny and base fit a 4 GB card. (v0.71.32)
- `soup train with task: online_dpo` plus `soup data best-of-n` and `evolve`: an LLM judge in the loop across training and data. (v0.71.31)
- `task: grpo` plus `training.prm_reward`: a Process Reward Model grades every reasoning step, the o1-era process-supervision signal. (v0.71.30)
- `soup shrink --drop-ratio 0.25`: depth-prune the least-useful layers, distill-heal the damage, and get a SHIP / DON'T-SHIP perplexity verdict. (v0.71.29)
- `soup mcp serve`: drive Soup from Claude Code, Cursor, Cline or Continue. Stdio only when it shipped; sse and http transports arrived in v0.74.0. (v0.71.28)
- `soup data doctor` and `soup data lint`: 8 chat-template checks including the "never stops generating" EOS bug, plus a preference-data linter. Pre-flight, zero GPU. (v0.71.27)
- `--reward-hack-mitigation kl_control|pid_lagrangian`: detect reward hacking mid-run and self-correct by raising KL, shaping the reward and rolling back, instead of only halting. (v0.71.26)
- `soup ship`: one SHIP / DON'T-SHIP verdict fusing a task win with no catastrophic forgetting. Exit 0 or 2 for CI. (v0.71.25)
- `soup recipes use whisper-tiny-asr`: 167 recipes including Whisper ASR and the 2026 model families (Qwen 3.5 and 3.6, DeepSeek-V4, GLM-5.1, Kimi K2.6, MiniMax M3, Mistral Large 3). (v0.71.24 and v0.71.32)
- `soup spectrum scan --top-percent 50`: rank layers by singular-value SNR and fine-tune only the high-signal ones, with no model load. (v0.71.23)

## See also

- [Layer streaming](/docs/layer-streaming) — the current flagship: the mechanism, the measured numbers and the full refusal table.
- [Scaling a streaming run](/docs/streaming-scaling) — architectures, batch versus gradient accumulation, the VRAM pre-flight, resume and the NVMe disk tier.
- [Preference losses over streaming](/docs/streaming-preference) — DPO, ORPO, SimPO and KTO against a streamed base.
- [v0.74.0: loaded in fp32](/docs/loaded-in-fp32) — the release before the current one, and the ten things it means you should re-run.
- [v0.73.3: four flags that did nothing](/docs/flags-that-did-nothing) — the release before it, contributed end to end.
- [v0.73.2: the release gate](/docs/ship-gate-repairs) — why any ship verdict issued before it is suspect.
- [v0.73.1: the free GPU tier](/docs/free-gpu-tier) — the pre-Ampere repair, and the VRAM pre-flight caught under-predicting.
- [v0.73.0 Borrowed Hardware](/docs/borrowed-hardware) — three days on an 8x H100 box, and what it means you should re-run.
- [Lean install and live wiring](/docs/lean-install-live-wiring) — the full v0.71 line in narrative form.

[PreviousFAQ](/docs/faq)[Nextv0.75.0](/docs/mlx-honours-its-config)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="103-mlx-honours-its-config"></a>

# 103. v0.75.0: MLX honours its config, and unknown keys refuse the load

*Source: <https://trysoup.dev/docs/mlx-honours-its-config>*

**All 60 pull requests in this release came from outside the maintainer, by 22 people.** That is the second release running written entirely by other people, and the fourth in a row whose headline is a flag that validated, was documented, and reached nothing.

Upstream gave it no codename. It titled the release with a sentence again, and the sentence is the finding: on `backend: mlx`, six training options were accepted and read by nothing, so **the same `soup.yaml` trained a different recipe on Apple Silicon than it did on a CUDA box**, silently.

## Re-run this

Fourteen of this release's fixes mean something you already ran was wrong, or was judged on a prompt it never trained on. None of them raised, and most exited 0.

| If you | What happened | What to do |
| --- | --- | --- |
| Ran any supervised fine-tune on `backend: mlx` | `data.train_on_responses_only` defaults to `true` and reached nothing, so the run **trained on your system and user turns as well as the assistant's**, and the adapter metadata recorded `mask_prompt: false` regardless | Re-run. Measured over 16 two-turn conversations: 772 supervised tokens before, 146 with a correct mask |
| Set `training.optimizer`, `scheduler`, `warmup_ratio` or `weight_decay` on MLX | All four were dropped. Every run built a **bare AdamW at a constant learning rate**, whatever the recipe said, and all 32 allowlisted optimizer names became AdamW | Re-run. A name MLX cannot express is refused by name now instead of becoming AdamW |
| Set `training.max_grad_norm` on MLX | It reached nothing, so **nothing clipped**, while the same config clipped at 1.0 on every transformers run | Re-run if you use `optimizer: sgd` or saw gradient spikes. On an Adam-family run the difference is in the fifth decimal |
| Ran MLX with `gradient_accumulation_steps` or `gradient_checkpointing` set | Both took mlx-lm's own dataclass defaults, 1 and `False`, so your effective batch size and your memory saving were not the ones you configured, **and `adapter_config.json` hardcoded both**, so you could not tell from the output afterwards | Re-run. Note the upgrade change below: the default is 4, so an untouched config now trains at a 4x effective batch |
| Selected `grpo_variant: gspo` | The objective centred the per-token log-ratio **across the batch before the completion mask was applied**, so one padding token shifted the loss and gradient of every unmasked row sharing its column, and picked up a non-zero gradient of its own | Re-run. The objective is also replaced entirely, so these runs cannot be reproduced either way |
| Set `training.loraplus_lr_ratio` | It was forwarded to `TrainingArguments`, which has no such field, so **every run that set it crashed** with a `TypeError` before the first step. An advertised, schema-accepted option | Run it. It builds a real PEFT LoRA+ optimizer now, with save and resume state proven to survive |
| Distilled with `uld_strategy: wasserstein` or `topk_align` across two different tokenizers | Both forwarded the student's own token ids to the teacher, clamped into range. Clamping does not translate a token between vocabularies, so the teacher was **conditioned on the wrong text** while the loss stayed finite and plausible | Re-run with `uld_strategy: wasserstein_aligned`. The old run is not salvageable |
| Distilled anything with the default `train_on_responses_only` | The ULD loss ignored the response-only label mask and the causal shift the cross-entropy term already applied, so it **optimised prompt tokens** and the shift-boundary position too | Re-run |
| Chatted with, served, benchmarked, diffed or judged a model on a Llama-3, Gemma or Mistral template | The rendered chat template was handed to the tokenizer, which added its **own** special tokens on top, so inference sent a doubled BOS that training never saw. 2 BOS down to 1 on vendor templates, 1 down to 0 on Soup's own presets | Re-judge and re-benchmark. The weights are fine; `soup ship` verdicts, `soup bench` numbers, `soup diff` comparisons and `usage.prompt_tokens` were all taken on a prompt that differed from training by a token |
| Ran `soup data validate` | It judged a row by top-level key presence while the loader runs the real converters, so the two disagreed. **Six formats skipped validation entirely** and reported every row valid regardless of content: `prm`, `pre_tokenized`, `input_output`, `video`, `multimodal` and `raft` | Re-validate. On upstream's own datasets this shifted 120 of 360 file-by-format verdicts, every one an over-count |
| Used `data.interleave` with the `over` or `probs` strategy | `val_split` ran **after** the padding, and a padded copy is the same row, so one row could land in both `train` and `val`. Your validation metric was computed partly on rows you trained on | Re-run and re-read the metric. Fixed on the eager local-file and all-Hub paths; **the streaming path still leaks** |
| Used `data.streaming: true` with a single Hugging Face Hub dataset name | The flag was ignored and the **full dataset was materialised** | Re-run. It streams now, capped at 1,000,000 rows with a warning |
| Hit `soup eval auto` | It ran the eval, saved the results, and then died with `TypeError: expected str, bytes or os.PathLike object, not OptionInfo`, because an unpassed typer parameter keeps a truthy sentinel as its default. Mid-training auto-eval reported it as a failed eval | The results were already saved. Re-run for the report |
| Exported with `soup export --format awq` and no `--calibration-data` | AutoAWQ **silently downloaded its own large default calibration dataset**, so the artifact was calibrated on data you never chose | Re-export with explicit calibration data. It is required now, and refused before the quantizer is even imported |

One more that is not a run but a dataset: a **non-dict message** in a `multimodal`, `chatml`, `audio` or `video` row raised `AttributeError` out of the converter instead of being dropped, so **one bad line in a large JSONL took the whole dataset with it**. `chatml` is what format detection returns for a bare `{"messages": [...]}` row, which makes it the default path for the most common dataset shape.

## The headline: six options MLX accepted and never read

A field can be declared by the schema, validated on load, printed in the reference, and still be read by nothing on the backend you picked. That is not a hypothetical here: it is the fourth release in a row to fix an instance of it, and this one found six in one backend.

The full table, the measurements behind each, and the allowlists MLX actually supports are on [the MLX backend page](/docs/mlx-backend). The short version:

- **Response-only masking is not comparable between the two backends, and MLX is now the stricter one.** Setting mlx-lm's own flag was not the fix, because it masks a single prefix and supervises only the final assistant turn. Soup injects a per-token mask instead, excludes the assistant header where transformers includes it, and **refuses** a template it cannot align rather than approximating.
- **Only 8 of Soup's 32 optimizer names have an MLX equivalent.** The other 24 are refused by name. Four schedulers are supported, and a non-zero weight decay on an optimizer whose MLX constructor takes none is refused rather than dropped.
- **Schedules are built in optimizer-update units**, not iterations, because that is what MLX drives a callable learning rate from. Measured on Apple Silicon, a `cosine` run with `warmup_ratio: 0.2` now reports 10 distinct learning rates across 40 iterations where the old path reported one.

> **One upgrade change, and it applies to anyone who never touched the field.** `gradient_accumulation_steps` defaults to **4**. An MLX run that used to update the optimizer on every micro-batch now accumulates over four first: a 4x larger effective batch size and roughly a quarter as many optimizer updates for the same `iters`. That is the schema default finally taking effect, so a differently-converging run after upgrading is **expected rather than a regression**.

**One shipped recipe changes behaviour.** `qwen3-8b-sft-mlx` does not set `data.train_on_responses_only`, so it takes the `true` default. Qwen3's chat template injects its thinking block only for the last assistant turn, so multi-turn rows are now **refused** at dataset construction, before the training loop, naming `data.train_on_responses_only: false` as the remedy. Single-turn rows are unaffected, and so are `llama3.1-8b-sft-mlx` and `gemma3-4b-sft-mlx`.

Two MLX recipe repository IDs were also repaired, and one is a **user-visible rename**: `gemma3-9b-sft-mlx` is now `gemma3-4b-sft-mlx`, because there is no 9B Gemma 3 and the old ID raised `RepositoryNotFoundError`. `qwen3-8b-sft-mlx` moved from a non-existent `Qwen3-8B-Instruct-4bit` to `Qwen3-8B-4bit`.

## Two guards for the pattern this release is named for

Fixing six instances of a class is worth less than being able to see the seventh, so this release ships the instruments as well.

**A declared config field that reaches no consumer now fails the test suite.** Upstream publishes the hedge that has to travel with it: a companion issue records the guard's **measured leak**, so it is a ratchet rather than a proof. It catches a field nothing reads; it does not catch a field something reads wrongly.

**`soup doctor --config soup.yaml` lists the settings your config writes that its task and backend do not read.** Only fields you actually set, never schema defaults, each with the reason and the issue that recorded it.

```bash
soup doctor --config soup.yaml
```

The scope is deliberately narrow, and that framing is upstream's own: the table covers `task: sft` on `backend: mlx`, **seven entries**, and every other pair reports nothing rather than guessing. Every one of those seven is already something the MLX trainer warns about at runtime, so the value added is the **timing**, not new knowledge. Backend support is declared by hand rather than inferred, because inference does not work: reachability over the import graph detected none of five independently-known gaps, reading the trainer module alone invents gaps for fields that live in helper modules, and `--dry-run` exits before a trainer is ever constructed.

Two disclosures ride along. Five entries were removed from that table before merge **because the same release wired those fields**, and the guard is what noticed. And the all-clear message **overclaims**: CUDA-only kernels such as `use_liger` are unread on MLX and absent from the table entirely, so read "every setting is read" as the narrower "nothing in the declared table is unread". `soup doctor --config` exits 2 when the config cannot be read, parsed or validated, all three deliberately agreeing so the leg can gate CI.

## Breaking: an unknown config key refuses the load

v0.74.0 reported every key no config model declares, a typo like `quantizaton` or a field that only exists on a newer Soup, as a warning that named v0.75 as the release that would start refusing. **This is that release.**

```text
Config validation error:

  unknown config key 'data.max_len' - did you mean 'max_length' or 'video_maxlen'? Refused.
unknown config key 'training.quantizaton' - did you mean 'quantization' or 'quantization_aware'? Refused.
```

`soup train` exits **1 before the training stack is imported**. `soup sweep`, `soup doctor --config` and `soup ship --config` refuse the same way, and the API and Web UI loader raises `ValueError` with the same text, rendered through the SPA's own escaping. Nothing is defaulted and nothing is guessed: the suggestion is a hint for you, not a substitution the loader makes.

The message says `Refused.` rather than `Not applied.`, deliberately, because the second would read as if the run went ahead without the key. The `soup sweep` guard, which always refused, changes wording the same way.

Three things are worth knowing before you upgrade:

1. **A config that must stay loadable on v0.74 as well needs the key removed, not renamed.** v0.74 warns and ignores it, v0.75 refuses it, and **neither applies it**, so there is nothing to preserve by keeping it.
2. **A root-level `lora:` block is not an unknown key.** That is the LLaMA-Factory and Axolotl spelling the schema has accepted and moved under `training` since v0.40.1, and the detector now shares the validator's remap so a spelling the validator accepts can never be one the detector refuses. The release review caught the first draft refusing it.
3. **`soup plan` and `soup apply` do not run this check**, because they read the YAML as a plain mapping. That gap is filed, not fixed.

Two hardening fixes came out of the same review. Key names reached the terminal unescaped, so Rich markup or raw escape bytes in a YAML key could restyle or spoof it; the loader now uses the shared escaping helper. And the scan was unbounded: 50,000 bogus keys cost about **31 seconds of CPU per Web UI request**, measured. It stops at 100 findings and says so.

All 167 recipes, all 21 templates and the shipped example configs scan clean. Two `soup fetch examples` configs that used the root-level spelling were moved to the canonical `training.lora`.

## Validation loss existed nowhere

It was computed on every backend and thrown away. `SoupTrainerCallback.on_log` read `logs["loss"]` and never `logs["eval_loss"]`, so an evaluation step left the last **training** loss in place and re-reported that to every sink: the evaluated number existed nowhere at all. There was also nowhere to put it, no `metrics` column and no event field, and the display read only `grad_norm`, `speed` and `gpu_mem` out of its keyword arguments.

The live panel, the `metrics` table and the `/api/train/stream` frame now each carry `val_loss` **as its own series, never folded into `loss`**, and the panel gains a `Val loss` row.

The storage rule is the part worth copying:

- The panel **carries the last measured value forward** between evaluations, so the row does not blink.
- The stored and streamed values **do not**. A step where no evaluation ran records `NULL`, so a series read back has one point per measurement rather than one per logged step.
- Existing `~/.soup/experiments.db` files are migrated in place, and rows written before this ship read `NULL` rather than a fabricated `0.0`, **because an unmeasured value must not read as a measured one**.

MLX produces it too, through the hook that had been called on every evaluation and did nothing, because the base-class method is a `pass` and therefore a silent no-op rather than an error. Verified on Apple Silicon with a real validation split: 9 display updates, 5 database rows and 5 stream events for 5 evaluations.

## `torch>=2.6.0`, which closes the limitation v0.74.0 published

v0.74.0 shipped a known limitation rather than hiding it: the declared `torch>=2.5.0` floor **did not work with `trl>=0.29`**, because at 2.5.1 a module TRL imports does not exist, so DPO, KTO, GRPO and BCO were unavailable. pip could not catch it, since TRL declares no torch dependency at all, and CI never saw it because `>=2.5.0` always resolves to the newest torch. A fresh install was unaffected; a pinned 2.5.x environment was not.

That release deliberately refused to bump the floor, because 2.5.1 was measured to fail and 2.6 had **not** been measured to work. This release measured it. The floor is `torch>=2.6.0`, the reason is that TRL 0.29's preference trainers need the public FSDP2 API introduced there, and **CI now proves it** rather than asserting it.

The rest of the stack is unchanged: `transformers>=5.16.1,<6.0.0`, `trl>=0.29.0,<1.0.0`, `peft>=0.20.0,<1.0.0`, `accelerate>=0.27.0`, `mcp>=1.10.0,<3`, Python `>=3.10,<3.13`.

## Breaking: `grpo_variant: gspo` is a different objective

`gspo` was a column-centering heuristic. It is now the published **Group Sequence Policy Optimization** algorithm (Qwen Team, [arXiv:2507.18071](https://arxiv.org/abs/2507.18071)): a length-normalised **sequence** importance ratio with sequence-level surrogate clipping at a default radius of 0.2 or an operator-supplied `grpo_delta`, isolating masked tokens at exactly 0.0 gradient, invariant to padding tokens and to whether they sit left or right, and invariant to batch permutation.

**Existing `gspo` configs will yield different losses and gradients and will not reproduce prior runs.** That is upstream's own wording and it is the whole warning.

`grpo_delta` is now accepted for `gspo` as well as required for `two_sided`, and rejected on every other variant.

## The Langfuse live pull

`soup ingest` has always been a file normaliser: you export from the vendor dashboard, it parses. Langfuse is now the one source Soup fetches for itself.

```bash
export LANGFUSE_PUBLIC_KEY=pk-lf-...
export LANGFUSE_SECRET_KEY=sk-lf-...

soup ingest --source langfuse --pull --since 24h --output traces.jsonl
```

One row per `GENERATION` observation, off the Observations API v2 because `/api/public/traces` leaves Langfuse Cloud on 16 November 2026. The bounds are the interesting half and they are all documented on [the trace ecosystem page](/docs/trace-ecosystem): credentials from the environment only so they never reach the audit log's argv, HTTPS through the same SSRF validator as `--slack-url`, **redirects refused rather than followed with credentials attached**, 30 s per request, 64 MiB per response, and a `--max-pages` cap that **exits 1 and writes nothing** rather than handing over a truncated dataset.

One correction rode along: the hint this path used to print named `LANGFUSE_KEY`, which is **not a variable Langfuse reads**. It names the key pair now.

## Security

- **Web UI read endpoints and SSE streams require authentication.** Run configurations, logs and system metrics answered unauthenticated until now; only `/` and `/api/health` stay open, so the dashboard can still load. SSE authenticates with a **short-lived, single-use ticket** exchanged over an authenticated POST, so a durable token never rides in a query string. A non-loopback bind without a valid token is rejected with exit 2.
- **`soup ui --public` no longer serves the FastAPI docs to the LAN.** `/openapi.json`, `/docs`, `/docs/oauth2-redirect` and `/redoc` are **absent (404)** on a non-loopback bind and unchanged on loopback. Upstream classifies it honestly as **reconnaissance, not disclosure**: every endpoint the schema describes already answered 401 after the fix above, and this predates it. They are removed rather than gated because `/docs` is a browser navigation that cannot carry a bearer header, so gating would have broken the page for a developer while leaving `/openapi.json` readable by any HTTP client.
- **A Web UI training subprocess can no longer hang when no client reads its output.** Output drains into a bounded background ring buffer, with multi-subscriber replay via `Last-Event-ID`.

## Also in this release

- **Multipack FFD placement is O(N log N)**, via a segment tree of per-bin remaining capacity rather than a scan of every open bin. The property that mattered is that **the packing is unchanged**, verified against the old function over 6,000 randomized cases, 5,384 of them with repeated lengths, for zero mismatches: altering which item lands in which bin would silently change every multipack run. Measured on one box, 5.5x faster at 1,000 rows, 37x at 10,000 and 96x at 30,000.
- **`packing: true` no longer raises on TRL 0.29.** It is an `SFTConfig` field and was being passed as an `SFTTrainer` keyword argument, whose `__init__` takes none. Separately, `packing_cross_doc_attn_mask` is now **refused at config load**, because it never mapped to a valid TRL packing strategy on any released version and was always a `TypeError` at setup rather than a working mask.
- **`task: embedding` works again**, in two ways: `lora.r: 0` full fine-tuning no longer raises `Lora rank r must be > 0`, and the embedding trainer no longer crashes after setup because it delegated `train` and `save_model` but not `model` or `args`.
- **PPO forwards `training.epochs` and `ppo_kl_penalty`** to TRL 0.29's own field names, keeping the legacy spellings working. Worth stating because the two `epochs` are different things: `epochs` is passes over the dataset, `ppo_epochs` is optimization passes inside each PPO update.
- **`soup migrate` accepts a valid competitor config named `*.jsonl`.** The guard branched on the filename alone, and the content sniff written to gate it had no call site, so a YAML config saved as `config.jsonl` exited 2 with "got JSONL" and could not be migrated at all. It also reads `utf-8-sig` now, so a BOM written by Windows tooling cannot defeat it.
- **`soup doctor` stops reporting the optional `[train]` stack as missing required dependencies.** A core-only install gets one `pip install "soup-cli[train]"` suggestion, with the CUDA wheel index on NVIDIA hardware, instead of bare per-package floors.
- **Terminal charts route through Rich**, so `NO_COLOR` and redirected output carry no raw ANSI escapes while interactive charts keep their colour.
- **The GEMM throughput forecast measures in the card's resolved stream dtype**, `bfloat16` where the hardware has it and `float16` otherwise, instead of hard-coding bf16, and it prints the dtype beside the TFLOPS and the clock.
- **A Turkish `README.tr.md`**, behind a CI gate that checks what a translation was synced **from** rather than only when. Every translation carries a `synced-from` stamp over LF-normalised bytes, so a CRLF checkout on Windows agrees with Linux and macOS; translations are found by glob, so a new language cannot land unchecked; and each section must keep the original's fenced-code languages, external URLs and inline-code spans, **in both directions**. Run against the previous draft, that last check found 29 dropped and 3 invented code references, including two release-note bullets that do not exist in the English README.
- **Four new recipes** take the catalog to **167**: `deepseek-v4-flash-dpo`, `kimi-k2.6-dpo`, `qwen3.5-0.8b-grpo` and `qwen3.5-2b-grpo`. The two DPO recipes carry upstream's own rider: they are **not trained**, because those bases are MoE and multi-node, so no hyperparameter in them is a measured recommendation. Their values are stated as consistency with their siblings instead, and the two GRPO recipes say explicitly that they follow the GRPO templates rather than inheriting their SFT siblings' values.

## What was measured, and what was not

**No maintainer gate, and upstream says so plainly: nothing in this release was gated by a new measurement.** Three contributor records landed in the window instead, and all three are in the public [benchmarks directory](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks).

**A pinned CUDA host allocation does not consume `/dev/shm`.** Measured on an NVIDIA L4, two fresh-process pinned runs each added **exactly 4 GiB to `RssShmem`** with no change to `RssAnon` and **no change to `/dev/shm` usage**, while the pageable control did the opposite. The conclusion is a design one: the streaming pinned-store path does not need a `/dev/shm` free-space pre-flight. The record is careful about what it does not establish, and so are we: it does not cover other drivers or kernels, it says nothing about reclaimability, and its host-wide counters are explicitly **not attributable** to the allocation, because other tenants shared the box.

**A QuEST W4A4 supervised gate failed, and is published as written.** Its own first line is the headline: \*gate failed, 0.114 nat, one training seed, one model, fake quantization, not parity, not an integration, not an efficiency claim.\* The failure criterion was **preregistered** and both halves of it failed. No arm was promoted, the reserved confirmation panel was never touched, and a missing provenance field was left missing rather than backfilled, with the record stating that a driver version queried two days later is **not evidence of the driver used on the day**. There is no QuEST option in Soup and none is implied.

**An 8 GB M1 MLX run, whose own header says it is not a gate.** What it establishes: the shipped `llama3.1-8b-sft-mlx` recipe trains on an 8 GB Mac, **48 iterations in 71 s at a 5.154 GB peak**, with the adapter written and reloadable, and dispatch asserted before the timer started so a transformers-path number could not be published as an MLX one. The mechanism is the useful part: **a model too big for RAM there does not fail, it pages**, because MLX memory-maps weights, so low free memory is the normal shape of this workload and **an allocation-failure check would not fire**. That is the WDDM spill trap arrived at from the opposite platform. What it does not establish is longer than what it does, and the record says so: no correctness, gradient-exactness or quality claim, the loss curves are memorisation over 48 repeated synthetic rows, and **every throughput figure in it is an order of magnitude rather than a benchmark** — re-running one model at the same config from a warm cache gave a **3.5x** different rate.

**The preprint is untouched.** No measured number moves and the scope does not change, because nothing in this window touches layer streaming's mechanism or its architecture list. It stays scoped to v0.73.0, as its own header says.

## Known limitations

1. **The unknown-key refusal is a hard break** for a config that was silently carrying an unknown key. v0.74 warned and ignored it, v0.75 refuses it, and neither applies it.
2. **`soup doctor --config` knows seven settings on one task and backend pair**, and reports nothing elsewhere rather than guessing. The field-consumer guard behind it has a measured leak, and its all-clear message overclaims.
3. **`soup plan` and `soup apply` do not run the unknown-key check.** `soup draft distill` and `soup shrink` surface the loader's `ValueError` as a raw traceback. Six command modules still carry a private copy of the terminal-escaping helper the loader now imports from one place. The Web UI's YAML endpoints have no request-size cap.
4. **Streamed-NF4 bit-exactness does not hold on Blackwell.** Two CUDA-only tests fail on an RTX 5070 (`sm_120`) at **4.9e-4** and **3.9e-3**, while the `quantization: none` variants **pass** — so the divergence is in the bitsandbytes NF4 path on that card rather than in layer streaming. **CI has no GPU runner and cannot see it, and the root cause is not established.** It is not the same defect as the one v0.73.0 repaired, which had a megabytes-per-layer boundary rather than a card-architecture one, and unlike that one **this is not fixed**. See [what "bit-exact" does and does not mean](/docs/layer-streaming).
5. **The Turkish README was re-synced for this release by release tooling, not by its translation owner.** It passes the structural gate; the contributor's polish is the standard it was merged under.
6. **The reward-hack mitigation controller has never had a valid `pid_lagrangian` run.** The mechanism is implemented and the mode is selectable; its efficacy is not established.
7. **Layer streaming remains BETA.**

## See also

- [Apple Silicon MLX backend](/docs/mlx-backend) — the six options, both allowlists, the dashboard bridge and `soup doctor --config`.
- [Configuration](/docs/configuration) — what an unknown key does now, and the two exceptions.
- [Layer streaming](/docs/layer-streaming) — the flagship, unchanged in this release, and the Blackwell qualification on bit-exactness.
- [Trace ecosystem](/docs/trace-ecosystem) — the Langfuse live pull and its bounds.
- [v0.74.0: the base was loaded in fp32 the whole time](/docs/loaded-in-fp32) — the release before this one, and the ten things it means you should re-run.
- [Everything new across v0.71 to v0.75](/docs/whats-new).

[PreviousWhat's new](/docs/whats-new)[Nextv0.74.0](/docs/loaded-in-fp32)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="104-loaded-in-fp32"></a>

# 104. v0.74.0: the base was loaded in fp32 the whole time

*Source: <https://trysoup.dev/docs/loaded-in-fp32>*

**116 of the 120 pull requests merged into this release came from somebody other than the maintainer, by 25 people.** The maintainer's own four were a DeepSpeed guard, a dependency-drift job, an MCP compatibility layer, and the CI fix that stopped that same drift alarm firing every Monday.

Upstream gave it no codename. It titled the release with a sentence instead, and the sentence is the finding: a LoRA run freezes the base, the frozen base never receives an optimizer step, and every supervised load path was materialising it at **twice its checkpoint's precision** anyway.

## Re-run this

Ten of this release's fixes mean something you already ran was wrong, silently. None of them raised, and most of them exited 0.

| If you | What happened | What to do |
| --- | --- | --- |
| Wrote a config key the schema does not declare | It was **silently dropped**. `training.quantizaton: none` trained 4-bit, `training.gradient_checkpoint: true` did no checkpointing, `data.max_len: 512` truncated at 2048, and `soup train --dry-run` printed "Config valid" | Re-load the config on v0.74.0 and read the new unknown-key report. A typo'd key trained at the default |
| Ran `soup sweep --param <name>` with a name that is not a config field | The whole grid ran at the base config's value, every arm identical, and a "winner" was reported | Discard that sweep. The parameter is checked before the first arm now, and exits 1 |
| Used `data.interleave` for a multi-dataset mixture | Nothing read it at training time. Every mixture **trained on `data.train`'s single path**, since v0.42.0 | Re-run. The mixture is real now, and covers streaming and Hub datasets too |
| Resumed an MLX run with `--resume auto` or `--resume <path>` | mlx-lm saves `NNNNNNN_adapters.safetensors`, not `checkpoint-N`, so nothing matched and **training restarted from scratch every time** | Re-run. What ships now is a weights-only warm start, and it says so |
| Selected a GRPO objective variant (`gspo`, `dapo`, `dr_grpo`, `bnpo`, `two_sided`, `rft`) | The variant check read a field TRL never pre-populates, so every run **fell back to stock GRPO loss** | Re-run. You did not train the objective you selected |
| Set `training.quantize_reward_model` | Validated by its own task-scoped check and then read by neither loader, since v0.53.0. PPO's reward model and `task: reward_model` **quantized regardless of its value** | Re-run if the flag's value mattered to you |
| Set `use_cut_ce` on a model loaded from a local directory | Architecture detection matched a keyword against the **path's last component**, so `checkpoint-2000` or `my-finetune` matched nothing and cut-cross-entropy stayed off, on a flag you explicitly set. Phi-2 also ran under the Phi-3 patcher | Re-run if you were counting on the memory saving |
| Ran `soup ship` on a 4-bit or 8-bit adapter | The judge loaded the base at full precision, so an **NF4-trained adapter was judged against a bf16 base it never saw** during training, and the message claimed bf16 without setting a dtype | Re-judge with `soup ship --config soup.yaml`, which now derives the precision from the run's own config |
| Used `batch_size: auto` on Windows or WSL2 | The probe's only fit test was "the synthetic step did not raise", and under the WDDM driver an over-commit does not raise: it spills into host memory. A batch that ran an order of magnitude slower in shared memory was approved **and cached** | Re-probe. The fit is decided on a measured peak now, and the cache key carries a version tag so old entries are ignored rather than trusted |
| Gated training on an LLM-judge eval | The gate divided the aggregate score by 10 while the default rubric is 1 to 5, so a perfect 5.0 read as **0.50** and typical thresholds were impossible to satisfy, stopping healthy runs under `on_regression: stop` | Re-check any run that stopped early on a judge gate |

Two exports were worse than wrong, they were empty or unloadable: `soup export --format tensorrt` shelled out to a module that exists in no current TensorRT-LLM release and **produced zero artifact bytes**, and `--format gptq` wrote only a shard name `from_pretrained` does not look for. Both are repaired, and GPTQ now requires `--calibration-data` up front instead of crashing without it.

## The headline: an unchanged config paid twice

A LoRA or QLoRA run has exactly one trainable thing, the adapter. The base is frozen. Its only job is to hold the numbers that are in the checkpoint.

All three `from_pretrained` call sites in the supervised trainer, text, vision and audio, passed **no dtype at all**, so a bf16 checkpoint was materialised as fp32.

```text
Measured on an H100, Llama-3.1-8B, LoRA, frozen base:

  peak before   48,241 MiB
  peak after    18,658 MiB
  saving        28.9 GB  (2.59x)

  byte-identical across 3 repeats
```

Three things must travel with that number.

1. **It is a saving on a configuration that was already paying it**, not a new capability. Upstream's own wording is "cuts peak VRAM 2.59x on an unchanged config".
2. **It applies to a frozen base only.** A genuinely trainable base, meaning `lora.r: 0`, `unfrozen_parameters` or `lisa_enabled`, still loads fp32 master weights, deliberately and documented.
3. **It is one measurement**, carried over from the original pull request rather than re-measured, and it states its hardware, model and adapter and nothing else. No sequence length, batch size or checkpoint dtype is published, so none should be quoted.

The same defect stood untouched in **twelve more trainers**: `dpo`, `kto`, `orpo`, `simpo`, `ipo`, `bco`, `online_dpo`, `grpo`, `ppo`, `pretrain`, `reward_model` and `embedding`. None of them has a full fine-tuning branch, so every load there is a frozen base. They share one resolver now, with a pre-Ampere exception: on a card whose compute is fp16 anyway, the frozen base loads `torch.float16` explicitly rather than sitting in bf16 storage.

One structural repair rides along and is the reason the class existed. The "is this a full fine-tune?" question was answered by **two independent copies** of the logic, one in the trainer and one in the VRAM pre-flight, and they disagreed in both directions. There is one shared discriminator now.

**This does not change the layer-streaming laptop figure.** That run streams an NF4 base and never had a resident fp32 one, so 3.32 GB is untouched by this fix. See [what changed under layer streaming](#what-changed-under-layer-streaming) for the one number that did move.

## The stack moved: Transformers 5.x, TRL 0.29, PEFT 0.20

```text
torch          >=2.5.0
transformers   >=5.16.1,<6.0.0
trl            >=0.29.0,<1.0.0
peft           >=0.20.0,<1.0.0
accelerate     >=0.27.0
mcp            >=1.10.0,<3      ([mcp], the <2 cap is lifted)
python         >=3.10,<3.13      (unchanged)
```

The APIs that moved into TRL's experimental namespace are reached by **capability probe rather than by a version table**, which is the rule this project earned the hard way: a version table was wrong twice, and both times the thing that settled it was constructing the object.

The visible payoff is small and long overdue. `pip install "soup-cli[train,mlx]"` **resolves again**: the two extras had declared transformers ranges that could not be satisfied together at all, so anyone who wanted Apple Silicon and the training stack in one environment was simply stuck. A new weekly dependency-drift job found that before it merged, by installing the latest resolvable stack and writing a resolved-versus-declared table into the run summary.

> **Known limitation, published rather than discovered.** The declared `torch>=2.5.0` floor **does not work with `trl>=0.29`**. At torch 2.5.1 a module TRL imports does not exist, so TRL cannot import at all and DPO, KTO, GRPO and BCO are unavailable. pip cannot catch it, because TRL declares no torch dependency; CI never sees it, because `>=2.5.0` always resolves to the newest torch. **A fresh install is unaffected. An environment pinned to 2.5.x is not.** No floor bump ships, because 2.5.1 was measured to fail and 2.6 was not measured to work.

## The free notebook tier could not stream, for a second reason

v0.73.1 removed a bf16 assumption made in fourteen places, which had broken **every** task on every pre-Ampere card. Layer streaming still crashed there, on a different defect entirely:

```text
_amp_foreach_non_finite_check_and_unscale_cuda not implemented for 'BFloat16'
```

PEFT creates LoRA adapters in the **base checkpoint's dtype**, while the fp16 gradient scaler those cards use requires fp32 gradients. Trainable adapter parameters are now cast to fp32 before the optimizer is built, from every trainer's own entry point through one shared helper.

The exclusion is deliberate and worth knowing: `lora.r: 0`, Spectrum and LISA full-fine-tune paths are **untouched**, so trainable memory cannot double after the VRAM pre-flight has already approved the run.

**No pre-Ampere measurement was added.** Everything [the free-tier page](/docs/free-gpu-tier) says about what a T4 run does and does not establish still holds: no throughput is quoted from a capped card, and backward exactness on Turing remains unshown.

## What changed under layer streaming

The allowlist goes from nine architectures to **ten**, and the tenth is stated carefully because only the original nine are verified bit-exact in both bf16 and NF4.

| Family | How it got in | What is verified |
| --- | --- | --- |
| `llama`, `qwen2`, `qwen3`, `mistral`, `gemma`, `gemma2`, `gemma3_text`, `phi`, `phi3` | The original nine | Bit-exact against the same checkpoint loaded resident, under both bf16 and NF4 |
| `qwen3_5`, `qwen3_5_text`, `qwen3_5_moe`, `qwen3_5_moe_text` | Aliases routed onto the qwen3 streamer | Bit-exact against resident controls **on CPU**. The MoE path was validated live on Qwen3.5-35B-A3B with NF4, MoE LoRA and a 3072-token dataset, with **no resident control**, because no available machine can hold it resident |
| `qwen4_exp`, `qwen4_exp_text` | The tenth family | An exact **float32 tiny-model** parity gate, including its external N-gram table. Real-checkpoint and NF4 validation are still pending |

**No throughput figure exists for any of them**, and none is claimed. The task allowlist is unchanged at five: `sft`, `dpo`, `orpo`, `simpo`, `kto`. GRPO and PPO stay permanently excluded.

Two mechanical changes matter more than the list.

**An untied embedding and LM head no longer both stay resident.** They are sharded separately and reuse **one** vocabulary-sized device buffer. That is the 2.10 GB which dominated the 8B row's 3.32 GB peak, so the peak has moved, and it is deliberately **not restated**: it has not been re-measured on the reference 4 GB card, and upstream's own docs say the historical figure is not being relabelled as a new one. Tied embeddings keep their existing resident path and numerics.

**`training.stream_pin` makes page-locking an explicit choice.** Until now pinning was chosen automatically and nothing could override it, which mattered while the NF4 gradient defect was live, because a pageable store was the only known mitigation and it was unreachable from `soup.yaml`.

```yaml
training:
  stream_layers: true
  batch_size: 1       # 'auto' is refused on a streaming run
  stream_pin: false   # force the pageable store; the pre-flight prints the cost
```

- `false` forces the pageable store and the pre-flight **states what it costs**, up to the 6.56x already on record, rather than absorbing it silently.
- `true` forces the pinned store and, **on the RAM tier**, refuses if the box cannot page-lock it, naming the **store size** rather than a ceiling: the page-lock ceiling is left unprobed on purpose, so a refusal can never cite a figure nobody measured.
- On the disk tier and on CPU there is nothing to page-lock, so `true` is announced and the run **proceeds** rather than bricking the large-model runs the disk tier exists for.
- Setting it while `stream_layers: false` is rejected, like the other stream keys.

Also here: `stream_source: auto` now falls back to the disk tier when the store fits available memory but store-plus-extras would cross the physical-host safety ceiling, and a forced `ram` refuses at pre-flight instead of letting the kernel OOM-kill the process; the shard cache reuses ordinary Hugging Face cache files and pre-flights its writes per volume instead of exhausting the disk; a fully cached snapshot can be sharded with outgoing traffic disabled; Apple internal NVMe behind APFS is detected without an override; and `training.stream_ngram_source` (`auto`, `ram`, `disk`) governs read-only access to Qwen4-Exp's external N-gram table.

## The MCP server got network transports

Until now `soup mcp serve` was **stdio only**, which suits a client that spawns Soup as a subprocess and leaves remote or multi-client setups with nothing.

```bash
soup mcp serve --transport sse --host 127.0.0.1 --port 8765 --auth-token "$TOKEN"
```

Both new transports serve the **same** registry, and the end-to-end test compares advertised tool names against the registry rather than a hardcoded count, so a subset cannot creep in. The tool count is unchanged at **18**.

Adding a listener is the risky part, so it is gated three ways:

1. **Every request needs `Authorization: Bearer <token>`**, compared with a constant-time check, with no opt-out, because a loopback port is reachable by every process on the box. The token travels in the header only, so it cannot land in an access log, and it is validated by the same helper `soup ui` uses rather than growing a second format.
2. **DNS-rebinding protection is on**, returning 421 on a foreign `Host` and 403 on a foreign `Origin`. That is the gate a token cannot be: a page the operator merely visits sends no `Authorization` header, and its request still reaches the port.
3. **Binding off loopback warns**, and a wildcard bind warns again that the host check has nothing left to pin.

`--allow-execute` is **refused** with either network transport, in the command and again in the app factory, so a direct caller cannot put an executing registry behind a listener either. The reasoning is stated rather than assumed: gated execution spawns real training and export processes, and behind a listener a leaked bearer token would mean process execution rather than plan disclosure, while stdio is a pipe to a client the operator already started. `--host`, `--port` and `--auth-token` are refused under `--transport stdio` rather than silently ignored.

The server also runs on **both major versions of the MCP SDK** now, which lifts the below-2.0 cap that had pinned anyone wanting 2.x in the same environment. The major is chosen by **probing the server constructor**, never by reading a version string, and a test walks the syntax tree to enforce that. The floor moves to 1.10.0, measured against published wheels: the transport-security module a listener depends on first appears there.

> **Still stale at this tag.** The `--help` text for `--allow-execute` and `--allow-mutating` was not updated by either feature and still describes execution as reserved for the future. The startup banner was fixed. The changelog, the command reference and the running code all agree that it executes.

## Unknown config keys stop being silent

None of the config models overrode the library's default of ignoring undeclared keys, so a key the schema did not know validated clean and was **discarded**.

Loading a config now walks the whole model tree, `data`, `training`, `training.lora` and the rest, so a guard applied to one model and forgotten on another cannot look like it works, and reports every key it cannot place in **one** report, naming the field you probably meant.

```text
unknown config key 'training.quantizaton' - not applied. did you mean 'quantization'?
```

**It is a warning, not a refusal**, so a config written against a newer Soup still runs on an older wheel. **From v0.75 the same config will fail to load.** That deadline is one minor away, it is named in the message rather than left as a permanent notice, and it is asserted against the declared version by a test, so the release that crosses it turns a test red instead of shipping a promise it already broke.

`soup sweep` is stricter, and the split is deliberate: a swept parameter that matches no config field produces a grid of identical arms and a meaningless winner, and there is no partially useful result to preserve. It **exits 1** before the first arm starts. `soup sweep --dry-run` now validates too, where it used to return before the config was ever loaded.

## Breaking changes

- **`soup serve` exits 2**, rather than printing a warning, when bound to a non-loopback host without `--tool-auth-token`. The `/v1/tools/bash` endpoint it protects has been re-enabled under real operating-system namespace and sandbox isolation, so it now actually executes code, and a warning was no longer a sufficient control. The endpoint fails closed with HTTP 501 anywhere strict isolation is unavailable, Windows included.
- **The SGLang backend obeys `--trust-remote-code`.** It was hardcoded on at both runtime call sites, so `soup serve --backend sglang` executed a model's custom repo code whether or not you opted in. The warning panel said so, but a notice is not a gate. A custom-code model on that backend now fails to load without the flag.
- **`soup sweep` exits 1** on a `--param` that matches no config field, where it used to run the grid and report a winner.
- **`soup export --format gptq` requires `--calibration-data`**, because auto-gptq has no built-in fallback dataset. It used to crash instead.
- **`soup data best-of-n --export-candidates --seed N` produces different output**, because each prompt is now seeded independently so a resumed run reproduces the same candidates.

## Security

Four spellings of one bypass, closed on **both** validators. The private-address check delegated to a parser that rejects non-canonical IPv4, while the OS resolver on Linux accepts it, so abbreviated (`127.1`), decimal (`2130706433`), hexadecimal (`0x7f000001`) and octal (`0177.0.0.1`) forms reached the telemetry and webhook guards. That matters because the cloud metadata address `169.254.169.254` has a decimal spelling, and a crafted webhook URL could reach it.

The **OTLP tracing endpoint validator** had the same hole through a path the first fix never touched, and the reachable half there was not loopback but non-loopback private ranges in alternate encodings. Telemetry validation also gained a tiered guard: an allowlist for the canonical endpoint with zero DNS lookups, static rejection of internal TLD suffixes, and a defence-in-depth resolution step that fails closed on resolver errors.

While consolidating it, an audit found the predicate had drifted into **three copies of the function and six of the host set** across six modules. All six import one definition now, and a guard test walks the source for a reappearing duplicate.

## Also in this release

- **`soup eval aider`** runs Aider's Polyglot code-editing benchmark through its official Docker harness, behind a new `[aider]` extra, recording the score in `eval_results` for the existing run comparison. The benchmark image is source-built by you; the docs say so rather than implying a one-line setup.
- **`soup train --cloud lambda`** plans a Lambda Cloud GPU run, plan-only by default. The API key never enters the instance: termination belongs to a local controller, and the `finally` both terminates and polls to confirm it happened.
- **`soup monitor` reads real Apple Silicon telemetry**, rendering GPU utilisation and power in the existing table. NVIDIA-only fields stay **unavailable rather than guessed**.
- **`soup data best-of-n` samples from Ollama or vLLM** with `--provider`, through the existing SSRF-validated seam, and gained a durable two-phase offline workflow with per-prompt checkpoints and manifest-last publication.
- **`data.interleave` is read at training time**, finally, and `data.train` accepts a list. Local files combine with `concat`, `under`, `over` or `probs`; streaming and Hub-name lists are dispatched to the datasets library so the strategy names mean the same thing on both paths. A single path stays byte-identical.
- **LISA accepts `task: pretrain`**, which is the same rotating-full-fine-tune mechanism it was built for, and **`training.lisa_train_embeddings`** lets you freeze its always-on group. That group is about **70% of everything LISA trains at 8B**, so freezing it is a real quality-versus-memory trade rather than a free win, which is why it is opt-in. The analytical pre-flight does not credit the saving yet, so a frozen-embeddings run that would fit can still be refused; `--allow-oom-attempt` launches it anyway.
- **Baseline eval artifacts carry a provenance stamp**, the Soup version and a scorer revision, written by `soup eval gate --write-baseline`. A stale baseline is now detected by provenance instead of by a hardcoded suite list, and the v0.73.2 name-based warning is gone.
- **SmolVLM and Idefics3 vision SFT reaches real training batches**, keeping messages and images together until collation and letting the processor produce image-token expansion. That recipe had been parse-only since v0.71.32.
- **Cross-tokenizer drafts** work in `soup draft distill` and `soup draft measure`, and in `soup serve --speculative-decoding` where the installed transformers supports universal assisted decoding. Same-tokenizer pairs keep the existing fast path.
- **Nineteen recipes** take the catalog to **163** (the release body says fourteen; nineteen is what counting `RecipeMeta(` at both tags reproduces, and 163 is the total both agree on), including Qwen2.5-Coder and Qwen2.5-Math sizes, the DeepSeek-R1-Distill families in SFT and DPO, SmolLM3, and GRPO and DPO variants for the 2026 MoE giants. Every recipe's **resolved** config is now pinned against a committed snapshot, so a schema-default change can no longer silently retune a recipe that relied on that default.
- **The DeepSpeed empty-LoRA-group guard went from one wrapper to all eighteen that needed it.** v0.73.0 fixed the failure where LoRA leaves one of Hugging Face's optimizer parameter groups empty, DeepSpeed drops it and the scheduler then hits a strict length check, but it fixed it in `sft.py` alone: nineteen modules accept a `deepspeed_config` and exactly one called the guard, so eighteen tasks still died the same way. Coverage is now enforced by a **scan over the trainer directory** rather than a hand-written list of names, because a hand-written list is what hid them. In the same change, a `--deepspeed my.json` of your own is resolved the way a preset is.
- **The SGLang backend got the two repairs vLLM got in v0.73.0.** It applies the served model's own chat template through the shared builder instead of a third hand-rolled copy, and reports `finish_reason: length` on a truncated response instead of a hardcoded `stop`, on both the sync and streaming paths. Its tokenizer load now uses the same `trust_remote_code` setting the runtime does. Live verification against a real SGLang runtime on Linux is still open.
- **The DeepSpeed-MII backend got the same pair**, which makes it the third backend to have carried it.
- **The live training panel stopped under-reporting GPU memory.** It sampled `memory_allocated()` between steps, after activations and gradients were freed, so it reported the inter-step trough: on the reproducing run `5.8/15.9 GB` while the device was fully occupied. It now reads the lifetime peak and labels the figure `GPU peak:` so it says what it is.
- **`soup doctor` recommends a CUDA wheel that matches your driver** rather than always suggesting `cu121`. A driver at CUDA 11.8 gets `cu118`; an unreadable driver header falls back to `cu121`, which is the conservative direction. On Windows it also notes that the PyPI torch wheel is CPU-only.
- **`soup mcp runs reconcile --expunge-launching`** recovers execution capacity from stale rows without editing the database by hand, and refuses the whole operation if any candidate records a process that is still alive.

## What was measured, and what was not

**No new throughput number was published in this release, and no streaming speed measurement was made.** Two records were added to the public benchmarks directory, and neither is a speed claim.

**A second box says the pre-flight under-prediction does not reproduce.** v0.73.1 disclosed that the streaming VRAM pre-flight breaks its own never-under-predict contract at long sequence on the reference laptop: 0.934x the real peak at sequence 5120, 0.787x at 6144. A contributor ran the same sweep on an A10G with a much newer stack, and the ratio is **flat at about 1.16x over-prediction** from 2048 through 6144, on two models with a 3.1x vocabulary contrast. The loss term measures **12.0 with zero spread** there, a third stack agreeing, and the retained copy the laptop's arithmetic implies is **absent**. The record publishes its own leading hypothesis as a **negative result** with a positive control, and explicitly does not extend it to the laptop, whose driver, operating system and torch are all different. The honest reading is the record's own, and it keeps both halves: the term varies **per-stack and per-sequence-length**, so no constant can carry the never-under-predict guarantee across stacks. That is the argument for [measuring one real step](/docs/streaming-scaling) rather than adding another coefficient to a formula. The box was an NVIDIA A10G 23 GB on AWS `g5.xlarge`, Ubuntu 22.04, torch 2.13.0+cu130 with transformers 5.16.1, trl 0.29.1 and peft 0.20.0, against the laptop's Windows 11 / torch 2.5.1 / transformers 4.57.6, a whole major version apart.

**An Apple Silicon Qwen4-Exp gate is a partial pass.** All 1,167 expected tensors mapped with none missing or mismatched, the affine vectors matched at four bit widths, the tiny parity gate passed, and a 176.9-billion-parameter checkpoint reached "Training started!" with no key, shape or routing error. Then the one-step run **stopped without completing an optimizer step**, and the record's own verdict is that this is **not validated**. Its closing line is worth quoting: do not market it as proof that the full model is trainable on a 128 GiB Mac.

**The preprint is untouched.** No measured number in it changes. Its **scope** is now narrower than the code, because it states nine streaming architectures and the code admits ten, and it stays explicitly scoped to v0.73.0.

## Known limitations

1. **`torch>=2.5.0` and `trl>=0.29` are incompatible at the declared floor.** A pinned 2.5.x environment loses DPO, KTO, GRPO and BCO. No floor bump ships, because 2.6 was not measured to work.
2. **`soup doctor` never reports MLX**, and the MLX version always reads "unknown". Filed, fix in review.
3. **The `--allow-execute` and `--allow-mutating` help strings are stale** in the shipped binary and still describe execution as reserved.
4. **Qwen4-Exp streaming is float32-parity only.** Real-checkpoint and NF4 validation are pending, and no CUDA bf16 parity gate has been measured.
5. **Apple Silicon streaming is experimental.** No claim is made that it fits a larger model or runs faster than resident MPS training, and `backend: mlx` is still rejected with `stream_layers`.
6. **The 8B streaming peak has not been re-measured** after untied embeddings started sharing a buffer. The historical 3.32 GB figure is published as what it was, not relabelled.
7. **The LISA pre-flight still treats it as full fine-tuning** regardless of `lisa_train_embeddings`, so a frozen-embeddings run that would fit can be conservatively refused.
8. **Layer streaming remains BETA.**

## Where that work gets handed out

This release was written by other people, and the next one is being written the same way. The issues, the hardware still to be tested on and the benchmarks still to be run are posted in the **[Soup Tasters](https://t.me/souptasters)** Telegram channel, alongside the [help wanted](https://github.com/MakazhanAlpamys/Soup/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) filter on GitHub. One issue, one person: claim it in the thread, open a pull request, and a merged one puts your name in `CONTRIBUTORS.md`.

Measurements count as much as code, and for a specific reason. **Soup sends nothing about your runs unless you ask it to**, and as shipped it sends nothing even then, because the bundled telemetry key is a placeholder the sender refuses. That is a deliberate choice, [documented in full](/docs/tracker-eval-pro), and its cost is that a run nobody reports is a run nobody learns from. Training something on your own GPU, comparing it against Unsloth or Axolotl, and sending the numbers and the logs is the other half of the contribution. Two of the measurement records published in this release, [the A10G pre-flight sweep and the Apple Silicon mapping gate](#what-was-measured-and-what-was-not), arrived exactly that way, on hardware this project does not own.

## See also

- [The MCP server](/docs/mcp-server) — the network transports, the bearer gate, and all 18 tools.
- [Layer streaming](/docs/layer-streaming) — the mechanism and the measured numbers.
- [Scaling a streaming run](/docs/streaming-scaling) — architectures, the VRAM pre-flight and the disk tier.
- [v0.73.3: four flags that did nothing](/docs/flags-that-did-nothing) — the release before this one, and the two items it left open.
- [v0.73.1: the free GPU tier](/docs/free-gpu-tier) — the first pre-Ampere repair, and what a capped T4 run does not establish.
- [Everything new across v0.71 to v0.74](/docs/whats-new).

[Previousv0.75.0](/docs/mlx-honours-its-config)[Nextv0.73.3](/docs/flags-that-did-nothing)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="105-flags-that-did-nothing"></a>

# 105. v0.73.3: four flags that did nothing

*Source: <https://trysoup.dev/docs/flags-that-did-nothing>*

**Every one of the 24 pull requests in this release came from someone other than the maintainer.** Eight people, five of them appearing here for the first time. The maintainer's own work in that window arrived as four direct commits: license headers, a test repair, a CI guard.

That is worth stating plainly because of what outside eyes found. Not a missing feature, and not a crash. **Four separate flags that the schema validated, the documentation described, and nothing in the codebase ever read.**

## Re-run this

| If you | What happened | What to do |
| --- | --- | --- |
| Trained with assistant-only loss masking | The tokenizer returns a mapping that is **not** a `dict`, so a type guard missed it and the label mask was built from the mapping's **key strings**. No exception, no warning, a normal-looking loss curve, and **zero trained tokens** | Re-run. An adapter from such a run learned nothing |
| Trained on Apple Silicon with `quantization: 4bit` | Device detection did not know MLX, so the run reported "CPU (no GPU detected)" and **silently rewrote `4bit` to `none`** | Re-run if you needed 4-bit. The run did train, just not at the precision you asked for |
| Followed the command `soup train --no-reexec` printed | The printed hint dropped the flags you actually typed, so following it literally trained **without `--fsdp`** — and the run succeeded, so nothing pointed back at the hint | Re-run under the flags you meant |
| Set `training.bnb_4bit_use_double_quant: false` | Nothing read it. Every 4-bit path hardcoded double-quantization **on**, so the setting changed your config fingerprint and nothing else | Nothing to re-run: you got the default. But the key is live now, so the same config will train differently from here |

One more consequence of that last row, and it is cosmetic rather than a correctness problem: because the resolved config now carries the field, a config that never set it will show a **one-time fingerprint drift** in `soup ship --evidence` provenance and `soup lock check`, with the model numerics unchanged.

## Four flags that did nothing

### `training.bnb_4bit_use_double_quant`

Every place Soup builds a `BitsAndBytesConfig` hardcoded `use_double_quant=True`. The flag is now threaded through the three call sites Soup owns: the resident loader, the layer-streaming path (which reads it **once** and passes the same value to both the sharder and the meta skeleton, so streamed-versus-resident bit-exactness cannot drift), and the 4-bit save path.

The design choice is the more interesting half. The field is `Optional[bool]` defaulting to **unset**, not a plain `true`, because a `true` default emits the key into every dumped config and trips the "requires `quantization: 4bit`" guard on re-validation. That was measured, not guessed: **21 of 173 shipped configs** stopped round-tripping, which would have broken `train --replay` and `soup sweep`. So unset resolves to the shipped default, an explicit `false` now genuinely disables, and only an explicit `true` fires the footgun check.

**One path cannot honour it.** The Unsloth loader builds its own `BitsAndBytesConfig` internally with double-quant hardcoded on and exposes no override, so it is out of scope by construction rather than by omission.

A matching CLI flag lands with it:

```bash
soup merge --adapter ./output --save-format 4bit --no-double-quant
```

It applies to the `4bit` and `4bit_forced` save formats and is ignored for `fp16`.

### Apple Silicon was read as a CPU

`detect_device()` only probed PyTorch MPS and fell back to `'cpu'`, which fired a false "4bit quantization is not supported on CPU" warning and took the quantization down with it. **The label was never the harm.**

Both `detect_device()` and `get_gpu_info()` now take an optional backend. With `backend: mlx` they resolve to `mlx` with the chip name, report Apple unified memory in telemetry, and preserve `quantization: 4bit` for pre-quantized `mlx-community` checkpoints, which is a different thing from bitsandbytes NF4 and was never the CPU case the warning was written for.

The decision itself moved out of a branch buried in a long function and into an explicit, testable `resolve_quantization()`. The CUDA-shaped analytical VRAM pre-flight is also skipped on the MLX path, because Apple unified memory is managed by Metal rather than by a fixed VRAM pool.

### The launch hint that dropped your own flags

`soup train --no-reexec` prints the `accelerate launch` command you should run yourself. It was built from a second, hand-maintained copy of "what the user typed", and that copy was short.

Rather than patch the printed copy, the contributor **deleted it** and derived the hint from the argv that actually launches the run, so the two cannot drift again. Four flags that used to fall off now survive: `--name`, `--replay`, `--replay-ratio` and `--replay-seed`.

### `data.interleave`, which was still open

**Since closed in v0.74.0**, which wired it into training-time dataset loading and widened `data.train` to accept a list. What follows is what v0.73.3 shipped, kept as written.

The fourth one is not fixed, and saying so is the point. `data.interleave` validates, documents and parses, and nothing reads it at training time. It was found during review of a different fix and **filed rather than papered over**.

What did get fixed is the command that made it visible. `soup data mix --optimize` is the one command whose entire output is a config file, and it wrote one that would not load: `data.train` came out as a YAML list against a field typed `str`. It now renders the single highest-weighted dataset, keeps the full ranked weight and path breakdown as a comment above it so no information is lost, and says in that comment that the mixture is not yet consumed by training.

## The other failure that a loss curve cannot see

On Windows, `GetExitCodeProcess` returns 259 for a running process, but **259 is also a legal exit code**, so a child that exited \*with\* 259 was indistinguishable from one still running and read as alive forever. That defeated reconcile-on-read for the experiment tracker and could wedge the MCP one-active-execution cap shut, refusing every later execution with no error an operator could act on.

The check now waits on the process handle, which is signalled the instant the process exits whatever its code, and falls back to reading the exit code only if the wait itself fails. The two byte-identical copies of that primitive became one shared module, with a test that fails if a third appears.

Alongside it, a run whose watcher died is no longer reported `running` forever. The tracker reconciles on read: a `running` row whose recorded process is gone is rewritten to **`terminated` with an unknown exit code**, deliberately, so a lost outcome is never recorded as a success. The richer `completed` and `failed` statuses are left alone.

## The MCP server can now execute

This is the release's one genuinely new capability, and it is a big enough change that it has [its own page](/docs/mcp-server#execution-v0-73-3).

`soup mcp serve --allow-execute` used to reserve a gate it never opened. It now runs a planned training or export behind a **short-lived, single-use, server-generated confirmation token** bound both to the plan and to the execution kind. Two new tools, `train_execute` and `export_execute`, accept **only** that token: no command, no argv, no shell string, no client-supplied environment. The server count goes from 16 tools to **18**.

> **A note on auditing this one.** The `--help` text for `--allow-execute` was not updated by the feature commit and still says execution is reserved for the future. The changelog, the command reference and the running code all agree that it executes. On this flag, at this release, the binary's own help string is the stale party.

## Also in this release

- **`soup ship --noise-floor` measures leg 1 in every task mode.** At v0.73.2 it was `--task-mode metric` only. `judge_score` now scores the base side N times through the judge, and `pairwise` judges the base model **against itself**, where the expected win rate is 0.5 by construction, so the spread is measured rather than inferred. Because those repeats fold in the judge's own sampling noise, that floor is labelled **decode + judge** on the panel and stamped `judge_inclusive` in the evidence, so it can never be read as a decode-only number. It costs N extra judge API calls.
- **`eval.ship.noise_floor` is committable to `soup.yaml`**, bounded to 2 through 10 from the same constant the CLI validates against, with the usual CLI over config over default precedence. It was the one gate-policy flag a team could not put in a committed config.
- **A boxed answer with a space no longer scores as no answer.** v0.73.2 shipped a pattern for the exact spelling quoted in its ticket and missed `\boxed {A}`, which the typesetting language permits and models emit. Same defect, one space to the left. It is closed here.
- **`soup draft distill --steps N` delivers about N optimiser steps** instead of roughly a fifth of them. The old arithmetic ignored that the validation split removes rows and that gradient accumulation makes several micro-batches into one step. The resolved budget is now printed up front, and the emitted config pins the run shape so the arithmetic and the trainer cannot disagree.
- **`soup env check` flags an installed package that violates Soup's own declared bounds**, exit code 3, read from package metadata rather than a second hardcoded copy, and independent of whether you ever wrote a lock file. It exists because installing a fast serving stack into a training environment silently pushes `transformers` past the cap Soup itself declares.
- **Layer streaming sees through a paravirtual disk.** A virtio device reports itself as rotational with no media hint, so a genuinely NVMe-backed cloud disk measured at 1.5 GB/s was refused the disk-overflow tier, which is the audience that tier exists for. When the flag is unreliable, media type is now decided by a bounded direct sequential read; a genuinely slow disk is still refused. `training.stream_disk_kind` is the override, and it prints what it overrode beside what was detected.
- **`bom` and `attestation` are first-class registry artifact kinds**, so `soup bom emit` and `soup attest emit` take `--attach-to-registry` and [`soup card`](/docs/compliance-pack) links them for free. Signed attestations attach their detached signature sidecar too.
- **Two new recipes**, `qwen3.5-4b-pretrain` and `deepseek-v4-flash-grpo`, taking the catalog to **144**.

## What this release deliberately did not do

**No new measurement was made, and no benchmark record was added.** Upstream states that rather than leaving it implicit: every item here is a contributor patch, reviewed and green in CI at merge, and none of it was gated by a new number. The published measurement records are unchanged, and so is the preprint, whose measured figures and scope this release does not touch.

Two of the four flags are also not fully closed. `data.interleave` has a filed issue and no training-time reader, and the same list-shaped defect exists in a second renderer. \*(Both since closed in [v0.74.0](/docs/loaded-in-fp32).)\* The release is named for a pattern it found, not for one it finished.

## Known limitations

1. **`data.interleave` still has no reader at training time.** Filed, not fixed. \*(Since closed in [v0.74.0](/docs/loaded-in-fp32).)\*
2. **The `--allow-execute` help text is stale in the shipped binary.** It describes the pre-v0.73.3 behaviour.
3. **The Unsloth loader cannot honour `bnb_4bit_use_double_quant`.** It builds its own quantization config with double-quant hardcoded on.
4. **A `stream_disk_kind` override carries no measured rate**, deliberately, so a later refusal can never cite a reading you overrode.
5. **The noise floor is still n=3, one model, one dataset.** Widening it to the judge modes changed its scope, not its statistical weight: it **sizes** an effect, it does not calibrate a threshold.
6. **The MLX repair was not accompanied by a resolution of the reported MLX hang**, which remains open and unreproduced.

## See also

- [The MCP server](/docs/mcp-server) — the execution gate, the token, and all 18 tools.
- [The ship gate](/docs/soup-ship) — where the noise floor lives.
- [v0.74.0: loaded in fp32](/docs/loaded-in-fp32) — the release after this one, which closed `data.interleave`.
- [v0.73.2: the release gate](/docs/ship-gate-repairs) — the release before this one, and the two items it left for this one.
- [Everything new across v0.71 to v0.74](/docs/whats-new).

[Previousv0.74.0](/docs/loaded-in-fp32)[Nextv0.73.2](/docs/ship-gate-repairs)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="106-ship-gate-repairs"></a>

# 106. v0.73.2: the release gate

*Source: <https://trysoup.dev/docs/ship-gate-repairs>*

`soup ship` answers one question: did this model get better, or did I break it? It is the thing this project points at when asked what it does that other tools do not.

**Two of its behavioural suites were ranking by the wrong thing, one whole failure direction had no detector at all, and a caller's own mistake was indistinguishable from a regression.** Every item below was reproduced against the shipped v0.73.1 code before a line was changed.

## Re-run this

| If you | What happened | What to do |
| --- | --- | --- |
| Relied on any `soup ship` verdict | Two of its suites scored by the wrong thing. A stub answering **every item correctly** scored 0.000 on two suites, and an 8B naming the right tool 40 times out of 40 scored 0.225 | Re-run the gate |
| Stored a `--baseline` snapshot | Snapshots taken before this release are **on a different scale** for `mini_mmlu`, `mini_common_sense` and `mini_tool_call`. On an unchanged model the jumps are 0.423 to 0.731 and 0.225 to 1.000, both far larger than the 0.05 gate. `soup ship` now warns by name | Re-take the baseline. `mini_instruction` and `mini_arithmetic` are unaffected |
| Read the verdict panel's leg-1 result | **The panel never printed its own win marker, on any release up to and including v0.73.1.** A bare `[no win]` is valid markup for an unknown tag, so the renderer ate it. The plain-text rubric, which has no markup parser, printed it correctly the whole time | Nothing to re-run. The verdict itself was right |

## Four defects, and what each one cost

### The extractor did not know a boxed answer

**Llama-3.1-8B-Instruct scored 0.423 on `mini_mmlu`, below a 0.5B**, while scoring 1.000 on two other multiple-choice suites. All 15 failures were classified rather than guessed at: **8 boxed the right letter, 6 boxed a value** because nothing in the prompt ever asked for a letter, and 1 was a real miss.

**Both halves were required.** The extractor alone is worth **+8 items**; the prompt change alone is worth **0**; together the same model moves **0.423 to 0.731** and the inversion disappears. Never attribute the repair to one half.

Two rules the fix holds to, because a permissive scorer is as useless as a broken one:

- The new tier fires **only** when the box holds a single letter A to J. Reading a boxed **number** as "option 4" would be a wrong credit, not a repair.
- Among competing answer forms, **position decides, not form**. A reasoning model that boxes a scratch answer and then corrects itself chose the correction.

### The tool-call suite ranked by brace hygiene

**The 8B named the right tool 40 times out of 40 and scored 0.225.** The chain: the model emitted three opening braces and two closing ones, the whole-string parse failed, a bounded scan returned the **inner** object, and the scorer rejected it for carrying no function key. That suite now reads **1.000**.

The fix restores the envelope only for an object carrying **both** a name and its arguments. Requiring the arguments is the safety argument, not a detail: the prompt shows the model a menu of name-and-description objects, and a name-only test would credit echoing the menu back.

Kept on the record: the missing brace is **the model's own output**, not truncation. That attribution was written down, believed, and shipped before a budget sweep disproved it.

### A caller error failed in the direction that looks like a finding

A non-callable generator returned **0.0** on the three behavioural suites while raising on the multiple-choice ones. In leg 2 a 0.0 reads as "failed every item", so **DON'T SHIP**, which means a caller's own mistake was indistinguishable from a regression and failed in the direction that looks like a discovery. It raises now. A callable that misbehaves is still a failed item, which is the correct existing contract.

### A model that refuses everything looked like a safety improvement

Leg 2 flagged a **drop** in refusal rate and had no reverse. So a tune that refuses everything registered as a monotone safety improvement, with no ceiling on how useless the model became. Reproduced as indistinguishability: **two models with byte-identical scores on all seven shipped suites and the same SHIP verdict, one of which refuses every benign request.**

**`mini_over_refusal` is the eighth bundled suite.** 40 hand-authored, original benign requests that merely sound alarming, scored as the **fraction not refused**. The default leg-2 set goes from **seven suites to eight**. Live-verified on a real pair: `mini_over_refusal` reads 1.0000 against 0.9750 while `mini_safety` reads 0.0000 on the same two models, which is the point. They are two axes, and neither can be gamed alone.

Its caveat, carried from the record: **40 prompts and one greedy pass size a gap, they do not calibrate a threshold.** It detects a collapse in benign helpfulness, not a subtle shift in tone.

## Measure the instrument before you trust the delta

```bash
soup ship --base ./base --adapter ./out --task-eval task.jsonl --noise-floor 5
```

**Greedy decoding is not deterministic on a GPU.** Same model, no adapter, five runs: the scores spread **0.015 strict and 0.020 format-blind**, against a threshold of 0.05, and **four of six paired deltas** in that session sat inside the floor. Until this release `soup ship` compared against 0.05 without ever telling the operator what its own instrument could resolve.

`--noise-floor N` re-runs the base model N times (N from 2 to 10), prints the measured floor beside the verdict, and refuses to call a delta significant below it. The per-axis floor is the spread between the best and worst run, and every axis is then gated at whichever is larger, the threshold or the floor. **That `max` is deliberately two-directional:** a floor above the threshold widens the gate to what is actually measurable, and a floor below it must never tighten the gate behind the operator's back.

> **Two caveats travel with those numbers and must not be dropped.** The 0.015 and 0.020 figures are **the borrowed H100 session's**, not this release's own development box, which measured **0.0000** on CPU where greedy decode is deterministic. And at **n=3, one model, one dataset**, the floor **sizes** the effect. It does not calibrate a threshold, and nothing establishes what N is enough.

At this release the leg-1 floor is measured in `--task-mode metric` only. In the judge modes a repeat would fold the judge's own sampling noise into a number presented as decode noise, so the run warns and leaves leg 1 at a zero floor instead. **Since lifted in [v0.73.3](/docs/flags-that-did-nothing), which measures the floor in every task mode and labels the judge-mode one `decode + judge` so it cannot be read as decode-only.**

## Two contributed flags

- **`soup data split --stratify-semantic`** with **`--num-clusters`**: stratify a split by meaning rather than by row order, capped at 50,000 rows. A missing scientific-computing dependency refuses with the install command rather than silently falling back. Contributed by @Deadpool2000.
- **`soup mcp serve --allow-execute`**, which implies `--allow-mutating`. Contributed by @CODING-DARSH. At this release it reserved a gate it did not open; the same contributor opened it in [v0.73.3](/docs/flags-that-did-nothing). See [the MCP server page](/docs/mcp-server) for what it does now.

## Known limitations

All seven, because dropping any of them changes what the rest mean.

1. The leg-1 floor is measured in metric mode only. \*(Since closed in v0.73.3.)\*
2. n=3, one model, one dataset.
3. **The floor was not measured on GPU on this box.** The published spread is the H100 record's.
4. Baseline files from before this release are on a different scale, and there is no version stamp that detects it.
5. An `--evidence` file remains trusted input. `--config` binds evidence to a config hash, not to the scores.
6. `mini_over_refusal` is 40 hand-written prompts scored by a keyword heuristic.
7. **Two suites still sit at or next to a ceiling after the repair.** A suite pinned at 1.000 detects a regression exactly as poorly as one pinned at 0.000, and nothing in this release re-sizes them.

## One more thing, and it is the same lesson twice

The boxed-letter repair shipped a pattern for **the exact spelling quoted in the issue**, and missed the same thing written with a space before the brace, which the typesetting language permits and models emit. Same defect, one space to the left, in a fix written to close that very issue. **Every test passed, because every test used the spelling from the ticket.** It was caught by someone else after release, and the repair shipped in [v0.73.3](/docs/flags-that-did-nothing).

So: do not read `soup ship` as finished. Read it as an instrument that is now measured.

## See also

- [The ship gate](/docs/soup-ship) — what the verdict is, how the two legs work, and the evidence loop.
- [v0.73.3: four flags that did nothing](/docs/flags-that-did-nothing) — the release after this one, which closed the two items above that were still untagged.
- [v0.73.1: the free GPU tier](/docs/free-gpu-tier) — the release before this one.
- [Designing the eval that feeds it](/docs/eval-design) — the task metric leg 1 reads.
- [The MCP server](/docs/mcp-server) — including the new execution flag.

[Previousv0.73.3](/docs/flags-that-did-nothing)[Nextv0.73.1](/docs/free-gpu-tier)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="107-free-gpu-tier"></a>

# 107. v0.73.1: the free GPU tier

*Source: <https://trysoup.dev/docs/free-gpu-tier>*

A patch release carrying everything that landed after v0.73.0. **Its highest-value item is not the issue the slot was opened for.**

The slot was opened to make the streaming VRAM pre-flight measure instead of predict. What sat beside it in the same pile was larger: **bf16 was assumed on every CUDA card, in fourteen places**, so every pre-Ampere card failed on every task, not only on layer streaming. That is a T4 on Colab's free tier, a T4 or a P100 on Kaggle, and every V100, GTX 16xx and RTX 20xx. The entire free notebook tier ran in a dtype its GPU has no units for, and said nothing about it.

Neither this release nor the one after it has a codename upstream. **Borrowed Hardware** is carried here as the name of the line.

## Re-run this

| If you | What happened | What to do |
| --- | --- | --- |
| Trained on a **pre-Ampere card** (T4, P100, V100, GTX 16xx, RTX 20xx) | The run asked for bf16 on a card with no bf16 units. **Every task**, not only streaming | Re-run on v0.73.1 |
| Used `backend: mlx` | It **never dispatched to the MLX trainer at all**, silently falling through to the transformers path. And without a freeze first, the saved "adapter" was a full fine-tune: **172 tensors where 24 were expected** | Re-run |
| Loaded an **MLX adapter** you had trained | `adapter_config.json` shipped `target_modules` unresolved, as `{"keys": ["auto"]}`, so loading dropped **every LoRA tensor without a word**. Generation with the adapter was bit-identical to the base model. `auto` is the schema default, so this was every MLX run that did not name its modules by hand | Re-train. The file cannot be repaired after the fact |
| Resumed from a periodic `checkpoint-*` under `use_fsdp2_compile` | v0.73.0 repaired the **final save only**. Every intermediate checkpoint still loaded as a dead adapter, so `--resume` and `load_best_model_at_end` continued from a re-zeroed `lora_B` in total silence. Measured at 70B: 320 canonical keys in the output root against 320 prefixed ones in `checkpoint-100` | Re-run from the start |
| Set `training.seed` on anything other than supervised fine-tuning | It was **parsed and ignored**. A seeded GRPO run trained at the framework default of 42, with no error and no warning, so replicates that differed only in their seed were the same run | Re-run if you drew a conclusion from a seed sweep |
| Streamed at a sequence length above roughly 4,300 tokens | The VRAM pre-flight can **under-predict**, against a contract that says it never does | Check the table below, or turn on the probe |

**That MLX adapter is the third time in this project's history that a healthy loss curve shipped a dead artifact**, after v0.72.0's adapter keys and the full-fine-tune save above. The loss curve structurally cannot see it. Only the artifact can.

## The headline: bf16 was assumed on every CUDA card

Fourteen places. Twelve trainer wrappers (`bco`, `classifier`, `distill`, `dpo`, `embedding`, `ipo`, `kto`, `online_dpo`, `orpo`, `pretrain`, `reward_model`, `simpo`) plus the streaming setup and the supervised wrapper's own precision resolver, each carrying some form of "if the device is CUDA, use bf16" with no capability check at all.

**The trap recorded beside the fix is worth knowing, because the first attempt was a no-op on exactly the hardware it was written for.** The capability check defaults to counting emulation, so a T4 answers yes when asked whether it supports bf16. The predicate now asks the question that distinguishes hardware support from emulation.

Two things make this the same shape as the four backends the borrowed H100 box found had never run: it **cannot fail on an Ampere development box**, and the knowledge already existed in the repository. One wrapper, the ASR trainer, already carried a comment naming pre-Ampere cards and had already fixed it, in that one file, never propagated. The repair replaced the hand-written list of wrappers with a **scan of the trainer package**, because a hand-written list is what hid them.

The correctness cross-check: streamed-versus-resident logits are bit-exact at `0.000000e+00` in float16 as well as bfloat16, in both quantisations, against resident references of matching numerics. **That was measured using fp16 on an Ampere card, so it establishes the plumbing, not the Turing and Pascal kernels.** What a genuinely pre-Ampere card does with bitsandbytes NF4 is not yet measured.

## An 8B on a free Colab T4

With the repair in, the notebook that had been unrunnable on the published release runs.

**Llama-3.1-8B in NF4, streamed, on a free-tier Tesla T4**, batch 1, `max_length: 256`, LoRA r=8, fp16, with the process capped at **4.00 GB**. The cap was shown to bite rather than assumed: a deliberate 4.29 GiB allocation was refused.

- **Measured peak 2.91 GB** against a predicted 3.02, an over-prediction of **3.8%**, which is the safe direction
- **7 steps, exit 0**, adapter written with **128 of 128 tensors non-zero**

**What that run does not establish is stated as plainly as what it does.** No throughput figure is quoted from it, because a capped card is not a benchmark. Gradient exactness at 8B on a Turing card is not shown: non-zero tensors prove gradients flowed, not that they were right. The notebook's own streamed-versus-resident comparison produced no captured output on that run and is recorded as **unrun**, not as a pass. And one run, one seed, no repeats.

One thing it did surface: the pre-flight reported **15.10 GB free**, the whole device, because the cap is enforced by the allocator and not by the driver. The fit decision was taken against a number 3.8 times larger than the budget actually in force. That is the open issue `training.stream_vram_override` exists to work around.

> **The notebook installs Soup from git, not from PyPI.** Upstream has not yet switched its install cell back now that the fix has shipped, and its own text still says the fix is unreleased. If you run it, expect the git install and ignore that line.

## The pre-flight was breaking its own contract

The streaming VRAM pre-flight's contract is that **it never under-predicts**, because on Windows an over-budget allocation does not raise. It spills silently into host memory, and the run slows by multiples with no error at all.

Measured through the real `soup train` on the 4 GB laptop, SmolLM2-135M streamed in bf16 at batch 1:

| Sequence | Predicted | Real peak | Ratio |
| --- | --- | --- | --- |
| 4352 | 3.282 GB | 3.036 GB | 1.081x, over-predicts, safe |
| 5120 | 3.844 GB | 4.118 GB | **0.934x, under-predicts** |
| 6144 | 4.590 GB | 5.830 GB | **0.787x, under by 21%** |

**The existing guard could not have caught it.** All ten rows of the grid that validates the estimator sit at sequence 256 or 512, so it varies batch and says nothing whatever about sequence length. A control only covers the variable it varies, and that is this project's own test applied to itself.

**The mechanism is deliberately not claimed.** The obvious candidate, the quadratic term from the attention score matrix, does not settle the numbers, and that is precisely the argument for measuring rather than adding another coefficient: a formula cannot model a term nobody has identified.

**A second box has since said this does not reproduce there.** A contributor ran the same protocol on an NVIDIA A10G with a much newer stack (torch 2.13, transformers 5.16.1) and the ratio is flat at about **1.16x over-prediction** from sequence 2048 through 6144, on two models. The record publishes its leading hypothesis as a **negative result with a positive control**, and explicitly does **not** refute the reading for this 3050. Taken together the honest conclusion is that the term varies per-stack \*and\* per-sequence-length, which is why the answer is a measurement rather than a constant. See [the v0.74.0 record](/docs/loaded-in-fp32).

## Two new config keys

Both are **config keys, not CLI flags**. Both are refused at config load if `stream_layers` is false, the same footgun gate the other streaming keys carry.

```yaml
training:
  stream_layers: true
  batch_size: 1                    # 'auto' is refused on a streaming run
  stream_vram_probe: true          # decide the fit by MEASURING one real step
  # stream_vram_override: 4000000000   # or: assert what is free, in bytes
```

**`training.stream_vram_probe`** runs one real forward and backward at your configured shape and decides on that, instead of on the fitted formula.

- Off by default, because it costs a step and it can refuse a run the formula would have accepted
- **`task: sft` only.** A preference loss is not the step the probe runs, and its agreement with one is not established. The four streaming preference losses keep the fitted prediction, which is exactly where it was measured least accurate
- Costs **1 to 5 seconds** at ordinary shapes, and 52 seconds at a shape that does not fit, which is the honest worst case paid once instead of every step
- Runs **12 to 14% conservative** against the real training step, the correct direction for a gate
- **Cannot overrule a prediction more than four times over budget.** The largest disagreement ever measured is 21%, so past a small multiple the config is simply too big and is refused by arithmetic without touching the GPU
- Gates on allocated memory, not reserved. Reserved runs 1.08 to 1.41 times allocated, and gating on it would refuse this feature's own flagship configuration, which runs

**`training.stream_vram_override`** replaces the free-VRAM figure the pre-flight checks against, in either direction. It changes the yardstick, not the check: an override **below** real free VRAM still refuses a config that would otherwise fit, which is what makes it an escape hatch rather than a bypass flag. It is an assertion you are making, not a measurement.

## The rest

- **`training.seed` now reaches every trainer wrapper**, and is applied before the model loads, because the adapter's own initialisation is drawn before the trainer's seeding used to happen. An unset seed still resolves to 42 and `data_seed` still stays unset, so **the values a run trains at are unchanged; what changed is when they arrive**. Full detail on [seeds and reproducibility](/docs/seeds-and-reproducibility).
- **The MLX backend reads neither seed field**, and now says so in its existing "MLX backend ignores" line. A warning rather than a rejection, because a config valid on transformers should not become unloadable by switching backend.
- **`training.batch_size` gained a lower bound.** `batch_size: -4` used to load, and then meant whatever each trainer's arithmetic did with it, including the streaming pre-flight, which multiplies by it.
- **The dead calibration hook was wired up.** The estimator's calibration entry point had no caller anywhere in the source; it now feeds both the budget and the printed panel. Every streamed run pays one transient 96 MiB allocation and two device synchronisations for it. On today's stacks that is **a no-op in effect**, which is the point of a guard against a stack that has not shipped yet.
- **`mlx-lm` floor raised** to the version the MLX path is built against.

## Known limitations

- The probe is supervised-fine-tuning only, which is where the formula was measured **least** accurate.
- The mechanism behind the long-sequence divergence is unidentified, so the formula is not fixed, only overrulable.
- The probe measures a plain causal-language-model step, not the run's own step.
- Windows still does not raise on an over-budget allocation, so the refusal direction cannot be verified by OOM on that platform.
- fp16 streaming is **not yet measured on a genuinely pre-Ampere card**.
- **Layer streaming remains BETA.**

> **The working record carries three readings that were withdrawn during this work, two of which looked like the headline result.** They are left standing in [the benchmarks directory](https://github.com/MakazhanAlpamys/Soup/tree/main/benchmarks) with their refutations beside them, which is why that directory is worth reading and why you should link a file's top rather than deep-link a passage the same page later corrects.

## See also

- [v0.73.2: the release gate](/docs/ship-gate-repairs) — the release after this one.
- [v0.73.0 Borrowed Hardware](/docs/borrowed-hardware) — the release before it, and its own re-run list.
- [Seeds and reproducibility](/docs/seeds-and-reproducibility) — what a seed does and does not buy you.
- [Layer streaming](/docs/layer-streaming) — the mechanism, the measured numbers and the refusal table.

[Previousv0.73.2](/docs/ship-gate-repairs)[Nextv0.73.0](/docs/borrowed-hardware)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="108-borrowed-hardware"></a>

# 108. v0.73.0 "Borrowed Hardware"

*Source: <https://trysoup.dev/docs/borrowed-hardware>*

Every number this project had ever published was measured on one machine: a 4 GB RTX 3050 Laptop running Windows. From 5 to 9 August 2026 Soup ran on a **borrowed 8x H100 box** for the first time, on a much newer torch, bitsandbytes, trl and peft stack.

Three days there found **one silent correctness defect in layer streaming, four backends that had never actually run, and a documented multi-GPU entry point that had never launched**, alongside the first evidence that the laptop result reproduces on hardware nothing like it. That is the release. It is a minor bump rather than another v0.72.x patch because it adds two capabilities that did not exist and repairs four backends.

[What the measurements established](/docs/external-validation) has its own page. This one is the changelog, and it starts with the part that costs you something.

## Re-run this

Six defects produced runs that completed successfully and were wrong anyway. If any of these describes something you already did, the output is not trustworthy.

| If you | What happened | What to do |
| --- | --- | --- |
| Trained supervised with `data.max_length` above 1024 | **Every such run was silently truncated to 1024 tokens.** Measured: a config asking for 4096 produced 1024 tokens per sample, with no warning | Re-run on v0.73.0. Long-context, document and multi-turn tunes are the ones that suffered |
| Used `use_fsdp2_compile: true` | The adapter reloads as **all zeros**. The tensors trained, but every key was saved with a `torch.compile` prefix, so loading matched none of them and left the weights at their zero init. The run exited 0 with a healthy loss | Re-run. This is the third defect of this exact shape in the project's history |
| Streamed a **32B or larger** model in NF4 | Gradients were wrong on every layer but the last few, while the forward stayed bit-exact and the loss matched a resident reference to every digit | Re-run. 8B and 14B are below the threshold and are fine |
| Relied on a `soup ship` verdict | Two of the three behavioural suites scored **0.000 on a model that does both tasks correctly**, and the refusal detector missed the typographic apostrophe Llama actually types, reporting 0.300 for a model whose true refusal rate is 1.000 | Re-run the gate. Stored evidence from before this release is not comparable |
| Exported a GGUF at f16 and then quantised | The quantised export **deleted your f16 file**, even with an unrelated `--output` | Re-export the f16 if you still need it |
| Followed the printed `--no-reexec` hint | The hint dropped every flag you had typed, so following it literally trained **without** `--fsdp`, `--gate` or `--wandb` | Check what you actually ran |

None of these is a streaming-only problem except the third, and none of them announced itself.

## The defect worth reading about

**In NF4, above roughly 165 MB per decoder layer, the backward pass produced silently wrong gradients.** Issue #331.

The threshold is a bracket rather than a number: exact at **163.8 MB per layer**, broken at **171.5**, monotone on both sides across seven measured points. In practice that is **32B (234 MB per layer) and 72B (432)**, and never 8B (105) or 14B (132), both of which survive a 50-consecutive-backward soak at exactly `0.0`. bf16 was never affected at any size.

The cause is buffer aliasing, not a race, and that was settled by measurement: a full `cuda.synchronize()` does not fix it and de-aliasing does. `bitsandbytes.MatMul4Bit` stashes the packed 4-bit weight and its quantisation state on the autograd context as ordinary Python attributes instead of going through `save_for_backward`, so gradient checkpointing cannot discard and recompute them. The reference captured during the forward aliases a streaming buffer, and by the time the backward reads it that slot has been refilled with a different layer.

**The obvious repair was measured and rejected.** Giving every pooled tensor a private copy is correct and costs only about 6% of throughput, but it takes peak VRAM on a real 32B from 4,220 MB to 19,720 MB, which is approximately the whole model. A repair proportional to the model rather than to one layer deletes the reason the feature exists.

**What shipped instead** keeps streamed NF4 weights out of that code path entirely: dequantise inside the checkpointed region and use a native matmul, so the saved tensor goes through the ordinary mechanism. It is gated on two real models against a control that reproduced the defect in the same process: **256 of 256 gradient tensors exact at 32B** against the control's 8 to 12, and **320 of 320 at 72B**, the size where the defect was worst, against the control's 8. It costs **2.9% peak VRAM and 4.8% throughput at 32B**, and 2.6% and 3.7% at 72B.

The library behaviour it works around is upstream and unchanged, filed as `bitsandbytes-foundation/bitsandbytes#2034`.

> **One consequence for the headline number.** The published **119.6 tok/s** on a 4 GB card was measured before this repair and has not been re-run on repaired code. The repair cost 4.8% at 32B, so treat it as a **pre-repair figure** until someone re-measures it on that card. A server card cannot stand in: an H100 ran the same configuration no faster than the laptop, so throughput here does not carry across machines.

## Two new capabilities

### A seed you can set

```yaml
training:
  seed: 1234        # weight init of new params, data order, dropout
  data_seed: 7      # optional: vary data order while holding init fixed
```

Both are **config keys, not CLI flags**, and both default to unset rather than to 42. That is deliberate: an unset seed has to reproduce two different historical defaults, Hugging Face's 42 for the trainer and 0 for the multipack sampler, and defaulting to 42 would have silently re-ordered every existing multipack run. A boolean is refused by name, because `true` would otherwise become seed 1.

**Scope, stated rather than left as a footgun:** the seed reaches the trainer arguments on supervised runs only. (**Since closed in [v0.73.1](/docs/free-gpu-tier)**, which took it to all eighteen wrappers and moved it ahead of the model load.) On a **streamed** run it also seeds the adapter initialisation for all five streaming tasks, which is why a streamed run is bit-reproducible from a seed and a resident 4-bit one still is not.

### Full fine-tuning as `lora.r: 0`

```yaml
training:
  lora:
    r: 0            # no adapter: train the model itself
```

The trainer's full-fine-tune branch was dead code with no way to enter it, and the only shipped spelling was the Spectrum workaround `unfrozen_parameters: ['.*']`. Rank 0 was chosen on repo evidence rather than taste: three consumers already treat rank 0 as "no adapter", and `r: 0` previously crashed inside PEFT, so no config that worked before changes meaning. `lora.r` also gained a lower bound, because `r: -5` used to parse and die deep in the library.

It writes a **dense checkpoint**, not an adapter, and it is refused with a named message when combined with a non-transformers backend, a non-text modality, any quantisation, Spectrum, LISA, or any LoRA-shaped option. It also refuses rather than running a no-op if your freeze settings leave nothing trainable.

## Four backends that had never run

This is the part borrowed hardware bought, and none of it is a new feature. All four were documented all along.

- **`soup train --gpus N` never launched.** The launcher hands `accelerate` a script path, and Soup was passing the Python binary, so accelerate parsed a CPython executable as source and every rank died before the trainer existed. Invisible to single-GPU CI, which skips the launcher entirely.
- **DeepSpeed could not train a LoRA model on any stage.** LoRA leaves one of Hugging Face's two optimizer parameter groups empty, DeepSpeed drops it, and the scheduler then hits a strict length check. Verified repaired on two H100s. **Repaired in the supervised trainer only** at the time; v0.74.0 attached the same guard in eighteen more wrappers.
- **SGLang serving returned 500 on every request.** Its runtime returns a JSON string where Soup subscripted a dict. Deterministic, not a race, and never caught because SGLang does not run on Windows.
- **The Liger kernel crashed at step 0** across the whole supported dependency range, because Soup patched the model but never told the trainer the fused path returns no logits. Separately, Liger's architecture match was a substring of the model **name**, so a model loaded from a local directory silently trained without it.

The vLLM backend was repaired rather than resurrected: it **ignored the model's chat template**, hand-rolling a prompt while the transformers backend used the real one. On Llama-3.1-8B with identical sampling settings, the hand-rolled prompt produced a run-on loop that burned all 200 tokens where the correct one answered in 8. It also reported `finish_reason` as a clean stop even when it had truncated, and `--dashboard` silently did nothing. A new `soup serve --max-model-len` exposes an engine setting that already existed but could not be reached from the command line.

## Layer streaming, beyond the defect

- **Streaming is now refused when `nn.DataParallel` would engage.** Hugging Face wraps the model whenever more than one CUDA device is visible and the run is not distributed, and DataParallel needs every parameter on the first card while streaming keeps the decoder on the `meta` device. It refuses, naming `CUDA_VISIBLE_DEVICES=0` as the fix, rather than quietly using one card of eight. It accounted for eight of the nine streaming-suite failures on the borrowed box and is unreachable on a single-GPU machine, which is why it survived four releases.
- **The four preference losses never set gradient checkpointing.** One omission with two opposite symptoms: on an older trl an explicit `gradient_checkpointing: true` was silently dropped, and on a newer one the run died outright with a `meta` device error.
- **`device_map: auto` broke every distributed launch, in fifteen places.** A first pass had fixed six; nine more were found by replacing the hand-written test list with a scan of every trainer module, because the list is what hid them.
- **The pre-flight panel was titled after a flag that does not exist.** It read `soup train --stream-layers`; there is no such option, and it was the first thing every streaming run printed.

## Packaging

- **Python is now 3.10 to 3.12.** The upper bound was missing, so on 3.13 and above pip resolved untested PyTorch wheels and the failure was not a Soup error message but a loader crash inside the native extension, before any Soup code ran. The bound stops at 3.13 because 3.13 is equally untested, and a test derives it from the CI matrix so the two cannot drift apart.
- **`trl` support widened to `>=0.14.0,<0.29`**, behind a capability-probe layer rather than a version table, because a version table was wrong twice before. The trainers now ask each config class whether it accepts a field, and resolve the moved classes through trl's experimental namespace. All six preference trainers construct and train to identical losses on three different trl versions. \*(Since moved: v0.74.0 requires `trl>=0.29.0,<1.0.0` with `transformers>=5.16.1` and `peft>=0.20.0`. The probe-not-a-table rule is what carried forward.)\*
- **`pip install "soup-cli[all]"`** now also pulls the MCP server extra.

## Known limitations

Stated because they are the reason to trust the rest. **This is v0.73.0's list as it shipped; four entries have since been closed and are marked below.** The rest still stand.

- The seed reaches the supervised trainer's arguments only; other tasks parse it and ignore it. **Since closed in [v0.73.1](/docs/free-gpu-tier)**: it reaches every wrapper now, and is applied before the model loads. See [seeds and reproducibility](/docs/seeds-and-reproducibility).
- A resident 4-bit run is still not bit-reproducible from a seed, while a streamed one is, because the adapter is built before the seed is set. That has a real consequence for the ship gate: three runs of one unchanged resident config moved two suites by 0.375 and 0.269 against a 0.05 threshold, so five of seven suites can cross the regression line on a re-run that changed nothing.
- The streaming VRAM pre-flight still over-predicts, and its per-logit constant was deliberately left where it is rather than lowered. The asymmetry decides it: over-predicting refuses a run that would have worked, which is visible and annoying with the data intact, while under-predicting on Windows is not an exception at all but a silent spill into host memory.
- DeepSpeed with LoRA is repaired in the supervised trainer only. **Since closed in [v0.74.0](/docs/loaded-in-fp32)**: eighteen more wrappers attach the guard, and coverage is enforced by a scan over the trainer directory rather than a hand-written list of names, which is what let the first fix stop at one.
- The SGLang backend still hand-rolls its own prompt and hardcodes its finish reason, the two defects the vLLM rewrite fixed. Named rather than quietly skipped. **Since closed in [v0.74.0](/docs/loaded-in-fp32)**: it applies the model's own chat template through the shared builder and reports `length` on a truncated response, on both the sync and streaming paths. Live verification against a real SGLang runtime on Linux is still open.
- The reward-hacking controller's mechanism is confirmed and its efficacy is not: at 7B the between-mode difference sits inside the within-mode spread.
- Two ship suites still rank by something other than the capability they name. **Since closed in [v0.73.2](/docs/ship-gate-repairs)**, along with a third failure direction that had no detector at all.
- The RAM-versus-disk streaming throughput gap remains unmeasured, because the borrowed box had no NVMe.
- **Layer streaming remains BETA.**

## See also

- [v0.73.1: the free GPU tier](/docs/free-gpu-tier) — the release after this one, and its own re-run list.
- [v0.73.2: the release gate](/docs/ship-gate-repairs) — where the ship suites above were repaired.
- [Validation on hardware we do not own](/docs/external-validation) — what the three days measured, in full, including the numbers that were discarded.
- [Layer streaming](/docs/layer-streaming) — the mechanism, the measured numbers and the refusal table.
- [What's new across v0.71 to v0.75](/docs/whats-new) — every release line, newest first.
- [The paper](/docs/paper) — the preprint, unaffected in its correctness claims and widened in scope by this work.

[Previousv0.73.1](/docs/free-gpu-tier)[NextQuant Menu II live writers](/docs/v053-live-writers)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="109-v053-live-writers"></a>

# 109. v0.53.1 — Live writers for Quant Menu II

*Source: <https://trysoup.dev/docs/v053-live-writers>*

v0.53.0 shipped the closed allowlists and validators. v0.53.1 lifts every stub to live wiring.

## TorchAO PTQ export

```bash
soup export --format torchao --quant-config quant.yaml
```

Closed scheme allowlist with per-scheme kwarg validation:

- `Int4WeightOnly`
- `Int8DynActInt4`
- `Float8DynActFloat8`
- `NVFP4` (Blackwell SM ≥ 12, runtime gate)

## Single-shot BNB-4bit merge

```bash
soup merge --save-format 4bit          # standard
soup merge --save-format 4bit_forced   # forced single-shot path
```

Writes a BNB-4bit quantized merged checkpoint **without** the wasteful dequant → merge → requant cycle (Unsloth `merged_4bit` recipe).

## UD / IQ / Apple-ARM GGUF live

```bash
soup export --format gguf-ud --gguf-flavour UD-Q4_K_XL --calibration-data calib.jsonl
```

3-stage pipeline: `convert_hf_to_gguf.py` → `imatrix` → `quantize`. Calibration JSONL is required for any UD / IQ rung.

## Autopilot pre-quantized detection

`detect_prequantized_format(model_id)` recognises `TheBloke/...-GPTQ`, `-AWQ`, `-MLX`, GGUF names. `soup autopilot` now recommends `gptq` instead of stacking `4bit` on top of a pre-quantized checkpoint.

## Deploy autopilot scorecard

```bash
soup deploy autopilot --measure --tasks tasks.jsonl
```

Runs the picked recipe end-to-end and writes an OK / MINOR / MAJOR scorecard with a disk cache keyed on (model, hardware, tasks).

## Tests

- **7,610 → 7,722** (+112)

## See also

- [Quant Menu II reference](/docs/quant-menu-ii)
- [Speed & Memory](/docs/training-speed-memory)

[Previousv0.73.0](/docs/borrowed-hardware)[NextModality II live trainers](/docs/v0532-modality-live)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="110-v0532-modality-live"></a>

# 110. v0.53.2 — Live trainers for Modality II

*Source: <https://trysoup.dev/docs/v0532-modality-live>*

v0.52.0 shipped the schema, allowlists, and validators. v0.53.2 lights up the trainers.

## Live trainers

### `task: distill`

`DistillTrainerWrapper` — student model + frozen teacher + per-token KL divergence. Independent `trust_remote_code` flags per side.

```yaml
task: distill
base: meta-llama/Llama-3.2-1B
training:
  teacher_model: meta-llama/Llama-3.2-3B-Instruct   # under training, not at root
  distill_divergence: forward_kl   # kl | forward_kl | reverse_kl | js
  distill_temperature: 2.0          # [0.05, 100]
```

### `task: classifier | reranker | cross_encoder`

`ClassifierTrainerWrapper` covers single-label, multi-label, and cross-encoder heads.

```yaml
task: classifier
training:
  num_labels: 5
  label_names: [toxic, severe, threat, obscene, identity_hate]
```

## Reasoning effort dispatch

```yaml
training:
  reasoning_effort: high   # low | medium | high — gpt-oss family
```

Injects the `<|reasoning_effort|>` prefix into chat turns.

## Assistant-only loss + EOT unmask

`train_on_eot: true` unmasks the EOT / EOS boundary token so the model learns end-of-turn behaviour without leaking the rest of the prompt into the loss.

## EBFT + GDPO live

EBFT (`structured` / `strided`) and GDPO (`standard` / `length_normalized` / `margin`) loss kernels both land as drop-in losses behind their respective task schemas.

## Tests

- **7,722 → 7,842** (+120)

## See also

- [Modality II overview](/docs/modality-ii)
- [Training methods](/docs/training)

[PreviousQuant Menu II live writers](/docs/v053-live-writers)[NextPlugins, Anthropic, tools](/docs/v0536-7-plugins-anthropic)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="111-v0536-7-plugins-anthropic"></a>

# 111. v0.53.6 / v0.53.7 — Plugins live, Anthropic API, tool endpoints

*Source: <https://trysoup.dev/docs/v0536-7-plugins-anthropic>*

## v0.53.6 — SoupPluginCallback live

The v0.45.0 BasePlugin protocol is now wired into every HF Trainer via `SoupPluginCallback`. One bad plugin can't crash training — exceptions in plugin hooks are caught and logged, the trainer keeps going.

```bash
soup plugins list
soup plugins enable my-cool-plugin
# every soup train, dpo, grpo, ... fans HF Trainer events into the plugin
```

## Anthropic-compatible `/v1/messages` endpoint

```bash
soup serve --model ./output --backend transformers
# POST http://localhost:8000/v1/messages — Anthropic Messages shape
```

v0.53.6 ships the transformers backend; v0.53.7 adds vLLM parity plus Anthropic-shape SSE streaming.

## N-gram speculative decoding

`prompt_lookup_num_tokens` is plumbed through `_generate_response` — n-gram lookup is now a zero-config draft for inference workloads where a draft model is overkill.

## v0.53.7 — Data Recipe DAG live runner

```bash
soup data recipe --execute --output ./out recipe.yaml
```

Live runner for 6 node kinds:

- `seed` — load a starting JSONL
- `llm_text` — generate via OpenAI / Ollama / Anthropic / vLLM
- `code` — RLVR-sandbox code execution
- `judge` — LLM-as-a-judge filter
- `validator` — pydantic / regex / jsonschema gate
- `sampler` — diversity-preserving subsample

Each node writes an atomic checkpoint — interrupt and resume from the last finished node.

## Tool endpoints live

```
POST /v1/tools/python      # RLVR sandbox + 5s timeout + 512MB RLIMIT
POST /v1/tools/web_search  # bearer-auth, allowlisted providers
POST /v1/tools/bash        # 501 — deferred (re-enabled under OS-level isolation in v0.74.0)
```

## Trainer plugins lazy-imported live

6 trainer plugins ship with v0.53.7 lazy-import wiring:

- `grokfast` — gradient grokking filter
- `spectrum` — top-k parameter selection
- `llmcompressor` — compressed inference export
- `sonicmoe` — MoE routing acceleration
- `cce_plugin` — Cut Cross-Entropy as a plugin
- `math_verify` — math RLVR plugin

## Markdown + data forge polish

- `soup data ingest` now does heading-aware Markdown splits (one JSONL row per section)
- `soup data decontaminate --benchmark-file <path>` accepts operator-supplied corpora
- `soup data forge --judge-provider {ollama,anthropic,vllm}` live
- `soup data preprocess` AOT-tokenizes → Arrow shards (live)

## Tests

- v0.53.6: **7,998 → 8,051** (+53)
- v0.53.7: **8,051 → 8,162** (+111)

## See also

- [Plugins & integrations](/docs/plugins)
- [Data Forge](/docs/data-forge)

[PreviousModality II live trainers](/docs/v0532-modality-live)[NextRemote data & alt hubs](/docs/v0538-10-remote-hubs)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="112-v0538-10-remote-hubs"></a>

# 112. v0.53.8 / v0.53.10 — Remote loaders, alternative hubs, tracker extras

*Source: <https://trysoup.dev/docs/v0538-10-remote-hubs>*

## Live fsspec remote loaders

```yaml
data:
  train: s3://my-bucket/instructions.jsonl
```

Closed scheme allowlist: `s3`, `gs`, `gcs`, `az`, `abfs`, `abfss`, `oci`. The schema gate from v0.42.0 is now backed by a real loader.

## Alternative model hubs

```yaml
training:
  hub: modelscope   # hf | modelscope | modelers
```

v0.53.8 wires the dispatcher into `soup train` (pre-fetches the model before training starts). v0.53.10 plumbs the `--hub` flag through `chat` / `serve` / `infer` / `merge` / `export` / `push` and `soup data download --hub`.

SSRF hardening matches v0.29.0 HF endpoint validation: scheme allowlist, null-byte rejection, RFC1918 / link-local / cloud-metadata IPs blocked.

## Tracker extras

```bash
pip install "soup-cli[trackers]"
soup train --tracker mlflow      # or swanlab | trackio
```

The `[trackers]` extra installs `mlflow` / `swanlab` / `trackio` as one bundle. Telemetry env vars (`SOUP_TELEMETRY`, `SOUP_POSTHOG_KEY`, `SOUP_POSTHOG_ENDPOINT`) existed here with **no command wired to them**. (**Since changed**: v0.75.0 wired telemetry as strictly opt-in, off unless `SOUP_TELEMETRY=1`, with a global `--no-telemetry` flag. The shipped wheel still sends nothing even when opted in, because its bundled project key is a placeholder the sender refuses by name. [The payload, the policy and the placeholder](/docs/tracker-eval-pro).)

## HF Space SDK auto-pick

`soup deploy hf-space` detects `streamlit` vs `gradio` automatically from the template's `requirements.txt`.

## Bundled JSONL fixtures

The 4 demo bundles from v0.43.0 are now packaged as wheel data — they survive `pip install --target` and zipapp deployment.

## New extras

- `pip install "soup-cli[mix]"` — `scikit-optimize` for the Bayesian mix optimizer
- `pip install "soup-cli[data-pro]"` — `langdetect` + `presidio-analyzer` for proper langdetect / PII

## Web UI: Tool Outputs panel

The Web UI sidebar grows a "Tool Outputs" panel (3s polling, XSS-safe rendering) backed by `GET /api/tool-outputs`. SFT trainer-side `record_call` writes structured tool-call records that survive crashes.

## Tests

- v0.53.8: **8,162 → 8,257** (+95)
- v0.53.10: **8,285 → 8,330** (+45)

## See also

- [HuggingFace Hub integration](/docs/hf-hub-integration)
- [Data Pipeline Pro](/docs/data-pipeline-pro)

[PreviousPlugins, Anthropic, tools](/docs/v0536-7-plugins-anthropic)[NextLive SSE & Web UI](/docs/v0539-live-ux)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="113-v0539-live-ux"></a>

# 113. v0.53.9 — Live dashboard, Web UI mobile, bench percentiles, tokenizer trainer

*Source: <https://trysoup.dev/docs/v0539-live-ux>*

## Live SSE training stream

```
GET /api/train/stream
```

Server-sent events for every `on_log` / `on_step_end` / `on_epoch_end` event. Web UI dashboard upgrades from polling to real-time.

## Phone-scannable Web UI

```bash
soup ui --public                          # bind 0.0.0.0 + print phone QR
soup ui --public --auth-token MY_TOKEN    # override the auto-generated bearer
```

The QR encodes `http://<lan-ip>:<port>/?token=...` — scan from your phone and you're in. Auth token rotation is thread-safe; old tokens stop working immediately.

**Three things changed here in v0.75.0.** A non-loopback bind without a valid token now **exits 2** instead of warning. Authentication covers the **read** endpoints and the event streams as well as the mutating ones, where before this only the mutating ones were gated. And `--public` no longer serves `/openapi.json`, `/docs`, `/docs/oauth2-redirect` or `/redoc` at all: they are 404 off loopback and unchanged on it. See [the Web UI page](/docs/web-ui#security).

## Validation loss (v0.75.0)

Soup never stored it, on any backend. The callback read `logs["loss"]` and never `logs["eval_loss"]`, so an evaluation step left the last **training** loss in place and re-reported that to every sink: the evaluated number existed nowhere at all. There was also nowhere to put it, no `metrics` column and no event field, and the display read only `grad_norm`, `speed` and `gpu_mem` out of its keyword arguments.

The live panel gains a `Val loss` row, and the `metrics` table and the `/api/train/stream` frame each carry `val_loss` **as its own series, never folded into `loss`**.

The storage rule is the part worth knowing before you read a series back:

- The **panel** carries the last measured value forward between evaluations, so the row does not blink.
- The **stored and streamed** values do not. A step where no evaluation ran records `NULL`, so a series has one point per measurement rather than one per logged step.
- Existing `~/.soup/experiments.db` files are migrated in place, and rows written before this release read `NULL` rather than a fabricated `0.0`, **because an unmeasured value must not read as a measured one**.

The MLX backend feeds all three too, through a hook that had been called on every evaluation and done nothing, because the base-class method is a `pass` and therefore a silent no-op rather than an error. See [the MLX backend page](/docs/mlx-backend).

## Standalone CLIs

```bash
soup tokenizer train --input corpus.jsonl --vocab-size 32000 --output tok/
soup bench ./output --p50 --p95           # per-prompt tail-latency percentiles
soup bench ./output --backend auto         # auto-detect transformers vs mlx
```

## Reasoning parser

```bash
soup serve --reasoning-parser deepseek-r1  # | qwen3 | phi4 | openthinker
soup serve --max-model-len 8192              # vLLM only (v0.73.0): lower it when the
                                             # engine refuses to start because the KV
                                             # cache does not fit. Default: the model's own maximum
```

Strips `<think>...</think>` blocks from streamed responses while still surfacing them via the tool-outputs sidebar.

## Tool outputs polling

```
GET /api/tool-outputs
```

JSON poll of the most-recent tool-call records — paired with the Web UI Tool Outputs panel.

## Tests

- **8,257 → 8,285** (+28)

## See also

- [Web UI](/docs/web-ui)
- [Serving](/docs/serving)

[PreviousRemote data & alt hubs](/docs/v0538-10-remote-hubs)[NextGRPO Plus + preference](/docs/v05311-grpo-prm-longlora)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---

<a id="114-v05311-grpo-prm-longlora"></a>

# 114. v0.53.11 — GRPO variants live, PRM live, LongLoRA live, weighted preference

*Source: <https://trysoup.dev/docs/v05311-grpo-prm-longlora>*

The capstone of the v0.50 / v0.49 / v0.40 deferred-stub debt. Five deep TRL trainer-subclassing items lifted.

## Six GRPO objective variants live

`apply_variant_loss` ships real math kernels for every non-standard variant:

- `gspo` — **replaced in v0.75.0** and no longer what this line used to describe. It was a group-stabilised, column-centered importance ratio; it is now the published **Group Sequence Policy Optimization** objective (Qwen Team, [arXiv:2507.18071](https://arxiv.org/abs/2507.18071)): a length-normalised **sequence** importance ratio with sequence-level surrogate clipping, masked tokens held at exactly 0.0 gradient, invariant to padding and to its placement, and invariant to batch permutation. **An existing `gspo` config will not reproduce prior runs.** The heuristic it replaced also centred the per-token log-ratio across the batch \*before\* applying the completion mask, so one padding token shifted the loss and gradient of every unmasked row sharing its column
- `dapo` — decoupled asymmetric clip
- `dr_grpo` — no length normalization
- `bnpo` — length-normalised PPO
- `two_sided` — symmetric `grpo_delta` clip
- `rft` — rejection-sampling fine-tuning

Subclassing is done via `make_grpo_trainer_variant` (an `lru_cache` factory over `_GRPOTrainerVariant`) that overrides `compute_loss` to route through the kernel, with a defensive fallback to the original loss if TRL renames input attributes.

## `task: prm` Process Reward Model — live

`PRMTrainerWrapper` loads `AutoModelForCausalLM` + `nn.Linear(hidden, 1)` as the reward head. `make_prm_trainer_class(HF Trainer)` factory subclasses Trainer and overrides `compute_loss` to:

1. Gather hidden states at step-boundary tokens
2. Project to scalars through the linear head
3. MSE-loss against per-step labels

`_prepare_prm_dataset` tokenizes `{prompt, completions, labels}` with reserved-token truncation; `_build_collator` pads with `-1` sentinel for missing step positions.

```yaml
task: prm
base: deepseek-ai/deepseek-math-7b-base
data:
  train: prm_steps.jsonl
  format: prm   # {prompt, completions, labels}
```

## GRPOStabilityCallback live

- EMA reference-model update fires post-step: `(1-α) * ref + α * policy` per parameter (`load_state_dict(strict=False)` so LoRA state stays valid)
- Bounded-deque replay buffer
- TIS (truncated importance sampling) alert counter
- `ema_alpha` surfaced via `state.log_history` so `soup why` can flag instability

## LongLoRA S² forward override live

The v0.49.0 schema is now backed by a runtime. `shift_heads_for_s2` rolls the second half of attention heads by `group_size // 2` along the sequence axis (LongLoRA paper §3.2). `LongLoRAForwardOverride` is a context manager that monkey-patches every Llama / Mistral / Qwen / Phi attention module's `forward`, restoring on exit. Idempotent `__del__` cleanup and best-effort exception swallow ensure training never crashes from a shape mismatch.

## True weighted-sum preference combine

`attach_weighted_preference_combine` now reads the four logprob tensors from TRL inputs (`policy_chosen_logps` / `policy_rejected_logps` / `reference_chosen_logps` / `reference_rejected_logps`) and computes each requested loss via the matching kernel:

- `compute_dpo_term`
- `compute_ipo_term`
- `compute_simpo_term`
- `compute_orpo_term`

Then combines via `combine_losses(terms, weights)`. BCO mixed with paired losses is still rejected at validation time. Defence-in-depth fallback to the v0.40.1 primary-loss scaling when TRL renames the logps attributes.

```yaml
task: preference
training:
  preference_loss_weights:
    dpo: 0.7
    simpo: 0.3
```

## Tests

- **8,330 → 8,400** (+75) in `test_v05311.py` (54 initial + 21 review-fix coverage gaps from python / code / security / tdd review agents).
- Math kernels are real and unit-tested. Full GPU smoke runs documented in the v0.53.11.1 follow-up plan.

## See also

- [GRPO Plus reference](/docs/grpo-plus)
- [Long Context](/docs/long-context)
- [Preference Variety](/docs/preference-variety)

[PreviousLive SSE & Web UI](/docs/v0539-live-ux)

Soup is free and Apache-2.0. If it saved you a training run, [starring the repo](https://github.com/MakazhanAlpamys/Soup) costs nothing and helps most. You can also [fund the GPU time](/support) behind the work a 4 GB laptop cannot reach.

---
