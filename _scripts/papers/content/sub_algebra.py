"""GCSE practice papers — major Algebra subtopics."""
from build import frac

EQUATIONS = {
    "title": "Solving Equations",
    "folder": "gcse/algebra",
    "slug": "equations-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Solve <i>x</i> + 7 = 12</p>",
            "steps": [
                "Undo the +7 by subtracting 7 from both sides.",
                "<i>x</i> = 12 &minus; 7 = 5",
            ],
            "answer": "<i>x</i> = 5",
        },
        {
            "marks": 2,
            "q": "<p>Solve</p>"
                 "<p class='part'>(a) 3<i>x</i> = 21</p>"
                 "<p class='part'>(b) " + frac("<i>x</i>", "4") + " = 5</p>",
            "steps": [
                "<b>(a)</b> Undo the &times;3 by dividing both sides by 3: <i>x</i> = 7",
                "<b>(b)</b> Undo the &divide;4 by multiplying both sides by 4: <i>x</i> = 20",
            ],
            "answer": "(a) <i>x</i> = 7 &nbsp;&nbsp; (b) <i>x</i> = 20",
        },
        {
            "marks": 2,
            "q": "<p>Solve 2<i>x</i> + 5 = 17</p>",
            "steps": [
                "Deal with the +5 first: subtract 5 from both sides to get 2<i>x</i> = 12",
                "Now divide both sides by 2: <i>x</i> = 6",
            ],
            "answer": "<i>x</i> = 6",
        },
        {
            "marks": 2,
            "q": "<p>Solve 5<i>x</i> &minus; 3 = 22</p>",
            "steps": [
                "Add 3 to both sides: 5<i>x</i> = 25",
                "Divide both sides by 5: <i>x</i> = 5",
                "Check: 5 &times; 5 &minus; 3 = 22 &#10003;",
            ],
            "answer": "<i>x</i> = 5",
        },
        {
            "marks": 3,
            "q": "<p>Solve 4<i>x</i> + 1 = 2<i>x</i> + 11</p>",
            "steps": [
                "Get all the <i>x</i> terms on one side. Subtract 2<i>x</i> from both sides.",
                "2<i>x</i> + 1 = 11",
                "Subtract 1 from both sides: 2<i>x</i> = 10",
                "Divide by 2: <i>x</i> = 5",
            ],
            "answer": "<i>x</i> = 5",
        },
        {
            "marks": 3,
            "q": "<p>Solve 3(<i>x</i> + 4) = 27</p>",
            "steps": [
                "The quickest route is to divide both sides by 3 first: <i>x</i> + 4 = 9",
                "Subtract 4: <i>x</i> = 5",
                "(Expanding first also works: 3<i>x</i> + 12 = 27, so 3<i>x</i> = 15 and <i>x</i> = 5.)",
            ],
            "answer": "<i>x</i> = 5",
        },
        {
            "marks": 3,
            "q": "<p>Solve " + frac("<i>x</i> + 5", "3") + " = 4</p>",
            "steps": [
                "Multiply both sides by 3 to clear the fraction: <i>x</i> + 5 = 12",
                "Subtract 5 from both sides: <i>x</i> = 7",
                "Check: (7 + 5) &divide; 3 = 4 &#10003;",
            ],
            "answer": "<i>x</i> = 7",
        },
        {
            "marks": 3,
            "q": "<p>Solve 7 &minus; 2<i>x</i> = 1</p>",
            "steps": [
                "Add 2<i>x</i> to both sides so the <i>x</i> term becomes positive: 7 = 1 + 2<i>x</i>",
                "Subtract 1 from both sides: 6 = 2<i>x</i>",
                "Divide by 2: <i>x</i> = 3",
                "Check: 7 &minus; 2 &times; 3 = 7 &minus; 6 = 1 &#10003;",
            ],
            "answer": "<i>x</i> = 3",
        },
        {
            "marks": 4,
            "q": "<p>The three angles of a triangle are <i>x</i>&deg;, 2<i>x</i>&deg; and (3<i>x</i> + 30)&deg;.</p>"
                 "<p class='part'>(a) Form an equation in <i>x</i> and solve it.</p>"
                 "<p class='part'>(b) Work out the size of each angle.</p>",
            "steps": [
                "<b>(a)</b> The angles of a triangle add up to 180&deg;.",
                "<i>x</i> + 2<i>x</i> + 3<i>x</i> + 30 = 180, which simplifies to 6<i>x</i> + 30 = 180",
                "6<i>x</i> = 150, so <i>x</i> = 25",
                "<b>(b)</b> The angles are 25&deg;, 2 &times; 25 = 50&deg; and 3 &times; 25 + 30 = 105&deg;",
                "Check: 25 + 50 + 105 = 180 &#10003;",
            ],
            "answer": "(a) <i>x</i> = 25 &nbsp;&nbsp; (b) 25&deg;, 50&deg; and 105&deg;",
        },
        {
            "marks": 4,
            "q": "<p>A rectangle has length (3<i>x</i> &minus; 1) cm and width (<i>x</i> + 2) cm.</p>"
                 "<p>The perimeter is 42 cm.</p>"
                 "<p class='part'>(a) Find the value of <i>x</i>.</p>"
                 "<p class='part'>(b) Work out the area of the rectangle.</p>",
            "steps": [
                "<b>(a)</b> Perimeter = 2 &times; (length + width) = 2[(3<i>x</i> &minus; 1) + (<i>x</i> + 2)]",
                "Inside the bracket: 4<i>x</i> + 1, so the perimeter is 8<i>x</i> + 2",
                "8<i>x</i> + 2 = 42, so 8<i>x</i> = 40 and <i>x</i> = 5",
                "<b>(b)</b> Length = 3 &times; 5 &minus; 1 = 14 cm and width = 5 + 2 = 7 cm",
                "Area = 14 &times; 7 = 98 cm<sup>2</sup> (check: perimeter 2(14 + 7) = 42 &#10003;)",
            ],
            "answer": "(a) <i>x</i> = 5 &nbsp;&nbsp; (b) 98 cm<sup>2</sup>",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Solve 5<i>x</i> + 2 = 3<i>x</i> + 14</p>",
            "steps": [
                "Subtract 3<i>x</i> from both sides: 2<i>x</i> + 2 = 14",
                "Subtract 2: 2<i>x</i> = 12, so <i>x</i> = 6",
            ],
            "answer": "<i>x</i> = 6",
        },
        {
            "marks": 2,
            "q": "<p>Solve 2(3<i>x</i> &minus; 1) = 4<i>x</i> + 8</p>",
            "steps": [
                "Expand the bracket: 6<i>x</i> &minus; 2 = 4<i>x</i> + 8",
                "Subtract 4<i>x</i>: 2<i>x</i> &minus; 2 = 8, so 2<i>x</i> = 10 and <i>x</i> = 5",
            ],
            "answer": "<i>x</i> = 5",
        },
        {
            "marks": 3,
            "q": "<p>Solve " + frac("2<i>x</i> &minus; 1", "5") + " = " + frac("<i>x</i> + 4", "3") + "</p>",
            "steps": [
                "Cross-multiply to clear both fractions: 3(2<i>x</i> &minus; 1) = 5(<i>x</i> + 4)",
                "Expand both sides: 6<i>x</i> &minus; 3 = 5<i>x</i> + 20",
                "Subtract 5<i>x</i>: <i>x</i> &minus; 3 = 20",
                "<i>x</i> = 23",
            ],
            "answer": "<i>x</i> = 23",
        },
        {
            "marks": 3,
            "q": "<p>Solve " + frac("<i>x</i>", "2") + " + " + frac("<i>x</i>", "3") + " = 10</p>",
            "steps": [
                "Multiply every term by 6, the lowest common multiple of 2 and 3.",
                "6 &times; " + frac("<i>x</i>", "2") + " = 3<i>x</i> and 6 &times; " + frac("<i>x</i>", "3") + " = 2<i>x</i>",
                "3<i>x</i> + 2<i>x</i> = 60, so 5<i>x</i> = 60",
                "<i>x</i> = 12 (check: 6 + 4 = 10 &#10003;)",
            ],
            "answer": "<i>x</i> = 12",
        },
        {
            "marks": 4,
            "q": "<p>Solve " + frac("3", "<i>x</i> + 1") + " = " + frac("2", "<i>x</i> &minus; 3") + "</p>",
            "steps": [
                "Cross-multiply: 3(<i>x</i> &minus; 3) = 2(<i>x</i> + 1)",
                "Expand: 3<i>x</i> &minus; 9 = 2<i>x</i> + 2",
                "Subtract 2<i>x</i>: <i>x</i> &minus; 9 = 2",
                "<i>x</i> = 11",
                "Check: " + frac("3", "12") + " = 0.25 and " + frac("2", "8") + " = 0.25 &#10003;",
            ],
            "answer": "<i>x</i> = 11",
        },
        {
            "marks": 4,
            "q": "<p>Make l the subject of the formula</p>"
                 "<p>&nbsp;&nbsp;T = 2&pi;&radic;(" + frac("l", "g") + ")</p>",
            "steps": [
                "Divide both sides by 2&pi;: " + frac("T", "2&pi;") + " = &radic;(" + frac("l", "g") + ")",
                "Square both sides to remove the square root: " + frac("T<sup>2</sup>", "4&pi;<sup>2</sup>") + " = " + frac("l", "g"),
                "Remember that squaring 2&pi; gives 4&pi;<sup>2</sup>, not 2&pi;<sup>2</sup>.",
                "Multiply both sides by g.",
            ],
            "answer": "l = " + frac("gT<sup>2</sup>", "4&pi;<sup>2</sup>"),
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) Show that the equation <i>x</i><sup>2</sup> &minus; <i>x</i> &minus; 5 = 0 "
                 "can be rearranged to give <i>x</i> = &radic;(5 + <i>x</i>)</p>"
                 "<p class='part'>(b) Starting with <i>x</i><sub>0</sub> = 2, use the iteration "
                 "<i>x</i><sub>n+1</sub> = &radic;(5 + <i>x</i><sub>n</sub>) three times. "
                 "Give each value to 4 decimal places.</p>",
            "steps": [
                "<b>(a)</b> Move the &minus;<i>x</i> and &minus;5 across: <i>x</i><sup>2</sup> = <i>x</i> + 5",
                "Take the (positive) square root of both sides: <i>x</i> = &radic;(5 + <i>x</i>)",
                "<b>(b)</b> <i>x</i><sub>1</sub> = &radic;(5 + 2) = &radic;7 = 2.6458",
                "<i>x</i><sub>2</sub> = &radic;(5 + 2.6458) = &radic;7.6458 = 2.7651",
                "<i>x</i><sub>3</sub> = &radic;(5 + 2.7651) = &radic;7.7651 = 2.7866",
                "The values are settling down towards the root, which is about 2.7913",
            ],
            "answer": "(b) <i>x</i><sub>1</sub> = 2.6458, <i>x</i><sub>2</sub> = 2.7651, <i>x</i><sub>3</sub> = 2.7866",
        },
        {
            "marks": 4,
            "q": "<p>Solve " + frac("<i>x</i> + 2", "4") + " &minus; " + frac("<i>x</i> &minus; 3", "6") + " = 1</p>",
            "steps": [
                "Multiply every term by 12, the lowest common multiple of 4 and 6.",
                "3(<i>x</i> + 2) &minus; 2(<i>x</i> &minus; 3) = 12",
                "Expand carefully &mdash; the minus sign multiplies both terms in the second bracket.",
                "3<i>x</i> + 6 &minus; 2<i>x</i> + 6 = 12",
                "<i>x</i> + 12 = 12, so <i>x</i> = 0",
                "Check: " + frac("2", "4") + " &minus; " + frac("&minus;3", "6") + " = 0.5 + 0.5 = 1 &#10003;",
            ],
            "answer": "<i>x</i> = 0",
        },
        {
            "marks": 4,
            "q": "<p>The three angles of a triangle are (2<i>x</i> + 10)&deg;, (3<i>x</i> &minus; 20)&deg; "
                 "and (<i>x</i> + 40)&deg;.</p>"
                 "<p class='part'>(a) Show that 6<i>x</i> + 30 = 180</p>"
                 "<p class='part'>(b) Work out the size of the largest angle.</p>",
            "steps": [
                "<b>(a)</b> Add the three expressions: 2<i>x</i> + 3<i>x</i> + <i>x</i> = 6<i>x</i>",
                "The numbers: 10 &minus; 20 + 40 = 30",
                "The angles of a triangle total 180&deg;, so 6<i>x</i> + 30 = 180",
                "<b>(b)</b> 6<i>x</i> = 150, so <i>x</i> = 25",
                "The angles are 2(25) + 10 = 60&deg;, 3(25) &minus; 20 = 55&deg; and 25 + 40 = 65&deg;",
                "Check: 60 + 55 + 65 = 180 &#10003;, and the largest is 65&deg;",
            ],
            "answer": "(b) 65&deg;",
        },
        {
            "marks": 5,
            "q": "<p class='part'>(a) Solve " + frac("2<i>x</i> + 3", "3") + " + " + frac("<i>x</i> &minus; 1", "2") + " = 4</p>"
                 "<p class='part'>(b) When 5 is added to a number and the result is doubled, the answer is the "
                 "same as multiplying the number by 3 and then subtracting 1. Find the number.</p>",
            "steps": [
                "<b>(a)</b> Multiply every term by 6: 2(2<i>x</i> + 3) + 3(<i>x</i> &minus; 1) = 24",
                "Expand: 4<i>x</i> + 6 + 3<i>x</i> &minus; 3 = 24",
                "Collect: 7<i>x</i> + 3 = 24, so 7<i>x</i> = 21 and <i>x</i> = 3",
                "<b>(b)</b> Call the number n. &lsquo;Add 5 then double&rsquo; is 2(n + 5).",
                "&lsquo;Multiply by 3 then subtract 1&rsquo; is 3n &minus; 1, so 2(n + 5) = 3n &minus; 1",
                "2n + 10 = 3n &minus; 1, so n = 11. Check: 2 &times; 16 = 32 and 3 &times; 11 &minus; 1 = 32 &#10003;",
            ],
            "answer": "(a) <i>x</i> = 3 &nbsp;&nbsp; (b) 11",
        },
    ],
}

BRACKETS = {
    "title": "Expanding and Factorising",
    "folder": "gcse/algebra",
    "slug": "brackets-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Expand 3(<i>x</i> + 2)</p>",
            "steps": [
                "Multiply both terms inside the bracket by 3.",
                "3 &times; <i>x</i> = 3<i>x</i> and 3 &times; 2 = 6",
            ],
            "answer": "3<i>x</i> + 6",
        },
        {
            "marks": 2,
            "q": "<p>Expand</p>"
                 "<p class='part'>(a) 5(2<i>x</i> &minus; 3)</p>"
                 "<p class='part'>(b) <i>x</i>(<i>x</i> + 7)</p>",
            "steps": [
                "<b>(a)</b> 5 &times; 2<i>x</i> = 10<i>x</i> and 5 &times; (&minus;3) = &minus;15",
                "<b>(b)</b> <i>x</i> &times; <i>x</i> = <i>x</i><sup>2</sup> and <i>x</i> &times; 7 = 7<i>x</i>",
            ],
            "answer": "(a) 10<i>x</i> &minus; 15 &nbsp;&nbsp; (b) <i>x</i><sup>2</sup> + 7<i>x</i>",
        },
        {
            "marks": 2,
            "q": "<p>Expand and simplify 2(<i>x</i> + 4) + 3(<i>x</i> &minus; 1)</p>",
            "steps": [
                "Expand each bracket: 2<i>x</i> + 8 and 3<i>x</i> &minus; 3",
                "Collect the <i>x</i> terms: 2<i>x</i> + 3<i>x</i> = 5<i>x</i>",
                "Collect the numbers: 8 &minus; 3 = 5",
            ],
            "answer": "5<i>x</i> + 5",
        },
        {
            "marks": 2,
            "q": "<p>Factorise 6<i>x</i> + 9</p>",
            "steps": [
                "The highest common factor of 6 and 9 is 3.",
                "6<i>x</i> &divide; 3 = 2<i>x</i> and 9 &divide; 3 = 3",
            ],
            "answer": "3(2<i>x</i> + 3)",
        },
        {
            "marks": 3,
            "q": "<p>Factorise fully</p>"
                 "<p class='part'>(a) 10<i>x</i> &minus; 15</p>"
                 "<p class='part'>(b) <i>x</i><sup>2</sup> &minus; 6<i>x</i></p>"
                 "<p class='part'>(c) 12<i>ab</i> + 8<i>b</i></p>",
            "steps": [
                "<b>(a)</b> The highest common factor is 5: 5(2<i>x</i> &minus; 3)",
                "<b>(b)</b> Both terms contain <i>x</i>: <i>x</i>(<i>x</i> &minus; 6)",
                "<b>(c)</b> The numbers share 4 and both terms contain <i>b</i>, so take out 4<i>b</i>.",
                "12<i>ab</i> &divide; 4<i>b</i> = 3<i>a</i> and 8<i>b</i> &divide; 4<i>b</i> = 2",
            ],
            "answer": "(a) 5(2<i>x</i> &minus; 3) &nbsp;&nbsp; (b) <i>x</i>(<i>x</i> &minus; 6) &nbsp;&nbsp; (c) 4<i>b</i>(3<i>a</i> + 2)",
        },
        {
            "marks": 3,
            "q": "<p>Expand and simplify (<i>x</i> + 3)(<i>x</i> + 4)</p>",
            "steps": [
                "Multiply every term in the first bracket by every term in the second.",
                "<i>x</i> &times; <i>x</i> = <i>x</i><sup>2</sup>, &nbsp; <i>x</i> &times; 4 = 4<i>x</i>",
                "3 &times; <i>x</i> = 3<i>x</i>, &nbsp; 3 &times; 4 = 12",
                "Collect the middle terms: 4<i>x</i> + 3<i>x</i> = 7<i>x</i>",
            ],
            "answer": "<i>x</i><sup>2</sup> + 7<i>x</i> + 12",
        },
        {
            "marks": 3,
            "q": "<p>Expand and simplify 4(2<i>x</i> &minus; 1) &minus; 3(<i>x</i> &minus; 5)</p>",
            "steps": [
                "First bracket: 4 &times; 2<i>x</i> = 8<i>x</i> and 4 &times; (&minus;1) = &minus;4",
                "Second bracket: be careful, the &minus;3 multiplies both terms.",
                "&minus;3 &times; <i>x</i> = &minus;3<i>x</i> and &minus;3 &times; (&minus;5) = +15",
                "Collect: 8<i>x</i> &minus; 3<i>x</i> = 5<i>x</i> and &minus;4 + 15 = 11",
            ],
            "answer": "5<i>x</i> + 11",
        },
        {
            "marks": 3,
            "q": "<p>Factorise <i>x</i><sup>2</sup> + 8<i>x</i> + 15</p>",
            "steps": [
                "Find two numbers that multiply to 15 and add to 8.",
                "Options for 15: 1 &times; 15 (sum 16) and 3 &times; 5 (sum 8) &#10003;",
                "So the brackets are (<i>x</i> + 3)(<i>x</i> + 5)",
                "Check by expanding: <i>x</i><sup>2</sup> + 5<i>x</i> + 3<i>x</i> + 15 = <i>x</i><sup>2</sup> + 8<i>x</i> + 15 &#10003;",
            ],
            "answer": "(<i>x</i> + 3)(<i>x</i> + 5)",
        },
        {
            "marks": 4,
            "q": "<p>Expand and simplify</p>"
                 "<p class='part'>(a) (<i>x</i> &minus; 2)(<i>x</i> + 6)</p>"
                 "<p class='part'>(b) (2<i>x</i> + 1)(<i>x</i> &minus; 3)</p>",
            "steps": [
                "<b>(a)</b> <i>x</i><sup>2</sup> + 6<i>x</i> &minus; 2<i>x</i> &minus; 12",
                "Collect: 6<i>x</i> &minus; 2<i>x</i> = 4<i>x</i>, giving <i>x</i><sup>2</sup> + 4<i>x</i> &minus; 12",
                "<b>(b)</b> 2<i>x</i> &times; <i>x</i> = 2<i>x</i><sup>2</sup>, &nbsp; 2<i>x</i> &times; (&minus;3) = &minus;6<i>x</i>",
                "1 &times; <i>x</i> = <i>x</i>, &nbsp; 1 &times; (&minus;3) = &minus;3",
                "Collect: &minus;6<i>x</i> + <i>x</i> = &minus;5<i>x</i>",
            ],
            "answer": "(a) <i>x</i><sup>2</sup> + 4<i>x</i> &minus; 12 &nbsp;&nbsp; (b) 2<i>x</i><sup>2</sup> &minus; 5<i>x</i> &minus; 3",
        },
        {
            "marks": 4,
            "q": "<p>A rectangle has length (<i>x</i> + 5) cm and width (<i>x</i> + 2) cm.</p>"
                 "<p class='part'>(a) Show that the area of the rectangle is "
                 "<i>x</i><sup>2</sup> + 7<i>x</i> + 10 cm<sup>2</sup>.</p>"
                 "<p class='part'>(b) A square of side <i>x</i> cm is cut out of the rectangle. Write down a "
                 "simplified expression for the area that is left.</p>",
            "steps": [
                "<b>(a)</b> Area = (<i>x</i> + 5)(<i>x</i> + 2)",
                "Expanding: <i>x</i><sup>2</sup> + 2<i>x</i> + 5<i>x</i> + 10",
                "Collect the middle terms: <i>x</i><sup>2</sup> + 7<i>x</i> + 10 as required.",
                "<b>(b)</b> The square has area <i>x</i> &times; <i>x</i> = <i>x</i><sup>2</sup> cm<sup>2</sup>",
                "Remaining area = (<i>x</i><sup>2</sup> + 7<i>x</i> + 10) &minus; <i>x</i><sup>2</sup> = 7<i>x</i> + 10",
            ],
            "answer": "(b) (7<i>x</i> + 10) cm<sup>2</sup>",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Expand and simplify (<i>x</i> + 4)(<i>x</i> &minus; 4)</p>",
            "steps": [
                "<i>x</i><sup>2</sup> &minus; 4<i>x</i> + 4<i>x</i> &minus; 16",
                "The two middle terms cancel out &mdash; this is the difference of two squares.",
            ],
            "answer": "<i>x</i><sup>2</sup> &minus; 16",
        },
        {
            "marks": 2,
            "q": "<p>Factorise <i>x</i><sup>2</sup> &minus; 81</p>",
            "steps": [
                "There is no <i>x</i> term and 81 = 9<sup>2</sup>, so use the difference of two squares.",
                "a<sup>2</sup> &minus; b<sup>2</sup> = (a + b)(a &minus; b) with a = <i>x</i> and b = 9",
            ],
            "answer": "(<i>x</i> + 9)(<i>x</i> &minus; 9)",
        },
        {
            "marks": 3,
            "q": "<p>Expand and simplify (2<i>x</i> &minus; 3)<sup>2</sup></p>",
            "steps": [
                "A square means the bracket multiplied by itself: (2<i>x</i> &minus; 3)(2<i>x</i> &minus; 3)",
                "2<i>x</i> &times; 2<i>x</i> = 4<i>x</i><sup>2</sup>",
                "The two cross terms: 2<i>x</i> &times; (&minus;3) = &minus;6<i>x</i>, twice, giving &minus;12<i>x</i>",
                "(&minus;3) &times; (&minus;3) = +9",
            ],
            "answer": "4<i>x</i><sup>2</sup> &minus; 12<i>x</i> + 9",
        },
        {
            "marks": 3,
            "q": "<p>Factorise 3<i>x</i><sup>2</sup> + 10<i>x</i> + 8</p>",
            "steps": [
                "Multiply the end numbers: 3 &times; 8 = 24. Find two numbers multiplying to 24 and adding to 10: 6 and 4.",
                "Split the middle term: 3<i>x</i><sup>2</sup> + 6<i>x</i> + 4<i>x</i> + 8",
                "Factorise in pairs: 3<i>x</i>(<i>x</i> + 2) + 4(<i>x</i> + 2)",
                "Both pairs share (<i>x</i> + 2), so the answer is (3<i>x</i> + 4)(<i>x</i> + 2)",
            ],
            "answer": "(3<i>x</i> + 4)(<i>x</i> + 2)",
        },
        {
            "marks": 4,
            "q": "<p>Expand and simplify (<i>x</i> + 2)(<i>x</i> &minus; 1)(<i>x</i> + 3)</p>",
            "steps": [
                "Multiply the first two brackets: (<i>x</i> + 2)(<i>x</i> &minus; 1) = <i>x</i><sup>2</sup> + <i>x</i> &minus; 2",
                "Now multiply that by (<i>x</i> + 3), term by term.",
                "<i>x</i>(<i>x</i><sup>2</sup> + <i>x</i> &minus; 2) = <i>x</i><sup>3</sup> + <i>x</i><sup>2</sup> &minus; 2<i>x</i>",
                "3(<i>x</i><sup>2</sup> + <i>x</i> &minus; 2) = 3<i>x</i><sup>2</sup> + 3<i>x</i> &minus; 6",
                "Add and collect: <i>x</i><sup>3</sup> + 4<i>x</i><sup>2</sup> + <i>x</i> &minus; 6",
            ],
            "answer": "<i>x</i><sup>3</sup> + 4<i>x</i><sup>2</sup> + <i>x</i> &minus; 6",
        },
        {
            "marks": 4,
            "q": "<p>Factorise fully</p>"
                 "<p class='part'>(a) 2<i>x</i><sup>2</sup> &minus; 18</p>"
                 "<p class='part'>(b) 4<i>x</i><sup>2</sup> &minus; 20<i>x</i> + 24</p>",
            "steps": [
                "<b>(a)</b> Take out the common factor 2 first: 2(<i>x</i><sup>2</sup> &minus; 9)",
                "The bracket is a difference of two squares: 2(<i>x</i> + 3)(<i>x</i> &minus; 3)",
                "<b>(b)</b> Take out 4: 4(<i>x</i><sup>2</sup> &minus; 5<i>x</i> + 6)",
                "Two numbers multiplying to 6 and adding to &minus;5 are &minus;2 and &minus;3.",
                "So the answer is 4(<i>x</i> &minus; 2)(<i>x</i> &minus; 3)",
            ],
            "answer": "(a) 2(<i>x</i> + 3)(<i>x</i> &minus; 3) &nbsp;&nbsp; (b) 4(<i>x</i> &minus; 2)(<i>x</i> &minus; 3)",
        },
        {
            "marks": 4,
            "q": "<p>Factorise 6<i>x</i><sup>2</sup> &minus; <i>x</i> &minus; 12</p>",
            "steps": [
                "Multiply the end numbers: 6 &times; (&minus;12) = &minus;72",
                "Find two numbers multiplying to &minus;72 and adding to &minus;1: &minus;9 and +8",
                "Split the middle term: 6<i>x</i><sup>2</sup> &minus; 9<i>x</i> + 8<i>x</i> &minus; 12",
                "Factorise in pairs: 3<i>x</i>(2<i>x</i> &minus; 3) + 4(2<i>x</i> &minus; 3)",
                "So the answer is (3<i>x</i> + 4)(2<i>x</i> &minus; 3)",
            ],
            "answer": "(3<i>x</i> + 4)(2<i>x</i> &minus; 3)",
        },
        {
            "marks": 4,
            "q": "<p>Simplify fully &nbsp;" + frac("2<i>x</i><sup>2</sup> + 7<i>x</i> + 3", "<i>x</i><sup>2</sup> &minus; 9") + "</p>",
            "steps": [
                "Factorise the top: 2 &times; 3 = 6, and 6 and 1 multiply to 6 and add to 7.",
                "2<i>x</i><sup>2</sup> + 6<i>x</i> + <i>x</i> + 3 = 2<i>x</i>(<i>x</i> + 3) + 1(<i>x</i> + 3) = (2<i>x</i> + 1)(<i>x</i> + 3)",
                "Factorise the bottom as a difference of two squares: (<i>x</i> + 3)(<i>x</i> &minus; 3)",
                "Cancel the common factor (<i>x</i> + 3).",
            ],
            "answer": frac("2<i>x</i> + 1", "<i>x</i> &minus; 3"),
        },
        {
            "marks": 4,
            "q": "<p>Prove that (n + 3)<sup>2</sup> &minus; (n + 1)<sup>2</sup> is always a multiple of 4 "
                 "for any integer n.</p>",
            "steps": [
                "Expand each square separately.",
                "(n + 3)<sup>2</sup> = n<sup>2</sup> + 6n + 9",
                "(n + 1)<sup>2</sup> = n<sup>2</sup> + 2n + 1",
                "Subtract: (n<sup>2</sup> + 6n + 9) &minus; (n<sup>2</sup> + 2n + 1) = 4n + 8",
                "Factorise: 4n + 8 = 4(n + 2)",
                "Since n + 2 is an integer, the result is 4 &times; an integer, so it is always a multiple of 4.",
            ],
            "answer": "4(n + 2), which is a multiple of 4 for every integer n",
        },
        {
            "marks": 5,
            "q": "<p class='part'>(a) Expand and simplify (2n + 1)<sup>2</sup> &minus; (2n &minus; 1)<sup>2</sup></p>"
                 "<p class='part'>(b) Hence explain why the difference between the squares of any two "
                 "consecutive odd numbers is always a multiple of 8.</p>",
            "steps": [
                "<b>(a)</b> (2n + 1)<sup>2</sup> = 4n<sup>2</sup> + 4n + 1",
                "(2n &minus; 1)<sup>2</sup> = 4n<sup>2</sup> &minus; 4n + 1",
                "Subtracting: (4n<sup>2</sup> + 4n + 1) &minus; (4n<sup>2</sup> &minus; 4n + 1) = 8n",
                "<b>(b)</b> 2n &minus; 1 and 2n + 1 are consecutive odd numbers for any integer n.",
                "Part (a) shows their squares differ by 8n.",
                "Since n is an integer, 8n is always a multiple of 8.",
            ],
            "answer": "(a) 8n &nbsp;&nbsp; (b) consecutive odd numbers can be written as 2n &minus; 1 and 2n + 1, "
                      "and their squares differ by 8n",
        },
    ],
}

SIMULTANEOUS = {
    "title": "Simultaneous Equations",
    "folder": "gcse/algebra",
    "slug": "simultaneous-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p><i>x</i> + <i>y</i> = 10 and <i>x</i> = 4</p>"
                 "<p>Work out the value of <i>y</i>.</p>",
            "steps": [
                "Substitute <i>x</i> = 4 into the first equation: 4 + <i>y</i> = 10",
                "<i>y</i> = 6",
            ],
            "answer": "<i>y</i> = 6",
        },
        {
            "marks": 2,
            "q": "<p>Solve</p><p class='part'><i>x</i> + <i>y</i> = 9</p><p class='part'><i>x</i> &minus; <i>y</i> = 3</p>",
            "steps": [
                "The <i>y</i> terms are +<i>y</i> and &minus;<i>y</i>, so <b>add</b> the equations.",
                "2<i>x</i> = 12, so <i>x</i> = 6",
                "Substitute back: 6 + <i>y</i> = 9, so <i>y</i> = 3",
            ],
            "answer": "<i>x</i> = 6, <i>y</i> = 3",
        },
        {
            "marks": 2,
            "q": "<p>Solve</p><p class='part'>3<i>x</i> + <i>y</i> = 17</p><p class='part'>&nbsp;&nbsp;<i>x</i> + <i>y</i> = 7</p>",
            "steps": [
                "Both equations have +<i>y</i>, so <b>subtract</b> the second from the first.",
                "2<i>x</i> = 10, so <i>x</i> = 5",
                "Substitute: 5 + <i>y</i> = 7, so <i>y</i> = 2",
            ],
            "answer": "<i>x</i> = 5, <i>y</i> = 2",
        },
        {
            "marks": 2,
            "q": "<p>Solve</p><p class='part'>4<i>x</i> + <i>y</i> = 14</p><p class='part'>2<i>x</i> + <i>y</i> = 8</p>",
            "steps": [
                "Subtract the second equation from the first to remove <i>y</i>.",
                "2<i>x</i> = 6, so <i>x</i> = 3",
                "Substitute into 2<i>x</i> + <i>y</i> = 8: 6 + <i>y</i> = 8, so <i>y</i> = 2",
            ],
            "answer": "<i>x</i> = 3, <i>y</i> = 2",
        },
        {
            "marks": 3,
            "q": "<p>Solve</p><p class='part'>2<i>x</i> + 3<i>y</i> = 16</p><p class='part'>2<i>x</i> + &nbsp;<i>y</i> = 8</p>",
            "steps": [
                "The <i>x</i> terms match, so subtract the second equation from the first.",
                "3<i>y</i> &minus; <i>y</i> = 2<i>y</i> and 16 &minus; 8 = 8, so 2<i>y</i> = 8",
                "<i>y</i> = 4",
                "Substitute into 2<i>x</i> + <i>y</i> = 8: 2<i>x</i> + 4 = 8, so <i>x</i> = 2",
            ],
            "answer": "<i>x</i> = 2, <i>y</i> = 4",
        },
        {
            "marks": 3,
            "q": "<p>Solve</p><p class='part'>5<i>x</i> &minus; 2<i>y</i> = 4</p><p class='part'>3<i>x</i> + 2<i>y</i> = 12</p>",
            "steps": [
                "The <i>y</i> terms are &minus;2<i>y</i> and +2<i>y</i>, so <b>add</b> the equations.",
                "8<i>x</i> = 16, so <i>x</i> = 2",
                "Substitute into 3<i>x</i> + 2<i>y</i> = 12: 6 + 2<i>y</i> = 12",
                "2<i>y</i> = 6, so <i>y</i> = 3",
            ],
            "answer": "<i>x</i> = 2, <i>y</i> = 3",
        },
        {
            "marks": 3,
            "q": "<p>Solve</p><p class='part'>&nbsp;<i>x</i> + 3<i>y</i> = 14</p><p class='part'>2<i>x</i> + &nbsp;<i>y</i> = 13</p>",
            "steps": [
                "Neither pair matches, so multiply the first equation by 2 to match the <i>x</i> terms.",
                "2<i>x</i> + 6<i>y</i> = 28",
                "Subtract the second equation: 5<i>y</i> = 15, so <i>y</i> = 3",
                "Substitute into <i>x</i> + 3<i>y</i> = 14: <i>x</i> + 9 = 14, so <i>x</i> = 5",
                "Check in the other equation: 2(5) + 3 = 13 &#10003;",
            ],
            "answer": "<i>x</i> = 5, <i>y</i> = 3",
        },
        {
            "marks": 3,
            "q": "<p>Solve</p><p class='part'><i>y</i> = 2<i>x</i> + 1</p><p class='part'>3<i>x</i> + <i>y</i> = 16</p>",
            "steps": [
                "The first equation already gives <i>y</i>, so substitute it into the second.",
                "3<i>x</i> + (2<i>x</i> + 1) = 16",
                "5<i>x</i> + 1 = 16, so 5<i>x</i> = 15 and <i>x</i> = 3",
                "<i>y</i> = 2(3) + 1 = 7",
            ],
            "answer": "<i>x</i> = 3, <i>y</i> = 7",
        },
        {
            "marks": 4,
            "q": "<p>3 coffees and 2 teas cost &pound;10.40</p>"
                 "<p>1 coffee and 2 teas cost &pound;6.00</p>"
                 "<p>Work out the cost of one coffee and the cost of one tea.</p>",
            "steps": [
                "Let c be the cost of a coffee and t the cost of a tea.",
                "3c + 2t = 10.40 and c + 2t = 6.00",
                "Both have +2t, so subtract: 2c = 4.40",
                "c = &pound;2.20",
                "Substitute: 2.20 + 2t = 6.00, so 2t = 3.80 and t = &pound;1.90",
                "Check: 3(2.20) + 2(1.90) = 6.60 + 3.80 = &pound;10.40 &#10003;",
            ],
            "answer": "coffee &pound;2.20, tea &pound;1.90",
        },
        {
            "marks": 4,
            "q": "<p>At a cinema, 2 adult tickets and 3 child tickets cost &pound;34.50</p>"
                 "<p>3 adult tickets and 2 child tickets cost &pound;38.00</p>"
                 "<p>Work out the cost of one adult ticket and one child ticket.</p>",
            "steps": [
                "Let a be the adult price and c the child price.",
                "2a + 3c = 34.50 and 3a + 2c = 38.00",
                "Multiply the first by 3 and the second by 2 to match the a terms.",
                "6a + 9c = 103.50 and 6a + 4c = 76.00",
                "Subtract: 5c = 27.50, so c = &pound;5.50",
                "Substitute: 2a + 16.50 = 34.50, so 2a = 18 and a = &pound;9.00",
            ],
            "answer": "adult &pound;9.00, child &pound;5.50",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Solve</p><p class='part'>3<i>x</i> + 2<i>y</i> = 12</p><p class='part'>&nbsp;<i>x</i> &minus; 2<i>y</i> = 4</p>",
            "steps": [
                "Add the equations to eliminate <i>y</i>: 4<i>x</i> = 16",
                "<i>x</i> = 4",
                "Substitute: 4 &minus; 2<i>y</i> = 4, so <i>y</i> = 0",
            ],
            "answer": "<i>x</i> = 4, <i>y</i> = 0",
        },
        {
            "marks": 2,
            "q": "<p>Solve</p><p class='part'><i>y</i> = 3<i>x</i> &minus; 2</p><p class='part'><i>y</i> = <i>x</i> + 6</p>",
            "steps": [
                "Both right-hand sides equal <i>y</i>, so set them equal: 3<i>x</i> &minus; 2 = <i>x</i> + 6",
                "2<i>x</i> = 8, so <i>x</i> = 4",
                "<i>y</i> = 4 + 6 = 10",
            ],
            "answer": "<i>x</i> = 4, <i>y</i> = 10",
        },
        {
            "marks": 3,
            "q": "<p>Solve</p><p class='part'>4<i>x</i> + 3<i>y</i> = 25</p><p class='part'>3<i>x</i> &minus; 2<i>y</i> = 6</p>",
            "steps": [
                "Multiply the first by 2 and the second by 3 so the <i>y</i> terms become 6<i>y</i> and &minus;6<i>y</i>.",
                "8<i>x</i> + 6<i>y</i> = 50 and 9<i>x</i> &minus; 6<i>y</i> = 18",
                "Add them: 17<i>x</i> = 68, so <i>x</i> = 4",
                "Substitute into 4<i>x</i> + 3<i>y</i> = 25: 16 + 3<i>y</i> = 25, so <i>y</i> = 3",
            ],
            "answer": "<i>x</i> = 4, <i>y</i> = 3",
        },
        {
            "marks": 3,
            "q": "<p>Solve</p><p class='part'>5<i>x</i> + 4<i>y</i> = 22</p><p class='part'>3<i>x</i> &minus; 2<i>y</i> = 0</p>",
            "steps": [
                "Multiply the second equation by 2: 6<i>x</i> &minus; 4<i>y</i> = 0",
                "Add to the first: 11<i>x</i> = 22, so <i>x</i> = 2",
                "Substitute into 3<i>x</i> &minus; 2<i>y</i> = 0: 6 = 2<i>y</i>, so <i>y</i> = 3",
                "Check: 5(2) + 4(3) = 10 + 12 = 22 &#10003;",
            ],
            "answer": "<i>x</i> = 2, <i>y</i> = 3",
        },
        {
            "marks": 4,
            "q": "<p>Solve</p><p class='part'><i>y</i> = <i>x</i><sup>2</sup> + 2</p><p class='part'><i>y</i> = 3<i>x</i> + 6</p>",
            "steps": [
                "Set the two expressions for <i>y</i> equal: <i>x</i><sup>2</sup> + 2 = 3<i>x</i> + 6",
                "Rearrange: <i>x</i><sup>2</sup> &minus; 3<i>x</i> &minus; 4 = 0",
                "Factorise: (<i>x</i> &minus; 4)(<i>x</i> + 1) = 0, so <i>x</i> = 4 or <i>x</i> = &minus;1",
                "Use the linear equation for the <i>y</i> values.",
                "<i>x</i> = 4 gives <i>y</i> = 18, and <i>x</i> = &minus;1 gives <i>y</i> = 3",
            ],
            "answer": "<i>x</i> = 4, <i>y</i> = 18 &nbsp;and&nbsp; <i>x</i> = &minus;1, <i>y</i> = 3",
        },
        {
            "marks": 4,
            "q": "<p>Solve</p><p class='part'><i>x</i><sup>2</sup> + <i>y</i><sup>2</sup> = 25</p>"
                 "<p class='part'><i>y</i> = <i>x</i> + 1</p>",
            "steps": [
                "Substitute <i>y</i> = <i>x</i> + 1 into the first equation.",
                "<i>x</i><sup>2</sup> + (<i>x</i> + 1)<sup>2</sup> = 25, and (<i>x</i> + 1)<sup>2</sup> = <i>x</i><sup>2</sup> + 2<i>x</i> + 1",
                "2<i>x</i><sup>2</sup> + 2<i>x</i> + 1 = 25, so 2<i>x</i><sup>2</sup> + 2<i>x</i> &minus; 24 = 0",
                "Divide by 2: <i>x</i><sup>2</sup> + <i>x</i> &minus; 12 = 0, which factorises as (<i>x</i> + 4)(<i>x</i> &minus; 3) = 0",
                "<i>x</i> = &minus;4 gives <i>y</i> = &minus;3, and <i>x</i> = 3 gives <i>y</i> = 4",
                "Check (3, 4): 9 + 16 = 25 &#10003;",
            ],
            "answer": "<i>x</i> = 3, <i>y</i> = 4 &nbsp;and&nbsp; <i>x</i> = &minus;4, <i>y</i> = &minus;3",
        },
        {
            "marks": 4,
            "q": "<p>4 small boxes and 3 large boxes have a total mass of 6.9 kg.</p>"
                 "<p>6 small boxes and 2 large boxes have a total mass of 7.6 kg.</p>"
                 "<p>Work out the mass of one small box and one large box.</p>",
            "steps": [
                "Let s and l be the masses in kilograms.",
                "4s + 3l = 6.9 and 6s + 2l = 7.6",
                "Multiply the first by 2 and the second by 3 to match the l terms.",
                "8s + 6l = 13.8 and 18s + 6l = 22.8",
                "Subtract: 10s = 9, so s = 0.9 kg",
                "Substitute: 3.6 + 3l = 6.9, so 3l = 3.3 and l = 1.1 kg",
            ],
            "answer": "small box 0.9 kg, large box 1.1 kg",
        },
        {
            "marks": 4,
            "q": "<p>Find the coordinates of the point where the line <i>y</i> = 2<i>x</i> + 3 crosses "
                 "the line 3<i>x</i> + 2<i>y</i> = 20</p>",
            "steps": [
                "The crossing point satisfies both equations, so solve them simultaneously.",
                "Substitute <i>y</i> = 2<i>x</i> + 3 into the second equation.",
                "3<i>x</i> + 2(2<i>x</i> + 3) = 20",
                "3<i>x</i> + 4<i>x</i> + 6 = 20, so 7<i>x</i> = 14 and <i>x</i> = 2",
                "<i>y</i> = 2(2) + 3 = 7",
                "Check: 3(2) + 2(7) = 6 + 14 = 20 &#10003;",
            ],
            "answer": "(2, 7)",
        },
        {
            "marks": 4,
            "q": "<p>Show that the line <i>y</i> = <i>x</i> + 5 is a tangent to the curve "
                 "<i>y</i> = <i>x</i><sup>2</sup> + 3<i>x</i> + 6, and find the point where they touch.</p>",
            "steps": [
                "Set the two expressions equal: <i>x</i><sup>2</sup> + 3<i>x</i> + 6 = <i>x</i> + 5",
                "Rearrange: <i>x</i><sup>2</sup> + 2<i>x</i> + 1 = 0",
                "Factorise: (<i>x</i> + 1)<sup>2</sup> = 0",
                "There is only one (repeated) solution, <i>x</i> = &minus;1, so the line meets the curve at exactly "
                "one point &mdash; that is what makes it a tangent.",
                "<i>y</i> = &minus;1 + 5 = 4, so they touch at (&minus;1, 4)",
            ],
            "answer": "Repeated root <i>x</i> = &minus;1, so it is a tangent, touching at (&minus;1, 4)",
        },
        {
            "marks": 5,
            "q": "<p>At a theatre, a group of 5 adults and 3 children pay &pound;55.</p>"
                 "<p>A group of 3 adults and 7 children pay &pound;59.</p>"
                 "<p class='part'>(a) Work out the price of an adult ticket and a child ticket.</p>"
                 "<p class='part'>(b) Work out the cost for 4 adults and 6 children.</p>",
            "steps": [
                "<b>(a)</b> Let a and c be the ticket prices in pounds.",
                "5a + 3c = 55 and 3a + 7c = 59",
                "Multiply the first by 7 and the second by 3 to match the c terms.",
                "35a + 21c = 385 and 9a + 21c = 177",
                "Subtract: 26a = 208, so a = &pound;8",
                "Substitute into 5a + 3c = 55: 40 + 3c = 55, so 3c = 15 and c = &pound;5",
                "<b>(b)</b> 4 &times; 8 + 6 &times; 5 = 32 + 30 = &pound;62",
            ],
            "answer": "(a) adult &pound;8, child &pound;5 &nbsp;&nbsp; (b) &pound;62",
        },
    ],
}

SEQUENCES = {
    "title": "Sequences",
    "folder": "gcse/algebra",
    "slug": "sequences-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write down the next term of this sequence.</p>"
                 "<p><b>4&nbsp;&nbsp; 9&nbsp;&nbsp; 14&nbsp;&nbsp; 19</b></p>",
            "steps": [
                "The sequence goes up by 5 each time.",
                "19 + 5 = 24",
            ],
            "answer": "24",
        },
        {
            "marks": 2,
            "q": "<p>Find an expression for the <i>n</i>th term of this sequence.</p>"
                 "<p><b>3&nbsp;&nbsp; 7&nbsp;&nbsp; 11&nbsp;&nbsp; 15</b></p>",
            "steps": [
                "The common difference is 4, so the <i>n</i>th term starts with 4<i>n</i>.",
                "4<i>n</i> gives 4, 8, 12, 16 &mdash; each is 1 more than the sequence.",
                "So subtract 1.",
            ],
            "answer": "4<i>n</i> &minus; 1",
        },
        {
            "marks": 2,
            "q": "<p>The <i>n</i>th term of a sequence is 5<i>n</i> + 2</p>"
                 "<p>Write down the first three terms.</p>",
            "steps": [
                "Substitute <i>n</i> = 1: 5(1) + 2 = 7",
                "<i>n</i> = 2: 5(2) + 2 = 12",
                "<i>n</i> = 3: 5(3) + 2 = 17",
            ],
            "answer": "7, 12, 17",
        },
        {
            "marks": 2,
            "q": "<p>Find the 10th term of the sequence</p>"
                 "<p><b>6&nbsp;&nbsp; 10&nbsp;&nbsp; 14&nbsp;&nbsp; 18&nbsp;&nbsp; &hellip;</b></p>",
            "steps": [
                "The common difference is 4, so the <i>n</i>th term is 4<i>n</i> + 2",
                "Substitute <i>n</i> = 10: 4(10) + 2",
                "= 42",
            ],
            "answer": "42",
        },
        {
            "marks": 3,
            "q": "<p>Here is a sequence.</p><p><b>20&nbsp;&nbsp; 17&nbsp;&nbsp; 14&nbsp;&nbsp; 11</b></p>"
                 "<p class='part'>(a) Write down the next two terms.</p>"
                 "<p class='part'>(b) Find an expression for the <i>n</i>th term.</p>"
                 "<p class='part'>(c) Is &minus;7 a term of this sequence? Give a reason.</p>",
            "steps": [
                "<b>(a)</b> The sequence goes down by 3 each time: 8 and 5",
                "<b>(b)</b> A difference of &minus;3 means the <i>n</i>th term contains &minus;3<i>n</i>.",
                "&minus;3<i>n</i> gives &minus;3, &minus;6, &minus;9&hellip;, and the sequence is 23 more each time, so the <i>n</i>th term is 23 &minus; 3<i>n</i>",
                "<b>(c)</b> Set 23 &minus; 3<i>n</i> = &minus;7, so 3<i>n</i> = 30 and <i>n</i> = 10",
                "<i>n</i> = 10 is a whole number, so yes &mdash; &minus;7 is the 10th term.",
            ],
            "answer": "(a) 8 and 5 &nbsp;&nbsp; (b) 23 &minus; 3<i>n</i> &nbsp;&nbsp; (c) Yes, it is the 10th term",
        },
        {
            "marks": 3,
            "q": "<p>Here is a sequence.</p><p><b>2&nbsp;&nbsp; 5&nbsp;&nbsp; 7&nbsp;&nbsp; 12&nbsp;&nbsp; 19</b></p>"
                 "<p class='part'>(a) Describe the rule for finding the next term.</p>"
                 "<p class='part'>(b) Write down the next two terms.</p>",
            "steps": [
                "<b>(a)</b> Check whether each term is the sum of the two before it: 2 + 5 = 7 &#10003;, "
                "5 + 7 = 12 &#10003;, 7 + 12 = 19 &#10003;",
                "The rule is: add the two previous terms.",
                "<b>(b)</b> 12 + 19 = 31",
                "19 + 31 = 50",
            ],
            "answer": "(a) add the previous two terms &nbsp;&nbsp; (b) 31 and 50",
        },
        {
            "marks": 3,
            "q": "<p>Here is a sequence.</p><p><b>3&nbsp;&nbsp; 6&nbsp;&nbsp; 12&nbsp;&nbsp; 24</b></p>"
                 "<p class='part'>(a) Describe the rule for finding the next term.</p>"
                 "<p class='part'>(b) Write down the next two terms.</p>"
                 "<p class='part'>(c) Work out the 7th term.</p>",
            "steps": [
                "<b>(a)</b> Each term is double the one before, so the rule is &lsquo;multiply by 2&rsquo;.",
                "<b>(b)</b> 24 &times; 2 = 48 and 48 &times; 2 = 96",
                "<b>(c)</b> Continue: the 6th term is 96 and the 7th is 96 &times; 2 = 192",
                "(Or use 3 &times; 2<sup>6</sup> = 3 &times; 64 = 192.)",
            ],
            "answer": "(a) multiply by 2 &nbsp;&nbsp; (b) 48 and 96 &nbsp;&nbsp; (c) 192",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Write down the first five square numbers.</p>"
                 "<p class='part'>(b) Write down the first five triangular numbers.</p>"
                 "<p class='part'>(c) Which number appears in both lists?</p>",
            "steps": [
                "<b>(a)</b> Square numbers come from 1<sup>2</sup>, 2<sup>2</sup>, 3<sup>2</sup>&hellip;: 1, 4, 9, 16, 25",
                "<b>(b)</b> Triangular numbers add 1, then 2, then 3&hellip;: 1, 3, 6, 10, 15",
                "<b>(c)</b> The number 1 appears in both lists.",
            ],
            "answer": "(a) 1, 4, 9, 16, 25 &nbsp;&nbsp; (b) 1, 3, 6, 10, 15 &nbsp;&nbsp; (c) 1",
        },
        {
            "marks": 4,
            "q": "<p>The <i>n</i>th term of a sequence is 3<i>n</i> + 4</p>"
                 "<p class='part'>(a) Show that 102 is not a term of the sequence.</p>"
                 "<p class='part'>(b) Find the largest term of the sequence that is less than 200.</p>",
            "steps": [
                "<b>(a)</b> Set 3<i>n</i> + 4 = 102, so 3<i>n</i> = 98",
                "<i>n</i> = 32.66&hellip;, which is not a whole number, so 102 cannot be a term.",
                "<b>(b)</b> Solve 3<i>n</i> + 4 &lt; 200, so 3<i>n</i> &lt; 196 and <i>n</i> &lt; 65.33&hellip;",
                "The largest whole number is <i>n</i> = 65",
                "The term is 3(65) + 4 = 199",
            ],
            "answer": "(a) 3<i>n</i> = 98 gives <i>n</i> = 32.6&hellip;, not a whole number &nbsp;&nbsp; (b) 199",
        },
        {
            "marks": 4,
            "q": "<p>Matchstick patterns are made as shown. Pattern 1 uses 4 matches, pattern 2 uses 7 matches "
                 "and pattern 3 uses 10 matches.</p>"
                 "<p class='part'>(a) Find an expression for the number of matches in pattern <i>n</i>.</p>"
                 "<p class='part'>(b) How many matches are needed for pattern 20?</p>"
                 "<p class='part'>(c) Which pattern uses exactly 100 matches?</p>",
            "steps": [
                "<b>(a)</b> The numbers 4, 7, 10 go up by 3, so the expression starts with 3<i>n</i>.",
                "3<i>n</i> gives 3, 6, 9 &mdash; each is 1 less than the pattern, so the expression is 3<i>n</i> + 1",
                "<b>(b)</b> 3(20) + 1 = 61 matches",
                "<b>(c)</b> 3<i>n</i> + 1 = 100, so 3<i>n</i> = 99 and <i>n</i> = 33",
            ],
            "answer": "(a) 3<i>n</i> + 1 &nbsp;&nbsp; (b) 61 &nbsp;&nbsp; (c) pattern 33",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Find an expression for the <i>n</i>th term of</p>"
                 "<p><b>2&nbsp;&nbsp; 9&nbsp;&nbsp; 16&nbsp;&nbsp; 23</b></p>",
            "steps": [
                "The common difference is 7, so start with 7<i>n</i>.",
                "7<i>n</i> gives 7, 14, 21 &mdash; each is 5 more than the sequence.",
            ],
            "answer": "7<i>n</i> &minus; 5",
        },
        {
            "marks": 2,
            "q": "<p>The <i>n</i>th term of a sequence is <i>n</i><sup>2</sup> + 3</p>"
                 "<p>Work out the 6th term.</p>",
            "steps": [
                "Substitute <i>n</i> = 6: 6<sup>2</sup> + 3",
                "= 36 + 3 = 39",
            ],
            "answer": "39",
        },
        {
            "marks": 3,
            "q": "<p>Find an expression for the <i>n</i>th term of the quadratic sequence</p>"
                 "<p><b>4&nbsp;&nbsp; 7&nbsp;&nbsp; 12&nbsp;&nbsp; 19&nbsp;&nbsp; 28</b></p>",
            "steps": [
                "First differences: 3, 5, 7, 9. Second differences: 2, 2, 2 &mdash; constant, so it is quadratic.",
                "Half of the second difference is 1, so the expression starts with <i>n</i><sup>2</sup>.",
                "<i>n</i><sup>2</sup> gives 1, 4, 9, 16, 25",
                "Subtracting: 4 &minus; 1 = 3, 7 &minus; 4 = 3, 12 &minus; 9 = 3&hellip; a constant 3.",
            ],
            "answer": "<i>n</i><sup>2</sup> + 3",
        },
        {
            "marks": 3,
            "q": "<p>Find an expression for the <i>n</i>th term of</p>"
                 "<p><b>5&nbsp;&nbsp; 12&nbsp;&nbsp; 23&nbsp;&nbsp; 38&nbsp;&nbsp; 57</b></p>",
            "steps": [
                "First differences: 7, 11, 15, 19. Second differences: 4, 4, 4.",
                "Half of 4 is 2, so the expression starts with 2<i>n</i><sup>2</sup>.",
                "2<i>n</i><sup>2</sup> gives 2, 8, 18, 32, 50",
                "Subtracting: 3, 4, 5, 6, 7 &mdash; a linear sequence with <i>n</i>th term <i>n</i> + 2",
                "Check <i>n</i> = 3: 2(9) + 3 + 2 = 23 &#10003;",
            ],
            "answer": "2<i>n</i><sup>2</sup> + <i>n</i> + 2",
        },
        {
            "marks": 4,
            "q": "<p>Here is a geometric sequence.</p><p><b>5&nbsp;&nbsp; 15&nbsp;&nbsp; 45&nbsp;&nbsp; &hellip;</b></p>"
                 "<p class='part'>(a) Write down the common ratio.</p>"
                 "<p class='part'>(b) Find an expression for the <i>n</i>th term.</p>"
                 "<p class='part'>(c) Work out the 8th term.</p>",
            "steps": [
                "<b>(a)</b> 15 &divide; 5 = 3 and 45 &divide; 15 = 3, so the common ratio is 3.",
                "<b>(b)</b> The first term is 5 and each step multiplies by 3.",
                "The <i>n</i>th term is 5 &times; 3<sup><i>n</i> &minus; 1</sup> (the power is <i>n</i> &minus; 1 because the first term uses 3<sup>0</sup> = 1).",
                "<b>(c)</b> 8th term = 5 &times; 3<sup>7</sup>",
                "3<sup>7</sup> = 2187, so the term is 5 &times; 2187 = 10 935",
            ],
            "answer": "(a) 3 &nbsp;&nbsp; (b) 5 &times; 3<sup><i>n</i> &minus; 1</sup> &nbsp;&nbsp; (c) 10 935",
        },
        {
            "marks": 4,
            "q": "<p>The <i>n</i>th term of a sequence is <i>n</i><sup>2</sup> + 2<i>n</i></p>"
                 "<p>Show that 168 is a term of the sequence and state its position.</p>",
            "steps": [
                "Set the expression equal to 168: <i>n</i><sup>2</sup> + 2<i>n</i> = 168",
                "Rearrange into a quadratic: <i>n</i><sup>2</sup> + 2<i>n</i> &minus; 168 = 0",
                "Two numbers multiplying to &minus;168 and adding to 2 are 14 and &minus;12.",
                "(<i>n</i> + 14)(<i>n</i> &minus; 12) = 0, so <i>n</i> = &minus;14 or <i>n</i> = 12",
                "A position must be a positive whole number, so <i>n</i> = 12",
                "Check: 12<sup>2</sup> + 2(12) = 144 + 24 = 168 &#10003;",
            ],
            "answer": "Yes &mdash; 168 is the 12th term",
        },
        {
            "marks": 4,
            "q": "<p>The <i>n</i>th term of a sequence is 5<i>n</i> &minus; 3</p>"
                 "<p class='part'>(a) Find the first term of the sequence that is greater than 500.</p>"
                 "<p class='part'>(b) Prove that every term of the sequence is 2 more than a multiple of 5.</p>",
            "steps": [
                "<b>(a)</b> Solve 5<i>n</i> &minus; 3 &gt; 500, so 5<i>n</i> &gt; 503 and <i>n</i> &gt; 100.6",
                "The first whole number is <i>n</i> = 101, giving 5(101) &minus; 3 = 502",
                "<b>(b)</b> Rewrite the expression: 5<i>n</i> &minus; 3 = 5<i>n</i> &minus; 5 + 2",
                "= 5(<i>n</i> &minus; 1) + 2",
                "Since <i>n</i> &minus; 1 is an integer, 5(<i>n</i> &minus; 1) is a multiple of 5, so every term is "
                "2 more than a multiple of 5.",
            ],
            "answer": "(a) 502 &nbsp;&nbsp; (b) 5<i>n</i> &minus; 3 = 5(<i>n</i> &minus; 1) + 2",
        },
        {
            "marks": 4,
            "q": "<p>A sequence is defined by <i>u</i><sub>1</sub> = 5 and "
                 "<i>u</i><sub>n+1</sub> = 2<i>u</i><sub>n</sub> &minus; 3</p>"
                 "<p class='part'>(a) Work out <i>u</i><sub>2</sub>, <i>u</i><sub>3</sub> and <i>u</i><sub>4</sub>.</p>"
                 "<p class='part'>(b) Describe what happens to the terms as <i>n</i> increases.</p>",
            "steps": [
                "<b>(a)</b> <i>u</i><sub>2</sub> = 2(5) &minus; 3 = 7",
                "<i>u</i><sub>3</sub> = 2(7) &minus; 3 = 11",
                "<i>u</i><sub>4</sub> = 2(11) &minus; 3 = 19",
                "<b>(b)</b> The gaps between terms (2, 4, 8&hellip;) keep doubling, so the terms grow faster and "
                "faster and increase without limit.",
            ],
            "answer": "(a) 7, 11, 19 &nbsp;&nbsp; (b) the terms increase, and the increases keep doubling, so the "
                      "sequence grows without limit",
        },
        {
            "marks": 4,
            "q": "<p>A pattern of dots grows like this: 1, 5, 13, 25, 41, &hellip;</p>"
                 "<p>Find an expression for the number of dots in the <i>n</i>th pattern.</p>",
            "steps": [
                "First differences: 4, 8, 12, 16. Second differences: 4, 4, 4 &mdash; so the sequence is quadratic.",
                "Half of 4 is 2, so start with 2<i>n</i><sup>2</sup>.",
                "2<i>n</i><sup>2</sup> gives 2, 8, 18, 32, 50",
                "Subtract from the sequence: 1 &minus; 2 = &minus;1, 5 &minus; 8 = &minus;3, 13 &minus; 18 = &minus;5, 25 &minus; 32 = &minus;7",
                "That leftover sequence &minus;1, &minus;3, &minus;5, &minus;7 has <i>n</i>th term 1 &minus; 2<i>n</i>",
                "Check <i>n</i> = 4: 2(16) &minus; 8 + 1 = 32 &minus; 7 = 25 &#10003;",
            ],
            "answer": "2<i>n</i><sup>2</sup> &minus; 2<i>n</i> + 1",
        },
        {
            "marks": 5,
            "q": "<p>The <i>n</i>th term of a sequence is <i>n</i><sup>2</sup> + 5<i>n</i></p>"
                 "<p class='part'>(a) Prove that every term of the sequence is an even number.</p>"
                 "<p class='part'>(b) Two consecutive terms of the sequence differ by 26. Find these two terms.</p>",
            "steps": [
                "<b>(a)</b> Factorise the expression: <i>n</i><sup>2</sup> + 5<i>n</i> = <i>n</i>(<i>n</i> + 5)",
                "If <i>n</i> is even, then <i>n</i>(<i>n</i> + 5) has an even factor, so the product is even.",
                "If <i>n</i> is odd, then <i>n</i> + 5 is even, so again the product is even.",
                "Either way the product is even, so every term is an even number.",
                "<b>(b)</b> The difference between consecutive terms is "
                "[(<i>n</i> + 1)<sup>2</sup> + 5(<i>n</i> + 1)] &minus; [<i>n</i><sup>2</sup> + 5<i>n</i>]",
                "= (<i>n</i><sup>2</sup> + 2<i>n</i> + 1 + 5<i>n</i> + 5) &minus; (<i>n</i><sup>2</sup> + 5<i>n</i>) = 2<i>n</i> + 6",
                "Set 2<i>n</i> + 6 = 26, so <i>n</i> = 10",
                "The terms are <i>u</i><sub>10</sub> = 100 + 50 = 150 and <i>u</i><sub>11</sub> = 121 + 55 = 176 "
                "(and 176 &minus; 150 = 26 &#10003;)",
            ],
            "answer": "(a) <i>n</i>(<i>n</i> + 5) always has an even factor &nbsp;&nbsp; (b) 150 and 176",
        },
    ],
}

INEQUALITIES = {
    "title": "Inequalities",
    "folder": "gcse/algebra",
    "slug": "inequalities-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>List all the integers n that satisfy &minus;2 &lt; n &le; 2</p>",
            "steps": [
                "The strict sign &lt; means &minus;2 itself is <b>not</b> included.",
                "The sign &le; means 2 <b>is</b> included.",
            ],
            "answer": "&minus;1, 0, 1, 2",
        },
        {
            "marks": 2,
            "q": "<p>Solve <i>x</i> + 5 &gt; 9</p>",
            "steps": [
                "Subtract 5 from both sides, exactly as you would for an equation.",
                "<i>x</i> &gt; 4",
            ],
            "answer": "<i>x</i> &gt; 4",
        },
        {
            "marks": 2,
            "q": "<p>Solve 3<i>x</i> &le; 21</p>",
            "steps": [
                "Divide both sides by 3.",
                "Because 3 is positive, the inequality sign stays the same way round.",
            ],
            "answer": "<i>x</i> &le; 7",
        },
        {
            "marks": 2,
            "q": "<p>Solve 2<i>x</i> &minus; 1 &lt; 11</p>",
            "steps": [
                "Add 1 to both sides: 2<i>x</i> &lt; 12",
                "Divide both sides by 2: <i>x</i> &lt; 6",
            ],
            "answer": "<i>x</i> &lt; 6",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Solve 5<i>x</i> + 3 &ge; 23</p>"
                 "<p class='part'>(b) Write down the smallest integer that satisfies the inequality.</p>",
            "steps": [
                "<b>(a)</b> Subtract 3 from both sides: 5<i>x</i> &ge; 20",
                "Divide by 5: <i>x</i> &ge; 4",
                "<b>(b)</b> The sign &ge; includes 4 itself, so the smallest integer is 4.",
            ],
            "answer": "(a) <i>x</i> &ge; 4 &nbsp;&nbsp; (b) 4",
        },
        {
            "marks": 3,
            "q": "<p>Solve 4(<i>x</i> &minus; 2) &le; 12</p>",
            "steps": [
                "Divide both sides by 4 first: <i>x</i> &minus; 2 &le; 3",
                "Add 2 to both sides: <i>x</i> &le; 5",
                "(Expanding first also works: 4<i>x</i> &minus; 8 &le; 12, so 4<i>x</i> &le; 20.)",
            ],
            "answer": "<i>x</i> &le; 5",
        },
        {
            "marks": 3,
            "q": "<p>Solve &minus;3 &lt; 2<i>x</i> + 1 &le; 9</p>",
            "steps": [
                "Whatever you do, do it to all three parts of the inequality.",
                "Subtract 1 throughout: &minus;4 &lt; 2<i>x</i> &le; 8",
                "Divide throughout by 2: &minus;2 &lt; <i>x</i> &le; 4",
            ],
            "answer": "&minus;2 &lt; <i>x</i> &le; 4",
        },
        {
            "marks": 3,
            "q": "<p>Solve 7 &minus; <i>x</i> &gt; 2</p>",
            "steps": [
                "The safest method is to add <i>x</i> to both sides: 7 &gt; 2 + <i>x</i>",
                "Subtract 2: 5 &gt; <i>x</i>, which is the same as <i>x</i> &lt; 5",
                "If instead you subtract 7 and get &minus;<i>x</i> &gt; &minus;5, remember that dividing by &minus;1 "
                "<b>flips</b> the sign to give <i>x</i> &lt; 5",
            ],
            "answer": "<i>x</i> &lt; 5",
        },
        {
            "marks": 4,
            "q": "<p>List all the integer values of n that satisfy 3 &le; 2n + 1 &lt; 13</p>",
            "steps": [
                "Subtract 1 from all three parts: 2 &le; 2n &lt; 12",
                "Divide all three parts by 2: 1 &le; n &lt; 6",
                "n = 1 is included because of the &le; sign.",
                "n = 6 is <b>not</b> included because of the &lt; sign.",
            ],
            "answer": "n = 1, 2, 3, 4, 5",
        },
        {
            "marks": 4,
            "q": "<p>A rectangle has width <i>x</i> cm and length (<i>x</i> + 4) cm.</p>"
                 "<p>The perimeter is less than 40 cm, and <i>x</i> is a whole number greater than 3.</p>"
                 "<p>Find all the possible values of <i>x</i>.</p>",
            "steps": [
                "Perimeter = 2[<i>x</i> + (<i>x</i> + 4)] = 2(2<i>x</i> + 4) = 4<i>x</i> + 8",
                "So 4<i>x</i> + 8 &lt; 40",
                "4<i>x</i> &lt; 32, giving <i>x</i> &lt; 8",
                "We are also told <i>x</i> &gt; 3, so 3 &lt; <i>x</i> &lt; 8",
                "The whole numbers strictly between 3 and 8 are 4, 5, 6 and 7.",
            ],
            "answer": "<i>x</i> = 4, 5, 6 or 7",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Solve 5 &minus; 2<i>x</i> &ge; 1</p>",
            "steps": [
                "Subtract 5 from both sides: &minus;2<i>x</i> &ge; &minus;4",
                "Divide both sides by &minus;2. Dividing by a negative <b>reverses</b> the inequality sign.",
                "<i>x</i> &le; 2",
            ],
            "answer": "<i>x</i> &le; 2",
        },
        {
            "marks": 2,
            "q": "<p>Solve 3(<i>x</i> + 2) &lt; 5<i>x</i> &minus; 4</p>",
            "steps": [
                "Expand: 3<i>x</i> + 6 &lt; 5<i>x</i> &minus; 4",
                "Subtract 3<i>x</i>: 6 &lt; 2<i>x</i> &minus; 4",
                "Add 4: 10 &lt; 2<i>x</i>, so 5 &lt; <i>x</i>, i.e. <i>x</i> &gt; 5",
            ],
            "answer": "<i>x</i> &gt; 5",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> &lt; 36</p>",
            "steps": [
                "Do not just write <i>x</i> &lt; 6 &mdash; negative values matter too.",
                "The critical values come from <i>x</i><sup>2</sup> = 36, so <i>x</i> = 6 or <i>x</i> = &minus;6",
                "Sketch <i>y</i> = <i>x</i><sup>2</sup> &minus; 36: a U-shaped curve crossing at &minus;6 and 6.",
                "It is below zero <b>between</b> the two roots.",
            ],
            "answer": "&minus;6 &lt; <i>x</i> &lt; 6",
        },
        {
            "marks": 3,
            "q": "<p>Solve <i>x</i><sup>2</sup> &ge; 49</p>",
            "steps": [
                "The critical values are <i>x</i> = 7 and <i>x</i> = &minus;7",
                "The curve <i>y</i> = <i>x</i><sup>2</sup> &minus; 49 is above (or on) the axis <b>outside</b> the roots.",
                "So the solution is in two separate pieces.",
            ],
            "answer": "<i>x</i> &le; &minus;7 &nbsp;or&nbsp; <i>x</i> &ge; 7",
        },
        {
            "marks": 4,
            "q": "<p>Solve <i>x</i><sup>2</sup> &minus; 2<i>x</i> &minus; 15 &lt; 0</p>",
            "steps": [
                "Factorise to find the critical values: two numbers multiplying to &minus;15 and adding to &minus;2 "
                "are &minus;5 and +3.",
                "(<i>x</i> &minus; 5)(<i>x</i> + 3) = 0 gives <i>x</i> = 5 and <i>x</i> = &minus;3",
                "Sketch the U-shaped curve crossing the axis at &minus;3 and 5.",
                "The curve is <b>below</b> the axis between the roots.",
            ],
            "answer": "&minus;3 &lt; <i>x</i> &lt; 5",
        },
        {
            "marks": 4,
            "q": "<p>Solve <i>x</i><sup>2</sup> + 4<i>x</i> &minus; 12 &ge; 0</p>",
            "steps": [
                "Factorise: two numbers multiplying to &minus;12 and adding to 4 are 6 and &minus;2.",
                "(<i>x</i> + 6)(<i>x</i> &minus; 2) = 0, so the critical values are &minus;6 and 2",
                "The U-shaped curve is above or on the axis outside the roots.",
                "Because the sign is &ge;, the critical values themselves are included.",
            ],
            "answer": "<i>x</i> &le; &minus;6 &nbsp;or&nbsp; <i>x</i> &ge; 2",
        },
        {
            "marks": 4,
            "q": "<p>Solve 2<i>x</i><sup>2</sup> &minus; 5<i>x</i> &minus; 3 &le; 0</p>",
            "steps": [
                "Multiply the end numbers: 2 &times; (&minus;3) = &minus;6. Two numbers multiplying to &minus;6 and "
                "adding to &minus;5 are &minus;6 and +1.",
                "2<i>x</i><sup>2</sup> &minus; 6<i>x</i> + <i>x</i> &minus; 3 = 2<i>x</i>(<i>x</i> &minus; 3) + 1(<i>x</i> &minus; 3) = (2<i>x</i> + 1)(<i>x</i> &minus; 3)",
                "Critical values: <i>x</i> = &minus;" + frac("1", "2") + " and <i>x</i> = 3",
                "The coefficient of <i>x</i><sup>2</sup> is positive, so the curve is below or on the axis between the roots.",
            ],
            "answer": "&minus;" + frac("1", "2") + " &le; <i>x</i> &le; 3",
        },
        {
            "marks": 4,
            "q": "<p>The region R is defined by the three inequalities</p>"
                 "<p class='part'><i>y</i> &ge; 1</p>"
                 "<p class='part'><i>y</i> &le; <i>x</i> + 2</p>"
                 "<p class='part'><i>x</i> + <i>y</i> &le; 6</p>"
                 "<p>Find the coordinates of the three corners of R.</p>",
            "steps": [
                "The corners are where each pair of boundary lines cross.",
                "<i>y</i> = 1 meets <i>y</i> = <i>x</i> + 2 when 1 = <i>x</i> + 2, so <i>x</i> = &minus;1 &rarr; (&minus;1, 1)",
                "<i>y</i> = 1 meets <i>x</i> + <i>y</i> = 6 when <i>x</i> + 1 = 6, so <i>x</i> = 5 &rarr; (5, 1)",
                "<i>y</i> = <i>x</i> + 2 meets <i>x</i> + <i>y</i> = 6: substitute to get <i>x</i> + <i>x</i> + 2 = 6",
                "2<i>x</i> = 4, so <i>x</i> = 2 and <i>y</i> = 4 &rarr; (2, 4)",
            ],
            "answer": "(&minus;1, 1), (5, 1) and (2, 4)",
        },
        {
            "marks": 4,
            "q": "<p>Kim has &pound;50. She buys a bag costing &pound;14 and wants to spend the rest on books "
                 "costing &pound;6.50 each.</p>"
                 "<p>Form an inequality and use it to find the greatest number of books she can buy.</p>",
            "steps": [
                "Let n be the number of books. The total spent must be at most &pound;50.",
                "14 + 6.5n &le; 50",
                "Subtract 14: 6.5n &le; 36",
                "Divide by 6.5: n &le; 5.538&hellip;",
                "n must be a whole number, so the greatest possible value is 5.",
                "Check: 14 + 5 &times; 6.50 = &pound;46.50, and 6 books would cost &pound;53 &mdash; too much.",
            ],
            "answer": "14 + 6.5n &le; 50, giving 5 books",
        },
        {
            "marks": 5,
            "q": "<p>Find all the integer values of <i>x</i> that satisfy <b>both</b> of these inequalities.</p>"
                 "<p class='part'><i>x</i><sup>2</sup> &minus; 16 &lt; 0</p>"
                 "<p class='part'>2<i>x</i> + 5 &ge; 1</p>",
            "steps": [
                "Solve each inequality separately, then find where the two solutions overlap.",
                "First: <i>x</i><sup>2</sup> &lt; 16, with critical values <i>x</i> = &minus;4 and <i>x</i> = 4",
                "A U-shaped curve is below the axis between its roots, so &minus;4 &lt; <i>x</i> &lt; 4",
                "Second: 2<i>x</i> &ge; &minus;4, so <i>x</i> &ge; &minus;2",
                "The overlap is &minus;2 &le; <i>x</i> &lt; 4",
                "The integers in that range are &minus;2, &minus;1, 0, 1, 2 and 3 (4 is excluded).",
            ],
            "answer": "<i>x</i> = &minus;2, &minus;1, 0, 1, 2, 3",
        },
    ],
}

PAPERS = [EQUATIONS, BRACKETS, SIMULTANEOUS, SEQUENCES, INEQUALITIES]
