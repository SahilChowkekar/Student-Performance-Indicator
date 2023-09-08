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
- [Microsoft Azure CICD Deployment with GitHub Actions](#microsoft-azure-cicd-deployment-with-github-actions)



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

![Student Performance Indicator Screenshot](https://github.com/SahilChowkekar/Student-Performance-Indicator/blob/master/img/Screenshot.png)



## Conclusion

- Summarized the key findings from the analysis.
- Highlighted the impact of various factors on student performance.


# Microsoft Azure CICD Deployment with GitHub Actions

This guide will walk you through deploying your web app to Azure Web App via Azure Container Registry. Please follow the steps carefully.

## Prerequisites
Before you begin, make sure you have the following prerequisites in place:
- An Azure account.
- Docker installed on your local machine.
- Your web app code hosted in a GitHub repository.

## Step 1: Log in to Your Azure Account
To log in to your Microsoft Azure account, visit https://portal.azure.com, enter your account email and password, and follow the authentication steps if applicable.

## Step 2: Create an Azure Container Registry
1. Navigate to the Azure portal.
2. Click on "Container Registries."
3. Create a new Azure Container Registry, filling in the required details.
## Step 3: Enable Admin User and Save Credentials
1. Inside your Azure Container Registry, go to "Access keys."
2. Enable the Admin user.
3. Save the login server and password as you'll need them later.
## Step 4: Build the Docker Image
1. Open your terminal.
2. Navigate to your web app project directory.
3. Build the Docker image with the following command:
```bash
docker build -t testdockersahil.azurecr.io/studentperformance:latest .
```
## Step 5: Login to Azure Container Registry
1. In your terminal, log in to the Azure Container Registry using the credentials you saved earlier:
```bash
docker login testdockersahil.azurecr.io
```
## Step 6: Push the Docker Image
1. Push the Docker image to the Azure Container Registry:
```bash
docker push testdockersahil.azurecr.io/studentperformance:latest
```
## Step 7: Create an Azure Web App
1. In the Azure portal, create a new Azure Web App.
2. Fill in the required details and select "Azure Container Registry" as the image source.
## Step 8: Deployment Center Configuration
1. After the deployment of your Azure Web App is complete, go to the "Deployment Center" in the Azure portal.
2. Click on "GitHub Action" under the "Source" section.
3. Fill in all the details, including your GitHub repository.
4. Be sure to update the workflow to use the updated **master_studentperformancecheck.yml** file.
## Step 9: GitHub Actions Deployment
1. Go to your GitHub repository.
3. Under the "Actions" tab, you will see the deployment happening.
3. After the deployment is successful, click on the "Evaluated Environment URL" to access your web app.
## Step 10: Accessing Your Web App
-  Alternatively, you can access your web app by going to your Azure Web App in the Azure portal and clicking on the "Browse" or "Default Domain" option.
\

These guidelines provide a step-by-step approach to deploying your Student Performance Indicator Web App to Azure Web App using Docker and GitHub Actions. Be sure to replace placeholders with your actual Azure and GitHub details. 




