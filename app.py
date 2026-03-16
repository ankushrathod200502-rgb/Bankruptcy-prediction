import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("bankruptcy_model.pkl","rb"))

st.title("Bankruptcy Prediction System")

industrial_risk = st.selectbox("Industrial Risk",[0,0.5,1])
management_risk = st.selectbox("Management Risk",[0,0.5,1])
financial_flexibility = st.selectbox("Financial Flexibility",[0,0.5,1])
credibility = st.selectbox("Credibility",[0,0.5,1])
competitiveness = st.selectbox("Competitiveness",[0,0.5,1])
operating_risk = st.selectbox("Operating Risk",[0,0.5,1])

if st.button("Predict"):

    data = np.array([[industrial_risk,
                      management_risk,
                      financial_flexibility,
                      credibility,
                      competitiveness,
                      operating_risk]])

    prediction = model.predict(data)

    if prediction[0] == 0:
        st.error("Company may go BANKRUPT")
    else:
        st.success("Company is NON-BANKRUPT")