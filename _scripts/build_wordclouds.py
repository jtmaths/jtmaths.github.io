#!/usr/bin/env python3
"""Generate the word-cloud blocks for index.md and each section's index.md.

Single source of truth for every topic/subtopic link across every qualification.
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

ALEVEL1_TOPICS = [
    ("proof", "Proof", "lg", [
        ("Proof Overview", "overview.html", "md"),
        ("Proof by Deduction and Exhaustion", "deduction-exhaustion.html", "md"),
        ("Disproof by Counter-example", "counter-examples.html", "sm"),
    ]),
    ("algebra", "Algebra and Functions", "xl", [
        ("Algebra Overview", "overview.html", "md"),
        ("Indices and Surds", "indices-surds.html", "md"),
        ("Quadratic Functions", "quadratics.html", "md"),
        ("Simultaneous Equations", "simultaneous-equations.html", "sm"),
        ("Linear and Quadratic Inequalities", "inequalities.html", "sm"),
        ("Polynomials and the Factor Theorem", "polynomials.html", "md"),
        ("Curve Sketching and Proportion", "curve-sketching.html", "sm"),
        ("Transformations of Graphs", "transformations.html", "sm"),
        ("The Binomial Expansion", "binomial-expansion.html", "md"),
    ]),
    ("coordinate-geometry", "Coordinate Geometry", "lg", [
        ("Coordinate Geometry Overview", "overview.html", "md"),
        ("Straight Lines", "straight-lines.html", "md"),
        ("Circles", "circles.html", "md"),
    ]),
    ("trigonometry", "Trigonometry", "lg", [
        ("Trigonometry Overview", "overview.html", "md"),
        ("Sine and Cosine Rules", "sine-cosine-rules.html", "md"),
        ("Trigonometric Graphs", "trig-graphs.html", "sm"),
        ("Trigonometric Identities", "identities.html", "sm"),
        ("Trigonometric Equations", "equations.html", "md"),
    ]),
    ("exponentials-logarithms", "Exponentials and Logarithms", "lg", [
        ("Exponentials and Logarithms Overview", "overview.html", "md"),
        ("Exponential Functions and e", "exponential-functions.html", "md"),
        ("Logarithms and Their Laws", "logarithms.html", "md"),
        ("Exponential and Log Equations", "equations.html", "sm"),
        ("Exponential Modelling", "modelling.html", "sm"),
    ]),
    ("differentiation", "Differentiation", "xl", [
        ("Differentiation Overview", "overview.html", "md"),
        ("Differentiation from First Principles", "first-principles.html", "sm"),
        ("Differentiating Powers of x", "rules.html", "md"),
        ("Tangents and Normals", "tangents-normals.html", "sm"),
        ("Stationary Points and Optimisation", "stationary-points.html", "md"),
    ]),
    ("integration", "Integration", "lg", [
        ("Integration Overview", "overview.html", "md"),
        ("Indefinite Integration", "indefinite-integration.html", "md"),
        ("Definite Integrals and Areas", "definite-integrals.html", "md"),
    ]),
    ("vectors", "Vectors", "lg", [
        ("Vectors Overview", "overview.html", "md"),
        ("Vectors in Two Dimensions", "vectors-2d.html", "md"),
        ("Vector Geometry", "vector-geometry.html", "sm"),
    ]),
    ("statistics", "Statistics", "xl", [
        ("Statistics Overview", "overview.html", "md"),
        ("Statistical Sampling", "sampling.html", "md"),
        ("Presenting Data", "data-presentation.html", "sm"),
        ("Measures of Location and Spread", "measures.html", "md"),
        ("Correlation and Outliers", "bivariate-data.html", "sm"),
    ]),
    ("probability", "Probability and Distributions", "lg", [
        ("Probability Overview", "overview.html", "md"),
        ("Probability and Venn Diagrams", "probability.html", "md"),
        ("The Binomial Distribution", "binomial-distribution.html", "md"),
    ]),
    ("hypothesis-testing", "Hypothesis Testing", "lg", [
        ("Hypothesis Testing Overview", "overview.html", "md"),
        ("The Language of Hypothesis Testing", "language.html", "sm"),
        ("Binomial Hypothesis Tests", "binomial-tests.html", "md"),
    ]),
    ("mechanics", "Mechanics", "xl", [
        ("Mechanics Overview", "overview.html", "md"),
        ("Quantities, Units and Modelling", "units-modelling.html", "xs"),
        ("Motion Graphs", "kinematics-graphs.html", "sm"),
        ("Constant Acceleration (suvat)", "suvat.html", "md"),
        ("Variable Acceleration", "variable-acceleration.html", "sm"),
        ("Forces and Newton's Laws", "forces-newtons-laws.html", "md"),
    ]),
]

ALEVEL2_TOPICS = [
    ("proof", "Proof", "lg", [
        ("Proof Overview", "overview.html", "md"),
        ("Proof by Contradiction", "contradiction.html", "md"),
    ]),
    ("algebra", "Algebra and Functions", "xl", [
        ("Algebra Overview", "overview.html", "md"),
        ("Algebraic and Partial Fractions", "partial-fractions.html", "md"),
        ("The Modulus Function", "modulus.html", "sm"),
        ("Composite and Inverse Functions", "functions.html", "md"),
        ("Combined Transformations", "transformations.html", "sm"),
    ]),
    ("parametric-equations", "Parametric Equations", "lg", [
        ("Parametric Equations Overview", "overview.html", "md"),
        ("Parametric and Cartesian Forms", "parametric-equations.html", "md"),
        ("Parametric Modelling", "modelling.html", "sm"),
    ]),
    ("sequences-series", "Sequences and Series", "xl", [
        ("Sequences and Series Overview", "overview.html", "md"),
        ("Sequences and Sigma Notation", "sequences.html", "sm"),
        ("Arithmetic Sequences and Series", "arithmetic.html", "md"),
        ("Geometric Sequences and Series", "geometric.html", "md"),
        ("The General Binomial Expansion", "binomial-expansion.html", "sm"),
    ]),
    ("trigonometry", "Trigonometry", "xl", [
        ("Trigonometry Overview", "overview.html", "md"),
        ("Radians, Arcs and Sectors", "radians.html", "md"),
        ("Small Angle Approximations", "small-angles.html", "xs"),
        ("Reciprocal and Inverse Functions", "reciprocal-inverse.html", "sm"),
        ("Compound and Double Angles", "compound-angles.html", "md"),
        ("The R cos(x + a) Form", "harmonic-form.html", "sm"),
        ("Trigonometric Proof and Modelling", "proof-modelling.html", "xs"),
    ]),
    ("differentiation", "Differentiation", "xl", [
        ("Differentiation Overview", "overview.html", "md"),
        ("Exponentials, Logs and Trig", "standard-derivatives.html", "md"),
        ("Chain, Product and Quotient Rules", "chain-product-quotient.html", "md"),
        ("Implicit and Parametric Differentiation", "implicit-parametric.html", "sm"),
        ("Concavity and Points of Inflection", "concavity.html", "sm"),
        ("Connected Rates of Change", "connected-rates.html", "sm"),
    ]),
    ("integration", "Integration", "xl", [
        ("Integration Overview", "overview.html", "md"),
        ("Standard Integrals", "standard-integrals.html", "md"),
        ("Integration by Substitution", "substitution.html", "md"),
        ("Integration by Parts", "by-parts.html", "md"),
        ("Integrating with Partial Fractions", "partial-fractions.html", "sm"),
        ("Areas and Integration as a Limit", "areas.html", "sm"),
        ("Differential Equations", "differential-equations.html", "md"),
    ]),
    ("numerical-methods", "Numerical Methods", "lg", [
        ("Numerical Methods Overview", "overview.html", "md"),
        ("Locating Roots", "locating-roots.html", "sm"),
        ("Iteration", "iteration.html", "md"),
        ("The Newton-Raphson Method", "newton-raphson.html", "md"),
        ("The Trapezium Rule", "trapezium-rule.html", "sm"),
    ]),
    ("vectors", "Vectors", "lg", [
        ("Vectors Overview", "overview.html", "md"),
        ("Vectors in Three Dimensions", "vectors-3d.html", "md"),
    ]),
    ("statistics", "Statistics", "xl", [
        ("Statistics Overview", "overview.html", "md"),
        ("Regression and Exponential Models", "regression.html", "sm"),
        ("Conditional Probability", "conditional-probability.html", "md"),
        ("The Normal Distribution", "normal-distribution.html", "md"),
        ("Choosing a Distribution", "choosing-distributions.html", "sm"),
    ]),
    ("hypothesis-testing", "Hypothesis Testing", "lg", [
        ("Hypothesis Testing Overview", "overview.html", "md"),
        ("Testing for Correlation", "correlation-tests.html", "sm"),
        ("Testing a Normal Mean", "normal-mean-tests.html", "md"),
    ]),
    ("mechanics", "Mechanics", "xl", [
        ("Mechanics Overview", "overview.html", "md"),
        ("Moments", "moments.html", "md"),
        ("Resolving Forces and Inclined Planes", "resolving-forces.html", "md"),
        ("Friction", "friction.html", "sm"),
        ("Projectiles", "projectiles.html", "md"),
        ("Kinematics with Calculus and Vectors", "kinematics-vectors.html", "sm"),
    ]),
]

# section key -> (url/folder prefix, topic list)
SECTIONS = {
    "gcse": ("gcse", GCSE_TOPICS),
    "fsmq": ("fsmq", FSMQ_TOPICS),
    "alevel1": ("alevel-year1", ALEVEL1_TOPICS),
    "alevel2": ("alevel-year2", ALEVEL2_TOPICS),
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
    n_al1, n_al2 = count("alevel1"), count("alevel2")
    for key, label in (("gcse", "GCSE"), ("fsmq", "FSMQ"),
                       ("alevel1", "A Level Year 1"), ("alevel2", "A Level Year 2")):
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
        + mixed_cloud("fsmq") + "\n"
        '<h2 id="explore-a-level-maths-year-1">Explore A Level Maths Year 1</h2>\n'
        '<p>The first year of A Level Mathematics &mdash; pure, statistics and '
        'mechanics &mdash; with notes, worked examples and practice questions '
        'with answers:</p>\n'
        + topics_cloud("alevel1") + "\n"
        '<p class="wc-label">&hellip;or jump straight to any of the '
        f'{n_al1} Year 1 pages</p>\n'
        + mixed_cloud("alevel1") + "\n"
        '<h2 id="explore-a-level-maths-year-2">Explore A Level Maths Year 2</h2>\n'
        '<p>The second year of A Level Mathematics, completing the full course:</p>\n'
        + topics_cloud("alevel2") + "\n"
        '<p class="wc-label">&hellip;or jump straight to any of the '
        f'{n_al2} Year 2 pages</p>\n'
        + mixed_cloud("alevel2")
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

    alevel1, alevel2 = (
        '{% include wordcloud-style.html %}\n'
        '<h2 id="all-topics">All topics</h2>\n'
        + topics_cloud(key) + "\n"
        '<h2 id="all-pages">Every page</h2>\n'
        + grouped_clouds(key)
        for key in ("alevel1", "alevel2")
    )

    for path, block in (("index.md", home), ("gcse/index.md", gcse),
                        ("fsmq/index.md", fsmq),
                        ("alevel-year1/index.md", alevel1),
                        ("alevel-year2/index.md", alevel2)):
        print(f"{path:21} \u2192 {splice(path, block)} links")
