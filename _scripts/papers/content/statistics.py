"""GCSE practice paper — Statistics (topic level)."""
from build import frac

PAPER = {
    "title": "Statistics",
    "folder": "gcse/statistics",
    "slug": "statistics-practice",
    "foundation": [
        {
            "marks": 1,
            "q": "<p>Write down the mode of these numbers.</p>"
                 "<p><b>3&nbsp;&nbsp; 7&nbsp;&nbsp; 4&nbsp;&nbsp; 7&nbsp;&nbsp; 2&nbsp;&nbsp; 9&nbsp;&nbsp; 7</b></p>",
            "steps": [
                "The mode is the value that appears most often.",
                "7 appears three times; every other value appears once.",
            ],
            "answer": "7",
        },
        {
            "marks": 2,
            "q": "<p>Work out the mean of these numbers.</p>"
                 "<p><b>4&nbsp;&nbsp; 8&nbsp;&nbsp; 5&nbsp;&nbsp; 11&nbsp;&nbsp; 7</b></p>",
            "steps": [
                "Add all the values: 4 + 8 + 5 + 11 + 7 = 35",
                "Divide by how many there are: 35 &divide; 5 = 7",
            ],
            "answer": "7",
        },
        {
            "marks": 2,
            "q": "<p>Here are seven numbers.</p>"
                 "<p><b>12&nbsp;&nbsp; 5&nbsp;&nbsp; 9&nbsp;&nbsp; 15&nbsp;&nbsp; 3&nbsp;&nbsp; 9&nbsp;&nbsp; 20</b></p>"
                 "<p class='part'>(a) Work out the median.</p>"
                 "<p class='part'>(b) Work out the range.</p>",
            "steps": [
                "Put the numbers in order first: 3, 5, 9, 9, 12, 15, 20",
                "<b>(a)</b> There are 7 values, so the median is the 4th one along: 9",
                "<b>(b)</b> Range = largest &minus; smallest = 20 &minus; 3 = 17",
            ],
            "answer": "(a) 9 &nbsp;&nbsp; (b) 17",
        },
        {
            "marks": 2,
            "q": "<p>The table shows the favourite sport of some students.</p>"
                 "<table class='d'><tr><th>Sport</th><th>Football</th><th>Netball</th><th>Rugby</th><th>Tennis</th></tr>"
                 "<tr><th>Frequency</th><td>12</td><td>8</td><td>5</td><td>7</td></tr></table>"
                 "<p class='part'>(a) Write down the modal sport.</p>"
                 "<p class='part'>(b) How many students were asked altogether?</p>",
            "steps": [
                "<b>(a)</b> The modal sport is the one with the highest frequency, which is football with 12.",
                "<b>(b)</b> Add all the frequencies: 12 + 8 + 5 + 7 = 32",
            ],
            "answer": "(a) Football &nbsp;&nbsp; (b) 32 students",
        },
        {
            "marks": 3,
            "q": "<p>The table shows the number of pets owned by 25 families.</p>"
                 "<table class='d'><tr><th>Number of pets</th><th>0</th><th>1</th><th>2</th><th>3</th></tr>"
                 "<tr><th>Frequency</th><td>8</td><td>10</td><td>5</td><td>2</td></tr></table>"
                 "<p>Work out the mean number of pets per family.</p>",
            "steps": [
                "Multiply each number of pets by its frequency to find the total number of pets.",
                "0 &times; 8 = 0, &nbsp; 1 &times; 10 = 10, &nbsp; 2 &times; 5 = 10, &nbsp; 3 &times; 2 = 6",
                "Total pets = 0 + 10 + 10 + 6 = 26",
                "Total families = 8 + 10 + 5 + 2 = 25",
                "Mean = " + frac("26", "25") + " = 1.04",
            ],
            "answer": "1.04 pets per family",
        },
        {
            "marks": 3,
            "q": "<p>Describe the type of correlation you would expect to see on a scatter graph of</p>"
                 "<p class='part'>(a) the age of a car and its value</p>"
                 "<p class='part'>(b) the height of a person and their shoe size</p>"
                 "<p class='part'>(c) the house number a person lives at and their shoe size.</p>",
            "steps": [
                "<b>(a)</b> Older cars are generally worth less, so as one goes up the other goes down &mdash; negative correlation.",
                "<b>(b)</b> Taller people generally have bigger feet, so both go up together &mdash; positive correlation.",
                "<b>(c)</b> There is no sensible link between a house number and a shoe size &mdash; no correlation.",
                "Remember that correlation does not prove that one thing causes the other.",
            ],
            "answer": "(a) negative &nbsp;&nbsp; (b) positive &nbsp;&nbsp; (c) none",
        },
        {
            "marks": 3,
            "q": "<p>90 people were asked to name their favourite colour. The results are shown in a pie chart.</p>"
                 "<p class='part'>(a) 30 people chose blue. Work out the angle of the blue sector.</p>"
                 "<p class='part'>(b) The angle of the red sector is 72&deg;. How many people chose red?</p>",
            "steps": [
                "A full pie chart is 360&deg; and represents all 90 people.",
                "So each person is worth 360 &divide; 90 = 4&deg;",
                "<b>(a)</b> 30 people &times; 4&deg; = 120&deg;",
                "<b>(b)</b> 72 &divide; 4 = 18 people",
            ],
            "answer": "(a) 120&deg; &nbsp;&nbsp; (b) 18 people",
        },
        {
            "marks": 3,
            "q": "<p>The table shows the time, t minutes, that 30 people waited for a bus.</p>"
                 "<table class='d'><tr><th>Time (t minutes)</th><th>0 &lt; t &le; 10</th><th>10 &lt; t &le; 20</th>"
                 "<th>20 &lt; t &le; 30</th><th>30 &lt; t &le; 40</th></tr>"
                 "<tr><th>Frequency</th><td>5</td><td>12</td><td>8</td><td>5</td></tr></table>"
                 "<p class='part'>(a) Write down the modal class.</p>"
                 "<p class='part'>(b) Write down the class interval that contains the median.</p>",
            "steps": [
                "<b>(a)</b> The modal class is the interval with the highest frequency, which is 12.",
                "That is 10 &lt; t &le; 20",
                "<b>(b)</b> With 30 values the median lies between the 15th and 16th values.",
                "Running totals: 5 after the first class, then 5 + 12 = 17 after the second.",
                "Both the 15th and 16th values fall inside the second class.",
            ],
            "answer": "(a) 10 &lt; t &le; 20 &nbsp;&nbsp; (b) 10 &lt; t &le; 20",
        },
        {
            "marks": 4,
            "q": "<p>Use the same table of waiting times.</p>"
                 "<table class='d'><tr><th>Time (t minutes)</th><th>0 &lt; t &le; 10</th><th>10 &lt; t &le; 20</th>"
                 "<th>20 &lt; t &le; 30</th><th>30 &lt; t &le; 40</th></tr>"
                 "<tr><th>Frequency</th><td>5</td><td>12</td><td>8</td><td>5</td></tr></table>"
                 "<p class='part'>(a) Work out an estimate for the mean waiting time.</p>"
                 "<p class='part'>(b) Explain why your answer is only an estimate.</p>",
            "steps": [
                "<b>(a)</b> Use the midpoint of each class to stand for every value in it.",
                "Midpoints: 5, 15, 25 and 35",
                "Midpoint &times; frequency: 5 &times; 5 = 25, &nbsp; 15 &times; 12 = 180, &nbsp; 25 &times; 8 = 200, &nbsp; 35 &times; 5 = 175",
                "Total = 25 + 180 + 200 + 175 = 580, and there are 30 people.",
                "Mean = " + frac("580", "30") + " = 19.33&hellip; minutes",
                "<b>(b)</b> The table does not give the individual times, so using midpoints assumes the values are "
                "spread evenly within each class, which may not be true.",
            ],
            "answer": "(a) about 19.3 minutes &nbsp;&nbsp; (b) the original data is grouped, so midpoints are only assumed values",
        },
        {
            "marks": 4,
            "q": "<p>Class A has 10 students and their mean test score is 62.</p>"
                 "<p>Class B has 15 students and their mean test score is 68.</p>"
                 "<p class='part'>(a) Work out the mean score of all 25 students.</p>"
                 "<p class='part'>(b) The range for class A is 30 and the range for class B is 12. "
                 "Write down one comparison you can make between the two classes.</p>",
            "steps": [
                "<b>(a)</b> You cannot average the two means, because the classes are different sizes.",
                "Total for class A = 10 &times; 62 = 620",
                "Total for class B = 15 &times; 68 = 1020",
                "Overall total = 620 + 1020 = 1640 over 25 students.",
                "Mean = " + frac("1640", "25") + " = 65.6",
                "<b>(b)</b> Class B has the smaller range, so its scores are more consistent (less spread out) "
                "than class A&rsquo;s. (Class B also has the higher mean, so on average it scored better.)",
            ],
            "answer": "(a) 65.6 &nbsp;&nbsp; (b) class B&rsquo;s scores are more consistent &mdash; a much smaller range",
        },
    ],
    "higher": [
        {
            "marks": 2,
            "q": "<p>The mean of eight numbers is 15.</p>"
                 "<p>One of the numbers, 22, is removed.</p>"
                 "<p>Work out the mean of the remaining seven numbers.</p>",
            "steps": [
                "Total of the eight numbers = 8 &times; 15 = 120",
                "After removing 22 the total is 120 &minus; 22 = 98, spread over 7 numbers.",
                "New mean = 98 &divide; 7 = 14",
            ],
            "answer": "14",
        },
        {
            "marks": 2,
            "q": "<p>Ella wants to find out how much exercise adults in her town do each week.</p>"
                 "<p>She asks 50 people as they leave a gym.</p>"
                 "<p>Give one reason why her sample may be biased, and suggest one improvement.</p>",
            "steps": [
                "People leaving a gym are far more likely to exercise regularly than the population as a whole.",
                "So the sample is not representative &mdash; it will overestimate the average amount of exercise.",
                "A better method would be to select people at random from the whole town, for example from the "
                "electoral roll, or to survey in several different locations at different times.",
            ],
            "answer": "Gym-goers are not typical of all adults, so the results will be too high; take a random sample "
                      "from the whole town instead",
        },
        {
            "marks": 3,
            "q": "<p>A school has 300 students in Year 10 and 200 students in Year 11.</p>"
                 "<p>A stratified sample of 75 students is taken from these two year groups.</p>"
                 "<p>Work out how many students should be taken from each year group.</p>",
            "steps": [
                "There are 300 + 200 = 500 students altogether.",
                "The sampling fraction is " + frac("75", "500") + " = 0.15",
                "Year 10: 0.15 &times; 300 = 45 students",
                "Year 11: 0.15 &times; 200 = 30 students",
                "Check: 45 + 30 = 75 &#10003;",
            ],
            "answer": "45 from Year 10 and 30 from Year 11",
        },
        {
            "marks": 3,
            "q": "<p>The cumulative frequency table shows the heights, h cm, of 80 plants.</p>"
                 "<table class='d'><tr><th>Height (h cm)</th><th>h &le; 150</th><th>h &le; 160</th>"
                 "<th>h &le; 170</th><th>h &le; 180</th><th>h &le; 190</th></tr>"
                 "<tr><th>Cumulative frequency</th><td>8</td><td>24</td><td>56</td><td>72</td><td>80</td></tr></table>"
                 "<p>Use the table to estimate the median height.</p>",
            "steps": [
                "With 80 plants the median is the value of the 40th plant (half of 80).",
                "The running totals show 24 plants up to 160 cm and 56 up to 170 cm, so the 40th plant lies "
                "in the class 160 &lt; h &le; 170.",
                "That class contains 56 &minus; 24 = 32 plants, and the 40th is the 40 &minus; 24 = 16th of them.",
                frac("16", "32") + " of the way through a 10 cm class is 5 cm.",
                "Median &asymp; 160 + 5 = 165 cm",
            ],
            "answer": "about 165 cm",
        },
        {
            "marks": 4,
            "q": "<p>The table shows the times, t minutes, taken by 87 people to finish a puzzle.</p>"
                 "<table class='d'><tr><th>Time (t minutes)</th><th>0 &lt; t &le; 10</th><th>10 &lt; t &le; 20</th>"
                 "<th>20 &lt; t &le; 40</th><th>40 &lt; t &le; 70</th></tr>"
                 "<tr><th>Frequency</th><td>15</td><td>24</td><td>30</td><td>18</td></tr></table>"
                 "<p class='part'>(a) Work out the frequency density for each class.</p>"
                 "<p class='part'>(b) Estimate the number of people who took between 30 and 40 minutes.</p>",
            "steps": [
                "<b>(a)</b> Frequency density = " + frac("frequency", "class width"),
                "0&ndash;10 (width 10): 15 &divide; 10 = 1.5 &nbsp;&middot;&nbsp; 10&ndash;20 (width 10): 24 &divide; 10 = 2.4",
                "20&ndash;40 (width 20): 30 &divide; 20 = 1.5 &nbsp;&middot;&nbsp; 40&ndash;70 (width 30): 18 &divide; 30 = 0.6",
                "<b>(b)</b> 30 to 40 minutes is half of the 20 &lt; t &le; 40 class, which is 20 minutes wide.",
                "Assume the 30 people are spread evenly: " + frac("10", "20") + " &times; 30 = 15 people "
                "(or frequency density 1.5 &times; width 10 = 15).",
            ],
            "answer": "(a) 1.5, 2.4, 1.5, 0.6 &nbsp;&nbsp; (b) about 15 people",
        },
        {
            "marks": 4,
            "q": "<p>Box plots were drawn for the test marks of a group of boys and a group of girls.</p>"
                 "<table class='d'><tr><th></th><th>Min</th><th>LQ</th><th>Median</th><th>UQ</th><th>Max</th></tr>"
                 "<tr><th>Boys</th><td>12</td><td>20</td><td>26</td><td>33</td><td>45</td></tr>"
                 "<tr><th>Girls</th><td>15</td><td>24</td><td>28</td><td>32</td><td>40</td></tr></table>"
                 "<p class='part'>(a) Work out the interquartile range for each group.</p>"
                 "<p class='part'>(b) Make two comparisons between the marks of the boys and the girls.</p>",
            "steps": [
                "<b>(a)</b> Interquartile range = upper quartile &minus; lower quartile.",
                "Boys: 33 &minus; 20 = 13 &nbsp;&middot;&nbsp; Girls: 32 &minus; 24 = 8",
                "<b>(b)</b> Comparison 1 &mdash; averages: the girls&rsquo; median (28) is higher than the boys&rsquo; (26), "
                "so on average the girls scored slightly more.",
                "Comparison 2 &mdash; spread: the girls&rsquo; interquartile range (8) is smaller than the boys&rsquo; (13), "
                "so the girls&rsquo; marks were more consistent.",
                "Always compare one average <b>and</b> one measure of spread, and refer to the numbers.",
            ],
            "answer": "(a) boys 13, girls 8 &nbsp;&nbsp; (b) girls have the higher median (28 v 26) and the smaller IQR "
                      "(8 v 13), so they scored higher and more consistently",
        },
        {
            "marks": 4,
            "q": "<p>A scatter graph was drawn of revision time, <i>x</i> hours, against test score, <i>y</i> marks, "
                 "for 12 students who each revised between 2 and 12 hours.</p>"
                 "<p>The line of best fit has equation <i>y</i> = 2.5<i>x</i> + 12</p>"
                 "<p class='part'>(a) Estimate the score of a student who revised for 8 hours.</p>"
                 "<p class='part'>(b) Interpret the number 2.5 in the context of the question.</p>"
                 "<p class='part'>(c) Explain why the line should not be used to estimate the score of a student "
                 "who revised for 40 hours.</p>",
            "steps": [
                "<b>(a)</b> Substitute <i>x</i> = 8: <i>y</i> = 2.5 &times; 8 + 12 = 20 + 12 = 32 marks",
                "<b>(b)</b> 2.5 is the gradient, so each extra hour of revision is associated with about "
                "2.5 extra marks.",
                "<b>(c)</b> 40 hours is well outside the range of the original data (2 to 12 hours).",
                "Using the line beyond the data is extrapolation, and there is no evidence that the same "
                "straight-line pattern continues that far &mdash; the formula would predict 112 marks, which may "
                "not even be possible.",
            ],
            "answer": "(a) 32 marks &nbsp;&nbsp; (b) about 2.5 extra marks per extra hour of revision &nbsp;&nbsp; "
                      "(c) 40 hours is outside the data range, so it is unreliable extrapolation",
        },
        {
            "marks": 4,
            "q": "<p>The table shows the weights, w kg, of 40 parcels.</p>"
                 "<table class='d'><tr><th>Weight (w kg)</th><th>0 &lt; w &le; 20</th><th>20 &lt; w &le; 40</th>"
                 "<th>40 &lt; w &le; 60</th><th>60 &lt; w &le; 80</th></tr>"
                 "<tr><th>Frequency</th><td>7</td><td>13</td><td>15</td><td>5</td></tr></table>"
                 "<p>Work out an estimate for the mean weight of a parcel.</p>",
            "steps": [
                "Use the midpoint of each class as a representative value.",
                "Midpoints: 10, 30, 50 and 70",
                "Midpoint &times; frequency: 10 &times; 7 = 70, &nbsp; 30 &times; 13 = 390, &nbsp; 50 &times; 15 = 750, &nbsp; 70 &times; 5 = 350",
                "Total = 70 + 390 + 750 + 350 = 1560",
                "There are 7 + 13 + 15 + 5 = 40 parcels.",
                "Mean = " + frac("1560", "40") + " = 39 kg",
            ],
            "answer": "39 kg",
        },
        {
            "marks": 4,
            "q": "<p>A group contains 20 people.</p>"
                 "<p>The mean age of the 12 women in the group is 34 years.</p>"
                 "<p>The mean age of all 20 people is 31 years.</p>"
                 "<p>Work out the mean age of the 8 men.</p>",
            "steps": [
                "Turn every mean into a total.",
                "Total age of all 20 people = 20 &times; 31 = 620 years",
                "Total age of the 12 women = 12 &times; 34 = 408 years",
                "Total age of the 8 men = 620 &minus; 408 = 212 years",
                "Mean age of the men = " + frac("212", "8") + " = 26.5 years",
            ],
            "answer": "26.5 years",
        },
        {
            "marks": 5,
            "q": "<p>A histogram was drawn for the distances, d km, travelled by 82 delivery drivers. "
                 "The bars have these frequency densities.</p>"
                 "<table class='d'><tr><th>Distance (d km)</th><th>0 &lt; d &le; 10</th><th>10 &lt; d &le; 20</th>"
                 "<th>20 &lt; d &le; 50</th><th>50 &lt; d &le; 80</th></tr>"
                 "<tr><th>Frequency density</th><td>1.2</td><td>2.8</td><td>1.0</td><td>0.4</td></tr></table>"
                 "<p class='part'>(a) Work out the frequency of each class and show that the total is 82.</p>"
                 "<p class='part'>(b) Estimate the number of drivers who travelled more than 40 km.</p>"
                 "<p class='part'>(c) Estimate the median distance.</p>",
            "steps": [
                "<b>(a)</b> Frequency = frequency density &times; class width.",
                "1.2 &times; 10 = 12, &nbsp; 2.8 &times; 10 = 28, &nbsp; 1.0 &times; 30 = 30, &nbsp; 0.4 &times; 30 = 12",
                "Total = 12 + 28 + 30 + 12 = 82 &#10003;",
                "<b>(b)</b> More than 40 km covers the last 10 km of the 20&ndash;50 class plus the whole 50&ndash;80 class.",
                "40 to 50 km: 1.0 &times; 10 = 10 drivers, and 50 to 80 km: 12 drivers, giving 10 + 12 = 22 drivers.",
                "<b>(c)</b> The median is the 41st value (half of 82).",
                "Running totals: 12 up to 10 km, then 12 + 28 = 40 up to 20 km, then 70 up to 50 km.",
                "So the 41st value is the 1st value in the 20 &lt; d &le; 50 class, which holds 30 drivers across 30 km.",
                "Median &asymp; 20 + " + frac("1", "30") + " &times; 30 = 21 km",
            ],
            "answer": "(a) 12, 28, 30, 12 (total 82) &nbsp;&nbsp; (b) about 22 drivers &nbsp;&nbsp; (c) about 21 km",
        },
    ],
}
