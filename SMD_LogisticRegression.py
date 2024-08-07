import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

raw_data = pd.read_csv("D:/Projects/Spam Mail Detection/mail_data.csv")

# replace all the null values and store it in mail_data
# it replaces the null values with NaN
mail_data = raw_data.where(pd.notnull(raw_data))

# Label encoding - replacing all the label with spam as 0 and ham as 1
mail_data.loc[mail_data['Category'] == 'spam','Category'] = 0
mail_data.loc[mail_data['Category'] == 'ham','Category'] = 1

X = mail_data['Message']
Y = mail_data['Category']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state= 4)

# Extracting feature with minimum document frequency 1..below 0 it will bo ignored
feature_extraction = TfidfVectorizer(min_df = 1, stop_words = 'english', lowercase = True)

# we will encounter some numerical value for the words by Term Frequency - Inverse document frequency
X_train_features = feature_extraction.fit_transform(X_train)

# We dont want our model to look at our testing data, So We need not want to fit
X_test_features = feature_extraction.transform(X_test)

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

model = LogisticRegression()
model.fit(X_train_features,Y_train)

predicted_Y_values_train = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, predicted_Y_values_train)
print("Accuracy on Training data : ",accuracy_on_training_data)

predicted_Y_values_test = model.predict(X_test_features)
accuracy_on_testing_data = accuracy_score(Y_test,predicted_Y_values_test)
print("Accuracy on Testing data : ",accuracy_on_testing_data)


#Building a predictive model

Mail = ["Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030"]

Mail_Features = feature_extraction.transform(Mail)
prediction = model.predict(Mail_Features)
print(prediction)

#Visulaizing our data how they change in each step
print(X)
print("__________________________________________________________________________")
print(X_train)
print(X_train_features)
print("___________________________________________________________________________")
print(Y)
print("___________________________________________________________________________")
print(Y_train)

# plt.plot(feature_extraction)

if (prediction == 1):
    print("It is not a spam Mail.")
else:
    print("Its a spam Mail.")

