"""GCSE practice paper — Number (topic level)."""
from build import frac

PAPER = {
    "title": "Number",
    "folder": "gcse/number",
    "slug": "number-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Work out 7 + 2 &times; 6</p>",
            "steps": [
                "BIDMAS tells you to do the multiplication before the addition.",
                "2 &times; 6 = 12",
                "7 + 12 = 19",
            ],
            "answer": "19",
        },
        {
            "marks": 2,
            "q": "<p>Write 45% as</p>"
                 "<p class='part'>(a) a decimal</p>"
                 "<p class='part'>(b) a fraction in its simplest form.</p>",
            "steps": [
                "<b>(a)</b> Per cent means &lsquo;out of 100&rsquo;, so 45% = " + frac("45", "100") + " = 0.45",
                "<b>(b)</b> Start from " + frac("45", "100") + " and cancel.",
                "The highest common factor of 45 and 100 is 5.",
                "45 &divide; 5 = 9 and 100 &divide; 5 = 20, giving " + frac("9", "20"),
            ],
            "answer": "(a) 0.45 &nbsp;&nbsp; (b) " + frac("9", "20"),
        },
        {
            "marks": 2,
            "q": "<p>Write down the value of</p>"
                 "<p class='part'>(a) 5<sup>2</sup></p>"
                 "<p class='part'>(b) &radic;81</p>",
            "steps": [
                "<b>(a)</b> 5<sup>2</sup> means 5 &times; 5 = 25",
                "<b>(b)</b> &radic;81 asks &lsquo;what number times itself gives 81?&rsquo;",
                "9 &times; 9 = 81, so &radic;81 = 9",
            ],
            "answer": "(a) 25 &nbsp;&nbsp; (b) 9",
        },
        {
            "marks": 2,
            "q": "<p>Work out " + frac("3", "8") + " of 240</p>",
            "steps": [
                "First find one eighth by dividing by the denominator.",
                "240 &divide; 8 = 30",
                "Now multiply by the numerator: 30 &times; 3 = 90",
            ],
            "answer": "90",
        },
        {
            "marks": 2,
            "q": "<p>Write 90 as a product of its prime factors. "
                 "Give your answer in index form.</p>",
            "steps": [
                "Use a factor tree, dividing by the smallest prime each time.",
                "90 = 2 &times; 45",
                "45 = 3 &times; 15, and 15 = 3 &times; 5",
                "So 90 = 2 &times; 3 &times; 3 &times; 5",
                "In index form the two 3s become 3<sup>2</sup>.",
            ],
            "answer": "90 = 2 &times; 3<sup>2</sup> &times; 5",
        },
        {
            "marks": 3,
            "q": "<p>Work out " + frac("2", "3") + " + " + frac("1", "4") +
                 "</p><p>Give your answer as a fraction in its simplest form.</p>",
            "steps": [
                "You can only add fractions with the same denominator.",
                "The lowest common multiple of 3 and 4 is 12, so write both over 12.",
                frac("2", "3") + " = " + frac("8", "12") + " &nbsp; (multiply top and bottom by 4)",
                frac("1", "4") + " = " + frac("3", "12") + " &nbsp; (multiply top and bottom by 3)",
                "Now add the numerators only: " + frac("8", "12") + " + " + frac("3", "12") + " = " + frac("11", "12"),
                "11 and 12 share no common factor, so this is already simplest.",
            ],
            "answer": frac("11", "12"),
        },
        {
            "marks": 3,
            "q": "<p>A coat costs &pound;80.</p>"
                 "<p>In a sale the price is reduced by 15%.</p>"
                 "<p>Work out the sale price of the coat.</p>",
            "steps": [
                "<i>Method 1 &mdash; find the reduction, then subtract.</i>",
                "10% of 80 = 8, so 5% of 80 = 4",
                "15% of 80 = 8 + 4 = &pound;12",
                "Sale price = 80 &minus; 12 = &pound;68",
                "<i>Method 2 &mdash; use a multiplier.</i> A 15% decrease means paying 85%, so multiply by 0.85.",
                "80 &times; 0.85 = &pound;68 &nbsp;(same answer, and quicker)",
            ],
            "answer": "&pound;68",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Write 0.0037 in standard form.</p>"
                 "<p class='part'>(b) Write 5.2 &times; 10<sup>3</sup> as an ordinary number.</p>",
            "steps": [
                "<b>(a)</b> Standard form is A &times; 10<sup>n</sup> where 1 &le; A &lt; 10.",
                "Move the decimal point in 0.0037 three places right to get 3.7.",
                "The number is smaller than 1, so the power is negative: 3.7 &times; 10<sup>&minus;3</sup>",
                "<b>(b)</b> 10<sup>3</sup> = 1000, so move the point three places right.",
                "5.2 &times; 1000 = 5200",
            ],
            "answer": "(a) 3.7 &times; 10<sup>&minus;3</sup> &nbsp;&nbsp; (b) 5200",
        },
        {
            "marks": 4,
            "q": "<p>Find</p>"
                 "<p class='part'>(a) the highest common factor (HCF) of 42 and 70</p>"
                 "<p class='part'>(b) the lowest common multiple (LCM) of 42 and 70.</p>",
            "steps": [
                "Write each number as a product of primes first.",
                "42 = 2 &times; 3 &times; 7",
                "70 = 2 &times; 5 &times; 7",
                "<b>(a)</b> For the HCF, multiply the primes that appear in <i>both</i> lists.",
                "Both contain one 2 and one 7, so HCF = 2 &times; 7 = 14",
                "<b>(b)</b> For the LCM, take every prime that appears, to its highest power.",
                "LCM = 2 &times; 3 &times; 5 &times; 7 = 210",
                "Check: 42 &times; 70 = 2940 and 14 &times; 210 = 2940 &#10003; "
                "(HCF &times; LCM always equals the product of the two numbers)",
            ],
            "answer": "(a) 14 &nbsp;&nbsp; (b) 210",
        },
        {
            "marks": 4,
            "q": "<p>At a bus station, buses to Leeds leave every 12 minutes and buses "
                 "to York leave every 18 minutes.</p>"
                 "<p>At 9 am a bus to Leeds and a bus to York leave at the same time.</p>"
                 "<p class='part'>(a) At what time do a Leeds bus and a York bus next leave together?</p>"
                 "<p class='part'>(b) Including the 9 am departure, how many times do they leave "
                 "together up to and including 12 noon?</p>",
            "steps": [
                "They leave together after a number of minutes that is a multiple of both 12 and 18 &mdash; "
                "so you need the LCM.",
                "12 = 2<sup>2</sup> &times; 3 &nbsp; and &nbsp; 18 = 2 &times; 3<sup>2</sup>",
                "LCM = 2<sup>2</sup> &times; 3<sup>2</sup> = 36 minutes",
                "<b>(a)</b> 9:00 am + 36 minutes = <b>9:36 am</b>",
                "<b>(b)</b> From 9 am to 12 noon is 3 hours = 180 minutes.",
                "180 &divide; 36 = 5, so there are 5 further departures after 9 am.",
                "Listing them: 9:00, 9:36, 10:12, 10:48, 11:24, 12:00",
                "Including the 9 am one, that is 6 times in total.",
            ],
            "answer": "(a) 9:36 am &nbsp;&nbsp; (b) 6 times",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Evaluate</p>"
                 "<p class='part'>(a) 3<sup>&minus;2</sup></p>"
                 "<p class='part'>(b) 16<sup>1/2</sup></p>",
            "steps": [
                "<b>(a)</b> A negative power means &lsquo;one over&rsquo; the positive power.",
                "3<sup>&minus;2</sup> = " + frac("1", "3<sup>2</sup>") + " = " + frac("1", "9"),
                "<b>(b)</b> A power of &frac12; means the square root.",
                "16<sup>1/2</sup> = &radic;16 = 4",
            ],
            "answer": "(a) " + frac("1", "9") + " &nbsp;&nbsp; (b) 4",
        },
        {
            "marks": 2,
            "q": "<p>Simplify fully &radic;72</p>",
            "steps": [
                "Look for a factor of 72 that is a perfect square.",
                "72 = 36 &times; 2, and 36 is a square number.",
                "&radic;72 = &radic;36 &times; &radic;2",
                "&radic;36 = 6, so &radic;72 = 6&radic;2",
            ],
            "answer": "6&radic;2",
        },
        {
            "marks": 2,
            "q": "<p>Work out (4 &times; 10<sup>5</sup>) &times; (3 &times; 10<sup>&minus;2</sup>)</p>"
                 "<p>Give your answer in standard form.</p>",
            "steps": [
                "Multiply the number parts and the powers of 10 separately.",
                "4 &times; 3 = 12",
                "10<sup>5</sup> &times; 10<sup>&minus;2</sup> = 10<sup>5&minus;2</sup> = 10<sup>3</sup> (add the indices)",
                "This gives 12 &times; 10<sup>3</sup>, but 12 is not between 1 and 10.",
                "12 &times; 10<sup>3</sup> = 1.2 &times; 10<sup>1</sup> &times; 10<sup>3</sup> = 1.2 &times; 10<sup>4</sup>",
            ],
            "answer": "1.2 &times; 10<sup>4</sup>",
        },
        {
            "marks": 2,
            "q": "<p>Rationalise the denominator of " + frac("6", "&radic;3") +
                 " and simplify your answer.</p>",
            "steps": [
                "Multiply the top and the bottom by &radic;3. This does not change the value, "
                "because you are multiplying by 1.",
                frac("6", "&radic;3") + " &times; " + frac("&radic;3", "&radic;3") + " = " + frac("6&radic;3", "3"),
                "&radic;3 &times; &radic;3 = 3, which is why the surd disappears from the bottom.",
                "Now cancel: 6 &divide; 3 = 2, giving 2&radic;3",
            ],
            "answer": "2&radic;3",
        },
        {
            "marks": 3,
            "q": "<p>Write the recurring decimal 0.2&#775;7&#775; (that is, 0.272727&hellip;) "
                 "as a fraction in its simplest form.</p>",
            "steps": [
                "Let <span class='v'>x</span> = 0.272727&hellip;",
                "Two digits repeat, so multiply by 100: 100<span class='v'>x</span> = 27.272727&hellip;",
                "Subtract the first line from the second &mdash; the recurring tails cancel exactly.",
                "100<span class='v'>x</span> &minus; <span class='v'>x</span> = 27.2727&hellip; &minus; 0.2727&hellip;",
                "99<span class='v'>x</span> = 27, so <span class='v'>x</span> = " + frac("27", "99"),
                "Cancel by 9: " + frac("27", "99") + " = " + frac("3", "11"),
            ],
            "answer": frac("3", "11"),
        },
        {
            "marks": 3,
            "q": "<p>Expand and simplify (3 + &radic;5)(2 &minus; &radic;5)</p>",
            "steps": [
                "Expand the brackets in the usual way (each term in the first times each in the second).",
                "3 &times; 2 = 6",
                "3 &times; (&minus;&radic;5) = &minus;3&radic;5",
                "&radic;5 &times; 2 = 2&radic;5",
                "&radic;5 &times; (&minus;&radic;5) = &minus;5 &nbsp;(because &radic;5 &times; &radic;5 = 5)",
                "Collect: 6 &minus; 5 = 1, and &minus;3&radic;5 + 2&radic;5 = &minus;&radic;5",
            ],
            "answer": "1 &minus; &radic;5",
        },
        {
            "marks": 3,
            "q": "<p>The length of a rod is 12.4 cm, correct to 1 decimal place.</p>"
                 "<p class='part'>(a) Write down the error interval for the length.</p>"
                 "<p class='part'>(b) Four of these rods are joined to make a square. "
                 "Work out the upper bound of the perimeter.</p>",
            "steps": [
                "<b>(a)</b> Rounded to 1 d.p., so the rounding unit is 0.1 and half of it is 0.05.",
                "Lower bound = 12.4 &minus; 0.05 = 12.35 cm",
                "Upper bound = 12.4 + 0.05 = 12.45 cm",
                "Error interval: 12.35 &le; L &lt; 12.45",
                "<b>(b)</b> For the largest possible perimeter, use the largest possible length.",
                "Perimeter = 4 &times; 12.45 = 49.8 cm",
            ],
            "answer": "(a) 12.35 &le; L &lt; 12.45 &nbsp;&nbsp; (b) 49.8 cm",
        },
        {
            "marks": 3,
            "q": "<p><span class='v'>x</span> = 4.6 and <span class='v'>y</span> = 2.3, "
                 "each correct to 1 decimal place.</p>"
                 "<p>Work out the upper bound of " + frac("<span class='v'>x</span>", "<span class='v'>y</span>") +
                 ". Give your answer to 3 significant figures.</p>",
            "steps": [
                "Write down the bounds for each value first.",
                "4.55 &le; <span class='v'>x</span> &lt; 4.65 &nbsp; and &nbsp; 2.25 &le; <span class='v'>y</span> &lt; 2.35",
                "A fraction is largest when the top is as big as possible and the bottom as "
                "<i>small</i> as possible.",
                "So use " + frac("4.65", "2.25"),
                "4.65 &divide; 2.25 = 2.0666&hellip;",
                "To 3 significant figures this is 2.07",
            ],
            "answer": "2.07",
        },
        {
            "marks": 3,
            "q": "<p>Evaluate " + frac("16", "81") + "<sup>&minus;3/4</sup></p>"
                 "<p>Give your answer as a fraction.</p>",
            "steps": [
                "Deal with the negative sign first: it means turn the fraction upside down.",
                frac("16", "81") + "<sup>&minus;3/4</sup> = " + frac("81", "16") + "<sup>3/4</sup>",
                "The denominator of the power (4) means take the fourth root.",
                "&#8732;81 = 3 and &#8732;16 = 2, giving " + frac("3", "2"),
                "The numerator of the power (3) means cube it.",
                frac("3", "2") + "<sup>3</sup> = " + frac("27", "8"),
            ],
            "answer": frac("27", "8") + " &nbsp;(= 3.375)",
        },
        {
            "marks": 4,
            "q": "<p>A car travels 96 metres, measured to the nearest metre, "
                 "in 7.2 seconds, measured to 1 decimal place.</p>"
                 "<p class='part'>(a) Calculate the upper bound for the average speed of the car. "
                 "Give your answer to 3 significant figures.</p>"
                 "<p class='part'>(b) Explain which bounds you used and why.</p>",
            "steps": [
                "Find the bounds for each measurement.",
                "Distance to the nearest metre: 95.5 &le; <span class='v'>d</span> &lt; 96.5",
                "Time to 1 d.p.: 7.15 &le; <span class='v'>t</span> &lt; 7.25",
                "Speed = " + frac("distance", "time") + ", so the speed is greatest when the "
                "distance is greatest and the time is <i>smallest</i>.",
                "<b>(a)</b> Upper bound = " + frac("96.5", "7.15"),
                "96.5 &divide; 7.15 = 13.4965&hellip;",
                "To 3 significant figures this is 13.5 m/s",
                "<b>(b)</b> The upper bound of the distance (96.5 m) was used because a longer "
                "distance in the same time means a faster speed. The lower bound of the time "
                "(7.15 s) was used because covering the distance in less time also means a "
                "faster speed. Together these give the largest possible value of the fraction.",
            ],
            "answer": "(a) 13.5 m/s &nbsp;&nbsp; (b) greatest distance (96.5 m) &divide; least time (7.15 s)",
        },
    ],
}
