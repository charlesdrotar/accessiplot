# accessiplot
A python library to enhance the accessibility of matplotlib plots

## Install using a new Anaconda environment
We need to install 3.8+ because we are forcing matplotlib 3.7.0+ which requires that version of python.
`conda create -n "accessiplot" python=3.8.0`

`conda activate "accessiplot"`

`cd </path/to/repo/>`

`python setup.py install`

## Run tests

From base of repo:
`pip install -r test_requirements.txt`

`pytest -v --durations=20 --cov-config .coveragerc --cov accessiplot -p no:logging`