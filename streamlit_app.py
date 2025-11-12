import streamlit as st
import pandas as pd

st.title('🤖 MACHINE LEARNING APP')
st.info('This app build a Machine learning model')
with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/AK-627/ahmedak-ai/refs/heads/master/tiger_cleaned.csv')
  st.write(df)
  st.write('**X**')
  X = df.drop('Common_Name',axis=1)
  st.write(X)
  st.write('**y**')
  y=df.Common_Name
  st.write(y)

with st.expander('Data Visualization'):
  st.scatter_chart(data=df,x='Length',y='Weight')  # removed invalid color arg

#Data Preparations
with st.sidebar:
  st.header('Input Features')
  #Common Name,Scientific Name,Continent,Sex,Length,Weight
  Common_Name=st.selectbox('Common_Name',('Bengal Tiger','Siberian Tiger','Indochinese','Malayan Tiger'))
  Scientific_Name=st.selectbox('Scientific_Name',('Panthera tigris tigris','Panthera tigris altaica','Panthera tigris corbetti','Panthera tigris jacksoni','Panthera tigris amoyensis'))
  Continent=st.selectbox('Continent',('Asia',))   # <- fixed: single-item tuple
  Sex=st.selectbox('Sex',('Male','Female'))
  Length=st.slider('Length(m)',2.0,3.5,2.5)        # <- fixed: scalar default
  Weight=st.slider('Weight(kg)',80,300,120)       # <- fixed: scalar default

  #CREATING A DATAFRAME that matches X's columns (do NOT include Common_Name)
  data_for_X = {
        'Scientific_Name':Scientific_Name,
        'Continent':Continent,
        'Sex':Sex,
        'Length':Length,
        'Weight':Weight
  }
  input_df = pd.DataFrame(data_for_X, index=[0])

# CONCAT with X (columns match) and display
input_tiger = pd.concat([input_df, X], axis=0, ignore_index=True)
st.write("## Input + Dataset (preview)")
st.write(input_tiger.head())
