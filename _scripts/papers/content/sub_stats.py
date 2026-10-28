"""GCSE practice papers — major Probability and Statistics subtopics."""
from build import frac

TREE_DIAGRAMS = {
    "title": "Tree Diagrams and Combined Events",
    "folder": "gcse/probability",
    "slug": "tree-diagrams-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>A fair coin is flipped twice.</p><p>How many possible outcomes are there?</p>",
            "steps": [
                "Each flip has 2 outcomes, and the two flips are independent.",
                "2 &times; 2 = 4 (HH, HT, TH, TT)",
            ],
            "answer": "4",
        },
        {
            "marks": 2,
            "q": "<p>A fair coin is flipped and a fair four-sided dice is rolled.</p>"
                 "<p class='part'>(a) How many possible outcomes are there?</p>"
                 "<p class='part'>(b) Write down the probability of getting a head and a 4.</p>",
            "steps": [
                "<b>(a)</b> 2 outcomes for the coin &times; 4 for the dice = 8 outcomes.",
                "<b>(b)</b> Only one of the 8 equally likely outcomes is (head, 4).",
                "So the probability is " + frac("1", "8") + ".",
            ],
            "answer": "(a) 8 &nbsp;&nbsp; (b) " + frac("1", "8"),
        },
        {
            "marks": 2,
            "q": "<p>A and B are independent events with P(A) = 0.5 and P(B) = 0.2</p>"
                 "<p>Work out P(A and B).</p>",
            "steps": [
                "For independent events, multiply along the branches.",
                "0.5 &times; 0.2 = 0.1",
            ],
            "answer": "0.1",
        },
        {
            "marks": 2,
            "q": "<p>A fair coin is flipped twice.</p><p>Work out the probability of getting two heads.</p>",
            "steps": [
                "P(head) = " + frac("1", "2") + " each time, and the flips are independent.",
                frac("1", "2") + " &times; " + frac("1", "2") + " = " + frac("1", "4"),
            ],
            "answer": frac("1", "4"),
        },
        {
            "marks": 3,
            "q": "<p>A bag contains 3 red and 7 blue counters. A counter is taken, its colour recorded, "
                 "and it is <b>replaced</b>. A second counter is then taken.</p>"
                 "<p class='part'>(a) Work out the probability that both counters are red.</p>"
                 "<p class='part'>(b) Work out the probability that both counters are blue.</p>",
            "steps": [
                "Because the counter is replaced, P(red) = 0.3 and P(blue) = 0.7 on both draws.",
                "<b>(a)</b> 0.3 &times; 0.3 = 0.09",
                "<b>(b)</b> 0.7 &times; 0.7 = 0.49",
            ],
            "answer": "(a) 0.09 &nbsp;&nbsp; (b) 0.49",
        },
        {
            "marks": 3,
            "q": "<p>Using the same bag and method (3 red, 7 blue, with replacement, two draws),</p>"
                 "<p>work out the probability of getting at least one red counter.</p>",
            "steps": [
                "&lsquo;At least one red&rsquo; is the opposite of &lsquo;no reds at all&rsquo;.",
                "P(no reds) = P(both blue) = 0.7 &times; 0.7 = 0.49",
                "P(at least one red) = 1 &minus; 0.49",
                "= 0.51",
            ],
            "answer": "0.51",
        },
        {
            "marks": 3,
            "q": "<p>A spinner has probability 0.3 of landing on &lsquo;win&rsquo;. It is spun twice.</p>"
                 "<p>Work out the probability of winning exactly once.</p>",
            "steps": [
                "There are two ways: win then lose, or lose then win. Both count.",
                "Win then lose: 0.3 &times; 0.7 = 0.21",
                "Lose then win: 0.7 &times; 0.3 = 0.21",
                "Add the two routes: 0.21 + 0.21 = 0.42",
            ],
            "answer": "0.42",
        },
        {
            "marks": 3,
            "q": "<p>Two fair six-sided dice are rolled.</p>"
                 "<p class='part'>(a) Work out the probability that both scores are even.</p>"
                 "<p class='part'>(b) Work out the probability of getting at least one 6.</p>",
            "steps": [
                "<b>(a)</b> P(even) = " + frac("3", "6") + " = " + frac("1", "2") + " for each dice.",
                frac("1", "2") + " &times; " + frac("1", "2") + " = " + frac("1", "4"),
                "<b>(b)</b> Use the complement. P(not a 6) = " + frac("5", "6") + " each time.",
                "P(no 6s) = " + frac("5", "6") + " &times; " + frac("5", "6") + " = " + frac("25", "36"),
                "P(at least one 6) = 1 &minus; " + frac("25", "36") + " = " + frac("11", "36"),
            ],
            "answer": "(a) " + frac("1", "4") + " &nbsp;&nbsp; (b) " + frac("11", "36"),
        },
        {
            "marks": 4,
            "q": "<p>A bag contains 4 red and 6 blue counters. Two counters are taken at random "
                 "<b>without</b> replacement.</p>"
                 "<p class='part'>(a) Write down the probability that the first counter is red.</p>"
                 "<p class='part'>(b) Given that the first counter was red, write down the probability that "
                 "the second is red.</p>"
                 "<p class='part'>(c) Work out the probability that both counters are red.</p>",
            "steps": [
                "<b>(a)</b> There are 10 counters and 4 are red: " + frac("4", "10") + " = " + frac("2", "5"),
                "<b>(b)</b> One red counter has gone, so 3 reds remain out of 9 counters: " + frac("3", "9") + " = " + frac("1", "3"),
                "<b>(c)</b> Multiply along the branches: " + frac("4", "10") + " &times; " + frac("3", "9") + " = " + frac("12", "90"),
                "Simplify by dividing by 6: " + frac("2", "15"),
            ],
            "answer": "(a) " + frac("2", "5") + " &nbsp;&nbsp; (b) " + frac("1", "3") + " &nbsp;&nbsp; (c) " + frac("2", "15"),
        },
        {
            "marks": 4,
            "q": "<p>Using the same bag (4 red, 6 blue, two counters taken without replacement),</p>"
                 "<p>work out the probability that the two counters are of different colours.</p>",
            "steps": [
                "There are two successful routes: red then blue, or blue then red.",
                "Red then blue: " + frac("4", "10") + " &times; " + frac("6", "9") + " = " + frac("24", "90"),
                "Blue then red: " + frac("6", "10") + " &times; " + frac("4", "9") + " = " + frac("24", "90"),
                "Add them: " + frac("24", "90") + " + " + frac("24", "90") + " = " + frac("48", "90"),
                "Divide top and bottom by 6: " + frac("8", "15"),
            ],
            "answer": frac("8", "15") + " (about 0.533)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>A and B are independent with P(A) = 0.6 and P(B) = 0.25</p>"
                 "<p>Work out P(A and not B).</p>",
            "steps": [
                "P(not B) = 1 &minus; 0.25 = 0.75",
                "0.6 &times; 0.75 = 0.45",
            ],
            "answer": "0.45",
        },
        {
            "marks": 2,
            "q": "<p>A biased coin has P(head) = 0.7. It is flipped three times.</p>"
                 "<p>Work out the probability of getting three heads.</p>",
            "steps": [
                "The flips are independent, so multiply.",
                "0.7<sup>3</sup> = 0.343",
            ],
            "answer": "0.343",
        },
        {
            "marks": 3,
            "q": "<p>The same biased coin (P(head) = 0.7) is flipped three times.</p>"
                 "<p>Work out the probability of getting at least one head.</p>",
            "steps": [
                "Use the complement: the opposite of &lsquo;at least one head&rsquo; is &lsquo;no heads at all&rsquo;.",
                "P(tail) = 0.3, so P(three tails) = 0.3<sup>3</sup> = 0.027",
                "P(at least one head) = 1 &minus; 0.027 = 0.973",
            ],
            "answer": "0.973",
        },
        {
            "marks": 3,
            "q": "<p>A bag contains 5 red and 4 green counters. Two are taken without replacement.</p>"
                 "<p>Work out the probability that they are the same colour.</p>",
            "steps": [
                "Both red: " + frac("5", "9") + " &times; " + frac("4", "8") + " = " + frac("20", "72"),
                "Both green: " + frac("4", "9") + " &times; " + frac("3", "8") + " = " + frac("12", "72"),
                "Add: " + frac("20", "72") + " + " + frac("12", "72") + " = " + frac("32", "72"),
                "Divide by 8: " + frac("4", "9"),
            ],
            "answer": frac("4", "9") + " (about 0.444)",
        },
        {
            "marks": 4,
            "q": "<p>A factory uses two machines. Machine A makes 70% of the items and 3% of them are faulty. "
                 "Machine B makes the other 30% and 8% of those are faulty.</p>"
                 "<p>Work out the probability that a randomly chosen item is faulty.</p>",
            "steps": [
                "Draw a tree: first branch A (0.7) or B (0.3), second branch faulty or not.",
                "A and faulty: 0.7 &times; 0.03 = 0.021",
                "B and faulty: 0.3 &times; 0.08 = 0.024",
                "These are the only two ways to get a faulty item, so add them.",
                "0.021 + 0.024 = 0.045",
            ],
            "answer": "0.045",
        },
        {
            "marks": 4,
            "q": "<p>Using the same factory information, an item is found to be faulty.</p>"
                 "<p>Work out the probability that it was made by machine B.</p>",
            "steps": [
                "This is conditional: restrict attention to the faulty items only.",
                "P(faulty) = 0.045 from before.",
                "P(B and faulty) = 0.024",
                "P(B | faulty) = " + frac("0.024", "0.045"),
                "= " + frac("24", "45") + " = " + frac("8", "15") + " &asymp; 0.533",
            ],
            "answer": frac("8", "15") + " (about 0.533)",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains 6 white and 4 black counters. Three are taken at random without "
                 "replacement.</p>"
                 "<p>Work out the probability that all three are white.</p>",
            "steps": [
                "Each time a white counter is removed, both the number of whites and the total go down by 1.",
                "First: " + frac("6", "10") + " &nbsp;&middot;&nbsp; second: " + frac("5", "9") + " &nbsp;&middot;&nbsp; third: " + frac("4", "8"),
                "Multiply: " + frac("6", "10") + " &times; " + frac("5", "9") + " &times; " + frac("4", "8") + " = " + frac("120", "720"),
                "= " + frac("1", "6"),
            ],
            "answer": frac("1", "6") + " (about 0.167)",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains n blue counters and 4 red counters.</p>"
                 "<p>Two counters are taken at random without replacement. The probability that both are "
                 "blue is " + frac("1", "3") + "</p>"
                 "<p class='part'>(a) Show that n<sup>2</sup> &minus; 5n &minus; 6 = 0</p>"
                 "<p class='part'>(b) Work out the number of blue counters.</p>",
            "steps": [
                "<b>(a)</b> There are n + 4 counters, so P(first blue) = " + frac("n", "n + 4"),
                "P(second blue) = " + frac("n &minus; 1", "n + 3"),
                frac("n(n &minus; 1)", "(n + 4)(n + 3)") + " = " + frac("1", "3"),
                "Cross-multiply: 3n(n &minus; 1) = (n + 4)(n + 3), so 3n<sup>2</sup> &minus; 3n = n<sup>2</sup> + 7n + 12",
                "2n<sup>2</sup> &minus; 10n &minus; 12 = 0, and dividing by 2 gives n<sup>2</sup> &minus; 5n &minus; 6 = 0",
                "<b>(b)</b> (n &minus; 6)(n + 1) = 0, so n = 6 or n = &minus;1; a count must be positive, so n = 6",
                "Check: " + frac("6", "10") + " &times; " + frac("5", "9") + " = " + frac("30", "90") + " = " + frac("1", "3") + " &#10003;",
            ],
            "answer": "(b) 6 blue counters",
        },
        {
            "marks": 4,
            "q": "<p>A spinner has probability 0.4 of landing on red. It is spun three times.</p>"
                 "<p>Work out the probability of getting exactly two reds.</p>",
            "steps": [
                "Exactly two reds can happen in three different orders: RRN, RNR and NRR.",
                "Each of those has probability 0.4 &times; 0.4 &times; 0.6 = 0.096",
                "There are 3 such orders, so multiply.",
                "3 &times; 0.096 = 0.288",
            ],
            "answer": "0.288",
        },
        {
            "marks": 5,
            "q": "<p>Bag A contains 3 red and 5 blue counters. Bag B contains 4 red and 2 blue counters.</p>"
                 "<p>One counter is taken at random from bag A and placed into bag B.</p>"
                 "<p>A counter is then taken at random from bag B.</p>"
                 "<p>Work out the probability that the counter taken from bag B is red.</p>",
            "steps": [
                "Bag B always ends up with 7 counters, but how many are red depends on the first counter.",
                "<b>Case 1 &mdash; red moved (probability " + frac("3", "8") + "):</b> bag B becomes 5 red and 2 blue.",
                "P(red from B) = " + frac("5", "7") + ", so this route gives " + frac("3", "8") + " &times; " + frac("5", "7") + " = " + frac("15", "56"),
                "<b>Case 2 &mdash; blue moved (probability " + frac("5", "8") + "):</b> bag B becomes 4 red and 3 blue.",
                "P(red from B) = " + frac("4", "7") + ", so this route gives " + frac("5", "8") + " &times; " + frac("4", "7") + " = " + frac("20", "56"),
                "Add the two routes: " + frac("15", "56") + " + " + frac("20", "56") + " = " + frac("35", "56") + " = " + frac("5", "8"),
            ],
            "answer": frac("5", "8") + " (0.625)",
        },
    ],
}

CONDITIONAL = {
    "title": "Conditional Probability",
    "folder": "gcse/probability",
    "slug": "conditional-probability-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>A bag contains 5 red and 3 blue counters. One red counter is taken out and not "
                 "replaced.</p>"
                 "<p>How many counters are left in the bag?</p>",
            "steps": [
                "There were 5 + 3 = 8 counters.",
                "8 &minus; 1 = 7",
            ],
            "answer": "7",
        },
        {
            "marks": 2,
            "q": "<p>A bag contains 5 red and 3 blue counters. One red counter is taken out and not replaced.</p>"
                 "<p>Work out the probability that the next counter taken is also red.</p>",
            "steps": [
                "After removing a red, there are 4 reds left.",
                "The total is now 7 counters.",
            ],
            "answer": frac("4", "7"),
        },
        {
            "marks": 2,
            "q": "<p>Ten cards numbered 1 to 10 are shuffled. One card is taken and <b>not</b> replaced; "
                 "it is the 3.</p>"
                 "<p>Work out the probability that the next card taken is even.</p>",
            "steps": [
                "The even cards are 2, 4, 6, 8 and 10, so 5 of them &mdash; and the 3 was odd, so none has gone.",
                "There are now 9 cards left.",
            ],
            "answer": frac("5", "9"),
        },
        {
            "marks": 2,
            "q": "<p>The table shows information about 40 students.</p>"
                 "<table class='d'><tr><th></th><th>Likes science</th><th>Does not like science</th><th>Total</th></tr>"
                 "<tr><th>Likes maths</th><td>15</td><td>9</td><td>24</td></tr>"
                 "<tr><th>Does not like maths</th><td>6</td><td>10</td><td>16</td></tr></table>"
                 "<p>A student who likes maths is chosen at random. Work out the probability that they "
                 "also like science.</p>",
            "steps": [
                "The condition restricts us to the 24 students who like maths.",
                "Of those, 15 also like science.",
                frac("15", "24") + " = " + frac("5", "8"),
            ],
            "answer": frac("5", "8") + " (0.625)",
        },
        {
            "marks": 3,
            "q": "<p>A bag contains 4 green and 5 yellow counters. Two are taken without replacement.</p>"
                 "<p>Work out the probability that both are green.</p>",
            "steps": [
                "P(first green) = " + frac("4", "9"),
                "After a green is removed there are 3 greens out of 8 counters: " + frac("3", "8"),
                "Multiply: " + frac("4", "9") + " &times; " + frac("3", "8") + " = " + frac("12", "72"),
                "= " + frac("1", "6"),
            ],
            "answer": frac("1", "6"),
        },
        {
            "marks": 3,
            "q": "<p>A bag contains 4 green and 5 yellow counters. Two are taken without replacement.</p>"
                 "<p>The first counter is green. Work out the probability that the second is yellow.</p>",
            "steps": [
                "Removing a green counter does not change the number of yellows, which is still 5.",
                "But the total falls from 9 to 8.",
                "So the probability is " + frac("5", "8") + ".",
            ],
            "answer": frac("5", "8") + " (0.625)",
        },
        {
            "marks": 3,
            "q": "<p>In a group of 50 people, 30 are male. 12 of the males and 8 of the females wear glasses.</p>"
                 "<p class='part'>(a) A male is chosen at random. Work out the probability that he wears glasses.</p>"
                 "<p class='part'>(b) A female is chosen at random. Work out the probability that she wears "
                 "glasses.</p>",
            "steps": [
                "<b>(a)</b> Restrict to the 30 males, of whom 12 wear glasses.",
                frac("12", "30") + " = " + frac("2", "5"),
                "<b>(b)</b> There are 50 &minus; 30 = 20 females, of whom 8 wear glasses.",
                frac("8", "20") + " = " + frac("2", "5"),
                "The two answers happen to be equal here, which suggests glasses-wearing is not linked to sex "
                "in this group.",
            ],
            "answer": "(a) " + frac("2", "5") + " &nbsp;&nbsp; (b) " + frac("2", "5"),
        },
        {
            "marks": 3,
            "q": "<p>Two cards are dealt from a shuffled pack of 52 playing cards, without replacement.</p>"
                 "<p>Work out the probability that both are hearts. (There are 13 hearts in a pack.)</p>",
            "steps": [
                "P(first heart) = " + frac("13", "52") + " = " + frac("1", "4"),
                "One heart has gone, so 12 hearts remain out of 51 cards: " + frac("12", "51") + " = " + frac("4", "17"),
                "Multiply: " + frac("1", "4") + " &times; " + frac("4", "17"),
                "= " + frac("1", "17"),
            ],
            "answer": frac("1", "17") + " (about 0.0588)",
        },
        {
            "marks": 4,
            "q": "<p>80 students were asked how they travel to school. The table is incomplete.</p>"
                 "<table class='d'><tr><th></th><th>Bus</th><th>Walk</th><th>Total</th></tr>"
                 "<tr><th>Year 10</th><td>27</td><td>&nbsp;</td><td>45</td></tr>"
                 "<tr><th>Year 11</th><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"
                 "<tr><th>Total</th><td>50</td><td>&nbsp;</td><td>80</td></tr></table>"
                 "<p>A student who takes the bus is chosen at random. Work out the probability that "
                 "the student is in Year 11.</p>",
            "steps": [
                "Complete the table. Year 10 who walk: 45 &minus; 27 = 18",
                "Year 11 total: 80 &minus; 45 = 35",
                "Year 11 on the bus: 50 &minus; 27 = 23 (and so 35 &minus; 23 = 12 walk).",
                "Check the walk column: 18 + 12 = 30, and 50 + 30 = 80 &#10003;",
                "The condition restricts us to the 50 bus users, of whom 23 are in Year 11.",
            ],
            "answer": frac("23", "50") + " (0.46)",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains 3 red, 4 blue and 5 green counters. Two counters are taken at random "
                 "without replacement.</p>"
                 "<p class='part'>(a) Work out the probability that both are red.</p>"
                 "<p class='part'>(b) The first counter is blue. Work out the probability that the second "
                 "is green.</p>",
            "steps": [
                "There are 3 + 4 + 5 = 12 counters altogether.",
                "<b>(a)</b> " + frac("3", "12") + " &times; " + frac("2", "11") + " = " + frac("6", "132") + " = " + frac("1", "22"),
                "<b>(b)</b> Removing a blue counter leaves all 5 greens in place.",
                "The total is now 11, so the probability is " + frac("5", "11") + ".",
            ],
            "answer": "(a) " + frac("1", "22") + " &nbsp;&nbsp; (b) " + frac("5", "11"),
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>P(A) = 0.4 and P(A and B) = 0.1</p><p>Work out P(B | A).</p>",
            "steps": [
                "P(B | A) = " + frac("P(A and B)", "P(A)"),
                "= " + frac("0.1", "0.4") + " = 0.25",
            ],
            "answer": "0.25",
        },
        {
            "marks": 2,
            "q": "<p>A bag contains 7 red and 5 blue counters. Two are taken without replacement, and "
                 "the first is red.</p>"
                 "<p>Write down the probability that the second is also red.</p>",
            "steps": [
                "One red counter has been removed, so 6 reds remain.",
                "The total has also dropped by one, from 12 counters to 11.",
            ],
            "answer": frac("6", "11"),
        },
        {
            "marks": 3,
            "q": "<p>A bag contains 6 red and 6 blue counters. Two are taken without replacement.</p>"
                 "<p>Work out the probability that both are red.</p>",
            "steps": [
                "P(first red) = " + frac("6", "12") + " = " + frac("1", "2"),
                "P(second red) = " + frac("5", "11"),
                frac("6", "12") + " &times; " + frac("5", "11") + " = " + frac("30", "132"),
                "= " + frac("5", "22"),
            ],
            "answer": frac("5", "22") + " (about 0.227)",
        },
        {
            "marks": 3,
            "q": "<p>Using the same bag (6 red, 6 blue, two taken without replacement),</p>"
                 "<p>work out the probability that exactly one counter is red.</p>",
            "steps": [
                "Red then blue: " + frac("6", "12") + " &times; " + frac("6", "11") + " = " + frac("36", "132"),
                "Blue then red: " + frac("6", "12") + " &times; " + frac("6", "11") + " = " + frac("36", "132"),
                "Add: " + frac("72", "132"),
                "Divide top and bottom by 12: " + frac("6", "11"),
            ],
            "answer": frac("6", "11") + " (about 0.545)",
        },
        {
            "marks": 4,
            "q": "<p>In a survey of 60 people, 35 own a dog, 28 own a cat and 12 own both.</p>"
                 "<p class='part'>(a) A cat owner is chosen at random. Work out the probability they also "
                 "own a dog.</p>"
                 "<p class='part'>(b) A dog owner is chosen at random. Work out the probability they also "
                 "own a cat.</p>"
                 "<p class='part'>(c) Work out the probability that a randomly chosen person owns neither.</p>",
            "steps": [
                "Fill in a Venn diagram: both = 12, dog only = 35 &minus; 12 = 23, cat only = 28 &minus; 12 = 16",
                "Neither = 60 &minus; (23 + 12 + 16) = 60 &minus; 51 = 9",
                "<b>(a)</b> Restrict to the 28 cat owners: " + frac("12", "28") + " = " + frac("3", "7"),
                "<b>(b)</b> Restrict to the 35 dog owners: " + frac("12", "35"),
                "<b>(c)</b> " + frac("9", "60") + " = " + frac("3", "20") + " = 0.15",
            ],
            "answer": "(a) " + frac("3", "7") + " &nbsp;&nbsp; (b) " + frac("12", "35") + " &nbsp;&nbsp; (c) 0.15",
        },
        {
            "marks": 4,
            "q": "<p>5% of a population has a certain condition.</p>"
                 "<p>A test gives a positive result for 90% of people who have the condition, and also gives "
                 "a positive result for 8% of people who do not have it.</p>"
                 "<p class='part'>(a) Work out the probability that a randomly chosen person tests positive.</p>"
                 "<p class='part'>(b) A person tests positive. Work out the probability that they actually "
                 "have the condition, to 3 significant figures.</p>",
            "steps": [
                "<b>(a)</b> Has condition and positive: 0.05 &times; 0.9 = 0.045",
                "No condition and positive: 0.95 &times; 0.08 = 0.076",
                "P(positive) = 0.045 + 0.076 = 0.121",
                "<b>(b)</b> Restrict to the people who test positive.",
                "P(condition | positive) = " + frac("0.045", "0.121") + " = 0.37190&hellip;",
                "So only about 37% of positive results are genuine, because the condition is rare.",
            ],
            "answer": "(a) 0.121 &nbsp;&nbsp; (b) 0.372 (3 s.f.)",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains 5 red and 3 blue counters. Three are taken without replacement.</p>"
                 "<p>Work out the probability that all three are red.</p>",
            "steps": [
                "P(first red) = " + frac("5", "8"),
                "P(second red) = " + frac("4", "7") + " and P(third red) = " + frac("3", "6"),
                "Multiply: " + frac("5", "8") + " &times; " + frac("4", "7") + " &times; " + frac("3", "6"),
                "= " + frac("60", "336"),
                "Divide top and bottom by 12: " + frac("5", "28"),
            ],
            "answer": frac("5", "28") + " (about 0.179)",
        },
        {
            "marks": 4,
            "q": "<p>P(A) = 0.6, P(B | A) = 0.3 and P(B | not A) = 0.5</p>"
                 "<p class='part'>(a) Work out P(B).</p>"
                 "<p class='part'>(b) Work out P(A | B).</p>",
            "steps": [
                "<b>(a)</b> A and B: 0.6 &times; 0.3 = 0.18",
                "Not A and B: 0.4 &times; 0.5 = 0.2",
                "P(B) = 0.18 + 0.2 = 0.38",
                "<b>(b)</b> P(A | B) = " + frac("P(A and B)", "P(B)") + " = " + frac("0.18", "0.38"),
                "= " + frac("18", "38") + " = " + frac("9", "19") + " &asymp; 0.474",
            ],
            "answer": "(a) 0.38 &nbsp;&nbsp; (b) " + frac("9", "19") + " (about 0.474)",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains 5 white counters and n black counters.</p>"
                 "<p>Two counters are taken without replacement. The probability that both are white "
                 "is " + frac("5", "14") + "</p>"
                 "<p>Work out the value of n.</p>",
            "steps": [
                "There are n + 5 counters, so P(both white) = " + frac("5", "n + 5") + " &times; " + frac("4", "n + 4"),
                frac("20", "(n + 5)(n + 4)") + " = " + frac("5", "14"),
                "Cross-multiply: 20 &times; 14 = 5(n + 5)(n + 4), so 280 = 5(n<sup>2</sup> + 9n + 20)",
                "Divide by 5: 56 = n<sup>2</sup> + 9n + 20, so n<sup>2</sup> + 9n &minus; 36 = 0",
                "(n + 12)(n &minus; 3) = 0, so n = 3 (rejecting the negative solution).",
                "Check: " + frac("5", "8") + " &times; " + frac("4", "7") + " = " + frac("20", "56") + " = " + frac("5", "14") + " &#10003;",
            ],
            "answer": "n = 3",
        },
        {
            "marks": 5,
            "q": "<p>A box contains 4 milk chocolates and 6 dark chocolates. Two are taken at random "
                 "without replacement.</p>"
                 "<p class='part'>(a) Work out the probability that both are milk.</p>"
                 "<p class='part'>(b) Work out the probability that the second chocolate is dark.</p>"
                 "<p class='part'>(c) Given that the second chocolate is dark, work out the probability that "
                 "the first was milk.</p>",
            "steps": [
                "<b>(a)</b> " + frac("4", "10") + " &times; " + frac("3", "9") + " = " + frac("12", "90") + " = " + frac("2", "15"),
                "<b>(b)</b> There are two routes to a dark second chocolate.",
                "Milk then dark: " + frac("4", "10") + " &times; " + frac("6", "9") + " = " + frac("24", "90"),
                "Dark then dark: " + frac("6", "10") + " &times; " + frac("5", "9") + " = " + frac("30", "90"),
                "P(second dark) = " + frac("54", "90") + " = " + frac("3", "5") + " (the same as P(first dark), which is no accident).",
                "<b>(c)</b> Restrict to the cases where the second is dark.",
                "P(first milk | second dark) = " + frac("24", "90") + " &divide; " + frac("54", "90")
                + " = " + frac("24", "54") + " = " + frac("4", "9"),
            ],
            "answer": "(a) " + frac("2", "15") + " &nbsp;&nbsp; (b) " + frac("3", "5") + " &nbsp;&nbsp; (c) " + frac("4", "9"),
        },
    ],
}

AVERAGES = {
    "title": "Averages and Spread",
    "folder": "gcse/statistics",
    "slug": "averages-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write down the mode of these numbers.</p>"
                 "<p><b>5&nbsp;&nbsp; 8&nbsp;&nbsp; 5&nbsp;&nbsp; 2&nbsp;&nbsp; 9</b></p>",
            "steps": [
                "The mode is the most common value.",
                "5 appears twice; every other value appears once.",
            ],
            "answer": "5",
        },
        {
            "marks": 2,
            "q": "<p>Work out the mean of</p><p><b>3&nbsp;&nbsp; 9&nbsp;&nbsp; 4&nbsp;&nbsp; 8&nbsp;&nbsp; 6</b></p>",
            "steps": [
                "Total = 3 + 9 + 4 + 8 + 6 = 30",
                "There are 5 values, so the mean is 30 &divide; 5 = 6",
            ],
            "answer": "6",
        },
        {
            "marks": 2,
            "q": "<p>Here are six numbers.</p>"
                 "<p><b>14&nbsp;&nbsp; 7&nbsp;&nbsp; 11&nbsp;&nbsp; 3&nbsp;&nbsp; 9&nbsp;&nbsp; 20</b></p>"
                 "<p class='part'>(a) Work out the median.</p>"
                 "<p class='part'>(b) Work out the range.</p>",
            "steps": [
                "Order them first: 3, 7, 9, 11, 14, 20",
                "<b>(a)</b> With 6 values there is no single middle one, so average the 3rd and 4th.",
                "(9 + 11) &divide; 2 = 10",
                "<b>(b)</b> Range = 20 &minus; 3 = 17",
            ],
            "answer": "(a) 10 &nbsp;&nbsp; (b) 17",
        },
        {
            "marks": 2,
            "q": "<p>A shoe shop wants to know which size to stock the most of.</p>"
                 "<p>Which average should the manager use, and why?</p>",
            "steps": [
                "The manager wants the size that sells most often.",
                "That is the mode &mdash; the most frequently occurring value.",
                "A mean shoe size (such as 7.4) would not even be a real size to stock.",
            ],
            "answer": "the mode &mdash; it gives the most commonly bought size",
        },
        {
            "marks": 3,
            "q": "<p>The table shows the number of goals scored in 20 matches.</p>"
                 "<table class='d'><tr><th>Goals</th><th>0</th><th>1</th><th>2</th><th>3</th></tr>"
                 "<tr><th>Frequency</th><td>5</td><td>8</td><td>4</td><td>3</td></tr></table>"
                 "<p>Work out the mean number of goals per match.</p>",
            "steps": [
                "Multiply each number of goals by its frequency.",
                "0 &times; 5 = 0, &nbsp; 1 &times; 8 = 8, &nbsp; 2 &times; 4 = 8, &nbsp; 3 &times; 3 = 9",
                "Total goals = 0 + 8 + 8 + 9 = 25",
                "Total matches = 5 + 8 + 4 + 3 = 20",
                "Mean = " + frac("25", "20") + " = 1.25",
            ],
            "answer": "1.25 goals per match",
        },
        {
            "marks": 3,
            "q": "<p>The mean of four numbers is 12.</p>"
                 "<p>Three of the numbers are 8, 15 and 11.</p>"
                 "<p>Work out the fourth number.</p>",
            "steps": [
                "If the mean of 4 numbers is 12, the total must be 4 &times; 12 = 48",
                "The three known numbers add to 8 + 15 + 11 = 34",
                "Fourth number = 48 &minus; 34 = 14",
            ],
            "answer": "14",
        },
        {
            "marks": 3,
            "q": "<p>Here is a set of data.</p>"
                 "<p><b>5&nbsp;&nbsp; 6&nbsp;&nbsp; 7&nbsp;&nbsp; 8&nbsp;&nbsp; 44</b></p>"
                 "<p class='part'>(a) Work out the mean.</p>"
                 "<p class='part'>(b) Work out the median.</p>"
                 "<p class='part'>(c) Which average better represents this data? Explain.</p>",
            "steps": [
                "<b>(a)</b> Total = 5 + 6 + 7 + 8 + 44 = 70, so the mean is 70 &divide; 5 = 14",
                "<b>(b)</b> The data is already in order, so the median is the 3rd value: 7",
                "<b>(c)</b> The mean of 14 is larger than four of the five values, because the outlier 44 pulls "
                "it up.",
                "The median of 7 is much more typical of the data, so it is the better average here.",
            ],
            "answer": "(a) 14 &nbsp;&nbsp; (b) 7 &nbsp;&nbsp; (c) the median, because 44 is an outlier that "
                      "distorts the mean",
        },
        {
            "marks": 3,
            "q": "<p>Here are eight numbers in order.</p>"
                 "<p><b>3&nbsp;&nbsp; 5&nbsp;&nbsp; 7&nbsp;&nbsp; 8&nbsp;&nbsp; 11&nbsp;&nbsp; 13&nbsp;&nbsp; "
                 "16&nbsp;&nbsp; 20</b></p>"
                 "<p class='part'>(a) Work out the lower and upper quartiles.</p>"
                 "<p class='part'>(b) Work out the interquartile range.</p>",
            "steps": [
                "The median splits the data into two halves of four values each: (3, 5, 7, 8) and (11, 13, 16, 20).",
                "<b>(a)</b> The lower quartile is the median of the first half: (5 + 7) &divide; 2 = 6",
                "The upper quartile is the median of the second half: (13 + 16) &divide; 2 = 14.5",
                "<b>(b)</b> IQR = 14.5 &minus; 6 = 8.5",
            ],
            "answer": "(a) LQ 6, UQ 14.5 &nbsp;&nbsp; (b) 8.5",
        },
        {
            "marks": 4,
            "q": "<p>The table shows the times, t minutes, taken by 40 people to complete a task.</p>"
                 "<table class='d'><tr><th>Time (t min)</th><th>0 &lt; t &le; 10</th><th>10 &lt; t &le; 20</th>"
                 "<th>20 &lt; t &le; 30</th><th>30 &lt; t &le; 40</th></tr>"
                 "<tr><th>Frequency</th><td>6</td><td>14</td><td>12</td><td>8</td></tr></table>"
                 "<p>Work out an estimate for the mean time.</p>",
            "steps": [
                "Use the midpoint of each class: 5, 15, 25 and 35.",
                "Midpoint &times; frequency: 5 &times; 6 = 30, &nbsp; 15 &times; 14 = 210",
                "25 &times; 12 = 300, &nbsp; 35 &times; 8 = 280",
                "Total = 30 + 210 + 300 + 280 = 820",
                "Mean = " + frac("820", "40") + " = 20.5 minutes",
            ],
            "answer": "20.5 minutes",
        },
        {
            "marks": 4,
            "q": "<p>Team A scored these goals in 8 matches: 0, 1, 1, 2, 3, 4, 4, 5</p>"
                 "<p>Team B scored these goals in 8 matches: 1, 2, 2, 2, 3, 3, 3, 4</p>"
                 "<p class='part'>(a) Work out the mean for each team.</p>"
                 "<p class='part'>(b) Work out the range for each team.</p>"
                 "<p class='part'>(c) Compare the two teams.</p>",
            "steps": [
                "<b>(a)</b> Team A total = 0 + 1 + 1 + 2 + 3 + 4 + 4 + 5 = 20, so the mean is 20 &divide; 8 = 2.5",
                "Team B total = 1 + 2 + 2 + 2 + 3 + 3 + 3 + 4 = 20, so the mean is also 2.5",
                "<b>(b)</b> Team A range = 5 &minus; 0 = 5 &nbsp;&middot;&nbsp; Team B range = 4 &minus; 1 = 3",
                "<b>(c)</b> The two teams score the same number of goals on average.",
                "Team B has the smaller range, so its scoring is more consistent from match to match.",
            ],
            "answer": "(a) both 2.5 &nbsp;&nbsp; (b) A: 5, B: 3 &nbsp;&nbsp; (c) same mean, but team B is more "
                      "consistent",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>The mean of 10 numbers is 18. Another number, 29, is added to the set.</p>"
                 "<p>Work out the new mean.</p>",
            "steps": [
                "Total of the 10 numbers = 10 &times; 18 = 180",
                "New total = 180 + 29 = 209 over 11 numbers.",
                "209 &divide; 11 = 19",
            ],
            "answer": "19",
        },
        {
            "marks": 2,
            "q": "<p>The mean of five numbers is 14. Four of them are 10, 12, 15 and 18.</p>"
                 "<p>Work out the fifth number.</p>",
            "steps": [
                "Total = 5 &times; 14 = 70",
                "The four known numbers add to 10 + 12 + 15 + 18 = 55",
                "Fifth number = 70 &minus; 55 = 15",
            ],
            "answer": "15",
        },
        {
            "marks": 3,
            "q": "<p>The mean mark of 8 boys is 65. The mean mark of 12 girls is 70.</p>"
                 "<p>Work out the mean mark of all 20 students.</p>",
            "steps": [
                "You cannot average 65 and 70, because the groups are different sizes.",
                "Boys total = 8 &times; 65 = 520",
                "Girls total = 12 &times; 70 = 840",
                "Overall total = 1360 over 20 students.",
                "Mean = " + frac("1360", "20") + " = 68",
            ],
            "answer": "68",
        },
        {
            "marks": 3,
            "q": "<p>The table shows the times, t minutes, of 40 phone calls.</p>"
                 "<table class='d'><tr><th>Time (t min)</th><th>0 &lt; t &le; 10</th><th>10 &lt; t &le; 20</th>"
                 "<th>20 &lt; t &le; 30</th><th>30 &lt; t &le; 40</th></tr>"
                 "<tr><th>Frequency</th><td>7</td><td>15</td><td>13</td><td>5</td></tr></table>"
                 "<p>Estimate the median time.</p>",
            "steps": [
                "With 40 values the median is the 20th value.",
                "Running totals: 7 up to 10 minutes, then 7 + 15 = 22 up to 20 minutes.",
                "So the 20th value lies in the class 10 &lt; t &le; 20, which holds 15 values.",
                "It is the 20 &minus; 7 = 13th value of those 15, so go " + frac("13", "15") + " of the way through a 10-minute class.",
                frac("13", "15") + " &times; 10 = 8.67, so the median is about 10 + 8.67 = 18.7 minutes",
            ],
            "answer": "about 18.7 minutes",
        },
        {
            "marks": 4,
            "q": "<p>Here are nine values in order.</p>"
                 "<p><b>12&nbsp; 15&nbsp; 18&nbsp; 21&nbsp; 22&nbsp; 25&nbsp; 28&nbsp; 30&nbsp; 35</b></p>"
                 "<p>Work out the five values needed to draw a box plot, and the interquartile range.</p>",
            "steps": [
                "Minimum = 12 and maximum = 35",
                "With 9 values the median is the 5th: 22",
                "The lower half (below the median) is 12, 15, 18, 21, so the lower quartile is (15 + 18) &divide; 2 = 16.5",
                "The upper half is 25, 28, 30, 35, so the upper quartile is (28 + 30) &divide; 2 = 29",
                "IQR = 29 &minus; 16.5 = 12.5",
            ],
            "answer": "min 12, LQ 16.5, median 22, UQ 29, max 35; IQR = 12.5",
        },
        {
            "marks": 4,
            "q": "<p>Box plots were drawn for two groups.</p>"
                 "<table class='d'><tr><th></th><th>Min</th><th>LQ</th><th>Median</th><th>UQ</th><th>Max</th></tr>"
                 "<tr><th>Group X</th><td>5</td><td>12</td><td>18</td><td>26</td><td>40</td></tr>"
                 "<tr><th>Group Y</th><td>8</td><td>14</td><td>17</td><td>21</td><td>30</td></tr></table>"
                 "<p class='part'>(a) Work out the interquartile range for each group.</p>"
                 "<p class='part'>(b) Make two comparisons between the groups.</p>",
            "steps": [
                "<b>(a)</b> Group X: 26 &minus; 12 = 14 &nbsp;&middot;&nbsp; Group Y: 21 &minus; 14 = 7",
                "<b>(b)</b> Averages: the medians are close (18 for X, 17 for Y), so typical values are similar, "
                "with X very slightly higher.",
                "Spread: Group Y has both a smaller interquartile range (7 against 14) and a smaller overall "
                "range (22 against 35), so its values are much more consistent.",
                "Always support a comparison with the numbers from the box plots.",
            ],
            "answer": "(a) X: 14, Y: 7 &nbsp;&nbsp; (b) similar medians (18 v 17), but Y is far more consistent "
                      "(IQR 7 v 14)",
        },
        {
            "marks": 4,
            "q": "<p>The table shows the number of pets owned by some families.</p>"
                 "<table class='d'><tr><th>Pets</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>"
                 "<tr><th>Frequency</th><td>3</td><td>5</td><td><i>x</i></td><td>4</td><td>2</td></tr></table>"
                 "<p>The mean number of pets is 1.8. Work out the value of <i>x</i>.</p>",
            "steps": [
                "Total number of families = 3 + 5 + <i>x</i> + 4 + 2 = 14 + <i>x</i>",
                "Total number of pets = 0 + 5 + 2<i>x</i> + 12 + 8 = 25 + 2<i>x</i>",
                "Mean = " + frac("25 + 2<i>x</i>", "14 + <i>x</i>") + " = 1.8",
                "Multiply out: 25 + 2<i>x</i> = 1.8(14 + <i>x</i>) = 25.2 + 1.8<i>x</i>",
                "0.2<i>x</i> = 0.2, so <i>x</i> = 1",
                "Check: 15 families, 27 pets, and 27 &divide; 15 = 1.8 &#10003;",
            ],
            "answer": "<i>x</i> = 1",
        },
        {
            "marks": 4,
            "q": "<p>The table shows data grouped into classes of unequal width.</p>"
                 "<table class='d'><tr><th>Value (x)</th><th>0 &lt; x &le; 5</th><th>5 &lt; x &le; 15</th>"
                 "<th>15 &lt; x &le; 35</th></tr>"
                 "<tr><th>Frequency</th><td>8</td><td>22</td><td>20</td></tr></table>"
                 "<p class='part'>(a) Work out an estimate for the mean.</p>"
                 "<p class='part'>(b) Work out which class is the modal class, explaining your reasoning.</p>",
            "steps": [
                "<b>(a)</b> Midpoints are 2.5, 10 and 25.",
                "2.5 &times; 8 = 20, &nbsp; 10 &times; 22 = 220, &nbsp; 25 &times; 20 = 500, giving a total of 740",
                "There are 8 + 22 + 20 = 50 values, so the mean is " + frac("740", "50") + " = 14.8",
                "<b>(b)</b> With unequal widths you must compare frequency densities, not raw frequencies.",
                "8 &divide; 5 = 1.6, &nbsp; 22 &divide; 10 = 2.2, &nbsp; 20 &divide; 20 = 1.0",
                "The highest density is 2.2, so the modal class is 5 &lt; x &le; 15.",
            ],
            "answer": "(a) 14.8 &nbsp;&nbsp; (b) 5 &lt; x &le; 15, because it has the greatest frequency density (2.2)",
        },
        {
            "marks": 4,
            "q": "<p>A set of 12 numbers has a mean of 25.</p>"
                 "<p>Two of the numbers, 18 and 22, are removed.</p>"
                 "<p>Work out the mean of the remaining numbers.</p>",
            "steps": [
                "Total of the 12 numbers = 12 &times; 25 = 300",
                "The two removed numbers add to 18 + 22 = 40",
                "New total = 300 &minus; 40 = 260",
                "There are now 10 numbers, so the mean is " + frac("260", "10") + " = 26",
                "The mean has gone up, which makes sense because both removed values were below 25.",
            ],
            "answer": "26",
        },
        {
            "marks": 5,
            "q": "<p>The table shows the number of siblings of 30 students.</p>"
                 "<table class='d'><tr><th>Siblings</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>"
                 "<tr><th>Frequency</th><td>6</td><td>10</td><td>8</td><td>4</td><td>2</td></tr></table>"
                 "<p class='part'>(a) Write down the mode.</p>"
                 "<p class='part'>(b) Work out the median.</p>"
                 "<p class='part'>(c) Work out the mean, to 2 decimal places.</p>"
                 "<p class='part'>(d) Write down the range.</p>",
            "steps": [
                "<b>(a)</b> The largest frequency is 10, which belongs to 1 sibling, so the mode is 1.",
                "<b>(b)</b> With 30 values the median is between the 15th and 16th values.",
                "Running totals: 6 students have 0 siblings, then 6 + 10 = 16 have 1 or fewer.",
                "Both the 15th and 16th values are 1, so the median is 1.",
                "<b>(c)</b> Total siblings = 0 &times; 6 + 1 &times; 10 + 2 &times; 8 + 3 &times; 4 + 4 &times; 2 = 0 + 10 + 16 + 12 + 8 = 46",
                "Mean = " + frac("46", "30") + " = 1.5333&hellip;, which is 1.53 to 2 decimal places.",
                "<b>(d)</b> Range = 4 &minus; 0 = 4",
            ],
            "answer": "(a) 1 &nbsp;&nbsp; (b) 1 &nbsp;&nbsp; (c) 1.53 &nbsp;&nbsp; (d) 4",
        },
    ],
}

HISTOGRAMS = {
    "title": "Histograms and Cumulative Frequency",
    "folder": "gcse/statistics",
    "slug": "histograms-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>In a histogram where every class has the same width, what does the height of each bar "
                 "represent?</p>",
            "steps": [
                "With equal class widths, the frequency density is just the frequency divided by the same "
                "number every time.",
                "So the heights are simply proportional to the frequencies.",
            ],
            "answer": "the frequency of that class",
        },
        {
            "marks": 2,
            "q": "<p>Complete the cumulative frequency column.</p>"
                 "<table class='d'><tr><th>Class</th><th>Frequency</th><th>Cumulative frequency</th></tr>"
                 "<tr><td>0 &lt; x &le; 10</td><td>5</td><td>&nbsp;</td></tr>"
                 "<tr><td>10 &lt; x &le; 20</td><td>9</td><td>&nbsp;</td></tr>"
                 "<tr><td>20 &lt; x &le; 30</td><td>12</td><td>&nbsp;</td></tr>"
                 "<tr><td>30 &lt; x &le; 40</td><td>4</td><td>&nbsp;</td></tr></table>",
            "steps": [
                "Cumulative frequency is a running total.",
                "5, then 5 + 9 = 14, then 14 + 12 = 26, then 26 + 4 = 30",
            ],
            "answer": "5, 14, 26, 30",
        },
        {
            "marks": 2,
            "q": "<p>Using the completed table above,</p>"
                 "<p class='part'>(a) how many values are 30 or less?</p>"
                 "<p class='part'>(b) how many values are more than 20?</p>",
            "steps": [
                "<b>(a)</b> Read the cumulative frequency for x &le; 30: 26",
                "<b>(b)</b> The total is 30, and 14 values are 20 or less.",
                "30 &minus; 14 = 16",
            ],
            "answer": "(a) 26 &nbsp;&nbsp; (b) 16",
        },
        {
            "marks": 2,
            "q": "<p>Using the same table (total frequency 30), write down the class interval that contains "
                 "the median.</p>",
            "steps": [
                "The median is between the 15th and 16th values.",
                "The cumulative frequencies are 5, 14, 26, 30, so the 15th and 16th values fall in the "
                "third class.",
            ],
            "answer": "20 &lt; x &le; 30",
        },
        {
            "marks": 3,
            "q": "<p>A frequency polygon is to be drawn for this table.</p>"
                 "<table class='d'><tr><th>Class</th><th>0&ndash;10</th><th>10&ndash;20</th><th>20&ndash;30</th>"
                 "<th>30&ndash;40</th></tr>"
                 "<tr><th>Frequency</th><td>8</td><td>14</td><td>11</td><td>5</td></tr></table>"
                 "<p>Write down the four points that should be plotted.</p>",
            "steps": [
                "A frequency polygon is plotted at the <b>midpoint</b> of each class.",
                "Midpoints: 5, 15, 25 and 35",
                "Pair each midpoint with its frequency.",
            ],
            "answer": "(5, 8), (15, 14), (25, 11) and (35, 5)",
        },
        {
            "marks": 3,
            "q": "<p>Work out the frequency density for each class.</p>"
                 "<table class='d'><tr><th>Class width</th><th>10</th><th>10</th><th>10</th><th>10</th></tr>"
                 "<tr><th>Frequency</th><td>12</td><td>25</td><td>18</td><td>5</td></tr></table>",
            "steps": [
                "Frequency density = " + frac("frequency", "class width"),
                "12 &divide; 10 = 1.2 and 25 &divide; 10 = 2.5",
                "18 &divide; 10 = 1.8 and 5 &divide; 10 = 0.5",
            ],
            "answer": "1.2, 2.5, 1.8 and 0.5",
        },
        {
            "marks": 3,
            "q": "<p>Class A is 0 &lt; x &le; 10 with frequency 20. Class B is 10 &lt; x &le; 30 with "
                 "frequency 30.</p>"
                 "<p class='part'>(a) Work out the frequency density of each class.</p>"
                 "<p class='part'>(b) Which class has the values packed more closely together? Explain.</p>",
            "steps": [
                "<b>(a)</b> Class A: 20 &divide; 10 = 2 &nbsp;&middot;&nbsp; Class B: 30 &divide; 20 = 1.5",
                "<b>(b)</b> Class B has more values, but they are spread over a much wider range.",
                "Class A has the higher frequency density, so its values are packed more closely.",
            ],
            "answer": "(a) A: 2, B: 1.5 &nbsp;&nbsp; (b) class A, because it has the greater frequency density",
        },
        {
            "marks": 3,
            "q": "<p>The table shows cumulative frequencies for the heights, h cm, of 50 plants.</p>"
                 "<table class='d'><tr><th>Height</th><th>h &le; 160</th><th>h &le; 170</th><th>h &le; 180</th>"
                 "<th>h &le; 190</th></tr>"
                 "<tr><th>Cumulative frequency</th><td>12</td><td>30</td><td>46</td><td>50</td></tr></table>"
                 "<p>Estimate how many plants are 175 cm or less.</p>",
            "steps": [
                "175 is halfway between 170 and 180.",
                "The cumulative frequency rises from 30 to 46 across that class, an increase of 16.",
                "Assuming the values are spread evenly, half of that increase has happened by 175: "
                + frac("1", "2") + " &times; 16 = 8",
                "Estimate = 30 + 8 = 38 plants",
            ],
            "answer": "about 38 plants",
        },
        {
            "marks": 4,
            "q": "<p>The table shows cumulative frequencies for 60 values.</p>"
                 "<table class='d'><tr><th>Value (x)</th><th>x &le; 10</th><th>x &le; 20</th><th>x &le; 30</th>"
                 "<th>x &le; 40</th><th>x &le; 50</th></tr>"
                 "<tr><th>Cumulative frequency</th><td>10</td><td>25</td><td>45</td><td>55</td><td>60</td></tr></table>"
                 "<p class='part'>(a) Estimate the median.</p>"
                 "<p class='part'>(b) Estimate the lower quartile.</p>"
                 "<p class='part'>(c) Estimate the interquartile range.</p>",
            "steps": [
                "<b>(a)</b> The median is the 30th value (half of 60). It lies between 20 and 30, where the "
                "cumulative frequency goes from 25 to 45.",
                "It is the 30 &minus; 25 = 5th of those 20 values: 20 + " + frac("5", "20") + " &times; 10 = 22.5",
                "<b>(b)</b> The lower quartile is the 15th value, between 10 and 20 (cumulative 10 to 25).",
                "10 + " + frac("5", "15") + " &times; 10 = 13.3 (1 d.p.)",
                "<b>(c)</b> The upper quartile is the 45th value, which the table shows is exactly at x = 30.",
                "IQR = 30 &minus; 13.3 = 16.7",
            ],
            "answer": "(a) about 22.5 &nbsp;&nbsp; (b) about 13.3 &nbsp;&nbsp; (c) about 16.7",
        },
        {
            "marks": 4,
            "q": "<p>A histogram has these bars.</p>"
                 "<table class='d'><tr><th>Class</th><th>0&ndash;5</th><th>5&ndash;10</th><th>10&ndash;20</th>"
                 "<th>20&ndash;40</th></tr>"
                 "<tr><th>Frequency density</th><td>4</td><td>6</td><td>3</td><td>1</td></tr></table>"
                 "<p class='part'>(a) Work out the frequency of each class and the total.</p>"
                 "<p class='part'>(b) Estimate how many values are greater than 15.</p>",
            "steps": [
                "<b>(a)</b> Frequency = frequency density &times; class width.",
                "4 &times; 5 = 20, &nbsp; 6 &times; 5 = 30, &nbsp; 3 &times; 10 = 30, &nbsp; 1 &times; 20 = 20",
                "Total = 20 + 30 + 30 + 20 = 100",
                "<b>(b)</b> From 15 to 20 is half of the 10&ndash;20 class: 3 &times; 5 = 15 values.",
                "The whole 20&ndash;40 class adds 20 more, so the estimate is 15 + 20 = 35",
            ],
            "answer": "(a) 20, 30, 30, 20 (total 100) &nbsp;&nbsp; (b) about 35",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>A class is 20 &lt; x &le; 50 and its frequency is 45.</p>"
                 "<p>Work out the frequency density.</p>",
            "steps": [
                "Class width = 50 &minus; 20 = 30",
                "Frequency density = " + frac("45", "30") + " = 1.5",
            ],
            "answer": "1.5",
        },
        {
            "marks": 2,
            "q": "<p>A histogram bar has frequency density 2.4 and covers a class of width 5.</p>"
                 "<p>Work out the frequency of that class.</p>",
            "steps": [
                "Frequency = frequency density &times; class width",
                "= 2.4 &times; 5 = 12",
            ],
            "answer": "12",
        },
        {
            "marks": 3,
            "q": "<p>Complete the frequency density column.</p>"
                 "<table class='d'><tr><th>Class width</th><th>6</th><th>11</th><th>13</th><th>24</th></tr>"
                 "<tr><th>Frequency</th><td>18</td><td>33</td><td>26</td><td>12</td></tr></table>",
            "steps": [
                "Divide each frequency by its class width.",
                "18 &divide; 6 = 3 and 33 &divide; 11 = 3",
                "26 &divide; 13 = 2 and 12 &divide; 24 = 0.5",
            ],
            "answer": "3, 3, 2 and 0.5",
        },
        {
            "marks": 3,
            "q": "<p>A class 20 &lt; x &le; 40 has frequency 36.</p>"
                 "<p>Estimate how many values lie between 25 and 40.</p>",
            "steps": [
                "The class is 20 wide and the part we want, from 25 to 40, is 15 wide.",
                "Assume the values are spread evenly across the class.",
                frac("15", "20") + " &times; 36 = 0.75 &times; 36",
                "= 27 values",
            ],
            "answer": "about 27",
        },
        {
            "marks": 4,
            "q": "<p>A histogram has these bars.</p>"
                 "<table class='d'><tr><th>Class</th><th>0&ndash;10</th><th>10&ndash;20</th><th>20&ndash;50</th>"
                 "<th>50&ndash;80</th></tr>"
                 "<tr><th>Frequency density</th><td>1.5</td><td>2.8</td><td>1.0</td><td>0.4</td></tr></table>"
                 "<p class='part'>(a) Work out the total frequency.</p>"
                 "<p class='part'>(b) Estimate the median.</p>",
            "steps": [
                "<b>(a)</b> Frequencies: 1.5 &times; 10 = 15, &nbsp; 2.8 &times; 10 = 28, &nbsp; "
                "1.0 &times; 30 = 30, &nbsp; 0.4 &times; 30 = 12",
                "Total = 15 + 28 + 30 + 12 = 85",
                "<b>(b)</b> The median is the 42.5th value (half of 85).",
                "Running totals: 15 up to 10, then 15 + 28 = 43 up to 20, so the median is in 10&ndash;20.",
                "It is the 42.5 &minus; 15 = 27.5th of the 28 values in that class.",
                "Median &asymp; 10 + " + frac("27.5", "28") + " &times; 10 = 10 + 9.82 = 19.8",
            ],
            "answer": "(a) 85 &nbsp;&nbsp; (b) about 19.8",
        },
        {
            "marks": 4,
            "q": "<p>The table shows cumulative frequencies for 80 values.</p>"
                 "<table class='d'><tr><th>Value (x)</th><th>x &le; 20</th><th>x &le; 40</th><th>x &le; 60</th>"
                 "<th>x &le; 80</th><th>x &le; 100</th></tr>"
                 "<tr><th>Cumulative frequency</th><td>8</td><td>26</td><td>54</td><td>72</td><td>80</td></tr></table>"
                 "<p class='part'>(a) Estimate the median.</p>"
                 "<p class='part'>(b) Estimate the quartiles.</p>"
                 "<p class='part'>(c) Work out the interquartile range.</p>",
            "steps": [
                "<b>(a)</b> The median is the 40th value, lying between 40 and 60 (cumulative 26 to 54).",
                "40 + " + frac("14", "28") + " &times; 20 = 40 + 10 = 50",
                "<b>(b)</b> Lower quartile: the 20th value, between 20 and 40 (cumulative 8 to 26).",
                "20 + " + frac("12", "18") + " &times; 20 = 20 + 13.3 = 33.3",
                "Upper quartile: the 60th value, between 60 and 80 (cumulative 54 to 72).",
                "60 + " + frac("6", "18") + " &times; 20 = 60 + 6.7 = 66.7",
                "<b>(c)</b> IQR = 66.7 &minus; 33.3 = 33.4 (about 33)",
            ],
            "answer": "(a) 50 &nbsp;&nbsp; (b) LQ about 33.3, UQ about 66.7 &nbsp;&nbsp; (c) about 33.4",
        },
        {
            "marks": 4,
            "q": "<p>Using the same cumulative frequency table (80 values),</p>"
                 "<p class='part'>(a) estimate how many values are greater than 70.</p>"
                 "<p class='part'>(b) express that as a percentage of the total.</p>",
            "steps": [
                "<b>(a)</b> First estimate the cumulative frequency at 70, which is halfway between 60 and 80.",
                "The cumulative frequency rises from 54 to 72 there, an increase of 18.",
                "Halfway gives 54 + " + frac("1", "2") + " &times; 18 = 54 + 9 = 63 values at 70 or below.",
                "Values above 70 = 80 &minus; 63 = 17",
                "<b>(b)</b> " + frac("17", "80") + " &times; 100 = 21.25%",
            ],
            "answer": "(a) about 17 &nbsp;&nbsp; (b) about 21.25%",
        },
        {
            "marks": 4,
            "q": "<p>Two groups of test marks have these summary values.</p>"
                 "<table class='d'><tr><th></th><th>Median</th><th>Lower quartile</th><th>Upper quartile</th></tr>"
                 "<tr><th>Group P</th><td>54</td><td>41</td><td>68</td></tr>"
                 "<tr><th>Group Q</th><td>60</td><td>54</td><td>67</td></tr></table>"
                 "<p class='part'>(a) Work out the interquartile range for each group.</p>"
                 "<p class='part'>(b) Compare the two groups, giving two clear comparisons.</p>",
            "steps": [
                "<b>(a)</b> Group P: 68 &minus; 41 = 27 &nbsp;&middot;&nbsp; Group Q: 67 &minus; 54 = 13",
                "<b>(b)</b> Averages: Group Q has the higher median (60 against 54), so on average Group Q "
                "scored better.",
                "Spread: Group Q has the smaller interquartile range (13 against 27), so its marks are more "
                "consistent &mdash; the middle half of Q&rsquo;s marks are packed into a much narrower band.",
            ],
            "answer": "(a) P: 27, Q: 13 &nbsp;&nbsp; (b) Q has the higher median (60 v 54) and the smaller IQR "
                      "(13 v 27), so it scored higher and more consistently",
        },
        {
            "marks": 4,
            "q": "<p>A histogram has three bars. The first, for 0 &lt; x &le; 20, has frequency density 1.2. "
                 "The second, for 20 &lt; x &le; 30, has frequency 30. The third covers 30 &lt; x &le; 60.</p>"
                 "<p>The total frequency is 90. Work out the frequency density of the third bar.</p>",
            "steps": [
                "First bar frequency = 1.2 &times; 20 = 24",
                "Second bar frequency = 30 (given).",
                "Third bar frequency = 90 &minus; 24 &minus; 30 = 36",
                "The third class width is 60 &minus; 30 = 30",
                "Frequency density = " + frac("36", "30") + " = 1.2",
            ],
            "answer": "1.2",
        },
        {
            "marks": 5,
            "q": "<p>A histogram of the times, t minutes, taken by 80 people has these bars.</p>"
                 "<table class='d'><tr><th>Time (t min)</th><th>0 &lt; t &le; 10</th><th>10 &lt; t &le; 20</th>"
                 "<th>20 &lt; t &le; 40</th><th>40 &lt; t &le; 80</th></tr>"
                 "<tr><th>Frequency density</th><td>1.2</td><td>2.8</td><td>1.4</td><td>0.3</td></tr></table>"
                 "<p class='part'>(a) Work out the frequency of each class and show the total is 80.</p>"
                 "<p class='part'>(b) Estimate the median.</p>"
                 "<p class='part'>(c) Estimate how many people took more than 30 minutes.</p>"
                 "<p class='part'>(d) Estimate the interquartile range.</p>",
            "steps": [
                "<b>(a)</b> 1.2 &times; 10 = 12, &nbsp; 2.8 &times; 10 = 28, &nbsp; 1.4 &times; 20 = 28, &nbsp; "
                "0.3 &times; 40 = 12",
                "Total = 12 + 28 + 28 + 12 = 80 &#10003;",
                "<b>(b)</b> The median is the 40th value. Running totals are 12, 40, 68, 80.",
                "The 40th value is exactly the last of the second class, so the median is about 20 minutes.",
                "<b>(c)</b> From 30 to 40 is half of the third class: " + frac("1", "2") + " &times; 28 = 14",
                "Plus the whole final class of 12, giving 14 + 12 = 26 people.",
                "<b>(d)</b> Lower quartile: the 20th value, in the second class (12 to 40).",
                "10 + " + frac("8", "28") + " &times; 10 = 12.9 (1 d.p.)",
                "Upper quartile: the 60th value, in the third class (40 to 68): 20 + " + frac("20", "28") + " &times; 20 = 34.3",
                "IQR &asymp; 34.3 &minus; 12.9 = 21.4 minutes",
            ],
            "answer": "(a) 12, 28, 28, 12 (total 80) &nbsp;&nbsp; (b) about 20 minutes &nbsp;&nbsp; "
                      "(c) about 26 people &nbsp;&nbsp; (d) about 21.4 minutes",
        },
    ],
}

PAPERS = [TREE_DIAGRAMS, CONDITIONAL, AVERAGES, HISTOGRAMS]
