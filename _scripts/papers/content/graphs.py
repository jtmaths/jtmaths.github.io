"""GCSE practice paper — Graphs (topic level)."""
from build import frac

# ── two small hand-built graphs, drawn as inline SVG so they print offline ──

DT_GRAPH = """
<svg width="330" height="205" viewBox="0 0 330 205" xmlns="http://www.w3.org/2000/svg"
     font-family="Arial, Helvetica, sans-serif" font-size="9">
  <g stroke="#dbe0ea" stroke-width="1">
    <line x1="92"  y1="20" x2="92"  y2="170"/><line x1="144" y1="20" x2="144" y2="170"/>
    <line x1="196" y1="20" x2="196" y2="170"/><line x1="248" y1="20" x2="248" y2="170"/>
    <line x1="300" y1="20" x2="300" y2="170"/>
    <line x1="40" y1="145" x2="300" y2="145"/><line x1="40" y1="120" x2="300" y2="120"/>
    <line x1="40" y1="95"  x2="300" y2="95"/> <line x1="40" y1="70"  x2="300" y2="70"/>
    <line x1="40" y1="45"  x2="300" y2="45"/> <line x1="40" y1="20"  x2="300" y2="20"/>
  </g>
  <g stroke="#333" stroke-width="1.4">
    <line x1="40" y1="170" x2="312" y2="170"/><line x1="40" y1="170" x2="40" y2="16"/>
  </g>
  <polyline points="40,170 144,70 196,70 300,170"
            fill="none" stroke="#4f46e5" stroke-width="2.2"/>
  <g fill="#4f46e5"><circle cx="40" cy="170" r="2.6"/><circle cx="144" cy="70" r="2.6"/>
     <circle cx="196" cy="70" r="2.6"/><circle cx="300" cy="170" r="2.6"/></g>
  <g fill="#333" text-anchor="middle">
    <text x="40" y="183">0</text><text x="92" y="183">1</text><text x="144" y="183">2</text>
    <text x="196" y="183">3</text><text x="248" y="183">4</text><text x="300" y="183">5</text>
    <text x="175" y="198" font-size="9.5">Time (hours)</text>
  </g>
  <g fill="#333" text-anchor="end">
    <text x="34" y="173">0</text><text x="34" y="148">20</text><text x="34" y="123">40</text>
    <text x="34" y="98">60</text><text x="34" y="73">80</text><text x="34" y="48">100</text>
    <text x="34" y="23">120</text>
  </g>
  <text x="14" y="95" fill="#333" font-size="9.5" text-anchor="middle"
        transform="rotate(-90 14 95)">Distance (km)</text>
</svg>
"""

VT_GRAPH = """
<svg width="340" height="205" viewBox="0 0 340 205" xmlns="http://www.w3.org/2000/svg"
     font-family="Arial, Helvetica, sans-serif" font-size="9">
  <g stroke="#dbe0ea" stroke-width="1">
    <line x1="85"  y1="20" x2="85"  y2="170"/><line x1="130" y1="20" x2="130" y2="170"/>
    <line x1="175" y1="20" x2="175" y2="170"/><line x1="220" y1="20" x2="220" y2="170"/>
    <line x1="265" y1="20" x2="265" y2="170"/><line x1="310" y1="20" x2="310" y2="170"/>
    <line x1="40" y1="140" x2="310" y2="140"/><line x1="40" y1="110" x2="310" y2="110"/>
    <line x1="40" y1="80"  x2="310" y2="80"/> <line x1="40" y1="50"  x2="310" y2="50"/>
    <line x1="40" y1="20"  x2="310" y2="20"/>
  </g>
  <g stroke="#333" stroke-width="1.4">
    <line x1="40" y1="170" x2="322" y2="170"/><line x1="40" y1="170" x2="40" y2="16"/>
  </g>
  <polyline points="40,170 112,50 220,50 310,170"
            fill="none" stroke="#4f46e5" stroke-width="2.2"/>
  <g fill="#4f46e5"><circle cx="40" cy="170" r="2.6"/><circle cx="112" cy="50" r="2.6"/>
     <circle cx="220" cy="50" r="2.6"/><circle cx="310" cy="170" r="2.6"/></g>
  <g fill="#333" text-anchor="middle">
    <text x="40" y="183">0</text><text x="85" y="183">5</text><text x="130" y="183">10</text>
    <text x="175" y="183">15</text><text x="220" y="183">20</text><text x="265" y="183">25</text>
    <text x="310" y="183">30</text>
    <text x="180" y="198" font-size="9.5">Time (seconds)</text>
  </g>
  <g fill="#333" text-anchor="end">
    <text x="34" y="173">0</text><text x="34" y="143">5</text><text x="34" y="113">10</text>
    <text x="34" y="83">15</text><text x="34" y="53">20</text><text x="34" y="23">25</text>
  </g>
  <text x="14" y="95" fill="#333" font-size="9.5" text-anchor="middle"
        transform="rotate(-90 14 95)">Speed (m/s)</text>
</svg>
"""

PAPER = {
    "title": "Graphs",
    "folder": "gcse/graphs",
    "slug": "graphs-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write down the gradient of the line with equation <i>y</i> = 3<i>x</i> &minus; 5</p>",
            "steps": [
                "A straight line written as <i>y</i> = m<i>x</i> + c has gradient m.",
                "Here the number multiplying <i>x</i> is 3.",
            ],
            "answer": "3",
        },
        {
            "marks": 2,
            "q": "<p>A straight line has equation <i>y</i> = 2<i>x</i> + 1</p>"
                 "<p class='part'>(a) Write down the gradient of the line.</p>"
                 "<p class='part'>(b) Write down the coordinates of the point where the line crosses the <i>y</i>-axis.</p>",
            "steps": [
                "Compare with <i>y</i> = m<i>x</i> + c, where m is the gradient and c is the <i>y</i>-intercept.",
                "<b>(a)</b> m = 2",
                "<b>(b)</b> c = 1, and the line crosses the <i>y</i>-axis where <i>x</i> = 0, so the point is (0, 1)",
            ],
            "answer": "(a) 2 &nbsp;&nbsp; (b) (0, 1)",
        },
        {
            "marks": 2,
            "q": "<p>Does the point (3, 7) lie on the line <i>y</i> = 2<i>x</i> + 1?</p>"
                 "<p>You must show your working.</p>",
            "steps": [
                "Substitute the <i>x</i>-coordinate into the equation and see whether you get the <i>y</i>-coordinate.",
                "<i>x</i> = 3 gives <i>y</i> = 2 &times; 3 + 1 = 7",
                "This matches the <i>y</i>-coordinate of the point, so (3, 7) is on the line.",
            ],
            "answer": "Yes &mdash; when <i>x</i> = 3, <i>y</i> = 2(3) + 1 = 7",
        },
        {
            "marks": 3,
            "q": "<p>Complete the table of values for <i>y</i> = 2<i>x</i> &minus; 3</p>"
                 "<table class='d'><tr><th><i>x</i></th><td>&minus;1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr>"
                 "<tr><th><i>y</i></th><td>&nbsp;</td><td>&minus;3</td><td>&nbsp;</td><td>1</td><td>&nbsp;</td></tr></table>",
            "steps": [
                "Substitute each <i>x</i>-value into <i>y</i> = 2<i>x</i> &minus; 3 in turn.",
                "<i>x</i> = &minus;1: <i>y</i> = 2(&minus;1) &minus; 3 = &minus;2 &minus; 3 = &minus;5",
                "<i>x</i> = 1: <i>y</i> = 2(1) &minus; 3 = &minus;1",
                "<i>x</i> = 3: <i>y</i> = 2(3) &minus; 3 = 3",
                "Sensible check: the <i>y</i>-values go up by 2 each time, matching the gradient of 2.",
            ],
            "answer": "&minus;5, &minus;3, &minus;1, 1, 3",
        },
        {
            "marks": 3,
            "q": "<p>A is the point (1, 2) and B is the point (7, 10).</p>"
                 "<p class='part'>(a) Write down the coordinates of the midpoint of AB.</p>"
                 "<p class='part'>(b) Work out the gradient of the line AB.</p>",
            "steps": [
                "<b>(a)</b> The midpoint is the average of the coordinates.",
                "<i>x</i>: (1 + 7) &divide; 2 = 4 and <i>y</i>: (2 + 10) &divide; 2 = 6, so the midpoint is (4, 6)",
                "<b>(b)</b> Gradient = " + frac("change in <i>y</i>", "change in <i>x</i>"),
                "Change in <i>y</i> = 10 &minus; 2 = 8 and change in <i>x</i> = 7 &minus; 1 = 6",
                "Gradient = " + frac("8", "6") + " = " + frac("4", "3"),
            ],
            "answer": "(a) (4, 6) &nbsp;&nbsp; (b) " + frac("4", "3"),
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Find the equation of the line with gradient &minus;2 that passes through (0, 4).</p>"
                 "<p class='part'>(b) Is your line parallel to <i>y</i> = &minus;2<i>x</i> + 9? Give a reason.</p>",
            "steps": [
                "<b>(a)</b> Use <i>y</i> = m<i>x</i> + c with m = &minus;2.",
                "The point (0, 4) is on the <i>y</i>-axis, so it gives the intercept directly: c = 4",
                "The equation is <i>y</i> = &minus;2<i>x</i> + 4",
                "<b>(b)</b> Parallel lines have equal gradients.",
                "Both lines have gradient &minus;2, so yes, they are parallel (they just cross the <i>y</i>-axis at different points).",
            ],
            "answer": "(a) <i>y</i> = &minus;2<i>x</i> + 4 &nbsp;&nbsp; (b) Yes &mdash; both have gradient &minus;2",
        },
        {
            "marks": 3,
            "q": "<p>A taxi firm charges a fixed fee of &pound;3 plus &pound;2 for every mile travelled.</p>"
                 "<p class='part'>(a) Write a formula for the cost C pounds of a journey of m miles.</p>"
                 "<p class='part'>(b) Work out the cost of a 7 mile journey.</p>"
                 "<p class='part'>(c) If the formula is drawn as a graph, what does the number 3 tell you?</p>",
            "steps": [
                "<b>(a)</b> The mileage part is 2 &times; m and the fixed fee is added on: C = 2m + 3",
                "<b>(b)</b> Substitute m = 7: C = 2 &times; 7 + 3 = 14 + 3 = 17",
                "So the journey costs &pound;17",
                "<b>(c)</b> The 3 is the value of C when m = 0, so it is the <i>y</i>-intercept of the graph &mdash; the fixed charge you pay before travelling any distance.",
            ],
            "answer": "(a) C = 2m + 3 &nbsp;&nbsp; (b) &pound;17 &nbsp;&nbsp; (c) it is the <i>y</i>-intercept &mdash; the fixed charge",
        },
        {
            "marks": 3,
            "q": "<p>The distance&ndash;time graph shows a cyclist&rsquo;s journey away from home and back again.</p>"
                 + DT_GRAPH +
                 "<p class='part'>(a) How far had the cyclist travelled after 2 hours?</p>"
                 "<p class='part'>(b) For how long did the cyclist stop?</p>"
                 "<p class='part'>(c) Work out the cyclist&rsquo;s speed during the first stage of the journey.</p>",
            "steps": [
                "<b>(a)</b> Read up from 2 hours to the graph, then across to the distance axis: 80 km",
                "<b>(b)</b> A horizontal section means the distance is not changing, so the cyclist is stopped.",
                "The flat part runs from 2 hours to 3 hours, so the stop lasted 1 hour.",
                "<b>(c)</b> On a distance&ndash;time graph, speed is the gradient.",
                "Speed = " + frac("80 km", "2 hours") + " = 40 km/h",
            ],
            "answer": "(a) 80 km &nbsp;&nbsp; (b) 1 hour &nbsp;&nbsp; (c) 40 km/h",
        },
        {
            "marks": 4,
            "q": "<p>A straight line L passes through the points (1, 5) and (4, 14).</p>"
                 "<p>Find the equation of L.</p>",
            "steps": [
                "First find the gradient: m = " + frac("14 &minus; 5", "4 &minus; 1") + " = " + frac("9", "3") + " = 3",
                "Now use <i>y</i> = 3<i>x</i> + c and substitute one of the points.",
                "Using (1, 5): 5 = 3 &times; 1 + c",
                "So c = 5 &minus; 3 = 2",
                "The equation is <i>y</i> = 3<i>x</i> + 2",
                "Check with the other point: 3 &times; 4 + 2 = 14 &#10003;",
            ],
            "answer": "<i>y</i> = 3<i>x</i> + 2",
        },
        {
            "marks": 4,
            "q": "<p>Two mobile phone tariffs are available.</p>"
                 "<p class='part'><b>Plan A:</b> &pound;10 per month plus 5p for each minute of calls.</p>"
                 "<p class='part'><b>Plan B:</b> no monthly fee, 15p for each minute of calls.</p>"
                 "<p class='part'>(a) Write a formula for the monthly cost, in pounds, of each plan for m minutes of calls.</p>"
                 "<p class='part'>(b) Find the number of minutes for which the two plans cost the same.</p>"
                 "<p class='part'>(c) Which plan is cheaper for someone who talks for 150 minutes a month? Show your working.</p>",
            "steps": [
                "<b>(a)</b> Work in pounds, so 5p = &pound;0.05 and 15p = &pound;0.15",
                "Plan A: C = 0.05m + 10 &nbsp; and &nbsp; Plan B: C = 0.15m",
                "<b>(b)</b> The plans cost the same where the two graphs cross, so set the formulas equal: 0.05m + 10 = 0.15m",
                "Subtract 0.05m from both sides: 10 = 0.1m, so m = 100 minutes",
                "<b>(c)</b> Plan A for 150 minutes: 0.05 &times; 150 + 10 = 7.50 + 10 = &pound;17.50",
                "Plan B for 150 minutes: 0.15 &times; 150 = &pound;22.50, so Plan A is cheaper by &pound;5.",
            ],
            "answer": "(a) A: C = 0.05m + 10, B: C = 0.15m &nbsp;&nbsp; (b) 100 minutes &nbsp;&nbsp; (c) Plan A (&pound;17.50 against &pound;22.50)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Work out the gradient of the line joining (&minus;2, 1) and (4, 13).</p>",
            "steps": [
                "Gradient = " + frac("change in <i>y</i>", "change in <i>x</i>"),
                "Change in <i>y</i> = 13 &minus; 1 = 12 and change in <i>x</i> = 4 &minus; (&minus;2) = 6",
                "Gradient = 12 &divide; 6 = 2",
            ],
            "answer": "2",
        },
        {
            "marks": 2,
            "q": "<p>Rearrange 2<i>y</i> &minus; 6<i>x</i> = 8 into the form <i>y</i> = m<i>x</i> + c and write down the gradient.</p>",
            "steps": [
                "Add 6<i>x</i> to both sides: 2<i>y</i> = 6<i>x</i> + 8",
                "Divide every term by 2: <i>y</i> = 3<i>x</i> + 4",
                "The gradient is the number multiplying <i>x</i>, which is 3.",
            ],
            "answer": "<i>y</i> = 3<i>x</i> + 4, gradient 3",
        },
        {
            "marks": 3,
            "q": "<p>Find the equation of the line that is parallel to <i>y</i> = 3<i>x</i> &minus; 1 and passes through the point (2, 11).</p>",
            "steps": [
                "Parallel lines have the same gradient, so the new line is <i>y</i> = 3<i>x</i> + c",
                "Substitute the point (2, 11): 11 = 3 &times; 2 + c",
                "11 = 6 + c, so c = 5",
                "The equation is <i>y</i> = 3<i>x</i> + 5",
            ],
            "answer": "<i>y</i> = 3<i>x</i> + 5",
        },
        {
            "marks": 3,
            "q": "<p>Find the equation of the line perpendicular to <i>y</i> = 2<i>x</i> + 3 that passes through the point (4, 1).</p>",
            "steps": [
                "Perpendicular gradients multiply to &minus;1, so the new gradient is &minus;" + frac("1", "2"),
                "The line is <i>y</i> = &minus;" + frac("1", "2") + "<i>x</i> + c",
                "Substitute (4, 1): 1 = &minus;" + frac("1", "2") + " &times; 4 + c = &minus;2 + c",
                "So c = 3 and the equation is <i>y</i> = &minus;" + frac("1", "2") + "<i>x</i> + 3",
            ],
            "answer": "<i>y</i> = &minus;" + frac("1", "2") + "<i>x</i> + 3 &nbsp;(or <i>x</i> + 2<i>y</i> = 6)",
        },
        {
            "marks": 4,
            "q": "<p>The value, &pound;V, of a car after t years is modelled by</p>"
                 "<p>&nbsp;&nbsp;V = 12000 &times; 0.85<sup>t</sup></p>"
                 "<p class='part'>(a) Write down the value of the car when it was new.</p>"
                 "<p class='part'>(b) Work out the value of the car after 3 years.</p>"
                 "<p class='part'>(c) What does the number 0.85 tell you about the value of the car?</p>",
            "steps": [
                "<b>(a)</b> &lsquo;When new&rsquo; means t = 0, and 0.85<sup>0</sup> = 1, so V = 12000",
                "<b>(b)</b> Substitute t = 3: V = 12000 &times; 0.85<sup>3</sup>",
                "0.85<sup>3</sup> = 0.614125",
                "V = 12000 &times; 0.614125 = 7369.5, so the car is worth &pound;7369.50",
                "<b>(c)</b> Each year the value is multiplied by 0.85, which is 85% of the previous year&rsquo;s value.",
                "So the car loses 15% of its value every year &mdash; this is exponential decay, giving a curve that falls steeply then flattens.",
            ],
            "answer": "(a) &pound;12 000 &nbsp;&nbsp; (b) &pound;7369.50 &nbsp;&nbsp; (c) the value falls by 15% each year",
        },
        {
            "marks": 4,
            "q": "<p>The graph of <i>y</i> = f(<i>x</i>) has a minimum point at (2, &minus;3).</p>"
                 "<p>Write down the coordinates of the minimum point of each of these graphs.</p>"
                 "<p class='part'>(a) <i>y</i> = f(<i>x</i>) + 5</p>"
                 "<p class='part'>(b) <i>y</i> = f(<i>x</i> &minus; 3)</p>"
                 "<p class='part'>(c) <i>y</i> = &minus;f(<i>x</i>)</p>"
                 "<p class='part'>(d) <i>y</i> = f(2<i>x</i>)</p>",
            "steps": [
                "<b>(a)</b> Adding 5 <i>outside</i> the function shifts the graph up 5, so only the <i>y</i>-coordinate changes: (2, 2)",
                "<b>(b)</b> Changing <i>x</i> to <i>x</i> &minus; 3 <i>inside</i> the function shifts the graph 3 to the <b>right</b>: (5, &minus;3)",
                "<b>(c)</b> The minus in front reflects the graph in the <i>x</i>-axis, so the <i>y</i>-coordinate changes sign: (2, 3). "
                "(This point is now a maximum.)",
                "<b>(d)</b> f(2<i>x</i>) is a stretch parallel to the <i>x</i>-axis with scale factor "
                + frac("1", "2") + ", so the <i>x</i>-coordinate is halved: (1, &minus;3)",
            ],
            "answer": "(a) (2, 2) &nbsp;&nbsp; (b) (5, &minus;3) &nbsp;&nbsp; (c) (2, 3) &nbsp;&nbsp; (d) (1, &minus;3)",
        },
        {
            "marks": 4,
            "q": "<p>The speed&ndash;time graph shows the first 30 seconds of a car&rsquo;s journey.</p>"
                 + VT_GRAPH +
                 "<p class='part'>(a) Work out the acceleration during the first 8 seconds.</p>"
                 "<p class='part'>(b) Work out the total distance travelled in the 30 seconds.</p>",
            "steps": [
                "<b>(a)</b> On a speed&ndash;time graph the gradient is the acceleration.",
                "The speed rises from 0 to 20 m/s in 8 s, so acceleration = " + frac("20", "8") + " = 2.5 m/s<sup>2</sup>",
                "<b>(b)</b> On a speed&ndash;time graph the <b>area under the graph</b> is the distance travelled.",
                "Split the shape into a triangle, a rectangle and a triangle.",
                "Triangle (0&ndash;8 s): " + frac("1", "2") + " &times; 8 &times; 20 = 80 m",
                "Rectangle (8&ndash;20 s): 12 &times; 20 = 240 m &nbsp;&middot;&nbsp; Triangle (20&ndash;30 s): "
                + frac("1", "2") + " &times; 10 &times; 20 = 100 m",
                "Total = 80 + 240 + 100 = 420 m",
            ],
            "answer": "(a) 2.5 m/s<sup>2</sup> &nbsp;&nbsp; (b) 420 m",
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) Factorise fully <i>x</i><sup>3</sup> &minus; 4<i>x</i></p>"
                 "<p class='part'>(b) Hence write down the coordinates of the three points where the curve "
                 "<i>y</i> = <i>x</i><sup>3</sup> &minus; 4<i>x</i> crosses the <i>x</i>-axis.</p>",
            "steps": [
                "<b>(a)</b> Every term has a factor of <i>x</i>: <i>x</i>(<i>x</i><sup>2</sup> &minus; 4)",
                "The bracket is the difference of two squares: <i>x</i><sup>2</sup> &minus; 4 = (<i>x</i> + 2)(<i>x</i> &minus; 2)",
                "So <i>x</i><sup>3</sup> &minus; 4<i>x</i> = <i>x</i>(<i>x</i> + 2)(<i>x</i> &minus; 2)",
                "<b>(b)</b> The curve meets the <i>x</i>-axis where <i>y</i> = 0, so each factor in turn is zero.",
                "<i>x</i> = 0, <i>x</i> = &minus;2 and <i>x</i> = 2",
            ],
            "answer": "(a) <i>x</i>(<i>x</i> + 2)(<i>x</i> &minus; 2) &nbsp;&nbsp; (b) (&minus;2, 0), (0, 0) and (2, 0)",
        },
        {
            "marks": 4,
            "q": "<p>The line 3<i>x</i> + 4<i>y</i> = 24 crosses the <i>x</i>-axis at A and the <i>y</i>-axis at B. "
                 "O is the origin.</p>"
                 "<p class='part'>(a) Write down the coordinates of A and of B.</p>"
                 "<p class='part'>(b) Work out the length of AB.</p>"
                 "<p class='part'>(c) Work out the area of triangle OAB.</p>",
            "steps": [
                "<b>(a)</b> On the <i>x</i>-axis, <i>y</i> = 0: 3<i>x</i> = 24, so <i>x</i> = 8 and A is (8, 0)",
                "On the <i>y</i>-axis, <i>x</i> = 0: 4<i>y</i> = 24, so <i>y</i> = 6 and B is (0, 6)",
                "<b>(b)</b> OAB is right-angled at O, so use Pythagoras: AB<sup>2</sup> = 8<sup>2</sup> + 6<sup>2</sup> = 64 + 36 = 100",
                "AB = &radic;100 = 10",
                "<b>(c)</b> Area = " + frac("1", "2") + " &times; base &times; height = " + frac("1", "2") + " &times; 8 &times; 6 = 24 square units",
            ],
            "answer": "(a) A(8, 0), B(0, 6) &nbsp;&nbsp; (b) 10 &nbsp;&nbsp; (c) 24 square units",
        },
        {
            "marks": 5,
            "q": "<p>A circle has equation <i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> = 20</p>"
                 "<p>The line <i>y</i> = <i>x</i> &minus; 2 cuts the circle at the points P and Q.</p>"
                 "<p class='part'>(a) Find the coordinates of P and Q.</p>"
                 "<p class='part'>(b) Work out the exact length of PQ, giving your answer in the form a&radic;b.</p>",
            "steps": [
                "<b>(a)</b> Substitute <i>y</i> = <i>x</i> &minus; 2 into the circle equation.",
                "<i>x</i><sup>2</sup> + (<i>x</i> &minus; 2)<sup>2</sup> = 20, and (<i>x</i> &minus; 2)<sup>2</sup> = <i>x</i><sup>2</sup> &minus; 4<i>x</i> + 4",
                "So 2<i>x</i><sup>2</sup> &minus; 4<i>x</i> + 4 = 20, giving 2<i>x</i><sup>2</sup> &minus; 4<i>x</i> &minus; 16 = 0",
                "Divide by 2: <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 8 = 0, which factorises to (<i>x</i> &minus; 4)(<i>x</i> + 2) = 0",
                "<i>x</i> = 4 gives <i>y</i> = 4 &minus; 2 = 2, and <i>x</i> = &minus;2 gives <i>y</i> = &minus;2 &minus; 2 = &minus;4",
                "So the points are (4, 2) and (&minus;2, &minus;4). Check (4, 2): 16 + 4 = 20 &#10003;",
                "<b>(b)</b> Horizontal difference = 4 &minus; (&minus;2) = 6 and vertical difference = 2 &minus; (&minus;4) = 6",
                "PQ<sup>2</sup> = 6<sup>2</sup> + 6<sup>2</sup> = 72, so PQ = &radic;72 = &radic;36 &times; &radic;2 = 6&radic;2",
            ],
            "answer": "(a) P(4, 2) and Q(&minus;2, &minus;4) &nbsp;&nbsp; (b) PQ = 6&radic;2",
        },
    ],
}
