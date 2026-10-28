"""GCSE practice papers — major Geometry and Measures subtopics."""
from build import col, frac

ANGLES = {
    "title": "Angle Rules and Polygons",
    "folder": "gcse/geometry",
    "slug": "angle-rules-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Two angles lie on a straight line. One is 115&deg;.</p>"
                 "<p>Work out the other angle.</p>",
            "steps": [
                "Angles on a straight line add up to 180&deg;.",
                "180 &minus; 115 = 65",
            ],
            "answer": "65&deg;",
        },
        {
            "marks": 2,
            "q": "<p>Three angles meet at a point. Two of them are 90&deg; and 130&deg;.</p>"
                 "<p>Work out the third angle.</p>",
            "steps": [
                "Angles around a point add up to 360&deg;.",
                "90 + 130 = 220",
                "360 &minus; 220 = 140",
            ],
            "answer": "140&deg;",
        },
        {
            "marks": 2,
            "q": "<p>Two straight lines cross. One of the angles formed is 72&deg;.</p>"
                 "<p class='part'>(a) Write down the angle vertically opposite it.</p>"
                 "<p class='part'>(b) Work out one of the other two angles.</p>",
            "steps": [
                "<b>(a)</b> Vertically opposite angles are equal, so it is 72&deg;.",
                "<b>(b)</b> The other angles lie on a straight line with the 72&deg; angle.",
                "180 &minus; 72 = 108&deg;",
            ],
            "answer": "(a) 72&deg; &nbsp;&nbsp; (b) 108&deg;",
        },
        {
            "marks": 2,
            "q": "<p>A triangle has angles of 43&deg; and 90&deg;.</p><p>Work out the third angle.</p>",
            "steps": [
                "The angles of a triangle add up to 180&deg;.",
                "43 + 90 = 133",
                "180 &minus; 133 = 47",
            ],
            "answer": "47&deg;",
        },
        {
            "marks": 3,
            "q": "<p>An isosceles triangle has an apex angle of 40&deg;.</p>"
                 "<p>Work out the size of each of the two base angles.</p>",
            "steps": [
                "In an isosceles triangle the two base angles are equal.",
                "The three angles total 180&deg;, so the two base angles share 180 &minus; 40 = 140&deg;.",
                "140 &divide; 2 = 70&deg; each.",
            ],
            "answer": "70&deg; each",
        },
        {
            "marks": 3,
            "q": "<p>A quadrilateral has angles of 85&deg;, 100&deg;, 120&deg; and <i>x</i>&deg;.</p>"
                 "<p>Work out the value of <i>x</i>.</p>",
            "steps": [
                "The angles of a quadrilateral add up to 360&deg;.",
                "85 + 100 + 120 = 305",
                "<i>x</i> = 360 &minus; 305 = 55",
            ],
            "answer": "<i>x</i> = 55",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Work out the size of one exterior angle of a regular pentagon.</p>"
                 "<p class='part'>(b) Work out the size of one interior angle of a regular pentagon.</p>",
            "steps": [
                "<b>(a)</b> The exterior angles of any polygon add up to 360&deg;.",
                "For a regular pentagon: 360 &divide; 5 = 72&deg;",
                "<b>(b)</b> An interior angle and its exterior angle lie on a straight line.",
                "180 &minus; 72 = 108&deg;",
            ],
            "answer": "(a) 72&deg; &nbsp;&nbsp; (b) 108&deg;",
        },
        {
            "marks": 3,
            "q": "<p>Two parallel lines are crossed by a straight line. One of the angles formed at the first "
                 "crossing is 118&deg;.</p>"
                 "<p class='part'>(a) Write down the size of the corresponding angle at the second crossing, "
                 "with a reason.</p>"
                 "<p class='part'>(b) Work out the size of the co-interior angle, with a reason.</p>",
            "steps": [
                "<b>(a)</b> Corresponding angles (in the same position at each crossing) are equal on "
                "parallel lines.",
                "So the corresponding angle is 118&deg;.",
                "<b>(b)</b> Co-interior angles lie between the parallel lines on the same side of the crossing "
                "line and add up to 180&deg;.",
                "180 &minus; 118 = 62&deg;",
            ],
            "answer": "(a) 118&deg; (corresponding angles are equal) &nbsp;&nbsp; "
                      "(b) 62&deg; (co-interior angles add to 180&deg;)",
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) Work out the sum of the interior angles of a hexagon.</p>"
                 "<p class='part'>(b) Five of the angles of a hexagon are 100&deg;, 120&deg;, 130&deg;, 140&deg; "
                 "and 110&deg;. Work out the sixth angle.</p>",
            "steps": [
                "<b>(a)</b> Sum of interior angles = (n &minus; 2) &times; 180&deg; with n = 6",
                "= 4 &times; 180 = 720&deg;",
                "<b>(b)</b> Add the five known angles: 100 + 120 + 130 + 140 + 110 = 600",
                "720 &minus; 600 = 120&deg;",
            ],
            "answer": "(a) 720&deg; &nbsp;&nbsp; (b) 120&deg;",
        },
        {
            "marks": 4,
            "q": "<p>A regular polygon has an exterior angle of 24&deg;.</p>"
                 "<p class='part'>(a) How many sides does it have?</p>"
                 "<p class='part'>(b) Work out one interior angle.</p>"
                 "<p class='part'>(c) Work out the sum of its interior angles.</p>",
            "steps": [
                "<b>(a)</b> The exterior angles total 360&deg;, so the number of sides is 360 &divide; 24 = 15",
                "<b>(b)</b> Interior angle = 180 &minus; 24 = 156&deg;",
                "<b>(c)</b> Sum = (15 &minus; 2) &times; 180 = 13 &times; 180 = 2340&deg;",
                "Check: 15 &times; 156 = 2340 &#10003;",
            ],
            "answer": "(a) 15 sides &nbsp;&nbsp; (b) 156&deg; &nbsp;&nbsp; (c) 2340&deg;",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Work out the sum of the interior angles of a decagon (10 sides).</p>",
            "steps": [
                "Sum = (n &minus; 2) &times; 180&deg; = (10 &minus; 2) &times; 180",
                "= 8 &times; 180 = 1440&deg;",
            ],
            "answer": "1440&deg;",
        },
        {
            "marks": 2,
            "q": "<p>A regular polygon has an interior angle of 162&deg;.</p>"
                 "<p>How many sides does it have?</p>",
            "steps": [
                "Exterior angle = 180 &minus; 162 = 18&deg;",
                "Number of sides = 360 &divide; 18 = 20",
            ],
            "answer": "20 sides",
        },
        {
            "marks": 3,
            "q": "<p>In a regular polygon, each interior angle is 4 times the size of each exterior angle.</p>"
                 "<p>How many sides does the polygon have?</p>",
            "steps": [
                "Let the exterior angle be e, so the interior angle is 4e.",
                "They lie on a straight line: e + 4e = 180",
                "5e = 180, so e = 36&deg;",
                "Number of sides = 360 &divide; 36 = 10",
            ],
            "answer": "10 sides",
        },
        {
            "marks": 3,
            "q": "<p>The angles of a triangle are (3<i>x</i> &minus; 10)&deg;, (2<i>x</i> + 20)&deg; and "
                 "(<i>x</i> + 50)&deg;.</p>"
                 "<p>Work out the size of each angle.</p>",
            "steps": [
                "Add them and set equal to 180: 3<i>x</i> + 2<i>x</i> + <i>x</i> = 6<i>x</i> and &minus;10 + 20 + 50 = 60",
                "6<i>x</i> + 60 = 180, so 6<i>x</i> = 120 and <i>x</i> = 20",
                "The angles are 3(20) &minus; 10 = 50&deg;, 2(20) + 20 = 60&deg; and 20 + 50 = 70&deg;",
                "Check: 50 + 60 + 70 = 180 &#10003;",
            ],
            "answer": "50&deg;, 60&deg; and 70&deg;",
        },
        {
            "marks": 4,
            "q": "<p>Prove that the exterior angle of a triangle is equal to the sum of the two interior "
                 "angles at the other two vertices.</p>",
            "steps": [
                "Call the three interior angles a, b and c, and let the exterior angle at the c vertex be e.",
                "The angles of a triangle add up to 180&deg;, so a + b + c = 180",
                "The interior angle c and the exterior angle e lie on a straight line, so c + e = 180",
                "From the second equation, e = 180 &minus; c",
                "From the first equation, a + b = 180 &minus; c",
                "Both expressions equal 180 &minus; c, so e = a + b as required.",
            ],
            "answer": "e = 180 &minus; c = a + b",
        },
        {
            "marks": 4,
            "q": "<p>A regular hexagon, a square and one other regular polygon fit together exactly around "
                 "a point, with no gaps.</p>"
                 "<p>How many sides does the third polygon have?</p>",
            "steps": [
                "Interior angle of a regular hexagon = 180 &minus; (360 &divide; 6) = 120&deg;",
                "Interior angle of a square = 90&deg;",
                "Angles around a point total 360&deg;, so the third angle is 360 &minus; 120 &minus; 90 = 150&deg;",
                "Its exterior angle is 180 &minus; 150 = 30&deg;",
                "Number of sides = 360 &divide; 30 = 12",
            ],
            "answer": "12 sides",
        },
        {
            "marks": 4,
            "q": "<p>A regular octagon and a regular pentagon are placed so that they share one complete side.</p>"
                 "<p>Work out the size of the angle between them at one of the shared vertices, measured "
                 "outside both shapes.</p>",
            "steps": [
                "Interior angle of a regular octagon = 180 &minus; (360 &divide; 8) = 180 &minus; 45 = 135&deg;",
                "Interior angle of a regular pentagon = 180 &minus; (360 &divide; 5) = 180 &minus; 72 = 108&deg;",
                "At the shared vertex, the two interior angles and the outside angle fit around a point.",
                "Outside angle = 360 &minus; 135 &minus; 108",
                "= 117&deg;",
            ],
            "answer": "117&deg;",
        },
        {
            "marks": 4,
            "q": "<p>The five interior angles of a pentagon are <i>x</i>&deg;, (<i>x</i> + 20)&deg;, "
                 "(<i>x</i> + 30)&deg;, (<i>x</i> + 40)&deg; and (<i>x</i> + 50)&deg;.</p>"
                 "<p>Work out the size of the largest angle.</p>",
            "steps": [
                "Sum of the interior angles of a pentagon = (5 &minus; 2) &times; 180 = 540&deg;",
                "Adding the expressions: 5<i>x</i> + (20 + 30 + 40 + 50) = 5<i>x</i> + 140",
                "5<i>x</i> + 140 = 540, so 5<i>x</i> = 400 and <i>x</i> = 80",
                "The largest angle is <i>x</i> + 50 = 130&deg;",
                "Check: 80 + 100 + 110 + 120 + 130 = 540 &#10003;",
            ],
            "answer": "130&deg;",
        },
        {
            "marks": 4,
            "q": "<p>Prove, using the properties of parallel lines, that the angles of a triangle add up "
                 "to 180&deg;.</p>",
            "steps": [
                "Take triangle ABC with interior angles a at A, b at B and c at C.",
                "Draw a line through C parallel to AB.",
                "The angle between that line and CA (on the A side) equals a, because alternate angles on "
                "parallel lines are equal.",
                "Likewise the angle between the line and CB equals b, again by alternate angles.",
                "Those two angles together with c lie on a straight line through C, so they add up to 180&deg;.",
                "Therefore a + b + c = 180&deg;.",
            ],
            "answer": "Drawing a parallel line through one vertex gives two alternate angles equal to a and b, "
                      "and a + b + c is then a straight line = 180&deg;",
        },
        {
            "marks": 5,
            "q": "<p>In a regular polygon, each interior angle is 20&deg; more than 7 times each "
                 "exterior angle.</p>"
                 "<p class='part'>(a) How many sides does the polygon have?</p>"
                 "<p class='part'>(b) Work out the size of one interior angle.</p>"
                 "<p class='part'>(c) Work out the sum of the interior angles.</p>",
            "steps": [
                "<b>(a)</b> Let the exterior angle be e, so the interior angle is 7e + 20.",
                "Interior and exterior angles lie on a straight line: e + 7e + 20 = 180",
                "8e = 160, so e = 20&deg;",
                "Number of sides = 360 &divide; 20 = 18",
                "<b>(b)</b> Interior angle = 180 &minus; 20 = 160&deg; (check: 7 &times; 20 + 20 = 160 &#10003;)",
                "<b>(c)</b> Sum = (18 &minus; 2) &times; 180 = 16 &times; 180 = 2880&deg;",
            ],
            "answer": "(a) 18 sides &nbsp;&nbsp; (b) 160&deg; &nbsp;&nbsp; (c) 2880&deg;",
        },
    ],
}

PYTHAG_TRIG = {
    "title": "Pythagoras and Trigonometry",
    "folder": "gcse/geometry",
    "slug": "pythagoras-trig-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Complete Pythagoras&rsquo; theorem for a right-angled triangle with shorter sides "
                 "a and b and hypotenuse c.</p>"
                 "<p>&nbsp;&nbsp;a<sup>2</sup> + &#9633; = &#9633;</p>",
            "steps": [
                "The two shorter sides squared add up to the hypotenuse squared.",
                "The hypotenuse is always the longest side, opposite the right angle.",
            ],
            "answer": "a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>",
        },
        {
            "marks": 2,
            "q": "<p>A right-angled triangle has shorter sides 6 cm and 8 cm.</p>"
                 "<p>Work out the length of the hypotenuse.</p>",
            "steps": [
                "6<sup>2</sup> + 8<sup>2</sup> = 36 + 64 = 100",
                "Hypotenuse = &radic;100 = 10 cm",
            ],
            "answer": "10 cm",
        },
        {
            "marks": 2,
            "q": "<p>A right-angled triangle has shorter sides 9 cm and 12 cm.</p>"
                 "<p>Work out the length of the hypotenuse.</p>",
            "steps": [
                "9<sup>2</sup> + 12<sup>2</sup> = 81 + 144 = 225",
                "&radic;225 = 15 cm",
            ],
            "answer": "15 cm",
        },
        {
            "marks": 2,
            "q": "<p>A right-angled triangle has hypotenuse 13 cm and one shorter side 5 cm.</p>"
                 "<p>Work out the length of the other shorter side.</p>",
            "steps": [
                "To find a shorter side you <b>subtract</b>: 13<sup>2</sup> &minus; 5<sup>2</sup>",
                "169 &minus; 25 = 144",
                "&radic;144 = 12 cm",
            ],
            "answer": "12 cm",
        },
        {
            "marks": 3,
            "q": "<p>A right-angled triangle has shorter sides 7 cm and 10 cm.</p>"
                 "<p>Work out the hypotenuse, correct to 1 decimal place.</p>",
            "steps": [
                "7<sup>2</sup> + 10<sup>2</sup> = 49 + 100 = 149",
                "&radic;149 = 12.2065&hellip;",
                "Rounded to 1 decimal place that is 12.2 cm.",
            ],
            "answer": "12.2 cm (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>A right-angled triangle has hypotenuse 15 cm and one shorter side 9 cm.</p>"
                 "<p class='part'>(a) Work out the other shorter side.</p>"
                 "<p class='part'>(b) Work out the area of the triangle.</p>",
            "steps": [
                "<b>(a)</b> 15<sup>2</sup> &minus; 9<sup>2</sup> = 225 &minus; 81 = 144, so the side is &radic;144 = 12 cm",
                "<b>(b)</b> The two shorter sides are perpendicular, so use them as base and height.",
                "Area = " + frac("1", "2") + " &times; 9 &times; 12 = 54 cm<sup>2</sup>",
            ],
            "answer": "(a) 12 cm &nbsp;&nbsp; (b) 54 cm<sup>2</sup>",
        },
        {
            "marks": 3,
            "q": "<p>In a right-angled triangle the hypotenuse is 10 cm and one angle is 40&deg;.</p>"
                 "<p>Work out the side opposite the 40&deg; angle, to 1 decimal place.</p>",
            "steps": [
                "You know the hypotenuse and want the opposite side, so use sine.",
                "sin 40&deg; = " + frac("opposite", "10"),
                "opposite = 10 &times; sin 40&deg; = 10 &times; 0.642787&hellip;",
                "= 6.4278&hellip; cm",
            ],
            "answer": "6.4 cm (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>In a right-angled triangle the hypotenuse is 12 cm and one angle is 25&deg;.</p>"
                 "<p>Work out the side adjacent to the 25&deg; angle, to 1 decimal place.</p>",
            "steps": [
                "Hypotenuse and adjacent means cosine.",
                "cos 25&deg; = " + frac("adjacent", "12"),
                "adjacent = 12 &times; cos 25&deg; = 12 &times; 0.906307&hellip;",
                "= 10.8757&hellip; cm",
            ],
            "answer": "10.9 cm (1 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>In a right-angled triangle, the side opposite angle &theta; is 5 cm and the "
                 "hypotenuse is 9 cm.</p>"
                 "<p>Work out the size of angle &theta;, to 1 decimal place.</p>",
            "steps": [
                "Opposite and hypotenuse means sine.",
                "sin &theta; = " + frac("5", "9") + " = 0.5555&hellip;",
                "To find the angle, use the inverse sine function.",
                "&theta; = sin<sup>&minus;1</sup>(0.5555&hellip;)",
                "= 33.749&hellip;&deg;",
            ],
            "answer": "&theta; = 33.7&deg; (1 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>A ladder of length 5 m leans against a vertical wall. The foot of the ladder is 1.4 m "
                 "from the base of the wall.</p>"
                 "<p class='part'>(a) How far up the wall does the ladder reach? Give your answer to "
                 "1 decimal place.</p>"
                 "<p class='part'>(b) Work out the angle between the ladder and the ground, to 1 decimal place.</p>",
            "steps": [
                "<b>(a)</b> The wall, ground and ladder form a right-angled triangle with the ladder as "
                "the hypotenuse.",
                "height<sup>2</sup> = 5<sup>2</sup> &minus; 1.4<sup>2</sup> = 25 &minus; 1.96 = 23.04",
                "height = &radic;23.04 = 4.8 m exactly",
                "<b>(b)</b> The 1.4 m is adjacent to the angle and the 5 m is the hypotenuse, so use cosine.",
                "cos &theta; = " + frac("1.4", "5") + " = 0.28",
                "&theta; = cos<sup>&minus;1</sup>(0.28) = 73.739&hellip;&deg;",
            ],
            "answer": "(a) 4.8 m &nbsp;&nbsp; (b) 73.7&deg; (1 d.p.)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>A right-angled triangle has hypotenuse 17 cm and one shorter side 8 cm.</p>"
                 "<p>Work out the other shorter side.</p>",
            "steps": [
                "17<sup>2</sup> &minus; 8<sup>2</sup> = 289 &minus; 64 = 225",
                "&radic;225 = 15 cm",
            ],
            "answer": "15 cm",
        },
        {
            "marks": 2,
            "q": "<p>Work out the distance between the points (1, 2) and (5, 5).</p>",
            "steps": [
                "Horizontal difference = 5 &minus; 1 = 4 and vertical difference = 5 &minus; 2 = 3",
                "Distance<sup>2</sup> = 4<sup>2</sup> + 3<sup>2</sup> = 25, so the distance is 5",
            ],
            "answer": "5",
        },
        {
            "marks": 3,
            "q": "<p>In a right-angled triangle the side opposite angle &theta; is 8 cm and the side "
                 "adjacent is 6 cm.</p>"
                 "<p>Work out &theta;, to 1 decimal place.</p>",
            "steps": [
                "Opposite and adjacent means tangent.",
                "tan &theta; = " + frac("8", "6") + " = 1.3333&hellip;",
                "&theta; = tan<sup>&minus;1</sup>(1.3333&hellip;)",
                "= 53.130&hellip;&deg;",
            ],
            "answer": "&theta; = 53.1&deg; (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>Write down the exact value of</p>"
                 "<p class='part'>(a) sin 30&deg; &nbsp;&nbsp; (b) cos 60&deg; &nbsp;&nbsp; (c) tan 45&deg;</p>",
            "steps": [
                "These come from the standard triangles you are expected to know.",
                "<b>(a)</b> sin 30&deg; = " + frac("1", "2"),
                "<b>(b)</b> cos 60&deg; = " + frac("1", "2"),
                "<b>(c)</b> tan 45&deg; = 1",
            ],
            "answer": "(a) " + frac("1", "2") + " &nbsp;&nbsp; (b) " + frac("1", "2") + " &nbsp;&nbsp; (c) 1",
        },
        {
            "marks": 4,
            "q": "<p>A cuboid measures 6 cm by 8 cm by 10 cm.</p>"
                 "<p>Work out the length of the longest straight line that can be drawn inside it, "
                 "to 1 decimal place.</p>",
            "steps": [
                "The longest line is the space diagonal, from one corner to the opposite corner.",
                "First find the diagonal across the 6 by 8 face: 6<sup>2</sup> + 8<sup>2</sup> = 100, so it is 10 cm.",
                "Now use that as one side of a right-angled triangle with the 10 cm edge.",
                "diagonal<sup>2</sup> = 10<sup>2</sup> + 10<sup>2</sup> = 200",
                "&radic;200 = 14.142&hellip; cm",
                "(A shortcut is &radic;(6<sup>2</sup> + 8<sup>2</sup> + 10<sup>2</sup>) = &radic;200.)",
            ],
            "answer": "14.1 cm (1 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>In triangle ABC, angle A = 50&deg;, angle B = 35&deg; and side a (opposite A) = 12 cm.</p>"
                 "<p>Work out side b, to 3 significant figures.</p>",
            "steps": [
                "Two angles and the side opposite one of them means the sine rule.",
                frac("a", "sin A") + " = " + frac("b", "sin B") + ", so b = " + frac("a &times; sin B", "sin A"),
                "sin 35&deg; = 0.573576 and sin 50&deg; = 0.766044",
                "b = " + frac("12 &times; 0.573576", "0.766044") + " = " + frac("6.882917", "0.766044"),
                "= 8.9850&hellip; cm",
            ],
            "answer": "b = 8.99 cm (3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>A triangle has sides 5 cm, 7 cm and 9 cm.</p>"
                 "<p>Work out the size of the largest angle, to 1 decimal place.</p>",
            "steps": [
                "The largest angle is opposite the longest side, so it is opposite the 9 cm side.",
                "Use the cosine rule rearranged: cos C = " + frac("a<sup>2</sup> + b<sup>2</sup> &minus; c<sup>2</sup>", "2ab"),
                "cos C = " + frac("5<sup>2</sup> + 7<sup>2</sup> &minus; 9<sup>2</sup>", "2 &times; 5 &times; 7") + " = " + frac("25 + 49 &minus; 81", "70"),
                "= " + frac("&minus;7", "70") + " = &minus;0.1",
                "A negative cosine means the angle is obtuse.",
                "C = cos<sup>&minus;1</sup>(&minus;0.1) = 95.739&hellip;&deg;",
            ],
            "answer": "95.7&deg; (1 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>A triangle has two sides of 8 cm and 11 cm with an angle of 47&deg; between them.</p>"
                 "<p>Work out the area of the triangle, to 3 significant figures.</p>",
            "steps": [
                "Use Area = " + frac("1", "2") + "ab sin C, where C is the angle between the two sides.",
                "Area = " + frac("1", "2") + " &times; 8 &times; 11 &times; sin 47&deg;",
                frac("1", "2") + " &times; 8 &times; 11 = 44",
                "sin 47&deg; = 0.731354&hellip;",
                "44 &times; 0.731354 = 32.179&hellip; cm<sup>2</sup>",
            ],
            "answer": "32.2 cm<sup>2</sup> (3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>A ship sails 40 km on a bearing of 070&deg;, then 30 km on a bearing of 160&deg;.</p>"
                 "<p class='part'>(a) Work out how far the ship now is from its starting point.</p>"
                 "<p class='part'>(b) Work out the bearing of the ship from its starting point, to the "
                 "nearest degree.</p>",
            "steps": [
                "<b>(a)</b> The bearings differ by 160 &minus; 70 = 90&deg;, so the two legs are at right angles.",
                "distance<sup>2</sup> = 40<sup>2</sup> + 30<sup>2</sup> = 1600 + 900 = 2500",
                "&radic;2500 = 50 km",
                "<b>(b)</b> In that right-angled triangle, the angle at the start between the first leg and "
                "the direct line is tan<sup>&minus;1</sup>(" + frac("30", "40") + ") = 36.87&deg;",
                "The direct line is that much further clockwise than the 070&deg; bearing.",
                "Bearing = 070 + 36.87 = 106.87&deg;, so 107&deg; to the nearest degree.",
            ],
            "answer": "(a) 50 km &nbsp;&nbsp; (b) 107&deg;",
        },
        {
            "marks": 5,
            "q": "<p>A pyramid has a square base ABCD of side 8 cm. The apex E is directly above the centre "
                 "of the base, and EA = 10 cm.</p>"
                 "<p class='part'>(a) Work out the length of the base diagonal AC, to 2 decimal places.</p>"
                 "<p class='part'>(b) Work out the vertical height of the pyramid, to 2 decimal places.</p>"
                 "<p class='part'>(c) Work out the angle EA makes with the base, to 1 decimal place.</p>",
            "steps": [
                "<b>(a)</b> AC is the diagonal of an 8 cm square: AC<sup>2</sup> = 8<sup>2</sup> + 8<sup>2</sup> = 128",
                "AC = &radic;128 = 11.3137&hellip; cm, so 11.31 cm",
                "<b>(b)</b> The apex is above the centre, so the horizontal distance from A to that point "
                "is half of AC = 5.6568&hellip; cm",
                "height<sup>2</sup> = 10<sup>2</sup> &minus; 5.6568<sup>2</sup> = 100 &minus; 32 = 68",
                "height = &radic;68 = 8.2462&hellip; cm, so 8.25 cm",
                "<b>(c)</b> In that right-angled triangle the adjacent side is 5.6568 and the hypotenuse is 10.",
                "cos &theta; = " + frac("5.6568", "10") + ", so &theta; = cos<sup>&minus;1</sup>(0.56568) = 55.550&hellip;&deg;",
            ],
            "answer": "(a) 11.31 cm &nbsp;&nbsp; (b) 8.25 cm &nbsp;&nbsp; (c) 55.6&deg;",
        },
    ],
}

CIRCLE_THEOREMS = {
    "title": "Circle Theorems",
    "folder": "gcse/geometry",
    "slug": "circle-theorems-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>What is the name of a straight line drawn from the centre of a circle to a point "
                 "on the circumference?</p>",
            "steps": [
                "It is half of a diameter.",
                "Every radius of a circle is the same length.",
            ],
            "answer": "a radius",
        },
        {
            "marks": 2,
            "q": "<p class='part'>(a) What is a chord of a circle?</p>"
                 "<p class='part'>(b) What is a tangent to a circle?</p>",
            "steps": [
                "<b>(a)</b> A chord is a straight line joining two points on the circumference. "
                "(A diameter is the special chord that passes through the centre.)",
                "<b>(b)</b> A tangent is a straight line that touches the circle at exactly one point.",
            ],
            "answer": "(a) a line joining two points on the circumference &nbsp;&nbsp; "
                      "(b) a line touching the circle at exactly one point",
        },
        {
            "marks": 2,
            "q": "<p>AB is a diameter of a circle. C is another point on the circle.</p>"
                 "<p>Write down the size of angle ACB and give a reason.</p>",
            "steps": [
                "The angle standing on a diameter, drawn from the circumference, is always a right angle.",
                "This is the &lsquo;angle in a semicircle&rsquo; theorem.",
            ],
            "answer": "90&deg; &mdash; the angle in a semicircle is a right angle",
        },
        {
            "marks": 2,
            "q": "<p>A, B and C are points on a circle with centre O. Angle AOC = 100&deg; and B lies on "
                 "the major arc.</p>"
                 "<p>Work out angle ABC.</p>",
            "steps": [
                "The angle at the centre is twice the angle at the circumference on the same arc.",
                "100 &divide; 2 = 50&deg;",
            ],
            "answer": "50&deg;",
        },
        {
            "marks": 3,
            "q": "<p>PQRS is a cyclic quadrilateral. Angle PQR = 105&deg;.</p>"
                 "<p>Work out angle PSR and give a reason.</p>",
            "steps": [
                "PQR and PSR are opposite angles of a cyclic quadrilateral.",
                "Opposite angles of a cyclic quadrilateral add up to 180&deg;.",
                "180 &minus; 105 = 75&deg;",
            ],
            "answer": "75&deg; &mdash; opposite angles of a cyclic quadrilateral add to 180&deg;",
        },
        {
            "marks": 3,
            "q": "<p>A tangent touches a circle of radius 5 cm at point T. P is a point on the tangent "
                 "with PT = 12 cm. O is the centre.</p>"
                 "<p>Work out the length of OP.</p>",
            "steps": [
                "A tangent meets a radius at 90&deg;, so triangle OTP is right-angled at T.",
                "OP<sup>2</sup> = OT<sup>2</sup> + TP<sup>2</sup> = 5<sup>2</sup> + 12<sup>2</sup>",
                "= 25 + 144 = 169",
                "OP = &radic;169 = 13 cm",
            ],
            "answer": "13 cm",
        },
        {
            "marks": 3,
            "q": "<p>Two angles at the circumference of a circle both stand on the same chord AB and are "
                 "on the same side of it. One of them is 38&deg;.</p>"
                 "<p>Write down the size of the other angle and give a reason.</p>",
            "steps": [
                "Angles standing on the same chord, in the same segment, are equal.",
                "So the other angle is also 38&deg;.",
                "This is the &lsquo;angles in the same segment&rsquo; theorem.",
            ],
            "answer": "38&deg; &mdash; angles in the same segment are equal",
        },
        {
            "marks": 3,
            "q": "<p>A and B are points on a circle with centre O. Angle AOB = 70&deg;.</p>"
                 "<p>Work out the size of angle OAB, explaining your reasoning.</p>",
            "steps": [
                "OA and OB are both radii, so they are equal in length.",
                "That makes triangle OAB isosceles, so angles OAB and OBA are equal.",
                "The three angles total 180&deg;, so the two equal angles share 180 &minus; 70 = 110&deg;.",
                "110 &divide; 2 = 55&deg;",
            ],
            "answer": "55&deg; &mdash; OA and OB are radii, so the triangle is isosceles",
        },
        {
            "marks": 4,
            "q": "<p>A, B and C are points on a circle with centre O, with C on the major arc AB.</p>"
                 "<p>Angle OAB = 25&deg;.</p>"
                 "<p class='part'>(a) Write down angle OBA, with a reason.</p>"
                 "<p class='part'>(b) Work out angle AOB.</p>"
                 "<p class='part'>(c) Work out angle ACB.</p>",
            "steps": [
                "<b>(a)</b> OA and OB are radii, so triangle OAB is isosceles and angle OBA = 25&deg;.",
                "<b>(b)</b> The angles of triangle OAB total 180&deg;.",
                "Angle AOB = 180 &minus; 25 &minus; 25 = 130&deg;",
                "<b>(c)</b> The angle at the centre is twice the angle at the circumference on the same arc.",
                "Angle ACB = 130 &divide; 2 = 65&deg;",
            ],
            "answer": "(a) 25&deg; (isosceles, two radii) &nbsp;&nbsp; (b) 130&deg; &nbsp;&nbsp; (c) 65&deg;",
        },
        {
            "marks": 4,
            "q": "<p>AB is a diameter of a circle with AB = 13 cm. C is a point on the circle with "
                 "AC = 5 cm.</p>"
                 "<p class='part'>(a) Write down angle ACB, with a reason.</p>"
                 "<p class='part'>(b) Work out the length of BC.</p>"
                 "<p class='part'>(c) Work out the area of triangle ABC.</p>",
            "steps": [
                "<b>(a)</b> Angle ACB = 90&deg;, because the angle in a semicircle is a right angle.",
                "<b>(b)</b> Triangle ACB is right-angled at C, so BC<sup>2</sup> = 13<sup>2</sup> &minus; 5<sup>2</sup>",
                "= 169 &minus; 25 = 144, so BC = 12 cm",
                "<b>(c)</b> AC and BC are perpendicular, so use them as base and height.",
                "Area = " + frac("1", "2") + " &times; 5 &times; 12 = 30 cm<sup>2</sup>",
            ],
            "answer": "(a) 90&deg; (angle in a semicircle) &nbsp;&nbsp; (b) 12 cm &nbsp;&nbsp; (c) 30 cm<sup>2</sup>",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>The angle at the centre of a circle standing on an arc is 84&deg;.</p>"
                 "<p>Work out the angle at the circumference standing on the same arc.</p>",
            "steps": [
                "The angle at the centre is twice the angle at the circumference.",
                "84 &divide; 2 = 42&deg;",
            ],
            "answer": "42&deg;",
        },
        {
            "marks": 2,
            "q": "<p>In a cyclic quadrilateral, two opposite angles are <i>x</i>&deg; and 3<i>x</i>&deg;.</p>"
                 "<p>Work out the value of <i>x</i>.</p>",
            "steps": [
                "Opposite angles of a cyclic quadrilateral add up to 180&deg;.",
                "<i>x</i> + 3<i>x</i> = 180, so 4<i>x</i> = 180",
                "<i>x</i> = 45",
            ],
            "answer": "<i>x</i> = 45",
        },
        {
            "marks": 3,
            "q": "<p>PT is a tangent to a circle with centre O, touching at T. The radius is 6 cm and "
                 "PT = 8 cm.</p>"
                 "<p class='part'>(a) Work out the length of OP.</p>"
                 "<p class='part'>(b) Work out the size of angle TPO, to 1 decimal place.</p>",
            "steps": [
                "<b>(a)</b> Angle OTP = 90&deg; because a tangent meets a radius at right angles.",
                "OP<sup>2</sup> = 6<sup>2</sup> + 8<sup>2</sup> = 100, so OP = 10 cm",
                "<b>(b)</b> At P, the opposite side is OT = 6 and the adjacent side is PT = 8.",
                "tan(TPO) = " + frac("6", "8") + " = 0.75, so angle TPO = tan<sup>&minus;1</sup>(0.75) = 36.869&hellip;&deg;",
            ],
            "answer": "(a) 10 cm &nbsp;&nbsp; (b) 36.9&deg;",
        },
        {
            "marks": 3,
            "q": "<p>A tangent touches a circle at A. A chord AB is drawn, and the angle between the tangent "
                 "and the chord is 54&deg;.</p>"
                 "<p>Write down the size of the angle in the alternate segment, and state the theorem you "
                 "have used.</p>",
            "steps": [
                "The alternate segment theorem says the angle between a tangent and a chord equals the "
                "angle in the alternate segment.",
                "The alternate segment is the one on the other side of the chord.",
                "So the angle there is also 54&deg;.",
            ],
            "answer": "54&deg; &mdash; by the alternate segment theorem",
        },
        {
            "marks": 4,
            "q": "<p>ABCD is a cyclic quadrilateral in which AB is a diameter of the circle.</p>"
                 "<p>Angle ADC = 130&deg;.</p>"
                 "<p class='part'>(a) Work out angle ABC, with a reason.</p>"
                 "<p class='part'>(b) Write down angle ACB, with a reason.</p>"
                 "<p class='part'>(c) Work out angle BAC.</p>",
            "steps": [
                "<b>(a)</b> ADC and ABC are opposite angles of a cyclic quadrilateral, so they add to 180&deg;.",
                "Angle ABC = 180 &minus; 130 = 50&deg;",
                "<b>(b)</b> Angle ACB stands on the diameter AB, so it is 90&deg; (angle in a semicircle).",
                "<b>(c)</b> In triangle ABC the angles total 180&deg;.",
                "Angle BAC = 180 &minus; 90 &minus; 50 = 40&deg;",
            ],
            "answer": "(a) 50&deg; (cyclic quadrilateral) &nbsp;&nbsp; (b) 90&deg; (angle in a semicircle) &nbsp;&nbsp; "
                      "(c) 40&deg;",
        },
        {
            "marks": 4,
            "q": "<p>A, B and C are points on a circle with centre O. Angle BAC = 35&deg;.</p>"
                 "<p class='part'>(a) Work out angle BOC, with a reason.</p>"
                 "<p class='part'>(b) Work out angle OBC.</p>",
            "steps": [
                "<b>(a)</b> The angle at the centre is twice the angle at the circumference on the same arc BC.",
                "Angle BOC = 2 &times; 35 = 70&deg;",
                "<b>(b)</b> OB and OC are radii, so triangle OBC is isosceles.",
                "The two base angles share 180 &minus; 70 = 110&deg;.",
                "Angle OBC = 110 &divide; 2 = 55&deg;",
            ],
            "answer": "(a) 70&deg; (angle at centre is twice the angle at circumference) &nbsp;&nbsp; (b) 55&deg;",
        },
        {
            "marks": 4,
            "q": "<p>TA is a tangent to a circle, touching at A. ABCD is a cyclic quadrilateral.</p>"
                 "<p>Angle TAB = 65&deg; and angle ABC = 80&deg;.</p>"
                 "<p class='part'>(a) Work out angle ACB, with a reason.</p>"
                 "<p class='part'>(b) Write down angle ADB, with a reason.</p>"
                 "<p class='part'>(c) Work out angle ADC.</p>",
            "steps": [
                "<b>(a)</b> Angle TAB is between the tangent and the chord AB, so it equals the angle in the "
                "alternate segment, which is angle ACB.",
                "Angle ACB = 65&deg;",
                "<b>(b)</b> Angles ADB and ACB both stand on the chord AB in the same segment, so they are equal.",
                "Angle ADB = 65&deg;",
                "<b>(c)</b> ABC and ADC are opposite angles of the cyclic quadrilateral.",
                "Angle ADC = 180 &minus; 80 = 100&deg;",
            ],
            "answer": "(a) 65&deg; (alternate segment) &nbsp;&nbsp; (b) 65&deg; (same segment) &nbsp;&nbsp; (c) 100&deg;",
        },
        {
            "marks": 4,
            "q": "<p>PT is a tangent to a circle with centre O, touching at T. The radius is 7 cm and "
                 "OP = 25 cm.</p>"
                 "<p class='part'>(a) Work out the length of PT.</p>"
                 "<p class='part'>(b) Work out angle TOP, to 1 decimal place.</p>",
            "steps": [
                "<b>(a)</b> Angle OTP = 90&deg;, so PT<sup>2</sup> = 25<sup>2</sup> &minus; 7<sup>2</sup>",
                "= 625 &minus; 49 = 576, so PT = &radic;576 = 24 cm",
                "<b>(b)</b> At O, the adjacent side is OT = 7 and the hypotenuse is OP = 25.",
                "cos(TOP) = " + frac("7", "25") + " = 0.28, so angle TOP = cos<sup>&minus;1</sup>(0.28) = 73.739&hellip;&deg;",
            ],
            "answer": "(a) 24 cm &nbsp;&nbsp; (b) 73.7&deg;",
        },
        {
            "marks": 4,
            "q": "<p>PA and PB are tangents to a circle with centre O, touching at A and B.</p>"
                 "<p>Angle APB = 48&deg;.</p>"
                 "<p class='part'>(a) Write down angle OAP, with a reason.</p>"
                 "<p class='part'>(b) Work out angle AOB.</p>"
                 "<p class='part'>(c) Work out angle OAB.</p>",
            "steps": [
                "<b>(a)</b> Angle OAP = 90&deg;, because a tangent meets a radius at right angles.",
                "<b>(b)</b> OAPB is a quadrilateral with angles 90&deg;, 48&deg;, 90&deg; and AOB, totalling 360&deg;.",
                "Angle AOB = 360 &minus; 90 &minus; 90 &minus; 48 = 132&deg;",
                "<b>(c)</b> OA and OB are radii, so triangle OAB is isosceles.",
                "Angle OAB = (180 &minus; 132) &divide; 2 = 24&deg;",
            ],
            "answer": "(a) 90&deg; (tangent meets radius at 90&deg;) &nbsp;&nbsp; (b) 132&deg; &nbsp;&nbsp; (c) 24&deg;",
        },
        {
            "marks": 5,
            "q": "<p>Prove that the angle at the centre of a circle is twice the angle at the circumference "
                 "when both stand on the same arc.</p>",
            "steps": [
                "Let O be the centre, A and B be the ends of the arc, and P a point on the major arc. "
                "Draw the line PO and extend it to meet the circle again at Q.",
                "OA = OP because both are radii, so triangle OAP is isosceles and angle OAP = angle OPA. "
                "Call each of these a.",
                "Angle AOQ is the exterior angle of triangle OAP at O, so angle AOQ = a + a = 2a.",
                "In the same way OB = OP, so triangle OBP is isosceles with equal angles b, and "
                "angle BOQ = 2b.",
                "Angle AOB = angle AOQ + angle BOQ = 2a + 2b = 2(a + b)",
                "Angle APB = angle OPA + angle OPB = a + b, so angle AOB = 2 &times; angle APB as required.",
            ],
            "answer": "Splitting the figure with the line PO gives two isosceles triangles; each contributes "
                      "an exterior angle of double its base angle, so the centre angle is 2(a + b) = twice "
                      "the circumference angle",
        },
    ],
}

TRANSFORMATIONS = {
    "title": "Transformations",
    "folder": "gcse/geometry",
    "slug": "transformations-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Which transformation moves every point of a shape the same distance in the same "
                 "direction, without turning or resizing it?</p>",
            "steps": [
                "The shape simply slides across the grid.",
                "The image is congruent to the original &mdash; same shape, same size, same way up.",
            ],
            "answer": "a translation",
        },
        {
            "marks": 2,
            "q": "<p>Translate the point (3, 2) by the vector " + col("4", "&minus;5") + "</p>"
                 "<p>Write down the coordinates of the image.</p>",
            "steps": [
                "The top number moves the point horizontally and the bottom number vertically.",
                "<i>x</i>: 3 + 4 = 7",
                "<i>y</i>: 2 + (&minus;5) = &minus;3",
            ],
            "answer": "(7, &minus;3)",
        },
        {
            "marks": 2,
            "q": "<p>Reflect the point (3, 5)</p>"
                 "<p class='part'>(a) in the <i>x</i>-axis</p>"
                 "<p class='part'>(b) in the <i>y</i>-axis</p>",
            "steps": [
                "<b>(a)</b> Reflecting in the <i>x</i>-axis changes the sign of the <i>y</i>-coordinate: (3, &minus;5)",
                "<b>(b)</b> Reflecting in the <i>y</i>-axis changes the sign of the <i>x</i>-coordinate: (&minus;3, 5)",
            ],
            "answer": "(a) (3, &minus;5) &nbsp;&nbsp; (b) (&minus;3, 5)",
        },
        {
            "marks": 2,
            "q": "<p>Rotate the point (4, 0) through 90&deg; anticlockwise about the origin.</p>",
            "steps": [
                "The point is 4 units along the positive <i>x</i>-axis.",
                "Turning 90&deg; anticlockwise takes it to 4 units up the positive <i>y</i>-axis.",
            ],
            "answer": "(0, 4)",
        },
        {
            "marks": 3,
            "q": "<p>Reflect the point (2, 3)</p>"
                 "<p class='part'>(a) in the line <i>y</i> = <i>x</i></p>"
                 "<p class='part'>(b) in the line <i>y</i> = 1</p>",
            "steps": [
                "<b>(a)</b> Reflecting in <i>y</i> = <i>x</i> swaps the coordinates: (3, 2)",
                "<b>(b)</b> The point is 3 &minus; 1 = 2 units above the line <i>y</i> = 1.",
                "The image must be 2 units below the line, at <i>y</i> = 1 &minus; 2 = &minus;1",
                "The <i>x</i>-coordinate does not change, so the image is (2, &minus;1).",
            ],
            "answer": "(a) (3, 2) &nbsp;&nbsp; (b) (2, &minus;1)",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Enlarge the point (2, 3) by scale factor 3 about the origin.</p>"
                 "<p class='part'>(b) A shape is enlarged by scale factor 3. What happens to its area?</p>",
            "steps": [
                "<b>(a)</b> Multiply both coordinates by 3: (6, 9)",
                "<b>(b)</b> Both dimensions are 3 times as long, so the area is multiplied by 3<sup>2</sup>.",
                "The area becomes 9 times as large.",
            ],
            "answer": "(a) (6, 9) &nbsp;&nbsp; (b) the area is multiplied by 9",
        },
        {
            "marks": 3,
            "q": "<p>Rotate the point (3, 1) about the origin</p>"
                 "<p class='part'>(a) through 180&deg;</p>"
                 "<p class='part'>(b) through 90&deg; clockwise</p>",
            "steps": [
                "<b>(a)</b> A 180&deg; rotation about the origin changes the sign of both coordinates: (&minus;3, &minus;1)",
                "<b>(b)</b> For 90&deg; clockwise, (<i>x</i>, <i>y</i>) maps to (<i>y</i>, &minus;<i>x</i>).",
                "So (3, 1) maps to (1, &minus;3).",
            ],
            "answer": "(a) (&minus;3, &minus;1) &nbsp;&nbsp; (b) (1, &minus;3)",
        },
        {
            "marks": 3,
            "q": "<p>Which of these transformations always give an image congruent to the original shape?</p>"
                 "<p><b>reflection &nbsp;&middot;&nbsp; rotation &nbsp;&middot;&nbsp; translation "
                 "&nbsp;&middot;&nbsp; enlargement</b></p>"
                 "<p>Explain your answer.</p>",
            "steps": [
                "Congruent means exactly the same shape <b>and</b> the same size.",
                "Reflections, rotations and translations move a shape without changing any lengths, so the "
                "image is congruent.",
                "An enlargement changes the lengths (unless the scale factor is 1), so the image is a "
                "different size &mdash; similar but not congruent.",
            ],
            "answer": "reflection, rotation and translation &mdash; enlargement changes the size",
        },
        {
            "marks": 4,
            "q": "<p>Triangle P has vertices (1, 1), (3, 1) and (1, 4).</p>"
                 "<p>Triangle Q has vertices (1, &minus;1), (3, &minus;1) and (1, &minus;4).</p>"
                 "<p>Describe fully the single transformation that maps P onto Q.</p>",
            "steps": [
                "Compare each pair of points: the <i>x</i>-coordinates are unchanged and the "
                "<i>y</i>-coordinates have changed sign.",
                "(1, 1) &rarr; (1, &minus;1), (3, 1) &rarr; (3, &minus;1), (1, 4) &rarr; (1, &minus;4)",
                "Changing the sign of <i>y</i> only is a reflection in the <i>x</i>-axis.",
                "A full description names the transformation and the mirror line.",
            ],
            "answer": "a reflection in the <i>x</i>-axis (the line <i>y</i> = 0)",
        },
        {
            "marks": 4,
            "q": "<p>Triangle T has vertices (1, 1), (2, 1) and (1, 3).</p>"
                 "<p class='part'>(a) Enlarge T by scale factor 2 about the origin. Write down the new vertices.</p>"
                 "<p class='part'>(b) Enlarge T by scale factor 2 about the point (1, 1). Write down the "
                 "new vertices.</p>",
            "steps": [
                "<b>(a)</b> About the origin, simply double both coordinates.",
                "(2, 2), (4, 2) and (2, 6)",
                "<b>(b)</b> About (1, 1), first write each point as a step from the centre, then double it.",
                "(1, 1) is the centre, so it does not move.",
                "(2, 1) is 1 right of the centre; doubling gives 2 right, so the image is (3, 1).",
                "(1, 3) is 2 up from the centre; doubling gives 4 up, so the image is (1, 5).",
            ],
            "answer": "(a) (2, 2), (4, 2), (2, 6) &nbsp;&nbsp; (b) (1, 1), (3, 1), (1, 5)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Rotate the point (2, 5) through 90&deg; clockwise about the origin.</p>",
            "steps": [
                "For a 90&deg; clockwise rotation about the origin, (<i>x</i>, <i>y</i>) maps to "
                "(<i>y</i>, &minus;<i>x</i>).",
                "So (2, 5) maps to (5, &minus;2).",
            ],
            "answer": "(5, &minus;2)",
        },
        {
            "marks": 2,
            "q": "<p>Enlarge the point (4, &minus;2) by scale factor &minus;1 about the origin.</p>",
            "steps": [
                "A negative scale factor puts the image on the opposite side of the centre.",
                "Multiply both coordinates by &minus;1: (&minus;4, 2)",
            ],
            "answer": "(&minus;4, 2)",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Enlarge the point (5, 3) by scale factor " + frac("1", "2")
                 + " about the origin.</p>"
                 "<p class='part'>(b) A shape of area 40 cm<sup>2</sup> is enlarged by the same scale factor. "
                 "Work out the new area.</p>",
            "steps": [
                "<b>(a)</b> Halve both coordinates: (2.5, 1.5)",
                "<b>(b)</b> Area scale factor = (" + frac("1", "2") + ")<sup>2</sup> = " + frac("1", "4"),
                "40 &times; " + frac("1", "4") + " = 10 cm<sup>2</sup>",
            ],
            "answer": "(a) (2.5, 1.5) &nbsp;&nbsp; (b) 10 cm<sup>2</sup>",
        },
        {
            "marks": 3,
            "q": "<p>Triangle A has vertices (0, 0), (2, 0) and (0, 3).</p>"
                 "<p>Triangle B has vertices (0, 0), (&minus;2, 0) and (0, &minus;3).</p>"
                 "<p>Describe fully the single transformation that maps A onto B.</p>",
            "steps": [
                "Both coordinates have changed sign in every case.",
                "That is exactly what a rotation of 180&deg; about the origin does.",
                "The shape is the same size, so it is not an ordinary enlargement.",
            ],
            "answer": "a rotation of 180&deg; about the origin",
        },
        {
            "marks": 4,
            "q": "<p>A shape is reflected in the <i>x</i>-axis, and the image is then reflected in the "
                 "<i>y</i>-axis.</p>"
                 "<p>Show that the result is the same as a single rotation, and describe that rotation fully.</p>",
            "steps": [
                "Start with a general point (a, b).",
                "Reflecting in the <i>x</i>-axis gives (a, &minus;b).",
                "Reflecting that in the <i>y</i>-axis gives (&minus;a, &minus;b).",
                "So the combined effect changes the sign of both coordinates.",
                "That is a rotation of 180&deg; about the origin, for every point of the shape.",
            ],
            "answer": "(a, b) &rarr; (&minus;a, &minus;b), which is a rotation of 180&deg; about the origin",
        },
        {
            "marks": 4,
            "q": "<p>Enlarge the point (4, 3) by scale factor &minus;2 about the centre (1, 1).</p>",
            "steps": [
                "Write the point as a step from the centre: (4 &minus; 1, 3 &minus; 1) = (3, 2)",
                "Multiply that step by the scale factor &minus;2: (&minus;6, &minus;4)",
                "The negative sign sends the image to the opposite side of the centre.",
                "Add the step back on to the centre: (1 &minus; 6, 1 &minus; 4)",
                "The image is (&minus;5, &minus;3).",
            ],
            "answer": "(&minus;5, &minus;3)",
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) A shape is reflected in the line <i>x</i> = 3. Which points of the "
                 "shape do not move? Explain.</p>"
                 "<p class='part'>(b) A shape is rotated about the point (2, 5). Which points do not move? "
                 "Explain.</p>",
            "steps": [
                "Points that do not move under a transformation are called invariant points.",
                "<b>(a)</b> Any point already on the mirror line reflects onto itself.",
                "So the invariant points are those with <i>x</i> = 3.",
                "<b>(b)</b> A rotation turns every point around the centre.",
                "Only the centre itself stays where it is, so (2, 5) is the only invariant point.",
            ],
            "answer": "(a) the points on the line <i>x</i> = 3 &nbsp;&nbsp; (b) only the centre (2, 5)",
        },
        {
            "marks": 4,
            "q": "<p>Describe fully the single transformation equivalent to each pair.</p>"
                 "<p class='part'>(a) A translation by " + col("5", "0") + " followed by a translation by "
                 + col("&minus;2", "3") + "</p>"
                 "<p class='part'>(b) A reflection in <i>y</i> = <i>x</i> followed by a reflection in "
                 "<i>y</i> = &minus;<i>x</i></p>",
            "steps": [
                "<b>(a)</b> Add the two vectors: 5 + (&minus;2) = 3 and 0 + 3 = 3",
                "So the single transformation is a translation by " + col("3", "3"),
                "<b>(b)</b> Take a general point (a, b). Reflecting in <i>y</i> = <i>x</i> swaps the "
                "coordinates to give (b, a).",
                "Reflecting (<i>x</i>, <i>y</i>) in <i>y</i> = &minus;<i>x</i> gives (&minus;<i>y</i>, &minus;<i>x</i>), "
                "so (b, a) becomes (&minus;a, &minus;b).",
                "Both coordinates have changed sign, which is a rotation of 180&deg; about the origin.",
            ],
            "answer": "(a) a translation by " + col("3", "3") + " &nbsp;&nbsp; (b) a rotation of 180&deg; "
                      "about the origin",
        },
        {
            "marks": 4,
            "q": "<p>Rotate the point (5, 2) through 90&deg; anticlockwise about the centre (1, 1).</p>",
            "steps": [
                "Write the point as a step from the centre: (5 &minus; 1, 2 &minus; 1) = (4, 1)",
                "For a 90&deg; anticlockwise rotation, a step (<i>x</i>, <i>y</i>) becomes "
                "(&minus;<i>y</i>, <i>x</i>).",
                "So (4, 1) becomes (&minus;1, 4).",
                "Add the new step back on to the centre: (1 &minus; 1, 1 + 4)",
                "The image is (0, 5).",
            ],
            "answer": "(0, 5)",
        },
        {
            "marks": 5,
            "q": "<p>Triangle T has vertices (1, 1), (4, 1) and (1, 3).</p>"
                 "<p class='part'>(a) T is enlarged by scale factor &minus;2 about the origin to give T&prime;. "
                 "Find the vertices of T&prime;.</p>"
                 "<p class='part'>(b) Work out the area of T.</p>"
                 "<p class='part'>(c) Work out the area of T&prime;.</p>",
            "steps": [
                "<b>(a)</b> With the origin as centre, multiply every coordinate by &minus;2.",
                "(1, 1) &rarr; (&minus;2, &minus;2), &nbsp; (4, 1) &rarr; (&minus;8, &minus;2), &nbsp; (1, 3) &rarr; (&minus;2, &minus;6)",
                "<b>(b)</b> T is right-angled: the base from (1, 1) to (4, 1) is 3 and the height from "
                "(1, 1) to (1, 3) is 2.",
                "Area = " + frac("1", "2") + " &times; 3 &times; 2 = 3 square units",
                "<b>(c)</b> The area scale factor is the square of the length scale factor, and squaring "
                "removes the minus sign: (&minus;2)<sup>2</sup> = 4",
                "Area of T&prime; = 3 &times; 4 = 12 square units",
            ],
            "answer": "(a) (&minus;2, &minus;2), (&minus;8, &minus;2), (&minus;2, &minus;6) &nbsp;&nbsp; "
                      "(b) 3 square units &nbsp;&nbsp; (c) 12 square units",
        },
    ],
}

AREA_VOLUME = {
    "title": "Area, Perimeter and Volume",
    "folder": "gcse/geometry",
    "slug": "area-volume-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Work out the area of a rectangle measuring 7 cm by 5 cm.</p>",
            "steps": [
                "Area of a rectangle = length &times; width",
                "7 &times; 5 = 35",
            ],
            "answer": "35 cm<sup>2</sup>",
        },
        {
            "marks": 2,
            "q": "<p>Work out the area of a triangle with base 12 cm and perpendicular height 5 cm.</p>",
            "steps": [
                "Area = " + frac("1", "2") + " &times; base &times; height",
                "= " + frac("1", "2") + " &times; 12 &times; 5 = 30",
            ],
            "answer": "30 cm<sup>2</sup>",
        },
        {
            "marks": 2,
            "q": "<p>Work out the area of a trapezium with parallel sides 6 cm and 10 cm and "
                 "perpendicular height 4 cm.</p>",
            "steps": [
                "Area = " + frac("1", "2") + " &times; (a + b) &times; h",
                "a + b = 6 + 10 = 16",
                "= " + frac("1", "2") + " &times; 16 &times; 4 = 32",
            ],
            "answer": "32 cm<sup>2</sup>",
        },
        {
            "marks": 2,
            "q": "<p>Work out the circumference of a circle of radius 7 cm, correct to 1 decimal place.</p>",
            "steps": [
                "Circumference = 2&pi;r = 2 &times; &pi; &times; 7 = 14&pi;",
                "14 &times; 3.14159&hellip; = 43.982&hellip;",
            ],
            "answer": "44.0 cm (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>Work out the area of a circle of radius 6 cm, correct to 1 decimal place.</p>",
            "steps": [
                "Area = &pi;r<sup>2</sup>",
                "= &pi; &times; 6<sup>2</sup> = 36&pi;",
                "36 &times; 3.14159&hellip; = 113.097&hellip;",
            ],
            "answer": "113.1 cm<sup>2</sup> (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>A cuboid measures 5 cm by 4 cm by 9 cm.</p>"
                 "<p class='part'>(a) Work out its volume.</p>"
                 "<p class='part'>(b) Work out its total surface area.</p>",
            "steps": [
                "<b>(a)</b> Volume = 5 &times; 4 &times; 9 = 180 cm<sup>3</sup>",
                "<b>(b)</b> The six faces come in three matching pairs.",
                "5 &times; 4 = 20, &nbsp; 5 &times; 9 = 45, &nbsp; 4 &times; 9 = 36",
                "Surface area = 2 &times; (20 + 45 + 36) = 2 &times; 101 = 202 cm<sup>2</sup>",
            ],
            "answer": "(a) 180 cm<sup>3</sup> &nbsp;&nbsp; (b) 202 cm<sup>2</sup>",
        },
        {
            "marks": 3,
            "q": "<p>Work out the volume of a cylinder with radius 3 cm and height 8 cm, correct to "
                 "1 decimal place.</p>",
            "steps": [
                "Volume of a cylinder = &pi;r<sup>2</sup>h",
                "= &pi; &times; 3<sup>2</sup> &times; 8 = 72&pi;",
                "72 &times; 3.14159&hellip; = 226.194&hellip;",
            ],
            "answer": "226.2 cm<sup>3</sup> (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>An L-shape is made by taking a rectangle 10 cm by 6 cm and cutting away a rectangle "
                 "4 cm by 3 cm from one corner.</p>"
                 "<p>Work out the area of the L-shape.</p>",
            "steps": [
                "Work out the two areas and subtract.",
                "Large rectangle: 10 &times; 6 = 60 cm<sup>2</sup>",
                "Cut-out rectangle: 4 &times; 3 = 12 cm<sup>2</sup>",
                "60 &minus; 12 = 48 cm<sup>2</sup>",
            ],
            "answer": "48 cm<sup>2</sup>",
        },
        {
            "marks": 4,
            "q": "<p>A semicircle has radius 5 cm.</p>"
                 "<p class='part'>(a) Work out its area, correct to 1 decimal place.</p>"
                 "<p class='part'>(b) Work out its perimeter, correct to 1 decimal place.</p>",
            "steps": [
                "<b>(a)</b> Area of the whole circle = &pi; &times; 5<sup>2</sup> = 25&pi; = 78.539&hellip; cm<sup>2</sup>",
                "Half of that is 39.269&hellip; cm<sup>2</sup>",
                "<b>(b)</b> The perimeter is the curved part <b>plus</b> the straight diameter.",
                "Curved part = " + frac("1", "2") + " &times; 2&pi; &times; 5 = 5&pi; = 15.707&hellip; cm",
                "Diameter = 10 cm, so the perimeter is 15.707 + 10 = 25.707&hellip; cm",
            ],
            "answer": "(a) 39.3 cm<sup>2</sup> &nbsp;&nbsp; (b) 25.7 cm (both 1 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>A prism has a trapezium cross-section with parallel sides 5 cm and 9 cm and "
                 "perpendicular height 4 cm. The prism is 12 cm long.</p>"
                 "<p class='part'>(a) Work out the area of the cross-section.</p>"
                 "<p class='part'>(b) Work out the volume of the prism.</p>",
            "steps": [
                "<b>(a)</b> Area = " + frac("1", "2") + " &times; (5 + 9) &times; 4",
                "= " + frac("1", "2") + " &times; 14 &times; 4 = 28 cm<sup>2</sup>",
                "<b>(b)</b> Volume of a prism = area of cross-section &times; length",
                "= 28 &times; 12 = 336 cm<sup>3</sup>",
            ],
            "answer": "(a) 28 cm<sup>2</sup> &nbsp;&nbsp; (b) 336 cm<sup>3</sup>",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Work out the volume of a sphere of radius 3 cm. Give your answer in terms of &pi;.</p>",
            "steps": [
                "Volume of a sphere = " + frac("4", "3") + "&pi;r<sup>3</sup>",
                "r<sup>3</sup> = 27, so the volume is " + frac("4", "3") + " &times; 27&pi; = 36&pi;",
            ],
            "answer": "36&pi; cm<sup>3</sup>",
        },
        {
            "marks": 2,
            "q": "<p>Work out the volume of a cone with radius 4 cm and height 9 cm. Give your answer in "
                 "terms of &pi;.</p>",
            "steps": [
                "Volume of a cone = " + frac("1", "3") + "&pi;r<sup>2</sup>h",
                "= " + frac("1", "3") + " &times; &pi; &times; 16 &times; 9 = 48&pi;",
            ],
            "answer": "48&pi; cm<sup>3</sup>",
        },
        {
            "marks": 3,
            "q": "<p>Work out the surface area of a sphere of radius 5 cm, correct to "
                 "3 significant figures.</p>",
            "steps": [
                "Surface area of a sphere = 4&pi;r<sup>2</sup>",
                "= 4 &times; &pi; &times; 25 = 100&pi;",
                "100 &times; 3.14159&hellip; = 314.159&hellip;",
            ],
            "answer": "314 cm<sup>2</sup> (3 s.f.)",
        },
        {
            "marks": 3,
            "q": "<p>A sector of a circle has radius 8 cm and angle 45&deg;.</p>"
                 "<p>Work out the arc length, correct to 3 significant figures.</p>",
            "steps": [
                "The sector is " + frac("45", "360") + " = " + frac("1", "8") + " of the whole circle.",
                "Full circumference = 2 &times; &pi; &times; 8 = 16&pi; = 50.265&hellip; cm",
                "Arc = " + frac("1", "8") + " &times; 50.265&hellip; = 6.2832&hellip; cm",
            ],
            "answer": "6.28 cm (3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>A sector of a circle has radius 10 cm and angle 72&deg;.</p>"
                 "<p class='part'>(a) Work out its area, correct to 1 decimal place.</p>"
                 "<p class='part'>(b) Work out its perimeter, correct to 1 decimal place.</p>",
            "steps": [
                "The sector is " + frac("72", "360") + " = 0.2 of the whole circle.",
                "<b>(a)</b> Full area = &pi; &times; 100 = 314.159&hellip; cm<sup>2</sup>",
                "Sector area = 0.2 &times; 314.159&hellip; = 62.831&hellip; cm<sup>2</sup>",
                "<b>(b)</b> Arc = 0.2 &times; 2&pi; &times; 10 = 0.2 &times; 62.831&hellip; = 12.566&hellip; cm",
                "The perimeter also includes the two straight radii: 12.566 + 10 + 10 = 32.566&hellip; cm",
            ],
            "answer": "(a) 62.8 cm<sup>2</sup> &nbsp;&nbsp; (b) 32.6 cm (both 1 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>A cone has radius 5 cm and slant height 13 cm.</p>"
                 "<p class='part'>(a) Work out the curved surface area, correct to 3 significant figures.</p>"
                 "<p class='part'>(b) Work out the total surface area, correct to 3 significant figures.</p>",
            "steps": [
                "<b>(a)</b> Curved surface area of a cone = &pi;rl",
                "= &pi; &times; 5 &times; 13 = 65&pi; = 204.203&hellip; cm<sup>2</sup>",
                "<b>(b)</b> The total also includes the circular base of area &pi;r<sup>2</sup> = 25&pi;",
                "Total = 65&pi; + 25&pi; = 90&pi;",
                "90 &times; 3.14159&hellip; = 282.743&hellip; cm<sup>2</sup>",
            ],
            "answer": "(a) 204 cm<sup>2</sup> &nbsp;&nbsp; (b) 283 cm<sup>2</sup> (both 3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>A solid is made from a cylinder of radius 4 cm and height 10 cm, with a hemisphere of "
                 "radius 4 cm on top.</p>"
                 "<p>Work out the total volume, correct to 3 significant figures.</p>",
            "steps": [
                "Cylinder: &pi;r<sup>2</sup>h = &pi; &times; 16 &times; 10 = 160&pi;",
                "Hemisphere: half of " + frac("4", "3") + "&pi;r<sup>3</sup> = " + frac("2", "3") + " &times; &pi; &times; 64 = " + frac("128", "3") + "&pi;",
                frac("128", "3") + " = 42.666&hellip;, so the total is (160 + 42.667)&pi; = 202.667&pi;",
                "202.667 &times; 3.14159&hellip; = 636.696&hellip; cm<sup>3</sup>",
            ],
            "answer": "637 cm<sup>3</sup> (3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>A cylinder has volume 500 cm<sup>3</sup> and height 10 cm.</p>"
                 "<p>Work out its radius, correct to 2 decimal places.</p>",
            "steps": [
                "Volume = &pi;r<sup>2</sup>h, so 500 = &pi; &times; r<sup>2</sup> &times; 10",
                "r<sup>2</sup> = " + frac("500", "10&pi;") + " = " + frac("50", "&pi;"),
                frac("50", "3.14159&hellip;") + " = 15.9155&hellip;",
                "r = &radic;15.9155&hellip; = 3.9894&hellip; cm",
            ],
            "answer": "3.99 cm (2 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>A sphere of radius r fits exactly inside a cylinder of radius r and height 2r.</p>"
                 "<p>Show that the volume of the sphere is " + frac("2", "3")
                 + " of the volume of the cylinder.</p>",
            "steps": [
                "Sphere: V = " + frac("4", "3") + "&pi;r<sup>3</sup>",
                "Cylinder: V = &pi;r<sup>2</sup>h with h = 2r, so V = &pi;r<sup>2</sup> &times; 2r = 2&pi;r<sup>3</sup>",
                "Divide the sphere volume by the cylinder volume: " + frac(frac("4", "3") + "&pi;r<sup>3</sup>", "2&pi;r<sup>3</sup>"),
                "The &pi;r<sup>3</sup> cancels, leaving " + frac("4", "3") + " &divide; 2 = " + frac("4", "6") + " = " + frac("2", "3"),
                "So the sphere occupies exactly two-thirds of the cylinder.",
            ],
            "answer": frac("4", "3") + "&pi;r<sup>3</sup> &divide; 2&pi;r<sup>3</sup> = " + frac("2", "3"),
        },
        {
            "marks": 5,
            "q": "<p>A solid is made from a cone of radius 6 cm and slant height 10 cm standing on top of "
                 "a cylinder of radius 6 cm and height 15 cm.</p>"
                 "<p class='part'>(a) Work out the vertical height of the cone.</p>"
                 "<p class='part'>(b) Work out the total volume of the solid, to the nearest cm<sup>3</sup>.</p>"
                 "<p class='part'>(c) Work out the total surface area of the solid, to 3 significant figures. "
                 "(The solid has a flat circular base but no join surfaces.)</p>",
            "steps": [
                "<b>(a)</b> The radius, height and slant height form a right-angled triangle.",
                "height<sup>2</sup> = 10<sup>2</sup> &minus; 6<sup>2</sup> = 100 &minus; 36 = 64, so the height is 8 cm",
                "<b>(b)</b> Cylinder: &pi; &times; 36 &times; 15 = 540&pi;",
                "Cone: " + frac("1", "3") + " &times; &pi; &times; 36 &times; 8 = 96&pi;, so the total is 636&pi;",
                "636 &times; 3.14159&hellip; = 1998.05&hellip;, so 1998 cm<sup>3</sup>",
                "<b>(c)</b> Curved cone: &pi;rl = &pi; &times; 6 &times; 10 = 60&pi; &nbsp;&middot;&nbsp; "
                "curved cylinder: 2&pi;rh = 2&pi; &times; 6 &times; 15 = 180&pi; &nbsp;&middot;&nbsp; "
                "base: &pi;r<sup>2</sup> = 36&pi;",
                "Total = 60&pi; + 180&pi; + 36&pi; = 276&pi; = 867.08&hellip; cm<sup>2</sup>",
            ],
            "answer": "(a) 8 cm &nbsp;&nbsp; (b) 1998 cm<sup>3</sup> &nbsp;&nbsp; (c) 867 cm<sup>2</sup>",
        },
    ],
}

VECTORS = {
    "title": "Vectors",
    "folder": "gcse/geometry",
    "slug": "vectors-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write the translation &lsquo;3 units right and 2 units down&rsquo; as a column vector.</p>",
            "steps": [
                "The top number is the horizontal move (right is positive).",
                "The bottom number is the vertical move (down is negative).",
            ],
            "answer": col("3", "&minus;2"),
        },
        {
            "marks": 2,
            "q": "<p>Work out " + col("2", "5") + " + " + col("3", "&minus;1") + "</p>",
            "steps": [
                "Add the top numbers and add the bottom numbers separately.",
                "Top: 2 + 3 = 5",
                "Bottom: 5 + (&minus;1) = 4",
            ],
            "answer": col("5", "4"),
        },
        {
            "marks": 2,
            "q": "<p>Work out " + col("6", "2") + " &minus; " + col("1", "5") + "</p>",
            "steps": [
                "Subtract the top numbers and the bottom numbers separately.",
                "Top: 6 &minus; 1 = 5",
                "Bottom: 2 &minus; 5 = &minus;3",
            ],
            "answer": col("5", "&minus;3"),
        },
        {
            "marks": 2,
            "q": "<p>Work out 3" + col("2", "&minus;4") + "</p>",
            "steps": [
                "Multiply both numbers in the vector by 3.",
                "3 &times; 2 = 6 and 3 &times; (&minus;4) = &minus;12",
            ],
            "answer": col("6", "&minus;12"),
        },
        {
            "marks": 3,
            "q": "<p><b>a</b> = " + col("3", "1") + " and <b>b</b> = " + col("&minus;2", "4") + "</p>"
                 "<p>Work out <b>a</b> + 2<b>b</b></p>",
            "steps": [
                "First work out 2<b>b</b>: 2 &times; (&minus;2) = &minus;4 and 2 &times; 4 = 8, giving " + col("&minus;4", "8"),
                "Now add <b>a</b>: top 3 + (&minus;4) = &minus;1",
                "Bottom: 1 + 8 = 9",
            ],
            "answer": col("&minus;1", "9"),
        },
        {
            "marks": 3,
            "q": "<p><b>a</b> = " + col("3", "1") + " and <b>b</b> = " + col("&minus;2", "4") + "</p>"
                 "<p>Work out 2<b>a</b> &minus; <b>b</b></p>",
            "steps": [
                "2<b>a</b> = " + col("6", "2"),
                "Subtracting <b>b</b> means subtracting &minus;2 and 4.",
                "Top: 6 &minus; (&minus;2) = 8",
                "Bottom: 2 &minus; 4 = &minus;2",
            ],
            "answer": col("8", "&minus;2"),
        },
        {
            "marks": 3,
            "q": "<p>A is the point (1, 2). A is translated by " + col("4", "&minus;3") + " to give B.</p>"
                 "<p class='part'>(a) Write down the coordinates of B.</p>"
                 "<p class='part'>(b) Write down the vector that would translate B back to A.</p>",
            "steps": [
                "<b>(a)</b> <i>x</i>: 1 + 4 = 5 and <i>y</i>: 2 + (&minus;3) = &minus;1, so B is (5, &minus;1)",
                "<b>(b)</b> Going back undoes the move, so change the sign of both numbers.",
                "The vector is " + col("&minus;4", "3"),
            ],
            "answer": "(a) (5, &minus;1) &nbsp;&nbsp; (b) " + col("&minus;4", "3"),
        },
        {
            "marks": 3,
            "q": "<p>Work out the magnitude (length) of</p>"
                 "<p class='part'>(a) " + col("6", "8") + " &nbsp;&nbsp; (b) " + col("5", "12") + "</p>",
            "steps": [
                "Use Pythagoras: magnitude = &radic;(<i>x</i><sup>2</sup> + <i>y</i><sup>2</sup>)",
                "<b>(a)</b> &radic;(36 + 64) = &radic;100 = 10",
                "<b>(b)</b> &radic;(25 + 144) = &radic;169 = 13",
            ],
            "answer": "(a) 10 &nbsp;&nbsp; (b) 13",
        },
        {
            "marks": 4,
            "q": "<p>The vector from O to A is " + col("2", "3") + " and the vector from O to B is "
                 + col("5", "7") + "</p>"
                 "<p class='part'>(a) Work out the vector from A to B.</p>"
                 "<p class='part'>(b) Work out the length of AB.</p>",
            "steps": [
                "<b>(a)</b> To go from A to B, travel back to O then out to B.",
                "AB = &minus;OA + OB = OB &minus; OA",
                "Top: 5 &minus; 2 = 3 and bottom: 7 &minus; 3 = 4, giving " + col("3", "4"),
                "<b>(b)</b> Length = &radic;(3<sup>2</sup> + 4<sup>2</sup>) = &radic;25 = 5",
            ],
            "answer": "(a) " + col("3", "4") + " &nbsp;&nbsp; (b) 5",
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) Show that " + col("4", "6") + " and " + col("6", "9")
                 + " are parallel.</p>"
                 "<p class='part'>(b) Write " + col("10", "15") + " as a multiple of " + col("2", "3") + "</p>",
            "steps": [
                "Two vectors are parallel when one is a multiple of the other.",
                "<b>(a)</b> 6 &divide; 4 = 1.5 and 9 &divide; 6 = 1.5",
                "Both numbers scale by the same factor, so " + col("6", "9") + " = 1.5" + col("4", "6")
                + " and the vectors are parallel.",
                "<b>(b)</b> 10 &divide; 2 = 5 and 15 &divide; 3 = 5",
                "So " + col("10", "15") + " = 5" + col("2", "3"),
            ],
            "answer": "(a) the second is 1.5 times the first &nbsp;&nbsp; (b) 5" + col("2", "3"),
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p><b>a</b> = " + col("4", "&minus;1") + " and <b>b</b> = " + col("&minus;2", "3") + "</p>"
                 "<p>Work out 3<b>a</b> + 2<b>b</b></p>",
            "steps": [
                "3<b>a</b> = " + col("12", "&minus;3") + " and 2<b>b</b> = " + col("&minus;4", "6"),
                "Top: 12 + (&minus;4) = 8 and bottom: &minus;3 + 6 = 3",
            ],
            "answer": col("8", "3"),
        },
        {
            "marks": 2,
            "q": "<p>Work out the magnitude of " + col("&minus;7", "24") + "</p>",
            "steps": [
                "Magnitude = &radic;((&minus;7)<sup>2</sup> + 24<sup>2</sup>)",
                "= &radic;(49 + 576) = &radic;625 = 25",
                "Squaring removes the minus sign, so a magnitude is never negative.",
            ],
            "answer": "25",
        },
        {
            "marks": 3,
            "q": "<p>In triangle OAB, the vector from O to A is <b>a</b> and the vector from O to B "
                 "is <b>b</b>.</p>"
                 "<p>Write the vector from A to B in terms of <b>a</b> and <b>b</b>.</p>",
            "steps": [
                "There is no direct information about AB, so build a route through O.",
                "AB = AO + OB",
                "AO is the reverse of OA, so AO = &minus;<b>a</b>",
            ],
            "answer": "<b>b</b> &minus; <b>a</b>",
        },
        {
            "marks": 3,
            "q": "<p>In triangle OAB, OA = <b>a</b> and OB = <b>b</b>. M is the midpoint of AB.</p>"
                 "<p>Write the vector from O to M in terms of <b>a</b> and <b>b</b>.</p>",
            "steps": [
                "Travel from O to A, then half way along AB.",
                "AB = <b>b</b> &minus; <b>a</b>, so AM = " + frac("1", "2") + "(<b>b</b> &minus; <b>a</b>)",
                "OM = <b>a</b> + " + frac("1", "2") + "(<b>b</b> &minus; <b>a</b>) = " + frac("1", "2") + "<b>a</b> + " + frac("1", "2") + "<b>b</b>",
            ],
            "answer": frac("1", "2") + "(<b>a</b> + <b>b</b>)",
        },
        {
            "marks": 4,
            "q": "<p>In triangle OAB, OA = <b>a</b> and OB = <b>b</b>. P lies on AB so that AP : PB = 1 : 3</p>"
                 "<p>Write the vector from O to P in terms of <b>a</b> and <b>b</b>.</p>",
            "steps": [
                "AP : PB = 1 : 3 means AB is split into 4 equal parts, and P is 1 part along.",
                "So AP = " + frac("1", "4") + "AB = " + frac("1", "4") + "(<b>b</b> &minus; <b>a</b>)",
                "OP = OA + AP = <b>a</b> + " + frac("1", "4") + "(<b>b</b> &minus; <b>a</b>)",
                "Expand: <b>a</b> &minus; " + frac("1", "4") + "<b>a</b> + " + frac("1", "4") + "<b>b</b>",
                "= " + frac("3", "4") + "<b>a</b> + " + frac("1", "4") + "<b>b</b>",
            ],
            "answer": frac("3", "4") + "<b>a</b> + " + frac("1", "4") + "<b>b</b>",
        },
        {
            "marks": 4,
            "q": "<p>OC = 3<b>a</b> + 2<b>b</b> and OD = 6<b>a</b> + 4<b>b</b>.</p>"
                 "<p>Show that O, C and D lie on the same straight line.</p>",
            "steps": [
                "Look for a multiple linking the two vectors.",
                "6<b>a</b> + 4<b>b</b> = 2(3<b>a</b> + 2<b>b</b>)",
                "So OD = 2 &times; OC.",
                "Because OD is a multiple of OC, the two vectors are parallel.",
                "They also both start at O, so the three points must lie on one straight line "
                "(with D twice as far from O as C).",
            ],
            "answer": "OD = 2 OC, so the vectors are parallel and share the point O, making O, C and D collinear",
        },
        {
            "marks": 4,
            "q": "<p>OA = 2<b>a</b> + <b>b</b>, OB = 4<b>a</b> + 3<b>b</b> and OC = 7<b>a</b> + 6<b>b</b>.</p>"
                 "<p>Show that A, B and C lie on the same straight line.</p>",
            "steps": [
                "Find the vectors between the points, not just from O.",
                "AB = OB &minus; OA = (4<b>a</b> + 3<b>b</b>) &minus; (2<b>a</b> + <b>b</b>) = 2<b>a</b> + 2<b>b</b>",
                "BC = OC &minus; OB = (7<b>a</b> + 6<b>b</b>) &minus; (4<b>a</b> + 3<b>b</b>) = 3<b>a</b> + 3<b>b</b>",
                "BC = 1.5(2<b>a</b> + 2<b>b</b>) = 1.5 AB, so AB and BC are parallel.",
                "They share the point B, so A, B and C are collinear.",
            ],
            "answer": "AB = 2<b>a</b> + 2<b>b</b> and BC = 1.5 AB, so the points are collinear",
        },
        {
            "marks": 4,
            "q": "<p>OACB is a parallelogram with OA = <b>a</b> and OB = <b>b</b>.</p>"
                 "<p>M is the midpoint of AC.</p>"
                 "<p>Write the vector from O to M in terms of <b>a</b> and <b>b</b>.</p>",
            "steps": [
                "In parallelogram OACB, the side AC is parallel and equal to OB.",
                "So AC = <b>b</b>",
                "M is the midpoint of AC, so AM = " + frac("1", "2") + "<b>b</b>",
                "OM = OA + AM = <b>a</b> + " + frac("1", "2") + "<b>b</b>",
            ],
            "answer": "<b>a</b> + " + frac("1", "2") + "<b>b</b>",
        },
        {
            "marks": 4,
            "q": "<p>In triangle OAB, OA = <b>a</b> and OB = <b>b</b>. P lies on AB with AP : PB = 2 : 3</p>"
                 "<p>Show that OP = " + frac("1", "5") + "(3<b>a</b> + 2<b>b</b>)</p>",
            "steps": [
                "AB is divided into 2 + 3 = 5 equal parts and P is 2 parts along from A.",
                "AP = " + frac("2", "5") + "(<b>b</b> &minus; <b>a</b>)",
                "OP = <b>a</b> + " + frac("2", "5") + "(<b>b</b> &minus; <b>a</b>)",
                "= <b>a</b> &minus; " + frac("2", "5") + "<b>a</b> + " + frac("2", "5") + "<b>b</b> = " + frac("3", "5") + "<b>a</b> + " + frac("2", "5") + "<b>b</b>",
                "Taking out the factor " + frac("1", "5") + " gives " + frac("1", "5") + "(3<b>a</b> + 2<b>b</b>) as required.",
            ],
            "answer": "OP = " + frac("3", "5") + "<b>a</b> + " + frac("2", "5") + "<b>b</b> = " + frac("1", "5") + "(3<b>a</b> + 2<b>b</b>)",
        },
        {
            "marks": 5,
            "q": "<p>OABC is a parallelogram with OA = <b>a</b> and OC = <b>c</b>.</p>"
                 "<p>M is the midpoint of AB and N is the midpoint of BC.</p>"
                 "<p class='part'>(a) Write OM in terms of <b>a</b> and <b>c</b>.</p>"
                 "<p class='part'>(b) Write ON in terms of <b>a</b> and <b>c</b>.</p>"
                 "<p class='part'>(c) Show that MN is parallel to AC, and state the ratio of their lengths.</p>",
            "steps": [
                "<b>(a)</b> In the parallelogram, AB is parallel and equal to OC, so AB = <b>c</b>.",
                "M is halfway along AB, so OM = <b>a</b> + " + frac("1", "2") + "<b>c</b>",
                "<b>(b)</b> Likewise CB is parallel and equal to OA, so CB = <b>a</b>.",
                "N is halfway along CB, so ON = <b>c</b> + " + frac("1", "2") + "<b>a</b>",
                "<b>(c)</b> MN = ON &minus; OM = (<b>c</b> + " + frac("1", "2") + "<b>a</b>) &minus; (<b>a</b> + " + frac("1", "2") + "<b>c</b>)",
                "= " + frac("1", "2") + "<b>c</b> &minus; " + frac("1", "2") + "<b>a</b> = " + frac("1", "2") + "(<b>c</b> &minus; <b>a</b>)",
                "AC = OC &minus; OA = <b>c</b> &minus; <b>a</b>, so MN = " + frac("1", "2") + "AC.",
                "MN is a multiple of AC, so they are parallel, and MN is half the length of AC (ratio 1 : 2).",
            ],
            "answer": "(a) <b>a</b> + " + frac("1", "2") + "<b>c</b> &nbsp;&nbsp; (b) " + frac("1", "2")
                      + "<b>a</b> + <b>c</b> &nbsp;&nbsp; (c) MN = " + frac("1", "2") + "AC, so parallel with "
                      "lengths in the ratio 1 : 2",
        },
    ],
}

PAPERS = [ANGLES, PYTHAG_TRIG, CIRCLE_THEOREMS, TRANSFORMATIONS, AREA_VOLUME, VECTORS]
