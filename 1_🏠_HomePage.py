import streamlit as st
from PIL import Image
from gtts import gTTS
from io import BytesIO
import IPython.display as ipd
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title='Getting Started',
    page_icon=":seedling:",
)

st.title('Crop Yield Prediction ":seedling:"')
st.subheader('Empowering Agriculture with Precision')
st.sidebar.success("Please select a page above.")


image_url ='https://californiaagnet.com/wp-content/uploads/sites/13/2022/10/fruitveggies-850x491.jpeg'
st.image(image_url, width=700)


col1, col2, col2, col4, col5 = st.columns(5)



with col5:
    st.page_link("C:\\Nidhi\\predictive_analysis\\pages\\2_🌾_About.py", label="Next", icon="➡")



sound_file = BytesIO()
tts = gTTS('Add text-to-speech to your app', lang='en')
tts.write_to_fp(sound_file)
















