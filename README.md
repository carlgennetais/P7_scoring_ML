# P7_scoring_ML

<!--toc:start-->
- [Context](#context)
- [Description](#description)
- [Usage](#usage)
- [Install](#install)
- [Makefile](#makefile)
- [Project Organization](#project-organization)
- [Credits](#credits)
- [Screenshots](#screenshots)
<!--toc:end-->


## Context
School project #7 with OpenClassrooms

## Description
API providing financial data about customers and their loan application results. The project is split in 3 github repositories:

1. [Machine learning](https://github.com/carlgennetais/P7_scoring_ML) (this one)
2. [Back: API built with FastAPI](https://github.com/carlgennetais/P7_scoring_back)
3. [Front: Dashboard built with Streamlit](https://github.com/carlgennetais/P7_scoring_front/)


## Usage
Visit the live URL : <https://p7-carl-demo.streamlit.app/>


## Install
```
$ make requirements
$ make data
```

## Makefile
```
Available rules:
clean               Delete all compiled Python files 
clean_code          Clean notebooks and python fils with black and isort 
create_environment  Set up python interpreter environment 
data                Make Dataset 
lint                Lint using flake8 
requirements        Install Python Dependencies 
test_environment    Test python environment is setup correctly 
update_API_models   Copy models to local repo of API 
```

## Project Organization

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- This README
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── img                <- image folder
    │
    ├── models             <- Trained model and shap explanation
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        └── features       <- Scripts to turn raw data into features for modeling
            └── lightgmb_with_simple_features.py      <- Kaggle Kernel


## Credits

* [Aguiar from Kaggle](https://www.kaggle.com/code/jsaguiar/lightgbm-with-simple-features/) for his Feature Engineering work
## Screenshots

![](./img/homepage.png)
![](./img/example_granted.png)
![](./img/shap_example_1.png)
![](./img/shap_example_2.png)

