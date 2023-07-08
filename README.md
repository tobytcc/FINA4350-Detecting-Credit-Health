## Abstract
Our project aims to answer the following question: **Can publicly available information detect deteriorating credit health in advance?** There is a wealth of information regarding quantitative indicators and projections surrounding fixed income investments, but we believe financial institutions fail to utilise qualitative information sufficiently in such predictive models. Recent advancements in NLP and text analytics allow for underlying factors in such areas to be scraped, quantified, and analyzed readily, and we aim to highlight how qualitative information from credit agencies and firms can provide information on impending changes to a firm's financials and bond drivers. 

## Approach
We have chosen to analyse the real estate sector in China, particularly around its collapse in 2019. We aim to backtest signals from qualitative documents, investigating how such documents could have predicted the impending collapse in corporate bonds. This event was triggered by rating changes given equity overvaluations, unsustainable debt levels, and most importantly, failure to meet the "Three Red Lines" policy - all events that were outlined through text in rationales for rating downgrades.

Example for rating reports can be found [here](https://www.moodys.com/research/Moodys-downgrades-Evergrandes-bond-rating-to-B2-outlook-negative--PR_212356).

We scraped such reports and quantified them through n-gram vectorization. We then chose to run a two-pronged approach to analysis and modelling:
1. running a k-means unsupervised machine learning model - We then applied our model to annual reports from such companies from 2019-2022, identifying similar word patterns and allowing our model to predict risks of collapse. 
2. calculating SCM similarity scores through vector geometry - We also applied these scores to annual reports, calculating similarity scores. High similarity scores meant similar patterns were detected in annual reports, theoretically predicting a high rate of collapse.

## Results
Full results can be found in our [Final Report](Final%20Report.pdf).

#### K-means Clustering Approach:
From visual inspection, we can observe 5 clusters of words, with center points of each cluster highlighted in larger grey circles. The clusters are quite distinct and far apart, representing an effective separation of groups of words in our training set. We then manually inspected each cluster to see which cluster is closely related to default, picking cluster 0 and 4. 

![Results from K-means Clustering Approach](/Images/clustering%20approach%20results.jpg)

#### SCM Similarity Approach:
As seen below, some of the words such as “dollar” or “experienced” don’t give much meaning in the context of analyzing credit downgrades. This shows that even after obtaining results, we must manually filter irrelevant words from the dataset, in other words, removing noise. Regardless, there are words that are highly relevant to downgrades. 

![Results from SCM Similarity Approach](/Images/similarity%20approach%20results.jpg)

#### Final Results:
Based on our assessment of 53 MD&A (Management Discussion and Analysis) reports, our model can reasonably detect credit deterioration in company documents. All documents showed a degree of similarity between 50-80%, and mostly fell into clusters 0 and 4. The reports with the highest similarity scores within the correct clusters belong to a set of companies that suffered significant setbacks towards their credit situation during the Chinese Real Estate crisis.Our results also show that both of our approaches have generated coherent results. The documents that show the highest similarity scores all originate from clusters 0 and 4, which matched our manual judgement of clusters. All generated similarity scores also fell within a reasonable band, which suggests our analysis was conducted properly and efficiently. 

![Final Results from testing data from MD&A Section of Annual Reports](/Images/final%20results.jpg)

#### Future Implications
We believe our project idea can be applied to many aspects of financial valuation, investigation, and research. The development of improved credit health valuation helps rating agencies improve in accuracy of their reports and ratings, and reduces information asymmetry and investors can make more rational predictions with qualitative information. Asset managers and investment firms can improve their scope of valid improvement strategies, and provide research and quantitative measurements as credit health becomes more quantifiable.

## Instructions
1. main-scrape.py to scrape, pre-process and transform data 
2. clustering-approach to run k-means approach
3. similarity-approach to run SCM similarity scores

FORMATTING for data files must be followed:
- training data formatting in downgrade-reports.csv
-   testing data formatting in 4-30_testingdata_v2.csv

## Future Improvements
- The project is limited in scope to the collapse of the Chinese property sector in 2019. However, the infrastructure for this idea can be implemented in any sector and time period, given the resources to collect such data. It can be interesting to see the underlying qualitative factors that influence credit/fixed income investments in other sectors and geographies.
- Our project takes a very heavy-handed approach, focusing on creating a proof-of-concept that neglected efficiency and scalability. The code can be refactored and optimised, and the data pipeline streamlined to provide a more efficient solution, particularly for larger databases.

## Project Members
We are a team of students from the University of Hong Kong (HKU), conducting this project under the guidance of Dr. Matthias Buehlmaier for *FINA4350 - Text Analytics and Natural Language Processing for Finance and Fintech.*
For more info about this project, please click [here](https://buehlmaier.github.io/FINA4350-student-blog-2023-01/).

Group Lead: Toby Chiu

Group Members:
- Steven Lu
- Lawrence Chan
- Fiona Li
- Lawrence Wan
