import streamlit as st

image = st.camera_input('Take a picture')

st.write(type(image))