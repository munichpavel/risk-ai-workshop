# Introduction to AI, risk management and regulation exercises

These exercises are mainly to get your laptop (or possibly Google Colab) environment set-up.

You are free to use python or R to complete any exercise of this workshop.

## Data wrangling: `big-claim-events.csv` (*)

Load into your favorite data frame (R, pandas, polars, ...) the data [../notebooks/data/big-claim-events.csv](../notebooks/data/big-claim-events.csv), and for each of the four sub-populations defined by $\textrm{skin-cancer}=i, \textrm{depression}=j$, where $i,j \in \{0, 1\}$, calculate the ratio of big-claims to total claims for the sub-population.

## Data quality: `aggregate-claim.csv` (*)

Load into some data frame [../notebooks/data/aggregate-claim.csv](../notebooks/data/aggregate-claim.csv). Identify at least one potential data quality issue.

Hint: There are some convenient data profiling tools for both python (e.g. [fg-data-profiling](https://github.com/Data-Centric-AI-Community/fg-data-profiling), formerly `ydata-profiling`, formerly-er `pandas-profiling`) and R (e.g. [DataExplorer](https://cran.r-project.org/web/packages/DataExplorer/vignettes/dataexplorer-intro.html)).