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
  y=df.Common_Name
  y
with st.expander('Data Visualization'):
  st.scatter_chart(data=df,x='Length',y='Weight',color='Common_Name')
#Data Preparations
with st.sidebar:
  st.header('Input Features')
  #Common Name,Scientific Name,Continent,Sex,Length,Weight
  Scientific_Name=st.selectbox('Scientific_Name',('Panthera tigris tigris','Panthera tigris altaica','Panthera tigris corbetti','Panthera tigris jacksoni','Panthera tigris amoyensis'))
