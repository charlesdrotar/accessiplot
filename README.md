# accessiplot

![Github Actions Status](https://github.com/charlesdrotar/accessiplot/actions/workflows/python-app.yml/badge.svg)
![Supported versions](https://img.shields.io/badge/python-3.8+-blue.svg)
[![Documentation Status](https://readthedocs.org/projects/accessiplot/badge/?version=latest)](https://accessiplot.readthedocs.io/en/latest/?badge=latest)

A python library to enhance the accessibility of matplotlib plots

## Install using a new Anaconda environment
We need to install 3.8+ because we are forcing matplotlib 3.7.0+ which requires that version of python.

```
conda create -n "accessiplot" python=3.8.0

conda activate "accessiplot"

cd </path/to/repo/>

python setup.py install
```

## Run tests

From base of repo:

```
pip install -r test_requirements.txt

pytest -v --durations=20 --cov-config .coveragerc --cov accessiplot -p no:logging --cov-fail-under=85
```

## Build the docs

From `docs/`:

```
make clean html

sphinx-build -b html docs/ docs/build/html
```

## Check linting of files

From base of repo:

```
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```