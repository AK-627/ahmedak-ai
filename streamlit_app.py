import streamlit as st
import pandas as pd


st.title('🤖 MACHINE LEARNING APP')

st.info('This app build a Machine learning model')
df=pd.read_csv('https://raw.githubusercontent.com/AK-627/ahmedak-ai/33af28282fed9d82d5a8b634e864f5786c67c161/tiger_cleaned.csv')
df
