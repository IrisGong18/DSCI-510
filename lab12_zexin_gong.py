#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd


DATA_URL = 'car_data.csv'

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()

# Sidebar configuration
st.sidebar.header('Filter Options')
car_name = st.sidebar.text_input('Car Name', '')
transmission = st.sidebar.multiselect('Transmission', ['Manual', 'Automatic'], ['Manual', 'Automatic'])
selling_price = st.sidebar.slider('Selling Range', min_value=0, max_value=35, value=(0, 20))
year = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))


# Filtering data based on the selections
if st.sidebar.button('Submit'):
    filtered_data = data
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name, case=False)]
    if transmission:
        filtered_data = filtered_data[filtered_data['Transmission'].isin(transmission)]
    filtered_data = filtered_data[(filtered_data['Selling_Price'] >= selling_price[0]) & (filtered_data['Selling_Price'] <= selling_price[1])]
    filtered_data = filtered_data[(filtered_data['Year'] >= year[0]) & (filtered_data['Year'] <= year[1])]
    
    st.write(filtered_data)
else:
    st.write(data)



# In[ ]:




