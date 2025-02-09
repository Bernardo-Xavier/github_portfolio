# NLP Text Classification Project: Sentiment Analysis on COVID-19 Tweets

## Overview
This project focuses on sentiment analysis of COVID-19-related tweets using various Natural Language Processing (NLP) techniques and neural network models. The goal is to classify tweets into sentiment categories such as Positive, Negative, Neutral, Extremely Positive, and Extremely Negative.

## Dataset
The dataset contains text data related to COVID-19, including columns such as `UserName`, `ScreenName`, `Location`, `TweetAt`, `OriginalTweet`, and `Sentiment`. The dataset is divided into a training set and a test set.

## Project Structure
1. **Dataset Definition**: The dataset is loaded and explored to understand its structure and content.
2. **Visualization**: The distribution of sentiment labels and tweet lengths is visualized using word clouds and bar plots.
3. **Text Cleaning**: Two different approaches are used to clean the text data, ensuring it is suitable for model training.
4. **Model Implementation**: Various neural network models (e.g., TPNs, CVNs, RLS TV) are implemented with different optimizers (e.g., SGD, Adam).
5. **Model Comparison**: The performance of all models is compared, with the RLS TV model achieving the highest accuracy.
6. **Conclusion**: The project demonstrates the effectiveness of different neural networks and optimizers for text classification tasks.

## Requirements
- Python 3.x
- Libraries: pandas, matplotlib, sklearn, tensorflow, nltk, wordcloud

## Results
The RLS TV model achieved the highest accuracy among the tested models. Detailed results and visualizations are provided in the project notebook.
