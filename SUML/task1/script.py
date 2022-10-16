import streamlit as st
import transformers
from PIL import Image

def run():
    st.write('Congratulations! You have successfully launched the application')
    st.title('Text translator')
    st.header('English-German translation')
    image = Image.open('todd-howard-it-just-works.gif')
    st.image(image, caption='It just works!')

    clicked = st.button('Click me!')
    if clicked:
        st.write('This application was made by s20335')

    option = st.selectbox(
        'Translation option',
        ('English to German translation', 'Option not yet available'))
    
    if option == 'English to German translation':
        en_de_translator = transformers.pipeline("translation_en_to_de")
        text = st.text_input('Text to translate')
        st.write(en_de_translator(text)[0]['translation_text'])

if __name__ == '__main__':
    run()