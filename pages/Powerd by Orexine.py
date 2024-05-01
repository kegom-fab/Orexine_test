import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Opportunity",
    page_icon="📝",
)

st.markdown(f'<h1 style="font-size:30px; text-align: center;text-decoration: underline">{"Orexine"}</h1>', unsafe_allow_html=True)

st.markdown(f'<h3 style="font-size:20px; text-align: center;">{"Welcome to our company!!!"}</h3>', unsafe_allow_html=True)
logo_image = "orexine.jpg"
st.image(logo_image, use_column_width=True)
text = """
    <div style="text-align: justify">
    We are a dynamic company specializing in software development, data analysis, digital transformation, IT consulting, and business analysis. 
    Our team provides innovative and tailored solutions to meet the growing needs of our clients in today's digital world. 
    Whether it's creating custom software, conducting in-depth data analysis, optimizing business processes, or implementing digital strategies, 
    we are here to support our clients at every step of their digital transformation journey.
    </div>
    """

st.markdown(text, unsafe_allow_html=True)

st.markdown(f'<h1 style="color: blue; font-size:18px; text-align: center">{"Powerd by Orexine"}</h1>', unsafe_allow_html=True)
