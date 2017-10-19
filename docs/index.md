
<!-- # National Achievement Survey of Class VIII students -->
## Introduction

This is a project based on a use case of [Gramener](https://gramener.com), a data science company. The aim is to identify the trends in 8th grade student performance based on National Achievement Survey by NCERT.

### About this report

This is a distilled version of analysis with the most significant insights about data. The orignial version with codes used to generate graphs can be found [**here**](/dsgramner/ipython_md/analysis.html)

## Questions

We have attempted to answer three most pertaining questions below.

1. [What influences students performance the most?](#what-influences-students-performance-the-most)
2. [How do boys and girls perform across states?](#how-do-boys-and-girls-perform-across-states)
3. [Do students from South Indian states really excel at Math and Science?](#do-students-from-south-indian-states-really-excel-at-math-and-science)

### What influences students performance the most?

We addded an additional feature as 'performance' = average of ('Maths %', 'Reading %', 'Science %', 'Social %') to find which feature has the highest overall influence on student performance. A feature selection is performed based on `SelectKBest` to evaluvate the relative importance of features based on the scores. The heat map sumamrize the feature importance for each subject: Reading, Science, Social, Mathew and Overall performance. It is curious that certian features are more promienent in deciding the marks of subjects

<div align = "center"><img src="./index_files/f1_heatmap.png"></div>

> The top features were found for each category is given below.

<div align = "center">

|Parameter|Best Feature |
|---:|:---|
|Overall Performance|'Father edu'|
|Maths|'Help in household'|
|Reading|'Mother edu'|
|Science|'Father edu'|
|Social|'Help in household'|

</div>

> This concludes that the education of parents and whether they help in household were decisive in predicting a student's  performance.

#### Some interesting observations

* Some features are influential in the performance of certain subjects alone
    * Siblings <-> Reading %
    * Computer Use <-> Math %
    * Subjects <-> Science %
    * Give Language Hw <-> Math %
    * State <-> Math %
    * Correct Math HW <-> Math %
    * Correct Sci HW <-> Math %
* Certain features given below consistently stands out and are highly relevant factors irrespective of any subjects considered. Hence these features can be considered as a good performance predictors.
    * Father edu
    * Mother edu
    * Read other books
    * help in HouseholdFather occupation
    * Express science views
    * Express SocSci views
    * Solve science problems

#### Factors influencing average performance

Here we describe the process by which we calculated the scores for performance. A simillar treatment is used for calculating scores in each category in ('Maths %', 'Reading %', 'Science %', 'Social %')

> Among top features, 'Father edu' has distinctly high score for performance, almost **30%** higher than the second best feature indicating a very high relevance.


    count    180774.000000
    mean         38.095342
    std          14.949624
    min           0.000000
    25%          27.035000
    50%          35.640000
    75%          47.320000
    max         100.000000
    Name: performance, dtype: float64
    ======	Target Variable	: performance ======
    Best 5 Features:
     [('Father edu', 3906.8744966773766), 
     ('Mother edu', 3052.1893687615902), 
     ('Help in household', 2793.8799410412198), 
     ('Read other books', 2661.1779134014673), 
     ('Father occupation', 2428.0365114374408)]


<div align = "center"><img src="./index_files/f2_perfomance_score.png"></div>


> Since father education has the highest score, we decided to plot the performance set w.r.t 'Father edu' to explicitly see the influence. The plot shows an upward trend in the median performance %.


<div align = "center"><img src="./index_files/f3_perf_fath_edu.png"></div>

**Legend**

            Column                    Name Level          Rename
    24  Father edu        Degree and above     5  Degree & above
    25  Father edu              Illiterate     1      Illiterate
    26  Father edu          Not applicable     0  Not applicable
    27  Father edu           Primary level     2         Primary
    28  Father edu         Secondary level     3       Secondary
    29  Father edu  Senior secondary level     4    Sr secondary



### How do boys and girls perform across states?


<div align = "center"><img src="./index_files/output_19_0.png"></div>

> Among most states, Girls tend to have a higher median performance than boys.

Some states with notable exception to this rule are Jharkand (JH) and Bihar (BH). Since these state have high gender inequality, this trend could be due to lack of access to education to girls. To confirm, it has to be crosschecked with percentage of girls with access to education.

Of the states where girls perform better, Kerala and Delhi stands out. Both states showed that median % of girls is almost 4% better than boys.

<div align = "center"><img src="./index_files/output_20_0.png" width="45%"></div>

> Although the sample size vary across states, the sample size of boys and girls were almost equal within each state.

The figure shown above sumamrizes all the data based on gender difference. We used two axes for representing data for each state (1) Actual median performance (2) Difference in the median between boys and girls. The length of lines (from 0 at the center) represent the median values while the size of circles maps to sample size. The red and blue bar graph indicates difference with blue favouring girls and red favouring boys. 

### Do students from South Indian states really excel at Math and Science?

To determine this, we considered southern states as : "Andhra Pradesh", "Kerala", "Karnataka" and "Tamil Nadu". Meanwhile other states are referred to "the rest of the country". The performance score for 'Science and Math' is defined as the mean value of both 'Science' and 'Math'. 


<div align = "center"><img src="./index_files/output_30_0.png"></div>

> Both southern states and the rest of the country followed a simillar distribution even though the smaple size was differnt.

We found that central tendendencies of `Southern States` to be slightly lower than rest of the country. But it should be noted that number of samples in the `Southern States` is far less. Also, it should be understood that the enrollment rate of southern states is usually higher than rest of country which could be driving down the median values. Overall, it has to be concluded that south indian states perform badly compared to the rest of the country. The consclusions are based on unequal sample sizes as indicated by the size of the circles below each violin plot.

<div align = "center"><img src="./index_files/output_33_0.png"></div>

> Smaple size from Karnatake was small compared to other southern states but showed a wide range

To identify if all southern states follow this pattern, we split the data into corresponding southern state. We found that "Kerala" as a notable exception to the trend of southern states. "Kerala" tends to have higher median score than other southern states, rest of the country and the overall median of country. Another exception is the distribution of marks from "Tamil Nadu" with longer tails. "Tamil Nadu" followed the trend of the rest of the country with longer tails at highest end but has lower median score than all others. Although "Kerala" has a higher median, the distribution is narrower compared to other states.