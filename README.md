<H1>Spam Mail Detection with Logistic Regression.<H1>
<p>This project demonstrates how to build a spam mail detection model using machine learning. The model is built using logistic regression and TF-IDF vectorization. Here’s a step-by-step explanation of how I implemented this project</p>
<H2>1. Importing Necessary Libraries</H2>

![image](https://github.com/user-attachments/assets/5ebba0be-117b-4368-9246-a4d9af533140)

<H2>2. Loading the Dataset</H2>

![image](https://github.com/user-attachments/assets/8ad74b0c-395a-4c97-aaa6-aa7beab8a7dc)

<H2>3. Handling Missing Values</H2>
<p>To handle any missing values in the dataset, I replaced them with NaN using pandas.notnull() function.</p>

![image](https://github.com/user-attachments/assets/7c9d2b0d-d4e1-4ecb-a53b-235b0b3f8e17)
<H2>4. Label Encoding</H2>
<p>I encoded the labels by replacing 'spam' with 0 and 'ham' with 1.</p>
![image](https://github.com/user-attachments/assets/296640ab-ede6-49a7-87cc-6fb78c1198a9)

<H2>5. Separating Data and Labels</H2>
<p>I separated the data (messages) and labels (categories).</p>
![image](https://github.com/user-attachments/assets/3982df5f-1e58-4430-8137-b9a9831313bc)

<H2>6. Splitting the Data</H2>
<p>I split the dataset into training and testing sets using an 80-20 split.</p>
![image](https://github.com/user-attachments/assets/3bcd8c90-919e-4906-95fa-72359d72560a)

<H2>7. Feature Extraction using TF-IDF Vectorizer</H2>
<p>I used TfidfVectorizer to convert text data into numerical features.</p>
![image](https://github.com/user-attachments/assets/8ab17ab3-4018-4fa5-95d8-4566c86567f4)

<H2>8. Converting Labels to Integer</H2>
<p>I converted the labels to integer type for compatibility with the logistic regression model.</p>
![image](https://github.com/user-attachments/assets/e641ab09-d032-4e4a-8307-c72dc08c912d)

<H2>9. Training the Model</H2>
<p>I trained a logistic regression model on the training data.</p>
![image](https://github.com/user-attachments/assets/5be0a651-3cb5-4558-a18d-3f39e143131e)

<H2>10. Evaluating the Model</H2>
<p>I evaluated the model's performance on both training and testing data using accuracy score.</p>
![image](https://github.com/user-attachments/assets/bd88916e-5e9e-4aff-90f5-2eb595404f3e)

<H2>11. Making Predictions</H2>
<p>I built a predictive model to classify new emails as spam or not spam.</p>
<p><strong>Note : Give whatever mail you want to check whether it is spam or ham</strong></p> 
![image](https://github.com/user-attachments/assets/47ed455d-1666-4209-96c8-e235909f9ff2)

<H1>12. Visualizing Data</H1>
<p>I printed the data at various stages to understand the transformations.</p>
![image](https://github.com/user-attachments/assets/a8f1804e-1b9e-4c4c-b12d-713292effcb9)

<H2>13. Interpreting the Prediction</H2>
<p>Finally, I interpreted the prediction result and printed whether the mail is spam or not.</p>
![image](https://github.com/user-attachments/assets/5c288a27-f77c-4739-b8d4-060b17400150)

<H1>Summary.</H1>
<p>In this project, I successfully built a spam mail detection model using logistic regression and TF-IDF vectorization. The model was trained on a labeled dataset and achieved good accuracy in predicting whether a mail is spam or not. The project demonstrates the complete process from data loading and preprocessing to model training, evaluation, and prediction.

Feel free to clone this repository and try it out with your own dataset!</p>





