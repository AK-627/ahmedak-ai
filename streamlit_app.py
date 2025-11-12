import streamlit as st
import pandas as pd


st.title('🤖 MACHINE LEARNING APP')
st.info('This app build a Machine learning model')
with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/AK-627/ahmedak-ai/refs/heads/master/tiger_cleaned.csv')
  df
  st.write('**X**')
  X = df.drop('Common_Name',axis=1)
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
  Sex=st.selectbox('Sex',('Male','Female'))
  Length=st.slider('Length(m)',2.0,3.5,(2.1,3.1))
  Weight=st.slider('Weight(kg)',80,300,(100,200))

  #CEATING A DATAFRAME
  data={'Scientific_Name':Scientific_Name,
        'Sex':Sex,
        'Length':Length,
        'Weight':Weight}
  input_df=pd.DataFrame(data,index=[0])
  input_tiger=pd.concat([input_df, X],axis=0)
input_tiger

  
  
