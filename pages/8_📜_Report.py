import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Crop Yield Report")


crop = pd.read_csv("crop_data/crop_yield.csv")

crop_state = crop.groupby('State').sum()
crop_state.sort_values(by = 'Yield', inplace=True, ascending = False)

tab1, tab2, tab3 = st.tabs(["Statewise Yield", "Statewise Annual Rainfall","Statewise Fertilizer Usage"])

with tab2:
    st.subheader("Annual Rainfall in States of India")

    # Create an interactive bar chart with Plotly Express
    fig = px.bar(crop, x='State', y='Annual_Rainfall', color='State', hover_data=['Annual_Rainfall'])

    # Adjust the size of the plot if needed
    fig.update_layout(width=800, height=600)

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    st.write("**The state of Meghalaya has the highest Annual Rainfall followed by the state West Bengal.**")

    st.markdown(
        'In 2020, a noticeable downturn was evident across various agricultural metrics, encompassing crop yield, cultivated area, and the utilization of pesticides and fertilizers. This decline is potentially linked to the nationwide lockdown imposed in India in response to the COVID-19 virus, causing disruptions in agricultural practices. Upon initial data examination, a positive skewness in the distribution of data features was observed.'

        'Following meticulous data cleaning and scaling procedures, a transformative process ensued, yielding a more normalized and linearly distributed dataset. This normalization holds paramount importance in ensuring the reliability of subsequent statistical analyses and model performance. Subsequent assessments affirmed the fulfillment of assumptions regarding linearity, independence, normality, and homoscedasticity in the data.'

        'More specifically, the features showcased a more symmetric distribution post-scaling, aligning with the assumptions of normality. The lack of significant correlations among most features, except for the positive correlation noted between production and yield, and between Pesticide and Fertilizer substantiates the assumption of independence among variables. These findings significantly contribute to fortifying the robustness of subsequent analyses and modeling endeavors within the agricultural dataset.')

with tab1:
    st.subheader("Crop Yield in States of India")
    # Create an interactive bar chart with Plotly Express
    fig = px.bar(crop, x='State', y='Yield', color='State', hover_data=['Yield'])

    # Adjust the size of the plot if needed
    fig.update_layout(width=800, height=600)

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    st.write("**In India, West Bengal produces the highest yield, followed by Puducherry and Andhra Pradesh.**")

    st.markdown('In 2020, a noticeable downturn was evident across various agricultural metrics, encompassing crop yield, cultivated area, and the utilization of pesticides and fertilizers. This decline is potentially linked to the nationwide lockdown imposed in India in response to the COVID-19 virus, causing disruptions in agricultural practices. Upon initial data examination, a positive skewness in the distribution of data features was observed.'

        'Following meticulous data cleaning and scaling procedures, a transformative process ensued, yielding a more normalized and linearly distributed dataset. This normalization holds paramount importance in ensuring the reliability of subsequent statistical analyses and model performance. Subsequent assessments affirmed the fulfillment of assumptions regarding linearity, independence, normality, and homoscedasticity in the data.'

        'More specifically, the features showcased a more symmetric distribution post-scaling, aligning with the assumptions of normality. The lack of significant correlations among most features, except for the positive correlation noted between production and yield, and between Pesticide and Fertilizer substantiates the assumption of independence among variables. These findings significantly contribute to fortifying the robustness of subsequent analyses and modeling endeavors within the agricultural dataset.')

with tab3:
    st.subheader("Fertilizer Usage in States of India")

    # Create an interactive bar chart with Plotly Express
    fig = px.bar(crop, x='State', y='Fertilizer', color='State', hover_data=['Fertilizer'])

    # Adjust the size of the plot if needed
    fig.update_layout(width=800, height=600)

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    st.write("**Uttar Pradesh leads in the highest fertilizer usage, followed by Madhya Pradesh and Maharashtra in terms of quantity.**")

    st.markdown(
        'In 2020, a noticeable downturn was evident across various agricultural metrics, encompassing crop yield, cultivated area, and the utilization of pesticides and fertilizers. This decline is potentially linked to the nationwide lockdown imposed in India in response to the COVID-19 virus, causing disruptions in agricultural practices. Upon initial data examination, a positive skewness in the distribution of data features was observed.'

        'Following meticulous data cleaning and scaling procedures, a transformative process ensued, yielding a more normalized and linearly distributed dataset. This normalization holds paramount importance in ensuring the reliability of subsequent statistical analyses and model performance. Subsequent assessments affirmed the fulfillment of assumptions regarding linearity, independence, normality, and homoscedasticity in the data.'

        'More specifically, the features showcased a more symmetric distribution post-scaling, aligning with the assumptions of normality. The lack of significant correlations among most features, except for the positive correlation noted between production and yield, and between Pesticide and Fertilizer substantiates the assumption of independence among variables. These findings significantly contribute to fortifying the robustness of subsequent analyses and modeling endeavors within the agricultural dataset.')

col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("pages/7_🤖_Modeling.py", label="Previous", icon="⬅")

with col5:

    st.page_link("pages/9_🤝_Help.py", label="Next", icon="➡")