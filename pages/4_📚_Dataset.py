import streamlit as st
import pandas as pd
from streamlit_supabase_auth import logout_button

session_state = st.session_state

if hasattr(st,'session_state'):

    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 4_Dataset")
    else:
        print("session_state is not fully initialized - 4_Dataset")
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()
else:
    st.warning('Session_state not initialized. - 4_Dataset')

st.title('Dataset - Indian Crop Yield :chart_with_upwards_trend:')

#st.sidebar.header('Dataset :chart_with_upwards_trend:')

st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The crop yield prediction dataset is accessible on Kaggle, covering Indian agriculture from 1997 to 2020. '
             'The comprehensive dataset, sourced from government outlets like District-wise Season-wise Crop Production '
             'Statistics, FAOSTAT, Rainfall India, Environics India, and IMD Pune, includes vital features for prediction.'
             ' These features encompass crop types, crop years, cropping seasons, states, cultivation areas, production '
             'quantities, annual rainfall, fertilizer and pesticide usage, and calculated yields. The structured data, '
             'presented in CSV format, consists of both qualitative (e.g., crop, state, season) and quantitative '
             '(e.g., crop_year, area, production, rainfall, fertilizer, pesticide usage, yield) information. The dataset '
             'contains 10 columns and 19,698 rows, representing data for various crops and their corresponding features '
             'over the specified period. ')



crop = pd.read_csv('crop_data/crop_yield.csv')
st.write(crop)

st.session_state['crop'] = pd.read_csv('crop_data/crop_yield.csv')

with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()

col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("pages/3_🌾_About.py", label="Previous", icon="⬅")

with col5:

    st.page_link("pages/5_📈_Descriptive.py", label="Next", icon="➡")

