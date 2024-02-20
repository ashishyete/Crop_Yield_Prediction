import streamlit as st
from gtts import gTTS
from io import BytesIO
import warnings
import os
warnings.filterwarnings("ignore")
from streamlit_supabase_auth import logout_button



st.set_page_config(
    page_title='Getting Started',
    page_icon=":seedling:",
)
session_state = st.session_state
def logoutfunct():
    print('Logout function called.')
    logout_button()
    #st.markdown('<meta http-equiv="refresh" content="2">', unsafe_allow_html=True)


if hasattr(st,'session_state'):

    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 2_HomePage")
    else:
        print("session_state is not fully initialized - 2_HomePage")
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()
else:
    st.warning('Session_state not initialized.')

st.title('Crop Yield Prediction ":seedling:"')
st.subheader('Empowering Agriculture with Precision')
#st.sidebar.success("Please select a page above.")
with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logoutfunct()

image_url ='https://californiaagnet.com/wp-content/uploads/sites/13/2022/10/fruitveggies-850x491.jpeg'
st.image(image_url, width=700)


col1, col2, col2, col4, col5 = st.columns(5)



with col5:
    st.page_link('pages/3_🌾_About.py', label="Next", icon="➡")



sound_file = BytesIO()
tts = gTTS('Add text-to-speech to your app', lang='en')
tts.write_to_fp(sound_file)