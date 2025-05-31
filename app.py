import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("Fraud_detection_pipeline.pkl")

# App Title and Description
st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and click the Predict button.")

st.divider()

# Input Fields
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=9000.0)

# Predict Button
if st.button("Predict"):  
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Make prediction
    prediction = model.predict(input_data)[0] 

    # Show result
    st.subheader(f"Prediction: {'Fraud' if prediction == 1 else 'Not Fraud'}")
    if prediction == 1:
        st.error("This transaction may be fraudulent!")
    else:
        st.success("This transaction appears to be safe.")

