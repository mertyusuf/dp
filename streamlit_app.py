import streamlit as st
import pandas as pd


st.title('Machine Learning App')

st.info('This is a app builds a machine learning model!')
with st.expender('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
