import streamlit as st
import pandas as pd
import joblib

model = joblib.load("./assignment 21/heart.pkl")
encoded_columns = joblib.load("./assignment 21/columns.pkl")

st.set_page_config(
    page_title="Heart Disease Predictor",
    layout="centered"
)

st.title("Heart Disease Predictor")

st.write(
    "Enter the patients details below to predict Heart Disease."
)

Age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=40
)

RestingBP = st.number_input(
    "RestingBP",
    min_value=70,
    max_value=200,
    value=120
)

Cholesterol = st.number_input(
    "Cholesterol",
    min_value=100,
    max_value=600,
    value=200
)

FastingBS = st.number_input(
    "FastingBS",
    min_value=0,
    max_value=1,
    value=0
)

MaxHR = st.number_input(
    "MaxHR",
    min_value=60,
    max_value=250,
    value=150
)

Oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=6.5,
    value=1.0,
    step=0.1
)


Sex = st.selectbox(
    "Sex",
    ["Mail(M)", "Femail(F)"]
)

ChestPainType = st.selectbox(
    "ChestPainType",
    ["ASY", "ATA", "NAP","TA"]
)

RestingECG = st.selectbox(
    "RestingECG",
    ["LVH", "Normal", "ST"]
)

ExerciseAngina = st.selectbox(
    "ExerciseAngina",
    ["NO(N)", "YES(Y)"]
)
ST_Slope = st.selectbox(
    "ST_Slope",
    ["Down", "Flat","Up"]
)

predict = st.button("Predict Heart Disease")

if predict:
    
        input_df = pd.DataFrame({
            "Age": [Age],
            "Sex": [Sex],
            "ChestPainType": [ChestPainType],
            "RestingBP": [RestingBP],
            "Cholesterol": [Cholesterol],
            "FastingBS": [FastingBS],
            "RestingECG": [RestingECG],
            "MaxHR": [MaxHR],
            "ExerciseAngina": [ExerciseAngina],
            "Oldpeak": [Oldpeak],
            "ST_Slope": [ST_Slope]
        })

        input_df = pd.get_dummies(input_df)

        input_df = input_df.reindex(
           columns=encoded_columns,
           fill_value=0
        )

        prediction = model.predict(input_df)
        if prediction[0] == 1:
            st.error("Prediction: Heart Disease Detected")
        else:
            st.success("Prediction: No Heart Disease Detected")