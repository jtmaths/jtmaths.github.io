#!/usr/bin/env python3
"""Add / refresh the "Practice papers" section in each GCSE topic index.md.

Driven by the same `content` package that builds the PDFs, so the links can
never drift from the files that actually exist.

Usage:
    python3 _scripts/papers/link_indexes.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

START = "<!-- PAPERS:START -->"
END = "<!-- PAPERS:END -->"

# Topic folder -> (index path, ordered list of paper slugs)
ORDER = [
    ("gcse/number", [
        "number-practice", "fractions-practice", "percentages-practice",
        "powers-practice", "rounding-practice",
    ]),
    ("gcse/algebra", [
        "algebra-practice", "equations-practice", "brackets-practice",
        "simultaneous-practice", "sequences-practice", "inequalities-practice",
    ]),
    ("gcse/quadratics", [
        "quadratics-practice", "quadratics-factorising-practice",
        "quadratic-formula-practice", "completing-the-square-practice",
    ]),
    ("gcse/graphs", [
        "graphs-practice", "straight-line-graphs-practice",
        "quadratic-graphs-practice", "real-life-graphs-practice",
    ]),
    ("gcse/ratio", [
        "ratio-practice", "ratio-notation-practice", "proportion-practice",
        "compound-measures-practice", "similar-shapes-practice", "growth-decay-practice",
    ]),
    ("gcse/geometry", [
        "geometry-practice", "angle-rules-practice", "pythagoras-trig-practice",
        "circle-theorems-practice", "transformations-practice",
        "area-volume-practice", "vectors-practice",
    ]),
    ("gcse/probability", [
        "probability-practice", "tree-diagrams-practice",
        "conditional-probability-practice",
    ]),
    ("gcse/statistics", [
        "statistics-practice", "averages-practice", "histograms-practice",
    ]),
]

BLURB = ("Printable A4 practice papers. Each paper has 10 foundation-level questions and "
         "10 higher-level questions, with the easiest first and the hardest last, and comes "
         "with a second PDF that works through every question step by step.")


def build_section(topic_folder, slugs, papers):
    """Return the markdown block for one topic, or raise if a PDF is missing."""
    lines = [START, "", "## Practice papers", "", BLURB, ""]
    for i, slug in enumerate(slugs):
        paper = papers[slug]
        # relative path from the topic index to the paper's folder
        rel = os.path.relpath(paper["folder"], topic_folder)
        prefix = "" if rel == "." else rel + "/"
        qs = f'{prefix}{slug}-questions.pdf'
        sol = f'{prefix}{slug}-solutions.pdf'
        for p in (qs, sol):
            full = os.path.join(ROOT, topic_folder, p)
            if not os.path.isfile(full):
                raise FileNotFoundError(full)
        label = paper["title"] + (" &mdash; whole topic" if i == 0 else "")
        lines.append(f'* **{label}** &middot; [questions]({qs}) &middot; [solutions]({sol})')
    lines += ["", END]
    return "\n".join(lines)


def splice(path, block):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if pattern.search(text):
        new = pattern.sub(lambda _: block, text)
    else:
        new = text.rstrip("\n") + "\n\n" + block + "\n"
    if new != text:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
        return True
    return False


def main():
    sys.path.insert(0, HERE)
    from content import PAPERS

    known = {s for _, slugs in ORDER for s in slugs}
    missing = sorted(set(PAPERS) - known)
    if missing:
        print("Papers not listed in ORDER:", ", ".join(missing))
        return 1
    unknown = sorted(known - set(PAPERS))
    if unknown:
        print("ORDER lists unknown papers:", ", ".join(unknown))
        return 1

    total = 0
    for topic_folder, slugs in ORDER:
        index = os.path.join(ROOT, topic_folder, "index.md")
        if not os.path.isfile(index):
            print("No index.md for", topic_folder)
            return 1
        block = build_section(topic_folder, slugs, PAPERS)
        changed = splice(index, block)
        total += len(slugs)
        print(f'  {topic_folder:20s} {len(slugs)} papers  '
              f'({len(slugs) * 2} PDFs)  {"updated" if changed else "unchanged"}')
    print(f"\n{total} papers linked, {total * 2} PDF links, all files verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
