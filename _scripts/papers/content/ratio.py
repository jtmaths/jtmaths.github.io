"""GCSE practice paper — Ratio, Proportion and Rates of Change (topic level)."""
from build import frac

PAPER = {
    "title": "Ratio, Proportion and Rates of Change",
    "folder": "gcse/ratio",
    "slug": "ratio-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write the ratio 12 : 18 in its simplest form.</p>",
            "steps": [
                "Find the highest common factor of 12 and 18, which is 6.",
                "Divide both sides by 6: 12 &divide; 6 = 2 and 18 &divide; 6 = 3",
            ],
            "answer": "2 : 3",
        },
        {
            "marks": 2,
            "q": "<p>Share &pound;60 in the ratio 2 : 3</p>",
            "steps": [
                "Add the parts of the ratio: 2 + 3 = 5 parts altogether.",
                "One part is worth &pound;60 &divide; 5 = &pound;12",
                "2 parts = 2 &times; 12 = &pound;24 and 3 parts = 3 &times; 12 = &pound;36",
                "Check: 24 + 36 = 60 &#10003;",
            ],
            "answer": "&pound;24 and &pound;36",
        },
        {
            "marks": 2,
            "q": "<p>A recipe for 4 people uses 200 g of rice.</p>"
                 "<p>How much rice is needed for 10 people?</p>",
            "steps": [
                "Find the amount for one person first: 200 &divide; 4 = 50 g per person.",
                "Then multiply by 10: 50 &times; 10 = 500 g",
            ],
            "answer": "500 g",
        },
        {
            "marks": 2,
            "q": "<p>Work out 15% of 240</p>",
            "steps": [
                "10% of 240 = 240 &divide; 10 = 24",
                "5% is half of 10%, so 5% of 240 = 12",
                "15% = 10% + 5% = 24 + 12 = 36",
            ],
            "answer": "36",
        },
        {
            "marks": 3,
            "q": "<p>A map is drawn to a scale of 1 : 25 000</p>"
                 "<p>Two villages are 6 cm apart on the map.</p>"
                 "<p>Work out the real distance between the villages, in kilometres.</p>",
            "steps": [
                "The scale means 1 cm on the map represents 25 000 cm in real life.",
                "6 cm represents 6 &times; 25 000 = 150 000 cm",
                "Convert to metres: 150 000 &divide; 100 = 1500 m",
                "Convert to kilometres: 1500 &divide; 1000 = 1.5 km",
            ],
            "answer": "1.5 km",
        },
        {
            "marks": 3,
            "q": "<p class='part'>(a) Increase &pound;48 by 25%</p>"
                 "<p class='part'>(b) Decrease 90 kg by 30%</p>",
            "steps": [
                "<b>(a)</b> 25% of 48 = 48 &divide; 4 = 12",
                "Increase means add on: 48 + 12 = &pound;60",
                "<b>(b)</b> 10% of 90 = 9, so 30% of 90 = 27",
                "Decrease means take away: 90 &minus; 27 = 63 kg",
                "(A quicker method is to multiply by 1.25 and by 0.7.)",
            ],
            "answer": "(a) &pound;60 &nbsp;&nbsp; (b) 63 kg",
        },
        {
            "marks": 3,
            "q": "<p>A 500 g box of cereal costs &pound;1.80</p>"
                 "<p>An 800 g box of the same cereal costs &pound;2.72</p>"
                 "<p>Which box is better value for money? You must show your working.</p>",
            "steps": [
                "Compare the two boxes using the same measure &mdash; the cost of 1 gram.",
                "Small box: 180p &divide; 500 = 0.36p per gram",
                "Large box: 272p &divide; 800 = 0.34p per gram",
                "The large box costs less per gram, so it is better value.",
            ],
            "answer": "The 800 g box (0.34p per gram against 0.36p per gram)",
        },
        {
            "marks": 3,
            "q": "<p>A car travels 150 km in 2 hours 30 minutes.</p>"
                 "<p>Work out the average speed of the car in km/h.</p>",
            "steps": [
                "The time must be in hours to get an answer in km/h.",
                "30 minutes = 0.5 hours, so the time is 2.5 hours.",
                "Speed = " + frac("distance", "time") + " = " + frac("150", "2.5"),
                "150 &divide; 2.5 = 60",
            ],
            "answer": "60 km/h",
        },
        {
            "marks": 4,
            "q": "<p>In a class the ratio of boys to girls is 3 : 5</p>"
                 "<p>There are 12 more girls than boys.</p>"
                 "<p>Work out the total number of students in the class.</p>",
            "steps": [
                "The difference between the parts of the ratio is 5 &minus; 3 = 2 parts.",
                "Those 2 parts are worth 12 students.",
                "So 1 part = 12 &divide; 2 = 6 students.",
                "The total is 3 + 5 = 8 parts, so the class has 8 &times; 6 = 48 students.",
                "Check: boys = 3 &times; 6 = 18, girls = 5 &times; 6 = 30, and 30 &minus; 18 = 12 &#10003;",
            ],
            "answer": "48 students",
        },
        {
            "marks": 4,
            "q": "<p>Here is a recipe for 12 biscuits.</p>"
                 "<table class='d'><tr><th>Flour</th><th>Butter</th><th>Sugar</th></tr>"
                 "<tr><td>150 g</td><td>80 g</td><td>60 g</td></tr></table>"
                 "<p>Kim has 400 g of flour, 200 g of butter and 200 g of sugar.</p>"
                 "<p>What is the greatest number of biscuits Kim can make?</p>",
            "steps": [
                "Work out how many batches of 12 each ingredient would allow.",
                "Flour: 400 &divide; 150 = 2.66&hellip; batches",
                "Butter: 200 &divide; 80 = 2.5 batches",
                "Sugar: 200 &divide; 60 = 3.33&hellip; batches",
                "The butter runs out first, so it limits her to 2.5 batches.",
                "2.5 &times; 12 = 30 biscuits.",
            ],
            "answer": "30 biscuits (butter is the limiting ingredient)",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>Write the ratio 4 : 10 in the form 1 : n</p>",
            "steps": [
                "To make the left-hand side 1, divide both sides by 4.",
                "4 &divide; 4 = 1 and 10 &divide; 4 = 2.5",
            ],
            "answer": "1 : 2.5",
        },
        {
            "marks": 2,
            "q": "<p>Express 45 minutes as a percentage of 3 hours.</p>",
            "steps": [
                "Put both times into the same units: 3 hours = 180 minutes.",
                "Write the fraction: " + frac("45", "180") + " = " + frac("1", "4"),
                "Convert to a percentage: " + frac("1", "4") + " &times; 100 = 25%",
            ],
            "answer": "25%",
        },
        {
            "marks": 3,
            "q": "<p>In a sale, the price of a jacket is increased by 20%.</p>"
                 "<p>The new price is &pound;54</p>"
                 "<p>Work out the original price of the jacket.</p>",
            "steps": [
                "This is a reverse percentage &mdash; do not simply take 20% off &pound;54.",
                "The original price is 100%; after a 20% increase the new price is 120% of it.",
                "So 120% = &pound;54, which means the multiplier used was 1.2",
                "Original price = 54 &divide; 1.2 = &pound;45",
                "Check: 45 &times; 1.2 = 54 &#10003;",
            ],
            "answer": "&pound;45",
        },
        {
            "marks": 3,
            "q": "<p>Ravi invests &pound;2000 in an account paying 3% compound interest per year.</p>"
                 "<p>Work out the value of the investment after 4 years.</p>"
                 "<p>Give your answer to the nearest penny.</p>",
            "steps": [
                "Compound interest multiplies by the same factor every year.",
                "The multiplier for a 3% increase is 1.03",
                "After 4 years the value is 2000 &times; 1.03<sup>4</sup>",
                "1.03<sup>4</sup> = 1.12550881",
                "2000 &times; 1.12550881 = 2251.01762, which is &pound;2251.02 to the nearest penny.",
            ],
            "answer": "&pound;2251.02",
        },
        {
            "marks": 4,
            "q": "<p><i>y</i> is inversely proportional to <i>x</i><sup>2</sup>.</p>"
                 "<p>When <i>x</i> = 2, <i>y</i> = 9</p>"
                 "<p class='part'>(a) Find a formula for <i>y</i> in terms of <i>x</i>.</p>"
                 "<p class='part'>(b) Work out <i>y</i> when <i>x</i> = 6</p>"
                 "<p class='part'>(c) Work out the positive value of <i>x</i> when <i>y</i> = 4</p>",
            "steps": [
                "<b>(a)</b> Inversely proportional to <i>x</i><sup>2</sup> means <i>y</i> = " + frac("k", "<i>x</i><sup>2</sup>"),
                "Substitute <i>x</i> = 2 and <i>y</i> = 9: 9 = " + frac("k", "4") + ", so k = 36",
                "The formula is <i>y</i> = " + frac("36", "<i>x</i><sup>2</sup>"),
                "<b>(b)</b> <i>y</i> = " + frac("36", "6<sup>2</sup>") + " = " + frac("36", "36") + " = 1",
                "<b>(c)</b> 4 = " + frac("36", "<i>x</i><sup>2</sup>") + ", so 4<i>x</i><sup>2</sup> = 36 and <i>x</i><sup>2</sup> = 9",
                "The positive root is <i>x</i> = 3",
            ],
            "answer": "(a) <i>y</i> = " + frac("36", "<i>x</i><sup>2</sup>") + " &nbsp;&nbsp; (b) 1 &nbsp;&nbsp; (c) 3",
        },
        {
            "marks": 4,
            "q": "<p>A bag contains red counters and blue counters in the ratio 5 : 3</p>"
                 "<p>10 more blue counters are put into the bag.</p>"
                 "<p>The ratio of red to blue counters is now 5 : 4</p>"
                 "<p>Work out the total number of counters now in the bag.</p>",
            "steps": [
                "Let the original numbers be 5<i>x</i> red and 3<i>x</i> blue.",
                "After adding 10 blue counters the ratio is 5<i>x</i> : (3<i>x</i> + 10) = 5 : 4",
                "Cross-multiply: 4 &times; 5<i>x</i> = 5 &times; (3<i>x</i> + 10), so 20<i>x</i> = 15<i>x</i> + 50",
                "5<i>x</i> = 50, so <i>x</i> = 10",
                "Red = 5 &times; 10 = 50 and blue = 3 &times; 10 + 10 = 40",
                "Total = 50 + 40 = 90. Check: 50 : 40 simplifies to 5 : 4 &#10003;",
            ],
            "answer": "90 counters",
        },
        {
            "marks": 4,
            "q": "<p>Two solids are mathematically similar.</p>"
                 "<p>The smaller solid has surface area 50 cm<sup>2</sup> and volume 40 cm<sup>3</sup>.</p>"
                 "<p>The larger solid has surface area 200 cm<sup>2</sup>.</p>"
                 "<p>Work out the volume of the larger solid.</p>",
            "steps": [
                "For similar solids the area scale factor is the square of the length scale factor.",
                "Area scale factor = " + frac("200", "50") + " = 4",
                "So the length scale factor is &radic;4 = 2",
                "The volume scale factor is the cube of the length scale factor: 2<sup>3</sup> = 8",
                "Volume of larger solid = 40 &times; 8 = 320 cm<sup>3</sup>",
            ],
            "answer": "320 cm<sup>3</sup>",
        },
        {
            "marks": 4,
            "q": "<p>A block of metal has mass 2.4 kg and volume 300 cm<sup>3</sup>.</p>"
                 "<p class='part'>(a) Work out the density of the metal in g/cm<sup>3</sup>.</p>"
                 "<p class='part'>(b) A second block of the same metal has volume 750 cm<sup>3</sup>. "
                 "Work out its mass in kilograms.</p>",
            "steps": [
                "<b>(a)</b> The units g/cm<sup>3</sup> tell you the mass must be in grams: 2.4 kg = 2400 g",
                "Density = " + frac("mass", "volume") + " = " + frac("2400", "300") + " = 8 g/cm<sup>3</sup>",
                "<b>(b)</b> Same metal means the same density, so rearrange to mass = density &times; volume.",
                "Mass = 8 &times; 750 = 6000 g",
                "Convert back: 6000 &divide; 1000 = 6 kg",
            ],
            "answer": "(a) 8 g/cm<sup>3</sup> &nbsp;&nbsp; (b) 6 kg",
        },
        {
            "marks": 4,
            "q": "<p>A lorry drives 120 km at an average speed of 80 km/h.</p>"
                 "<p>It then drives a further 60 km at an average speed of 40 km/h.</p>"
                 "<p>Work out the average speed for the whole journey.</p>",
            "steps": [
                "You cannot just average 80 and 40 &mdash; the two stages take different amounts of time.",
                "Find each time using time = " + frac("distance", "speed"),
                "First stage: 120 &divide; 80 = 1.5 hours",
                "Second stage: 60 &divide; 40 = 1.5 hours, so the total time is 3 hours.",
                "Total distance = 120 + 60 = 180 km",
                "Average speed = " + frac("180", "3") + " = 60 km/h",
            ],
            "answer": "60 km/h",
        },
        {
            "marks": 5,
            "q": "<p>The population of a town is 40 000.</p>"
                 "<p>The population is falling by 4% each year.</p>"
                 "<p class='part'>(a) Work out the population after 5 years, to the nearest whole number.</p>"
                 "<p class='part'>(b) Find the least number of complete years it takes for the population "
                 "to fall below 30 000.</p>",
            "steps": [
                "<b>(a)</b> A 4% fall means multiplying by 1 &minus; 0.04 = 0.96 each year.",
                "After 5 years: 40 000 &times; 0.96<sup>5</sup>",
                "0.96<sup>5</sup> = 0.8153726976, so the population is 40 000 &times; 0.8153726976 = 32 614.9&hellip;",
                "To the nearest whole number that is 32 615 people.",
                "<b>(b)</b> Try successive years until the population drops below 30 000.",
                "After 7 years: 40 000 &times; 0.96<sup>7</sup> = 40 000 &times; 0.751447&hellip; = 30 057.9 &mdash; still above 30 000.",
                "After 8 years: 40 000 &times; 0.96<sup>8</sup> = 40 000 &times; 0.721389&hellip; = 28 855.6 &mdash; below 30 000.",
                "So it takes 8 complete years.",
            ],
            "answer": "(a) 32 615 &nbsp;&nbsp; (b) 8 years",
        },
    ],
}
