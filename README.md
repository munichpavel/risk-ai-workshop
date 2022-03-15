# Risk, Artificial Intelligence and Discrete Geometry

![ci](https://github.com/munichpavel/risk-ai-workshop/actions/workflows/ci.yml/badge.svg)

## Quickstart

* `git clone` the repository and `cd` into the root directory.
* For the exercise Jupyter notebooks
  * create a virutual environment (recommended)  e.g. with [venv](https://docs.python.org/3/library/venv.html), [conda](https://docs.conda.io/en/latest/) or other.

  * install python dependencies with `pip install -r requirements.txt` in a virtual environment,  Requires libglpk-dev for `fake_data_for_learning`.

## Workshop topics

## Artificial intelligence for risk management

* [Slides](slides/ai-for-risk)
* [Examples and exercises](notebooks/model-selection-exercises.ipynb)

## Discrete geometry for risk

* [Slides](slides/discrete-geometry)
* Examples and exercises: [graphical models](notebooks/graphical-models-exercises.ipynb), [probability polytopes](notebooks/probability-polytope-exercises.ipynb)

## Correlation and causality

* [Slides](slides/correlation-causality)
* [Examples and exercises](notebooks/causal-models-exercises.ipynb)

## [Artificial intelligence in practice](slides/ai-in-practice)

## Relate python packages

In the exercise notebooks and `requirements.txt` you see which python packages I used in creating and solving the exercises, though this list is far from exhaustive. Below are some (additional) python packages that may be useful

## Graph visualization

* [graphviz](https://graphviz.readthedocs.io/en/stable/)
* [networkx](https://networkx.github.io/), plus many graph operations

## Bayesian networks, causal inference

* [pgmpy](https://pgmpy.org/)
* [brent](https://koaning.github.io/brent/)
* [causalgraphicalmodels](https://github.com/ijmbarr/causalgraphicalmodels)
* [causality](https://github.com/akelleh/causality)
* [dowhy](https://microsoft.github.io/dowhy/)
* [pyro](https://pyro.ai/)

## Releases

I follow a semantic-versioning-like convention for releases of `<workshop-year>.<minor>.<patch>`. For now, the `minor` value will be an incrementing integer; as the module being developed in this repo is not planned to be pushed to [pypi](https://pypi.org/), I won't be very strict, and will likely keep `minor` at 0 even if the api changes. If it looks like I would ever give more than one workshop a year, the `minor` value could be used for the month of the workshop.

### Process of creating a new workshop release

If the release is for a new workshop year, then first manually change the version in the code-base to `<new-year>.0.0`. This release need not be a tagged release, as it is the same as the final release of the previous workshop in an earlier year.

Once an initial release has been created for a new workshop, create subsequent tagged releases by using [bump2version](https://pypi.org/project/bump2version/).

## Release history

### Latest

Add github actions workflow for automated testing, with unit, notebook-run and latex-slides-build

Add github actions job for continuous delivery of slide artifacts

### v2022.0.1

Add initial exercises and methods for Simpson's paradox.

### v2020-02-uni-lj

Created prior to the above versioning scheme, workshop at University of Ljublana in February, 2020.
