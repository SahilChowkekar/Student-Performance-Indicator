# Student Performance Indicator 





## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Technology Used](#technology-used)
- [Installation](#installation)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Preview of Student Performance Indicator ](#preview-of-student-performance-indicator)
- [Conclusion](#conclusion)


## Introduction

This project aims to understand and analyze student performance (test scores) based on various variables such as gender, ethnicity, parental level of education, lunch type, and test preparation course. Additionally, it includes the implementation of machine learning models to predict student math scores based on these variables.


## Dataset

The dataset used for this project is sourced from Kaggle and contains the following columns:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

You can access the dataset here: [Student Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)


## Technology Used

The following technologies were used in this project:

- Python
- Jupyter Notebook
- NumPy
- pandas
- scikit-learn
- Matplotlib
- Seaborn
- FastAPI



## Installation
1. Clone the repository:
```bash
git clone https://github.com/SahilChowkekar/Student-Performance-Indicator.git

```

2. Navigate to the project directory:
```bash
cd Student-Performance-Indicator

```
3. Create a conda environment after opening the repository:
```bash
conda create -n student-performance-env python=3.8 -y
```

4. Activate the conda environment:
```bash
conda activate student-performance-env
```
5. Install the required dependencies:
```bash
pip install -r requirements.txt
```

6. Finally, run the following command to start the application:
```bash
python app.py
```

7. Open your preferred web browser and visit:
```bash
http://127.0.0.1:5000

```


## Data Preprocessing

- Checked for missing values (there were none).
- Checked for duplicates (there were none).
- Examined data types and converted categorical columns using one-hot encoding.
- Created new features like "Total Score" and "Average" for analysis.

## Exploratory Data Analysis

- Explored the distribution of scores and other variables.
- Visualized data using various plots such as histograms, bar plots, and pie charts.
- Identified insights and correlations between variables.

## Model Training

- Trained several machine learning models, including Linear Regression, Lasso, Ridge, K-Neighbors Regressor, Decision Tree Regressor, Random Forest Regressor, XGBRegressor, CatBoost Regressor, and AdaBoost Regressor.
- Split the data into training and testing sets.
- Evaluated model performance using metrics like Mean Absolute Error, Root Mean Squared Error, and R-squared (R2) score.

## Model Evaluation

- Assessed the performance of each model on both the training and testing datasets.
- Analyzed which model performed the best for predicting math scores.





## Preview of Student Performance Indicator 

Here's a preview of the Student Performance Indicator in action:

![Student Performance Indicator Screenshot](images/text-summarizer-screenshot.png)



## Conclusion

- Summarized the key findings from the analysis.
- Highlighted the impact of various factors on student performance.