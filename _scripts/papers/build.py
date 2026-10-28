#!/usr/bin/env python3
"""Build GCSE practice-paper PDFs (questions + worked solutions).

Content lives in the `content` package as plain Python data; this module turns
it into print-ready HTML and then into PDFs via headless Chrome.

Usage:
    python3 _scripts/papers/build.py            # build every paper
    python3 _scripts/papers/build.py number     # build just these keys
"""
import html as _html
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ──────────────────────────────────────────────────────────── styling ──
CSS = """
@page { size: A4; margin: 16mm 15mm 14mm 15mm; }
* { box-sizing: border-box; }
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 10.6pt; line-height: 1.5; color: #111; margin: 0;
}
.banner {
  background: #4f46e5; color: #fff;
  padding: 11px 15px; border-radius: 7px; margin-bottom: 4mm;
}
.banner h1 { margin: 0; font-size: 15pt; }
.banner .sub { font-size: 9pt; opacity: .93; margin-top: 2px; }
.meta {
  display: flex; justify-content: space-between;
  font-size: 8.6pt; color: #444;
  border-bottom: 1px solid #c7d2fe; padding-bottom: 5px; margin-bottom: 5mm;
}
.sect {
  background: #eef2ff; border-left: 4px solid #4f46e5;
  padding: 7px 12px; margin: 6mm 0 4mm; border-radius: 0 5px 5px 0;
  break-after: avoid;
}
.sect h2 { margin: 0; font-size: 11.5pt; color: #3730a3; }
.sect .note { font-size: 8.8pt; color: #555; margin-top: 1px; }
.q { break-inside: avoid; margin-bottom: 4.5mm; }
.qhead { display: flex; align-items: baseline; gap: 8px; margin-bottom: 2px; }
.qn {
  background: #4f46e5; color: #fff; font-weight: 700; font-size: 9pt;
  min-width: 19px; height: 19px; border-radius: 50%;
  display: inline-flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.marks { margin-left: auto; font-size: 8.8pt; color: #6d28d9; font-weight: 700; white-space: nowrap; }
.qbody { padding-left: 27px; }
.qbody p { margin: 0 0 3px; }
.part { margin: 2px 0 2px 12px; }
.ans { border-bottom: 1px dotted #9aa; margin: 3mm 27px 0 27px; }
.ans.h1 { height: 8mm; } .ans.h2 { height: 14mm; }
.ans.h3 { height: 20mm; } .ans.h4 { height: 27mm; }
.sol { padding-left: 27px; margin-top: 2px; }
.step { display: flex; gap: 7px; margin: 2px 0; align-items: flex-start; }
.sn { color: #6d28d9; font-weight: 700; flex-shrink: 0; font-size: 9.6pt; }
.final {
  background: #f0fdf4; border-left: 3px solid #22c55e;
  padding: 4px 9px; margin-top: 4px; border-radius: 0 4px 4px 0; font-size: 10.2pt;
}
.final b { color: #166534; }
table.d { border-collapse: collapse; margin: 3px 0; font-size: 9.6pt; }
table.d td, table.d th { border: 1px solid #94a3b8; padding: 2.5px 8px; text-align: center; }
table.d th { background: #eef2ff; font-weight: 700; }
.frac { display: inline-block; vertical-align: -0.55em; text-align: center; margin: 0 .12em; }
.frac .n { display: block; padding: 0 .28em; font-size: .92em; }
.frac .d { display: block; padding: 0 .28em; border-top: 1.1px solid #111; font-size: .92em; }
.v { font-style: italic; }
.cv { display: inline-flex; align-items: center; vertical-align: -0.55em; margin: 0 .1em; }
.cv .b { font-size: 1.9em; line-height: 1; font-weight: 300; }
.cv .k { display: inline-block; text-align: center; padding: 0 .16em; line-height: 1.2; font-size: .9em; }
.cv .k span { display: block; }
.foot {
  margin-top: 7mm; padding-top: 4px; border-top: 1px solid #c7d2fe;
  font-size: 8.2pt; color: #777; text-align: center;
}
svg { display: block; margin: 3px 0 3px 0; }
"""

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>
<div class="banner"><h1>{h1}</h1><div class="sub">{sub}</div></div>
<div class="meta"><span>{left}</span><span>jtmaths.org &middot; free maths resources</span></div>
{body}
<div class="foot">{foot}</div>
</body></html>
"""


def frac(n, d):
    """Stacked fraction, safe in both PDFs."""
    return f'<span class="frac"><span class="n">{n}</span><span class="d">{d}</span></span>'


def col(a, b):
    """A 2 x 1 column vector in round brackets."""
    return ('<span class="cv"><span class="b">(</span><span class="k">'
            f'<span>{a}</span><span>{b}</span>'
            '</span><span class="b">)</span></span>')


def _space_class(marks):
    return "h1" if marks <= 1 else "h2" if marks <= 2 else "h3" if marks <= 4 else "h4"


def _questions_html(items, start=1, with_space=True):
    out = []
    for i, q in enumerate(items, start):
        space = f'<div class="ans {_space_class(q["marks"])}"></div>' if with_space else ""
        plural = "" if q["marks"] == 1 else "s"
        out.append(
            f'<div class="q"><div class="qhead"><span class="qn">{i}</span>'
            f'<span class="marks">[{q["marks"]} mark{plural}]</span></div>'
            f'<div class="qbody">{q["q"]}</div>{space}</div>'
        )
    return "\n".join(out)


def _solutions_html(items, start=1):
    out = []
    for i, q in enumerate(items, start):
        steps = "".join(
            f'<div class="step"><span class="sn">{n}</span><span>{s}</span></div>'
            for n, s in enumerate(q["steps"], 1)
        )
        plural = "" if q["marks"] == 1 else "s"
        out.append(
            f'<div class="q"><div class="qhead"><span class="qn">{i}</span>'
            f'<span class="marks">[{q["marks"]} mark{plural}]</span></div>'
            f'<div class="qbody">{q["q"]}</div>'
            f'<div class="sol">{steps}'
            f'<div class="final"><b>Answer:</b> {q["answer"]}</div></div></div>'
        )
    return "\n".join(out)


FOUND_NOTE = ("Questions 1&ndash;3 are the most straightforward; they get harder "
              "as you go on. Question 10 is the most challenging.")
HIGHER_NOTE = ("Higher-tier style. Again, questions 1&ndash;3 are the gentlest and "
               "question 10 is the hardest.")


def render(paper, solutions):
    """Return the full HTML string for one paper."""
    f, h = paper["foundation"], paper["higher"]
    kind = "Worked Solutions" if solutions else "Practice Questions"
    body = (
        f'<div class="sect"><h2>Section A &middot; Foundation</h2>'
        f'<div class="note">{FOUND_NOTE}</div></div>'
        + (_solutions_html(f) if solutions else _questions_html(f))
        + f'<div class="sect"><h2>Section B &middot; Higher</h2>'
          f'<div class="note">{HIGHER_NOTE}</div></div>'
        + (_solutions_html(h) if solutions else _questions_html(h))
    )
    total = sum(q["marks"] for q in f + h)
    return PAGE.format(
        css=CSS,
        title=f'{paper["title"]} — {kind}',
        h1=_html.escape(paper["title"]),
        sub=f'GCSE Maths &middot; {kind}',
        left=f'20 questions &middot; {total} marks total',
        body=body,
        foot=("Worked solutions &middot; " if solutions else "")
             + "jtmaths.org &middot; free maths resources for everyone",
    )


def to_pdf(html_str, pdf_path):
    tmp = pdf_path + ".tmp.html"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(html_str)
    res = subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", "file://" + os.path.abspath(tmp)],
        capture_output=True, text=True, timeout=180,
    )
    os.remove(tmp)
    if not os.path.isfile(pdf_path) or os.path.getsize(pdf_path) < 2000:
        raise RuntimeError(f"PDF not produced for {pdf_path}\n{res.stderr[-600:]}")
    return os.path.getsize(pdf_path)


def build(paper):
    """Write both PDFs for one paper. Returns (questions_path, solutions_path)."""
    for key in ("title", "folder", "slug", "foundation", "higher"):
        if key not in paper:
            raise KeyError(f"paper missing '{key}'")
    for sec in ("foundation", "higher"):
        if len(paper[sec]) != 10:
            raise ValueError(f'{paper["slug"]}: {sec} has {len(paper[sec])} questions, need 10')
        for n, q in enumerate(paper[sec], 1):
            for k in ("q", "marks", "steps", "answer"):
                if k not in q:
                    raise KeyError(f'{paper["slug"]} {sec} Q{n}: missing "{k}"')
            if not q["steps"]:
                raise ValueError(f'{paper["slug"]} {sec} Q{n}: no solution steps')

    folder = os.path.join(ROOT, paper["folder"])
    os.makedirs(folder, exist_ok=True)
    qp = os.path.join(folder, f'{paper["slug"]}-questions.pdf')
    sp = os.path.join(folder, f'{paper["slug"]}-solutions.pdf')
    to_pdf(render(paper, False), qp)
    to_pdf(render(paper, True), sp)
    return qp, sp


def main(argv):
    from content import PAPERS
    keys = argv or sorted(PAGE and PAPERS.keys())
    unknown = [k for k in keys if k not in PAPERS]
    if unknown:
        print("Unknown paper key(s):", ", ".join(unknown))
        print("Available:", ", ".join(sorted(PAPERS)))
        return 1
    for k in keys:
        p = PAPERS[k]
        qp, sp = build(p)
        marks = sum(q["marks"] for q in p["foundation"] + p["higher"])
        print(f'  {k:34s} {marks:3d} marks  '
              f'{os.path.getsize(qp)//1024:4d}KB + {os.path.getsize(sp)//1024:4d}KB')
    print(f"\n{len(keys)} paper(s) built = {len(keys)*2} PDFs")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    sys.exit(main(sys.argv[1:]))
