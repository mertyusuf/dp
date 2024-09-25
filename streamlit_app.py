import streamlit as st
import pandas as pd


st.title('Machine Learning App')

st.info('This is a app builds a machine learning model!')
df = pd.read_csv('https://raw.githubusercontent.com/mertyusuf/dp/master/credit22.csv', sep=';', encoding='utf-8')
df
