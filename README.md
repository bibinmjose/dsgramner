[Insights](https://bibinmjose.github.io/dsgramner/)  from this project

[Github repo](https://github.com/bibinmjose/dsgramner) for the project.

## Setup

To reproduce the project clone repository: 
`git clone https://github.com/bibinmjose/dsgramner.git`

unzip `gramener-usecase-nas.zip` to root folder `/dsgramner` if doesn't exist

Original ipython notebook is in root folder while an html redering can be accessed from [**here**](https://bibinmjose.github.io/dsgramner/ipython_md/analysis.html).

`jupyter-notebook National\ Achievement\ Survey.ipynb`

Execute all the cells in jupyter notebook

raw `.html` of ipython notebook can be found at root folder as well.

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
and run `python LR_model.py`

## To Do
- [X] Make a simple linear model
- [ ] Split each categorical variable into its own category in the linear model.

By [Bibin Jose](https://bibinmjose.github.io/)
