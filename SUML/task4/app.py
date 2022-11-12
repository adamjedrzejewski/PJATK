import streamlit as st
import fastbook
from fastai.vision.widgets import *
from fastai.vision.all import *

learn_inference = fastbook.load_learner('eye_model.pkl')

st.title("Application for recognizing gender")
source = st.selectbox('data source', ['upload', 'camera'])
if source == 'upload':
    data = st.file_uploader('Choose a photo')
elif source == 'camera':
    data = st.camera_input('Take a picture')
else:
    data = None

image = None
if data is not None:
    image = PILImage.create((data))

clicked = st.button("Classification")
if clicked:
    if image is not None:
        pred, pred_idx, probs = learn_inference.predict(image)
        col1, col2 = st.columns(2)
        col1.metric("Prediction", pred)
        prob = float(probs[pred_idx]) * 100
        if 'old_prob' not in st.session_state:
            st.session_state['old_prob'] = prob

        delta = prob - st.session_state['old_prob']
        col2.metric("Probability", f'{prob:.0f}%', delta=f'{delta:.0f}')
        st.session_state['old_prob'] = prob
    else:
        st.write('You need to upload an image first')
