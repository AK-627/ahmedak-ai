import streamlit as st
import pandas as pd


st.title('🤖 MACHINE LEARNING APP')
st.info('This app build a Machine learning model')
with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/AK-627/ahmedak-ai/refs/heads/master/tiger_cleaned.csv')
  df
  st.write('**X**')
  X=df.drop('Common_Name',axis=1)
  X
  st.write('**y**')
  y=df.('Common_Name')
  y
