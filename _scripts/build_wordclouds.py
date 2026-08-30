#!/usr/bin/env python3
"""Generate the GCSE word-cloud blocks for index.md and gcse/index.md.

Single source of truth for every topic/subtopic link. Validates that each
target file actually exists before writing anything.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root

# (folder, Topic label, size, [(label, file, size), ...])
TOPICS = [
    ("number", "Number", "xl", [
        ("Overview of Numbers", "overview.html", "md"),
        ("BIDMAS / BODMAS", "bidmas.html", "sm"),
        ("BIDMAS Misconceptions", "bidmas2.html", "xs"),
        ("Powers and Roots", "powers.html", "sm"),
        ("Prime Numbers", "primes.html", "sm"),
        ("Fractions and Decimals", "fractions.html", "md"),
        ("Recurring Decimals", "fractions2.html", "xs"),
        ("Percentages", "percentage.html", "md"),
        ("Factors and Multiples", "factors.html", "sm"),
        ("Prime Factors", "primefactors.html", "xs"),
        ("Systematic Listing", "lists.html", "xs"),
        ("Surds", "surds.html", "sm"),
        ("Standard Form", "standardform.html", "sm"),
        ("Standard Units", "units.html", "xs"),
        ("Rounding and Accuracy", "rounding.html", "sm"),
        ("Limits of Accuracy", "limits.html", "xs"),
    ]),
    ("algebra", "Algebra", "xl", [
        ("Algebra Overview", "overview.html", "md"),
        ("Multiplying Brackets", "brackets.html", "sm"),
        ("Changing the Subject", "subject.html", "sm"),
        ("Equations", "equations.html", "md"),
        ("Algebraic Fractions", "algebraic_fractions.html", "xs"),
        ("Inequalities", "inequalities.html", "sm"),
        ("Algebraic Manipulation", "manipulation.html", "sm"),
        ("Identities and Proofs", "identities.html", "xs"),
        ("Simultaneous Equations", "simultaneous1.html", "md"),
        ("Simultaneous Quadratics", "simultaneous2.html", "xs"),
        ("Functions", "functions.html", "sm"),
        ("More Functions", "functions2.html", "xs"),
        ("Iterative Methods", "iterative1.html", "xs"),
        ("More Iterative Methods", "iterative2.html", "xs"),
        ("Sequences", "sequences1.html", "md"),
        ("More Sequences", "sequences2.html", "xs"),
    ]),
    ("quadratics", "Quadratics", "lg", [
        ("Quadratics Overview", "overview.html", "md"),
        ("Factorising Questions", "factors/questions.html", "sm"),
        ("Factorising Answers", "factors/answers.html", "xs"),
        ("The Quadratic Formula", "formula/index.html", "md"),
        ("Formula Cheat Sheet", "formula/cheat-sheet.html", "sm"),
        ("Formula Questions", "formula/questions.html", "xs"),
        ("Formula Answers", "formula/answers.html", "xs"),
        ("Formula Checklist", "formula/quiz.html", "xs"),
        ("Completing the Square", "completing-the-square/completing-the-square.html", "md"),
        ("Completing the Square Questions", "completing-the-square/questions.html", "xs"),
        ("Completing the Square Answers", "completing-the-square/answers.html", "xs"),
        ("Advanced Questions", "completing-the-square/questions2.html", "xs"),
        ("Advanced Answers", "completing-the-square/answers2.html", "xs"),
    ]),
    ("graphs", "Graphs", "lg", [
        ("Graphs Overview", "overview.html", "md"),
        ("Straight Line Graphs", "straight_line_graphs.html", "md"),
        ("Graphical Inequalities", "inequalities.html", "sm"),
        ("Graphs of Functions", "functions.html", "sm"),
        ("Roots and Turning Points", "quadratics.html", "sm"),
        ("Translations and Reflections", "translations.html", "sm"),
        ("Real World Graphs", "real-world.html", "xs"),
        ("Graphs of Circles", "circles.html", "sm"),
    ]),
    ("ratio", "Ratio and Proportion", "xl", [
        ("Ratio Overview", "overview.html", "md"),
        ("Units and Compound Units", "units.html", "sm"),
        ("Scale Drawings and Maps", "scale-diagrams.html", "sm"),
        ("One Quantity as a Fraction", "fraction-of-another.html", "xs"),
        ("Ratio Notation", "ratio-notation.html", "md"),
        ("Sharing in a Ratio", "sharing-in-a-ratio.html", "md"),
        ("Multiplicative Relationships", "multiplicative-relationships.html", "xs"),
        ("Proportion as Equal Ratios", "proportion-equal-ratios.html", "xs"),
        ("Ratios and Linear Functions", "ratios-fractions-linear.html", "xs"),
        ("Percentage Change", "percentages.html", "md"),
        ("Direct and Inverse Proportion", "direct-inverse-proportion.html", "sm"),
        ("Compound Measures", "compound-measures.html", "sm"),
        ("Similar Shapes", "similar-shapes.html", "sm"),
        ("Equations of Proportion", "proportion-equations.html", "xs"),
        ("Gradient as a Rate of Change", "gradient-rate-of-change.html", "sm"),
        ("Instantaneous Rates of Change", "instantaneous-rate-of-change.html", "xs"),
        ("Growth and Decay", "growth-and-decay.html", "sm"),
    ]),
    ("geometry", "Geometry and Measures", "xl", [
        ("Geometry Overview", "overview.html", "md"),
        ("Conventions and Notation", "conventions.html", "xs"),
        ("Constructions and Loci", "constructions-loci.html", "sm"),
        ("Angle Rules and Polygons", "angle-rules.html", "md"),
        ("Triangles and Quadrilaterals", "quadrilaterals-triangles.html", "sm"),
        ("Congruent Triangles", "congruent-triangles.html", "sm"),
        ("Geometric Proof", "geometric-proof.html", "xs"),
        ("Transformations", "transformations.html", "md"),
        ("Combined Transformations", "combined-transformations.html", "xs"),
        ("Parts of a Circle", "circle-parts.html", "sm"),
        ("Circle Theorems", "circle-theorems.html", "md"),
        ("Coordinate Geometry", "coordinate-geometry.html", "sm"),
        ("3D Shapes", "3d-shapes.html", "sm"),
        ("Plans and Elevations", "plans-elevations.html", "xs"),
        ("Units of Measure", "units-measures.html", "xs"),
        ("Measuring and Bearings", "measuring-bearings.html", "sm"),
        ("Area and Volume Formulae", "area-volume-formulae.html", "md"),
        ("Surface Area and Volume", "circles-surface-area.html", "sm"),
        ("Arcs and Sectors", "arcs-sectors.html", "sm"),
        ("Congruence and Similarity", "congruence-similarity.html", "xs"),
        ("Pythagoras and Trigonometry", "pythagoras-trigonometry.html", "md"),
        ("Exact Trig Values", "exact-trig-values.html", "xs"),
        ("Sine and Cosine Rules", "sine-cosine-rules.html", "sm"),
        ("Vectors and Translations", "vectors-translations.html", "sm"),
        ("Vector Arithmetic", "vector-arithmetic.html", "xs"),
        ("Vector Proof", "vector-proofs.html", "xs"),
    ]),
    ("probability", "Probability", "lg", [
        ("Probability Overview", "overview.html", "md"),
        ("Tables and Frequency Trees", "frequency-tables.html", "sm"),
        ("Expected Outcomes", "expected-outcomes.html", "sm"),
        ("The Probability Scale", "probability-scale.html", "sm"),
        ("Mutually Exclusive Events", "exhaustive-events.html", "sm"),
        ("Experimental Probability", "experimental-probability.html", "xs"),
        ("Listing and Venn Diagrams", "listing-outcomes.html", "xs"),
        ("Sample Space Diagrams", "sample-space.html", "md"),
        ("Tree Diagrams", "combined-events.html", "md"),
        ("Conditional Probability", "conditional-probability.html", "md"),
    ]),
    ("statistics", "Statistics", "lg", [
        ("Statistics Overview", "overview.html", "md"),
        ("Sampling and Populations", "sampling.html", "sm"),
        ("Charts and Diagrams", "charts-and-tables.html", "sm"),
        ("Histograms and Cumulative Frequency", "histograms-cumulative-frequency.html", "md"),
        ("Averages, Spread and Box Plots", "averages-and-spread.html", "md"),
        ("Describing a Population", "describing-populations.html", "xs"),
        ("Scatter Graphs and Correlation", "scatter-graphs.html", "md"),
    ]),
]

START = "<!-- WORDCLOUD:START -->"
END = "<!-- WORDCLOUD:END -->"


def validate():
    """Every link target must exist on disk."""
    missing = []
    for folder, _, _, subs in TOPICS:
        if not os.path.isfile(os.path.join(ROOT, "gcse", folder, "index.md")):
            missing.append(f"gcse/{folder}/index.md")
        for _, f, _ in subs:
            p = os.path.join(ROOT, "gcse", folder, f)
            if not os.path.isfile(p):
                missing.append(f"gcse/{folder}/{f}")
    return missing


def link(label, href, size):
    return f'<a class="{size}" href="{href}">{label}</a>'


def topics_cloud():
    items = [link(name, f"/gcse/{folder}/", size) for folder, name, size, _ in TOPICS]
    return '<div class="wc wc-topics">' + "".join(items) + "</div>"


def mixed_cloud():
    """All subtopics interleaved round-robin, so the cloud mixes subjects."""
    lists = [[(l, f"/gcse/{folder}/{f}", s) for l, f, s in subs]
             for folder, _, _, subs in TOPICS]
    out, i = [], 0
    while any(lists):
        for lst in lists:
            if i < len(lst):
                out.append(lst[i])
        i += 1
        if i > max(len(l) for l in lists):
            break
    return '<div class="wc">' + "".join(link(*x) for x in out) + "</div>"


def grouped_clouds():
    parts = []
    for folder, name, _, subs in TOPICS:
        parts.append(
            f'<p class="wc-label"><a href="/gcse/{folder}/">{name}</a> '
            f'&middot; {len(subs)} pages</p>'
        )
        items = "".join(link(l, f"/gcse/{folder}/{f}", s) for l, f, s in subs)
        parts.append(f'<div class="wc">{items}</div>')
    return "\n".join(parts)


def splice(path, block):
    """Replace the region between the markers, or append it if absent."""
    full = os.path.join(ROOT, path)
    with open(full, encoding="utf-8") as fh:
        text = fh.read()
    payload = f"{START}\n{block}\n{END}"
    if START in text and END in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END),
                      lambda _: payload, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + payload + "\n"
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)
    return sum(1 for _ in re.finditer(r'<a class=', payload))


if __name__ == "__main__":
    miss = validate()
    if miss:
        print("MISSING TARGETS:")
        for m in miss:
            print("  ", m)
        sys.exit(1)

    total = sum(len(s) for _, _, _, s in TOPICS)
    print(f"{len(TOPICS)} topics, {total} subtopics — all targets verified")

    home = (
        '{% include wordcloud-style.html %}\n'
        '<h2 id="explore-gcse-maths">Explore GCSE Maths</h2>\n'
        '<p>Every topic, with full notes, worked examples and practice questions '
        'with answers. Pick a topic:</p>\n'
        + topics_cloud() + "\n"
        '<p class="wc-label">&hellip;or jump straight to any of the '
        f'{total} subtopics</p>\n'
        + mixed_cloud()
    )

    gcse = (
        '{% include wordcloud-style.html %}\n'
        '<h2 id="all-topics">All topics</h2>\n'
        + topics_cloud() + "\n"
        '<h2 id="all-subtopics">Every subtopic</h2>\n'
        + grouped_clouds()
    )

    n1 = splice("index.md", home)
    n2 = splice("gcse/index.md", gcse)
    print(f"index.md      → {n1} links")
    print(f"gcse/index.md → {n2} links")
