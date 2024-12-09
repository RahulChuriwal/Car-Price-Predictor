import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

data = pd.read_csv('Cleaned_Car_data.csv')

st.markdown(
    """
    <style>
    /* Change cursor to pointer for dropdowns */
    .stSelectbox > div:first-child {
        cursor: pointer !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Car Price Prediction App")
st.write("""
### Predict the price of a car based on its specifications!
Provide the details of the car you are interested in, and this app will predict its estimated price.
""")

st.sidebar.header("Enter Car Details")

name = st.sidebar.selectbox(
    "Car Model",
    data['name'].unique()
)

filtered_data = data[data['name'] == name]
company = filtered_data['company'].iloc[0]
st.sidebar.write(f"Car Manufacturer: **{company}**")

year = st.sidebar.slider(
    "Year of Manufacturing",
    int(data['year'].min()),
    int(data['year'].max()),
    step=1
)

kms_driven = st.sidebar.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=500000,
    step=1000
)

fuel_type = st.sidebar.radio(
    "Fuel Type",
    data['fuel_type'].unique()
)

# Predict Button
if st.sidebar.button("Predict Price"):
    # Prepare the input data
    input_data = pd.DataFrame(
        [[name, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    predicted_price = model.predict(input_data)[0]

    st.success(f"Estimated Price for the selected car is ₹{predicted_price:,.2f}")
