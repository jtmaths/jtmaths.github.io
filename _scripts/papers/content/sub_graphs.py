"""GCSE practice papers — major Graphs subtopics."""
from build import frac

CONVERSION_GRAPH = """
<svg width="340" height="205" viewBox="0 0 340 205" xmlns="http://www.w3.org/2000/svg"
     font-family="Arial, Helvetica, sans-serif" font-size="9">
  <g stroke="#e3e7ef" stroke-width="1">
    <line x1="71"  y1="20" x2="71"  y2="170"/><line x1="123" y1="20" x2="123" y2="170"/>
    <line x1="175" y1="20" x2="175" y2="170"/><line x1="227" y1="20" x2="227" y2="170"/>
    <line x1="279" y1="20" x2="279" y2="170"/>
    <line x1="45" y1="151.25" x2="305" y2="151.25"/><line x1="45" y1="113.75" x2="305" y2="113.75"/>
    <line x1="45" y1="76.25"  x2="305" y2="76.25"/> <line x1="45" y1="38.75"  x2="305" y2="38.75"/>
  </g>
  <g stroke="#c3cad8" stroke-width="1">
    <line x1="97"  y1="20" x2="97"  y2="170"/><line x1="149" y1="20" x2="149" y2="170"/>
    <line x1="201" y1="20" x2="201" y2="170"/><line x1="253" y1="20" x2="253" y2="170"/>
    <line x1="305" y1="20" x2="305" y2="170"/>
    <line x1="45" y1="132.5" x2="305" y2="132.5"/><line x1="45" y1="95" x2="305" y2="95"/>
    <line x1="45" y1="57.5"  x2="305" y2="57.5"/> <line x1="45" y1="20" x2="305" y2="20"/>
  </g>
  <g stroke="#333" stroke-width="1.4">
    <line x1="45" y1="170" x2="315" y2="170"/><line x1="45" y1="170" x2="45" y2="16"/>
  </g>
  <line x1="45" y1="170" x2="305" y2="20" stroke="#4f46e5" stroke-width="2.2"/>
  <g fill="#333" text-anchor="middle">
    <text x="45" y="183">0</text><text x="97" y="183">10</text><text x="149" y="183">20</text>
    <text x="201" y="183">30</text><text x="253" y="183">40</text><text x="305" y="183">50</text>
    <text x="180" y="198" font-size="9.5">Distance (miles)</text>
  </g>
  <g fill="#333" text-anchor="end">
    <text x="39" y="173">0</text><text x="39" y="135.5">20</text><text x="39" y="98">40</text>
    <text x="39" y="60.5">60</text><text x="39" y="23">80</text>
  </g>
  <text x="14" y="95" fill="#333" font-size="9.5" text-anchor="middle"
        transform="rotate(-90 14 95)">Distance (km)</text>
</svg>
"""

STRAIGHT_LINE = {
    "title": "Straight Line Graphs",
    "folder": "gcse/graphs",
    "slug": "straight-line-graphs-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write down the gradient of the line <i>y</i> = 5<i>x</i> + 2</p>",
            "steps": [
                "In <i>y</i> = m<i>x</i> + c, the gradient is m &mdash; the number in front of <i>x</i>.",
                "Here that number is 5, and the +2 is the <i>y</i>-intercept, not the gradient.",
            ],
            "answer": "5",
        },
        {
            "marks": 2,
            "q": "<p>A line has equation <i>y</i> = &minus;3<i>x</i> + 7</p>"
                 "<p class='part'>(a) Write down the gradient.</p>"
                 "<p class='part'>(b) Write down the coordinates of the <i>y</i>-intercept.</p>",
            "steps": [
                "<b>(a)</b> The gradient is &minus;3, so the line slopes downwards.",
                "<b>(b)</b> c = 7, and the <i>y</i>-intercept always has <i>x</i> = 0, giving (0, 7)",
            ],
            "answer": "(a) &minus;3 &nbsp;&nbsp; (b) (0, 7)",
        },
        {
            "marks": 2,
            "q": "<p>Complete the table of values for <i>y</i> = <i>x</i> + 3</p>"
                 "<table class='d'><tr><th><i>x</i></th><td>&minus;2</td><td>0</td><td>2</td></tr>"
                 "<tr><th><i>y</i></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>",
            "steps": [
                "<i>x</i> = &minus;2: <i>y</i> = &minus;2 + 3 = 1",
                "<i>x</i> = 0: <i>y</i> = 0 + 3 = 3",
                "<i>x</i> = 2: <i>y</i> = 2 + 3 = 5",
            ],
            "answer": "1, 3, 5",
        },
        {
            "marks": 2,
            "q": "<p>Which of these lines is parallel to <i>y</i> = 4<i>x</i> &minus; 1?</p>"
                 "<p><b>A:</b> <i>y</i> = 4<i>x</i> + 3 &nbsp;&nbsp;&nbsp; <b>B:</b> <i>y</i> = &minus;4<i>x</i> + 1 "
                 "&nbsp;&nbsp;&nbsp; <b>C:</b> <i>y</i> = <i>x</i> + 4</p>"
                 "<p>Give a reason for your answer.</p>",
            "steps": [
                "Parallel lines have the same gradient.",
                "The gradient of <i>y</i> = 4<i>x</i> &minus; 1 is 4.",
                "A has gradient 4, B has gradient &minus;4 and C has gradient 1.",
            ],
            "answer": "A &mdash; it has the same gradient of 4",
        },
        {
            "marks": 3,
            "q": "<p>Work out the gradient of the line joining (2, 3) and (6, 11).</p>",
            "steps": [
                "Gradient = " + frac("change in <i>y</i>", "change in <i>x</i>"),
                "Change in <i>y</i> = 11 &minus; 3 = 8",
                "Change in <i>x</i> = 6 &minus; 2 = 4",
                "Gradient = 8 &divide; 4 = 2",
            ],
            "answer": "2",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Find the equation of the line with gradient 3 that passes through (0, &minus;2).</p>"
                 "<p class='part'>(b) Show that the point (4, 10) lies on this line.</p>",
            "steps": [
                "<b>(a)</b> Use <i>y</i> = m<i>x</i> + c with m = 3.",
                "The point (0, &minus;2) lies on the <i>y</i>-axis, so c = &minus;2, giving <i>y</i> = 3<i>x</i> &minus; 2",
                "<b>(b)</b> Substitute <i>x</i> = 4: <i>y</i> = 3 &times; 4 &minus; 2 = 10",
                "This matches the <i>y</i>-coordinate, so the point is on the line.",
            ],
            "answer": "(a) <i>y</i> = 3<i>x</i> &minus; 2 &nbsp;&nbsp; (b) 3(4) &minus; 2 = 10 &#10003;",
        },
        {
            "marks": 3,
            "q": "<p>The line 2<i>x</i> + <i>y</i> = 8 crosses the <i>x</i>-axis at A and the <i>y</i>-axis at B.</p>"
                 "<p>Write down the coordinates of A and B.</p>",
            "steps": [
                "On the <i>x</i>-axis, <i>y</i> = 0: 2<i>x</i> = 8, so <i>x</i> = 4 and A is (4, 0)",
                "On the <i>y</i>-axis, <i>x</i> = 0: <i>y</i> = 8, so B is (0, 8)",
                "A quick sketch confirms the line slopes downwards from (0, 8) to (4, 0).",
            ],
            "answer": "A(4, 0) and B(0, 8)",
        },
        {
            "marks": 3,
            "q": "<p>Rearrange 3<i>y</i> = 6<i>x</i> &minus; 9 into the form <i>y</i> = m<i>x</i> + c.</p>"
                 "<p>Write down the gradient and the <i>y</i>-intercept.</p>",
            "steps": [
                "Divide every term by 3.",
                "3<i>y</i> &divide; 3 = <i>y</i>, &nbsp; 6<i>x</i> &divide; 3 = 2<i>x</i>, &nbsp; 9 &divide; 3 = 3",
                "<i>y</i> = 2<i>x</i> &minus; 3",
                "So the gradient is 2 and the <i>y</i>-intercept is (0, &minus;3).",
            ],
            "answer": "<i>y</i> = 2<i>x</i> &minus; 3; gradient 2, <i>y</i>-intercept (0, &minus;3)",
        },
        {
            "marks": 4,
            "q": "<p>A straight line passes through (1, 4) and (3, 10).</p>"
                 "<p>Find the equation of the line.</p>",
            "steps": [
                "Gradient = " + frac("10 &minus; 4", "3 &minus; 1") + " = " + frac("6", "2") + " = 3",
                "So the line is <i>y</i> = 3<i>x</i> + c",
                "Substitute (1, 4): 4 = 3 &times; 1 + c",
                "c = 1",
                "The equation is <i>y</i> = 3<i>x</i> + 1 (check with (3, 10): 9 + 1 = 10 &#10003;).",
            ],
            "answer": "<i>y</i> = 3<i>x</i> + 1",
        },
        {
            "marks": 4,
            "q": "<p>A is the point (&minus;1, 2) and B is the point (5, 10).</p>"
                 "<p class='part'>(a) Write down the coordinates of the midpoint of AB.</p>"
                 "<p class='part'>(b) Work out the gradient of AB.</p>"
                 "<p class='part'>(c) Work out the length of AB.</p>",
            "steps": [
                "<b>(a)</b> Average the coordinates: <i>x</i> = (&minus;1 + 5) &divide; 2 = 2 and <i>y</i> = (2 + 10) &divide; 2 = 6",
                "The midpoint is (2, 6).",
                "<b>(b)</b> Gradient = " + frac("10 &minus; 2", "5 &minus; (&minus;1)") + " = " + frac("8", "6") + " = " + frac("4", "3"),
                "<b>(c)</b> Use Pythagoras on the horizontal and vertical differences, 6 and 8.",
                "AB<sup>2</sup> = 6<sup>2</sup> + 8<sup>2</sup> = 36 + 64 = 100, so AB = 10",
            ],
            "answer": "(a) (2, 6) &nbsp;&nbsp; (b) " + frac("4", "3") + " &nbsp;&nbsp; (c) 10",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Work out the gradient of the line joining (&minus;3, 5) and (1, &minus;3).</p>",
            "steps": [
                "Change in <i>y</i> = &minus;3 &minus; 5 = &minus;8",
                "Change in <i>x</i> = 1 &minus; (&minus;3) = 4",
                "Gradient = &minus;8 &divide; 4 = &minus;2",
            ],
            "answer": "&minus;2",
        },
        {
            "marks": 2,
            "q": "<p>Rearrange 4<i>x</i> &minus; 2<i>y</i> = 10 into the form <i>y</i> = m<i>x</i> + c.</p>",
            "steps": [
                "Subtract 4<i>x</i> from both sides: &minus;2<i>y</i> = &minus;4<i>x</i> + 10",
                "Divide every term by &minus;2, changing every sign.",
                "<i>y</i> = 2<i>x</i> &minus; 5",
            ],
            "answer": "<i>y</i> = 2<i>x</i> &minus; 5",
        },
        {
            "marks": 3,
            "q": "<p>Find the equation of the line parallel to <i>y</i> = &minus;2<i>x</i> + 1 that passes "
                 "through the point (3, 1).</p>",
            "steps": [
                "Parallel means the same gradient, so the line is <i>y</i> = &minus;2<i>x</i> + c",
                "Substitute (3, 1): 1 = &minus;2 &times; 3 + c = &minus;6 + c",
                "c = 7",
            ],
            "answer": "<i>y</i> = &minus;2<i>x</i> + 7",
        },
        {
            "marks": 3,
            "q": "<p>Find the equation of the line perpendicular to <i>y</i> = " + frac("1", "2")
                 + "<i>x</i> &minus; 4 that passes through the point (2, 5).</p>",
            "steps": [
                "Perpendicular gradients multiply to &minus;1.",
                frac("1", "2") + " &times; m = &minus;1, so m = &minus;2",
                "The line is <i>y</i> = &minus;2<i>x</i> + c, and substituting (2, 5) gives 5 = &minus;4 + c",
                "c = 9",
            ],
            "answer": "<i>y</i> = &minus;2<i>x</i> + 9",
        },
        {
            "marks": 4,
            "q": "<p>A is the point (1, 2) and B is the point (5, 10).</p>"
                 "<p>Find the equation of the perpendicular bisector of AB.</p>",
            "steps": [
                "The perpendicular bisector goes through the midpoint of AB at right angles to it.",
                "Midpoint = ((1 + 5) &divide; 2, (2 + 10) &divide; 2) = (3, 6)",
                "Gradient of AB = " + frac("8", "4") + " = 2, so the perpendicular gradient is &minus;" + frac("1", "2"),
                "The line is <i>y</i> = &minus;" + frac("1", "2") + "<i>x</i> + c",
                "Substitute (3, 6): 6 = &minus;1.5 + c, so c = 7.5",
            ],
            "answer": "<i>y</i> = &minus;" + frac("1", "2") + "<i>x</i> + 7.5 &nbsp;(or <i>x</i> + 2<i>y</i> = 15)",
        },
        {
            "marks": 4,
            "q": "<p>A is (&minus;2, &minus;5), B is (1, 1) and C is (4, 7).</p>"
                 "<p class='part'>(a) Show that A, B and C lie on the same straight line.</p>"
                 "<p class='part'>(b) Find the equation of that line.</p>",
            "steps": [
                "<b>(a)</b> Gradient AB = " + frac("1 &minus; (&minus;5)", "1 &minus; (&minus;2)") + " = " + frac("6", "3") + " = 2",
                "Gradient BC = " + frac("7 &minus; 1", "4 &minus; 1") + " = " + frac("6", "3") + " = 2",
                "The gradients are equal and the two segments share the point B, so all three points lie on one line.",
                "<b>(b)</b> Using <i>y</i> = 2<i>x</i> + c with the point B(1, 1): 1 = 2 + c, so c = &minus;1",
                "The line is <i>y</i> = 2<i>x</i> &minus; 1 (check C: 2(4) &minus; 1 = 7 &#10003;).",
            ],
            "answer": "(a) both gradients are 2 and they share B &nbsp;&nbsp; (b) <i>y</i> = 2<i>x</i> &minus; 1",
        },
        {
            "marks": 4,
            "q": "<p>The line L has equation 3<i>x</i> + 2<i>y</i> = 12</p>"
                 "<p class='part'>(a) Find the gradient of L.</p>"
                 "<p class='part'>(b) Find the equation of the line perpendicular to L through (0, 1).</p>"
                 "<p class='part'>(c) Does the point (6, &minus;3) lie on L? Show your working.</p>",
            "steps": [
                "<b>(a)</b> Rearrange: 2<i>y</i> = &minus;3<i>x</i> + 12, so <i>y</i> = &minus;" + frac("3", "2") + "<i>x</i> + 6",
                "The gradient is &minus;" + frac("3", "2"),
                "<b>(b)</b> The perpendicular gradient is " + frac("2", "3") + " (because &minus;" + frac("3", "2") + " &times; " + frac("2", "3") + " = &minus;1).",
                "The point (0, 1) gives the intercept directly: <i>y</i> = " + frac("2", "3") + "<i>x</i> + 1",
                "<b>(c)</b> Substitute into 3<i>x</i> + 2<i>y</i>: 3(6) + 2(&minus;3) = 18 &minus; 6 = 12 &#10003;",
            ],
            "answer": "(a) &minus;" + frac("3", "2") + " &nbsp;&nbsp; (b) <i>y</i> = " + frac("2", "3")
                      + "<i>x</i> + 1 &nbsp;&nbsp; (c) yes",
        },
        {
            "marks": 4,
            "q": "<p>The line <i>y</i> = &minus;<i>x</i> + 6 crosses the <i>x</i>-axis at P and the "
                 "<i>y</i>-axis at Q. O is the origin.</p>"
                 "<p class='part'>(a) Write down the coordinates of P and Q.</p>"
                 "<p class='part'>(b) Find the exact length of PQ.</p>"
                 "<p class='part'>(c) Find the area of triangle OPQ.</p>",
            "steps": [
                "<b>(a)</b> <i>y</i> = 0 gives <i>x</i> = 6, so P is (6, 0). <i>x</i> = 0 gives <i>y</i> = 6, so Q is (0, 6).",
                "<b>(b)</b> PQ<sup>2</sup> = 6<sup>2</sup> + 6<sup>2</sup> = 72",
                "PQ = &radic;72 = &radic;36 &times; &radic;2 = 6&radic;2",
                "<b>(c)</b> The triangle is right-angled at O with legs 6 and 6.",
                "Area = " + frac("1", "2") + " &times; 6 &times; 6 = 18 square units",
            ],
            "answer": "(a) P(6, 0), Q(0, 6) &nbsp;&nbsp; (b) 6&radic;2 &nbsp;&nbsp; (c) 18 square units",
        },
        {
            "marks": 4,
            "q": "<p>The line through (2, k) and (5, 11) has gradient 3.</p>"
                 "<p class='part'>(a) Find the value of k.</p>"
                 "<p class='part'>(b) Find the equation of the line.</p>",
            "steps": [
                "<b>(a)</b> Gradient = " + frac("11 &minus; k", "5 &minus; 2") + " = " + frac("11 &minus; k", "3"),
                "Set this equal to 3: 11 &minus; k = 9",
                "k = 2",
                "<b>(b)</b> Using <i>y</i> = 3<i>x</i> + c with (5, 11): 11 = 15 + c, so c = &minus;4",
                "The line is <i>y</i> = 3<i>x</i> &minus; 4 (check (2, 2): 6 &minus; 4 = 2 &#10003;).",
            ],
            "answer": "(a) k = 2 &nbsp;&nbsp; (b) <i>y</i> = 3<i>x</i> &minus; 4",
        },
        {
            "marks": 5,
            "q": "<p>The line <i>y</i> = 2<i>x</i> + 1 meets the line 3<i>x</i> + 2<i>y</i> = 16 at the point A.</p>"
                 "<p class='part'>(a) Find the coordinates of A.</p>"
                 "<p class='part'>(b) Find the equation of the line through A that is perpendicular to "
                 "<i>y</i> = 2<i>x</i> + 1</p>"
                 "<p class='part'>(c) Find where this perpendicular line crosses the <i>x</i>-axis.</p>",
            "steps": [
                "<b>(a)</b> Substitute <i>y</i> = 2<i>x</i> + 1 into 3<i>x</i> + 2<i>y</i> = 16",
                "3<i>x</i> + 2(2<i>x</i> + 1) = 16, so 7<i>x</i> + 2 = 16 and <i>x</i> = 2",
                "<i>y</i> = 2(2) + 1 = 5, so A is (2, 5).",
                "<b>(b)</b> The perpendicular gradient is &minus;" + frac("1", "2"),
                "<i>y</i> = &minus;" + frac("1", "2") + "<i>x</i> + c, and substituting A gives 5 = &minus;1 + c, so c = 6",
                "The line is <i>y</i> = &minus;" + frac("1", "2") + "<i>x</i> + 6",
                "<b>(c)</b> Set <i>y</i> = 0: " + frac("1", "2") + "<i>x</i> = 6, so <i>x</i> = 12, giving (12, 0)",
            ],
            "answer": "(a) (2, 5) &nbsp;&nbsp; (b) <i>y</i> = &minus;" + frac("1", "2")
                      + "<i>x</i> + 6 &nbsp;&nbsp; (c) (12, 0)",
        },
    ],
}

QUAD_GRAPHS = {
    "title": "Quadratic and Other Graphs",
    "folder": "gcse/graphs",
    "slug": "quadratic-graphs-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>What is the name of the shape of the graph of <i>y</i> = <i>x</i><sup>2</sup>?</p>",
            "steps": [
                "A quadratic graph is a smooth symmetrical U-shape.",
                "Its mathematical name is a parabola.",
            ],
            "answer": "a parabola (a U-shaped curve)",
        },
        {
            "marks": 2,
            "q": "<p>Complete the table of values for <i>y</i> = <i>x</i><sup>2</sup></p>"
                 "<table class='d'><tr><th><i>x</i></th><td>&minus;2</td><td>&minus;1</td><td>0</td><td>1</td><td>2</td></tr>"
                 "<tr><th><i>y</i></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>",
            "steps": [
                "Squaring a negative number gives a positive answer.",
                "(&minus;2)<sup>2</sup> = 4 and (&minus;1)<sup>2</sup> = 1",
                "0<sup>2</sup> = 0, 1<sup>2</sup> = 1 and 2<sup>2</sup> = 4",
                "Notice the symmetry of the values either side of 0.",
            ],
            "answer": "4, 1, 0, 1, 4",
        },
        {
            "marks": 2,
            "q": "<p>Work out the values of <i>y</i> for <i>y</i> = <i>x</i><sup>2</sup> &minus; 3 when</p>"
                 "<p class='part'>(a) <i>x</i> = &minus;2 &nbsp;&nbsp; (b) <i>x</i> = 0 &nbsp;&nbsp; (c) <i>x</i> = 3</p>",
            "steps": [
                "<b>(a)</b> (&minus;2)<sup>2</sup> &minus; 3 = 4 &minus; 3 = 1",
                "<b>(b)</b> 0 &minus; 3 = &minus;3",
                "<b>(c)</b> 9 &minus; 3 = 6",
            ],
            "answer": "(a) 1 &nbsp;&nbsp; (b) &minus;3 &nbsp;&nbsp; (c) 6",
        },
        {
            "marks": 2,
            "q": "<p>Write down the coordinates of the points where the curve "
                 "<i>y</i> = <i>x</i><sup>2</sup> &minus; 4 crosses the <i>x</i>-axis.</p>",
            "steps": [
                "On the <i>x</i>-axis, <i>y</i> = 0, so <i>x</i><sup>2</sup> &minus; 4 = 0",
                "<i>x</i><sup>2</sup> = 4, so <i>x</i> = 2 or <i>x</i> = &minus;2",
            ],
            "answer": "(2, 0) and (&minus;2, 0)",
        },
        {
            "marks": 3,
            "q": "<p>A curve has equation <i>y</i> = <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 3</p>"
                 "<p class='part'>(a) Factorise <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 3</p>"
                 "<p class='part'>(b) Write down where the curve crosses the <i>x</i>-axis.</p>"
                 "<p class='part'>(c) Write down where the curve crosses the <i>y</i>-axis.</p>",
            "steps": [
                "<b>(a)</b> Two numbers multiplying to &minus;3 and adding to &minus;2 are &minus;3 and +1.",
                "So the answer is (<i>x</i> &minus; 3)(<i>x</i> + 1)",
                "<b>(b)</b> Setting each bracket to zero gives <i>x</i> = 3 and <i>x</i> = &minus;1",
                "The crossing points are (3, 0) and (&minus;1, 0).",
                "<b>(c)</b> Setting <i>x</i> = 0 gives <i>y</i> = &minus;3, so (0, &minus;3)",
            ],
            "answer": "(a) (<i>x</i> &minus; 3)(<i>x</i> + 1) &nbsp;&nbsp; (b) (3, 0) and (&minus;1, 0) &nbsp;&nbsp; (c) (0, &minus;3)",
        },
        {
            "marks": 3,
            "q": "<p>The curve <i>y</i> = <i>x</i><sup>2</sup> &minus; 6<i>x</i> + 8 crosses the <i>x</i>-axis "
                 "at <i>x</i> = 2 and <i>x</i> = 4.</p>"
                 "<p class='part'>(a) Write down the equation of the line of symmetry.</p>"
                 "<p class='part'>(b) Work out the coordinates of the turning point.</p>",
            "steps": [
                "<b>(a)</b> A parabola is symmetrical, so the line of symmetry is halfway between the roots.",
                "(2 + 4) &divide; 2 = 3, so the line is <i>x</i> = 3",
                "<b>(b)</b> The turning point lies on that line, so substitute <i>x</i> = 3.",
                "<i>y</i> = 9 &minus; 18 + 8 = &minus;1, giving the minimum point (3, &minus;1)",
            ],
            "answer": "(a) <i>x</i> = 3 &nbsp;&nbsp; (b) (3, &minus;1)",
        },
        {
            "marks": 3,
            "q": "<p>Describe the shape of the graph of each equation.</p>"
                 "<p class='part'>(a) <i>y</i> = <i>x</i><sup>3</sup></p>"
                 "<p class='part'>(b) <i>y</i> = " + frac("1", "<i>x</i>") + "</p>"
                 "<p class='part'>(c) <i>y</i> = 2<sup><i>x</i></sup></p>",
            "steps": [
                "<b>(a)</b> A cubic graph &mdash; a smooth curve with an S-shaped bend, going from bottom left "
                "to top right.",
                "<b>(b)</b> A reciprocal graph &mdash; two separate curved branches, one in each of the "
                "top-right and bottom-left regions, never touching the axes.",
                "<b>(c)</b> An exponential graph &mdash; always positive, rising more and more steeply, and "
                "getting closer and closer to the <i>x</i>-axis on the left without ever reaching it.",
            ],
            "answer": "(a) cubic &nbsp;&nbsp; (b) reciprocal (two branches) &nbsp;&nbsp; (c) exponential growth",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Complete the table of values for <i>y</i> = <i>x</i><sup>2</sup> + 2<i>x</i></p>"
                 "<table class='d'><tr><th><i>x</i></th><td>&minus;3</td><td>&minus;2</td><td>&minus;1</td><td>0</td><td>1</td></tr>"
                 "<tr><th><i>y</i></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>"
                 "<p class='part'>(b) Write down the coordinates of the minimum point.</p>",
            "steps": [
                "<b>(a)</b> <i>x</i> = &minus;3: 9 &minus; 6 = 3 &nbsp;&middot;&nbsp; <i>x</i> = &minus;2: 4 &minus; 4 = 0",
                "<i>x</i> = &minus;1: 1 &minus; 2 = &minus;1 &nbsp;&middot;&nbsp; <i>x</i> = 0: 0 &nbsp;&middot;&nbsp; <i>x</i> = 1: 1 + 2 = 3",
                "<b>(b)</b> The smallest <i>y</i>-value in the table is &minus;1 at <i>x</i> = &minus;1, and the values "
                "are symmetrical about it.",
                "So the minimum point is (&minus;1, &minus;1).",
            ],
            "answer": "(a) 3, 0, &minus;1, 0, 3 &nbsp;&nbsp; (b) (&minus;1, &minus;1)",
        },
        {
            "marks": 4,
            "q": "<p>Use an algebraic method to find the solutions of "
                 "<i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 4 = 0, correct to 1 decimal place.</p>"
                 "<p>These are the values where the curve <i>y</i> = <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 4 "
                 "crosses the <i>x</i>-axis.</p>",
            "steps": [
                "The expression will not factorise, so complete the square.",
                "Half of &minus;2 is &minus;1: (<i>x</i> &minus; 1)<sup>2</sup> &minus; 1 &minus; 4 = (<i>x</i> &minus; 1)<sup>2</sup> &minus; 5",
                "(<i>x</i> &minus; 1)<sup>2</sup> = 5, so <i>x</i> &minus; 1 = &plusmn;&radic;5 = &plusmn;2.2360&hellip;",
                "<i>x</i> = 1 + 2.236 = 3.236&hellip; or <i>x</i> = 1 &minus; 2.236 = &minus;1.236&hellip;",
                "So the curve crosses the axis at about <i>x</i> = 3.2 and <i>x</i> = &minus;1.2",
            ],
            "answer": "<i>x</i> = 3.2 &nbsp;and&nbsp; <i>x</i> = &minus;1.2 (1 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>A curve has equation <i>y</i> = <i>x</i><sup>3</sup> &minus; 4<i>x</i></p>"
                 "<p class='part'>(a) Factorise <i>x</i><sup>3</sup> &minus; 4<i>x</i> fully.</p>"
                 "<p class='part'>(b) Write down the three values of <i>x</i> where the curve meets the <i>x</i>-axis.</p>"
                 "<p class='part'>(c) Work out <i>y</i> when <i>x</i> = 3</p>",
            "steps": [
                "<b>(a)</b> Take out the common factor <i>x</i>: <i>x</i>(<i>x</i><sup>2</sup> &minus; 4)",
                "The bracket is a difference of two squares: <i>x</i>(<i>x</i> + 2)(<i>x</i> &minus; 2)",
                "<b>(b)</b> Setting each factor to zero gives <i>x</i> = 0, <i>x</i> = &minus;2 and <i>x</i> = 2",
                "<b>(c)</b> <i>y</i> = 3<sup>3</sup> &minus; 4 &times; 3 = 27 &minus; 12 = 15",
            ],
            "answer": "(a) <i>x</i>(<i>x</i> + 2)(<i>x</i> &minus; 2) &nbsp;&nbsp; (b) &minus;2, 0 and 2 &nbsp;&nbsp; (c) 15",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Write down the coordinates of the turning point of "
                 "<i>y</i> = (<i>x</i> &minus; 2)<sup>2</sup> + 5</p>",
            "steps": [
                "The squared bracket is smallest (zero) when <i>x</i> = 2",
                "Then <i>y</i> = 5, so the minimum point is (2, 5).",
            ],
            "answer": "(2, 5)",
        },
        {
            "marks": 2,
            "q": "<p>How many times does the curve <i>y</i> = <i>x</i><sup>3</sup> &minus; 3<i>x</i> cross the "
                 "<i>x</i>-axis? Show your working.</p>",
            "steps": [
                "Set <i>y</i> = 0 and factorise: <i>x</i>(<i>x</i><sup>2</sup> &minus; 3) = 0",
                "<i>x</i> = 0, or <i>x</i><sup>2</sup> = 3 giving <i>x</i> = &radic;3 and <i>x</i> = &minus;&radic;3",
                "That is three different values.",
            ],
            "answer": "3 times, at <i>x</i> = 0, &radic;3 and &minus;&radic;3",
        },
        {
            "marks": 3,
            "q": "<p>Find the coordinates of the turning point of "
                 "<i>y</i> = <i>x</i><sup>2</sup> + 4<i>x</i> &minus; 1 by completing the square.</p>",
            "steps": [
                "Half of 4 is 2, so (<i>x</i> + 2)<sup>2</sup> = <i>x</i><sup>2</sup> + 4<i>x</i> + 4",
                "<i>y</i> = (<i>x</i> + 2)<sup>2</sup> &minus; 4 &minus; 1 = (<i>x</i> + 2)<sup>2</sup> &minus; 5",
                "The bracket is zero when <i>x</i> = &minus;2, and then <i>y</i> = &minus;5",
            ],
            "answer": "minimum at (&minus;2, &minus;5)",
        },
        {
            "marks": 3,
            "q": "<p>A circle has equation <i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> = 49</p>"
                 "<p class='part'>(a) Write down the centre and the radius.</p>"
                 "<p class='part'>(b) Does the point (5, 5) lie inside, on, or outside the circle? "
                 "Show your working.</p>",
            "steps": [
                "<b>(a)</b> The form <i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> = r<sup>2</sup> has centre "
                "at the origin (0, 0) and radius r.",
                "49 = 7<sup>2</sup>, so the radius is 7.",
                "<b>(b)</b> Work out <i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> for the point: 5<sup>2</sup> + 5<sup>2</sup> = 50",
                "50 is greater than 49, so the point is further than 7 from the centre &mdash; it lies outside.",
            ],
            "answer": "(a) centre (0, 0), radius 7 &nbsp;&nbsp; (b) outside, since 50 &gt; 49",
        },
        {
            "marks": 4,
            "q": "<p>The point P(3, 4) lies on the circle <i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> = 25</p>"
                 "<p>Find the equation of the tangent to the circle at P.</p>",
            "steps": [
                "The tangent is perpendicular to the radius drawn to P.",
                "Gradient of the radius OP = " + frac("4 &minus; 0", "3 &minus; 0") + " = " + frac("4", "3"),
                "So the tangent gradient is &minus;" + frac("3", "4"),
                "Use <i>y</i> = &minus;" + frac("3", "4") + "<i>x</i> + c with P(3, 4): 4 = &minus;2.25 + c",
                "c = 6.25, so <i>y</i> = &minus;" + frac("3", "4") + "<i>x</i> + 6.25",
                "Multiplying by 4 gives the neater form 3<i>x</i> + 4<i>y</i> = 25",
            ],
            "answer": "3<i>x</i> + 4<i>y</i> = 25",
        },
        {
            "marks": 4,
            "q": "<p>The graph of <i>y</i> = f(<i>x</i>) passes through the point (2, 5).</p>"
                 "<p>Write down the coordinates of the corresponding point on each of these graphs.</p>"
                 "<p class='part'>(a) <i>y</i> = f(<i>x</i>) &minus; 3 &nbsp;&nbsp; (b) <i>y</i> = f(<i>x</i> + 1)</p>"
                 "<p class='part'>(c) <i>y</i> = 2f(<i>x</i>) &nbsp;&nbsp; (d) <i>y</i> = f(&minus;<i>x</i>)</p>",
            "steps": [
                "<b>(a)</b> Subtracting 3 outside the function moves the graph down 3: (2, 2)",
                "<b>(b)</b> Replacing <i>x</i> by <i>x</i> + 1 inside moves the graph 1 to the <b>left</b>: (1, 5)",
                "<b>(c)</b> Multiplying outside by 2 stretches vertically, doubling the <i>y</i>-coordinate: (2, 10)",
                "<b>(d)</b> Replacing <i>x</i> by &minus;<i>x</i> reflects the graph in the <i>y</i>-axis: (&minus;2, 5)",
            ],
            "answer": "(a) (2, 2) &nbsp;&nbsp; (b) (1, 5) &nbsp;&nbsp; (c) (2, 10) &nbsp;&nbsp; (d) (&minus;2, 5)",
        },
        {
            "marks": 4,
            "q": "<p>A curve has equation <i>y</i> = 3 &times; 2<sup><i>x</i></sup></p>"
                 "<p class='part'>(a) Work out <i>y</i> when <i>x</i> = 0</p>"
                 "<p class='part'>(b) Work out <i>y</i> when <i>x</i> = 4</p>"
                 "<p class='part'>(c) Work out <i>y</i> when <i>x</i> = &minus;1</p>"
                 "<p class='part'>(d) Explain why the curve never touches the <i>x</i>-axis.</p>",
            "steps": [
                "<b>(a)</b> 2<sup>0</sup> = 1, so <i>y</i> = 3 &times; 1 = 3",
                "<b>(b)</b> 2<sup>4</sup> = 16, so <i>y</i> = 3 &times; 16 = 48",
                "<b>(c)</b> 2<sup>&minus;1</sup> = " + frac("1", "2") + ", so <i>y</i> = 3 &times; 0.5 = 1.5",
                "<b>(d)</b> 2<sup><i>x</i></sup> is always greater than zero, however negative <i>x</i> becomes.",
                "So <i>y</i> gets closer and closer to 0 but never actually reaches it &mdash; the <i>x</i>-axis "
                "is an asymptote.",
            ],
            "answer": "(a) 3 &nbsp;&nbsp; (b) 48 &nbsp;&nbsp; (c) 1.5 &nbsp;&nbsp; (d) 2<sup><i>x</i></sup> is never zero",
        },
        {
            "marks": 4,
            "q": "<p>A curve has equation <i>y</i> = " + frac("12", "<i>x</i>") + "</p>"
                 "<p class='part'>(a) Complete the table of values.</p>"
                 "<table class='d'><tr><th><i>x</i></th><td>1</td><td>2</td><td>3</td><td>4</td><td>6</td></tr>"
                 "<tr><th><i>y</i></th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>"
                 "<p class='part'>(b) Explain why <i>x</i> = 0 cannot be used.</p>"
                 "<p class='part'>(c) Describe the symmetry of the full graph.</p>",
            "steps": [
                "<b>(a)</b> 12 &divide; 1 = 12, 12 &divide; 2 = 6, 12 &divide; 3 = 4, 12 &divide; 4 = 3, 12 &divide; 6 = 2",
                "<b>(b)</b> Substituting <i>x</i> = 0 would mean dividing 12 by zero, which has no value.",
                "So the curve has a break there and never crosses the <i>y</i>-axis.",
                "<b>(c)</b> There are two branches, one for positive <i>x</i> and one for negative <i>x</i>.",
                "The graph has rotational symmetry of order 2 about the origin.",
            ],
            "answer": "(a) 12, 6, 4, 3, 2 &nbsp;&nbsp; (b) it would mean dividing by zero &nbsp;&nbsp; "
                      "(c) rotational symmetry of order 2 about the origin",
        },
        {
            "marks": 4,
            "q": "<p>The curve <i>y</i> = <i>x</i><sup>2</sup> + 1 passes through the points (1.9, 4.61) "
                 "and (2.1, 5.41).</p>"
                 "<p class='part'>(a) Use these two points to estimate the gradient of the curve at <i>x</i> = 2</p>"
                 "<p class='part'>(b) Explain why this is only an estimate.</p>",
            "steps": [
                "<b>(a)</b> The line joining the two points is a chord, and its gradient approximates the "
                "gradient of the curve between them.",
                "Change in <i>y</i> = 5.41 &minus; 4.61 = 0.80",
                "Change in <i>x</i> = 2.1 &minus; 1.9 = 0.2",
                "Gradient = " + frac("0.80", "0.2") + " = 4",
                "<b>(b)</b> The gradient of a curve changes from point to point, so the chord&rsquo;s gradient is "
                "only an average over that small interval, not the exact gradient at <i>x</i> = 2 "
                "(although here the chord is short, so the estimate is good).",
            ],
            "answer": "(a) 4 &nbsp;&nbsp; (b) a chord gives an average gradient over an interval, not the exact "
                      "gradient at a single point",
        },
        {
            "marks": 5,
            "q": "<p>The graph of <i>y</i> = <i>x</i><sup>2</sup> &minus; 3<i>x</i> has been drawn.</p>"
                 "<p class='part'>(a) Explain which straight line should be drawn on the same axes to solve "
                 "<i>x</i><sup>2</sup> &minus; 3<i>x</i> = 2<i>x</i> &minus; 4</p>"
                 "<p class='part'>(b) Solve the equation algebraically.</p>"
                 "<p class='part'>(c) Write down the coordinates of the two points where the curve and the line "
                 "would cross.</p>",
            "steps": [
                "<b>(a)</b> The solutions are the <i>x</i>-values where the two sides of the equation are equal.",
                "The left-hand side is the curve already drawn, so draw the line <i>y</i> = 2<i>x</i> &minus; 4 "
                "and read off the <i>x</i>-coordinates where the graphs cross.",
                "<b>(b)</b> <i>x</i><sup>2</sup> &minus; 3<i>x</i> = 2<i>x</i> &minus; 4, so <i>x</i><sup>2</sup> &minus; 5<i>x</i> + 4 = 0",
                "Factorise: (<i>x</i> &minus; 1)(<i>x</i> &minus; 4) = 0, so <i>x</i> = 1 or <i>x</i> = 4",
                "<b>(c)</b> Substitute into the line <i>y</i> = 2<i>x</i> &minus; 4.",
                "<i>x</i> = 1 gives <i>y</i> = &minus;2 and <i>x</i> = 4 gives <i>y</i> = 4, so the points are "
                "(1, &minus;2) and (4, 4).",
            ],
            "answer": "(a) draw <i>y</i> = 2<i>x</i> &minus; 4 &nbsp;&nbsp; (b) <i>x</i> = 1 or <i>x</i> = 4 &nbsp;&nbsp; "
                      "(c) (1, &minus;2) and (4, 4)",
        },
    ],
}

REAL_LIFE = {
    "title": "Real-Life Graphs",
    "folder": "gcse/graphs",
    "slug": "real-life-graphs-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>The conversion graph changes between miles and kilometres.</p>"
                 + CONVERSION_GRAPH +
                 "<p>Use the graph to convert 20 miles into kilometres.</p>",
            "steps": [
                "Find 20 on the horizontal (miles) axis and go straight up to the line.",
                "Then read across to the vertical (kilometres) axis.",
            ],
            "answer": "32 km",
        },
        {
            "marks": 2,
            "q": "<p>Use the same conversion graph to change 48 kilometres into miles.</p>",
            "steps": [
                "This time start on the vertical axis at 48 km.",
                "Go across to the line, then straight down to the miles axis.",
                "This reads 30 miles. (Check: 30 &times; 1.6 = 48 &#10003;)",
            ],
            "answer": "30 miles",
        },
        {
            "marks": 2,
            "q": "<p>The conversion line passes through (0, 0) and (50, 80).</p>"
                 "<p class='part'>(a) Work out the gradient of the line.</p>"
                 "<p class='part'>(b) What does the gradient tell you?</p>",
            "steps": [
                "<b>(a)</b> Gradient = " + frac("80 &minus; 0", "50 &minus; 0") + " = 1.6",
                "<b>(b)</b> The gradient is the number of kilometres per mile.",
                "So 1 mile is about 1.6 km.",
            ],
            "answer": "(a) 1.6 &nbsp;&nbsp; (b) 1 mile &asymp; 1.6 km",
        },
        {
            "marks": 2,
            "q": "<p>A plumber charges a &pound;40 call-out fee plus &pound;25 for each hour worked.</p>"
                 "<p>Write a formula for the cost, C pounds, of a job lasting h hours.</p>",
            "steps": [
                "The hourly part is 25 &times; h.",
                "The call-out fee is added on whatever the length of the job.",
            ],
            "answer": "C = 25h + 40",
        },
        {
            "marks": 3,
            "q": "<p>Using C = 25h + 40</p>"
                 "<p class='part'>(a) Work out the cost of a job lasting 3 hours.</p>"
                 "<p class='part'>(b) A job cost &pound;165. How many hours did it take?</p>",
            "steps": [
                "<b>(a)</b> C = 25 &times; 3 + 40 = 75 + 40 = &pound;115",
                "<b>(b)</b> 25h + 40 = 165",
                "25h = 125, so h = 5 hours",
            ],
            "answer": "(a) &pound;115 &nbsp;&nbsp; (b) 5 hours",
        },
        {
            "marks": 3,
            "q": "<p>A cyclist travels 24 km in 1 hour 30 minutes.</p>"
                 "<p class='part'>(a) Work out the average speed in km/h.</p>"
                 "<p class='part'>(b) At the same speed, how long would it take to travel 40 km?</p>",
            "steps": [
                "<b>(a)</b> 1 hour 30 minutes = 1.5 hours",
                "Speed = " + frac("24", "1.5") + " = 16 km/h",
                "<b>(b)</b> Time = " + frac("distance", "speed") + " = " + frac("40", "16") + " = 2.5 hours",
                "That is 2 hours 30 minutes.",
            ],
            "answer": "(a) 16 km/h &nbsp;&nbsp; (b) 2.5 hours",
        },
        {
            "marks": 3,
            "q": "<p>On a distance&ndash;time graph, describe what each of these tells you about the journey.</p>"
                 "<p class='part'>(a) A horizontal section.</p>"
                 "<p class='part'>(b) A steeper section.</p>"
                 "<p class='part'>(c) A section sloping back down to zero.</p>",
            "steps": [
                "<b>(a)</b> The distance is not changing, so the object is stationary (stopped).",
                "<b>(b)</b> A steeper gradient means more distance in the same time, so a faster speed.",
                "<b>(c)</b> The distance from the start is decreasing, so the object is travelling back "
                "towards its starting point.",
            ],
            "answer": "(a) stopped &nbsp;&nbsp; (b) travelling faster &nbsp;&nbsp; (c) returning to the start",
        },
        {
            "marks": 3,
            "q": "<p>The exchange rate is &pound;1 = &euro;1.15</p>"
                 "<p class='part'>(a) Change &pound;250 into euros.</p>"
                 "<p class='part'>(b) Change &euro;69 into pounds.</p>",
            "steps": [
                "<b>(a)</b> Pounds to euros means multiplying: 250 &times; 1.15 = 287.5",
                "So &pound;250 = &euro;287.50",
                "<b>(b)</b> Euros to pounds means dividing: 69 &divide; 1.15 = 60",
                "So &euro;69 = &pound;60",
            ],
            "answer": "(a) &euro;287.50 &nbsp;&nbsp; (b) &pound;60",
        },
        {
            "marks": 4,
            "q": "<p>Two gyms offer different deals.</p>"
                 "<p class='part'><b>Gym A:</b> &pound;30 per month plus &pound;2 for each visit.</p>"
                 "<p class='part'><b>Gym B:</b> &pound;10 per month plus &pound;6 for each visit.</p>"
                 "<p class='part'>(a) Write a formula for the monthly cost of each gym for v visits.</p>"
                 "<p class='part'>(b) For how many visits do the two gyms cost the same?</p>"
                 "<p class='part'>(c) Which gym is cheaper for someone who visits 8 times a month?</p>",
            "steps": [
                "<b>(a)</b> Gym A: C = 2v + 30 &nbsp;&nbsp; Gym B: C = 6v + 10",
                "<b>(b)</b> Set them equal: 2v + 30 = 6v + 10",
                "20 = 4v, so v = 5 visits",
                "<b>(c)</b> Gym A: 2 &times; 8 + 30 = &pound;46",
                "Gym B: 6 &times; 8 + 10 = &pound;58, so Gym A is cheaper by &pound;12.",
            ],
            "answer": "(a) A: 2v + 30, B: 6v + 10 &nbsp;&nbsp; (b) 5 visits &nbsp;&nbsp; (c) Gym A (&pound;46 v &pound;58)",
        },
        {
            "marks": 4,
            "q": "<p>A tank is filled with water at a constant rate.</p>"
                 "<p>After 2 minutes it holds 30 litres. After 5 minutes it holds 75 litres.</p>"
                 "<p class='part'>(a) Work out the rate of filling, in litres per minute.</p>"
                 "<p class='part'>(b) How much water was in the tank at the start?</p>"
                 "<p class='part'>(c) How long does it take to reach 200 litres?</p>",
            "steps": [
                "<b>(a)</b> The volume rises by 75 &minus; 30 = 45 litres in 5 &minus; 2 = 3 minutes.",
                "Rate = 45 &divide; 3 = 15 litres per minute (this is the gradient of the graph).",
                "<b>(b)</b> Working back from 2 minutes: 30 &minus; 2 &times; 15 = 0",
                "The tank started empty.",
                "<b>(c)</b> Time = 200 &divide; 15 = 13.33&hellip; minutes",
                "That is 13 minutes 20 seconds.",
            ],
            "answer": "(a) 15 litres/min &nbsp;&nbsp; (b) it was empty &nbsp;&nbsp; (c) 13 minutes 20 seconds",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>A car accelerates uniformly from rest to 24 m/s in 8 seconds.</p>"
                 "<p>Work out the acceleration.</p>",
            "steps": [
                "Acceleration is the gradient of a speed&ndash;time graph.",
                "Change in speed = 24 &minus; 0 = 24 m/s over 8 s.",
                "24 &divide; 8 = 3",
            ],
            "answer": "3 m/s<sup>2</sup>",
        },
        {
            "marks": 2,
            "q": "<p class='part'>(a) What does the gradient represent on a distance&ndash;time graph?</p>"
                 "<p class='part'>(b) What does the area under the graph represent on a speed&ndash;time graph?</p>",
            "steps": [
                "<b>(a)</b> Gradient = change in distance &divide; change in time, which is the speed.",
                "<b>(b)</b> Speed &times; time gives distance, and that is exactly what the area under the "
                "graph works out.",
            ],
            "answer": "(a) speed &nbsp;&nbsp; (b) distance travelled",
        },
        {
            "marks": 3,
            "q": "<p>A train travels at a constant 18 m/s for 25 seconds, then decelerates uniformly to rest "
                 "over the next 12 seconds.</p>"
                 "<p>Work out the total distance travelled.</p>",
            "steps": [
                "Sketch the speed&ndash;time graph: a rectangle followed by a triangle.",
                "Rectangle: 18 &times; 25 = 450 m",
                "Triangle: " + frac("1", "2") + " &times; 12 &times; 18 = 108 m",
                "Total = 450 + 108 = 558 m",
            ],
            "answer": "558 m",
        },
        {
            "marks": 3,
            "q": "<p>A driver covers 45 km at an average speed of 90 km/h, then 30 km at an average speed "
                 "of 60 km/h.</p>"
                 "<p>Work out the average speed for the whole journey.</p>",
            "steps": [
                "Find each time: 45 &divide; 90 = 0.5 hours and 30 &divide; 60 = 0.5 hours.",
                "Total time = 1 hour and total distance = 45 + 30 = 75 km.",
                "Average speed = " + frac("75", "1") + " = 75 km/h",
                "(Note this is not the same as averaging 90 and 60, which would give 75 only by coincidence "
                "because the two times happen to be equal.)",
            ],
            "answer": "75 km/h",
        },
        {
            "marks": 4,
            "q": "<p>The speed of a car, in m/s, is recorded every 2 seconds.</p>"
                 "<table class='d'><tr><th>Time (s)</th><td>0</td><td>2</td><td>4</td><td>6</td></tr>"
                 "<tr><th>Speed (m/s)</th><td>0</td><td>5</td><td>12</td><td>21</td></tr></table>"
                 "<p class='part'>(a) Use three trapezia to estimate the distance travelled in the "
                 "first 6 seconds.</p>"
                 "<p class='part'>(b) Is your answer an under-estimate or an over-estimate? Explain.</p>",
            "steps": [
                "<b>(a)</b> Each trapezium has width 2 and area " + frac("1", "2") + " &times; width &times; (sum of the two heights).",
                "0 to 2 s: " + frac("1", "2") + " &times; 2 &times; (0 + 5) = 5 m",
                "2 to 4 s: " + frac("1", "2") + " &times; 2 &times; (5 + 12) = 17 m",
                "4 to 6 s: " + frac("1", "2") + " &times; 2 &times; (12 + 21) = 33 m",
                "Total = 5 + 17 + 33 = 55 m",
                "<b>(b)</b> The speed is increasing faster and faster (gaps of 5, 7, 9), so the curve bends "
                "upwards and each straight chord lies above it &mdash; the estimate is too big.",
            ],
            "answer": "(a) about 55 m &nbsp;&nbsp; (b) an over-estimate, because the curve bends upwards and "
                      "the trapezia sit above it",
        },
        {
            "marks": 4,
            "q": "<p>The depth of water, d cm, in a container is measured over time.</p>"
                 "<table class='d'><tr><th>Time (min)</th><td>0</td><td>2</td><td>4</td><td>6</td></tr>"
                 "<tr><th>Depth (cm)</th><td>0</td><td>14</td><td>24</td><td>30</td></tr></table>"
                 "<p class='part'>(a) Work out the average rate of increase between 2 and 4 minutes.</p>"
                 "<p class='part'>(b) Describe how the rate of filling changes, and suggest what this says "
                 "about the shape of the container.</p>",
            "steps": [
                "<b>(a)</b> Depth rises by 24 &minus; 14 = 10 cm in 2 minutes.",
                "Rate = 10 &divide; 2 = 5 cm per minute",
                "<b>(b)</b> The rises in each 2-minute interval are 14 cm, 10 cm then 6 cm, so the depth is "
                "increasing more and more slowly.",
                "If water flows in at a steady rate, the level rises more slowly where the container is "
                "wider, so the container must get wider towards the top.",
            ],
            "answer": "(a) 5 cm/min &nbsp;&nbsp; (b) the rate is slowing down, so the container widens towards the top",
        },
        {
            "marks": 4,
            "q": "<p>A cup of coffee cools so that its temperature T &deg;C after t minutes is</p>"
                 "<p>&nbsp;&nbsp;T = 20 + 60 &times; 0.8<sup>t</sup></p>"
                 "<p class='part'>(a) Work out the starting temperature.</p>"
                 "<p class='part'>(b) Work out the temperature after 5 minutes, to 1 decimal place.</p>"
                 "<p class='part'>(c) Explain what the number 20 represents.</p>",
            "steps": [
                "<b>(a)</b> At t = 0, 0.8<sup>0</sup> = 1, so T = 20 + 60 = 80 &deg;C",
                "<b>(b)</b> 0.8<sup>5</sup> = 0.32768",
                "T = 20 + 60 &times; 0.32768 = 20 + 19.6608 = 39.6608&hellip;",
                "<b>(c)</b> As t grows, 0.8<sup>t</sup> gets closer and closer to 0, so T approaches 20.",
                "The 20 is the room temperature the coffee cools towards but never quite reaches.",
            ],
            "answer": "(a) 80 &deg;C &nbsp;&nbsp; (b) 39.7 &deg;C &nbsp;&nbsp; (c) the room temperature it cools towards",
        },
        {
            "marks": 4,
            "q": "<p>&pound;2000 is invested at 5% compound interest per year.</p>"
                 "<p class='part'>(a) Work out the value after 10 years, to the nearest penny.</p>"
                 "<p class='part'>(b) A graph of value against time is drawn. Explain why it is a curve "
                 "rather than a straight line.</p>",
            "steps": [
                "<b>(a)</b> The multiplier is 1.05 each year, so the value is 2000 &times; 1.05<sup>10</sup>",
                "1.05<sup>10</sup> = 1.6288946&hellip;",
                "2000 &times; 1.6288946 = 3257.789&hellip;, so &pound;3257.79",
                "<b>(b)</b> With compound interest the interest each year is worked out on a larger amount "
                "than the year before.",
                "So the yearly increase keeps growing, and a graph with an increasing gradient is a curve, "
                "not a straight line.",
            ],
            "answer": "(a) &pound;3257.79 &nbsp;&nbsp; (b) the yearly increase grows each year, so the gradient "
                      "increases",
        },
        {
            "marks": 4,
            "q": "<p>A car leaves home at 09:00, drives 90 km and arrives at 10:30. It stops for 30 minutes, "
                 "then drives the 90 km home, arriving at 12:30.</p>"
                 "<p class='part'>(a) Work out the average speed on the outward journey.</p>"
                 "<p class='part'>(b) Work out the average speed on the return journey.</p>"
                 "<p class='part'>(c) Work out the average speed for the whole trip, including the stop, "
                 "to 1 decimal place.</p>",
            "steps": [
                "<b>(a)</b> 09:00 to 10:30 is 1.5 hours, so speed = 90 &divide; 1.5 = 60 km/h",
                "<b>(b)</b> The stop ends at 11:00, so the return takes 11:00 to 12:30 = 1.5 hours.",
                "Speed = 90 &divide; 1.5 = 60 km/h",
                "<b>(c)</b> Total distance = 180 km and total time = 09:00 to 12:30 = 3.5 hours.",
                "Average speed = " + frac("180", "3.5") + " = 51.428&hellip; km/h",
            ],
            "answer": "(a) 60 km/h &nbsp;&nbsp; (b) 60 km/h &nbsp;&nbsp; (c) 51.4 km/h (1 d.p.)",
        },
        {
            "marks": 5,
            "q": "<p>A train accelerates uniformly from rest to V m/s in 20 seconds. It then travels at "
                 "V m/s for 60 seconds, before decelerating uniformly to rest in a further 40 seconds.</p>"
                 "<p>The total distance travelled is 3600 m.</p>"
                 "<p class='part'>(a) Find the value of V.</p>"
                 "<p class='part'>(b) Work out the acceleration during the first stage.</p>",
            "steps": [
                "<b>(a)</b> The speed&ndash;time graph is a trapezium: triangle, rectangle, triangle.",
                "First triangle: " + frac("1", "2") + " &times; 20 &times; V = 10V",
                "Rectangle: 60 &times; V = 60V &nbsp;&middot;&nbsp; Second triangle: " + frac("1", "2") + " &times; 40 &times; V = 20V",
                "Total area = 10V + 60V + 20V = 90V, and this equals 3600",
                "V = 3600 &divide; 90 = 40 m/s",
                "<b>(b)</b> Acceleration = " + frac("40", "20") + " = 2 m/s<sup>2</sup>",
            ],
            "answer": "(a) V = 40 m/s &nbsp;&nbsp; (b) 2 m/s<sup>2</sup>",
        },
    ],
}

PAPERS = [STRAIGHT_LINE, QUAD_GRAPHS, REAL_LIFE]
