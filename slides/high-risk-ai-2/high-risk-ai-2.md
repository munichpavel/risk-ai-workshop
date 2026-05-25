---
theme: gaia
paginate: true
author: Dr. Paul Larsen
backgroundColor: #fff
_class: lead
style: |
  .small-text {
    font-size: 0.5rem;
  }
  .ms-text {
    font-size: 0.75rem;
  }
  section.split {
    overflow: visible;
    display: grid;
    grid-template-columns: 500px 500px;
    grid-template-rows: auto 1fr;   /* Auto for heading, 1fr for content to fill space */
    grid-template-areas:
        "slideheading slideheading"
        "leftpanel rightpanel";
    gap: 20px; /* Optional: adds some space between columns and rows */
    height: 100%; /* Ensure section takes full slide height */
  }
  section.split h2 {
    grid-area: slideheading;
    font-size: 50px; /* Adjust as needed */
    text-align: center; /* Optional: center the heading */
  }

  section.split .ldiv {
    grid-area: leftpanel;
    width: 500px;
    font-size: 30px;
  }

  section.split .rdiv {
    grid-area: rightpanel;
    width: 500px;
    font-size: 30px;
  }

  blockquote.small {
    font-size: 0.6em;
  }
  section.math-heavy {
    font-size: 28px; /* Smaller base for this slide class */
  }

  section.math-heavy h2 {
    font-size: 40px; /* Scaled down header */
  }
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>
<!-- paginate: false -->
## Management of high risk AI, II


Dr. Paul Larsen
Head of Data and AI, Korapis d.o.o.
[paul-larsen-data-ai.com](https://paul-larsen-data-ai.com)

<br>

![h:40px center](../graphics/KORAPIS-color.jpg)

---
<!-- paginate: true -->
## Outline

* ~~High-risk in the AI Act (this session)~~
* ~~Optimization and discriminative ML (this session)~~
* Health insurance segmentation: empirical, logistic regression and decision trees
* Reflections on AI definition and model transparency

---
## Are data science fun and games over?

(Tech + algorithm)-first fun and games:

* Kaggle competition-like optimization of technical metrics
* Algorithm first, data semantics & quality last
* ML is all you need

<div style="text-align: center;">
<a title="John Grabill, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Grabill_-_The_Cow_Boy.jpg"><img width="256" alt="Grabill - The Cow Boy" src="graphics/Grabill_-_The_Cow_Boy.jpeg"></a>
</div>
<div style="text-align: center;">
<p class="small-text">
Source: <a href="https://commons.wikimedia.org/wiki/File:Grabill_-_The_Cow_Boy.jpg">File: The Cow Boy, John Grabill, Public domain, via Wikimedia Commons</a>.
</p>
</div>

---
## Document and justify high-risk decisions and practices

<!-- _class: split -->
<div class=ldiv>

<ol class="ms-text">
<li>Data quality and governance (Article 10)</li>
<li>Technical documentation (Article 11)</li>
<li>Record keeping (Article 12)</li>
<li>Transparency and provision of information regarding operation (Article 13)</li>
<li>Accuracy, robustness and cybersecurity (Article 14)</a>
</ol>

</div>
<div class=rdiv>

### Recall: AI systems vs non-AI software

Main ingredients of AI systems

<ol class="ms-text">
<li><b>Historical data</b> relevant to business domain</li>
<li><b>Optimization algorithms</b> to find best parameters from data</li>
<li><b>Human decisions</b> about data selection, algorithms, "best," ...</li>
</ol>

![h:300 center](graphics/data-opt-human-to-ai-black.png)
</div>

---
## AI Act data governance

<style scoped>
blockquote {
  font-size: 0.6em;
}
</style>


From Article 3, Definitions:

> (29) 'training data' means data used for training an AI system through fitting its learnable parameters;
>
> (30) 'validation data' means data used for providing an evaluation of the trained AI system and for tuning its non-learnable parameters and its learning process in order, inter alia, to prevent underfitting or overfitting;
>
> (31) 'validation data set' means a separate data set or part of the training data set, either as a fixed or variable split;
>
> (32) 'testing data' means data used for providing an independent evaluation of the AI system in order to confirm the expected performance of that system before its placing on the market or putting into service;

---
## AI Act data governance

Article 10 of high-risk section:

* training, validation and testing sets must meet use-cases specific quality criteria
* requirements about proper
   * *design*: is choice of splits defensible?,
   * *processing*: are labeling, cleansing, enrichment, aggregation steps robust?, and
   * *semantics*: are chosen data fields meaningful

---
## Why split historical data?

To minimize the fitted model's error on data samples not present in history $\to$ minimize **generalization error**.

In linear regression with mean-squared error, generalization error decomposes as `bias + variance + irreducible-error`.

* *High Bias (underfitting)*: The model family is too rigid or simple to capture the underlying data generating process.
* *High Variance (overfitting)*: The model is too sensitive and memorizes the historical noise of the training sample.

**Role of data splitting**:
* *Train Set*: Fits the model parameters (drives bias down).
* *Validation Set*: Tunes model complexity to find the optimal tradeoff between bias and variance.
* *Test Set*: A strictly held-out sample to provide an unbiased estimate of final generalization error.

---
## Data splitting (and more) in practice

Example: before "predicted" big-claim or not $\to$ sort customers into 2 group. New task: find m


---
<!-- _class: math-heavy -->
## Beyond a single split: $k$-fold cross-validation

When historical data is limited ...

**$k$-fold validation for hyperparameter tuning:**
* *Partition*: Divide the non-test data into $k$ equal-sized, disjoint folds.
* *Iterate*: For a given hyperparameter set, train the model $k$ times. In iteration $i$, validate on fold $i$ and train on the remaining $k-1$ folds.
* *Aggregate*: Average the $k$ validation errors to estimate the **generalization error** for that specific hyperparameter configuration.
* *Select & Retrain*: Choose the hyperparameters that minimized the estimated generalization error, then retrain the final model on the **entire** non-test dataset.
* *Test*: Evaluate this final model once on the hold-out Test set to report the true generalization error.