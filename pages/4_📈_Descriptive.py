import streamlit as st
import pandas as pd


st.title('Descriptive Analysis')
# Descriptive Analysis

crop = pd.read_csv("C:\\Nidhi\\crop\\crop_yield.csv")

df = crop.describe(include='all').T
st.write(df)


col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("C:\\Nidhi\\predictive_analysis\\pages\\3_📚_Dataset.py", label="Previous", icon="⬅")

with col5:

    st.page_link("C:\\Nidhi\\predictive_analysis\\pages\\5_📊_Exploration.py", label="Next", icon="➡")
