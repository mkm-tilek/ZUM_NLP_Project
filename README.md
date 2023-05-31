# ZUM_NLP_Project

### In this project was performed sentiment analysis based on tweets about war.

Datasets of 200k tweets collected with <b>snscrapper</b> library:
<link>https://github.com/JustAnotherArchivist/snscrape</link>


## Initialization
Open and run scrapper.py file in:
<code>/scripts/scrapper.py</code>
Scripts collects tweets about war in period of 2020-01-01 - 2023-03-01. All collected datasets will be stored in folder <code>/data</code>

## Order of execution
Open file tasks_1_5.ipynb <code>/scripts/tasks_1_5.ipynb</code> and run code blocks sequentially. All main stages of project are done in this file.

## Project contains:
#### STAGE 1: DATA COLLECTION
Snscraper, Data cleaning: normalisation, special characters removal, punctuation, URL, emails, duplicates, lowercase text and choose type of tokenizer.

#### STAGE 2: CLASSIC ML
  3 models to fit dat:
  Logistic Regression,
  DecisionTree Classifier,
  RandomForest Classifier
  
#### STAGE 3: NEURAL MODEL
LSTM effective for text processing tasks.

#### STAGE 4: LANGUAGE MODEL
DistilBERT generates contextualized word embeddings.
