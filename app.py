import streamlit as st # pyright: ignore[reportMissingImports]
import numpy as np  # pyright: ignore[reportMissingImports]
import joblib  # pyright: ignore[reportMissingImports]
status_prediction_model = joblib.load('status_prediction_model.pkl')
st.title('Country Status Prediction')
year = st.number_input('Year', min_value=2000, max_value=2015, step=1)
population = st.number_input('Population', min_value=30)
gdp_per_capita = st.number_input('GDP', min_value=1.00)
life_expectancy = st.number_input('Life Expectancy', min_value=35.00)
adult_mortality = st.number_input('Adult Mortality', min_value=0.00,max_value=800.00)
infant_deaths = st.number_input('infant deaths', min_value=0,max_value=2000)
alcohol = st.number_input('Alcohol', min_value=0.00)
percentage_expenditure = st.number_input('percentage expenditure', min_value=0.00)
hepatitis_b = st.number_input('Hepatitis B', min_value=0.00)
measles = st.number_input('Measles', min_value=0)
under_five_deaths = st.number_input('under-five deaths', min_value=0)
polio = st.number_input('Polio', min_value=0.00)
total_expenditure = st.number_input('Total expenditure', min_value=0.00,max_value=19.00)
diphtheria = st.number_input('Diphtheria', min_value=0.00,max_value=100.00)
hiv_aids = st.number_input('HIV/AIDS', min_value=0.00, max_value=51.00)
body_mass_index = st.number_input('BMI', min_value=0.00,max_value=90.00)
thinness_1_19_years = st.number_input('thinness 1-19 years', min_value=0.00,max_value=30.00,step=0.01)
thinness_5_9_years = st.number_input('thinness 5-9 years', min_value=0.00,max_value=30.00,step=0.01)
income_composition_of_resources = st.number_input('Income composition of resources', min_value=0.00,max_value=1.00)
schooling = st.number_input('Schooling', min_value=0.00,max_value=21.00)
if st.button('Predict Status'):
    input_data = [[year, population, gdp_per_capita,life_expectancy, adult_mortality, infant_deaths, alcohol,
                   percentage_expenditure, hepatitis_b, measles, under_five_deaths, polio, total_expenditure,
                   diphtheria, hiv_aids, body_mass_index, thinness_1_19_years, thinness_5_9_years, income_composition_of_resources, schooling]]
    prediction = status_prediction_model.predict(input_data)
    status_mapping = {0: 'Developing', 1: 'Developed'}
    predicted_status = status_mapping[prediction[0]]
    st.write(f'Predicted Status: {predicted_status}')

