import streamlit as st
import pandas as pd
import joblib

model = joblib.load("./assignment pkl/student_performance_dataset.pkl")
scaler = joblib.load("./assignment pkl/scaler.pkl")
encoded_columns = joblib.load("./assignment pkl/columns.pkl")

st.set_page_config(
    page_title="Student Performance Predictor",
    layout="centered"
)

st.title("Student Performance Predictor")

st.write(
    "Enter the Student details below to predict Student Performance."
)

student_id = st.number_input(
    "student_id",
    min_value=1,
    max_value=1000,
    value=1
)

study_time_hours = st.number_input(
    "study_time_hours",
    min_value=0,
    max_value=20,
    value=3
)

attendance_percent = st.number_input(
    "attendance_percent",
    min_value=35,
    max_value=100,
    value=50
)

sleep_hours = st.number_input(
    "sleep_hours",
    min_value=3,
    max_value=20,
    value=6
)

previous_grade = st.number_input(
    "previous_grade",
    min_value=30,
    max_value=100,
    value=60
)


gender = st.selectbox(
    "gender",
    ["Mail(M)", "Femail(F)"]
)

parental_education = st.selectbox(
    "parental_education",
    ["Bachelors", "High School", "Masters","PhD"]
)

internet_access = st.selectbox(
    "internet_access",
    ["Yes", "No"]
)

extracurricular_activities = st.selectbox(
    "extracurricular_activities",
    ["NO", "YES"]
)

part_time_job = st.selectbox(
    "part_time_job",
    ["No", "Yes"]
)

predict = st.button("Predict Student Performance")

if predict:
    
        input_df = pd.DataFrame({
            "student_id": [student_id],
            "gender": [gender],
            "study_time_hours": [study_time_hours],
            "attendance_percent": [attendance_percent],
            "sleep_hours": [sleep_hours],
            "parental_education": [parental_education],
            "internet_access": [internet_access],
            "extracurricular_activities": [extracurricular_activities],
            "part_time_job": [part_time_job],
            "previous_grade": [previous_grade]
        })
        input_df = pd.get_dummies(input_df)

        input_df = input_df.reindex(
            columns=encoded_columns,
            fill_value=0
        )

        prediction = model.predict(input_df)

        st.subheader("Prediction Result")
        st.success(f"Predicted Final Grade: {prediction[0]}")