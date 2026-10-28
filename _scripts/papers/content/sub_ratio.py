"""GCSE practice papers — major Ratio, Proportion and Rates of Change subtopics."""
from build import frac

RATIO_NOTATION = {
    "title": "Ratio Notation and Sharing",
    "folder": "gcse/ratio",
    "slug": "ratio-notation-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write the ratio 15 : 25 in its simplest form.</p>",
            "steps": [
                "The highest common factor of 15 and 25 is 5.",
                "15 &divide; 5 = 3 and 25 &divide; 5 = 5",
            ],
            "answer": "3 : 5",
        },
        {
            "marks": 2,
            "q": "<p>Write the ratio 24 : 36 : 60 in its simplest form.</p>",
            "steps": [
                "Look for a number that divides into all three. 12 works.",
                "24 &divide; 12 = 2, &nbsp; 36 &divide; 12 = 3, &nbsp; 60 &divide; 12 = 5",
                "2, 3 and 5 share no further common factor, so this is fully simplified.",
            ],
            "answer": "2 : 3 : 5",
        },
        {
            "marks": 2,
            "q": "<p>Share &pound;45 in the ratio 4 : 5</p>",
            "steps": [
                "4 + 5 = 9 parts altogether.",
                "One part = 45 &divide; 9 = &pound;5",
                "4 parts = &pound;20 and 5 parts = &pound;25 (check: 20 + 25 = 45 &#10003;)",
            ],
            "answer": "&pound;20 and &pound;25",
        },
        {
            "marks": 2,
            "q": "<p>Write the ratio 2 : 5 in the form 1 : n</p>",
            "steps": [
                "Divide both sides by 2 so the left-hand side becomes 1.",
                "2 &divide; 2 = 1 and 5 &divide; 2 = 2.5",
            ],
            "answer": "1 : 2.5",
        },
        {
            "marks": 3,
            "q": "<p>120 sweets are shared between three children in the ratio 3 : 4 : 5</p>"
                 "<p>How many sweets does each child get?</p>",
            "steps": [
                "3 + 4 + 5 = 12 parts.",
                "One part = 120 &divide; 12 = 10 sweets.",
                "3 parts = 30, &nbsp; 4 parts = 40, &nbsp; 5 parts = 50",
                "Check: 30 + 40 + 50 = 120 &#10003;",
            ],
            "answer": "30, 40 and 50 sweets",
        },
        {
            "marks": 3,
            "q": "<p>In a box of counters the ratio of red to blue is 2 : 7</p>"
                 "<p>There are 14 red counters.</p>"
                 "<p class='part'>(a) How many blue counters are there?</p>"
                 "<p class='part'>(b) How many counters are there altogether?</p>",
            "steps": [
                "2 parts are worth 14 counters, so 1 part = 7 counters.",
                "<b>(a)</b> Blue = 7 parts = 7 &times; 7 = 49 counters",
                "<b>(b)</b> Total = 2 + 7 = 9 parts = 9 &times; 7 = 63 counters",
                "(Or simply 14 + 49 = 63.)",
            ],
            "answer": "(a) 49 &nbsp;&nbsp; (b) 63",
        },
        {
            "marks": 3,
            "q": "<p>Write the ratio 45 minutes : 2 hours in its simplest form.</p>",
            "steps": [
                "Both quantities must be in the same units first.",
                "2 hours = 120 minutes, so the ratio is 45 : 120",
                "The highest common factor of 45 and 120 is 15.",
                "45 &divide; 15 = 3 and 120 &divide; 15 = 8",
            ],
            "answer": "3 : 8",
        },
        {
            "marks": 3,
            "q": "<p>A pastry mix uses flour and butter in the ratio 5 : 2</p>"
                 "<p>350 g of flour is used.</p>"
                 "<p class='part'>(a) How much butter is needed?</p>"
                 "<p class='part'>(b) What is the total mass of the mixture?</p>",
            "steps": [
                "5 parts = 350 g, so 1 part = 350 &divide; 5 = 70 g",
                "<b>(a)</b> Butter = 2 parts = 2 &times; 70 = 140 g",
                "<b>(b)</b> Total = 350 + 140 = 490 g",
            ],
            "answer": "(a) 140 g &nbsp;&nbsp; (b) 490 g",
        },
        {
            "marks": 4,
            "q": "<p>Some money is shared in the ratio 3 : 8</p>"
                 "<p>The larger share is &pound;75 more than the smaller share.</p>"
                 "<p>Work out the total amount of money.</p>",
            "steps": [
                "The difference between the parts is 8 &minus; 3 = 5 parts.",
                "Those 5 parts are worth &pound;75.",
                "1 part = 75 &divide; 5 = &pound;15",
                "The total is 3 + 8 = 11 parts, so 11 &times; 15 = &pound;165",
                "Check: shares are &pound;45 and &pound;120, and 120 &minus; 45 = &pound;75 &#10003;",
            ],
            "answer": "&pound;165",
        },
        {
            "marks": 4,
            "q": "<p>a : b = 2 : 3 &nbsp;and&nbsp; b : c = 4 : 5</p>"
                 "<p>Find the ratio a : b : c in its simplest form.</p>",
            "steps": [
                "The letter b appears in both ratios, so make its value match.",
                "b is 3 in the first ratio and 4 in the second. The lowest common multiple of 3 and 4 is 12.",
                "Multiply the first ratio by 4: a : b = 8 : 12",
                "Multiply the second ratio by 3: b : c = 12 : 15",
                "Now b agrees, so a : b : c = 8 : 12 : 15",
                "8, 12 and 15 share no common factor, so this is simplest form.",
            ],
            "answer": "8 : 12 : 15",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Write the ratio 0.4 : 1.2 in its simplest form.</p>",
            "steps": [
                "Multiply both sides by 10 to remove the decimals: 4 : 12",
                "Divide both sides by 4.",
            ],
            "answer": "1 : 3",
        },
        {
            "marks": 2,
            "q": "<p>Write the ratio 5 : 8 in the form n : 1</p>",
            "steps": [
                "This time divide both sides by 8 so the right-hand side becomes 1.",
                "5 &divide; 8 = 0.625 and 8 &divide; 8 = 1",
            ],
            "answer": "0.625 : 1",
        },
        {
            "marks": 3,
            "q": "<p><i>x</i> : <i>y</i> = 3 : 4 &nbsp;and&nbsp; <i>y</i> : <i>z</i> = 6 : 7</p>"
                 "<p>Find <i>x</i> : <i>y</i> : <i>z</i></p>",
            "steps": [
                "<i>y</i> is 4 in the first ratio and 6 in the second; the lowest common multiple is 12.",
                "Multiply the first ratio by 3: <i>x</i> : <i>y</i> = 9 : 12",
                "Multiply the second ratio by 2: <i>y</i> : <i>z</i> = 12 : 14",
                "Combining gives 9 : 12 : 14",
            ],
            "answer": "9 : 12 : 14",
        },
        {
            "marks": 3,
            "q": "<p>In a class the ratio of boys to girls is 5 : 7</p>"
                 "<p class='part'>(a) What fraction of the class are boys?</p>"
                 "<p class='part'>(b) There are 21 girls. How many students are in the class?</p>",
            "steps": [
                "<b>(a)</b> There are 5 + 7 = 12 parts, of which 5 are boys, so the fraction is " + frac("5", "12"),
                "<b>(b)</b> 7 parts = 21 girls, so 1 part = 3 students.",
                "Total = 12 parts = 12 &times; 3 = 36 students",
            ],
            "answer": "(a) " + frac("5", "12") + " &nbsp;&nbsp; (b) 36 students",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains red and blue counters in the ratio 3 : 5</p>"
                 "<p>12 more red counters are added and the ratio becomes 9 : 10</p>"
                 "<p>Work out the total number of counters now in the bag.</p>",
            "steps": [
                "Let the original numbers be 3<i>x</i> red and 5<i>x</i> blue.",
                "After adding: (3<i>x</i> + 12) : 5<i>x</i> = 9 : 10",
                "Cross-multiply: 10(3<i>x</i> + 12) = 9 &times; 5<i>x</i>, so 30<i>x</i> + 120 = 45<i>x</i>",
                "15<i>x</i> = 120, giving <i>x</i> = 8",
                "Red is now 3(8) + 12 = 36 and blue is 5(8) = 40",
                "Total = 76 (check: 36 : 40 simplifies to 9 : 10 &#10003;)",
            ],
            "answer": "76 counters",
        },
        {
            "marks": 4,
            "q": "<p>A money box contains 20p coins and 50p coins in the ratio 5 : 3</p>"
                 "<p>Six of the 50p coins are removed, and the ratio becomes 5 : 2</p>"
                 "<p>How many coins were in the box originally?</p>",
            "steps": [
                "Let the original numbers be 5<i>x</i> twenty-pence coins and 3<i>x</i> fifty-pence coins.",
                "After removing six: 5<i>x</i> : (3<i>x</i> &minus; 6) = 5 : 2",
                "Cross-multiply: 2 &times; 5<i>x</i> = 5(3<i>x</i> &minus; 6), so 10<i>x</i> = 15<i>x</i> &minus; 30",
                "5<i>x</i> = 30, giving <i>x</i> = 6",
                "Originally there were 5(6) = 30 twenty-pence and 3(6) = 18 fifty-pence coins.",
                "Total = 48 coins (check: 30 : 12 simplifies to 5 : 2 &#10003;)",
            ],
            "answer": "48 coins",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains 10p, 20p and 50p coins in the ratio 4 : 5 : 6</p>"
                 "<p>The total value of the coins is &pound;8.80</p>"
                 "<p>How many coins are there altogether?</p>",
            "steps": [
                "Let the numbers be 4<i>x</i>, 5<i>x</i> and 6<i>x</i>. Work in pence.",
                "Value = 4<i>x</i> &times; 10 + 5<i>x</i> &times; 20 + 6<i>x</i> &times; 50",
                "= 40<i>x</i> + 100<i>x</i> + 300<i>x</i> = 440<i>x</i> pence",
                "&pound;8.80 = 880p, so 440<i>x</i> = 880 and <i>x</i> = 2",
                "The numbers of coins are 8, 10 and 12, giving 30 coins in total.",
                "Check: 80p + 200p + 600p = 880p &#10003;",
            ],
            "answer": "30 coins",
        },
        {
            "marks": 4,
            "q": "<p>Some money is shared between A, B and C in the ratio 2 : 3 : 7</p>"
                 "<p>C receives &pound;120 more than B.</p>"
                 "<p>Work out how much each person receives.</p>",
            "steps": [
                "The difference between C and B is 7 &minus; 3 = 4 parts.",
                "4 parts = &pound;120, so 1 part = &pound;30",
                "A = 2 &times; 30 = &pound;60",
                "B = 3 &times; 30 = &pound;90 and C = 7 &times; 30 = &pound;210",
                "Check: 210 &minus; 90 = &pound;120 &#10003; (total &pound;360)",
            ],
            "answer": "A &pound;60, B &pound;90, C &pound;210",
        },
        {
            "marks": 4,
            "q": "<p>Paint is mixed using white and blue in the ratio 7 : 3</p>"
                 "<p>Tom needs 25 litres of the mixture but only has 6 litres of blue paint.</p>"
                 "<p class='part'>(a) Show that Tom cannot make 25 litres of the mixture.</p>"
                 "<p class='part'>(b) Work out the greatest volume of mixture he can make.</p>",
            "steps": [
                "<b>(a)</b> Blue is 3 parts out of 7 + 3 = 10, so it makes up " + frac("3", "10") + " of the mixture.",
                frac("3", "10") + " of 25 = 7.5 litres of blue paint is needed.",
                "Tom only has 6 litres, so he cannot make 25 litres.",
                "<b>(b)</b> With 6 litres of blue, 3 parts = 6, so 1 part = 2 litres.",
                "The mixture is 10 parts = 10 &times; 2 = 20 litres.",
            ],
            "answer": "(a) 7.5 litres of blue is needed &nbsp;&nbsp; (b) 20 litres",
        },
        {
            "marks": 5,
            "q": "<p>A map has a scale of 1 : 50 000</p>"
                 "<p>A rectangular field measures 4 cm by 3 cm on the map.</p>"
                 "<p class='part'>(a) Work out the real dimensions of the field in kilometres.</p>"
                 "<p class='part'>(b) Work out the real area of the field in km<sup>2</sup>.</p>"
                 "<p class='part'>(c) Explain why the area on the map is not " + frac("1", "50 000")
                 + " of the real area.</p>",
            "steps": [
                "<b>(a)</b> 1 cm on the map represents 50 000 cm = 500 m = 0.5 km.",
                "4 cm represents 4 &times; 0.5 = 2 km and 3 cm represents 3 &times; 0.5 = 1.5 km",
                "<b>(b)</b> Real area = 2 &times; 1.5 = 3 km<sup>2</sup>",
                "<b>(c)</b> Lengths are scaled by 50 000, but area involves two lengths multiplied together.",
                "So areas are scaled by 50 000<sup>2</sup> = 2 500 000 000, i.e. 2.5 &times; 10<sup>9</sup>",
                "(Check: the map area is 12 cm<sup>2</sup> and 3 km<sup>2</sup> = 3 &times; 10<sup>10</sup> cm<sup>2</sup>, "
                "and 3 &times; 10<sup>10</sup> &divide; 12 = 2.5 &times; 10<sup>9</sup> &#10003;)",
            ],
            "answer": "(a) 2 km by 1.5 km &nbsp;&nbsp; (b) 3 km<sup>2</sup> &nbsp;&nbsp; "
                      "(c) areas scale by the square of the length scale factor, 50 000<sup>2</sup>",
        },
    ],
}

PROPORTION = {
    "title": "Direct and Inverse Proportion",
    "folder": "gcse/ratio",
    "slug": "proportion-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>One pen costs 40p.</p><p>How much do 5 pens cost?</p>",
            "steps": [
                "The cost is directly proportional to the number of pens, so multiply.",
                "5 &times; 40p = 200p",
            ],
            "answer": "&pound;2.00",
        },
        {
            "marks": 2,
            "q": "<p>4 identical books cost &pound;26.</p><p>Work out the cost of 7 of these books.</p>",
            "steps": [
                "Find the cost of one book: 26 &divide; 4 = &pound;6.50",
                "7 books cost 7 &times; 6.50 = &pound;45.50",
            ],
            "answer": "&pound;45.50",
        },
        {
            "marks": 2,
            "q": "<p>3 workers can build a wall in 12 days.</p>"
                 "<p>How long would 6 workers, all working at the same rate, take?</p>",
            "steps": [
                "More workers means less time &mdash; this is inverse proportion.",
                "Doubling the number of workers halves the time.",
                "12 &divide; 2 = 6 days",
            ],
            "answer": "6 days",
        },
        {
            "marks": 2,
            "q": "<p>200 g of cheese costs &pound;3.20</p><p>Work out the cost of 350 g of the same cheese.</p>",
            "steps": [
                "Cost of 1 g = 320p &divide; 200 = 1.6p",
                "350 g costs 350 &times; 1.6 = 560p = &pound;5.60",
            ],
            "answer": "&pound;5.60",
        },
        {
            "marks": 3,
            "q": "<p><i>y</i> is directly proportional to <i>x</i>. When <i>x</i> = 4, <i>y</i> = 20</p>"
                 "<p class='part'>(a) Work out <i>y</i> when <i>x</i> = 7</p>"
                 "<p class='part'>(b) Work out <i>x</i> when <i>y</i> = 45</p>",
            "steps": [
                "Direct proportion means <i>y</i> = k<i>x</i> for some fixed number k.",
                "20 = k &times; 4, so k = 5 and <i>y</i> = 5<i>x</i>",
                "<b>(a)</b> <i>y</i> = 5 &times; 7 = 35",
                "<b>(b)</b> 45 = 5<i>x</i>, so <i>x</i> = 9",
            ],
            "answer": "(a) 35 &nbsp;&nbsp; (b) 9",
        },
        {
            "marks": 3,
            "q": "<p>5 machines fill 800 bottles in an hour.</p>"
                 "<p>How many bottles would 8 such machines fill in an hour?</p>",
            "steps": [
                "Find the rate for one machine: 800 &divide; 5 = 160 bottles per hour.",
                "8 machines fill 8 &times; 160 = 1280 bottles",
                "More machines means more bottles, so this is direct proportion.",
            ],
            "answer": "1280 bottles",
        },
        {
            "marks": 3,
            "q": "<p>6 people take 10 hours to paint a fence.</p>"
                 "<p>How long would 4 people take, working at the same rate?</p>",
            "steps": [
                "Work out the total work in person-hours: 6 &times; 10 = 60 person-hours.",
                "That total does not change, however many people work.",
                "Time for 4 people = 60 &divide; 4 = 15 hours",
                "Sensible check: fewer people means more time &#10003;",
            ],
            "answer": "15 hours",
        },
        {
            "marks": 3,
            "q": "<p>A recipe for 6 people uses 900 g of pasta.</p>"
                 "<p>How much pasta is needed for 10 people?</p>",
            "steps": [
                "Pasta for one person = 900 &divide; 6 = 150 g",
                "For 10 people: 10 &times; 150 = 1500 g",
                "That is 1.5 kg.",
            ],
            "answer": "1500 g (1.5 kg)",
        },
        {
            "marks": 4,
            "q": "<p><i>y</i> is directly proportional to <i>x</i>. When <i>x</i> = 3, <i>y</i> = 21</p>"
                 "<p class='part'>(a) Find the value of the constant of proportionality.</p>"
                 "<p class='part'>(b) Write a formula for <i>y</i> in terms of <i>x</i>.</p>"
                 "<p class='part'>(c) Work out <i>y</i> when <i>x</i> = 11</p>"
                 "<p class='part'>(d) Write down where the graph of <i>y</i> against <i>x</i> crosses the "
                 "<i>y</i>-axis.</p>",
            "steps": [
                "<b>(a)</b> <i>y</i> = k<i>x</i>, so 21 = 3k and k = 7",
                "<b>(b)</b> <i>y</i> = 7<i>x</i>",
                "<b>(c)</b> <i>y</i> = 7 &times; 11 = 77",
                "<b>(d)</b> When <i>x</i> = 0, <i>y</i> = 0, so the graph passes through the origin (0, 0).",
                "A direct proportion graph is always a straight line through the origin.",
            ],
            "answer": "(a) 7 &nbsp;&nbsp; (b) <i>y</i> = 7<i>x</i> &nbsp;&nbsp; (c) 77 &nbsp;&nbsp; (d) (0, 0)",
        },
        {
            "marks": 4,
            "q": "<p>For each pair of quantities, state whether they are in direct proportion or inverse "
                 "proportion.</p>"
                 "<p class='part'>(a) The number of workers and the time to finish a fixed job.</p>"
                 "<p class='part'>(b) The number of litres of petrol bought and the total cost.</p>"
                 "<p class='part'>(c) The average speed and the time taken for a fixed journey.</p>"
                 "<p class='part'>(d) The number of identical tins and their total mass.</p>",
            "steps": [
                "<b>(a)</b> More workers means less time, so inverse proportion.",
                "<b>(b)</b> More petrol means more cost, at a fixed price per litre, so direct proportion.",
                "<b>(c)</b> A higher speed means a shorter time for the same distance, so inverse proportion.",
                "<b>(d)</b> More tins means more mass, so direct proportion.",
            ],
            "answer": "(a) inverse &nbsp;&nbsp; (b) direct &nbsp;&nbsp; (c) inverse &nbsp;&nbsp; (d) direct",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p><i>y</i> is directly proportional to <i>x</i>, and <i>y</i> = 12 when <i>x</i> = 3</p>"
                 "<p>Find a formula for <i>y</i> in terms of <i>x</i>.</p>",
            "steps": [
                "Write <i>y</i> = k<i>x</i>",
                "12 = 3k, so k = 4",
            ],
            "answer": "<i>y</i> = 4<i>x</i>",
        },
        {
            "marks": 2,
            "q": "<p><i>y</i> is inversely proportional to <i>x</i>, and <i>y</i> = 5 when <i>x</i> = 4</p>"
                 "<p>Find a formula for <i>y</i> in terms of <i>x</i>.</p>",
            "steps": [
                "Write <i>y</i> = " + frac("k", "<i>x</i>"),
                "5 = " + frac("k", "4") + ", so k = 20",
            ],
            "answer": "<i>y</i> = " + frac("20", "<i>x</i>"),
        },
        {
            "marks": 3,
            "q": "<p><i>y</i> is proportional to <i>x</i><sup>2</sup>. When <i>x</i> = 3, <i>y</i> = 45</p>"
                 "<p>Work out <i>y</i> when <i>x</i> = 5</p>",
            "steps": [
                "Write <i>y</i> = k<i>x</i><sup>2</sup>",
                "45 = k &times; 9, so k = 5 and <i>y</i> = 5<i>x</i><sup>2</sup>",
                "<i>y</i> = 5 &times; 5<sup>2</sup> = 5 &times; 25",
            ],
            "answer": "125",
        },
        {
            "marks": 3,
            "q": "<p><i>y</i> is proportional to &radic;<i>x</i>. When <i>x</i> = 16, <i>y</i> = 12</p>"
                 "<p>Work out <i>y</i> when <i>x</i> = 25</p>",
            "steps": [
                "Write <i>y</i> = k&radic;<i>x</i>",
                "&radic;16 = 4, so 12 = 4k and k = 3",
                "<i>y</i> = 3&radic;25 = 3 &times; 5",
            ],
            "answer": "15",
        },
        {
            "marks": 4,
            "q": "<p><i>y</i> is inversely proportional to <i>x</i><sup>2</sup>. When <i>x</i> = 2, <i>y</i> = 9</p>"
                 "<p class='part'>(a) Find a formula for <i>y</i> in terms of <i>x</i>.</p>"
                 "<p class='part'>(b) Work out <i>y</i> when <i>x</i> = 6</p>"
                 "<p class='part'>(c) Work out the positive value of <i>x</i> when <i>y</i> = 4</p>",
            "steps": [
                "<b>(a)</b> <i>y</i> = " + frac("k", "<i>x</i><sup>2</sup>") + ", so 9 = " + frac("k", "4") + " and k = 36",
                "<i>y</i> = " + frac("36", "<i>x</i><sup>2</sup>"),
                "<b>(b)</b> <i>y</i> = " + frac("36", "36") + " = 1",
                "<b>(c)</b> 4 = " + frac("36", "<i>x</i><sup>2</sup>") + ", so 4<i>x</i><sup>2</sup> = 36",
                "<i>x</i><sup>2</sup> = 9, so the positive value is <i>x</i> = 3",
            ],
            "answer": "(a) <i>y</i> = " + frac("36", "<i>x</i><sup>2</sup>") + " &nbsp;&nbsp; (b) 1 &nbsp;&nbsp; (c) 3",
        },
        {
            "marks": 4,
            "q": "<p>The force F newtons between two magnets is inversely proportional to the square of the "
                 "distance d cm between them.</p>"
                 "<p>When d = 4, F = 5</p>"
                 "<p class='part'>(a) Find a formula for F in terms of d.</p>"
                 "<p class='part'>(b) Work out F when d = 10</p>"
                 "<p class='part'>(c) Work out d when F = 20</p>",
            "steps": [
                "<b>(a)</b> F = " + frac("k", "d<sup>2</sup>") + ", so 5 = " + frac("k", "16") + " and k = 80",
                "F = " + frac("80", "d<sup>2</sup>"),
                "<b>(b)</b> F = " + frac("80", "100") + " = 0.8 N",
                "<b>(c)</b> 20 = " + frac("80", "d<sup>2</sup>") + ", so 20d<sup>2</sup> = 80",
                "d<sup>2</sup> = 4, so d = 2 cm (a distance must be positive).",
            ],
            "answer": "(a) F = " + frac("80", "d<sup>2</sup>") + " &nbsp;&nbsp; (b) 0.8 N &nbsp;&nbsp; (c) 2 cm",
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) <i>y</i> is proportional to <i>x</i><sup>3</sup>. "
                 "What happens to <i>y</i> if <i>x</i> is doubled?</p>"
                 "<p class='part'>(b) <i>y</i> is inversely proportional to <i>x</i><sup>2</sup>. "
                 "What happens to <i>y</i> if <i>x</i> is trebled?</p>",
            "steps": [
                "<b>(a)</b> <i>y</i> = k<i>x</i><sup>3</sup>. Replacing <i>x</i> by 2<i>x</i> gives "
                "k(2<i>x</i>)<sup>3</sup> = 8k<i>x</i><sup>3</sup>",
                "So <i>y</i> is multiplied by 8.",
                "<b>(b)</b> <i>y</i> = " + frac("k", "<i>x</i><sup>2</sup>") + ". Replacing <i>x</i> by 3<i>x</i> gives "
                + frac("k", "9<i>x</i><sup>2</sup>"),
                "So <i>y</i> is divided by 9.",
            ],
            "answer": "(a) multiplied by 8 &nbsp;&nbsp; (b) divided by 9",
        },
        {
            "marks": 4,
            "q": "<p>The time T days to build a wall is inversely proportional to the number of workers n.</p>"
                 "<p>6 workers take 15 days.</p>"
                 "<p class='part'>(a) Find a formula for T in terms of n.</p>"
                 "<p class='part'>(b) How long would 10 workers take?</p>"
                 "<p class='part'>(c) How many workers are needed to finish in 5 days?</p>",
            "steps": [
                "<b>(a)</b> T = " + frac("k", "n") + ", so 15 = " + frac("k", "6") + " and k = 90",
                "T = " + frac("90", "n"),
                "<b>(b)</b> T = " + frac("90", "10") + " = 9 days",
                "<b>(c)</b> 5 = " + frac("90", "n") + ", so 5n = 90",
                "n = 18 workers",
            ],
            "answer": "(a) T = " + frac("90", "n") + " &nbsp;&nbsp; (b) 9 days &nbsp;&nbsp; (c) 18 workers",
        },
        {
            "marks": 4,
            "q": "<p><i>y</i> is directly proportional to <i>x</i><sup>2</sup> and inversely proportional "
                 "to <i>z</i>.</p>"
                 "<p>When <i>x</i> = 2 and <i>z</i> = 4, <i>y</i> = 3</p>"
                 "<p>Work out <i>y</i> when <i>x</i> = 4 and <i>z</i> = 6</p>",
            "steps": [
                "Combine both statements: <i>y</i> = " + frac("k<i>x</i><sup>2</sup>", "<i>z</i>"),
                "Substitute the known values: 3 = " + frac("k &times; 4", "4") + " = k",
                "So k = 3 and <i>y</i> = " + frac("3<i>x</i><sup>2</sup>", "<i>z</i>"),
                "<i>y</i> = " + frac("3 &times; 16", "6") + " = " + frac("48", "6") + " = 8",
            ],
            "answer": "8",
        },
        {
            "marks": 5,
            "q": "<p>The distance d metres needed to stop a car is proportional to the square of its "
                 "speed v mph.</p>"
                 "<p>At 30 mph the stopping distance is 45 m.</p>"
                 "<p class='part'>(a) Find a formula for d in terms of v.</p>"
                 "<p class='part'>(b) Work out the stopping distance at 60 mph.</p>"
                 "<p class='part'>(c) Explain the effect on the stopping distance of doubling the speed.</p>"
                 "<p class='part'>(d) Find the speed at which the stopping distance is 80 m.</p>",
            "steps": [
                "<b>(a)</b> d = kv<sup>2</sup>, so 45 = k &times; 900",
                "k = " + frac("45", "900") + " = 0.05, giving d = 0.05v<sup>2</sup>",
                "<b>(b)</b> d = 0.05 &times; 60<sup>2</sup> = 0.05 &times; 3600 = 180 m",
                "<b>(c)</b> Doubling v multiplies v<sup>2</sup> by 4, so the stopping distance becomes four "
                "times as long (45 m &rarr; 180 m confirms this).",
                "<b>(d)</b> 80 = 0.05v<sup>2</sup>, so v<sup>2</sup> = 1600",
                "v = 40 mph",
            ],
            "answer": "(a) d = 0.05v<sup>2</sup> &nbsp;&nbsp; (b) 180 m &nbsp;&nbsp; (c) it becomes 4 times as "
                      "long &nbsp;&nbsp; (d) 40 mph",
        },
    ],
}

COMPOUND = {
    "title": "Compound Measures",
    "folder": "gcse/ratio",
    "slug": "compound-measures-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Complete the formula.</p><p>&nbsp;&nbsp;speed = &#9633; &divide; &#9633;</p>",
            "steps": [
                "Speed tells you how much distance is covered in each unit of time.",
                "So you divide the distance travelled by the time taken.",
            ],
            "answer": "speed = distance &divide; time",
        },
        {
            "marks": 2,
            "q": "<p>A car travels 180 km in 3 hours.</p><p>Work out the average speed.</p>",
            "steps": [
                "Speed = " + frac("distance", "time") + " = " + frac("180", "3"),
                "= 60 km/h",
            ],
            "answer": "60 km/h",
        },
        {
            "marks": 2,
            "q": "<p>A cyclist rides at an average speed of 15 km/h for 2 hours.</p>"
                 "<p>How far does the cyclist travel?</p>",
            "steps": [
                "Distance = speed &times; time",
                "= 15 &times; 2 = 30 km",
            ],
            "answer": "30 km",
        },
        {
            "marks": 2,
            "q": "<p>A train travels 240 km at an average speed of 80 km/h.</p>"
                 "<p>How long does the journey take?</p>",
            "steps": [
                "Time = " + frac("distance", "speed") + " = " + frac("240", "80"),
                "= 3 hours",
            ],
            "answer": "3 hours",
        },
        {
            "marks": 3,
            "q": "<p>A runner covers 400 m in 50 seconds.</p>"
                 "<p class='part'>(a) Work out the speed in m/s.</p>"
                 "<p class='part'>(b) Convert your answer to km/h.</p>",
            "steps": [
                "<b>(a)</b> Speed = " + frac("400", "50") + " = 8 m/s",
                "<b>(b)</b> In one hour (3600 s) the runner would cover 8 &times; 3600 = 28 800 m",
                "28 800 m = 28.8 km, so the speed is 28.8 km/h",
                "(A useful shortcut: multiply m/s by 3.6 to get km/h.)",
            ],
            "answer": "(a) 8 m/s &nbsp;&nbsp; (b) 28.8 km/h",
        },
        {
            "marks": 3,
            "q": "<p>A block of wood has mass 480 g and volume 60 cm<sup>3</sup>.</p>"
                 "<p>Work out its density.</p>",
            "steps": [
                "Density = " + frac("mass", "volume"),
                "= " + frac("480", "60"),
                "= 8 g/cm<sup>3</sup>",
            ],
            "answer": "8 g/cm<sup>3</sup>",
        },
        {
            "marks": 3,
            "q": "<p>Gold has a density of 19.3 g/cm<sup>3</sup>.</p>"
                 "<p>Work out the mass of a piece of gold with volume 5 cm<sup>3</sup>.</p>",
            "steps": [
                "Rearrange the density formula: mass = density &times; volume",
                "= 19.3 &times; 5",
                "= 96.5 g",
            ],
            "answer": "96.5 g",
        },
        {
            "marks": 3,
            "q": "<p>A journey of 90 km is driven at an average speed of 40 km/h.</p>"
                 "<p>Work out the time taken, in hours and minutes.</p>",
            "steps": [
                "Time = " + frac("90", "40") + " = 2.25 hours",
                "The 0.25 is a fraction of an hour, not 25 minutes.",
                "0.25 &times; 60 = 15 minutes",
            ],
            "answer": "2 hours 15 minutes",
        },
        {
            "marks": 4,
            "q": "<p>A driver travels 60 km at an average speed of 30 km/h, then 90 km at an average speed "
                 "of 45 km/h.</p>"
                 "<p class='part'>(a) Work out the total time for the journey.</p>"
                 "<p class='part'>(b) Work out the average speed for the whole journey.</p>",
            "steps": [
                "<b>(a)</b> First stage: 60 &divide; 30 = 2 hours",
                "Second stage: 90 &divide; 45 = 2 hours, so the total time is 4 hours.",
                "<b>(b)</b> Total distance = 60 + 90 = 150 km",
                "Average speed = " + frac("150", "4") + " = 37.5 km/h",
                "Note this is not the average of 30 and 45 &mdash; you must use total distance over total time.",
            ],
            "answer": "(a) 4 hours &nbsp;&nbsp; (b) 37.5 km/h",
        },
        {
            "marks": 4,
            "q": "<p>A box has weight 240 N. Its base measures 0.4 m by 0.3 m.</p>"
                 "<p class='part'>(a) Work out the area of the base.</p>"
                 "<p class='part'>(b) Work out the pressure the box exerts on the floor.</p>"
                 "<p class='part'>(c) The box is turned so that a face measuring 0.4 m by 0.2 m is on the floor. "
                 "Work out the new pressure.</p>",
            "steps": [
                "<b>(a)</b> Area = 0.4 &times; 0.3 = 0.12 m<sup>2</sup>",
                "<b>(b)</b> Pressure = " + frac("force", "area") + " = " + frac("240", "0.12") + " = 2000 N/m<sup>2</sup>",
                "<b>(c)</b> New area = 0.4 &times; 0.2 = 0.08 m<sup>2</sup>",
                "Pressure = " + frac("240", "0.08") + " = 3000 N/m<sup>2</sup>",
                "A smaller area gives a larger pressure for the same weight.",
            ],
            "answer": "(a) 0.12 m<sup>2</sup> &nbsp;&nbsp; (b) 2000 N/m<sup>2</sup> &nbsp;&nbsp; (c) 3000 N/m<sup>2</sup>",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Convert 20 m/s into km/h.</p>",
            "steps": [
                "In one hour there are 3600 seconds, so the distance is 20 &times; 3600 = 72 000 m",
                "72 000 m = 72 km",
            ],
            "answer": "72 km/h",
        },
        {
            "marks": 2,
            "q": "<p>Convert 90 km/h into m/s.</p>",
            "steps": [
                "90 km = 90 000 m and 1 hour = 3600 s",
                frac("90 000", "3600") + " = 25",
            ],
            "answer": "25 m/s",
        },
        {
            "marks": 3,
            "q": "<p>A car travels 45 miles in 50 minutes.</p>"
                 "<p>Work out the average speed in miles per hour.</p>",
            "steps": [
                "The time must be in hours: 50 minutes = " + frac("50", "60") + " hours = " + frac("5", "6") + " hours",
                "Speed = 45 &divide; " + frac("5", "6") + " = 45 &times; " + frac("6", "5"),
                "= 54 mph",
            ],
            "answer": "54 mph",
        },
        {
            "marks": 3,
            "q": "<p>A metal cube of side 4 cm has mass 1.2 kg.</p>"
                 "<p>Work out the density of the metal in g/cm<sup>3</sup>.</p>",
            "steps": [
                "Volume of the cube = 4<sup>3</sup> = 64 cm<sup>3</sup>",
                "The units required are g/cm<sup>3</sup>, so convert the mass: 1.2 kg = 1200 g",
                "Density = " + frac("1200", "64") + " = 18.75 g/cm<sup>3</sup>",
            ],
            "answer": "18.75 g/cm<sup>3</sup>",
        },
        {
            "marks": 4,
            "q": "<p>200 cm<sup>3</sup> of liquid A with density 0.8 g/cm<sup>3</sup> is mixed with "
                 "300 cm<sup>3</sup> of liquid B with density 1.2 g/cm<sup>3</sup>.</p>"
                 "<p>Work out the density of the mixture.</p>",
            "steps": [
                "Find each mass separately using mass = density &times; volume.",
                "Liquid A: 0.8 &times; 200 = 160 g",
                "Liquid B: 1.2 &times; 300 = 360 g",
                "Total mass = 520 g and total volume = 500 cm<sup>3</sup>",
                "Density = " + frac("520", "500") + " = 1.04 g/cm<sup>3</sup>",
                "Note you cannot simply average 0.8 and 1.2, because the volumes are different.",
            ],
            "answer": "1.04 g/cm<sup>3</sup>",
        },
        {
            "marks": 4,
            "q": "<p>A train travels at a constant speed of 144 km/h.</p>"
                 "<p>How far does it travel in 25 seconds?</p>",
            "steps": [
                "Convert the speed to m/s so it matches the time in seconds.",
                "144 km = 144 000 m and 1 hour = 3600 s",
                frac("144 000", "3600") + " = 40 m/s",
                "Distance = 40 &times; 25 = 1000 m",
                "That is 1 km.",
            ],
            "answer": "1000 m (1 km)",
        },
        {
            "marks": 4,
            "q": "<p>A country has an area of 2.4 &times; 10<sup>5</sup> km<sup>2</sup> and a population of "
                 "1.8 &times; 10<sup>7</sup>.</p>"
                 "<p class='part'>(a) Work out the population density in people per km<sup>2</sup>.</p>"
                 "<p class='part'>(b) The population increases by 20%. Work out the new population density.</p>",
            "steps": [
                "<b>(a)</b> Population density = " + frac("population", "area") + " = " + frac("1.8 &times; 10<sup>7</sup>", "2.4 &times; 10<sup>5</sup>"),
                "Number parts: 1.8 &divide; 2.4 = 0.75. Powers: 10<sup>7</sup> &divide; 10<sup>5</sup> = 10<sup>2</sup>",
                "0.75 &times; 100 = 75 people per km<sup>2</sup>",
                "<b>(b)</b> The area does not change, so the density increases in the same proportion.",
                "75 &times; 1.2 = 90 people per km<sup>2</sup>",
            ],
            "answer": "(a) 75 people/km<sup>2</sup> &nbsp;&nbsp; (b) 90 people/km<sup>2</sup>",
        },
        {
            "marks": 4,
            "q": "<p>A tap fills a 45 litre bath in 6 minutes.</p>"
                 "<p class='part'>(a) Work out the rate of flow in litres per minute.</p>"
                 "<p class='part'>(b) Work out the rate of flow in litres per second.</p>"
                 "<p class='part'>(c) How long would the tap take to fill a 300 litre tank?</p>",
            "steps": [
                "<b>(a)</b> 45 &divide; 6 = 7.5 litres per minute",
                "<b>(b)</b> There are 60 seconds in a minute: 7.5 &divide; 60 = 0.125 litres per second",
                "<b>(c)</b> Time = " + frac("300", "7.5") + " = 40 minutes",
            ],
            "answer": "(a) 7.5 litres/min &nbsp;&nbsp; (b) 0.125 litres/s &nbsp;&nbsp; (c) 40 minutes",
        },
        {
            "marks": 4,
            "q": "<p>A cyclist rides 24 km at an average speed of 16 km/h, then returns along the same route "
                 "at an average speed of 12 km/h.</p>"
                 "<p>Work out the average speed for the whole journey, to 2 decimal places.</p>",
            "steps": [
                "Outward time = " + frac("24", "16") + " = 1.5 hours",
                "Return time = " + frac("24", "12") + " = 2 hours",
                "Total time = 3.5 hours and total distance = 48 km",
                "Average speed = " + frac("48", "3.5") + " = 13.714&hellip; km/h",
                "Notice this is less than the average of 16 and 12, because more time is spent at the "
                "slower speed.",
            ],
            "answer": "13.71 km/h (2 d.p.)",
        },
        {
            "marks": 5,
            "q": "<p>A solid metal cylinder has radius 3 cm and height 10 cm.</p>"
                 "<p>The metal has density 7.8 g/cm<sup>3</sup> and costs &pound;0.45 per gram.</p>"
                 "<p class='part'>(a) Work out the volume of the cylinder, to 3 decimal places.</p>"
                 "<p class='part'>(b) Work out the mass of the cylinder, to the nearest gram.</p>"
                 "<p class='part'>(c) Work out the cost of the metal, to the nearest penny.</p>",
            "steps": [
                "<b>(a)</b> Volume = &pi;r<sup>2</sup>h = &pi; &times; 3<sup>2</sup> &times; 10 = 90&pi;",
                "90 &times; 3.14159265&hellip; = 282.743 cm<sup>3</sup> (3 d.p.)",
                "<b>(b)</b> Mass = density &times; volume = 7.8 &times; 282.7433 = 2205.398&hellip; g",
                "To the nearest gram that is 2205 g.",
                "<b>(c)</b> Cost = 2205.398 &times; 0.45 = 992.429&hellip;",
                "So the metal costs &pound;992.43 (using the unrounded mass avoids rounding errors).",
            ],
            "answer": "(a) 282.743 cm<sup>3</sup> &nbsp;&nbsp; (b) 2205 g &nbsp;&nbsp; (c) &pound;992.43",
        },
    ],
}

SIMILAR = {
    "title": "Similar Shapes",
    "folder": "gcse/ratio",
    "slug": "similar-shapes-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Two similar triangles have corresponding sides of 3 cm and 9 cm.</p>"
                 "<p>Write down the scale factor of the enlargement.</p>",
            "steps": [
                "Scale factor = " + frac("new length", "original length") + " = " + frac("9", "3"),
                "9 &divide; 3 = 3, so every length in the larger triangle is 3 times as long.",
            ],
            "answer": "3",
        },
        {
            "marks": 2,
            "q": "<p>Rectangle A measures 4 cm by 6 cm. Rectangle B measures 10 cm by 15 cm.</p>"
                 "<p>Show that the two rectangles are similar.</p>",
            "steps": [
                "Compare the two pairs of corresponding sides.",
                "10 &divide; 4 = 2.5 and 15 &divide; 6 = 2.5",
                "Both give the same scale factor, so the rectangles are similar.",
            ],
            "answer": "Both ratios give a scale factor of 2.5, so they are similar",
        },
        {
            "marks": 2,
            "q": "<p>Two similar triangles have corresponding sides 5 cm and 15 cm.</p>"
                 "<p>Another side of the smaller triangle is 7 cm. Find the corresponding side of the "
                 "larger triangle.</p>",
            "steps": [
                "Scale factor = 15 &divide; 5 = 3",
                "7 &times; 3 = 21 cm",
            ],
            "answer": "21 cm",
        },
        {
            "marks": 2,
            "q": "<p>A shape has perimeter 12 cm. It is enlarged by scale factor 3.</p>"
                 "<p>Write down the perimeter of the enlarged shape.</p>",
            "steps": [
                "Perimeter is a length, so it is multiplied by the scale factor.",
                "12 &times; 3 = 36 cm",
            ],
            "answer": "36 cm",
        },
        {
            "marks": 3,
            "q": "<p>Triangle A has sides 6 cm, 8 cm and 10 cm.</p>"
                 "<p>Triangle B is similar to triangle A and its shortest side is 9 cm.</p>"
                 "<p>Work out the other two sides of triangle B.</p>",
            "steps": [
                "The shortest sides correspond: scale factor = " + frac("9", "6") + " = 1.5",
                "8 &times; 1.5 = 12 cm",
                "10 &times; 1.5 = 15 cm",
                "Check the ratios: 9 : 12 : 15 simplifies to 3 : 4 : 5, matching 6 : 8 : 10 &#10003;",
            ],
            "answer": "12 cm and 15 cm",
        },
        {
            "marks": 3,
            "q": "<p>Two triangles are similar. The angles of the first are 40&deg;, 60&deg; and 80&deg;.</p>"
                 "<p class='part'>(a) Write down the angles of the second triangle.</p>"
                 "<p class='part'>(b) Explain your answer.</p>",
            "steps": [
                "<b>(a)</b> 40&deg;, 60&deg; and 80&deg;",
                "<b>(b)</b> Similar shapes are the same shape but a different size.",
                "An enlargement changes lengths but never changes angles, so corresponding angles are equal.",
            ],
            "answer": "(a) 40&deg;, 60&deg; and 80&deg; &nbsp;&nbsp; (b) enlargement does not change angles",
        },
        {
            "marks": 3,
            "q": "<p>A shape has area 20 cm<sup>2</sup>. It is enlarged by scale factor 2.</p>"
                 "<p class='part'>(a) Work out the area of the enlarged shape.</p>"
                 "<p class='part'>(b) Explain why the answer is not 40 cm<sup>2</sup>.</p>",
            "steps": [
                "<b>(a)</b> Areas are multiplied by the <b>square</b> of the length scale factor.",
                "2<sup>2</sup> = 4, so the new area is 20 &times; 4 = 80 cm<sup>2</sup>",
                "<b>(b)</b> Area involves two lengths multiplied together, and each of those lengths doubles.",
                "So the area is doubled twice over, i.e. multiplied by 4, not 2.",
            ],
            "answer": "(a) 80 cm<sup>2</sup> &nbsp;&nbsp; (b) both dimensions double, so area is multiplied by 2<sup>2</sup>",
        },
        {
            "marks": 3,
            "q": "<p>In triangle ABC, the line DE is parallel to BC, with D on AB and E on AC.</p>"
                 "<p>AD = 4 cm, DB = 6 cm and AE = 6 cm.</p>"
                 "<p>Work out the length of EC.</p>",
            "steps": [
                "Because DE is parallel to BC, triangles ADE and ABC are similar.",
                "AB = AD + DB = 4 + 6 = 10 cm, so the scale factor from ADE to ABC is " + frac("10", "4") + " = 2.5",
                "AC = 6 &times; 2.5 = 15 cm",
                "EC = AC &minus; AE = 15 &minus; 6 = 9 cm",
            ],
            "answer": "EC = 9 cm",
        },
        {
            "marks": 4,
            "q": "<p>A photograph measures 8 cm by 12 cm.</p>"
                 "<p>It is enlarged so that the shorter side becomes 20 cm.</p>"
                 "<p class='part'>(a) Work out the scale factor.</p>"
                 "<p class='part'>(b) Work out the length of the longer side of the enlargement.</p>"
                 "<p class='part'>(c) Work out the area of the enlargement.</p>",
            "steps": [
                "<b>(a)</b> Scale factor = " + frac("20", "8") + " = 2.5",
                "<b>(b)</b> 12 &times; 2.5 = 30 cm",
                "<b>(c)</b> New area = 20 &times; 30 = 600 cm<sup>2</sup>",
                "Check with the area scale factor: original area 8 &times; 12 = 96 cm<sup>2</sup> and "
                "96 &times; 2.5<sup>2</sup> = 96 &times; 6.25 = 600 &#10003;",
            ],
            "answer": "(a) 2.5 &nbsp;&nbsp; (b) 30 cm &nbsp;&nbsp; (c) 600 cm<sup>2</sup>",
        },
        {
            "marks": 4,
            "q": "<p>In triangle PQR, the line ST is parallel to QR, with S on PQ and T on PR.</p>"
                 "<p>PS = 5 cm, SQ = 3 cm and ST = 4 cm.</p>"
                 "<p>Work out the length of QR.</p>",
            "steps": [
                "ST is parallel to QR, so triangles PST and PQR are similar (equal corresponding angles).",
                "PQ = PS + SQ = 5 + 3 = 8 cm",
                "Scale factor from PST to PQR = " + frac("PQ", "PS") + " = " + frac("8", "5") + " = 1.6",
                "QR = ST &times; 1.6 = 4 &times; 1.6",
                "= 6.4 cm",
            ],
            "answer": "QR = 6.4 cm",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Two similar shapes have a length scale factor of 4.</p>"
                 "<p>Write down the area scale factor.</p>",
            "steps": [
                "Area scale factor = (length scale factor)<sup>2</sup>",
                "4<sup>2</sup> = 16",
            ],
            "answer": "16",
        },
        {
            "marks": 2,
            "q": "<p>Two similar solids have a length scale factor of 3.</p>"
                 "<p>Write down the volume scale factor.</p>",
            "steps": [
                "Volume scale factor = (length scale factor)<sup>3</sup>",
                "3<sup>3</sup> = 27",
            ],
            "answer": "27",
        },
        {
            "marks": 3,
            "q": "<p>Two similar shapes have areas 18 cm<sup>2</sup> and 50 cm<sup>2</sup>.</p>"
                 "<p>Work out the length scale factor.</p>",
            "steps": [
                "Area scale factor = " + frac("50", "18") + " = " + frac("25", "9"),
                "The length scale factor is the square root of the area scale factor.",
                "&radic;(" + frac("25", "9") + ") = " + frac("5", "3"),
                "That is about 1.67.",
            ],
            "answer": frac("5", "3") + " &nbsp;(about 1.67)",
        },
        {
            "marks": 3,
            "q": "<p>Two similar solids have volumes 24 cm<sup>3</sup> and 375 cm<sup>3</sup>.</p>"
                 "<p>Work out the length scale factor.</p>",
            "steps": [
                "Volume scale factor = " + frac("375", "24") + " = 15.625",
                "The length scale factor is the cube root of the volume scale factor.",
                "The cube root of 15.625 is 2.5, because 2.5<sup>3</sup> = 15.625",
            ],
            "answer": "2.5",
        },
        {
            "marks": 4,
            "q": "<p>Solid A has surface area 48 cm<sup>2</sup> and volume 32 cm<sup>3</sup>.</p>"
                 "<p>Solid B is similar to A and has surface area 108 cm<sup>2</sup>.</p>"
                 "<p>Work out the volume of solid B.</p>",
            "steps": [
                "Area scale factor = " + frac("108", "48") + " = 2.25",
                "Length scale factor = &radic;2.25 = 1.5",
                "Volume scale factor = 1.5<sup>3</sup> = 3.375",
                "Volume of B = 32 &times; 3.375",
                "= 108 cm<sup>3</sup>",
            ],
            "answer": "108 cm<sup>3</sup>",
        },
        {
            "marks": 4,
            "q": "<p>Two similar cones have heights 6 cm and 9 cm.</p>"
                 "<p>The smaller cone has volume 40&pi; cm<sup>3</sup>.</p>"
                 "<p>Work out the volume of the larger cone, in terms of &pi;.</p>",
            "steps": [
                "Length scale factor = " + frac("9", "6") + " = 1.5",
                "Volume scale factor = 1.5<sup>3</sup> = 3.375",
                "Volume = 40&pi; &times; 3.375",
                "= 135&pi; cm<sup>3</sup>",
            ],
            "answer": "135&pi; cm<sup>3</sup>",
        },
        {
            "marks": 4,
            "q": "<p>A cone of height 12 cm has volume 96 cm<sup>3</sup>.</p>"
                 "<p>The top of the cone is cut off by a cut parallel to the base, exactly halfway up.</p>"
                 "<p class='part'>(a) Explain why the small cone removed has volume 12 cm<sup>3</sup>.</p>"
                 "<p class='part'>(b) Work out the volume of the remaining frustum.</p>",
            "steps": [
                "<b>(a)</b> The small cone is similar to the whole cone with length scale factor " + frac("1", "2"),
                "So its volume scale factor is (" + frac("1", "2") + ")<sup>3</sup> = " + frac("1", "8"),
                "Volume = 96 &times; " + frac("1", "8") + " = 12 cm<sup>3</sup>",
                "<b>(b)</b> The frustum is what is left after removing the small cone.",
                "96 &minus; 12 = 84 cm<sup>3</sup>",
            ],
            "answer": "(a) volume scale factor is " + frac("1", "8") + " &nbsp;&nbsp; (b) 84 cm<sup>3</sup>",
        },
        {
            "marks": 4,
            "q": "<p>Triangle ABC is similar to triangle PQR.</p>"
                 "<p>AB = 6 cm, BC = 8 cm and PQ = 9 cm. The area of triangle ABC is 24 cm<sup>2</sup>.</p>"
                 "<p class='part'>(a) Work out the length of QR.</p>"
                 "<p class='part'>(b) Work out the area of triangle PQR.</p>",
            "steps": [
                "<b>(a)</b> Length scale factor = " + frac("9", "6") + " = 1.5",
                "QR = 8 &times; 1.5 = 12 cm",
                "<b>(b)</b> Area scale factor = 1.5<sup>2</sup> = 2.25",
                "Area of PQR = 24 &times; 2.25 = 54 cm<sup>2</sup>",
            ],
            "answer": "(a) 12 cm &nbsp;&nbsp; (b) 54 cm<sup>2</sup>",
        },
        {
            "marks": 4,
            "q": "<p>Two similar statues are made from the same material.</p>"
                 "<p>The smaller statue is 30 cm tall and has mass 4.5 kg. The larger statue is 50 cm tall.</p>"
                 "<p>Work out the mass of the larger statue, to 1 decimal place.</p>",
            "steps": [
                "Length scale factor = " + frac("50", "30") + " = " + frac("5", "3"),
                "Because the material is the same, mass is proportional to volume.",
                "Volume (and mass) scale factor = (" + frac("5", "3") + ")<sup>3</sup> = " + frac("125", "27"),
                "Mass = 4.5 &times; " + frac("125", "27") + " = " + frac("562.5", "27") + " = 20.833&hellip; kg",
            ],
            "answer": "20.8 kg (1 d.p.)",
        },
        {
            "marks": 5,
            "q": "<p>In triangle ABC, angle ABC = 90&deg;. BD is perpendicular to AC, with D on AC.</p>"
                 "<p>AD = 4 cm and DC = 9 cm.</p>"
                 "<p class='part'>(a) Explain why triangle ABD is similar to triangle BCD.</p>"
                 "<p class='part'>(b) Work out the length of BD.</p>"
                 "<p class='part'>(c) Work out the length of AB, giving your answer in surd form.</p>",
            "steps": [
                "<b>(a)</b> Both triangles have a right angle at D.",
                "Angle BAD and angle CBD are both equal to 90&deg; &minus; angle ABD, so they are equal.",
                "Two pairs of equal angles means the triangles are similar.",
                "<b>(b)</b> Matching corresponding sides: " + frac("AD", "BD") + " = " + frac("BD", "DC"),
                "So BD<sup>2</sup> = AD &times; DC = 4 &times; 9 = 36, giving BD = 6 cm",
                "<b>(c)</b> Triangle ABD is right-angled at D, so AB<sup>2</sup> = AD<sup>2</sup> + BD<sup>2</sup>",
                "AB<sup>2</sup> = 16 + 36 = 52, so AB = &radic;52 = 2&radic;13 cm (about 7.21 cm)",
            ],
            "answer": "(b) BD = 6 cm &nbsp;&nbsp; (c) AB = 2&radic;13 cm",
        },
    ],
}

GROWTH = {
    "title": "Growth and Decay",
    "folder": "gcse/ratio",
    "slug": "growth-decay-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write down the single multiplier for a 5% increase.</p>",
            "steps": [
                "100% + 5% = 105%",
                "105% as a decimal is 1.05",
            ],
            "answer": "1.05",
        },
        {
            "marks": 2,
            "q": "<p>&pound;500 increases by 10%.</p><p>Work out the new amount.</p>",
            "steps": [
                "10% of 500 = 50",
                "500 + 50 = &pound;550 (or 500 &times; 1.1 = 550).",
            ],
            "answer": "&pound;550",
        },
        {
            "marks": 2,
            "q": "<p>A population of 8000 falls by 25%.</p><p>Work out the new population.</p>",
            "steps": [
                "25% of 8000 = 2000",
                "8000 &minus; 2000 = 6000 (or 8000 &times; 0.75 = 6000).",
            ],
            "answer": "6000",
        },
        {
            "marks": 2,
            "q": "<p>&pound;1000 is invested for 2 years at 3% <b>simple</b> interest.</p>"
                 "<p>Work out the total amount at the end.</p>",
            "steps": [
                "Simple interest gives the same amount each year: 3% of 1000 = &pound;30",
                "Two years gives 2 &times; 30 = &pound;60 of interest.",
                "Total = 1000 + 60 = &pound;1060",
            ],
            "answer": "&pound;1060",
        },
        {
            "marks": 3,
            "q": "<p>&pound;1000 is invested for 2 years at 3% <b>compound</b> interest.</p>"
                 "<p class='part'>(a) Work out the total amount at the end.</p>"
                 "<p class='part'>(b) How much more is this than with simple interest at the same rate?</p>",
            "steps": [
                "<b>(a)</b> The multiplier is 1.03 each year, applied twice.",
                "1000 &times; 1.03<sup>2</sup> = 1000 &times; 1.0609 = &pound;1060.90",
                "<b>(b)</b> Simple interest gives &pound;1060 exactly.",
                "1060.90 &minus; 1060 = &pound;0.90, so compound interest gives 90p more.",
                "The extra comes from earning interest on the first year&rsquo;s interest.",
            ],
            "answer": "(a) &pound;1060.90 &nbsp;&nbsp; (b) 90p more",
        },
        {
            "marks": 3,
            "q": "<p>A car is worth &pound;12 000. Its value falls by 20% each year.</p>"
                 "<p>Work out its value after 2 years.</p>",
            "steps": [
                "The multiplier for a 20% decrease is 0.8",
                "12 000 &times; 0.8 = &pound;9600 after one year",
                "9600 &times; 0.8 = &pound;7680 after two years",
                "(Or 12 000 &times; 0.8<sup>2</sup> = 12 000 &times; 0.64 = 7680.)",
            ],
            "answer": "&pound;7680",
        },
        {
            "marks": 3,
            "q": "<p>A colony of bacteria doubles in size every hour.</p>"
                 "<p>There are 500 bacteria at the start.</p>"
                 "<p>How many are there after 5 hours?</p>",
            "steps": [
                "Doubling five times means multiplying by 2<sup>5</sup>",
                "2<sup>5</sup> = 32",
                "500 &times; 32 = 16 000",
            ],
            "answer": "16 000 bacteria",
        },
        {
            "marks": 3,
            "q": "<p>&pound;2500 is invested at 4% compound interest per year.</p>"
                 "<p>Work out the value after 3 years, to the nearest penny.</p>",
            "steps": [
                "Multiplier = 1.04, applied 3 times.",
                "1.04<sup>3</sup> = 1.124864",
                "2500 &times; 1.124864 = 2812.16",
            ],
            "answer": "&pound;2812.16",
        },
        {
            "marks": 4,
            "q": "<p>&pound;5000 is invested for 3 years. Two accounts are available.</p>"
                 "<p class='part'><b>Account A:</b> 4% simple interest per year.</p>"
                 "<p class='part'><b>Account B:</b> 3.5% compound interest per year.</p>"
                 "<p>Which account gives more money after 3 years, and by how much?</p>",
            "steps": [
                "<b>Account A:</b> 4% of 5000 = &pound;200 each year.",
                "3 &times; 200 = &pound;600 interest, so the total is &pound;5600",
                "<b>Account B:</b> 5000 &times; 1.035<sup>3</sup>",
                "1.035<sup>3</sup> = 1.108717875, so the total is 5000 &times; 1.108717875 = &pound;5543.59",
                "5600 &minus; 5543.59 = &pound;56.41",
                "So Account A gives &pound;56.41 more.",
            ],
            "answer": "Account A, by &pound;56.41",
        },
        {
            "marks": 4,
            "q": "<p>After a 15% decrease, the value of an item is &pound;510.</p>"
                 "<p class='part'>(a) Work out the original value.</p>"
                 "<p class='part'>(b) Work out the size of the decrease in pounds.</p>",
            "steps": [
                "<b>(a)</b> A 15% decrease means the &pound;510 is 85% of the original.",
                "The multiplier used was 0.85, so divide to reverse it.",
                "510 &divide; 0.85 = &pound;600",
                "<b>(b)</b> 600 &minus; 510 = &pound;90",
                "Check: 15% of 600 = &pound;90 &#10003;",
            ],
            "answer": "(a) &pound;600 &nbsp;&nbsp; (b) &pound;90",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Write down the single multiplier for a 12.5% decrease.</p>",
            "steps": [
                "100% &minus; 12.5% = 87.5%",
                "87.5% as a decimal is 0.875",
            ],
            "answer": "0.875",
        },
        {
            "marks": 2,
            "q": "<p>&pound;8000 is invested at 2% compound interest per year.</p>"
                 "<p>Work out the value after 5 years, to the nearest penny.</p>",
            "steps": [
                "1.02<sup>5</sup> = 1.1040808032",
                "8000 &times; 1.1040808032 = 8832.646&hellip;",
            ],
            "answer": "&pound;8832.65",
        },
        {
            "marks": 3,
            "q": "<p>A radioactive substance decays by 8% each day.</p>"
                 "<p>There are 400 g at the start.</p>"
                 "<p>Work out the mass after 10 days, to 1 decimal place.</p>",
            "steps": [
                "The multiplier for an 8% decrease is 0.92",
                "Mass = 400 &times; 0.92<sup>10</sup>",
                "0.92<sup>10</sup> = 0.4343884&hellip;",
                "400 &times; 0.4343884 = 173.755&hellip; g",
            ],
            "answer": "173.8 g (1 d.p.)",
        },
        {
            "marks": 3,
            "q": "<p>An investment of &pound;4000 grows to &pound;4630.50 in 3 years with compound interest.</p>"
                 "<p>Work out the annual interest rate.</p>",
            "steps": [
                "The total multiplier over 3 years is " + frac("4630.50", "4000") + " = 1.157625",
                "The yearly multiplier is the cube root of this.",
                "The cube root of 1.157625 is 1.05 (since 1.05<sup>3</sup> = 1.157625).",
                "A multiplier of 1.05 means a 5% increase.",
            ],
            "answer": "5% per year",
        },
        {
            "marks": 4,
            "q": "<p>&pound;6000 is invested at 3% compound interest per year.</p>"
                 "<p>Work out the least number of complete years before the investment exceeds &pound;8000.</p>",
            "steps": [
                "Each year the value is multiplied by 1.03",
                "After 9 years: 6000 &times; 1.03<sup>9</sup> = 6000 &times; 1.304773 = &pound;7828.64 &mdash; not enough.",
                "After 10 years: 6000 &times; 1.03<sup>10</sup> = 6000 &times; 1.343916 = &pound;8063.50",
                "This is the first year the value is above &pound;8000.",
            ],
            "answer": "10 years",
        },
        {
            "marks": 4,
            "q": "<p>A machine is worth &pound;40 000 when new.</p>"
                 "<p>It loses 25% of its value in the first year and 15% of its value in each year after that.</p>"
                 "<p>Work out its value after 4 years.</p>",
            "steps": [
                "First year multiplier: 0.75. Later years multiplier: 0.85, used three times.",
                "Value = 40 000 &times; 0.75 &times; 0.85<sup>3</sup>",
                "40 000 &times; 0.75 = &pound;30 000",
                "0.85<sup>3</sup> = 0.614125",
                "30 000 &times; 0.614125 = &pound;18 423.75",
            ],
            "answer": "&pound;18 423.75",
        },
        {
            "marks": 4,
            "q": "<p>The number of users N of an app after t months is modelled by</p>"
                 "<p>&nbsp;&nbsp;N = 500 &times; 1.4<sup>t</sup></p>"
                 "<p class='part'>(a) How many users were there at the start?</p>"
                 "<p class='part'>(b) How many users after 6 months? Give your answer to the nearest whole number.</p>"
                 "<p class='part'>(c) What does the number 1.4 tell you?</p>",
            "steps": [
                "<b>(a)</b> At t = 0, 1.4<sup>0</sup> = 1, so N = 500 users.",
                "<b>(b)</b> 1.4<sup>6</sup> = 7.529536",
                "N = 500 &times; 7.529536 = 3764.768, so about 3765 users.",
                "<b>(c)</b> Each month the number of users is multiplied by 1.4, which is a 40% increase "
                "per month.",
            ],
            "answer": "(a) 500 &nbsp;&nbsp; (b) 3765 &nbsp;&nbsp; (c) the number of users grows by 40% each month",
        },
        {
            "marks": 4,
            "q": "<p>A substance has a half-life of 12 years, so its mass halves every 12 years.</p>"
                 "<p>There are 640 g at the start.</p>"
                 "<p class='part'>(a) Work out the mass after 48 years.</p>"
                 "<p class='part'>(b) Write a formula for the mass m grams after t years.</p>",
            "steps": [
                "<b>(a)</b> 48 &divide; 12 = 4, so the mass halves 4 times.",
                "640 &rarr; 320 &rarr; 160 &rarr; 80 &rarr; 40",
                "The mass is 40 g. (Or 640 &divide; 2<sup>4</sup> = 640 &divide; 16 = 40.)",
                "<b>(b)</b> The number of half-lives after t years is " + frac("t", "12"),
                "So m = 640 &times; (" + frac("1", "2") + ")<sup>t/12</sup>",
            ],
            "answer": "(a) 40 g &nbsp;&nbsp; (b) m = 640 &times; (" + frac("1", "2") + ")<sup>t/12</sup>",
        },
        {
            "marks": 4,
            "q": "<p>&pound;5000 is invested for one year. Two options are offered.</p>"
                 "<p class='part'><b>Option 1:</b> 6% interest added once, at the end of the year.</p>"
                 "<p class='part'><b>Option 2:</b> 0.5% interest added at the end of every month.</p>"
                 "<p>Which option gives more money, and by how much?</p>",
            "steps": [
                "<b>Option 1:</b> 5000 &times; 1.06 = &pound;5300",
                "<b>Option 2:</b> the multiplier 1.005 is applied 12 times.",
                "1.005<sup>12</sup> = 1.0616778&hellip;",
                "5000 &times; 1.0616778 = &pound;5308.39",
                "5308.39 &minus; 5300 = &pound;8.39",
                "Option 2 is better because the later months earn interest on interest already added.",
            ],
            "answer": "Option 2, by &pound;8.39",
        },
        {
            "marks": 5,
            "q": "<p>An amount &pound;P is invested at 4% compound interest per year.</p>"
                 "<p>After 5 years it is worth &pound;9733.22</p>"
                 "<p class='part'>(a) Work out P.</p>"
                 "<p class='part'>(b) Work out how many more complete years it takes for the investment to "
                 "exceed &pound;12 000.</p>",
            "steps": [
                "<b>(a)</b> The multiplier over 5 years is 1.04<sup>5</sup> = 1.2166529",
                "P &times; 1.2166529 = 9733.22, so P = 9733.22 &divide; 1.2166529 = &pound;8000",
                "<b>(b)</b> Start from &pound;9733.22 and keep multiplying by 1.04",
                "After 5 more years: 9733.22 &times; 1.2166529 = &pound;11 841.72 &mdash; not yet enough.",
                "After 6 more years: 9733.22 &times; 1.04<sup>6</sup> = 9733.22 &times; 1.2653190 = &pound;12 315.39",
                "So it takes 6 more complete years.",
            ],
            "answer": "(a) &pound;8000 &nbsp;&nbsp; (b) 6 more years",
        },
    ],
}

PAPERS = [RATIO_NOTATION, PROPORTION, COMPOUND, SIMILAR, GROWTH]
