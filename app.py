import pandas as pd
import numpy as np
import streamlit as st
import joblib
st.title("Gold Price Prediction App")
st.write("""
This app predicts the **Gold Price** based on various economic indicators using a pre-trained machine learning model.
""")
# Load the pre-trained model
model = joblib.load('RandomeForest.joblib')
# Define input features
features = {
    'SPX': st.number_input('S&P 500 Index', value=1000.0),
    'USO': st.number_input('United States Oil', value=50.0),
    'SLV': st.number_input('Silver Price', value=20.0),
    'EUR/USD': st.number_input('EUR/USD Exchange Rate', value=1.1)
}
# Create a DataFrame for the input features
input_data = pd.DataFrame([features])
# Predict button
if st.button('Predict Gold Price'):
    # Make prediction
    prediction = model.predict(input_data)
    # Display the result    
    st.success(f'The predicted Gold Price is: ${prediction[0]:.2f}')    
# Display input features
st.subheader('Input Features.')
st.write(input_data)

