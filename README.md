# predicting-roty-nba
Contributors: Mirza Abubacker and Shaheryar Haider\
Tools used: Python (BeautifulSoup, sklearntree), PowerBI\
(This README was not generated using an LLM, instead it was written by hand by Mirza) 

## NBA Rookie of the Year Prediction

# Overview
This repository contains a project that predicts the NBA Rookie of the Year using various technologies and data sources, including Python machine learning models, Excel for data preprocessing, and Python web scraping with BeautifulSoup for data collection.

# Technologies Used:
    - Python: Used for data scraping, data preprocessing, and machine learning.
    - BeautifulSoup: Used for web scraping NBA player statistics.
    - Excel: Used for data cleaning and preprocessing.
    - Visual Studio: Used for development and documenting code.
    - Scikit-Learn: Used for machine learning and model evaluation.

# Project Structure
    - data/: Contains the raw and preprocessed data files. The data was web-scrapped from RealGM. 
    - models/: Stores the trained machine learning models. Using a forest classifier model
    - scripts/: Python scripts for data scraping and other utilities.
    - README.md: This README file.

# Model Training and Evaluation
    - The script uses a Random Forest classifier to predict the NBA Rookie of the Year. 
    - Model accuracy is evaluated on a test set, and the results are printed to the console.

# Challenges
While working on this project, we faced a few challenges and hurdles such as incomplete data, outliers, and various  code breaks. For incomplete data, we had to import information from different key sources to fill in our missing gaps.For the outliers, we were able to manage to double-check the data with the different sources to have the correct data set on board. With the code breaks and errors, we were able to use stack overflow and fix up any issues with the code.
  
# Findings

# Conclusion
After running our machine learning model, our model predicts that Victor Wembanyama will be the Rookie of the Year in 2024.
  

# License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the content, but ensure you comply with the terms of the license.

