import streamlit as st
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

st.title("Dashboard - Tips Data")


df = pd.read_csv(DATA_PATH)
st.dataframe(df)

selected_day = st.selectbox('Select a day of the week', df['day'].unique())
selected_time = st.selectbox('Select a time of day', df['time'].unique())

# Filter the dataset based on user inputs
filtered_df = df[(df['day'] == selected_day) & (df['time'] == selected_time)]

# Create a histogram of tips using Plotly
fig1 = px.histogram(filtered_df, x='tip', nbins=30, title=f'Tips {selected_time} on {selected_day}')

# Create a box plot of tips by day using Plotly
fig2 = px.box(df, x='day', y='tip', color='time', title='Tips by Day and Time')

# Display the plots in Streamlit
st.plotly_chart(fig1)
st.plotly_chart(fig2)


###################################################################
