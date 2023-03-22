import pandas as pd
from pandas_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from streamlit_lottie import st_lottie
import json
with open('data_lt.json','r') as lott:
    anination = json.load(lott)
    lott.close()

st_lottie(anination,height = 200, width = 800,speed=0.5)
st.title("A Simple WebApp to do Basic DataExploration")
file_type = st.selectbox("What type of file do you want to analyze?",['csv','excel',""])
uploaded_data=st.file_uploader("Kindly upload your dataset")

if uploaded_data:
    if file_type == 'csv':
        data = pd.read_csv(uploaded_data)
    elif file_type == 'excel':
        data = pd.read_excel(uploaded_data)
    data_report = ProfileReport(data,explorative=True)
    st_profile_report(data_report)
