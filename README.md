[Insights from this project](https://bibinmjose.github.io/dsgramner/) 

## Setup

To reproduce the project clone the repository: 
`git clone https://github.com/bibinmjose/dsgramner.git`

The [ipython notebook](https://bibinmjose.github.io/dsgramner/ipython.html) is in root folder and can be opened in python3.

`jupyter-notebook National\ Achievement\ Survey.ipynb`

### Dependencies
The packages used include :
* `pandas`
* `numpy`
* `seaborn`
* `sklearn`
* `matplotlib`


## Data and Documentation

All the major documentation of this project can be accessed from the markdown file or the html in folder `docs`.

Datasets used for analysis is provided by "Gramener" and can be found in `gramener-usecase-nas`. Te dataset is based on the national achievement survey conducted by NCERT for 8th grade students.

## Model

Since inference is the goal of the questions asked, a linear model is a good choice than a complex one.

To run the model, `cd` into `/model`
and run `python3 LR_model.py`