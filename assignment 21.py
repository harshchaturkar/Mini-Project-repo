# Streamlit is used to create web applications.
import streamlit as st
# Pandas is used for data handling and DataFrame creation.
import pandas as pd
# Joblib is used to load saved machine learning models.
import joblib


model = joblib.load("./assignment 21/ford_car.pkl")
scaler = joblib.load("./assignment 21/scaler.pkl")
encoded_columns = joblib.load("./assignment 21/columns.pkl")



st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)
# Configure the Streamlit page.
# page_title sets the title shown in the browser tab.
# layout="centered" keeps the app content centered on the page,
# making it cleaner and easier to use for a simple car price prediction app.


st.title("Ford Car Price Predictor")

st.write(
    "Enter the car details below to predict its selling price."
)


year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2025,
    value=2018
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    max_value=500000,
    value=30000
)

tax = st.number_input(
    "Road Tax",
    min_value=0,
    max_value=1000,
    value=150
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    max_value=200.0,
    value=50.0
)

engineSize = st.number_input(
    "Engine Size",
    min_value=0.0,
    max_value=10.0,
    value=1.5
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic", "Semi-Auto"]
)

fuelType = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)
#Advantages :
#Prevents invalid user input.
#Ensures consistency in catergorical values.
#improves user experience.


model_name = st.text_input("Car Model","Fiesta")

predict = st.button("Predict Price")

if predict:
    
        input_df = pd.DataFrame({
            "model": [model_name],
            "year": [year],
            "transmission": [transmission],
            "mileage": [mileage],
            "fuelType": [fuelType],
            "tax": [tax],
            "mpg": [mpg],
            "engineSize": [engineSize]
        })

        input_df = pd.get_dummies(input_df)

        input_df = input_df.reindex(
            columns=encoded_columns,
            fill_value=0
        )

        # Numerical columns
        numeric_cols = [
            "year",
            "mileage",
            "tax",
            "mpg",
            "engineSize"
        ]

        input_df[numeric_cols] = scaler.transform(
            input_df[numeric_cols]
        )

        prediction = model.predict(input_df)

        st.success(
            f"Predicted Price: £{prediction[0]:,.2f}"
        )
