# High-risk AI exercises

## Analytical: Empirical distribution MLE for health insurance claims prediction (*)

Assume that the binary random variable $(\mathbf{X},Y) = (X_0, X_1, Y)$ is defined as in the slides about predicting big-claims in health insurance.

For the empirical model, we assign a distinct parameter to each feature subgroup:
* **Parameters:** $\theta = (p_{1|00}, p_{1|01}, p_{1|10}, p_{1|11})$
* **Model:** $\hat{p}_\theta(1 | x_0, x_1) = p_{1|x_0 x_1}$

Let $S_{ij}$ be the set of $N_{ij}$ records with features $x_0=i$ and $x_1=j$. The negative log-likelihood decouples into independent sums for each subgroup:

$$
\ell_{ij}(p_{1|ij}) = - \sum_{n \in S_{ij}} \Big[ y_n \log(p_{1|ij}) + (1-y_n) \log(1 - p_{1|ij}) \Big]
$$

Show analytically that MLE is solved by

$$
\hat{p}_{1|ij} = \frac{1}{N_{ij}} \sum_{n \in S_{ij}} y_n
$$

## Computational: Empirical distribution MLE for health insurance claims prediction (*)

Write python or R code to compute maximum likelihood estimates for predicting big claims based on data samples at [../notebooks/data/big-claim-events.csv](../notebooks/data/big-claim-events.csv).

Comment on the results.

## Train, validation and test sets for MLE, empirical distribution (*)

Since there are no hyper-parameters to choose for the empirical distribution model, we combine train and validation datasets.

Calculate the empirical MLE model for the train-validation set of records from 2022 and 2023, and compare to a test set of records from 2024.

## Bootstrap statistics on the train-validation set for MLE, empirical distribution (**)

Use [empirical bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) to estimate the mean MLE parameters and their standard deviations on the train-validation set from above.

## Analytical: Decision tree number of parameters (*)

Show that the number of parameters of a decision tree for our binary random variable $(\mathbf{X},Y) = (X_0, X_1, Y)$ of big-claims prediction cannot exceed the number of parameters of the empirical distribution model.
