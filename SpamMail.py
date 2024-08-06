import string                                         #remove punctuations from the sentence
import pandas as pd
import numpy as np

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

nltk.download(stopwords)

df = pd.read_csv("D:/Projects/Spam Mail Detection/spam_ham_dataset.csv")


