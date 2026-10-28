"""GCSE practice paper — Algebra (topic level)."""
from build import frac

PAPER = {
    "title": "Algebra",
    "folder": "gcse/algebra",
    "slug": "algebra-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Simplify 5<i>a</i> + 3<i>a</i> &minus; 2<i>a</i></p>",
            "steps": [
                "All three terms are &lsquo;lots of <i>a</i>&rsquo;, so they are like terms and can be collected.",
                "Work with the numbers in front: 5 + 3 &minus; 2 = 6",
                "So the answer is 6<i>a</i>",
            ],
            "answer": "6<i>a</i>",
        },
        {
            "marks": 2,
            "q": "<p>Work out the value of</p>"
                 "<p class='part'>(a) 3<i>x</i> + 4 when <i>x</i> = 5</p>"
                 "<p class='part'>(b) 2<i>x</i><sup>2</sup> when <i>x</i> = 3</p>",
            "steps": [
                "<b>(a)</b> Replace <i>x</i> with 5: 3 &times; 5 + 4",
                "3 &times; 5 = 15, then 15 + 4 = 19",
                "<b>(b)</b> 2<i>x</i><sup>2</sup> means &lsquo;square <i>x</i> first, then double&rsquo; (BIDMAS &mdash; indices before multiplying).",
                "3<sup>2</sup> = 9, then 2 &times; 9 = 18",
            ],
            "answer": "(a) 19 &nbsp;&nbsp; (b) 18",
        },
        {
            "marks": 2,
            "q": "<p>Expand</p>"
                 "<p class='part'>(a) 4(<i>x</i> + 3)</p>"
                 "<p class='part'>(b) 3(2<i>y</i> &minus; 5)</p>",
            "steps": [
                "<b>(a)</b> Multiply <i>everything</i> inside the bracket by 4.",
                "4 &times; <i>x</i> = 4<i>x</i> and 4 &times; 3 = 12, giving 4<i>x</i> + 12",
                "<b>(b)</b> 3 &times; 2<i>y</i> = 6<i>y</i> and 3 &times; (&minus;5) = &minus;15",
                "Keep the minus sign: 6<i>y</i> &minus; 15",
            ],
            "answer": "(a) 4<i>x</i> + 12 &nbsp;&nbsp; (b) 6<i>y</i> &minus; 15",
        },
        {
            "marks": 2,
            "q": "<p>Solve 5<i>x</i> &minus; 7 = 23</p>",
            "steps": [
                "Undo the &minus;7 first by adding 7 to both sides: 5<i>x</i> = 30",
                "Undo the &times;5 by dividing both sides by 5: <i>x</i> = 6",
                "Check: 5 &times; 6 &minus; 7 = 30 &minus; 7 = 23 &#10003;",
            ],
            "answer": "<i>x</i> = 6",
        },
        {
            "marks": 3,
            "q": "<p>Factorise fully</p>"
                 "<p class='part'>(a) 6<i>x</i> + 15</p>"
                 "<p class='part'>(b) <i>x</i><sup>2</sup> + 7<i>x</i></p>"
                 "<p class='part'>(c) 8<i>ab</i> &minus; 12<i>a</i></p>",
            "steps": [
                "&lsquo;Factorise fully&rsquo; means take out the <i>highest</i> common factor.",
                "<b>(a)</b> 6 and 15 are both multiples of 3, so 6<i>x</i> + 15 = 3(2<i>x</i> + 5)",
                "<b>(b)</b> Both terms contain <i>x</i>, so <i>x</i><sup>2</sup> + 7<i>x</i> = <i>x</i>(<i>x</i> + 7)",
                "<b>(c)</b> The numbers share 4 and both terms share <i>a</i>, so the common factor is 4<i>a</i>.",
                "8<i>ab</i> &divide; 4<i>a</i> = 2<i>b</i> and 12<i>a</i> &divide; 4<i>a</i> = 3, giving 4<i>a</i>(2<i>b</i> &minus; 3)",
            ],
            "answer": "(a) 3(2<i>x</i> + 5) &nbsp;&nbsp; (b) <i>x</i>(<i>x</i> + 7) &nbsp;&nbsp; (c) 4<i>a</i>(2<i>b</i> &minus; 3)",
        },
        {
            "marks": 3,
            "q": "<p>Here are the first four terms of a sequence.</p>"
                 "<p><b>5&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;13&nbsp;&nbsp;&nbsp;17</b></p>"
                 "<p class='part'>(a) Write down the next two terms.</p>"
                 "<p class='part'>(b) Find an expression for the <i>n</i>th term.</p>"
                 "<p class='part'>(c) Is 100 a term of this sequence? You must give a reason.</p>",
            "steps": [
                "<b>(a)</b> The sequence goes up by 4 each time, so the next terms are 17 + 4 = 21 and 21 + 4 = 25",
                "<b>(b)</b> A constant difference of 4 means the <i>n</i>th term starts with 4<i>n</i>.",
                "4<i>n</i> gives 4, 8, 12, 16 &mdash; each is 1 less than the sequence, so the <i>n</i>th term is 4<i>n</i> + 1",
                "<b>(c)</b> Set 4<i>n</i> + 1 = 100, so 4<i>n</i> = 99 and <i>n</i> = 24.75",
                "<i>n</i> must be a whole number (you cannot have term number 24.75), so 100 is not in the sequence.",
            ],
            "answer": "(a) 21 and 25 &nbsp;&nbsp; (b) 4<i>n</i> + 1 &nbsp;&nbsp; (c) No &mdash; 4<i>n</i> + 1 = 100 gives <i>n</i> = 24.75, which is not a whole number",
        },
        {
            "marks": 3,
            "q": "<p>Solve 4(<i>x</i> &minus; 2) = 2<i>x</i> + 10</p>",
            "steps": [
                "Expand the bracket on the left: 4<i>x</i> &minus; 8 = 2<i>x</i> + 10",
                "Get the <i>x</i> terms on one side &mdash; subtract 2<i>x</i> from both sides: 2<i>x</i> &minus; 8 = 10",
                "Add 8 to both sides: 2<i>x</i> = 18",
                "Divide both sides by 2: <i>x</i> = 9",
                "Check: 4(9 &minus; 2) = 28 and 2 &times; 9 + 10 = 28 &#10003;",
            ],
            "answer": "<i>x</i> = 9",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Solve the inequality 5<i>x</i> &minus; 3 &le; 17</p>"
                 "<p class='part'>(b) Write down the largest integer that satisfies your inequality.</p>",
            "steps": [
                "<b>(a)</b> Treat it exactly like an equation. Add 3 to both sides: 5<i>x</i> &le; 20",
                "Divide both sides by 5. Because 5 is positive, the inequality sign does not flip: <i>x</i> &le; 4",
                "<b>(b)</b> <i>x</i> &le; 4 includes 4 itself, so the largest integer is 4.",
            ],
            "answer": "(a) <i>x</i> &le; 4 &nbsp;&nbsp; (b) 4",
        },
        {
            "marks": 4,
            "q": "<p>Solve the simultaneous equations</p>"
                 "<p class='part'>3<i>x</i> + <i>y</i> = 14</p>"
                 "<p class='part'>&nbsp;&nbsp;<i>x</i> + <i>y</i> = 6</p>",
            "steps": [
                "The <i>y</i> terms are identical (both +<i>y</i>), so <b>subtract</b> the second equation from the first.",
                "(3<i>x</i> &minus; <i>x</i>) + (<i>y</i> &minus; <i>y</i>) = 14 &minus; 6, which gives 2<i>x</i> = 8",
                "So <i>x</i> = 4",
                "Substitute <i>x</i> = 4 into the simpler equation <i>x</i> + <i>y</i> = 6: 4 + <i>y</i> = 6, so <i>y</i> = 2",
                "Check in the other equation: 3 &times; 4 + 2 = 14 &#10003;",
            ],
            "answer": "<i>x</i> = 4, <i>y</i> = 2",
        },
        {
            "marks": 5,
            "q": "<p>A rectangle has length (2<i>x</i> + 3) cm and width (<i>x</i> &minus; 1) cm.</p>"
                 "<p>The perimeter of the rectangle is 34 cm.</p>"
                 "<p class='part'>(a) Show that 6<i>x</i> + 4 = 34</p>"
                 "<p class='part'>(b) Solve your equation to find <i>x</i>.</p>"
                 "<p class='part'>(c) Work out the area of the rectangle.</p>",
            "steps": [
                "<b>(a)</b> Perimeter = 2 &times; (length + width) = 2[(2<i>x</i> + 3) + (<i>x</i> &minus; 1)]",
                "Inside the brackets: 2<i>x</i> + <i>x</i> = 3<i>x</i> and 3 &minus; 1 = 2, giving 2(3<i>x</i> + 2)",
                "Expanding: 6<i>x</i> + 4, and this equals the perimeter 34, so 6<i>x</i> + 4 = 34 as required.",
                "<b>(b)</b> 6<i>x</i> = 30, so <i>x</i> = 5",
                "<b>(c)</b> Length = 2 &times; 5 + 3 = 13 cm and width = 5 &minus; 1 = 4 cm.",
                "Area = 13 &times; 4 = 52 cm<sup>2</sup> (check: perimeter = 2(13 + 4) = 34 &#10003;)",
            ],
            "answer": "(b) <i>x</i> = 5 &nbsp;&nbsp; (c) 52 cm<sup>2</sup>",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Expand and simplify (<i>x</i> + 5)(<i>x</i> &minus; 3)</p>",
            "steps": [
                "Multiply every term in the first bracket by every term in the second.",
                "<i>x</i> &times; <i>x</i> = <i>x</i><sup>2</sup>, &nbsp; <i>x</i> &times; (&minus;3) = &minus;3<i>x</i>, &nbsp; 5 &times; <i>x</i> = 5<i>x</i>, &nbsp; 5 &times; (&minus;3) = &minus;15",
                "Collect the middle terms: &minus;3<i>x</i> + 5<i>x</i> = 2<i>x</i>",
            ],
            "answer": "<i>x</i><sup>2</sup> + 2<i>x</i> &minus; 15",
        },
        {
            "marks": 2,
            "q": "<p>Simplify</p>"
                 "<p class='part'>(a) <i>x</i><sup>5</sup> &times; <i>x</i><sup>3</sup></p>"
                 "<p class='part'>(b) (2<i>y</i><sup>3</sup>)<sup>4</sup></p>",
            "steps": [
                "<b>(a)</b> Multiplying powers of the same letter means <i>adding</i> the indices: 5 + 3 = 8, so <i>x</i><sup>8</sup>",
                "<b>(b)</b> Everything inside the bracket is raised to the power 4 &mdash; including the 2.",
                "2<sup>4</sup> = 16 and (<i>y</i><sup>3</sup>)<sup>4</sup> = <i>y</i><sup>12</sup> (multiply the indices).",
            ],
            "answer": "(a) <i>x</i><sup>8</sup> &nbsp;&nbsp; (b) 16<i>y</i><sup>12</sup>",
        },
        {
            "marks": 3,
            "q": "<p>Factorise</p>"
                 "<p class='part'>(a) <i>x</i><sup>2</sup> &minus; 49</p>"
                 "<p class='part'>(b) 2<i>x</i><sup>2</sup> + 7<i>x</i> + 3</p>",
            "steps": [
                "<b>(a)</b> This is the difference of two squares: <i>x</i><sup>2</sup> &minus; 7<sup>2</sup>",
                "So <i>x</i><sup>2</sup> &minus; 49 = (<i>x</i> + 7)(<i>x</i> &minus; 7)",
                "<b>(b)</b> Multiply the outer numbers: 2 &times; 3 = 6. Find two numbers multiplying to 6 and adding to 7 &mdash; that is 6 and 1.",
                "Split the middle term: 2<i>x</i><sup>2</sup> + 6<i>x</i> + <i>x</i> + 3",
                "Factorise in pairs: 2<i>x</i>(<i>x</i> + 3) + 1(<i>x</i> + 3) = (2<i>x</i> + 1)(<i>x</i> + 3)",
            ],
            "answer": "(a) (<i>x</i> + 7)(<i>x</i> &minus; 7) &nbsp;&nbsp; (b) (2<i>x</i> + 1)(<i>x</i> + 3)",
        },
        {
            "marks": 3,
            "q": "<p>Solve the simultaneous equations</p>"
                 "<p class='part'>3<i>x</i> + 2<i>y</i> = 19</p>"
                 "<p class='part'>5<i>x</i> &minus; 2<i>y</i> = 5</p>",
            "steps": [
                "The <i>y</i> terms are +2<i>y</i> and &minus;2<i>y</i>, so <b>adding</b> the equations eliminates <i>y</i>.",
                "(3<i>x</i> + 5<i>x</i>) + (2<i>y</i> &minus; 2<i>y</i>) = 19 + 5, giving 8<i>x</i> = 24",
                "So <i>x</i> = 3",
                "Substitute into 3<i>x</i> + 2<i>y</i> = 19: 9 + 2<i>y</i> = 19, so 2<i>y</i> = 10 and <i>y</i> = 5",
                "Check in the second equation: 5 &times; 3 &minus; 2 &times; 5 = 15 &minus; 10 = 5 &#10003;",
            ],
            "answer": "<i>x</i> = 3, <i>y</i> = 5",
        },
        {
            "marks": 3,
            "q": "<p>Make <i>x</i> the subject of the formula</p>"
                 "<p>&nbsp;&nbsp;<i>y</i> = " + frac("3<i>x</i> + 2", "<i>x</i> &minus; 1") + "</p>",
            "steps": [
                "Multiply both sides by (<i>x</i> &minus; 1) to clear the fraction: <i>y</i>(<i>x</i> &minus; 1) = 3<i>x</i> + 2",
                "Expand the left-hand side: <i>xy</i> &minus; <i>y</i> = 3<i>x</i> + 2",
                "Collect every term containing <i>x</i> on one side: <i>xy</i> &minus; 3<i>x</i> = <i>y</i> + 2",
                "Factorise the left-hand side: <i>x</i>(<i>y</i> &minus; 3) = <i>y</i> + 2",
                "Divide by (<i>y</i> &minus; 3): <i>x</i> = " + frac("<i>y</i> + 2", "<i>y</i> &minus; 3"),
            ],
            "answer": "<i>x</i> = " + frac("<i>y</i> + 2", "<i>y</i> &minus; 3"),
        },
        {
            "marks": 4,
            "q": "<p>Simplify fully</p>"
                 "<p>&nbsp;&nbsp;" + frac("<i>x</i><sup>2</sup> &minus; 9", "<i>x</i><sup>2</sup> + <i>x</i> &minus; 12") + "</p>",
            "steps": [
                "Factorise the top. It is the difference of two squares: <i>x</i><sup>2</sup> &minus; 9 = (<i>x</i> + 3)(<i>x</i> &minus; 3)",
                "Factorise the bottom. Two numbers multiplying to &minus;12 and adding to +1 are +4 and &minus;3.",
                "So <i>x</i><sup>2</sup> + <i>x</i> &minus; 12 = (<i>x</i> + 4)(<i>x</i> &minus; 3)",
                "The fraction becomes " + frac("(<i>x</i> + 3)(<i>x</i> &minus; 3)", "(<i>x</i> + 4)(<i>x</i> &minus; 3)"),
                "Cancel the common factor (<i>x</i> &minus; 3) from top and bottom.",
            ],
            "answer": frac("<i>x</i> + 3", "<i>x</i> + 4"),
        },
        {
            "marks": 4,
            "q": "<p>f(<i>x</i>) = 3<i>x</i> &minus; 1 &nbsp;&nbsp;and&nbsp;&nbsp; g(<i>x</i>) = <i>x</i><sup>2</sup> + 2</p>"
                 "<p class='part'>(a) Work out fg(2)</p>"
                 "<p class='part'>(b) Find gf(<i>x</i>), giving your answer in the form a<i>x</i><sup>2</sup> + b<i>x</i> + c</p>"
                 "<p class='part'>(c) Find f<sup>&minus;1</sup>(<i>x</i>)</p>",
            "steps": [
                "<b>(a)</b> fg(2) means &lsquo;do g first, then f&rsquo;. g(2) = 2<sup>2</sup> + 2 = 6",
                "Then f(6) = 3 &times; 6 &minus; 1 = 17",
                "<b>(b)</b> gf(<i>x</i>) means &lsquo;do f first&rsquo;, so substitute 3<i>x</i> &minus; 1 into g: (3<i>x</i> &minus; 1)<sup>2</sup> + 2",
                "(3<i>x</i> &minus; 1)<sup>2</sup> = 9<i>x</i><sup>2</sup> &minus; 6<i>x</i> + 1, so gf(<i>x</i>) = 9<i>x</i><sup>2</sup> &minus; 6<i>x</i> + 3",
                "<b>(c)</b> Write <i>y</i> = 3<i>x</i> &minus; 1 and rearrange: <i>y</i> + 1 = 3<i>x</i>, so <i>x</i> = " + frac("<i>y</i> + 1", "3"),
                "Swap the letter back: f<sup>&minus;1</sup>(<i>x</i>) = " + frac("<i>x</i> + 1", "3"),
            ],
            "answer": "(a) 17 &nbsp;&nbsp; (b) 9<i>x</i><sup>2</sup> &minus; 6<i>x</i> + 3 &nbsp;&nbsp; (c) " + frac("<i>x</i> + 1", "3"),
        },
        {
            "marks": 4,
            "q": "<p>Here are the first five terms of a quadratic sequence.</p>"
                 "<p><b>3&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;15&nbsp;&nbsp;&nbsp;24&nbsp;&nbsp;&nbsp;35</b></p>"
                 "<p>Find an expression for the <i>n</i>th term.</p>",
            "steps": [
                "First differences: 5, 7, 9, 11. Second differences: 2, 2, 2 &mdash; constant, so the sequence is quadratic.",
                "The <i>n</i><sup>2</sup> coefficient is half the second difference: 2 &divide; 2 = 1, so the sequence starts with <i>n</i><sup>2</sup>.",
                "Write out <i>n</i><sup>2</sup>: 1, 4, 9, 16, 25",
                "Subtract from the sequence: 3 &minus; 1 = 2, 8 &minus; 4 = 4, 15 &minus; 9 = 6, 24 &minus; 16 = 8, 35 &minus; 25 = 10",
                "That leftover sequence 2, 4, 6, 8, 10 has <i>n</i>th term 2<i>n</i>.",
                "Check <i>n</i> = 4: 4<sup>2</sup> + 2 &times; 4 = 16 + 8 = 24 &#10003;",
            ],
            "answer": "<i>n</i><sup>2</sup> + 2<i>n</i>",
        },
        {
            "marks": 4,
            "q": "<p>Solve the inequality</p>"
                 "<p>&nbsp;&nbsp;<i>x</i><sup>2</sup> &minus; 5<i>x</i> &minus; 14 &gt; 0</p>",
            "steps": [
                "First find the critical values by solving <i>x</i><sup>2</sup> &minus; 5<i>x</i> &minus; 14 = 0",
                "Two numbers multiplying to &minus;14 and adding to &minus;5 are &minus;7 and +2, so (<i>x</i> &minus; 7)(<i>x</i> + 2) = 0",
                "The critical values are <i>x</i> = 7 and <i>x</i> = &minus;2",
                "Sketch the curve: it is a positive (U-shaped) parabola crossing the <i>x</i>-axis at &minus;2 and 7.",
                "The curve is <b>above</b> the axis (&gt; 0) outside the two roots.",
            ],
            "answer": "<i>x</i> &lt; &minus;2 &nbsp;or&nbsp; <i>x</i> &gt; 7",
        },
        {
            "marks": 5,
            "q": "<p>Prove that the sum of the squares of any two consecutive odd numbers is always 2 more than a multiple of 8.</p>",
            "steps": [
                "Use algebra so the proof covers <i>every</i> pair, not just examples.",
                "Any odd number can be written as 2<i>n</i> + 1, so the next odd number is 2<i>n</i> + 3 (where <i>n</i> is an integer).",
                "Square each: (2<i>n</i> + 1)<sup>2</sup> = 4<i>n</i><sup>2</sup> + 4<i>n</i> + 1 and (2<i>n</i> + 3)<sup>2</sup> = 4<i>n</i><sup>2</sup> + 12<i>n</i> + 9",
                "Add them: 8<i>n</i><sup>2</sup> + 16<i>n</i> + 10",
                "Take out a factor of 8 from as much as possible: 8(<i>n</i><sup>2</sup> + 2<i>n</i> + 1) + 2",
                "Since <i>n</i><sup>2</sup> + 2<i>n</i> + 1 is an integer, 8(<i>n</i><sup>2</sup> + 2<i>n</i> + 1) is a multiple of 8, so the total is always 2 more than a multiple of 8.",
            ],
            "answer": "(2<i>n</i> + 1)<sup>2</sup> + (2<i>n</i> + 3)<sup>2</sup> = 8(<i>n</i> + 1)<sup>2</sup> + 2, which is 2 more than a multiple of 8",
        },
    ],
}
