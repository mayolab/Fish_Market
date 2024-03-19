# Fish Species Prediction Model

## Overview
This project aims to predict the species of a fish based on various measurements such as its width, height , lenghts and weight. The model was initially built using a Decision Tree classifier, but after comparing it with a Random Forest classifier, RFC was found to be more accurate.

## Model Details
The final model is a Random Forest classifier with `n_estimators=100`. The `random_state` parameter was set to `42` to ensure the results are reproducible. The model achieved an accuracy of `0.78125` on the test data.

## Data
The model takes the following measurements as input:
- Weight
- Length1
- Length2
- Length3
- Height
- Width


The output is the predicted species of the fish.

