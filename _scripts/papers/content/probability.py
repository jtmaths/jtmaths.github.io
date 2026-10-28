"""GCSE practice paper — Probability (topic level)."""
from build import frac

PAPER = {
    "title": "Probability",
    "folder": "gcse/probability",
    "slug": "probability-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>A fair six-sided dice is rolled once.</p>"
                 "<p>Write down the probability of rolling a 3.</p>",
            "steps": [
                "There are 6 equally likely outcomes and only one of them is a 3.",
                "Probability = " + frac("number of successful outcomes", "total number of outcomes"),
            ],
            "answer": frac("1", "6"),
        },
        {
            "marks": 2,
            "q": "<p>A bag contains 5 red counters, 3 blue counters and 2 green counters.</p>"
                 "<p>One counter is taken at random.</p>"
                 "<p class='part'>(a) Write down the probability that it is blue.</p>"
                 "<p class='part'>(b) Write down the probability that it is not red.</p>",
            "steps": [
                "There are 5 + 3 + 2 = 10 counters altogether.",
                "<b>(a)</b> 3 of the 10 are blue, so P(blue) = " + frac("3", "10"),
                "<b>(b)</b> Not red means blue or green: 3 + 2 = 5 counters.",
                "P(not red) = " + frac("5", "10") + " = " + frac("1", "2"),
            ],
            "answer": "(a) " + frac("3", "10") + " &nbsp;&nbsp; (b) " + frac("1", "2"),
        },
        {
            "marks": 2,
            "q": "<p>The probability that it rains tomorrow is 0.35</p>"
                 "<p>Work out the probability that it does not rain tomorrow.</p>",
            "steps": [
                "&lsquo;Rains&rsquo; and &lsquo;does not rain&rsquo; are the only two possibilities, so their probabilities add to 1.",
                "P(no rain) = 1 &minus; 0.35",
            ],
            "answer": "0.65",
        },
        {
            "marks": 2,
            "q": "<p>A spinner has four colours. The table shows some of the probabilities.</p>"
                 "<table class='d'><tr><th>Colour</th><th>Red</th><th>Blue</th><th>Green</th><th>Yellow</th></tr>"
                 "<tr><th>Probability</th><td>0.2</td><td>0.3</td><td>0.15</td><td><i>x</i></td></tr></table>"
                 "<p>Work out the value of <i>x</i>.</p>",
            "steps": [
                "All the probabilities of a complete set of outcomes must add up to 1.",
                "0.2 + 0.3 + 0.15 = 0.65",
                "<i>x</i> = 1 &minus; 0.65 = 0.35",
            ],
            "answer": "<i>x</i> = 0.35",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) A fair six-sided dice is rolled 300 times. Estimate how many times it will land on 4.</p>"
                 "<p class='part'>(b) A biased coin has P(head) = 0.4. It is tossed 250 times. "
                 "Estimate the number of heads.</p>",
            "steps": [
                "Expected number = probability &times; number of trials.",
                "<b>(a)</b> P(4) = " + frac("1", "6") + ", so the estimate is " + frac("1", "6") + " &times; 300 = 50",
                "<b>(b)</b> 0.4 &times; 250 = 100",
                "These are estimates &mdash; the real results will vary a little each time.",
            ],
            "answer": "(a) 50 &nbsp;&nbsp; (b) 100",
        },
        {
            "marks": 3,
            "q": "<p>60 students travel to school by bus or on foot. The two-way table is incomplete.</p>"
                 "<table class='d'><tr><th></th><th>Walk</th><th>Bus</th><th>Total</th></tr>"
                 "<tr><th>Boys</th><td>15</td><td>&nbsp;</td><td>35</td></tr>"
                 "<tr><th>Girls</th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
                 "<tr><th>Total</th><td>24</td><td>&nbsp;</td><td>60</td></tr></table>"
                 "<p>A student is chosen at random. Work out the probability that the student is a girl "
                 "who travels by bus.</p>",
            "steps": [
                "Fill in the table using the row and column totals.",
                "Boys on the bus: 35 &minus; 15 = 20",
                "Girls altogether: 60 &minus; 35 = 25, and girls who walk: 24 &minus; 15 = 9",
                "Girls on the bus: 25 &minus; 9 = 16 (check the bus column: 20 + 16 = 36 and 24 + 36 = 60 &#10003;)",
                "P(girl on the bus) = " + frac("16", "60") + " = " + frac("4", "15"),
            ],
            "answer": frac("4", "15") + " (about 0.267)",
        },
        {
            "marks": 3,
            "q": "<p>Two fair six-sided dice are rolled and their scores are added together.</p>"
                 "<p class='part'>(a) Work out the probability that the total is 7.</p>"
                 "<p class='part'>(b) Work out the probability that the total is greater than 9.</p>",
            "steps": [
                "There are 6 &times; 6 = 36 equally likely outcomes.",
                "<b>(a)</b> Totals of 7 come from (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) &mdash; 6 outcomes.",
                "P(7) = " + frac("6", "36") + " = " + frac("1", "6"),
                "<b>(b)</b> Greater than 9 means 10, 11 or 12.",
                "10: (4,6), (5,5), (6,4) &mdash; 3 ways. 11: (5,6), (6,5) &mdash; 2 ways. 12: (6,6) &mdash; 1 way.",
                "That is 6 outcomes, so the probability is " + frac("6", "36") + " = " + frac("1", "6"),
            ],
            "answer": "(a) " + frac("1", "6") + " &nbsp;&nbsp; (b) " + frac("1", "6"),
        },
        {
            "marks": 3,
            "q": "<p>A drawing pin is dropped 200 times. It lands point up 130 times.</p>"
                 "<p class='part'>(a) Estimate the probability that the pin lands point up.</p>"
                 "<p class='part'>(b) The pin is going to be dropped 500 times. Estimate how many times "
                 "it will land point up.</p>",
            "steps": [
                "<b>(a)</b> This is experimental probability (relative frequency).",
                "P(point up) &asymp; " + frac("130", "200") + " = 0.65",
                "<b>(b)</b> Expected number = 0.65 &times; 500",
                "= 325 times",
            ],
            "answer": "(a) 0.65 &nbsp;&nbsp; (b) 325",
        },
        {
            "marks": 4,
            "q": "<p>In a group of 40 students, 22 study French, 18 study German and 9 study both languages.</p>"
                 "<p class='part'>(a) How many students study neither language?</p>"
                 "<p class='part'>(b) One student is chosen at random. Work out the probability that they "
                 "study French but not German.</p>"
                 "<p class='part'>(c) Work out the probability that they study at least one of the two languages.</p>",
            "steps": [
                "Start in the middle of the Venn diagram: 9 study both.",
                "French only = 22 &minus; 9 = 13, and German only = 18 &minus; 9 = 9",
                "<b>(a)</b> Inside the circles there are 13 + 9 + 9 = 31 students, so 40 &minus; 31 = 9 study neither.",
                "<b>(b)</b> P(French only) = " + frac("13", "40"),
                "<b>(c)</b> At least one language means the 31 students inside the circles.",
                "P(at least one) = " + frac("31", "40"),
            ],
            "answer": "(a) 9 &nbsp;&nbsp; (b) " + frac("13", "40") + " &nbsp;&nbsp; (c) " + frac("31", "40"),
        },
        {
            "marks": 4,
            "q": "<p>A bag contains 4 red counters and 6 blue counters.</p>"
                 "<p>A counter is taken at random, its colour recorded, and it is <b>put back</b>. "
                 "A second counter is then taken.</p>"
                 "<p class='part'>(a) Work out the probability that both counters are red.</p>"
                 "<p class='part'>(b) Work out the probability that one counter is red and the other is blue.</p>",
            "steps": [
                "Because the counter is put back, the probabilities are the same both times.",
                "P(red) = " + frac("4", "10") + " = 0.4 and P(blue) = " + frac("6", "10") + " = 0.6",
                "<b>(a)</b> Multiply along the branches: 0.4 &times; 0.4 = 0.16",
                "<b>(b)</b> There are two ways this can happen: red then blue, or blue then red.",
                "Red then blue: 0.4 &times; 0.6 = 0.24, and blue then red: 0.6 &times; 0.4 = 0.24",
                "Add the two routes: 0.24 + 0.24 = 0.48",
            ],
            "answer": "(a) 0.16 &nbsp;&nbsp; (b) 0.48",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>A and B are independent events. P(A) = 0.3 and P(B) = 0.5</p>"
                 "<p>Work out P(A and B).</p>",
            "steps": [
                "For independent events you multiply the probabilities.",
                "P(A and B) = 0.3 &times; 0.5",
            ],
            "answer": "0.15",
        },
        {
            "marks": 2,
            "q": "<p>A bag contains 5 red and 7 blue counters. One counter is taken and <b>not</b> replaced. "
                 "A second counter is then taken.</p>"
                 "<p>The first counter was red. Write down the probability that the second counter is also red.</p>",
            "steps": [
                "After one red counter is removed there are 4 red counters left.",
                "The total is now 12 &minus; 1 = 11 counters.",
            ],
            "answer": frac("4", "11"),
        },
        {
            "marks": 3,
            "q": "<p>A bag contains 3 green and 5 yellow sweets.</p>"
                 "<p>Two sweets are taken at random without replacement.</p>"
                 "<p>Work out the probability that both are green.</p>",
            "steps": [
                "First sweet: P(green) = " + frac("3", "8"),
                "One green sweet has now gone, so 2 greens remain out of 7 sweets: P(green) = " + frac("2", "7"),
                "Multiply along the branches: " + frac("3", "8") + " &times; " + frac("2", "7") + " = " + frac("6", "56"),
                "Simplify by dividing top and bottom by 2.",
            ],
            "answer": frac("3", "28"),
        },
        {
            "marks": 3,
            "q": "<p>The probability that a machine breaks down on any given day is 0.05, independently of other days.</p>"
                 "<p>Work out the probability that the machine breaks down on at least one of three days.</p>",
            "steps": [
                "&lsquo;At least one&rsquo; is much quicker using the complement.",
                "P(no breakdown on one day) = 1 &minus; 0.05 = 0.95",
                "P(no breakdown on all three days) = 0.95<sup>3</sup> = 0.857375",
                "P(at least one breakdown) = 1 &minus; 0.857375 = 0.142625",
            ],
            "answer": "0.142625 (about 0.143)",
        },
        {
            "marks": 4,
            "q": "<p>60% of the students at a school travel in by bus.</p>"
                 "<p>Of those who travel by bus, 15% are late. Of those who do not travel by bus, 5% are late.</p>"
                 "<p class='part'>(a) Work out the probability that a student chosen at random is late.</p>"
                 "<p class='part'>(b) A student is late. Work out the probability that this student came by bus.</p>",
            "steps": [
                "Draw a tree: first branch bus (0.6) or not bus (0.4); second branch late or not late.",
                "<b>(a)</b> Bus and late: 0.6 &times; 0.15 = 0.09",
                "Not bus and late: 0.4 &times; 0.05 = 0.02",
                "P(late) = 0.09 + 0.02 = 0.11",
                "<b>(b)</b> This is conditional: out of everyone who is late, what fraction came by bus?",
                "P(bus | late) = " + frac("0.09", "0.11") + " = " + frac("9", "11") + " &asymp; 0.818",
            ],
            "answer": "(a) 0.11 &nbsp;&nbsp; (b) " + frac("9", "11") + " (about 0.818)",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains 4 white counters and 6 black counters.</p>"
                 "<p>Two counters are taken at random without replacement.</p>"
                 "<p>Work out the probability that the two counters are the same colour.</p>",
            "steps": [
                "There are two ways to succeed: both white, or both black. Work them out separately and add.",
                "Both white: " + frac("4", "10") + " &times; " + frac("3", "9") + " = " + frac("12", "90"),
                "Both black: " + frac("6", "10") + " &times; " + frac("5", "9") + " = " + frac("30", "90"),
                "Add: " + frac("12", "90") + " + " + frac("30", "90") + " = " + frac("42", "90"),
                "Simplify by dividing top and bottom by 6.",
            ],
            "answer": frac("7", "15") + " (about 0.467)",
        },
        {
            "marks": 4,
            "q": "<p>100 people were asked whether they own a car (set A) and whether they own a bicycle (set B).</p>"
                 "<p>45 own a car, 38 own a bicycle and 20 own both.</p>"
                 "<p>One person is chosen at random. Work out</p>"
                 "<p class='part'>(a) P(A &cup; B)</p>"
                 "<p class='part'>(b) P(A&prime; &cap; B&prime;)</p>"
                 "<p class='part'>(c) P(A | B)</p>",
            "steps": [
                "Fill in the Venn diagram: both = 20, car only = 45 &minus; 20 = 25, bicycle only = 38 &minus; 20 = 18",
                "Neither = 100 &minus; (25 + 20 + 18) = 100 &minus; 63 = 37",
                "<b>(a)</b> A &cup; B means car or bicycle or both: 25 + 20 + 18 = 63, so P = " + frac("63", "100") + " = 0.63",
                "<b>(b)</b> A&prime; &cap; B&prime; means neither, which is the 37 people outside both circles: P = 0.37",
                "<b>(c)</b> P(A | B) restricts attention to the 38 bicycle owners.",
                "Of those, 20 also own a car, so P(A | B) = " + frac("20", "38") + " = " + frac("10", "19"),
            ],
            "answer": "(a) 0.63 &nbsp;&nbsp; (b) 0.37 &nbsp;&nbsp; (c) " + frac("10", "19") + " (about 0.526)",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains n red counters and 5 blue counters.</p>"
                 "<p>Two counters are taken at random without replacement.</p>"
                 "<p>The probability that both counters are red is " + frac("7", "22") + "</p>"
                 "<p class='part'>(a) Show that 3n<sup>2</sup> &minus; 17n &minus; 28 = 0</p>"
                 "<p class='part'>(b) Work out the number of red counters in the bag.</p>",
            "steps": [
                "<b>(a)</b> There are n + 5 counters in total, so P(first red) = " + frac("n", "n + 5"),
                "After one red is removed: P(second red) = " + frac("n &minus; 1", "n + 4"),
                "So " + frac("n(n &minus; 1)", "(n + 5)(n + 4)") + " = " + frac("7", "22"),
                "Cross-multiply: 22n(n &minus; 1) = 7(n + 5)(n + 4), so 22n<sup>2</sup> &minus; 22n = 7(n<sup>2</sup> + 9n + 20)",
                "22n<sup>2</sup> &minus; 22n = 7n<sup>2</sup> + 63n + 140, giving 15n<sup>2</sup> &minus; 85n &minus; 140 = 0",
                "Divide every term by 5: 3n<sup>2</sup> &minus; 17n &minus; 28 = 0 as required.",
                "<b>(b)</b> Factorise: (3n + 4)(n &minus; 7) = 0, so n = &minus;" + frac("4", "3") + " or n = 7",
                "The number of counters must be a positive whole number, so n = 7. "
                "Check: " + frac("7", "12") + " &times; " + frac("6", "11") + " = " + frac("42", "132") + " = " + frac("7", "22") + " &#10003;",
            ],
            "answer": "(b) 7 red counters",
        },
        {
            "marks": 4,
            "q": "<p>In a group of 30 students, 18 like maths, 14 like science and 6 like neither subject.</p>"
                 "<p>A student who likes maths is chosen at random.</p>"
                 "<p>Work out the probability that this student also likes science.</p>",
            "steps": [
                "First find how many like at least one subject: 30 &minus; 6 = 24",
                "Use the fact that 18 + 14 counts the &lsquo;both&rsquo; students twice.",
                "Number who like both = 18 + 14 &minus; 24 = 8",
                "The question restricts us to the 18 students who like maths.",
                "Of those 18, exactly 8 also like science, so the probability is " + frac("8", "18") + " = " + frac("4", "9"),
            ],
            "answer": frac("4", "9") + " (about 0.444)",
        },
        {
            "marks": 5,
            "q": "<p>A box contains 3 red sweets and 7 green sweets.</p>"
                 "<p>Three sweets are taken at random without replacement.</p>"
                 "<p>Work out the probability that at least one of them is red.</p>",
            "steps": [
                "&lsquo;At least one red&rsquo; covers many cases, so work out the opposite: no reds at all.",
                "First sweet green: " + frac("7", "10"),
                "Second sweet green (6 greens left out of 9): " + frac("6", "9"),
                "Third sweet green (5 greens left out of 8): " + frac("5", "8"),
                "P(no reds) = " + frac("7", "10") + " &times; " + frac("6", "9") + " &times; " + frac("5", "8")
                + " = " + frac("210", "720") + " = " + frac("7", "24"),
                "P(at least one red) = 1 &minus; " + frac("7", "24") + " = " + frac("17", "24"),
            ],
            "answer": frac("17", "24") + " (about 0.708)",
        },
    ],
}
