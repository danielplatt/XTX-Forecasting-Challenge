# XTX Markets Forecasting Challenge

## Description of the Challenge

The original challenge can be found here: https://github.com/correlation-one/XTXStarterKit.
The following description is taken from the README.md of that repository:
"The goal of this challenge is to create a program to predict stock movement based on real-market orderbook data. A dataset and some starter code has been provided to help build submissions."

## Solution to the Challenge

### trainForest.ipynb

A solution to the challenge can be found in trainForest.ipynb.
The file contains some basic data exploration, simple feature engineering, and the training of a random forest regressor using sklearn.

### forest-regressor-10-7.pckl

The trained random forest regressor with 10 estimators and maximum depth 7 is saved in forest-regressor-10-7.pckl.

### submission.py

A template for this file was provided by the competition.
The template was edited by loading the training forest regressor and using it to make the predictions.

### run_tester_python.py

This file was provided by the competition.
The files can be run using Python and will load submission.py to make some test predictions.

### Score of the Solution

The solution achieved an R2 score of 0.01781 on the test set.
The benchmark model achieve 0.03181 on the test set.
The solution placed top 100 among 3888 submissions but did not win any prize.
