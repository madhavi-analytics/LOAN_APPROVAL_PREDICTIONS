# LOAN_APPROVAL_PREDICTION

Project Overview

This project predicts whether a loan will be approved or not using Machine Learning algorithms. The model is trained using applicant details such as income, credit score, loan amount, loan term, existing loans, and dependents.

Features

- Predict loan approval status
- User-friendly Streamlit web application
- Machine Learning model integration
- Real-time prediction based on user input

Technologies Used

- Python
- Machine Learning
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

Dataset Features

The following input features are used for prediction:

- Income
- Credit Score
- Loan Amount
- Loan Term
- Existing Loans
- Dependents

Machine Learning Models Used

- Decision Tree Classifier
- Random Forest Classifier
- Logistic Regression

Among these, Logistic Regression provided better performance for prediction.

Project Structure

Loan-Approval-Prediction/

│── app.py
│── model.pkl
│── requirements.txt
│── Loan_approval_predictions.ipynb
│── README.md

How to Run the Project

1. Clone the repository
2. Install dependencies:

pip install -r requirements.txt

3. Run the Streamlit app:

streamlit run app.py

Future Improvements

- Improve model accuracy
- Add more features
- Enhance UI design
- Deploy advanced version with better predictions
