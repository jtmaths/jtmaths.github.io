"""GCSE practice papers — major Quadratics subtopics."""
from build import frac

FACTORISING = {
    "title": "Factorising and Solving Quadratics",
    "folder": "gcse/quadratics/factors",
    "slug": "quadratics-factorising-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Factorise <i>x</i><sup>2</sup> + 5<i>x</i></p>",
            "steps": [
                "Both terms contain <i>x</i>, so take <i>x</i> outside a bracket.",
                "<i>x</i><sup>2</sup> &divide; <i>x</i> = <i>x</i> and 5<i>x</i> &divide; <i>x</i> = 5",
            ],
            "answer": "<i>x</i>(<i>x</i> + 5)",
        },
        {
            "marks": 2,
            "q": "<p>Factorise <i>x</i><sup>2</sup> + 7<i>x</i> + 10</p>",
            "steps": [
                "Find two numbers that multiply to 10 and add to 7.",
                "2 &times; 5 = 10 and 2 + 5 = 7 &#10003;",
            ],
            "answer": "(<i>x</i> + 2)(<i>x</i> + 5)",
        },
        {
            "marks": 2,
            "q": "<p>Factorise <i>x</i><sup>2</sup> &minus; 4<i>x</i> + 3</p>",
            "steps": [
                "The number term is positive and the <i>x</i> term is negative, so both numbers are negative.",
                "&minus;1 &times; &minus;3 = 3 and &minus;1 + (&minus;3) = &minus;4 &#10003;",
            ],
            "answer": "(<i>x</i> &minus; 1)(<i>x</i> &minus; 3)",
        },
        {
            "marks": 2,
            "q": "<p>Solve (<i>x</i> &minus; 2)(<i>x</i> + 5) = 0</p>",
            "steps": [
                "If a product is zero, at least one factor must be zero.",
                "<i>x</i> &minus; 2 = 0 gives <i>x</i> = 2",
                "<i>x</i> + 5 = 0 gives <i>x</i> = &minus;5",
            ],
            "answer": "<i>x</i> = 2 &nbsp;or&nbsp; <i>x</i> = &minus;5",
        },
        {
            "marks": 3,
            "q": "<p>Factorise <i>x</i><sup>2</sup> + <i>x</i> &minus; 12</p>",
            "steps": [
                "The number term is negative, so the two numbers have different signs.",
                "Pairs multiplying to &minus;12: 1 and &minus;12, 2 and &minus;6, 3 and &minus;4, 4 and &minus;3&hellip;",
                "4 + (&minus;3) = 1 &#10003;",
                "So the brackets are (<i>x</i> + 4)(<i>x</i> &minus; 3)",
            ],
            "answer": "(<i>x</i> + 4)(<i>x</i> &minus; 3)",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 6<i>x</i> + 8 = 0</p>",
            "steps": [
                "Two numbers multiplying to 8 and adding to 6 are 2 and 4.",
                "(<i>x</i> + 2)(<i>x</i> + 4) = 0",
                "<i>x</i> = &minus;2 or <i>x</i> = &minus;4",
                "Check <i>x</i> = &minus;4: 16 &minus; 24 + 8 = 0 &#10003;",
            ],
            "answer": "<i>x</i> = &minus;2 &nbsp;or&nbsp; <i>x</i> = &minus;4",
        },
        {
            "marks": 3,
            "q": "<p>Factorise</p>"
                 "<p class='part'>(a) <i>x</i><sup>2</sup> &minus; 16</p>"
                 "<p class='part'>(b) <i>x</i><sup>2</sup> &minus; 100</p>",
            "steps": [
                "Both are a difference of two squares: a<sup>2</sup> &minus; b<sup>2</sup> = (a + b)(a &minus; b)",
                "<b>(a)</b> 16 = 4<sup>2</sup>, so <i>x</i><sup>2</sup> &minus; 16 = (<i>x</i> + 4)(<i>x</i> &minus; 4)",
                "<b>(b)</b> 100 = 10<sup>2</sup>, so <i>x</i><sup>2</sup> &minus; 100 = (<i>x</i> + 10)(<i>x</i> &minus; 10)",
            ],
            "answer": "(a) (<i>x</i> + 4)(<i>x</i> &minus; 4) &nbsp;&nbsp; (b) (<i>x</i> + 10)(<i>x</i> &minus; 10)",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> &minus; 5<i>x</i> = 0</p>",
            "steps": [
                "There is no number term, so take out the common factor <i>x</i>.",
                "<i>x</i>(<i>x</i> &minus; 5) = 0",
                "<i>x</i> = 0 or <i>x</i> &minus; 5 = 0",
                "Do not divide both sides by <i>x</i> &mdash; that would lose the solution <i>x</i> = 0.",
            ],
            "answer": "<i>x</i> = 0 &nbsp;or&nbsp; <i>x</i> = 5",
        },
        {
            "marks": 4,
            "q": "<p>A rectangle has width <i>x</i> cm and length (<i>x</i> + 2) cm. Its area is 48 cm<sup>2</sup>.</p>"
                 "<p class='part'>(a) Show that <i>x</i><sup>2</sup> + 2<i>x</i> &minus; 48 = 0</p>"
                 "<p class='part'>(b) Work out the length and width of the rectangle.</p>",
            "steps": [
                "<b>(a)</b> Area = <i>x</i>(<i>x</i> + 2) = <i>x</i><sup>2</sup> + 2<i>x</i>",
                "Setting this equal to 48 and moving 48 across gives <i>x</i><sup>2</sup> + 2<i>x</i> &minus; 48 = 0",
                "<b>(b)</b> Two numbers multiplying to &minus;48 and adding to 2 are 8 and &minus;6.",
                "(<i>x</i> + 8)(<i>x</i> &minus; 6) = 0, so <i>x</i> = &minus;8 or <i>x</i> = 6",
                "A width cannot be negative, so <i>x</i> = 6 cm and the length is 8 cm (6 &times; 8 = 48 &#10003;).",
            ],
            "answer": "(b) width 6 cm, length 8 cm",
        },
        {
            "marks": 4,
            "q": "<p>A curve has equation <i>y</i> = <i>x</i><sup>2</sup> &minus; <i>x</i> &minus; 6</p>"
                 "<p class='part'>(a) Factorise <i>x</i><sup>2</sup> &minus; <i>x</i> &minus; 6</p>"
                 "<p class='part'>(b) Write down where the curve crosses the <i>x</i>-axis.</p>"
                 "<p class='part'>(c) Write down where the curve crosses the <i>y</i>-axis.</p>"
                 "<p class='part'>(d) Write down the equation of the line of symmetry.</p>",
            "steps": [
                "<b>(a)</b> Two numbers multiplying to &minus;6 and adding to &minus;1 are &minus;3 and +2, "
                "so the answer is (<i>x</i> &minus; 3)(<i>x</i> + 2)",
                "<b>(b)</b> Set <i>y</i> = 0: <i>x</i> = 3 or <i>x</i> = &minus;2, giving (3, 0) and (&minus;2, 0)",
                "<b>(c)</b> Set <i>x</i> = 0: <i>y</i> = &minus;6, giving (0, &minus;6)",
                "<b>(d)</b> The line of symmetry runs halfway between the two roots.",
                "(3 + (&minus;2)) &divide; 2 = 0.5, so the line is <i>x</i> = 0.5",
            ],
            "answer": "(a) (<i>x</i> &minus; 3)(<i>x</i> + 2) &nbsp;&nbsp; (b) (3, 0) and (&minus;2, 0) &nbsp;&nbsp; "
                      "(c) (0, &minus;6) &nbsp;&nbsp; (d) <i>x</i> = 0.5",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Factorise 2<i>x</i><sup>2</sup> + 5<i>x</i> + 2</p>",
            "steps": [
                "Multiply the end numbers: 2 &times; 2 = 4. Two numbers multiplying to 4 and adding to 5 are 4 and 1.",
                "2<i>x</i><sup>2</sup> + 4<i>x</i> + <i>x</i> + 2 = 2<i>x</i>(<i>x</i> + 2) + 1(<i>x</i> + 2)",
            ],
            "answer": "(2<i>x</i> + 1)(<i>x</i> + 2)",
        },
        {
            "marks": 2,
            "q": "<p>Solve <i>x</i><sup>2</sup> &minus; 11<i>x</i> + 30 = 0</p>",
            "steps": [
                "Two negative numbers multiplying to 30 and adding to &minus;11 are &minus;5 and &minus;6.",
                "(<i>x</i> &minus; 5)(<i>x</i> &minus; 6) = 0",
            ],
            "answer": "<i>x</i> = 5 &nbsp;or&nbsp; <i>x</i> = 6",
        },
        {
            "marks": 3,
            "q": "<p>Solve 3<i>x</i><sup>2</sup> &minus; 12<i>x</i> = 0</p>",
            "steps": [
                "Take out the highest common factor, which is 3<i>x</i>.",
                "3<i>x</i>(<i>x</i> &minus; 4) = 0",
                "3<i>x</i> = 0 gives <i>x</i> = 0, and <i>x</i> &minus; 4 = 0 gives <i>x</i> = 4",
            ],
            "answer": "<i>x</i> = 0 &nbsp;or&nbsp; <i>x</i> = 4",
        },
        {
            "marks": 3,
            "q": "<p>Solve 4<i>x</i><sup>2</sup> &minus; 25 = 0</p>",
            "steps": [
                "This is a difference of two squares: 4<i>x</i><sup>2</sup> = (2<i>x</i>)<sup>2</sup> and 25 = 5<sup>2</sup>",
                "(2<i>x</i> + 5)(2<i>x</i> &minus; 5) = 0",
                "2<i>x</i> = &minus;5 gives <i>x</i> = &minus;2.5, and 2<i>x</i> = 5 gives <i>x</i> = 2.5",
            ],
            "answer": "<i>x</i> = 2.5 &nbsp;or&nbsp; <i>x</i> = &minus;2.5",
        },
        {
            "marks": 4,
            "q": "<p>Solve 2<i>x</i><sup>2</sup> + 7<i>x</i> &minus; 15 = 0</p>",
            "steps": [
                "Multiply the end numbers: 2 &times; (&minus;15) = &minus;30",
                "Two numbers multiplying to &minus;30 and adding to 7 are 10 and &minus;3.",
                "Split the middle term: 2<i>x</i><sup>2</sup> + 10<i>x</i> &minus; 3<i>x</i> &minus; 15 = 0",
                "Factorise in pairs: 2<i>x</i>(<i>x</i> + 5) &minus; 3(<i>x</i> + 5) = 0",
                "(2<i>x</i> &minus; 3)(<i>x</i> + 5) = 0, so <i>x</i> = 1.5 or <i>x</i> = &minus;5",
            ],
            "answer": "<i>x</i> = 1.5 &nbsp;or&nbsp; <i>x</i> = &minus;5",
        },
        {
            "marks": 4,
            "q": "<p>Solve 6<i>x</i><sup>2</sup> &minus; 11<i>x</i> + 3 = 0</p>",
            "steps": [
                "Multiply the end numbers: 6 &times; 3 = 18",
                "Two numbers multiplying to 18 and adding to &minus;11 are &minus;9 and &minus;2.",
                "6<i>x</i><sup>2</sup> &minus; 9<i>x</i> &minus; 2<i>x</i> + 3 = 0",
                "3<i>x</i>(2<i>x</i> &minus; 3) &minus; 1(2<i>x</i> &minus; 3) = 0",
                "(3<i>x</i> &minus; 1)(2<i>x</i> &minus; 3) = 0, so <i>x</i> = " + frac("1", "3") + " or <i>x</i> = " + frac("3", "2"),
            ],
            "answer": "<i>x</i> = " + frac("1", "3") + " &nbsp;or&nbsp; <i>x</i> = " + frac("3", "2"),
        },
        {
            "marks": 4,
            "q": "<p>Solve (<i>x</i> + 2)(<i>x</i> &minus; 1) = 18</p>",
            "steps": [
                "You cannot set each bracket equal to 18 &mdash; the product must equal <b>zero</b> first.",
                "Expand: <i>x</i><sup>2</sup> + <i>x</i> &minus; 2 = 18",
                "Rearrange: <i>x</i><sup>2</sup> + <i>x</i> &minus; 20 = 0",
                "Factorise: (<i>x</i> + 5)(<i>x</i> &minus; 4) = 0",
                "<i>x</i> = &minus;5 or <i>x</i> = 4. Check <i>x</i> = 4: 6 &times; 3 = 18 &#10003;",
            ],
            "answer": "<i>x</i> = 4 &nbsp;or&nbsp; <i>x</i> = &minus;5",
        },
        {
            "marks": 4,
            "q": "<p>Solve &nbsp;<i>x</i> + " + frac("20", "<i>x</i>") + " = 9</p>",
            "steps": [
                "Multiply every term by <i>x</i> to clear the fraction: <i>x</i><sup>2</sup> + 20 = 9<i>x</i>",
                "Rearrange: <i>x</i><sup>2</sup> &minus; 9<i>x</i> + 20 = 0",
                "Two numbers multiplying to 20 and adding to &minus;9 are &minus;4 and &minus;5.",
                "(<i>x</i> &minus; 4)(<i>x</i> &minus; 5) = 0",
                "Check <i>x</i> = 4: 4 + 5 = 9 &#10003;",
            ],
            "answer": "<i>x</i> = 4 &nbsp;or&nbsp; <i>x</i> = 5",
        },
        {
            "marks": 4,
            "q": "<p>Solve &nbsp;" + frac("1", "<i>x</i>") + " + " + frac("1", "<i>x</i> + 1")
                 + " = " + frac("5", "6") + "</p>",
            "steps": [
                "Multiply every term by 6<i>x</i>(<i>x</i> + 1) to clear all three fractions.",
                "6(<i>x</i> + 1) + 6<i>x</i> = 5<i>x</i>(<i>x</i> + 1)",
                "Expand: 6<i>x</i> + 6 + 6<i>x</i> = 5<i>x</i><sup>2</sup> + 5<i>x</i>",
                "Rearrange: 5<i>x</i><sup>2</sup> &minus; 7<i>x</i> &minus; 6 = 0",
                "5 &times; (&minus;6) = &minus;30; two numbers multiplying to &minus;30 and adding to &minus;7 are &minus;10 and 3.",
                "5<i>x</i>(<i>x</i> &minus; 2) + 3(<i>x</i> &minus; 2) = 0, so (5<i>x</i> + 3)(<i>x</i> &minus; 2) = 0",
            ],
            "answer": "<i>x</i> = 2 &nbsp;or&nbsp; <i>x</i> = &minus;" + frac("3", "5"),
        },
        {
            "marks": 5,
            "q": "<p>A right-angled triangle has shorter sides of length <i>x</i> cm and (<i>x</i> + 7) cm, "
                 "and hypotenuse (<i>x</i> + 8) cm.</p>"
                 "<p class='part'>(a) Show that <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 15 = 0</p>"
                 "<p class='part'>(b) Work out the lengths of all three sides.</p>",
            "steps": [
                "<b>(a)</b> By Pythagoras: <i>x</i><sup>2</sup> + (<i>x</i> + 7)<sup>2</sup> = (<i>x</i> + 8)<sup>2</sup>",
                "(<i>x</i> + 7)<sup>2</sup> = <i>x</i><sup>2</sup> + 14<i>x</i> + 49 and (<i>x</i> + 8)<sup>2</sup> = <i>x</i><sup>2</sup> + 16<i>x</i> + 64",
                "2<i>x</i><sup>2</sup> + 14<i>x</i> + 49 = <i>x</i><sup>2</sup> + 16<i>x</i> + 64",
                "Subtract everything on the right: <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 15 = 0 as required.",
                "<b>(b)</b> Factorise: (<i>x</i> &minus; 5)(<i>x</i> + 3) = 0, so <i>x</i> = 5 or <i>x</i> = &minus;3",
                "A length cannot be negative, so <i>x</i> = 5",
                "The sides are 5 cm, 12 cm and 13 cm (check: 25 + 144 = 169 &#10003;).",
            ],
            "answer": "(b) 5 cm, 12 cm and 13 cm",
        },
    ],
}

FORMULA = {
    "title": "The Quadratic Formula",
    "folder": "gcse/quadratics/formula",
    "slug": "quadratic-formula-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>For the equation 2<i>x</i><sup>2</sup> + 5<i>x</i> &minus; 3 = 0, write down the values "
                 "of a, b and c.</p>",
            "steps": [
                "Compare with the standard form a<i>x</i><sup>2</sup> + b<i>x</i> + c = 0",
                "The sign in front of each term belongs to that number.",
            ],
            "answer": "a = 2, b = 5, c = &minus;3",
        },
        {
            "marks": 2,
            "q": "<p>Work out the value of b<sup>2</sup> &minus; 4ac for <i>x</i><sup>2</sup> + 3<i>x</i> &minus; 4 = 0</p>",
            "steps": [
                "Here a = 1, b = 3 and c = &minus;4",
                "b<sup>2</sup> &minus; 4ac = 3<sup>2</sup> &minus; 4 &times; 1 &times; (&minus;4)",
                "= 9 + 16 = 25 (take care: subtracting a negative gives an addition).",
            ],
            "answer": "25",
        },
        {
            "marks": 2,
            "q": "<p>Use the quadratic formula to solve <i>x</i><sup>2</sup> + 3<i>x</i> &minus; 4 = 0</p>",
            "steps": [
                "From the previous question, b<sup>2</sup> &minus; 4ac = 25 and &radic;25 = 5",
                "<i>x</i> = " + frac("&minus;3 &plusmn; 5", "2"),
                "<i>x</i> = " + frac("2", "2") + " = 1 &nbsp;or&nbsp; <i>x</i> = " + frac("&minus;8", "2") + " = &minus;4",
            ],
            "answer": "<i>x</i> = 1 &nbsp;or&nbsp; <i>x</i> = &minus;4",
        },
        {
            "marks": 2,
            "q": "<p>Work out b<sup>2</sup> &minus; 4ac for 2<i>x</i><sup>2</sup> &minus; 4<i>x</i> + 5 = 0 and say what "
                 "this tells you about the solutions.</p>",
            "steps": [
                "a = 2, b = &minus;4, c = 5",
                "b<sup>2</sup> &minus; 4ac = (&minus;4)<sup>2</sup> &minus; 4 &times; 2 &times; 5 = 16 &minus; 40 = &minus;24",
                "You cannot take the square root of a negative number, so there are no real solutions.",
            ],
            "answer": "&minus;24 &mdash; the equation has no real solutions",
        },
        {
            "marks": 3,
            "q": "<p>Use the quadratic formula to solve <i>x</i><sup>2</sup> &minus; 6<i>x</i> + 5 = 0</p>",
            "steps": [
                "a = 1, b = &minus;6, c = 5",
                "b<sup>2</sup> &minus; 4ac = 36 &minus; 20 = 16, and &radic;16 = 4",
                "<i>x</i> = " + frac("6 &plusmn; 4", "2"),
                "<i>x</i> = " + frac("10", "2") + " = 5 &nbsp;or&nbsp; <i>x</i> = " + frac("2", "2") + " = 1",
            ],
            "answer": "<i>x</i> = 5 &nbsp;or&nbsp; <i>x</i> = 1",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 2<i>x</i> &minus; 1 = 0</p><p>Give your answers to 2 decimal places.</p>",
            "steps": [
                "a = 1, b = 2, c = &minus;1",
                "b<sup>2</sup> &minus; 4ac = 4 + 4 = 8, and &radic;8 = 2.8284&hellip;",
                "<i>x</i> = " + frac("&minus;2 &plusmn; 2.8284", "2"),
                "<i>x</i> = " + frac("0.8284", "2") + " = 0.4142&hellip; &nbsp;or&nbsp; <i>x</i> = " + frac("&minus;4.8284", "2") + " = &minus;2.4142&hellip;",
            ],
            "answer": "<i>x</i> = 0.41 &nbsp;or&nbsp; <i>x</i> = &minus;2.41 (2 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>Solve 2<i>x</i><sup>2</sup> + 5<i>x</i> + 1 = 0</p><p>Give your answers to 2 decimal places.</p>",
            "steps": [
                "a = 2, b = 5, c = 1",
                "b<sup>2</sup> &minus; 4ac = 25 &minus; 8 = 17, and &radic;17 = 4.1231&hellip;",
                "The denominator is 2a = 4",
                "<i>x</i> = " + frac("&minus;5 + 4.1231", "4") + " = &minus;0.2192&hellip; &nbsp;or&nbsp; <i>x</i> = " + frac("&minus;5 &minus; 4.1231", "4") + " = &minus;2.2808&hellip;",
            ],
            "answer": "<i>x</i> = &minus;0.22 &nbsp;or&nbsp; <i>x</i> = &minus;2.28 (2 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> &minus; 4<i>x</i> &minus; 3 = 0, giving your answers in surd form.</p>",
            "steps": [
                "a = 1, b = &minus;4, c = &minus;3",
                "b<sup>2</sup> &minus; 4ac = 16 + 12 = 28",
                "<i>x</i> = " + frac("4 &plusmn; &radic;28", "2"),
                "Simplify the surd: &radic;28 = &radic;4 &times; &radic;7 = 2&radic;7",
                "<i>x</i> = " + frac("4 &plusmn; 2&radic;7", "2") + " = 2 &plusmn; &radic;7 (divide every term by 2).",
            ],
            "answer": "<i>x</i> = 2 + &radic;7 &nbsp;or&nbsp; <i>x</i> = 2 &minus; &radic;7",
        },
        {
            "marks": 4,
            "q": "<p>Solve 3<i>x</i><sup>2</sup> &minus; 7<i>x</i> + 2 = 0</p>",
            "steps": [
                "a = 3, b = &minus;7, c = 2",
                "b<sup>2</sup> &minus; 4ac = 49 &minus; 24 = 25",
                "&radic;25 = 5, so the answers will be exact.",
                "<i>x</i> = " + frac("7 &plusmn; 5", "6"),
                "<i>x</i> = " + frac("12", "6") + " = 2 &nbsp;or&nbsp; <i>x</i> = " + frac("2", "6") + " = " + frac("1", "3"),
            ],
            "answer": "<i>x</i> = 2 &nbsp;or&nbsp; <i>x</i> = " + frac("1", "3"),
        },
        {
            "marks": 4,
            "q": "<p>A ball is thrown upwards. Its height, h metres, after t seconds is given by "
                 "h = 20t &minus; 5t<sup>2</sup></p>"
                 "<p class='part'>(a) Find the two times when the ball is 15 m above the ground.</p>"
                 "<p class='part'>(b) Explain why there are two answers.</p>",
            "steps": [
                "<b>(a)</b> Set h = 15: 20t &minus; 5t<sup>2</sup> = 15",
                "Rearrange: 5t<sup>2</sup> &minus; 20t + 15 = 0, and divide by 5: t<sup>2</sup> &minus; 4t + 3 = 0",
                "b<sup>2</sup> &minus; 4ac = 16 &minus; 12 = 4, and &radic;4 = 2",
                "t = " + frac("4 &plusmn; 2", "2") + ", so t = 3 or t = 1",
                "<b>(b)</b> The ball passes 15 m on the way up (after 1 second) and again on the way down "
                "(after 3 seconds).",
            ],
            "answer": "(a) t = 1 s and t = 3 s &nbsp;&nbsp; (b) once going up and once coming down",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 5<i>x</i> + 2 = 0, giving your answers to 2 decimal places.</p>",
            "steps": [
                "a = 1, b = 5, c = 2, so b<sup>2</sup> &minus; 4ac = 25 &minus; 8 = 17",
                "&radic;17 = 4.1231&hellip;",
                "<i>x</i> = " + frac("&minus;5 &plusmn; 4.1231", "2") + ", giving &minus;0.4384&hellip; and &minus;4.5616&hellip;",
            ],
            "answer": "<i>x</i> = &minus;0.44 &nbsp;or&nbsp; <i>x</i> = &minus;4.56 (2 d.p.)",
        },
        {
            "marks": 2,
            "q": "<p>Solve 2<i>x</i><sup>2</sup> &minus; 3<i>x</i> &minus; 4 = 0, giving your answers to 2 decimal places.</p>",
            "steps": [
                "a = 2, b = &minus;3, c = &minus;4, so b<sup>2</sup> &minus; 4ac = 9 + 32 = 41",
                "&radic;41 = 6.4031&hellip; and 2a = 4",
                "<i>x</i> = " + frac("3 &plusmn; 6.4031", "4") + ", giving 2.3508&hellip; and &minus;0.8508&hellip;",
            ],
            "answer": "<i>x</i> = 2.35 &nbsp;or&nbsp; <i>x</i> = &minus;0.85 (2 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>Solve 5<i>x</i><sup>2</sup> + 2<i>x</i> &minus; 2 = 0, giving your answers in surd form "
                 "as simply as possible.</p>",
            "steps": [
                "a = 5, b = 2, c = &minus;2",
                "b<sup>2</sup> &minus; 4ac = 4 + 40 = 44",
                "&radic;44 = &radic;4 &times; &radic;11 = 2&radic;11",
                "<i>x</i> = " + frac("&minus;2 &plusmn; 2&radic;11", "10"),
                "Divide every term by 2: <i>x</i> = " + frac("&minus;1 &plusmn; &radic;11", "5"),
            ],
            "answer": "<i>x</i> = " + frac("&minus;1 + &radic;11", "5") + " &nbsp;or&nbsp; " + frac("&minus;1 &minus; &radic;11", "5"),
        },
        {
            "marks": 3,
            "q": "<p>Solve 3<i>x</i><sup>2</sup> &minus; 6<i>x</i> + 1 = 0, giving your answers in surd form "
                 "as simply as possible.</p>",
            "steps": [
                "a = 3, b = &minus;6, c = 1",
                "b<sup>2</sup> &minus; 4ac = 36 &minus; 12 = 24, and &radic;24 = 2&radic;6",
                "<i>x</i> = " + frac("6 &plusmn; 2&radic;6", "6"),
                "Divide every term by 2: <i>x</i> = " + frac("3 &plusmn; &radic;6", "3"),
            ],
            "answer": "<i>x</i> = " + frac("3 + &radic;6", "3") + " &nbsp;or&nbsp; " + frac("3 &minus; &radic;6", "3"),
        },
        {
            "marks": 4,
            "q": "<p>Use the discriminant to state how many real solutions each equation has.</p>"
                 "<p class='part'>(a) <i>x</i><sup>2</sup> &minus; 6<i>x</i> + 9 = 0</p>"
                 "<p class='part'>(b) 2<i>x</i><sup>2</sup> + <i>x</i> + 3 = 0</p>"
                 "<p class='part'>(c) <i>x</i><sup>2</sup> + 4<i>x</i> &minus; 1 = 0</p>",
            "steps": [
                "The discriminant is b<sup>2</sup> &minus; 4ac: positive means two roots, zero means one repeated "
                "root, negative means none.",
                "<b>(a)</b> 36 &minus; 36 = 0, so there is exactly one (repeated) solution.",
                "<b>(b)</b> 1 &minus; 24 = &minus;23, which is negative, so there are no real solutions.",
                "<b>(c)</b> 16 + 4 = 20, which is positive, so there are two distinct real solutions.",
            ],
            "answer": "(a) one repeated root &nbsp;&nbsp; (b) none &nbsp;&nbsp; (c) two",
        },
        {
            "marks": 4,
            "q": "<p>The equation <i>x</i><sup>2</sup> + k<i>x</i> + 16 = 0 has two equal roots.</p>"
                 "<p>Find the possible values of k.</p>",
            "steps": [
                "Two equal roots means the discriminant is zero.",
                "a = 1, b = k, c = 16, so k<sup>2</sup> &minus; 4 &times; 1 &times; 16 = 0",
                "k<sup>2</sup> &minus; 64 = 0, so k<sup>2</sup> = 64",
                "k = 8 or k = &minus;8 &mdash; remember the negative root.",
                "Check k = &minus;8: <i>x</i><sup>2</sup> &minus; 8<i>x</i> + 16 = (<i>x</i> &minus; 4)<sup>2</sup> &#10003;",
            ],
            "answer": "k = 8 &nbsp;or&nbsp; k = &minus;8",
        },
        {
            "marks": 4,
            "q": "<p>The equation <i>x</i><sup>2</sup> + 6<i>x</i> + k = 0 has two different real solutions.</p>"
                 "<p>Find the range of possible values of k.</p>",
            "steps": [
                "Two different real solutions means the discriminant is strictly positive.",
                "a = 1, b = 6, c = k",
                "b<sup>2</sup> &minus; 4ac = 36 &minus; 4k &gt; 0",
                "36 &gt; 4k, so 9 &gt; k",
                "That is, k &lt; 9 (if k = 9 the roots would be equal).",
            ],
            "answer": "k &lt; 9",
        },
        {
            "marks": 4,
            "q": "<p>Solve (2<i>x</i> &minus; 1)(<i>x</i> + 3) = 5</p><p>Give your answers to 2 decimal places.</p>",
            "steps": [
                "Expand the left-hand side: 2<i>x</i><sup>2</sup> + 6<i>x</i> &minus; <i>x</i> &minus; 3 = 2<i>x</i><sup>2</sup> + 5<i>x</i> &minus; 3",
                "Set equal to 5 and rearrange: 2<i>x</i><sup>2</sup> + 5<i>x</i> &minus; 8 = 0",
                "a = 2, b = 5, c = &minus;8, so b<sup>2</sup> &minus; 4ac = 25 + 64 = 89",
                "&radic;89 = 9.4340&hellip; and 2a = 4",
                "<i>x</i> = " + frac("&minus;5 &plusmn; 9.4340", "4") + ", giving 1.1085&hellip; and &minus;3.6085&hellip;",
            ],
            "answer": "<i>x</i> = 1.11 &nbsp;or&nbsp; <i>x</i> = &minus;3.61 (2 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>A rectangle has width <i>x</i> cm and length (<i>x</i> + 3) cm.</p>"
                 "<p>Its area is 15 cm<sup>2</sup>.</p>"
                 "<p>Work out the width of the rectangle, correct to 2 decimal places.</p>",
            "steps": [
                "Area: <i>x</i>(<i>x</i> + 3) = 15, so <i>x</i><sup>2</sup> + 3<i>x</i> &minus; 15 = 0",
                "a = 1, b = 3, c = &minus;15, so b<sup>2</sup> &minus; 4ac = 9 + 60 = 69",
                "&radic;69 = 8.3066&hellip;",
                "<i>x</i> = " + frac("&minus;3 &plusmn; 8.3066", "2") + ", giving 2.6533&hellip; or &minus;5.6533&hellip;",
                "A width must be positive, so reject the negative answer.",
            ],
            "answer": "2.65 cm (2 d.p.)",
        },
        {
            "marks": 5,
            "q": "<p>A stone is thrown from the top of a wall. Its height, h metres above the ground, "
                 "t seconds later is given by</p>"
                 "<p>&nbsp;&nbsp;h = 1.5 + 12t &minus; 5t<sup>2</sup></p>"
                 "<p class='part'>(a) Write down the height of the wall.</p>"
                 "<p class='part'>(b) Find the time when the stone hits the ground, to 2 decimal places.</p>",
            "steps": [
                "<b>(a)</b> The stone leaves the wall at t = 0, when h = 1.5, so the wall is 1.5 m high.",
                "<b>(b)</b> The stone hits the ground when h = 0: 1.5 + 12t &minus; 5t<sup>2</sup> = 0",
                "Multiply by &minus;1 and reorder: 5t<sup>2</sup> &minus; 12t &minus; 1.5 = 0",
                "a = 5, b = &minus;12, c = &minus;1.5, so b<sup>2</sup> &minus; 4ac = 144 + 30 = 174",
                "&radic;174 = 13.1909&hellip; and 2a = 10",
                "t = " + frac("12 &plusmn; 13.1909", "10") + ", giving 2.5191&hellip; or &minus;0.1191&hellip;",
                "Time cannot be negative, so t = 2.52 seconds.",
            ],
            "answer": "(a) 1.5 m &nbsp;&nbsp; (b) 2.52 seconds (2 d.p.)",
        },
    ],
}

COMPLETING = {
    "title": "Completing the Square",
    "folder": "gcse/quadratics/completing-the-square",
    "slug": "completing-the-square-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>What number must be put in the box to make <i>x</i><sup>2</sup> + 6<i>x</i> + &#9633; "
                 "a perfect square?</p>",
            "steps": [
                "Halve the coefficient of <i>x</i>: 6 &divide; 2 = 3",
                "Square it: 3<sup>2</sup> = 9, and indeed <i>x</i><sup>2</sup> + 6<i>x</i> + 9 = (<i>x</i> + 3)<sup>2</sup>",
            ],
            "answer": "9",
        },
        {
            "marks": 2,
            "q": "<p>Write <i>x</i><sup>2</sup> + 4<i>x</i> + 1 in the form (<i>x</i> + a)<sup>2</sup> + b</p>",
            "steps": [
                "Half of 4 is 2, so start with (<i>x</i> + 2)<sup>2</sup>",
                "(<i>x</i> + 2)<sup>2</sup> = <i>x</i><sup>2</sup> + 4<i>x</i> + 4, which is 4 too big.",
                "So <i>x</i><sup>2</sup> + 4<i>x</i> + 1 = (<i>x</i> + 2)<sup>2</sup> &minus; 4 + 1",
            ],
            "answer": "(<i>x</i> + 2)<sup>2</sup> &minus; 3",
        },
        {
            "marks": 2,
            "q": "<p>Write <i>x</i><sup>2</sup> &minus; 6<i>x</i> + 10 in the form (<i>x</i> + a)<sup>2</sup> + b</p>",
            "steps": [
                "Half of &minus;6 is &minus;3, so start with (<i>x</i> &minus; 3)<sup>2</sup> = <i>x</i><sup>2</sup> &minus; 6<i>x</i> + 9",
                "That is 9 too big, so subtract 9 and add the original 10.",
                "(<i>x</i> &minus; 3)<sup>2</sup> &minus; 9 + 10 = (<i>x</i> &minus; 3)<sup>2</sup> + 1",
            ],
            "answer": "(<i>x</i> &minus; 3)<sup>2</sup> + 1",
        },
        {
            "marks": 2,
            "q": "<p>Write <i>x</i><sup>2</sup> + 10<i>x</i> in the form (<i>x</i> + a)<sup>2</sup> + b</p>",
            "steps": [
                "Half of 10 is 5, so start with (<i>x</i> + 5)<sup>2</sup> = <i>x</i><sup>2</sup> + 10<i>x</i> + 25",
                "There is no number term in the original, so subtract the whole 25.",
            ],
            "answer": "(<i>x</i> + 5)<sup>2</sup> &minus; 25",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Write <i>x</i><sup>2</sup> &minus; 8<i>x</i> + 20 in the form "
                 "(<i>x</i> + a)<sup>2</sup> + b</p>"
                 "<p class='part'>(b) Write down the smallest possible value of "
                 "<i>x</i><sup>2</sup> &minus; 8<i>x</i> + 20 and the value of <i>x</i> that gives it.</p>",
            "steps": [
                "<b>(a)</b> Half of &minus;8 is &minus;4, so (<i>x</i> &minus; 4)<sup>2</sup> = <i>x</i><sup>2</sup> &minus; 8<i>x</i> + 16",
                "(<i>x</i> &minus; 4)<sup>2</sup> &minus; 16 + 20 = (<i>x</i> &minus; 4)<sup>2</sup> + 4",
                "<b>(b)</b> A square is never negative, so the smallest (<i>x</i> &minus; 4)<sup>2</sup> can be is 0.",
                "That happens when <i>x</i> = 4, giving a smallest value of 4.",
            ],
            "answer": "(a) (<i>x</i> &minus; 4)<sup>2</sup> + 4 &nbsp;&nbsp; (b) smallest value 4, when <i>x</i> = 4",
        },
        {
            "marks": 3,
            "q": "<p>Write <i>x</i><sup>2</sup> + 3<i>x</i> + 1 in the form (<i>x</i> + a)<sup>2</sup> + b</p>",
            "steps": [
                "Half of 3 is 1.5, so start with (<i>x</i> + 1.5)<sup>2</sup>",
                "(<i>x</i> + 1.5)<sup>2</sup> = <i>x</i><sup>2</sup> + 3<i>x</i> + 2.25",
                "Subtract the extra 2.25 and add the original 1: &minus;2.25 + 1 = &minus;1.25",
            ],
            "answer": "(<i>x</i> + 1.5)<sup>2</sup> &minus; 1.25",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 6<i>x</i> + 5 = 0 by completing the square.</p>",
            "steps": [
                "Half of 6 is 3, so <i>x</i><sup>2</sup> + 6<i>x</i> + 5 = (<i>x</i> + 3)<sup>2</sup> &minus; 9 + 5 = (<i>x</i> + 3)<sup>2</sup> &minus; 4",
                "So (<i>x</i> + 3)<sup>2</sup> &minus; 4 = 0, giving (<i>x</i> + 3)<sup>2</sup> = 4",
                "Take the square root of both sides, remembering both signs: <i>x</i> + 3 = &plusmn;2",
                "<i>x</i> = &minus;3 + 2 = &minus;1 or <i>x</i> = &minus;3 &minus; 2 = &minus;5",
            ],
            "answer": "<i>x</i> = &minus;1 &nbsp;or&nbsp; <i>x</i> = &minus;5",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> &minus; 4<i>x</i> &minus; 1 = 0 by completing the square, "
                 "giving your answers in surd form.</p>",
            "steps": [
                "Half of &minus;4 is &minus;2, so the expression is (<i>x</i> &minus; 2)<sup>2</sup> &minus; 4 &minus; 1 = (<i>x</i> &minus; 2)<sup>2</sup> &minus; 5",
                "(<i>x</i> &minus; 2)<sup>2</sup> = 5",
                "<i>x</i> &minus; 2 = &plusmn;&radic;5",
                "<i>x</i> = 2 &plusmn; &radic;5",
            ],
            "answer": "<i>x</i> = 2 + &radic;5 &nbsp;or&nbsp; <i>x</i> = 2 &minus; &radic;5",
        },
        {
            "marks": 4,
            "q": "<p>A curve has equation <i>y</i> = <i>x</i><sup>2</sup> + 8<i>x</i> + 3</p>"
                 "<p class='part'>(a) Write the equation in the form <i>y</i> = (<i>x</i> + a)<sup>2</sup> + b</p>"
                 "<p class='part'>(b) Write down the coordinates of the minimum point.</p>"
                 "<p class='part'>(c) Write down the equation of the line of symmetry.</p>",
            "steps": [
                "<b>(a)</b> Half of 8 is 4: (<i>x</i> + 4)<sup>2</sup> = <i>x</i><sup>2</sup> + 8<i>x</i> + 16",
                "<i>y</i> = (<i>x</i> + 4)<sup>2</sup> &minus; 16 + 3 = (<i>x</i> + 4)<sup>2</sup> &minus; 13",
                "<b>(b)</b> The bracket is smallest (zero) when <i>x</i> = &minus;4, and then <i>y</i> = &minus;13",
                "The minimum point is (&minus;4, &minus;13).",
                "<b>(c)</b> The line of symmetry passes through the minimum: <i>x</i> = &minus;4",
            ],
            "answer": "(a) (<i>x</i> + 4)<sup>2</sup> &minus; 13 &nbsp;&nbsp; (b) (&minus;4, &minus;13) &nbsp;&nbsp; (c) <i>x</i> = &minus;4",
        },
        {
            "marks": 4,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 5<i>x</i> + 3 = 0 by completing the square.</p>"
                 "<p>Give your answers to 2 decimal places.</p>",
            "steps": [
                "Half of 5 is 2.5, so (<i>x</i> + 2.5)<sup>2</sup> = <i>x</i><sup>2</sup> + 5<i>x</i> + 6.25",
                "<i>x</i><sup>2</sup> + 5<i>x</i> + 3 = (<i>x</i> + 2.5)<sup>2</sup> &minus; 6.25 + 3 = (<i>x</i> + 2.5)<sup>2</sup> &minus; 3.25",
                "(<i>x</i> + 2.5)<sup>2</sup> = 3.25",
                "<i>x</i> + 2.5 = &plusmn;&radic;3.25 = &plusmn;1.80277&hellip;",
                "<i>x</i> = &minus;2.5 + 1.8028 = &minus;0.6972&hellip; or <i>x</i> = &minus;2.5 &minus; 1.8028 = &minus;4.3028&hellip;",
            ],
            "answer": "<i>x</i> = &minus;0.70 &nbsp;or&nbsp; <i>x</i> = &minus;4.30 (2 d.p.)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Write <i>x</i><sup>2</sup> &minus; 12<i>x</i> + 40 in the form (<i>x</i> + a)<sup>2</sup> + b</p>",
            "steps": [
                "Half of &minus;12 is &minus;6, so (<i>x</i> &minus; 6)<sup>2</sup> = <i>x</i><sup>2</sup> &minus; 12<i>x</i> + 36",
                "&minus;36 + 40 = 4",
            ],
            "answer": "(<i>x</i> &minus; 6)<sup>2</sup> + 4",
        },
        {
            "marks": 2,
            "q": "<p>Write down the coordinates of the minimum point of "
                 "<i>y</i> = (<i>x</i> &minus; 3)<sup>2</sup> + 7</p>",
            "steps": [
                "The squared bracket is smallest when it equals 0, which happens at <i>x</i> = 3",
                "Then <i>y</i> = 0 + 7 = 7",
            ],
            "answer": "(3, 7)",
        },
        {
            "marks": 3,
            "q": "<p>Write 2<i>x</i><sup>2</sup> + 8<i>x</i> + 5 in the form a(<i>x</i> + b)<sup>2</sup> + c</p>",
            "steps": [
                "Take the 2 out of the <i>x</i> terms only: 2(<i>x</i><sup>2</sup> + 4<i>x</i>) + 5",
                "Complete the square inside: <i>x</i><sup>2</sup> + 4<i>x</i> = (<i>x</i> + 2)<sup>2</sup> &minus; 4",
                "2[(<i>x</i> + 2)<sup>2</sup> &minus; 4] + 5 = 2(<i>x</i> + 2)<sup>2</sup> &minus; 8 + 5",
            ],
            "answer": "2(<i>x</i> + 2)<sup>2</sup> &minus; 3",
        },
        {
            "marks": 3,
            "q": "<p>Write 3<i>x</i><sup>2</sup> &minus; 12<i>x</i> + 7 in the form a(<i>x</i> + b)<sup>2</sup> + c</p>",
            "steps": [
                "Take out 3 from the first two terms: 3(<i>x</i><sup>2</sup> &minus; 4<i>x</i>) + 7",
                "<i>x</i><sup>2</sup> &minus; 4<i>x</i> = (<i>x</i> &minus; 2)<sup>2</sup> &minus; 4",
                "3[(<i>x</i> &minus; 2)<sup>2</sup> &minus; 4] + 7 = 3(<i>x</i> &minus; 2)<sup>2</sup> &minus; 12 + 7",
            ],
            "answer": "3(<i>x</i> &minus; 2)<sup>2</sup> &minus; 5",
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) Write 5 + 4<i>x</i> &minus; <i>x</i><sup>2</sup> in the form "
                 "a &minus; (<i>x</i> + b)<sup>2</sup></p>"
                 "<p class='part'>(b) Hence write down the maximum value of the expression and the value of "
                 "<i>x</i> at which it occurs.</p>",
            "steps": [
                "<b>(a)</b> Reorder and factor out &minus;1 from the <i>x</i> terms: &minus;(<i>x</i><sup>2</sup> &minus; 4<i>x</i>) + 5",
                "Complete the square inside: <i>x</i><sup>2</sup> &minus; 4<i>x</i> = (<i>x</i> &minus; 2)<sup>2</sup> &minus; 4",
                "&minus;[(<i>x</i> &minus; 2)<sup>2</sup> &minus; 4] + 5 = &minus;(<i>x</i> &minus; 2)<sup>2</sup> + 4 + 5 = 9 &minus; (<i>x</i> &minus; 2)<sup>2</sup>",
                "<b>(b)</b> We are now <b>subtracting</b> a square, so the expression is largest when the square is 0.",
                "That is when <i>x</i> = 2, giving a maximum value of 9.",
            ],
            "answer": "(a) 9 &minus; (<i>x</i> &minus; 2)<sup>2</sup> &nbsp;&nbsp; (b) maximum 9 at <i>x</i> = 2",
        },
        {
            "marks": 4,
            "q": "<p>Solve 2<i>x</i><sup>2</sup> &minus; 8<i>x</i> + 3 = 0 by completing the square.</p>"
                 "<p>Give your answers in surd form.</p>",
            "steps": [
                "Take out 2: 2(<i>x</i><sup>2</sup> &minus; 4<i>x</i>) + 3",
                "<i>x</i><sup>2</sup> &minus; 4<i>x</i> = (<i>x</i> &minus; 2)<sup>2</sup> &minus; 4, so the expression is 2(<i>x</i> &minus; 2)<sup>2</sup> &minus; 8 + 3 = 2(<i>x</i> &minus; 2)<sup>2</sup> &minus; 5",
                "Set to zero: 2(<i>x</i> &minus; 2)<sup>2</sup> = 5, so (<i>x</i> &minus; 2)<sup>2</sup> = " + frac("5", "2"),
                "<i>x</i> &minus; 2 = &plusmn;&radic;(" + frac("5", "2") + ") = &plusmn;" + frac("&radic;10", "2"),
                "<i>x</i> = 2 &plusmn; " + frac("&radic;10", "2"),
            ],
            "answer": "<i>x</i> = 2 + " + frac("&radic;10", "2") + " &nbsp;or&nbsp; <i>x</i> = 2 &minus; " + frac("&radic;10", "2"),
        },
        {
            "marks": 4,
            "q": "<p>A curve has equation <i>y</i> = <i>x</i><sup>2</sup> &minus; 6<i>x</i> + 11</p>"
                 "<p class='part'>(a) Complete the square.</p>"
                 "<p class='part'>(b) Write down the turning point.</p>"
                 "<p class='part'>(c) Explain why the equation "
                 "<i>x</i><sup>2</sup> &minus; 6<i>x</i> + 11 = 0 has no real solutions.</p>",
            "steps": [
                "<b>(a)</b> Half of &minus;6 is &minus;3: (<i>x</i> &minus; 3)<sup>2</sup> &minus; 9 + 11 = (<i>x</i> &minus; 3)<sup>2</sup> + 2",
                "<b>(b)</b> The smallest value of the bracket is 0 at <i>x</i> = 3, giving <i>y</i> = 2",
                "The turning point is a minimum at (3, 2).",
                "<b>(c)</b> Setting <i>y</i> = 0 gives (<i>x</i> &minus; 3)<sup>2</sup> = &minus;2",
                "A square can never be negative, so no real value of <i>x</i> works &mdash; the curve stays "
                "entirely above the <i>x</i>-axis.",
            ],
            "answer": "(a) (<i>x</i> &minus; 3)<sup>2</sup> + 2 &nbsp;&nbsp; (b) (3, 2) &nbsp;&nbsp; "
                      "(c) it would need (<i>x</i> &minus; 3)<sup>2</sup> = &minus;2, which is impossible",
        },
        {
            "marks": 4,
            "q": "<p>The graph of <i>y</i> = <i>x</i><sup>2</sup> is translated to give the graph of "
                 "<i>y</i> = (<i>x</i> + 3)<sup>2</sup> &minus; 5</p>"
                 "<p class='part'>(a) Describe fully the transformation.</p>"
                 "<p class='part'>(b) Write down the turning point of the new graph.</p>"
                 "<p class='part'>(c) Write down the equation of the line of symmetry.</p>",
            "steps": [
                "<b>(a)</b> The +3 is inside the bracket, so it moves the graph horizontally &mdash; and in the "
                "<b>opposite</b> direction to the sign, i.e. 3 to the left.",
                "The &minus;5 is outside, so it moves the graph 5 down.",
                "The transformation is a translation by the vector 3 left and 5 down.",
                "<b>(b)</b> The vertex of <i>y</i> = <i>x</i><sup>2</sup> at (0, 0) moves to (&minus;3, &minus;5).",
                "<b>(c)</b> The line of symmetry passes through the vertex: <i>x</i> = &minus;3",
            ],
            "answer": "(a) translation 3 left and 5 down &nbsp;&nbsp; (b) (&minus;3, &minus;5) &nbsp;&nbsp; "
                      "(c) <i>x</i> = &minus;3",
        },
        {
            "marks": 4,
            "q": "<p>Find the maximum value of 7 + 6<i>x</i> &minus; <i>x</i><sup>2</sup> and the value of "
                 "<i>x</i> at which it occurs.</p>",
            "steps": [
                "Factor out &minus;1 from the <i>x</i> terms: &minus;(<i>x</i><sup>2</sup> &minus; 6<i>x</i>) + 7",
                "Complete the square inside: <i>x</i><sup>2</sup> &minus; 6<i>x</i> = (<i>x</i> &minus; 3)<sup>2</sup> &minus; 9",
                "&minus;[(<i>x</i> &minus; 3)<sup>2</sup> &minus; 9] + 7 = &minus;(<i>x</i> &minus; 3)<sup>2</sup> + 9 + 7",
                "= 16 &minus; (<i>x</i> &minus; 3)<sup>2</sup>",
                "The square is smallest (zero) when <i>x</i> = 3, so the maximum value is 16.",
            ],
            "answer": "maximum 16, when <i>x</i> = 3",
        },
        {
            "marks": 5,
            "q": "<p class='part'>(a) Prove that <i>x</i><sup>2</sup> + 6<i>x</i> + 11 is positive for every "
                 "value of <i>x</i>.</p>"
                 "<p class='part'>(b) Find the least possible value of 2<i>x</i><sup>2</sup> &minus; 12<i>x</i> + 23 "
                 "and the value of <i>x</i> that gives it.</p>",
            "steps": [
                "<b>(a)</b> Complete the square: half of 6 is 3, so (<i>x</i> + 3)<sup>2</sup> = <i>x</i><sup>2</sup> + 6<i>x</i> + 9",
                "<i>x</i><sup>2</sup> + 6<i>x</i> + 11 = (<i>x</i> + 3)<sup>2</sup> + 2",
                "A square is never negative, so (<i>x</i> + 3)<sup>2</sup> &ge; 0 and the whole expression is at "
                "least 2, which is positive for every <i>x</i>.",
                "<b>(b)</b> Take out 2: 2(<i>x</i><sup>2</sup> &minus; 6<i>x</i>) + 23",
                "<i>x</i><sup>2</sup> &minus; 6<i>x</i> = (<i>x</i> &minus; 3)<sup>2</sup> &minus; 9, so the expression is 2(<i>x</i> &minus; 3)<sup>2</sup> &minus; 18 + 23 = 2(<i>x</i> &minus; 3)<sup>2</sup> + 5",
                "The least value is 5, when <i>x</i> = 3.",
            ],
            "answer": "(a) it equals (<i>x</i> + 3)<sup>2</sup> + 2 &ge; 2 &nbsp;&nbsp; (b) least value 5, at <i>x</i> = 3",
        },
    ],
}

PAPERS = [FACTORISING, FORMULA, COMPLETING]
