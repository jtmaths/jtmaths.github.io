#!/usr/bin/env python3
"""Generate the word-cloud blocks for index.md, gcse/index.md and fsmq/index.md.

Single source of truth for every topic/subtopic link across both qualifications.
Validates that each target file actually exists before writing anything.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root

# (folder, Topic label, size, [(label, file, size), ...])
GCSE_TOPICS = [
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

FSMQ_TOPICS = [
    ("algebra", "Algebra", "xl", [
        ("Algebra Overview", "overview.html", "md"),
        ("Algebraic Manipulation", "manipulation.html", "sm"),
        ("Polynomials and the Factor Theorem", "polynomials.html", "md"),
        ("Completing the Square", "completing-the-square.html", "sm"),
        ("Setting Up and Solving Equations", "equations.html", "md"),
        ("Linear and Quadratic Inequalities", "inequalities.html", "sm"),
        ("Inequalities in Two Variables", "inequalities-two-variables.html", "xs"),
        ("Recurrence Relationships", "recurrence-relations.html", "sm"),
    ]),
    ("enumeration", "Enumeration", "lg", [
        ("Enumeration Overview", "overview.html", "md"),
        ("The Binomial Expansion", "binomial-expansion.html", "md"),
        ("The Product Rule for Counting", "counting-product-rule.html", "sm"),
        ("Permutations", "permutations.html", "sm"),
        ("Combinations", "combinations.html", "sm"),
        ("Representing Outcomes", "representing-outcomes.html", "xs"),
        ("Counting in Probability", "binomial-probability.html", "md"),
    ]),
    ("coordinate-geometry", "Coordinate Geometry", "lg", [
        ("Coordinate Geometry Overview", "overview.html", "md"),
        ("Straight Lines", "straight-lines.html", "md"),
        ("The Geometry of Circles", "circles.html", "md"),
        ("Sketching Curves", "curve-sketching.html", "sm"),
        ("Tangents and Normals", "tangents-and-normals.html", "sm"),
        ("Linear Programming", "linear-programming.html", "md"),
    ]),
    ("trigonometry", "Pythagoras and Trigonometry", "lg", [
        ("Trigonometry Overview", "overview.html", "md"),
        ("Ratios of Any Angle", "ratios-of-any-angle.html", "md"),
        ("The Sine and Cosine Rules", "sine-and-cosine-rules.html", "md"),
        ("Trigonometric Identities", "trigonometric-identities.html", "sm"),
        ("Trigonometric Equations", "trigonometric-equations.html", "sm"),
        ("2-D and 3-D Problems", "three-dimensional-problems.html", "sm"),
    ]),
    ("calculus", "Calculus", "xl", [
        ("Calculus Overview", "overview.html", "md"),
        ("Differentiation", "differentiation.html", "md"),
        ("Tangents and Normals by Calculus", "tangents-normals.html", "sm"),
        ("Stationary Points", "stationary-points.html", "md"),
        ("Maximum and Minimum Problems", "optimisation.html", "sm"),
        ("Integration", "integration.html", "md"),
        ("Areas Under and Between Curves", "areas.html", "sm"),
        ("Application to Kinematics", "kinematics.html", "sm"),
    ]),
    ("numerical-methods", "Numerical Methods", "lg", [
        ("Numerical Methods Overview", "overview.html", "md"),
        ("Change of Sign", "change-of-sign.html", "md"),
        ("Iterative Methods", "iterative-methods.html", "md"),
        ("Gradients from Chords", "gradient-from-chords.html", "sm"),
        ("Estimating Areas", "area-estimates.html", "sm"),
        ("Numerical Methods in Context", "applications.html", "xs"),
    ]),
    ("exponentials-logarithms", "Exponentials and Logarithms", "lg", [
        ("Exponentials and Logarithms Overview", "overview.html", "md"),
        ("Exponential Functions", "exponential-functions.html", "md"),
        ("Logarithms and Their Laws", "logarithms.html", "md"),
        ("Solving Exponential Equations", "exponential-equations.html", "sm"),
        ("Reduction to Linear Form", "reduction-to-linear-form.html", "sm"),
        ("Growth and Decay", "growth-and-decay.html", "sm"),
    ]),
]

# section key -> (url/folder prefix, topic list)
SECTIONS = {
    "gcse": ("gcse", GCSE_TOPICS),
    "fsmq": ("fsmq", FSMQ_TOPICS),
}

START = "<!-- WORDCLOUD:START -->"
END = "<!-- WORDCLOUD:END -->"


def validate():
    """Every link target must exist on disk, in every section."""
    missing = []
    for prefix, topics in SECTIONS.values():
        for folder, _, _, subs in topics:
            idx = os.path.join(ROOT, prefix, folder, "index.md")
            if not os.path.isfile(idx):
                missing.append(f"{prefix}/{folder}/index.md")
            for _, f, _ in subs:
                if not os.path.isfile(os.path.join(ROOT, prefix, folder, f)):
                    missing.append(f"{prefix}/{folder}/{f}")
    return missing


def link(label, href, size):
    return f'<a class="{size}" href="{href}">{label}</a>'


def topics_cloud(section):
    prefix, topics = SECTIONS[section]
    items = [link(name, f"/{prefix}/{folder}/", size)
             for folder, name, size, _ in topics]
    return '<div class="wc wc-topics">' + "".join(items) + "</div>"


def mixed_cloud(section):
    """All subtopics interleaved round-robin, so the cloud mixes subjects."""
    prefix, topics = SECTIONS[section]
    lists = [[(l, f"/{prefix}/{folder}/{f}", s) for l, f, s in subs]
             for folder, _, _, subs in topics]
    out, i = [], 0
    while any(lists):
        for lst in lists:
            if i < len(lst):
                out.append(lst[i])
        i += 1
        if i > max(len(l) for l in lists):
            break
    return '<div class="wc">' + "".join(link(*x) for x in out) + "</div>"


def grouped_clouds(section):
    prefix, topics = SECTIONS[section]
    parts = []
    for folder, name, _, subs in topics:
        parts.append(
            f'<p class="wc-label"><a href="/{prefix}/{folder}/">{name}</a> '
            f'&middot; {len(subs)} pages</p>'
        )
        items = "".join(link(l, f"/{prefix}/{folder}/{f}", s) for l, f, s in subs)
        parts.append(f'<div class="wc">{items}</div>')
    return "\n".join(parts)


def count(section):
    return sum(len(subs) for _, _, _, subs in SECTIONS[section][1])


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

    n_gcse, n_fsmq = count("gcse"), count("fsmq")
    for key, label in (("gcse", "GCSE"), ("fsmq", "FSMQ")):
        topics = SECTIONS[key][1]
        print(f"{label}: {len(topics)} topics, {count(key)} subtopics "
              "\u2014 all targets verified")

    home = (
        '{% include wordcloud-style.html %}\n'
        '<h2 id="explore-gcse-maths">Explore GCSE Maths</h2>\n'
        '<p>Every topic, with full notes, worked examples and practice questions '
        'with answers. Pick a topic:</p>\n'
        + topics_cloud("gcse") + "\n"
        '<p class="wc-label">&hellip;or jump straight to any of the '
        f'{n_gcse} subtopics</p>\n'
        + mixed_cloud("gcse") + "\n"
        '<h2 id="explore-fsmq-additional-maths">Explore FSMQ Additional Maths</h2>\n'
        '<p>The full OCR Level 3 FSMQ: Additional Maths (6993) course, with notes, '
        'worked examples and practice questions with answers:</p>\n'
        + topics_cloud("fsmq") + "\n"
        '<p class="wc-label">&hellip;or jump straight to any of the '
        f'{n_fsmq} FSMQ pages</p>\n'
        + mixed_cloud("fsmq")
    )

    gcse = (
        '{% include wordcloud-style.html %}\n'
        '<h2 id="all-topics">All topics</h2>\n'
        + topics_cloud("gcse") + "\n"
        '<h2 id="all-subtopics">Every subtopic</h2>\n'
        + grouped_clouds("gcse")
    )

    fsmq = (
        '{% include wordcloud-style.html %}\n'
        '<h2 id="all-topics">All topics</h2>\n'
        + topics_cloud("fsmq") + "\n"
        '<h2 id="all-pages">Every page</h2>\n'
        + grouped_clouds("fsmq")
    )

    n1 = splice("index.md", home)
    n2 = splice("gcse/index.md", gcse)
    n3 = splice("fsmq/index.md", fsmq)
    print(f"index.md      \u2192 {n1} links")
    print(f"gcse/index.md \u2192 {n2} links")
    print(f"fsmq/index.md \u2192 {n3} links")
