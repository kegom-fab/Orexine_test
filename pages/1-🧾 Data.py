import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Opportunity",
    page_icon="📝",
)
data = pd.read_excel('Datatest.xlsx')

st.markdown(f'<h1 style="font-size:30px; text-align: center;text-decoration: underline">{"Data"}</h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="color:gray; font-size:13px; text-align: center">{"You can click on a column to sort!"}</h1>', unsafe_allow_html=True)

st.write(data)
st.write("Number of columns :", len(data.columns))
st.write("Number of raws :", len(data))
st.markdown(f'<h1 style="color: blue; font-size:18px; text-align: center">{"Powerd by Orexine"}</h1>', unsafe_allow_html=True)
