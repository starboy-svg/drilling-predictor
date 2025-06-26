
import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("drilling_model.pkl")

# Define output labels
output_labels = ['600', '300', '200', '100', '6', '3',
                 'av', 'pv', 'yp', 'cof', '10s_gs', '10min_gs']

st.title("🛢️ Drilling Fluid Rheology Predictor")
st.write("Enter the ingredient values below to predict 12 rheological properties.")

# Input fields
kcl = st.number_input("KCl", min_value=0.0, step=0.1)
naoh = st.number_input("NaOH", min_value=0.0, step=0.1)
xcd = st.number_input("XCD", min_value=0.0, step=0.1)
pacr = st.number_input("PAC-R", min_value=0.0, step=0.1)
barite = st.number_input("Barite", min_value=0.0, step=0.1)

if st.button("Predict"):
    input_data = np.array([[kcl, naoh, xcd, pacr, barite]])
    prediction = model.predict(input_data)[0]

    st.subheader("🔮 Predicted Rheological Properties:")
    for name, val in zip(output_labels, prediction):
        st.write(f"**{name}:** {val:.2f}")
