"""GCSE practice paper — Quadratics (topic level)."""
from build import frac

PAPER = {
    "title": "Quadratics",
    "folder": "gcse/quadratics",
    "slug": "quadratics-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Expand <i>x</i>(<i>x</i> + 4)</p>",
            "steps": [
                "Multiply each term inside the bracket by <i>x</i>.",
                "<i>x</i> &times; <i>x</i> = <i>x</i><sup>2</sup> and <i>x</i> &times; 4 = 4<i>x</i>",
            ],
            "answer": "<i>x</i><sup>2</sup> + 4<i>x</i>",
        },
        {
            "marks": 2,
            "q": "<p>Expand and simplify (<i>x</i> + 2)(<i>x</i> + 5)</p>",
            "steps": [
                "Multiply every term in the first bracket by every term in the second.",
                "<i>x</i> &times; <i>x</i> = <i>x</i><sup>2</sup>, &nbsp; <i>x</i> &times; 5 = 5<i>x</i>, &nbsp; 2 &times; <i>x</i> = 2<i>x</i>, &nbsp; 2 &times; 5 = 10",
                "Collect the two middle terms: 5<i>x</i> + 2<i>x</i> = 7<i>x</i>",
            ],
            "answer": "<i>x</i><sup>2</sup> + 7<i>x</i> + 10",
        },
        {
            "marks": 2,
            "q": "<p>Factorise <i>x</i><sup>2</sup> + 6<i>x</i> + 8</p>",
            "steps": [
                "Look for two numbers that <b>multiply</b> to 8 and <b>add</b> to 6.",
                "Pairs multiplying to 8: 1 and 8 (sum 9), 2 and 4 (sum 6) &#10003;",
                "So the brackets are (<i>x</i> + 2)(<i>x</i> + 4)",
            ],
            "answer": "(<i>x</i> + 2)(<i>x</i> + 4)",
        },
        {
            "marks": 2,
            "q": "<p>Solve (<i>x</i> &minus; 3)(<i>x</i> + 7) = 0</p>",
            "steps": [
                "If two things multiply to give 0, at least one of them must be 0.",
                "Either <i>x</i> &minus; 3 = 0, which gives <i>x</i> = 3",
                "Or <i>x</i> + 7 = 0, which gives <i>x</i> = &minus;7",
            ],
            "answer": "<i>x</i> = 3 &nbsp;or&nbsp; <i>x</i> = &minus;7",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 5<i>x</i> + 6 = 0</p>",
            "steps": [
                "Factorise first. Two numbers multiplying to 6 and adding to 5 are 2 and 3.",
                "(<i>x</i> + 2)(<i>x</i> + 3) = 0",
                "Set each bracket to zero: <i>x</i> + 2 = 0 gives <i>x</i> = &minus;2",
                "<i>x</i> + 3 = 0 gives <i>x</i> = &minus;3",
                "Check: (&minus;2)<sup>2</sup> + 5(&minus;2) + 6 = 4 &minus; 10 + 6 = 0 &#10003;",
            ],
            "answer": "<i>x</i> = &minus;2 &nbsp;or&nbsp; <i>x</i> = &minus;3",
        },
        {
            "marks": 3,
            "q": "<p>Factorise</p>"
                 "<p class='part'>(a) <i>x</i><sup>2</sup> &minus; 25</p>"
                 "<p class='part'>(b) <i>x</i><sup>2</sup> &minus; 3<i>x</i> &minus; 10</p>",
            "steps": [
                "<b>(a)</b> There is no <i>x</i> term and 25 = 5<sup>2</sup>, so this is the difference of two squares.",
                "<i>x</i><sup>2</sup> &minus; 25 = (<i>x</i> + 5)(<i>x</i> &minus; 5)",
                "<b>(b)</b> Two numbers multiplying to &minus;10 and adding to &minus;3. The signs must be different.",
                "&minus;5 &times; 2 = &minus;10 and &minus;5 + 2 = &minus;3 &#10003;",
                "So <i>x</i><sup>2</sup> &minus; 3<i>x</i> &minus; 10 = (<i>x</i> &minus; 5)(<i>x</i> + 2)",
            ],
            "answer": "(a) (<i>x</i> + 5)(<i>x</i> &minus; 5) &nbsp;&nbsp; (b) (<i>x</i> &minus; 5)(<i>x</i> + 2)",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> &minus; 7<i>x</i> + 12 = 0</p>",
            "steps": [
                "Two numbers multiplying to +12 and adding to &minus;7 must both be negative.",
                "&minus;3 &times; &minus;4 = 12 and &minus;3 + (&minus;4) = &minus;7 &#10003;",
                "(<i>x</i> &minus; 3)(<i>x</i> &minus; 4) = 0",
                "So <i>x</i> = 3 or <i>x</i> = 4",
            ],
            "answer": "<i>x</i> = 3 &nbsp;or&nbsp; <i>x</i> = 4",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> = 9<i>x</i></p>",
            "steps": [
                "Do <b>not</b> divide both sides by <i>x</i> &mdash; that would throw away one of the solutions.",
                "Move everything to one side: <i>x</i><sup>2</sup> &minus; 9<i>x</i> = 0",
                "Both terms have a common factor of <i>x</i>: <i>x</i>(<i>x</i> &minus; 9) = 0",
                "So <i>x</i> = 0 or <i>x</i> &minus; 9 = 0, giving <i>x</i> = 9",
                "Check: 0<sup>2</sup> = 9 &times; 0 &#10003; and 9<sup>2</sup> = 81 = 9 &times; 9 &#10003;",
            ],
            "answer": "<i>x</i> = 0 &nbsp;or&nbsp; <i>x</i> = 9",
        },
        {
            "marks": 4,
            "q": "<p>A rectangle has width <i>x</i> cm and length (<i>x</i> + 5) cm.</p>"
                 "<p>The area of the rectangle is 36 cm<sup>2</sup>.</p>"
                 "<p class='part'>(a) Show that <i>x</i><sup>2</sup> + 5<i>x</i> &minus; 36 = 0</p>"
                 "<p class='part'>(b) Work out the length and width of the rectangle.</p>",
            "steps": [
                "<b>(a)</b> Area = width &times; length = <i>x</i>(<i>x</i> + 5) = <i>x</i><sup>2</sup> + 5<i>x</i>",
                "This equals 36, so <i>x</i><sup>2</sup> + 5<i>x</i> = 36, and moving 36 across gives <i>x</i><sup>2</sup> + 5<i>x</i> &minus; 36 = 0",
                "<b>(b)</b> Two numbers multiplying to &minus;36 and adding to 5 are 9 and &minus;4.",
                "(<i>x</i> + 9)(<i>x</i> &minus; 4) = 0, so <i>x</i> = &minus;9 or <i>x</i> = 4",
                "A width cannot be negative, so reject <i>x</i> = &minus;9 and take <i>x</i> = 4",
                "Width = 4 cm, length = 4 + 5 = 9 cm (check: 4 &times; 9 = 36 &#10003;)",
            ],
            "answer": "(b) width 4 cm, length 9 cm",
        },
        {
            "marks": 4,
            "q": "<p>A curve has equation <i>y</i> = <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 8</p>"
                 "<p class='part'>(a) Factorise <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 8</p>"
                 "<p class='part'>(b) Write down the coordinates of the points where the curve crosses the <i>x</i>-axis.</p>"
                 "<p class='part'>(c) Write down the coordinates of the point where the curve crosses the <i>y</i>-axis.</p>",
            "steps": [
                "<b>(a)</b> Two numbers multiplying to &minus;8 and adding to &minus;2 are &minus;4 and +2.",
                "So <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 8 = (<i>x</i> &minus; 4)(<i>x</i> + 2)",
                "<b>(b)</b> The curve crosses the <i>x</i>-axis where <i>y</i> = 0, so solve (<i>x</i> &minus; 4)(<i>x</i> + 2) = 0",
                "<i>x</i> = 4 or <i>x</i> = &minus;2, giving the points (4, 0) and (&minus;2, 0)",
                "<b>(c)</b> The curve crosses the <i>y</i>-axis where <i>x</i> = 0.",
                "<i>y</i> = 0<sup>2</sup> &minus; 2(0) &minus; 8 = &minus;8, giving (0, &minus;8)",
            ],
            "answer": "(a) (<i>x</i> &minus; 4)(<i>x</i> + 2) &nbsp;&nbsp; (b) (4, 0) and (&minus;2, 0) &nbsp;&nbsp; (c) (0, &minus;8)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 3<i>x</i> &minus; 28 = 0</p>",
            "steps": [
                "Two numbers multiplying to &minus;28 and adding to +3 are +7 and &minus;4.",
                "(<i>x</i> + 7)(<i>x</i> &minus; 4) = 0",
                "So <i>x</i> = &minus;7 or <i>x</i> = 4",
            ],
            "answer": "<i>x</i> = &minus;7 &nbsp;or&nbsp; <i>x</i> = 4",
        },
        {
            "marks": 2,
            "q": "<p>Write <i>x</i><sup>2</sup> + 8<i>x</i> + 3 in the form (<i>x</i> + a)<sup>2</sup> + b</p>",
            "steps": [
                "Halve the coefficient of <i>x</i>: 8 &divide; 2 = 4, so start with (<i>x</i> + 4)<sup>2</sup>",
                "(<i>x</i> + 4)<sup>2</sup> = <i>x</i><sup>2</sup> + 8<i>x</i> + 16, which is 16 too big, so subtract 16.",
                "<i>x</i><sup>2</sup> + 8<i>x</i> + 3 = (<i>x</i> + 4)<sup>2</sup> &minus; 16 + 3 = (<i>x</i> + 4)<sup>2</sup> &minus; 13",
            ],
            "answer": "(<i>x</i> + 4)<sup>2</sup> &minus; 13",
        },
        {
            "marks": 3,
            "q": "<p>Solve 2<i>x</i><sup>2</sup> &minus; 5<i>x</i> &minus; 3 = 0</p>",
            "steps": [
                "Multiply the outer numbers: 2 &times; (&minus;3) = &minus;6. Find two numbers multiplying to &minus;6 and adding to &minus;5: that is &minus;6 and +1.",
                "Split the middle term: 2<i>x</i><sup>2</sup> &minus; 6<i>x</i> + <i>x</i> &minus; 3 = 0",
                "Factorise in pairs: 2<i>x</i>(<i>x</i> &minus; 3) + 1(<i>x</i> &minus; 3) = 0",
                "So (2<i>x</i> + 1)(<i>x</i> &minus; 3) = 0",
                "2<i>x</i> + 1 = 0 gives <i>x</i> = &minus;" + frac("1", "2") + ", and <i>x</i> &minus; 3 = 0 gives <i>x</i> = 3",
            ],
            "answer": "<i>x</i> = &minus;" + frac("1", "2") + " &nbsp;or&nbsp; <i>x</i> = 3",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 4<i>x</i> &minus; 6 = 0</p>"
                 "<p>Give your answers correct to 2 decimal places.</p>",
            "steps": [
                "This does not factorise, so use the quadratic formula <i>x</i> = "
                + frac("&minus;b &plusmn; &radic;(b<sup>2</sup> &minus; 4ac)", "2a"),
                "Here a = 1, b = 4, c = &minus;6",
                "b<sup>2</sup> &minus; 4ac = 4<sup>2</sup> &minus; 4 &times; 1 &times; (&minus;6) = 16 + 24 = 40",
                "<i>x</i> = " + frac("&minus;4 &plusmn; &radic;40", "2") + " &nbsp;and &radic;40 = 6.3245&hellip;",
                "<i>x</i> = " + frac("&minus;4 + 6.3245", "2") + " = 1.1622&hellip; or <i>x</i> = " + frac("&minus;4 &minus; 6.3245", "2") + " = &minus;5.1622&hellip;",
                "Rounding each to 2 decimal places gives 1.16 and &minus;5.16",
            ],
            "answer": "<i>x</i> = 1.16 &nbsp;or&nbsp; <i>x</i> = &minus;5.16 (2 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>Write 2<i>x</i><sup>2</sup> &minus; 12<i>x</i> + 5 in the form a(<i>x</i> + b)<sup>2</sup> + c</p>",
            "steps": [
                "Take the 2 out of the first two terms only: 2(<i>x</i><sup>2</sup> &minus; 6<i>x</i>) + 5",
                "Complete the square inside the bracket: <i>x</i><sup>2</sup> &minus; 6<i>x</i> = (<i>x</i> &minus; 3)<sup>2</sup> &minus; 9",
                "Substitute back: 2[(<i>x</i> &minus; 3)<sup>2</sup> &minus; 9] + 5",
                "Multiply the 2 through the square bracket: 2(<i>x</i> &minus; 3)<sup>2</sup> &minus; 18 + 5",
                "Simplify the numbers: 2(<i>x</i> &minus; 3)<sup>2</sup> &minus; 13",
            ],
            "answer": "2(<i>x</i> &minus; 3)<sup>2</sup> &minus; 13",
        },
        {
            "marks": 4,
            "q": "<p>The equation <i>x</i><sup>2</sup> + k<i>x</i> + 9 = 0 has exactly one solution.</p>"
                 "<p>Work out the possible values of k.</p>",
            "steps": [
                "A quadratic has exactly one (repeated) solution when the discriminant b<sup>2</sup> &minus; 4ac = 0",
                "Here a = 1, b = k and c = 9",
                "So k<sup>2</sup> &minus; 4 &times; 1 &times; 9 = 0, which gives k<sup>2</sup> &minus; 36 = 0",
                "k<sup>2</sup> = 36, so k = 6 or k = &minus;6 (remember the negative root).",
                "Check k = 6: <i>x</i><sup>2</sup> + 6<i>x</i> + 9 = (<i>x</i> + 3)<sup>2</sup>, a repeated root at <i>x</i> = &minus;3 &#10003;",
            ],
            "answer": "k = 6 &nbsp;or&nbsp; k = &minus;6",
        },
        {
            "marks": 4,
            "q": "<p>Solve &nbsp;<i>x</i> + " + frac("6", "<i>x</i>") + " = 5</p>",
            "steps": [
                "Clear the fraction by multiplying every term by <i>x</i>.",
                "<i>x</i> &times; <i>x</i> + " + frac("6", "<i>x</i>") + " &times; <i>x</i> = 5 &times; <i>x</i>, giving <i>x</i><sup>2</sup> + 6 = 5<i>x</i>",
                "Rearrange into the standard form: <i>x</i><sup>2</sup> &minus; 5<i>x</i> + 6 = 0",
                "Two numbers multiplying to 6 and adding to &minus;5 are &minus;2 and &minus;3.",
                "(<i>x</i> &minus; 2)(<i>x</i> &minus; 3) = 0, so <i>x</i> = 2 or <i>x</i> = 3",
                "Check <i>x</i> = 2: 2 + 6 &divide; 2 = 2 + 3 = 5 &#10003;",
            ],
            "answer": "<i>x</i> = 2 &nbsp;or&nbsp; <i>x</i> = 3",
        },
        {
            "marks": 4,
            "q": "<p>A curve has equation <i>y</i> = <i>x</i><sup>2</sup> &minus; 6<i>x</i> + 11</p>"
                 "<p class='part'>(a) Write the equation in the form (<i>x</i> + a)<sup>2</sup> + b</p>"
                 "<p class='part'>(b) Write down the coordinates of the turning point of the curve.</p>"
                 "<p class='part'>(c) Explain how you know the curve never crosses the <i>x</i>-axis.</p>",
            "steps": [
                "<b>(a)</b> Half of &minus;6 is &minus;3, so start with (<i>x</i> &minus; 3)<sup>2</sup> = <i>x</i><sup>2</sup> &minus; 6<i>x</i> + 9",
                "That is 9 too big, so <i>y</i> = (<i>x</i> &minus; 3)<sup>2</sup> &minus; 9 + 11 = (<i>x</i> &minus; 3)<sup>2</sup> + 2",
                "<b>(b)</b> (<i>x</i> &minus; 3)<sup>2</sup> is smallest when it equals 0, i.e. when <i>x</i> = 3, and then <i>y</i> = 2",
                "The turning point is a minimum at (3, 2).",
                "<b>(c)</b> A square is never negative, so (<i>x</i> &minus; 3)<sup>2</sup> + 2 is always at least 2.",
                "Since <i>y</i> can never be 0, the curve never reaches the <i>x</i>-axis.",
            ],
            "answer": "(a) (<i>x</i> &minus; 3)<sup>2</sup> + 2 &nbsp;&nbsp; (b) minimum at (3, 2) &nbsp;&nbsp; (c) the smallest value of <i>y</i> is 2, which is above the axis",
        },
        {
            "marks": 4,
            "q": "<p>Solve the simultaneous equations</p>"
                 "<p class='part'><i>y</i> = <i>x</i><sup>2</sup> &minus; 3<i>x</i> + 4</p>"
                 "<p class='part'><i>y</i> = 2<i>x</i> &minus; 2</p>",
            "steps": [
                "Both expressions equal <i>y</i>, so set them equal to each other.",
                "<i>x</i><sup>2</sup> &minus; 3<i>x</i> + 4 = 2<i>x</i> &minus; 2",
                "Move everything to one side: <i>x</i><sup>2</sup> &minus; 5<i>x</i> + 6 = 0",
                "Factorise: (<i>x</i> &minus; 2)(<i>x</i> &minus; 3) = 0, so <i>x</i> = 2 or <i>x</i> = 3",
                "Substitute into the simpler (linear) equation. When <i>x</i> = 2, <i>y</i> = 2(2) &minus; 2 = 2",
                "When <i>x</i> = 3, <i>y</i> = 2(3) &minus; 2 = 4",
            ],
            "answer": "<i>x</i> = 2, <i>y</i> = 2 &nbsp;and&nbsp; <i>x</i> = 3, <i>y</i> = 4",
        },
        {
            "marks": 5,
            "q": "<p>A rectangular lawn measures 12 m by 8 m.</p>"
                 "<p>A path of constant width <i>x</i> metres is laid all the way around the outside of the lawn.</p>"
                 "<p>The total area of the lawn and the path together is 192 m<sup>2</sup>.</p>"
                 "<p class='part'>(a) Show that <i>x</i><sup>2</sup> + 10<i>x</i> &minus; 24 = 0</p>"
                 "<p class='part'>(b) Work out the width of the path.</p>",
            "steps": [
                "<b>(a)</b> The path adds <i>x</i> to each side, so the outer rectangle is (12 + 2<i>x</i>) m by (8 + 2<i>x</i>) m.",
                "Total area = (12 + 2<i>x</i>)(8 + 2<i>x</i>) = 96 + 24<i>x</i> + 16<i>x</i> + 4<i>x</i><sup>2</sup> = 4<i>x</i><sup>2</sup> + 40<i>x</i> + 96",
                "Set this equal to 192: 4<i>x</i><sup>2</sup> + 40<i>x</i> + 96 = 192, so 4<i>x</i><sup>2</sup> + 40<i>x</i> &minus; 96 = 0",
                "Divide every term by 4: <i>x</i><sup>2</sup> + 10<i>x</i> &minus; 24 = 0 as required.",
                "<b>(b)</b> Two numbers multiplying to &minus;24 and adding to 10 are 12 and &minus;2, so (<i>x</i> + 12)(<i>x</i> &minus; 2) = 0",
                "<i>x</i> = &minus;12 or <i>x</i> = 2. A width cannot be negative, so <i>x</i> = 2",
                "Check: 16 &times; 12 = 192 m<sup>2</sup> &#10003;",
            ],
            "answer": "(b) the path is 2 m wide",
        },
    ],
}
