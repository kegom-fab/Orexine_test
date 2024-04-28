import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Opportunity",
    page_icon="📝",
)

data = pd.read_excel('Datatest.xlsx')
st.markdown(f'<h1 style="font-size:30px; text-align: center;text-decoration: underline">{"Statistics"}</h1>', unsafe_allow_html=True)
st.write("We have :", len(data.columns), "Columns, and", len(data), "Raws." )
st.write("Statistic of Character string columns")
st.write(data.describe(include='object'))
st.write("Statistic of date and numeric Columns")
st.write(data.describe())

st.markdown(f'<h1 style="color: blue; font-size:18px; text-align: center">{"Powerd by Orexine"}</h1>', unsafe_allow_html=True)

