# Risk, Artificial Intelligence and Discrete Geometry

![ci](https://github.com/munichpavel/risk-ai-workshop/actions/workflows/ci-cd.yml/badge.svg)

## Quick-start

* `git clone` the repository and `cd` into the root directory.
* For the exercise Jupyter notebooks
  * create a virtual environment (recommended)  e.g. with [venv](https://docs.python.org/3/library/venv.html), [conda](https://docs.conda.io/en/latest/) or other.
  * install python dependencies with `pip install -r requirements.txt` in a virtual environment. Note: the [fake-data-for-learning package](https://github.com/munichpavel/fake-data-for-learning) has some non-python dependencies; see its [installation instructions](https://github.com/munichpavel/fake-data-for-learning/blob/main/README.md#installation).

## Workshop topics

Slides are built as part of the repo's [ci-cd pipeline](.github/workflows/ci-cd.yml), and be found under [releases](https://github.com/munichpavel/risk-ai-workshop/releases). See e.g. [the v2022.1.1 release](https://github.com/munichpavel/risk-ai-workshop/releases/tag/v2022.1.1).

## Artificial intelligence for risk management

[Examples and exercises](notebooks/introduction-examples-exercises.ipynb)

## Discrete geometry for risk

Examples and exercises: [graphical models](notebooks/graphical-models-exercises.ipynb), [probability polytopes](notebooks/probability-polytope-exercises.ipynb), and [simpson's paradox](notebooks/simpsons-paradox-examples-exercises.ipynb)

## Correlation and causality

[Examples and exercises](notebooks/causal-models-exercises.ipynb)

## Risk and Artificial Intelligence in practice

* [Model Selection Examples](notebooks/model-selection-examples.ipynb)
* [Risk and AI in Practice Exercises](notebooks/risk-ai-practice-exercises.ipynb)
* [Model Selection Exercises (from 2017 workshop)](notebooks/model-selection-exercises.ipynb)

## Grading scheme for University of Ljubljana Masters in Mathematical Finance

The number of points for a correct solution for each exercise brings is equal to $2^{\mathrm{number\,of\,stars}}$. For a grade of 8 you have to get at least 6 points, for grade 9 at least 7 points and for 10 at least 8 points.

You have to solve one problem from each of the four sets of problems unless you solved one of the problems with three stars.

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

Note: I do not follow [Semantic Versioning](https://semver.org/) for this project. For the first digit (in semver, `major`), I use the year of the target workshop, and for the last (in semver `patch`), I increment when a chunk of work is done towards giving the workshop. The middle digit (in semver, `minor`) stays on 0 until I give the workshop, when it bumps to 1. Fixes to the given workshop get reflected in the patch versions `yyyy.1.<patch-version>`.

### Latest

Replace slide publishing workaround with instructions on accessing compiled slides under releases.

### v2022.1.1

* Fix typos in discrete geometry slides, including definition of d-separation
* Fix hit-rate average treatment effect results in slides
* Add ci / cd release step to make ci / cd slide artifacts publicly available

### v2022.1.0

Refactor introduction and concluding lectures, as well as their exercises

Add simpson's paradox content and exercises to the discrete geometry lecture

Add ci tests of package and notebooks for mac and windows (latest) operating systems

### v2022.0.2

Add github actions workflow for automated testing, with unit, notebook-run and latex-slides-build

Add github actions job for continuous delivery of slide artifacts

Add example of model selection pipeline for artificial credit scoring data

### v2022.0.1

Add initial exercises and methods for Simpson's paradox.

### v2020-02-uni-lj

Created prior to the above versioning scheme, workshop at University of Ljublana in February, 2020.
