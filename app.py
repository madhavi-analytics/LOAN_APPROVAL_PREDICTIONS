import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("Loan Approval Prediction")

income = st.number_input("Income")
credit = st.number_input("Credit Score")
loan = st.number_input("Loan Amount")
term = st.number_input("Loan Term")
existing = st.number_input("Existing Loans")
dependents = st.number_input("Dependents")

if st.button("Predict"):
    prediction = model.predict([
        [income, credit, loan, term, existing, dependents]
    ])

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Not Approved ❌")
