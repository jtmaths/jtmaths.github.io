"""GCSE practice paper — Geometry and Measures (topic level)."""
from build import frac

PARALLEL_LINES = """
<svg width="300" height="180" viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg"
     font-family="Arial, Helvetica, sans-serif" font-size="10">
  <g stroke="#333" stroke-width="1.5" fill="none">
    <line x1="35" y1="45" x2="265" y2="45"/>
    <line x1="35" y1="125" x2="265" y2="125"/>
    <line x1="105" y1="15" x2="215" y2="160" stroke="#4f46e5"/>
  </g>
  <g stroke="#333" stroke-width="1.5" fill="none">
    <path d="M 142 39 L 150 45 L 142 51"/>
    <path d="M 142 119 L 150 125 L 142 131"/>
  </g>
  <g fill="#4f46e5">
    <circle cx="128" cy="45" r="2.8"/><circle cx="188" cy="125" r="2.8"/>
  </g>
  <g fill="#111">
    <text x="26" y="49">A</text><text x="269" y="49">B</text>
    <text x="26" y="129">C</text><text x="269" y="129">D</text>
    <text x="97" y="13">P</text><text x="218" y="167">Q</text>
    <text x="114" y="58">X</text><text x="174" y="140">Y</text>
  </g>
  <g fill="#b91c1c" font-weight="bold">
    <text x="117" y="39" text-anchor="end">62&#176;</text>
  </g>
  <g fill="#166534" font-weight="bold">
    <text x="163" y="119">x</text><text x="206" y="119">y</text>
  </g>
  <text x="150" y="176" fill="#666" font-size="8" text-anchor="middle" font-style="italic">
    Diagram not accurately drawn
  </text>
</svg>
"""

PAPER = {
    "title": "Geometry and Measures",
    "folder": "gcse/geometry",
    "slug": "geometry-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Two angles lie on a straight line. One of them is 130&deg;.</p>"
                 "<p>Work out the size of the other angle.</p>",
            "steps": [
                "Angles on a straight line add up to 180&deg;.",
                "180 &minus; 130 = 50",
            ],
            "answer": "50&deg;",
        },
        {
            "marks": 2,
            "q": "<p class='part'>(a) Work out the area of a triangle with base 10 cm and perpendicular height 6 cm.</p>"
                 "<p class='part'>(b) Work out the area of a parallelogram with base 7 cm and perpendicular height 4 cm.</p>",
            "steps": [
                "<b>(a)</b> Area of a triangle = " + frac("1", "2") + " &times; base &times; height",
                "= " + frac("1", "2") + " &times; 10 &times; 6 = 30 cm<sup>2</sup>",
                "<b>(b)</b> Area of a parallelogram = base &times; height (no halving).",
                "= 7 &times; 4 = 28 cm<sup>2</sup>",
            ],
            "answer": "(a) 30 cm<sup>2</sup> &nbsp;&nbsp; (b) 28 cm<sup>2</sup>",
        },
        {
            "marks": 2,
            "q": "<p>Two angles of a triangle are 55&deg; and 68&deg;.</p>"
                 "<p>Work out the size of the third angle.</p>",
            "steps": [
                "The angles in a triangle add up to 180&deg;.",
                "55 + 68 = 123",
                "180 &minus; 123 = 57",
            ],
            "answer": "57&deg;",
        },
        {
            "marks": 2,
            "q": "<p>A circle has radius 5 cm.</p>"
                 "<p>Work out the circumference of the circle, correct to 1 decimal place.</p>",
            "steps": [
                "Circumference = 2&pi;r (use the radius, not the diameter).",
                "= 2 &times; &pi; &times; 5 = 10&pi;",
                "10 &times; 3.14159&hellip; = 31.4159&hellip;",
            ],
            "answer": "31.4 cm (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>A circle has diameter 12 cm.</p>"
                 "<p>Work out the area of the circle, correct to 1 decimal place.</p>",
            "steps": [
                "The area formula uses the radius, so halve the diameter first: r = 12 &divide; 2 = 6 cm",
                "Area = &pi;r<sup>2</sup> = &pi; &times; 6<sup>2</sup>",
                "= 36&pi;",
                "36 &times; 3.14159&hellip; = 113.097&hellip;",
            ],
            "answer": "113.1 cm<sup>2</sup> (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>Work out the size of one interior angle of a regular octagon.</p>",
            "steps": [
                "The exterior angles of any polygon add up to 360&deg;.",
                "A regular octagon has 8 equal exterior angles: 360 &divide; 8 = 45&deg;",
                "An interior angle and its exterior angle lie on a straight line.",
                "Interior angle = 180 &minus; 45 = 135&deg;",
            ],
            "answer": "135&deg;",
        },
        {
            "marks": 3,
            "q": "<p>A right-angled triangle has the two shorter sides 5 cm and 12 cm.</p>"
                 "<p class='part'>(a) Work out the length of the hypotenuse.</p>"
                 "<p class='part'>(b) Work out the perimeter of the triangle.</p>",
            "steps": [
                "<b>(a)</b> Pythagoras&rsquo; theorem: a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>",
                "5<sup>2</sup> + 12<sup>2</sup> = 25 + 144 = 169",
                "c = &radic;169 = 13 cm",
                "<b>(b)</b> Perimeter = 5 + 12 + 13 = 30 cm",
            ],
            "answer": "(a) 13 cm &nbsp;&nbsp; (b) 30 cm",
        },
        {
            "marks": 3,
            "q": "<p>In the diagram, AB is parallel to CD. The line PQ crosses AB at X and CD at Y.</p>"
                 + PARALLEL_LINES +
                 "<p class='part'>(a) Work out the size of the angle marked <i>x</i>. Give a reason for your answer.</p>"
                 "<p class='part'>(b) Work out the size of the angle marked <i>y</i>. Give a reason for your answer.</p>",
            "steps": [
                "<b>(a)</b> The 62&deg; angle and <i>x</i> are in matching positions at the two crossings &mdash; "
                "both sit above their line and to the left of PQ.",
                "Corresponding angles on parallel lines are equal, so <i>x</i> = 62&deg;",
                "<b>(b)</b> <i>y</i> and <i>x</i> together lie on the straight line CD, so they add to 180&deg;.",
                "<i>y</i> = 180 &minus; 62 = 118&deg;",
            ],
            "answer": "(a) <i>x</i> = 62&deg; (corresponding angles are equal) &nbsp;&nbsp; "
                      "(b) <i>y</i> = 118&deg; (angles on a straight line add to 180&deg;)",
        },
        {
            "marks": 4,
            "q": "<p>A prism has a cross-section that is a right-angled triangle with shorter sides "
                 "6 cm and 8 cm. The prism is 15 cm long.</p>"
                 "<p class='part'>(a) Work out the area of the cross-section.</p>"
                 "<p class='part'>(b) Work out the volume of the prism.</p>"
                 "<p class='part'>(c) Work out the total surface area of the prism.</p>",
            "steps": [
                "<b>(a)</b> Area = " + frac("1", "2") + " &times; 6 &times; 8 = 24 cm<sup>2</sup>",
                "<b>(b)</b> Volume of a prism = area of cross-section &times; length = 24 &times; 15 = 360 cm<sup>3</sup>",
                "<b>(c)</b> First find the third side of the triangle: &radic;(6<sup>2</sup> + 8<sup>2</sup>) = &radic;100 = 10 cm",
                "The two triangular ends give 2 &times; 24 = 48 cm<sup>2</sup>",
                "The three rectangles have a combined width equal to the triangle&rsquo;s perimeter: 6 + 8 + 10 = 24 cm",
                "So the rectangles give 24 &times; 15 = 360 cm<sup>2</sup>, and the total is 48 + 360 = 408 cm<sup>2</sup>",
            ],
            "answer": "(a) 24 cm<sup>2</sup> &nbsp;&nbsp; (b) 360 cm<sup>3</sup> &nbsp;&nbsp; (c) 408 cm<sup>2</sup>",
        },
        {
            "marks": 4,
            "q": "<p>A shape is made from a rectangle 12 cm by 8 cm with a semicircle of diameter 8 cm "
                 "cut out of one of the shorter ends.</p>"
                 "<p>Work out the area of the shape that is left, correct to 1 decimal place.</p>",
            "steps": [
                "Work out the two areas separately and subtract.",
                "Rectangle: 12 &times; 8 = 96 cm<sup>2</sup>",
                "The semicircle has diameter 8 cm, so its radius is 4 cm.",
                "Area of a full circle = &pi; &times; 4<sup>2</sup> = 16&pi; = 50.265&hellip; cm<sup>2</sup>",
                "A semicircle is half of that: 25.132&hellip; cm<sup>2</sup>",
                "Remaining area = 96 &minus; 25.132&hellip; = 70.867&hellip; cm<sup>2</sup>",
            ],
            "answer": "70.9 cm<sup>2</sup> (1 d.p.)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Work out the sum of the interior angles of a 12-sided polygon.</p>",
            "steps": [
                "The sum of the interior angles of an n-sided polygon is (n &minus; 2) &times; 180&deg;.",
                "Here n = 12, so (12 &minus; 2) &times; 180 = 10 &times; 180",
                "= 1800&deg;",
            ],
            "answer": "1800&deg;",
        },
        {
            "marks": 2,
            "q": "<p>A cylinder has radius 4 cm and height 10 cm.</p>"
                 "<p>Work out its volume, correct to 3 significant figures.</p>",
            "steps": [
                "Volume of a cylinder = &pi;r<sup>2</sup>h",
                "= &pi; &times; 4<sup>2</sup> &times; 10 = 160&pi;",
                "160 &times; 3.14159&hellip; = 502.65&hellip;",
            ],
            "answer": "503 cm<sup>3</sup> (3 s.f.)",
        },
        {
            "marks": 3,
            "q": "<p>A right-angled triangle has hypotenuse 12 cm.</p>"
                 "<p>One of the other angles is 35&deg;.</p>"
                 "<p>Work out the length of the side opposite the 35&deg; angle, to 3 significant figures.</p>",
            "steps": [
                "You know the hypotenuse and want the opposite side, so use sine (SOH).",
                "sin 35&deg; = " + frac("opposite", "12"),
                "Rearrange: opposite = 12 &times; sin 35&deg;",
                "sin 35&deg; = 0.573576&hellip;, so opposite = 12 &times; 0.573576 = 6.8829&hellip;",
            ],
            "answer": "6.88 cm (3 s.f.)",
        },
        {
            "marks": 3,
            "q": "<p>In a right-angled triangle the side opposite angle &theta; is 7 cm and "
                 "the side adjacent to &theta; is 9 cm.</p>"
                 "<p>Work out the size of angle &theta;, correct to 1 decimal place.</p>",
            "steps": [
                "Opposite and adjacent means tangent (TOA).",
                "tan &theta; = " + frac("7", "9") + " = 0.7777&hellip;",
                "To find the angle, use the inverse: &theta; = tan<sup>&minus;1</sup>(0.7777&hellip;)",
                "&theta; = 37.874&hellip;&deg;",
            ],
            "answer": "&theta; = 37.9&deg; (1 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) A, B and C are points on a circle with centre O. The angle AOC "
                 "at the centre is 130&deg;, and B lies on the major arc. Work out the size of angle ABC, "
                 "giving a reason.</p>"
                 "<p class='part'>(b) PQRS is a cyclic quadrilateral. Angle PSR = 115&deg;. "
                 "Work out the size of angle PQR, giving a reason.</p>",
            "steps": [
                "<b>(a)</b> The angle at the centre is twice the angle at the circumference when both stand on the same arc.",
                "Angle ABC = 130 &divide; 2 = 65&deg;",
                "<b>(b)</b> Opposite angles of a cyclic quadrilateral add up to 180&deg;.",
                "Angle PQR = 180 &minus; 115 = 65&deg;",
            ],
            "answer": "(a) 65&deg; &mdash; the angle at the centre is twice the angle at the circumference &nbsp;&nbsp; "
                      "(b) 65&deg; &mdash; opposite angles of a cyclic quadrilateral add to 180&deg;",
        },
        {
            "marks": 4,
            "q": "<p>In triangle ABC, angle A = 42&deg;, angle B = 68&deg; and side a (opposite A) = 9 cm.</p>"
                 "<p>Work out the length of side b, correct to 3 significant figures.</p>",
            "steps": [
                "You have two angles and the side opposite one of them, so use the sine rule.",
                frac("a", "sin A") + " = " + frac("b", "sin B"),
                "Substitute: " + frac("9", "sin 42&deg;") + " = " + frac("b", "sin 68&deg;"),
                "Rearrange: b = " + frac("9 &times; sin 68&deg;", "sin 42&deg;"),
                "sin 68&deg; = 0.927184 and sin 42&deg; = 0.669131",
                "b = " + frac("9 &times; 0.927184", "0.669131") + " = " + frac("8.34465", "0.669131") + " = 12.470&hellip;",
            ],
            "answer": "b = 12.5 cm (3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>A triangle has two sides of length 7 cm and 9 cm with an angle of 58&deg; between them.</p>"
                 "<p class='part'>(a) Work out the length of the third side, to 3 significant figures.</p>"
                 "<p class='part'>(b) Work out the area of the triangle, to 3 significant figures.</p>",
            "steps": [
                "<b>(a)</b> Two sides and the angle between them means the cosine rule: "
                "c<sup>2</sup> = a<sup>2</sup> + b<sup>2</sup> &minus; 2ab cos C",
                "c<sup>2</sup> = 7<sup>2</sup> + 9<sup>2</sup> &minus; 2 &times; 7 &times; 9 &times; cos 58&deg;",
                "= 49 + 81 &minus; 126 &times; 0.529919 = 130 &minus; 66.769&hellip; = 63.230&hellip;",
                "c = &radic;63.230&hellip; = 7.951&hellip; cm",
                "<b>(b)</b> Area = " + frac("1", "2") + "ab sin C = " + frac("1", "2") + " &times; 7 &times; 9 &times; sin 58&deg;",
                "= 31.5 &times; 0.848048 = 26.713&hellip; cm<sup>2</sup>",
            ],
            "answer": "(a) 7.95 cm &nbsp;&nbsp; (b) 26.7 cm<sup>2</sup> (both 3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>A sector of a circle has radius 9 cm and angle 140&deg;.</p>"
                 "<p class='part'>(a) Work out the length of the arc, to 3 significant figures.</p>"
                 "<p class='part'>(b) Work out the area of the sector, to 3 significant figures.</p>",
            "steps": [
                "A sector is a fraction " + frac("140", "360") + " of the whole circle.",
                "<b>(a)</b> Full circumference = 2 &times; &pi; &times; 9 = 18&pi; = 56.5487&hellip; cm",
                "Arc = " + frac("140", "360") + " &times; 56.5487&hellip; = 21.991&hellip; cm",
                "<b>(b)</b> Full area = &pi; &times; 9<sup>2</sup> = 81&pi; = 254.469&hellip; cm<sup>2</sup>",
                "Sector area = " + frac("140", "360") + " &times; 254.469&hellip; = 98.960&hellip; cm<sup>2</sup>",
            ],
            "answer": "(a) 22.0 cm &nbsp;&nbsp; (b) 99.0 cm<sup>2</sup> (both 3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>In triangle OAB, the vector from O to A is <b>a</b> and the vector from O to B is <b>b</b>.</p>"
                 "<p>M is the midpoint of AB. N is the point on OB such that ON : NB = 1 : 2</p>"
                 "<p class='part'>(a) Write the vector from A to B in terms of <b>a</b> and <b>b</b>.</p>"
                 "<p class='part'>(b) Write the vector from O to M in terms of <b>a</b> and <b>b</b>.</p>"
                 "<p class='part'>(c) Write the vector from M to N in terms of <b>a</b> and <b>b</b>.</p>",
            "steps": [
                "<b>(a)</b> To go from A to B, travel back to O then out to B: &minus;<b>a</b> + <b>b</b> = <b>b</b> &minus; <b>a</b>",
                "<b>(b)</b> M is halfway along AB, so from O go to A then half of AB.",
                "OM = <b>a</b> + " + frac("1", "2") + "(<b>b</b> &minus; <b>a</b>) = " + frac("1", "2") + "<b>a</b> + " + frac("1", "2") + "<b>b</b>",
                "<b>(c)</b> ON : NB = 1 : 2 means N is " + frac("1", "3") + " of the way along OB, so ON = " + frac("1", "3") + "<b>b</b>",
                "MN = MO + ON = &minus;OM + ON = &minus;" + frac("1", "2") + "<b>a</b> &minus; " + frac("1", "2") + "<b>b</b> + " + frac("1", "3") + "<b>b</b>",
                "Combine the <b>b</b> terms: &minus;" + frac("1", "2") + " + " + frac("1", "3") + " = &minus;" + frac("1", "6"),
            ],
            "answer": "(a) <b>b</b> &minus; <b>a</b> &nbsp;&nbsp; (b) " + frac("1", "2") + "(<b>a</b> + <b>b</b>) &nbsp;&nbsp; "
                      "(c) &minus;" + frac("1", "2") + "<b>a</b> &minus; " + frac("1", "6") + "<b>b</b>",
        },
        {
            "marks": 5,
            "q": "<p>A cuboid ABCDEFGH measures 8 cm by 6 cm by 5 cm, where ABCD is the "
                 "8 cm by 6 cm base and AE = 5 cm is vertical.</p>"
                 "<p class='part'>(a) Work out the length of the diagonal AG that runs from one corner of the "
                 "base to the opposite corner of the top. Give your answer to 3 significant figures.</p>"
                 "<p class='part'>(b) Work out the angle that AG makes with the base ABCD, to 1 decimal place.</p>",
            "steps": [
                "<b>(a)</b> Work in two stages. First find the diagonal AC across the base using Pythagoras.",
                "AC<sup>2</sup> = 8<sup>2</sup> + 6<sup>2</sup> = 64 + 36 = 100, so AC = 10 cm",
                "Now AG is the hypotenuse of the right-angled triangle ACG, where CG = 5 cm is vertical.",
                "AG<sup>2</sup> = AC<sup>2</sup> + CG<sup>2</sup> = 100 + 25 = 125, so AG = &radic;125 = 11.180&hellip; cm",
                "<b>(b)</b> The required angle is GAC, inside that same right-angled triangle.",
                "The side opposite is CG = 5 and the side adjacent is AC = 10, so tan(GAC) = " + frac("5", "10") + " = 0.5",
                "GAC = tan<sup>&minus;1</sup>(0.5) = 26.565&hellip;&deg;",
            ],
            "answer": "(a) 11.2 cm (3 s.f.) &nbsp;&nbsp; (b) 26.6&deg; (1 d.p.)",
        },
    ],
}
