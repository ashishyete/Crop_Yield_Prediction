import streamlit as st
import pandas as pd
from streamlit_supabase_auth import logout_button

session_state = st.session_state

if hasattr(st,'session_state'):

    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 5_Descriptive")
    else:
        print("session_state is not fully initialized - 5_Descriptive")
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()
else:
    st.warning('Session_state not initialized. - 5_Descriptive')

st.title('Descriptive Analysis')
# Descriptive Analysis

crop = pd.read_csv("crop_data/crop_yield.csv")

df = crop.describe(include='all').T
st.write(df)

with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()

col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("pages/4_📚_Dataset.py", label="Previous", icon="⬅")

with col5:

    st.page_link("pages/6_📊_Exploration.py", label="Next", icon="➡")
