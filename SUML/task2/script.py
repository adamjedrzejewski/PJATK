import pickle
import streamlit as st

rf_5_file = open('rf_5_model.pkl', 'rb')
rf_8_file = open('rf_8_model.pkl', 'rb')

rf_5_model = pickle.load(rf_5_file)
rf_8_model = pickle.load(rf_8_file)

left, right = st.columns(2)

with left:
    st.write('Patient data:')

    symptoms = st.slider('Number of symptoms', 1, 5)
    age = st.slider('Age', 11, 77)
    disease = st.slider('Number of diseases', 0, 5)
    height = st.slider('Height', 159, 200)
    medicines = st.slider('Number of medicines given for each patient', 1, 4)

with right:
    preffered_model_selection = st.selectbox(
        'Select Random forrest model:',
        ('max_depth=5', 'max_depth=8'))

    prediction = None
    if preffered_model_selection == 'max_depth=5':
        preffered_model = rf_5_model
    if preffered_model_selection == 'max_depth=8':
        preffered_model = rf_8_model

    prediction = preffered_model.predict([[symptoms, age, disease, height, medicines]])

    if prediction[0] == 1:
        st.write('Healed after one week')
    if prediction[0] == 0:
        st.write('Not healed after one week')

