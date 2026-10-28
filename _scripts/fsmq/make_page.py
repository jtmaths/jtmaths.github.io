#!/usr/bin/env python3
"""Wrap a body fragment in the standard self-contained JT Maths page shell.

The FSMQ pages use exactly the same styling as the GCSE pages so the two
sections of the site look and behave identically, and every generated file is
a stand-alone HTML document that works offline.

Usage:
    python3 _scripts/fsmq/make_page.py fsmq/algebra/polynomials.html \
        --title "Polynomials" --icon "🧮" \
        --sub "OCR FSMQ Additional Maths · Algebra (AL3–AL4)" \
        --badge "Level 3 · Ages 15–16" \
        --back overview.html \
        --footer "Polynomials (AL3–AL4) · OCR FSMQ Additional Maths" < body.html
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

STYLE = """\
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; line-height: 1.65; color: #1e1e2e; background: #f6f5ff; padding: 0 0 60px; }
    header { background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); color: #fff; padding: 40px 24px 32px; text-align: center; }
    header h1 { font-size: 2.2rem; margin-bottom: 8px; }
    header p  { font-size: 1.05rem; opacity: .9; }
    .badge { display: inline-block; background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.4); border-radius: 20px; padding: 3px 14px; font-size: .85rem; margin-top: 10px; }
    main { max-width: 860px; margin: 0 auto; padding: 28px 20px; }
    .section-title { display: flex; align-items: center; gap: 10px; background: #4f46e5; color: #fff; border-radius: 10px 10px 0 0; padding: 13px 20px; font-size: 1.2rem; font-weight: 700; margin-top: 36px; }
    .section-title .num { background: rgba(255,255,255,.25); border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 1rem; font-weight: 800; flex-shrink: 0; }
    .section-body { background: #fff; border: 1px solid #c7d2fe; border-top: none; border-radius: 0 0 10px 10px; padding: 22px 24px; }
    .concept { background: #eef2ff; border-left: 4px solid #4f46e5; border-radius: 6px; padding: 14px 18px; margin: 14px 0; }
    .concept strong { color: #3730a3; }
    .formula-box { background: #f5f3ff; border: 2px solid #7c3aed; border-radius: 8px; padding: 14px 20px; margin: 16px 0; text-align: center; font-size: 1.1rem; }
    .formula-box .label { font-size: .8rem; text-transform: uppercase; letter-spacing: .05em; color: #6d28d9; font-weight: 700; margin-bottom: 6px; }
    .steps { counter-reset: step; list-style: none; margin: 12px 0; }
    .steps li { counter-increment: step; display: flex; gap: 12px; margin-bottom: 10px; }
    .steps li::before { content: counter(step); background: #4f46e5; color: #fff; border-radius: 50%; min-width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; font-size: .85rem; font-weight: 700; flex-shrink: 0; margin-top: 1px; }
    .example { background: #faf5ff; border: 1px solid #ddd6fe; border-radius: 8px; margin: 18px 0; overflow: hidden; }
    .example-header { background: #7c3aed; color: #fff; padding: 8px 16px; font-weight: 700; font-size: .95rem; }
    .example-body { padding: 16px 20px; }
    .example-body p { margin-bottom: 8px; }
    .step-row { display: flex; gap: 10px; background: #ede9fe; border-radius: 6px; padding: 8px 12px; margin: 6px 0; align-items: flex-start; }
    .step-row .arrow { color: #6d28d9; font-weight: 800; flex-shrink: 0; }
    .tip { background: #fefce8; border-left: 4px solid #eab308; border-radius: 6px; padding: 12px 16px; margin: 14px 0; font-size: .95rem; }
    .tip strong { color: #92400e; }
    .warn { background: #fef2f2; border-left: 4px solid #ef4444; border-radius: 6px; padding: 12px 16px; margin: 14px 0; font-size: .95rem; }
    .warn strong { color: #b91c1c; }
    table { width: 100%; border-collapse: collapse; margin: 14px 0; }
    th { background: #4f46e5; color: #fff; padding: 9px 14px; text-align: left; font-size: .9rem; }
    td { padding: 9px 14px; border-bottom: 1px solid #e0e7ff; font-size: .95rem; }
    tr:last-child td { border-bottom: none; }
    tr:nth-child(even) td { background: #f5f3ff; }
    .svg-block { text-align: center; margin: 18px 0; }
    .svg-block svg { max-width: 100%; }
    .question { background: #fff; border: 1px solid #c7d2fe; border-radius: 8px; margin: 12px 0; overflow: hidden; }
    .question-header { background: #eef2ff; padding: 10px 16px; font-weight: 700; color: #3730a3; font-size: .95rem; }
    .question-body { padding: 10px 16px; }
    details summary { cursor: pointer; color: #4f46e5; font-weight: 600; padding: 8px 0 4px; font-size: .9rem; user-select: none; }
    details summary:hover { color: #3730a3; }
    .solution { background: #f0fdf4; border-left: 3px solid #22c55e; border-radius: 4px; padding: 12px 14px; margin-top: 8px; font-size: .93rem; }
    .solution p { margin-bottom: 6px; }
    .ref-grid { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 14px; }
    .ref-card { flex: 1; min-width: 180px; background: #f5f3ff; border: 1px solid #c4b5fd; border-radius: 8px; padding: 13px 15px; }
    .ref-card h4 { color: #4f46e5; font-size: .95rem; margin-bottom: 6px; }
    .ref-card p  { font-size: .88rem; line-height: 1.5; }
    .topic-list { list-style: none; margin: 10px 0; }
    .topic-list li { display: flex; gap: 12px; align-items: flex-start; background: #fafafe; border: 1px solid #ddd6fe; border-radius: 8px; padding: 11px 14px; margin-bottom: 8px; }
    .topic-list .code { background: #4f46e5; color: #fff; border-radius: 6px; font-size: .78rem; font-weight: 800; padding: 2px 8px; flex-shrink: 0; margin-top: 3px; min-width: 34px; text-align: center; }
    .topic-list a { color: #4338ca; font-weight: 700; text-decoration: none; }
    .topic-list a:hover { text-decoration: underline; }
    .topic-list .desc { display: block; font-size: .88rem; color: #444; }
    .backlink { display:inline-block; margin-top:6px; font-size:.85rem; color:#e0e7ff; text-decoration:none; }
    .backlink:hover { text-decoration:underline; }
    @media (max-width: 600px) { header h1 { font-size: 1.5rem; } .ref-grid { flex-direction: column; } }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} &ndash; OCR FSMQ Additional Maths</title>
  <script>
    MathJax = {{
      tex: {{
        inlineMath: [['\\\\(', '\\\\)'], ['$', '$']],
        displayMath: [['\\\\[', '\\\\]'], ['$$', '$$']],
        tags: 'none'
      }},
      options: {{ skipHtmlTags: ['script','noscript','style','textarea','pre'] }}
    }};
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script" async></script>
  <style>
{style}  </style>
</head>
<body>

<header>
  <h1>{icon} {title}</h1>
  <p>{sub}</p>
  <div class="badge">{badge}</div>{backlink}
</header>

<main>

{body}

<div style="text-align:center;margin-top:40px;color:#888;font-size:.85rem;">
  {footer} &middot; Created with MathJax
</div>

</main>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--title", required=True)
    ap.add_argument("--sub", required=True)
    ap.add_argument("--icon", default="")
    ap.add_argument("--badge", default="Level 3 &middot; Ages 15&ndash;16")
    ap.add_argument("--back", default="")
    ap.add_argument("--footer", default="")
    a = ap.parse_args()

    backlink = ""
    if a.back:
        backlink = ('<br>\n  <a class="backlink" href="%s">'
                    "&larr; Back to topic overview</a>" % a.back)

    page = TEMPLATE.format(
        title=a.title, sub=a.sub, icon=a.icon, badge=a.badge,
        backlink=backlink, style=STYLE,
        footer=a.footer or f"{a.title} &middot; OCR FSMQ Additional Maths",
        body=sys.stdin.read().rstrip(),
    )

    dest = os.path.join(ROOT, a.out)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"wrote {a.out} ({len(page.splitlines())} lines)")


if __name__ == "__main__":
    main()
