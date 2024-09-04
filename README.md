# Laptop Price Prediction

This repository contains a project aimed at predicting laptop prices using machine learning techniques. The project involves data preprocessing, feature engineering, and model testing using Streamlit for the user interface.

## Introduction
The goal of this project is to predict the prices of laptops based on various features such as brand, specifications, and other attributes. This can help me to understand more about machine learning and how it works.

## Dataset
The dataset used in this project contains various features of laptops, including:
- Brand
- Model
- Processor
- RAM
- Storage
- Screen Size
- Graphics card
- screen type
- Operating system
- Price

## Feature Engineering
Feature engineering steps include:
- Handling missing values
- Encoding categorical variables
- Scaling numerical features

## Modeling
We used Scikit-learn to build and test the model. The following steps were performed:
1. Data splitting into training and testing sets
2. Model selection and training
3. Model evaluation using metrics such as Mean Absolute Error (MAE) and R2_score

## Streamlit App
We developed a Streamlit app to provide an interactive interface for users to input laptop features and get price predictions. The app includes:
- Input fields for laptop features
- A button to generate predictions
- Display of predicted price

## Results
The model's performance was evaluated, and the results are as follows:
- Mean Absolute Error: 0.1583724829037032
- R2_Score: >= 86.56

## Installation
To run this project, you need to have Python installed along with the following libraries:
- pandas
- numpy
- scikit-learn
- streamlit

You can install the required libraries using:
```bash
pip install pandas numpy scikit-learn streamlit'''

Big credit to CampusX with there video to understand the project in depth 
