"""GCSE practice papers — major Number subtopics."""
from build import frac

FRACTIONS = {
    "title": "Fractions and Decimals",
    "folder": "gcse/number",
    "slug": "fractions-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write " + frac("18", "24") + " in its simplest form.</p>",
            "steps": [
                "The highest common factor of 18 and 24 is 6.",
                "18 &divide; 6 = 3 and 24 &divide; 6 = 4",
            ],
            "answer": frac("3", "4"),
        },
        {
            "marks": 2,
            "q": "<p>Work out " + frac("2", "5") + " + " + frac("1", "3") + "</p>",
            "steps": [
                "You can only add fractions with the same denominator. The lowest common multiple of 5 and 3 is 15.",
                frac("2", "5") + " = " + frac("6", "15") + " and " + frac("1", "3") + " = " + frac("5", "15"),
                "Add the numerators only: 6 + 5 = 11",
            ],
            "answer": frac("11", "15"),
        },
        {
            "marks": 2,
            "q": "<p>Work out " + frac("3", "4") + " &times; " + frac("2", "9") + "</p>"
                 "<p>Give your answer in its simplest form.</p>",
            "steps": [
                "To multiply fractions, multiply the tops and multiply the bottoms.",
                "3 &times; 2 = 6 and 4 &times; 9 = 36, giving " + frac("6", "36"),
                "Simplify by dividing top and bottom by 6.",
            ],
            "answer": frac("1", "6"),
        },
        {
            "marks": 2,
            "q": "<p>Write 0.6 as a fraction in its simplest form.</p>",
            "steps": [
                "The 6 is in the tenths column, so 0.6 = " + frac("6", "10"),
                "Divide top and bottom by 2.",
            ],
            "answer": frac("3", "5"),
        },
        {
            "marks": 3,
            "q": "<p>Work out 2" + frac("1", "2") + " + 1" + frac("3", "4") + "</p>"
                 "<p>Give your answer as a mixed number.</p>",
            "steps": [
                "Deal with the whole numbers first: 2 + 1 = 3",
                "Now the fractions: " + frac("1", "2") + " = " + frac("2", "4") + ", so " + frac("2", "4") + " + " + frac("3", "4") + " = " + frac("5", "4"),
                frac("5", "4") + " = 1" + frac("1", "4") + ", so carry the extra whole one across.",
                "3 + 1" + frac("1", "4") + " = 4" + frac("1", "4"),
            ],
            "answer": "4" + frac("1", "4"),
        },
        {
            "marks": 3,
            "q": "<p>Work out " + frac("5", "8") + " &divide; " + frac("3", "4") + "</p>"
                 "<p>Give your answer in its simplest form.</p>",
            "steps": [
                "To divide by a fraction, turn it upside down and multiply instead.",
                frac("5", "8") + " &divide; " + frac("3", "4") + " = " + frac("5", "8") + " &times; " + frac("4", "3"),
                "Multiply across: " + frac("20", "24"),
                "Divide top and bottom by 4.",
            ],
            "answer": frac("5", "6"),
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Work out " + frac("3", "5") + " of 45</p>"
                 "<p class='part'>(b) Work out " + frac("2", "7") + " of 91</p>",
            "steps": [
                "&lsquo;Of&rsquo; means multiply. Divide by the bottom, then multiply by the top.",
                "<b>(a)</b> 45 &divide; 5 = 9, then 9 &times; 3 = 27",
                "<b>(b)</b> 91 &divide; 7 = 13, then 13 &times; 2 = 26",
            ],
            "answer": "(a) 27 &nbsp;&nbsp; (b) 26",
        },
        {
            "marks": 3,
            "q": "<p>Write these four numbers in order, starting with the smallest.</p>"
                 "<p><b>0.7&nbsp;&nbsp;&nbsp;" + frac("2", "3") + "&nbsp;&nbsp;&nbsp;68%&nbsp;&nbsp;&nbsp;0.71</b></p>",
            "steps": [
                "Change everything into decimals so they can be compared fairly.",
                frac("2", "3") + " = 2 &divide; 3 = 0.666&hellip;",
                "68% = 68 &divide; 100 = 0.68",
                "Now compare 0.7, 0.666&hellip;, 0.68 and 0.71",
                "Smallest first: 0.666&hellip;, 0.68, 0.7, 0.71",
            ],
            "answer": frac("2", "3") + ", 68%, 0.7, 0.71",
        },
        {
            "marks": 4,
            "q": "<p>A jug contains " + frac("3", "4") + " of a litre of juice.</p>"
                 "<p>Ali pours out " + frac("2", "5") + " of the juice.</p>"
                 "<p>How many litres of juice are left in the jug?</p>",
            "steps": [
                "If " + frac("2", "5") + " is poured out, the fraction left is 1 &minus; " + frac("2", "5") + " = " + frac("3", "5"),
                "So we need " + frac("3", "5") + " of " + frac("3", "4") + " of a litre.",
                frac("3", "5") + " &times; " + frac("3", "4") + " = " + frac("9", "20"),
                frac("9", "20") + " will not cancel, since 9 and 20 share no common factor.",
                "As a decimal this is 0.45 litres, which is a sensible check &mdash; a bit more than half of 0.75.",
            ],
            "answer": frac("9", "20") + " of a litre (0.45 litres)",
        },
        {
            "marks": 4,
            "q": "<p>A recipe uses 1" + frac("1", "3") + " cups of flour for one batch of biscuits.</p>"
                 "<p>Kwame makes 4" + frac("1", "2") + " batches.</p>"
                 "<p>How many cups of flour does he use?</p>",
            "steps": [
                "Change both mixed numbers into improper fractions first.",
                "1" + frac("1", "3") + " = " + frac("4", "3") + " and 4" + frac("1", "2") + " = " + frac("9", "2"),
                "Multiply: " + frac("4", "3") + " &times; " + frac("9", "2") + " = " + frac("36", "6"),
                "36 &divide; 6 = 6",
                "Check roughly: about 1.33 &times; 4.5 &asymp; 6 &#10003;",
            ],
            "answer": "6 cups",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Write the recurring decimal 0.363636&hellip; as a fraction in its simplest form.</p>",
            "steps": [
                "Two digits repeat, so the fraction has 99 on the bottom: " + frac("36", "99"),
                "The highest common factor of 36 and 99 is 9.",
                "36 &divide; 9 = 4 and 99 &divide; 9 = 11",
            ],
            "answer": frac("4", "11"),
        },
        {
            "marks": 2,
            "q": "<p>Work out 1" + frac("2", "3") + " &divide; 2" + frac("1", "2") + "</p>",
            "steps": [
                "Convert to improper fractions: 1" + frac("2", "3") + " = " + frac("5", "3") + " and 2" + frac("1", "2") + " = " + frac("5", "2"),
                "Dividing means multiplying by the reciprocal: " + frac("5", "3") + " &times; " + frac("2", "5") + " = " + frac("10", "15"),
                "Simplify by dividing by 5.",
            ],
            "answer": frac("2", "3"),
        },
        {
            "marks": 3,
            "q": "<p>Prove that the recurring decimal 0.4555&hellip; (only the 5 repeats) is equal to " + frac("41", "90") + "</p>",
            "steps": [
                "Let <i>x</i> = 0.4555&hellip;",
                "Multiply by 10 so the repeating part starts straight after the point: 10<i>x</i> = 4.555&hellip;",
                "Multiply by 100: 100<i>x</i> = 45.555&hellip;",
                "Subtract the two lines &mdash; the endless 555&hellip; tails cancel: 100<i>x</i> &minus; 10<i>x</i> = 45.555&hellip; &minus; 4.555&hellip;",
                "90<i>x</i> = 41, so <i>x</i> = " + frac("41", "90") + " as required.",
            ],
            "answer": "0.4555&hellip; = " + frac("41", "90"),
        },
        {
            "marks": 3,
            "q": "<p>Work out the value of &nbsp;(" + frac("2", "3") + ")<sup>&minus;2</sup></p>",
            "steps": [
                "A negative index means &lsquo;turn the fraction upside down&rsquo;.",
                "(" + frac("2", "3") + ")<sup>&minus;2</sup> = (" + frac("3", "2") + ")<sup>2</sup>",
                "Square top and bottom: " + frac("3<sup>2</sup>", "2<sup>2</sup>") + " = " + frac("9", "4"),
            ],
            "answer": frac("9", "4") + " &nbsp;(or 2" + frac("1", "4") + ")",
        },
        {
            "marks": 4,
            "q": "<p>In a school, " + frac("3", "5") + " of the students are girls.</p>"
                 "<p>" + frac("2", "9") + " of the girls play hockey.</p>"
                 "<p class='part'>(a) What fraction of all the students are girls who play hockey?</p>"
                 "<p class='part'>(b) The school has 450 students. How many girls play hockey?</p>",
            "steps": [
                "<b>(a)</b> &lsquo;" + frac("2", "9") + " of " + frac("3", "5") + "&rsquo; means multiply the fractions.",
                frac("2", "9") + " &times; " + frac("3", "5") + " = " + frac("6", "45"),
                "Simplify by dividing top and bottom by 3: " + frac("2", "15"),
                "<b>(b)</b> " + frac("2", "15") + " of 450: 450 &divide; 15 = 30, then 30 &times; 2 = 60",
            ],
            "answer": "(a) " + frac("2", "15") + " &nbsp;&nbsp; (b) 60 girls",
        },
        {
            "marks": 4,
            "q": "<p>Write as a single fraction in its simplest form</p>"
                 "<p>&nbsp;&nbsp;" + frac("2", "<i>x</i> + 1") + " + " + frac("3", "<i>x</i> &minus; 2") + "</p>",
            "steps": [
                "The common denominator is the product of the two brackets: (<i>x</i> + 1)(<i>x</i> &minus; 2)",
                "Rewrite each fraction: " + frac("2(<i>x</i> &minus; 2)", "(<i>x</i> + 1)(<i>x</i> &minus; 2)") + " + " + frac("3(<i>x</i> + 1)", "(<i>x</i> + 1)(<i>x</i> &minus; 2)"),
                "Expand the numerators: 2<i>x</i> &minus; 4 and 3<i>x</i> + 3",
                "Add them: 2<i>x</i> &minus; 4 + 3<i>x</i> + 3 = 5<i>x</i> &minus; 1",
                "Nothing cancels, so leave the bottom in factorised form.",
            ],
            "answer": frac("5<i>x</i> &minus; 1", "(<i>x</i> + 1)(<i>x</i> &minus; 2)"),
        },
        {
            "marks": 4,
            "q": "<p>Work out &nbsp;(2" + frac("1", "4") + " &minus; 1" + frac("5", "6") + ") &divide; " + frac("5", "6") + "</p>",
            "steps": [
                "Do the bracket first. 2" + frac("1", "4") + " = " + frac("9", "4") + " and 1" + frac("5", "6") + " = " + frac("11", "6"),
                "The lowest common denominator of 4 and 6 is 12: " + frac("27", "12") + " &minus; " + frac("22", "12") + " = " + frac("5", "12"),
                "Now divide: " + frac("5", "12") + " &divide; " + frac("5", "6") + " = " + frac("5", "12") + " &times; " + frac("6", "5"),
                "= " + frac("30", "60") + " = " + frac("1", "2"),
            ],
            "answer": frac("1", "2"),
        },
        {
            "marks": 4,
            "q": "<p>Mia spends " + frac("2", "5") + " of her money on a coat.</p>"
                 "<p>She then spends " + frac("1", "3") + " of what is left on a pair of shoes.</p>"
                 "<p>Mia now has &pound;36 left.</p>"
                 "<p>How much money did she start with?</p>",
            "steps": [
                "After the coat she has 1 &minus; " + frac("2", "5") + " = " + frac("3", "5") + " of her money left.",
                "She spends " + frac("1", "3") + " of that, so " + frac("2", "3") + " of it remains.",
                "Fraction still left = " + frac("2", "3") + " &times; " + frac("3", "5") + " = " + frac("6", "15") + " = " + frac("2", "5"),
                "So " + frac("2", "5") + " of the original amount is &pound;36.",
                frac("1", "5") + " = 36 &divide; 2 = &pound;18, so the whole amount is 5 &times; 18 = &pound;90",
                "Check: coat &pound;36, leaving &pound;54; shoes " + frac("1", "3") + " of 54 = &pound;18, leaving &pound;36 &#10003;",
            ],
            "answer": "&pound;90",
        },
        {
            "marks": 4,
            "q": "<p>Simplify fully</p>"
                 "<p>&nbsp;&nbsp;" + frac("<i>x</i><sup>2</sup> &minus; 4", "<i>x</i><sup>2</sup> + 5<i>x</i> + 6")
                 + " &times; " + frac("<i>x</i> + 3", "<i>x</i> &minus; 2") + "</p>",
            "steps": [
                "Factorise everything you can before multiplying.",
                "<i>x</i><sup>2</sup> &minus; 4 = (<i>x</i> + 2)(<i>x</i> &minus; 2) &nbsp;(difference of two squares)",
                "<i>x</i><sup>2</sup> + 5<i>x</i> + 6 = (<i>x</i> + 2)(<i>x</i> + 3)",
                "The product is " + frac("(<i>x</i> + 2)(<i>x</i> &minus; 2)(<i>x</i> + 3)", "(<i>x</i> + 2)(<i>x</i> + 3)(<i>x</i> &minus; 2)"),
                "Every factor on the top also appears on the bottom, so everything cancels.",
            ],
            "answer": "1",
        },
        {
            "marks": 5,
            "q": "<p>A rectangular garden measures 2" + frac("3", "4") + " m by 1" + frac("1", "3") + " m.</p>"
                 "<p class='part'>(a) Work out the area of the garden. Give your answer as a mixed number.</p>"
                 "<p class='part'>(b) Fencing costs &pound;12 per metre. Work out the cost of fencing all the way round.</p>",
            "steps": [
                "<b>(a)</b> Convert to improper fractions: 2" + frac("3", "4") + " = " + frac("11", "4") + " and 1" + frac("1", "3") + " = " + frac("4", "3"),
                "Area = " + frac("11", "4") + " &times; " + frac("4", "3") + " = " + frac("44", "12") + " = " + frac("11", "3") + " = 3" + frac("2", "3") + " m<sup>2</sup>",
                "<b>(b)</b> Perimeter = 2 &times; (" + frac("11", "4") + " + " + frac("4", "3") + ")",
                "Common denominator 12: " + frac("33", "12") + " + " + frac("16", "12") + " = " + frac("49", "12"),
                "Perimeter = 2 &times; " + frac("49", "12") + " = " + frac("49", "6") + " m",
                "Cost = " + frac("49", "6") + " &times; 12 = 49 &times; 2 = &pound;98",
            ],
            "answer": "(a) 3" + frac("2", "3") + " m<sup>2</sup> &nbsp;&nbsp; (b) &pound;98",
        },
    ],
}

PERCENTAGES = {
    "title": "Percentages",
    "folder": "gcse/number",
    "slug": "percentages-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write 0.35 as a percentage.</p>",
            "steps": [
                "To change a decimal into a percentage, multiply by 100.",
                "0.35 &times; 100 = 35",
            ],
            "answer": "35%",
        },
        {
            "marks": 2,
            "q": "<p>Work out 20% of 65</p>",
            "steps": [
                "10% of 65 = 65 &divide; 10 = 6.5",
                "20% is double 10%: 2 &times; 6.5 = 13",
            ],
            "answer": "13",
        },
        {
            "marks": 2,
            "q": "<p>Write 18 out of 40 as a percentage.</p>",
            "steps": [
                "Write it as a fraction: " + frac("18", "40"),
                "Multiply by 100: " + frac("18", "40") + " &times; 100 = 18 &times; 2.5 = 45",
            ],
            "answer": "45%",
        },
        {
            "marks": 2,
            "q": "<p>Increase 200 by 12%</p>",
            "steps": [
                "10% of 200 = 20 and 1% of 200 = 2, so 12% = 20 + 2 + 2 = 24",
                "Increase means add on: 200 + 24 = 224",
                "(Or multiply straight away by 1.12.)",
            ],
            "answer": "224",
        },
        {
            "marks": 3,
            "q": "<p>A jacket costs &pound;70.</p>"
                 "<p>In a sale the price is reduced by 30%.</p>"
                 "<p>Work out the sale price.</p>",
            "steps": [
                "10% of 70 = 7, so 30% of 70 = 21",
                "The reduction is &pound;21.",
                "Sale price = 70 &minus; 21 = &pound;49",
                "(Or multiply by 0.7 directly: 70 &times; 0.7 = 49.)",
            ],
            "answer": "&pound;49",
        },
        {
            "marks": 3,
            "q": "<p>Work out 17.5% of 480 without a calculator.</p>",
            "steps": [
                "Break 17.5% into pieces you can find easily.",
                "10% of 480 = 48",
                "5% is half of 10% = 24",
                "2.5% is half of 5% = 12",
                "17.5% = 48 + 24 + 12 = 84",
            ],
            "answer": "84",
        },
        {
            "marks": 3,
            "q": "<p>Ben scored 34 out of 50 in a test.</p>"
                 "<p>Amy scored 27 out of 40 in a different test.</p>"
                 "<p>Who did better? You must show your working.</p>",
            "steps": [
                "Convert both scores to percentages so they can be compared.",
                "Ben: " + frac("34", "50") + " &times; 100 = 34 &times; 2 = 68%",
                "Amy: " + frac("27", "40") + " &times; 100 = 27 &times; 2.5 = 67.5%",
                "68% is greater than 67.5%.",
            ],
            "answer": "Ben (68% against Amy&rsquo;s 67.5%)",
        },
        {
            "marks": 3,
            "q": "<p>Priya invests &pound;500 for 3 years at 4% <b>simple</b> interest per year.</p>"
                 "<p>Work out the total amount in her account after 3 years.</p>",
            "steps": [
                "Simple interest means the same amount of interest is earned each year.",
                "4% of 500 = 0.04 &times; 500 = &pound;20 per year",
                "Over 3 years the interest is 3 &times; 20 = &pound;60",
                "Total = 500 + 60 = &pound;560",
            ],
            "answer": "&pound;560",
        },
        {
            "marks": 4,
            "q": "<p>A house was bought for &pound;180 000 and later sold for &pound;207 000.</p>"
                 "<p>Work out the percentage increase in the value of the house.</p>",
            "steps": [
                "First find the actual increase: 207 000 &minus; 180 000 = &pound;27 000",
                "Percentage change = " + frac("change", "original amount") + " &times; 100",
                "= " + frac("27 000", "180 000") + " &times; 100",
                frac("27", "180") + " = 0.15",
                "0.15 &times; 100 = 15%",
            ],
            "answer": "15% increase",
        },
        {
            "marks": 4,
            "q": "<p>A laptop is advertised at &pound;320 plus VAT at 20%.</p>"
                 "<p class='part'>(a) Work out the total price including VAT.</p>"
                 "<p class='part'>(b) A voucher takes 15% off the total price. Work out the price after the voucher.</p>",
            "steps": [
                "<b>(a)</b> 20% of 320 = 0.2 &times; 320 = &pound;64",
                "Total = 320 + 64 = &pound;384",
                "<b>(b)</b> Taking 15% off means paying 85%, so multiply by 0.85",
                "384 &times; 0.85 = 326.40",
                "The price is &pound;326.40",
            ],
            "answer": "(a) &pound;384 &nbsp;&nbsp; (b) &pound;326.40",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Write</p>"
                 "<p class='part'>(a) 0.8 as a percentage</p>"
                 "<p class='part'>(b) " + frac("3", "8") + " as a percentage</p>",
            "steps": [
                "<b>(a)</b> 0.8 &times; 100 = 80%",
                "<b>(b)</b> 3 &divide; 8 = 0.375, and 0.375 &times; 100 = 37.5%",
            ],
            "answer": "(a) 80% &nbsp;&nbsp; (b) 37.5%",
        },
        {
            "marks": 2,
            "q": "<p>Write down the single multiplier you would use for</p>"
                 "<p class='part'>(a) a 7% decrease</p>"
                 "<p class='part'>(b) a 3.5% increase</p>",
            "steps": [
                "<b>(a)</b> A decrease of 7% leaves 100 &minus; 7 = 93%, so the multiplier is 0.93",
                "<b>(b)</b> An increase of 3.5% gives 103.5%, so the multiplier is 1.035",
            ],
            "answer": "(a) 0.93 &nbsp;&nbsp; (b) 1.035",
        },
        {
            "marks": 3,
            "q": "<p>After a 12% discount, a coat costs &pound;52.80</p>"
                 "<p>Work out the original price of the coat.</p>",
            "steps": [
                "This is a reverse percentage &mdash; the &pound;52.80 is <i>after</i> the discount.",
                "The multiplier used was 1 &minus; 0.12 = 0.88",
                "So original price &times; 0.88 = 52.80",
                "Original price = 52.80 &divide; 0.88 = &pound;60",
                "Check: 60 &times; 0.88 = 52.80 &#10003;",
            ],
            "answer": "&pound;60",
        },
        {
            "marks": 3,
            "q": "<p>&pound;4000 is invested at 2.5% compound interest per year.</p>"
                 "<p>Work out the value of the investment after 3 years, to the nearest penny.</p>",
            "steps": [
                "The multiplier for a 2.5% increase is 1.025",
                "Value = 4000 &times; 1.025<sup>3</sup>",
                "1.025<sup>3</sup> = 1.076890625",
                "4000 &times; 1.076890625 = 4307.5625",
            ],
            "answer": "&pound;4307.56",
        },
        {
            "marks": 4,
            "q": "<p>A car is worth &pound;15 000 when new.</p>"
                 "<p>It loses 18% of its value in the first year, then 12% of its value in each year after that.</p>"
                 "<p>Work out the value of the car after 3 years.</p>",
            "steps": [
                "First year multiplier: 1 &minus; 0.18 = 0.82",
                "Later years multiplier: 1 &minus; 0.12 = 0.88, applied twice.",
                "Value = 15 000 &times; 0.82 &times; 0.88<sup>2</sup>",
                "15 000 &times; 0.82 = 12 300",
                "12 300 &times; 0.88 = 10 824, then 10 824 &times; 0.88 = 9525.12",
            ],
            "answer": "&pound;9525.12",
        },
        {
            "marks": 4,
            "q": "<p>The price of a phone is increased by 20% and then decreased by 20%.</p>"
                 "<p>Show that the final price is 4% less than the original price.</p>",
            "steps": [
                "Do not assume the two changes cancel out &mdash; the 20% decrease is taken from a bigger amount.",
                "Multiplier for the increase: 1.2",
                "Multiplier for the decrease: 0.8",
                "Overall multiplier = 1.2 &times; 0.8 = 0.96",
                "0.96 means the final price is 96% of the original, which is a 4% decrease.",
                "Check with &pound;100: it rises to &pound;120, then falls by &pound;24 to &pound;96 &#10003;",
            ],
            "answer": "Overall multiplier 1.2 &times; 0.8 = 0.96, so a 4% decrease",
        },
        {
            "marks": 4,
            "q": "<p>&pound;2500 is invested at 4% compound interest per year.</p>"
                 "<p>Work out the least number of complete years before the investment is worth more than &pound;3000.</p>",
            "steps": [
                "Each year the amount is multiplied by 1.04",
                "After 4 years: 2500 &times; 1.04<sup>4</sup> = 2500 &times; 1.16985856 = &pound;2924.65 &mdash; not enough.",
                "After 5 years: 2500 &times; 1.04<sup>5</sup> = 2500 &times; 1.2166529 = &pound;3041.63 &mdash; this is over &pound;3000.",
                "So it first passes &pound;3000 during the 5th year.",
            ],
            "answer": "5 years",
        },
        {
            "marks": 4,
            "q": "<p>An investment grows by 10% compound interest each year.</p>"
                 "<p>After 3 years it is worth &pound;6655.</p>"
                 "<p>Work out how much was invested at the start.</p>",
            "steps": [
                "The multiplier each year is 1.1, so over 3 years the total multiplier is 1.1<sup>3</sup>",
                "1.1<sup>3</sup> = 1.331",
                "So starting amount &times; 1.331 = 6655",
                "Starting amount = 6655 &divide; 1.331 = &pound;5000",
                "Check: 5000 &rarr; 5500 &rarr; 6050 &rarr; 6655 &#10003;",
            ],
            "answer": "&pound;5000",
        },
        {
            "marks": 4,
            "q": "<p>In a club, 60% of the members are women.</p>"
                 "<p>25% of the women and 40% of the men wear glasses.</p>"
                 "<p>What percentage of all the members wear glasses?</p>",
            "steps": [
                "Working with 100 members makes this easier: 60 women and 40 men.",
                "Women with glasses: 25% of 60 = 15",
                "Men with glasses: 40% of 40 = 16",
                "Total with glasses = 15 + 16 = 31 out of 100",
            ],
            "answer": "31%",
        },
        {
            "marks": 5,
            "q": "<p>A television has a list price of &pound;250.</p>"
                 "<p><b>Shop A</b> takes 20% off, then a further 10% off the reduced price.</p>"
                 "<p><b>Shop B</b> takes 30% off the list price.</p>"
                 "<p class='part'>(a) Work out the price in each shop.</p>"
                 "<p class='part'>(b) Which shop is cheaper, and by how much?</p>"
                 "<p class='part'>(c) Work out the single percentage reduction that Shop A actually gives.</p>",
            "steps": [
                "<b>(a)</b> Shop A: 250 &times; 0.8 = &pound;200, then 200 &times; 0.9 = &pound;180",
                "Shop B: 250 &times; 0.7 = &pound;175",
                "<b>(b)</b> Shop B is cheaper by 180 &minus; 175 = &pound;5",
                "<b>(c)</b> Shop A&rsquo;s overall multiplier is 0.8 &times; 0.9 = 0.72",
                "0.72 means the customer pays 72% of the list price.",
                "So the single reduction is 100 &minus; 72 = 28%, not the 30% you might expect from adding 20 and 10.",
            ],
            "answer": "(a) A &pound;180, B &pound;175 &nbsp;&nbsp; (b) Shop B, by &pound;5 &nbsp;&nbsp; (c) 28%",
        },
    ],
}

POWERS = {
    "title": "Powers, Roots and Standard Form",
    "folder": "gcse/number",
    "slug": "powers-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Work out 4<sup>3</sup></p>",
            "steps": [
                "4<sup>3</sup> means 4 &times; 4 &times; 4",
                "4 &times; 4 = 16, then 16 &times; 4 = 64",
            ],
            "answer": "64",
        },
        {
            "marks": 2,
            "q": "<p>Work out</p>"
                 "<p class='part'>(a) &radic;49</p>"
                 "<p class='part'>(b) the cube root of 27</p>",
            "steps": [
                "<b>(a)</b> 7 &times; 7 = 49, so &radic;49 = 7",
                "<b>(b)</b> 3 &times; 3 &times; 3 = 27, so the cube root of 27 is 3",
            ],
            "answer": "(a) 7 &nbsp;&nbsp; (b) 3",
        },
        {
            "marks": 2,
            "q": "<p>Simplify 3<sup>4</sup> &times; 3<sup>2</sup>, giving your answer as a single power of 3.</p>",
            "steps": [
                "When multiplying powers of the same number, add the indices.",
                "4 + 2 = 6",
                "So the answer is 3<sup>6</sup> (which equals 729).",
            ],
            "answer": "3<sup>6</sup>",
        },
        {
            "marks": 2,
            "q": "<p>Write 5600 in standard form.</p>",
            "steps": [
                "Standard form is A &times; 10<sup>n</sup> where A is between 1 and 10.",
                "Put the decimal point after the first digit: 5.6",
                "The point has moved 3 places, so the power is 3.",
            ],
            "answer": "5.6 &times; 10<sup>3</sup>",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Write 0.00042 in standard form.</p>"
                 "<p class='part'>(b) Write 3.1 &times; 10<sup>5</sup> as an ordinary number.</p>",
            "steps": [
                "<b>(a)</b> Move the point to just after the first non-zero digit: 4.2",
                "The point moved 4 places to the right, so the index is negative: 4.2 &times; 10<sup>&minus;4</sup>",
                "<b>(b)</b> A power of 5 means move the point 5 places to the right.",
                "3.1 becomes 310 000",
            ],
            "answer": "(a) 4.2 &times; 10<sup>&minus;4</sup> &nbsp;&nbsp; (b) 310 000",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Work out 2<sup>5</sup> &divide; 2<sup>2</sup></p>"
                 "<p class='part'>(b) Write down the value of 7<sup>0</sup></p>",
            "steps": [
                "<b>(a)</b> When dividing powers of the same number, subtract the indices: 5 &minus; 2 = 3",
                "2<sup>3</sup> = 8",
                "<b>(b)</b> Anything (other than 0) raised to the power 0 equals 1.",
            ],
            "answer": "(a) 8 &nbsp;&nbsp; (b) 1",
        },
        {
            "marks": 3,
            "q": "<p>Work out (3 &times; 10<sup>4</sup>) &times; (2 &times; 10<sup>3</sup>)</p>"
                 "<p>Give your answer in standard form.</p>",
            "steps": [
                "Multiply the number parts and the powers separately.",
                "3 &times; 2 = 6",
                "10<sup>4</sup> &times; 10<sup>3</sup> = 10<sup>7</sup> (add the indices)",
                "6 is between 1 and 10, so the answer is already in standard form.",
            ],
            "answer": "6 &times; 10<sup>7</sup>",
        },
        {
            "marks": 3,
            "q": "<p>In each pair, work out which is larger. Show your working.</p>"
                 "<p class='part'>(a) 2<sup>6</sup> or 3<sup>4</sup></p>"
                 "<p class='part'>(b) 5<sup>3</sup> or 2<sup>7</sup></p>",
            "steps": [
                "<b>(a)</b> 2<sup>6</sup> = 64 and 3<sup>4</sup> = 81, so 3<sup>4</sup> is larger.",
                "<b>(b)</b> 5<sup>3</sup> = 125 and 2<sup>7</sup> = 128, so 2<sup>7</sup> is larger.",
                "Notice you cannot just compare the bases or the indices &mdash; you must work them out.",
            ],
            "answer": "(a) 3<sup>4</sup> = 81 &nbsp;&nbsp; (b) 2<sup>7</sup> = 128",
        },
        {
            "marks": 4,
            "q": "<p class='part'>(a) Between which two consecutive whole numbers does &radic;150 lie? "
                 "Explain your answer.</p>"
                 "<p class='part'>(b) By working out 12.2<sup>2</sup> and 12.3<sup>2</sup>, say which of these is "
                 "closer to &radic;150.</p>",
            "steps": [
                "<b>(a)</b> 12<sup>2</sup> = 144 and 13<sup>2</sup> = 169",
                "150 lies between 144 and 169, so &radic;150 lies between 12 and 13.",
                "<b>(b)</b> 12.2<sup>2</sup> = 148.84 and 12.3<sup>2</sup> = 151.29",
                "150 &minus; 148.84 = 1.16 while 151.29 &minus; 150 = 1.29",
                "148.84 is the closer of the two, so &radic;150 is a little nearer to 12.2",
            ],
            "answer": "(a) between 12 and 13 &nbsp;&nbsp; (b) 12.2 is closer",
        },
        {
            "marks": 4,
            "q": "<p>The mass of the Sun is 1.99 &times; 10<sup>30</sup> kg.</p>"
                 "<p>The mass of the Earth is 5.97 &times; 10<sup>24</sup> kg.</p>"
                 "<p>How many times heavier is the Sun than the Earth?</p>"
                 "<p>Give your answer in standard form to 3 significant figures.</p>",
            "steps": [
                "Divide the Sun&rsquo;s mass by the Earth&rsquo;s mass.",
                "Number parts: 1.99 &divide; 5.97 = 0.33333&hellip;",
                "Powers: 10<sup>30</sup> &divide; 10<sup>24</sup> = 10<sup>6</sup> (subtract the indices)",
                "So the answer is 0.3333&hellip; &times; 10<sup>6</sup>",
                "0.3333 is less than 1, so adjust: 0.3333 &times; 10<sup>6</sup> = 3.333 &times; 10<sup>5</sup>",
            ],
            "answer": "3.33 &times; 10<sup>5</sup> times heavier (3 s.f.)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Work out</p>"
                 "<p class='part'>(a) 5<sup>&minus;2</sup></p>"
                 "<p class='part'>(b) 16<sup>3/4</sup></p>",
            "steps": [
                "<b>(a)</b> A negative index means &lsquo;one over&rsquo;: 5<sup>&minus;2</sup> = " + frac("1", "5<sup>2</sup>") + " = " + frac("1", "25"),
                "<b>(b)</b> The bottom of the fraction index is a root and the top is a power.",
                "The fourth root of 16 is 2, and 2<sup>3</sup> = 8",
            ],
            "answer": "(a) " + frac("1", "25") + " &nbsp;&nbsp; (b) 8",
        },
        {
            "marks": 2,
            "q": "<p>Simplify &radic;50 + &radic;8, giving your answer in the form a&radic;2</p>",
            "steps": [
                "Look for square factors. 50 = 25 &times; 2, so &radic;50 = 5&radic;2",
                "8 = 4 &times; 2, so &radic;8 = 2&radic;2",
                "Now they are like terms: 5&radic;2 + 2&radic;2 = 7&radic;2",
            ],
            "answer": "7&radic;2",
        },
        {
            "marks": 3,
            "q": "<p>Rationalise the denominator of " + frac("10", "&radic;5") + " and simplify your answer.</p>",
            "steps": [
                "Multiply the top and the bottom by &radic;5 &mdash; this does not change the value.",
                frac("10", "&radic;5") + " &times; " + frac("&radic;5", "&radic;5") + " = " + frac("10&radic;5", "5"),
                "&radic;5 &times; &radic;5 = 5, which clears the surd from the bottom.",
                "10 &divide; 5 = 2, so the answer is 2&radic;5",
            ],
            "answer": "2&radic;5",
        },
        {
            "marks": 3,
            "q": "<p>Expand and simplify (3 + &radic;2)(4 &minus; &radic;2)</p>",
            "steps": [
                "Multiply out all four pairs.",
                "3 &times; 4 = 12, &nbsp; 3 &times; (&minus;&radic;2) = &minus;3&radic;2",
                "&radic;2 &times; 4 = 4&radic;2, &nbsp; &radic;2 &times; (&minus;&radic;2) = &minus;2",
                "Collect: 12 &minus; 2 = 10 and &minus;3&radic;2 + 4&radic;2 = &radic;2",
            ],
            "answer": "10 + &radic;2",
        },
        {
            "marks": 4,
            "q": "<p>Work out (4.8 &times; 10<sup>5</sup>) &divide; (1.6 &times; 10<sup>&minus;2</sup>)</p>"
                 "<p>Give your answer in standard form.</p>",
            "steps": [
                "Divide the number parts: 4.8 &divide; 1.6 = 3",
                "Divide the powers by subtracting the indices: 5 &minus; (&minus;2) = 5 + 2 = 7",
                "Take care with the double negative &mdash; subtracting &minus;2 means adding 2.",
                "So the answer is 3 &times; 10<sup>7</sup>, already in standard form.",
            ],
            "answer": "3 &times; 10<sup>7</sup>",
        },
        {
            "marks": 4,
            "q": "<p>Work out the value of &nbsp;(" + frac("8", "27") + ")<sup>&minus;2/3</sup></p>",
            "steps": [
                "The negative sign means turn the fraction over: (" + frac("27", "8") + ")<sup>2/3</sup>",
                "The 3 on the bottom of the index means take the cube root of top and bottom.",
                "Cube root of 27 = 3 and cube root of 8 = 2, giving " + frac("3", "2"),
                "The 2 on the top of the index means square it: (" + frac("3", "2") + ")<sup>2</sup> = " + frac("9", "4"),
            ],
            "answer": frac("9", "4") + " &nbsp;(or 2.25)",
        },
        {
            "marks": 4,
            "q": "<p>Solve each equation.</p>"
                 "<p class='part'>(a) 2<sup><i>x</i></sup> = 32</p>"
                 "<p class='part'>(b) 3<sup><i>x</i> + 1</sup> = 81</p>"
                 "<p class='part'>(c) 5<sup><i>x</i></sup> = " + frac("1", "25") + "</p>",
            "steps": [
                "<b>(a)</b> Write 32 as a power of 2: 32 = 2<sup>5</sup>, so <i>x</i> = 5",
                "<b>(b)</b> 81 = 3<sup>4</sup>, so <i>x</i> + 1 = 4",
                "<i>x</i> = 3",
                "<b>(c)</b> " + frac("1", "25") + " = 5<sup>&minus;2</sup>, so <i>x</i> = &minus;2",
            ],
            "answer": "(a) 5 &nbsp;&nbsp; (b) 3 &nbsp;&nbsp; (c) &minus;2",
        },
        {
            "marks": 4,
            "q": "<p>A square has area 48 cm<sup>2</sup>.</p>"
                 "<p class='part'>(a) Find the exact length of one side, in the form a&radic;b.</p>"
                 "<p class='part'>(b) Find the exact perimeter of the square.</p>",
            "steps": [
                "<b>(a)</b> Side length = &radic;48",
                "Look for the largest square factor: 48 = 16 &times; 3",
                "&radic;48 = &radic;16 &times; &radic;3 = 4&radic;3 cm",
                "<b>(b)</b> Perimeter = 4 &times; 4&radic;3 = 16&radic;3 cm",
                "(As a check, 16&radic;3 &asymp; 27.7 cm, which is sensible for a square of area 48 cm<sup>2</sup>.)",
            ],
            "answer": "(a) 4&radic;3 cm &nbsp;&nbsp; (b) 16&radic;3 cm",
        },
        {
            "marks": 4,
            "q": "<p>The Earth is approximately 1.5 &times; 10<sup>8</sup> km from the Sun.</p>"
                 "<p>Light travels at approximately 3 &times; 10<sup>5</sup> km per second.</p>"
                 "<p>Work out how many minutes light takes to travel from the Sun to the Earth. "
                 "Give your answer to the nearest minute.</p>",
            "steps": [
                "Time = " + frac("distance", "speed") + " = " + frac("1.5 &times; 10<sup>8</sup>", "3 &times; 10<sup>5</sup>"),
                "Number parts: 1.5 &divide; 3 = 0.5",
                "Powers: 10<sup>8</sup> &divide; 10<sup>5</sup> = 10<sup>3</sup>",
                "Time = 0.5 &times; 10<sup>3</sup> = 500 seconds",
                "Convert to minutes: 500 &divide; 60 = 8.33&hellip; minutes",
            ],
            "answer": "about 8 minutes",
        },
        {
            "marks": 5,
            "q": "<p>Rationalise the denominator of</p>"
                 "<p>&nbsp;&nbsp;" + frac("5 + &radic;3", "2 &minus; &radic;3") + "</p>"
                 "<p>Give your answer in the form a + b&radic;3</p>",
            "steps": [
                "Multiply the top and bottom by the <b>conjugate</b> of the bottom, which is 2 + &radic;3",
                "Bottom: (2 &minus; &radic;3)(2 + &radic;3) = 4 + 2&radic;3 &minus; 2&radic;3 &minus; 3 = 4 &minus; 3 = 1",
                "The surd terms cancel &mdash; that is the point of using the conjugate.",
                "Top: (5 + &radic;3)(2 + &radic;3) = 10 + 5&radic;3 + 2&radic;3 + 3",
                "= 13 + 7&radic;3",
                "So the fraction is " + frac("13 + 7&radic;3", "1") + " = 13 + 7&radic;3",
            ],
            "answer": "13 + 7&radic;3",
        },
    ],
}

ROUNDING = {
    "title": "Rounding, Estimation and Bounds",
    "folder": "gcse/number",
    "slug": "rounding-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Round 4.837 to 1 decimal place.</p>",
            "steps": [
                "Look at the second decimal place, which is 3.",
                "3 is less than 5, so the first decimal place stays as it is.",
            ],
            "answer": "4.8",
        },
        {
            "marks": 2,
            "q": "<p>Round 27 483</p>"
                 "<p class='part'>(a) to the nearest 100</p>"
                 "<p class='part'>(b) to the nearest 1000</p>",
            "steps": [
                "<b>(a)</b> The tens digit is 8, which is 5 or more, so round the hundreds up: 27 500",
                "<b>(b)</b> The hundreds digit is 4, which is less than 5, so round down: 27 000",
            ],
            "answer": "(a) 27 500 &nbsp;&nbsp; (b) 27 000",
        },
        {
            "marks": 2,
            "q": "<p>Round 0.004617 to 2 significant figures.</p>",
            "steps": [
                "Leading zeros do not count, so the first significant figure is the 4 and the second is the 6.",
                "The next digit is 1, which is less than 5, so round down.",
                "Keep the zeros that hold the place value.",
            ],
            "answer": "0.0046",
        },
        {
            "marks": 2,
            "q": "<p>Round 78 452 to 3 significant figures.</p>",
            "steps": [
                "The first three significant figures are 7, 8 and 4.",
                "The next digit is 5, so round the 4 up to 5.",
                "Replace the remaining digits with zeros to keep the size right.",
            ],
            "answer": "78 500",
        },
        {
            "marks": 3,
            "q": "<p>Work out an estimate for 39.2 &times; 5.87</p>",
            "steps": [
                "Round each number to 1 significant figure.",
                "39.2 &asymp; 40 and 5.87 &asymp; 6",
                "40 &times; 6 = 240",
                "(The exact answer is 230.1&hellip;, so 240 is a reasonable estimate.)",
            ],
            "answer": "about 240",
        },
        {
            "marks": 3,
            "q": "<p>Work out an estimate for &nbsp;" + frac("28.7 &times; 9.6", "4.9") + "</p>",
            "steps": [
                "Round each number to 1 significant figure.",
                "28.7 &asymp; 30, &nbsp; 9.6 &asymp; 10, &nbsp; 4.9 &asymp; 5",
                "Top: 30 &times; 10 = 300",
                "300 &divide; 5 = 60",
            ],
            "answer": "about 60",
        },
        {
            "marks": 3,
            "q": "<p>A number, <i>n</i>, is rounded to the nearest 10. The result is 80.</p>"
                 "<p class='part'>(a) Write down the smallest possible value of <i>n</i>.</p>"
                 "<p class='part'>(b) Write down the error interval for <i>n</i> using inequalities.</p>",
            "steps": [
                "Anything from 75 upwards rounds up to 80.",
                "<b>(a)</b> The smallest value is 75",
                "<b>(b)</b> At the top end, 85 would round up to 90, so 85 is not included.",
                "The error interval is 75 &le; <i>n</i> &lt; 85",
            ],
            "answer": "(a) 75 &nbsp;&nbsp; (b) 75 &le; <i>n</i> &lt; 85",
        },
        {
            "marks": 3,
            "q": "<p>A length is measured as 6.4 cm, correct to 1 decimal place.</p>"
                 "<p class='part'>(a) Write down the lower bound of the length.</p>"
                 "<p class='part'>(b) Write down the upper bound of the length.</p>",
            "steps": [
                "1 decimal place means the measurement is accurate to within half of 0.1, which is 0.05",
                "<b>(a)</b> Lower bound = 6.4 &minus; 0.05 = 6.35 cm",
                "<b>(b)</b> Upper bound = 6.4 + 0.05 = 6.45 cm",
                "(Strictly the true length can equal 6.35 but not 6.45.)",
            ],
            "answer": "(a) 6.35 cm &nbsp;&nbsp; (b) 6.45 cm",
        },
        {
            "marks": 4,
            "q": "<p>Work out an estimate for &nbsp;" + frac("4.87<sup>2</sup> &times; 19.6", "0.51") + "</p>",
            "steps": [
                "Round each number to 1 significant figure.",
                "4.87 &asymp; 5, &nbsp; 19.6 &asymp; 20, &nbsp; 0.51 &asymp; 0.5",
                "Top: 5<sup>2</sup> &times; 20 = 25 &times; 20 = 500",
                "Dividing by 0.5 is the same as multiplying by 2.",
                "500 &divide; 0.5 = 1000",
            ],
            "answer": "about 1000",
        },
        {
            "marks": 4,
            "q": "<p>Sam estimates 4.8 &times; 6.2 as 5 &times; 6 = 30</p>"
                 "<p class='part'>(a) Work out the exact value of 4.8 &times; 6.2</p>"
                 "<p class='part'>(b) Is Sam&rsquo;s estimate too big or too small? Explain your answer without "
                 "using your answer to part (a).</p>",
            "steps": [
                "<b>(a)</b> 4.8 &times; 6.2 = 29.76",
                "<b>(b)</b> Sam rounded 4.8 <i>up</i> by 0.2 and rounded 6.2 <i>down</i> by 0.2.",
                "Rounding 4.8 up to 5 adds roughly 6 &times; 0.2 = 1.2 to the answer.",
                "Rounding 6.2 down to 6 takes away roughly 5 &times; 0.2 = 1.0",
                "The increase is bigger than the decrease, so the estimate is too big &mdash; an overestimate.",
            ],
            "answer": "(a) 29.76 &nbsp;&nbsp; (b) too big (an overestimate)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p><i>x</i> = 8.3 correct to 1 decimal place.</p>"
                 "<p>Write down the error interval for <i>x</i>.</p>",
            "steps": [
                "Half of the last place value is 0.05",
                "Lower bound = 8.3 &minus; 0.05 = 8.25 and upper bound = 8.3 + 0.05 = 8.35",
                "8.35 would round up to 8.4, so it is not included.",
            ],
            "answer": "8.25 &le; <i>x</i> &lt; 8.35",
        },
        {
            "marks": 2,
            "q": "<p>A mass m is 4.6 kg correct to 2 significant figures.</p>"
                 "<p>Write down the error interval for m.</p>",
            "steps": [
                "2 significant figures here means the value is given to the nearest 0.1 kg.",
                "Half of 0.1 is 0.05",
                "So the bounds are 4.6 &minus; 0.05 = 4.55 and 4.6 + 0.05 = 4.65",
            ],
            "answer": "4.55 &le; m &lt; 4.65",
        },
        {
            "marks": 3,
            "q": "<p>a = 12.4 and b = 3.7, each correct to 1 decimal place.</p>"
                 "<p>Work out the upper bound of a + b.</p>",
            "steps": [
                "Bounds for a: 12.35 to 12.45",
                "Bounds for b: 3.65 to 3.75",
                "To make a sum as large as possible, use the upper bound of both numbers.",
                "12.45 + 3.75 = 16.2",
            ],
            "answer": "16.2",
        },
        {
            "marks": 3,
            "q": "<p>a = 12.4 and b = 3.7, each correct to 1 decimal place.</p>"
                 "<p>Work out the lower bound of a &minus; b.</p>",
            "steps": [
                "To make a subtraction as small as possible, start from the smallest a and take away the largest b.",
                "Lower bound of a = 12.35 and upper bound of b = 3.75",
                "12.35 &minus; 3.75 = 8.6",
                "A common error is to use both lower bounds &mdash; that would give too large an answer.",
            ],
            "answer": "8.6",
        },
        {
            "marks": 4,
            "q": "<p>A rectangle has length 8.4 cm and width 5.2 cm, each correct to 1 decimal place.</p>"
                 "<p>Work out the upper bound of the area of the rectangle.</p>",
            "steps": [
                "Upper bound of the length = 8.45 cm",
                "Upper bound of the width = 5.25 cm",
                "For a product, the largest result comes from using both upper bounds.",
                "8.45 &times; 5.25 = 44.3625",
            ],
            "answer": "44.3625 cm<sup>2</sup>",
        },
        {
            "marks": 4,
            "q": "<p>A runner covers 240 m, measured to the nearest 10 m, in 18 seconds, measured to the "
                 "nearest second.</p>"
                 "<p class='part'>(a) Work out the upper bound of the average speed.</p>"
                 "<p class='part'>(b) Work out the lower bound of the average speed, to 2 decimal places.</p>",
            "steps": [
                "Distance bounds: 235 m to 245 m. Time bounds: 17.5 s to 18.5 s.",
                "<b>(a)</b> A fraction is largest when the top is largest and the bottom is smallest.",
                "Upper bound of speed = " + frac("245", "17.5") + " = 14 m/s",
                "<b>(b)</b> Smallest top over largest bottom.",
                "Lower bound of speed = " + frac("235", "18.5") + " = 12.7027&hellip; = 12.70 m/s (2 d.p.)",
            ],
            "answer": "(a) 14 m/s &nbsp;&nbsp; (b) 12.70 m/s",
        },
        {
            "marks": 4,
            "q": "<p>A number <i>x</i> is written as 6.3</p>"
                 "<p class='part'>(a) Write the error interval if 6.3 is <b>rounded</b> to 1 decimal place.</p>"
                 "<p class='part'>(b) Write the error interval if 6.3 is <b>truncated</b> to 1 decimal place.</p>"
                 "<p class='part'>(c) Explain the difference between the two intervals.</p>",
            "steps": [
                "<b>(a)</b> Rounding goes half a unit either side: 6.25 &le; <i>x</i> &lt; 6.35",
                "<b>(b)</b> Truncating simply chops off the remaining digits, so anything from 6.3 up to "
                "(but not including) 6.4 truncates to 6.3",
                "The interval is 6.3 &le; <i>x</i> &lt; 6.4",
                "<b>(c)</b> A rounded value sits in the middle of its interval, while a truncated value sits at "
                "the bottom of its interval &mdash; truncating never gives a value below the stated one.",
            ],
            "answer": "(a) 6.25 &le; <i>x</i> &lt; 6.35 &nbsp;&nbsp; (b) 6.3 &le; <i>x</i> &lt; 6.4 &nbsp;&nbsp; "
                      "(c) rounding is centred on 6.3; truncating starts at 6.3",
        },
        {
            "marks": 4,
            "q": "<p>A metal block has mass 250 g to the nearest 10 g and volume 40 cm<sup>3</sup> to the "
                 "nearest cm<sup>3</sup>.</p>"
                 "<p>Work out the upper bound of the density, in g/cm<sup>3</sup>, to 2 decimal places.</p>",
            "steps": [
                "Density = " + frac("mass", "volume"),
                "Mass bounds: 245 g to 255 g. Volume bounds: 39.5 cm<sup>3</sup> to 40.5 cm<sup>3</sup>.",
                "For the largest density, take the largest mass and the smallest volume.",
                "Upper bound = " + frac("255", "39.5") + " = 6.4556&hellip;",
            ],
            "answer": "6.46 g/cm<sup>3</sup> (2 d.p.)",
        },
        {
            "marks": 4,
            "q": "<p>a = 6.4 and b = 2.7, each correct to 1 decimal place.</p>"
                 "<p class='part'>(a) Work out the upper and lower bounds of " + frac("a", "b") + "</p>"
                 "<p class='part'>(b) Hence write down the value of " + frac("a", "b")
                 + " to a suitable degree of accuracy, explaining your answer.</p>",
            "steps": [
                "Bounds for a: 6.35 to 6.45. Bounds for b: 2.65 to 2.75.",
                "<b>(a)</b> Upper bound = " + frac("6.45", "2.65") + " = 2.4339&hellip;",
                "Lower bound = " + frac("6.35", "2.75") + " = 2.3090&hellip;",
                "<b>(b)</b> Compare the two bounds digit by digit: 2.43&hellip; and 2.30&hellip;",
                "They agree on the leading 2 but disagree in the first decimal place.",
                "So only the first significant figure is certain, and " + frac("a", "b") + " = 2 to 1 s.f.",
            ],
            "answer": "(a) upper 2.4339&hellip;, lower 2.3090&hellip; &nbsp;&nbsp; (b) 2 (1 s.f.), because the bounds "
                      "only agree to 1 significant figure",
        },
        {
            "marks": 5,
            "q": "<p>A car travels 96.5 km, correct to the nearest 0.1 km, in 1.25 hours, correct to the "
                 "nearest 0.01 hours.</p>"
                 "<p class='part'>(a) Work out the upper bound of the average speed, to 2 decimal places.</p>"
                 "<p class='part'>(b) Work out the lower bound of the average speed, to 2 decimal places.</p>"
                 "<p class='part'>(c) Write the average speed to a suitable degree of accuracy, giving a reason.</p>",
            "steps": [
                "Distance bounds: 96.45 km to 96.55 km. Time bounds: 1.245 h to 1.255 h.",
                "<b>(a)</b> Largest distance &divide; smallest time = " + frac("96.55", "1.245") + " = 77.5502&hellip; km/h",
                "So the upper bound is 77.55 km/h (2 d.p.).",
                "<b>(b)</b> Smallest distance &divide; largest time = " + frac("96.45", "1.255") + " = 76.8525&hellip; km/h",
                "So the lower bound is 76.85 km/h (2 d.p.).",
                "<b>(c)</b> Rounding both bounds to 2 significant figures gives 78 and 77, which still disagree; "
                "rounding to 1 significant figure gives 80 for both.",
                "So the speed can only safely be stated as 80 km/h (1 s.f.).",
            ],
            "answer": "(a) 77.55 km/h &nbsp;&nbsp; (b) 76.85 km/h &nbsp;&nbsp; (c) 80 km/h (1 s.f.) &mdash; "
                      "that is the most accurate value both bounds agree on",
        },
    ],
}

PAPERS = [FRACTIONS, PERCENTAGES, POWERS, ROUNDING]
