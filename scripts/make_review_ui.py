#!/usr/bin/env python3
"""
Génère l'INTERFACE DE REVUE des paires d'alignement (review.html à la racine).

But : transformer les 324 paires interpolées en lignes d'entraînement fiables
rapidement. Pour chaque ligne : l'image calligraphique + le texte proposé
(issu de la référence alignée), que tu **valides**, **corriges** ou **rejettes**.

Caractéristiques :
- Images en **chemins relatifs** (pas de base64) → page légère, images nettes,
  chargement paresseux. À ouvrir depuis la racine du projet.
- **Sauvegarde automatique** dans le navigateur (localStorage) : tu peux fermer
  et reprendre.
- **Clavier** : Entrée = valider + suivant · ✗ = rejeter · ↑/↓ = naviguer.
- **Export JSON** → `review.json`, à réinjecter avec `scripts/apply_review.py`.

Usage :
    python scripts/make_review_ui.py            # toutes les paires à revoir
    python scripts/make_review_ui.py --all      # y compris les ancres
    python scripts/make_review_ui.py --pages 1-5
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAIRS = ROOT / "data" / "alignment" / "pairs.jsonl"
GOLD = ROOT / "data" / "test_set" / "gold.jsonl"
OUT = ROOT / "review.html"
IMG_BASE = "data/lines/khassida"


def load_jsonl(p):
    p = Path(p)
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.exists() else []


def parse_pages(spec):
    if not spec:
        return None
    out = set()
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if "-" in chunk:
            a, b = chunk.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        elif chunk:
            out.add(int(chunk))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--all", action="store_true", help="Inclure aussi les ancres")
    ap.add_argument("--pages", default="", help="Restreindre, ex. '1-5' ou '1,3'")
    args = ap.parse_args()

    pairs = load_jsonl(PAIRS)
    gold_paths = {g["path"] for g in load_jsonl(GOLD)}
    pages = parse_pages(args.pages)

    items = []
    for p in pairs:
        if p["line_path"] in gold_paths:
            continue  # déjà vérité terrain
        if not args.all and not p.get("needs_review", True):
            continue
        page = int(p["line_path"].split("/")[0].split("-")[1])
        if pages and page not in pages:
            continue
        items.append({
            "id": p["line_id"],
            "path": p["line_path"],
            "page": page,
            "text": p["ref_text"],
            "method": p["method"],
            "score": p.get("score"),
        })

    data = json.dumps(items, ensure_ascii=False)
    html = f"""<!doctype html><html lang=fr><head><meta charset=utf-8>
<title>Revue d'alignement — Khassida</title>
<style>
:root{{--cream:#f7f4ed;--ink:#1c1c1c;--line:#eceae4;--muted:#5f5f5d}}
*{{box-sizing:border-box}}
body{{font-family:-apple-system,system-ui,sans-serif;margin:0;background:var(--cream);color:var(--ink)}}
header{{position:sticky;top:0;background:var(--cream);border-bottom:1px solid var(--line);
  padding:12px 20px;z-index:10;display:flex;gap:16px;align-items:center;flex-wrap:wrap}}
h1{{font-size:17px;margin:0}}
.meter{{flex:1;min-width:180px;height:10px;background:var(--line);border-radius:99px;overflow:hidden}}
.meter div{{height:100%;background:#1c7d3f;width:0}}
.count{{font-variant-numeric:tabular-nums;font-size:14px}}
button{{font:inherit;border:1px solid rgba(28,28,28,.4);background:transparent;color:var(--ink);
  border-radius:6px;padding:7px 13px;cursor:pointer}}
button.primary{{background:var(--ink);color:#fcfbf8;border-color:var(--ink)}}
button:active{{opacity:.8}}
main{{max-width:1100px;margin:0 auto;padding:18px 20px 120px}}
.card{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin:0 0 14px;
  scroll-margin-top:90px}}
.card.cur{{border-color:#b45309;box-shadow:0 4px 16px rgba(180,83,9,.18)}}
.card.ok{{border-left:5px solid #1c7d3f}} .card.no{{border-left:5px solid #b91c1c;opacity:.6}}
.meta{{display:flex;gap:10px;align-items:center;font-size:12px;color:var(--muted);margin-bottom:8px}}
.badge{{border:1px solid var(--line);border-radius:99px;padding:1px 9px}}
.badge.anchor{{background:#ecfdf5;border-color:#a7f3d0;color:#065f46}}
img{{width:100%;display:block;border:1px solid var(--line);border-radius:8px;background:#fff}}
textarea{{width:100%;font-size:26px;line-height:1.9;direction:rtl;text-align:right;margin-top:10px;
  padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--cream);
  color:var(--ink);resize:vertical;min-height:74px}}
.acts{{display:flex;gap:8px;margin-top:10px;align-items:center}}
.hint{{font-size:12px;color:var(--muted);margin-left:auto}}
footer{{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid var(--line);
  padding:10px 20px;display:flex;gap:12px;align-items:center;justify-content:center}}
kbd{{border:1px solid var(--line);border-bottom-width:2px;border-radius:4px;padding:1px 6px;
  font-family:ui-monospace,Menlo,monospace;font-size:11px;background:var(--cream)}}
</style></head><body>
<header>
  <h1>Revue d'alignement</h1>
  <div class=meter><div id=bar></div></div>
  <span class=count id=cnt>0</span>
  <button onclick=exportJSON()>⬇ Exporter review.json</button>
</header>
<main id=list></main>
<footer>
  <span class=hint><kbd>Entrée</kbd> valider + suivant · <kbd>x</kbd> rejeter ·
  <kbd>↑</kbd><kbd>↓</kbd> naviguer · sauvegarde auto</span>
</footer>
<script>
const ITEMS = {data};
const KEY = 'khassida_review_v1';
let state = JSON.parse(localStorage.getItem(KEY) || '{{}}');
let cur = 0;

function save(){{ localStorage.setItem(KEY, JSON.stringify(state)); paint(); }}

function paint(){{
  const done = Object.values(state).filter(s=>s.status==='ok').length;
  document.getElementById('bar').style.width = (done/ITEMS.length*100)+'%';
  document.getElementById('cnt').textContent = done+' / '+ITEMS.length+' validées';
  ITEMS.forEach((it,i)=>{{
    const c = document.getElementById('c'+i);
    const st = state[it.path];
    c.className = 'card' + (i===cur?' cur':'') + (st? (st.status==='ok'?' ok':' no') : '');
  }});
}}

function render(){{
  document.getElementById('list').innerHTML = ITEMS.map((it,i)=>{{
    const st = state[it.path];
    const txt = st && st.text!==undefined ? st.text : it.text;
    const badge = it.method==='anchor'
      ? `<span class="badge anchor">ancre ${{it.score??''}}</span>`
      : `<span class=badge>interpolée</span>`;
    return `<div class=card id=c${{i}}>
      <div class=meta><b>#${{i+1}}</b> <span>p.${{it.page}}</span>
        <code>${{it.path}}</code> ${{badge}}</div>
      <img loading=lazy src="{IMG_BASE}/${{it.path}}" onclick="focusI(${{i}})">
      <textarea id=t${{i}} dir=rtl oninput="edit(${{i}})" onfocus="cur=${{i}};paint()">${{txt}}</textarea>
      <div class=acts>
        <button class=primary onclick="ok(${{i}})">✓ Valider</button>
        <button onclick="no(${{i}})">✗ Rejeter</button>
        <span class=hint>illisible / mal segmentée → rejeter</span>
      </div></div>`;
  }}).join('');
  paint();
}}

function edit(i){{
  const it=ITEMS[i]; const v=document.getElementById('t'+i).value;
  state[it.path] = {{...(state[it.path]||{{}}), text:v, status:(state[it.path]||{{}}).status||null}};
  localStorage.setItem(KEY, JSON.stringify(state));
}}
function ok(i){{
  const it=ITEMS[i];
  state[it.path] = {{text:document.getElementById('t'+i).value, status:'ok',
                    corrected:document.getElementById('t'+i).value!==it.text}};
  save(); next(i);
}}
function no(i){{
  const it=ITEMS[i];
  state[it.path] = {{text:document.getElementById('t'+i).value, status:'rejected'}};
  save(); next(i);
}}
function next(i){{ focusI(Math.min(ITEMS.length-1, i+1)); }}
function focusI(i){{
  cur=i; const el=document.getElementById('c'+i);
  el.scrollIntoView({{block:'center',behavior:'smooth'}});
  document.getElementById('t'+i).focus(); paint();
}}
document.addEventListener('keydown', e=>{{
  if(e.key==='Enter' && !e.shiftKey){{ e.preventDefault(); ok(cur); }}
  else if(e.key==='ArrowDown' && e.altKey){{ e.preventDefault(); focusI(Math.min(ITEMS.length-1,cur+1)); }}
  else if(e.key==='ArrowUp' && e.altKey){{ e.preventDefault(); focusI(Math.max(0,cur-1)); }}
  else if(e.key==='x' && e.ctrlKey){{ e.preventDefault(); no(cur); }}
}});
function exportJSON(){{
  const rows = ITEMS.filter(it=>state[it.path]&&state[it.path].status)
    .map(it=>({{path:it.path, line_id:it.id, status:state[it.path].status,
                text:state[it.path].text, corrected:!!state[it.path].corrected}}));
  const blob = new Blob([JSON.stringify(rows,null,2)],{{type:'application/json'}});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(blob); a.download='review.json'; a.click();
}}
render();
</script></body></html>"""

    OUT.write_text(html, encoding="utf-8")
    n_anchor = sum(1 for i in items if i["method"] == "anchor")
    print(f"Interface de revue : {len(items)} lignes ({n_anchor} ancres) → {OUT}")
    print("Ouvre-la DEPUIS LA RACINE du projet (les images sont en chemins relatifs) :")
    print("  open review.html")
    print("Puis : valider/corriger → ⬇ Exporter review.json → "
          "python scripts/apply_review.py ~/Downloads/review.json")


if __name__ == "__main__":
    main()
