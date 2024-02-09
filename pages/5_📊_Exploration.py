import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



st.title("Exploration")


crop = pd.read_csv("C:\\Nidhi\\crop\\crop_yield.csv")

st.subheader(" Different Visual Distributions in the Indian Crop Yield Dataset")


# Assuming 'crop' is your DataFrame
yearly_yield = crop.groupby('Crop_Year').mean().reset_index()


# Define visualization categories
categories = {
    'Bar Plots': ['Crop Distribution', 'Season Distribution'],
    'Line Charts': ['Average Yield Over the Years', 'Average Area Used Over the Years',
                    'Annual Rainfall Over the Years', 'Fertilizers Used Over the Years',
                    'Pesticides Used Over the Years'],
    'Scatter Plots': ['Scatter Plot for Area Vs Yield', 'Scatter Plot for Annual Rainfall Vs Yield',
                      'Scatter Plot for Fertilizers Used Vs Yield', 'Scatter Plot for Pesticides Used Vs Yield'],
    'Heatmaps': ['Correlation Heatmap']
}


# Create select boxes for category and visualization
category = st.selectbox('Choose Category', list(categories.keys()))

visualization_options = categories[category]
visuals = st.selectbox('Choose Visualization', visualization_options)

# Plot based on user selection
if category == 'Bar Plots':
    if visuals == 'Crop Distribution':
        plot1 = pd.DataFrame(crop['Crop'].value_counts()).head(50)
        st.bar_chart(plot1)
    elif visuals == 'Season Distribution':
        plot2 = pd.DataFrame(crop['Season'].value_counts())
        st.bar_chart(plot2)
elif category == 'Line Charts':
    if visuals == 'Average Yield Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Yield'], use_container_width=True, color="#FF0000")
    elif visuals == 'Average Area Used Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Area'], use_container_width=True, color="#FF0000")
    elif visuals == 'Annual Rainfall Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Annual_Rainfall'], use_container_width=True, color="#FF0000")
    elif visuals == 'Fertilizers Used Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Fertilizer'], use_container_width=True, color="#FF0000")
    elif visuals == 'Pesticides Used Over the Years':
        st.line_chart(yearly_yield.set_index('Crop_Year')['Pesticide'], use_container_width=True, color="#FF0000")
elif category == 'Scatter Plots':
    if visuals == 'Scatter Plot for Area Vs Yield':
        st.scatter_chart(data=crop, x='Area', y='Yield')
    elif visuals == 'Scatter Plot for Annual Rainfall Vs Yield':
        st.scatter_chart(data=crop, x='Annual_Rainfall', y='Yield')
    elif visuals == 'Scatter Plot for Fertilizers Used Vs Yield':
        st.scatter_chart(data=crop, x='Fertilizer', y='Yield')
    elif visuals == 'Scatter Plot for Pesticides Used Vs Yield':
        st.scatter_chart(data=crop, x='Pesticide', y='Yield')
elif category == 'Heatmaps':
    if visuals == 'Correlation Heatmap':
        fig, ax = plt.subplots()
        sns.heatmap(yearly_yield.corr(), annot=True, linewidths=2, cmap="magma", ax=ax)
        st.pyplot(fig)


col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("C:\\Nidhi\\predictive_analysis\\pages\\4_📈_Descriptive.py", label="Previous", icon="⬅")

with col5:

    st.page_link("C:\\Nidhi\\predictive_analysis\\pages\\6_🛠_Preprocessing.py", label="Next", icon="➡")












