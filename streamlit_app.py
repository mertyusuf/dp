import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This is an app that builds a machine learning model!')
with st.expander('Data'):
    st.write('**Raw data**')
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
    st.write(df)
