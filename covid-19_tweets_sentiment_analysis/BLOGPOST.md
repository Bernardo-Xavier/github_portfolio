# Sentiment Analysis on COVID-19 Tweets: A Deep Dive into NLP Techniques

## Introduction
In the wake of the COVID-19 pandemic, social media platforms like Twitter have become a rich source of public sentiment. Analyzing this sentiment can provide valuable insights into public opinion and emotional responses during the crisis. In this project, we explore various Natural Language Processing (NLP) techniques to classify COVID-19-related tweets into different sentiment categories.

## Dataset Overview
The dataset used in this project contains COVID-19-related tweets, each labeled with a sentiment category: Positive, Negative, Neutral, Extremely Positive, or Extremely Negative. The dataset includes columns such as `UserName`, `ScreenName`, `Location`, `TweetAt`, `OriginalTweet`, and `Sentiment`.

## Methodology
### 1. Data Visualization
We started by visualizing the dataset to understand the distribution of sentiment labels and the length of tweets. Word clouds were generated to highlight the most frequent words in the tweets.

### 2. Text Cleaning
Text cleaning is a crucial step in NLP. We employed two different approaches to clean the text data, ensuring it was free from noise and ready for model training.

### 3. Model Implementation
We implemented several neural network models, including TPNs, CVNs, and RLS TV, each with different optimizers such as SGD and Adam. These models were trained on the cleaned dataset to classify the tweets based on sentiment.

### 4. Model Comparison
After training, we compared the performance of all models. The RLS TV model emerged as the best performer, achieving the highest accuracy in sentiment classification.

## Results and Discussion
The RLS TV model demonstrated superior performance, highlighting the effectiveness of advanced neural network architectures and optimizers in text classification tasks. The visualizations provided clear insights into the distribution of sentiments and the impact of text cleaning on model performance.

## Conclusion
This project underscores the importance of NLP techniques in analyzing public sentiment during global crises. The successful implementation of various neural network models and optimizers provides a robust framework for future text classification tasks.

## Future Work
Future work could involve exploring more advanced models, such as transformers, and expanding the dataset to include more diverse sources of text data. Additionally, real-time sentiment analysis could be implemented to provide ongoing insights into public opinion.

## References
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [NLTK Documentation](https://www.nltk.org/)