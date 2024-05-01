import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Opportunity",
    page_icon="📝",
)

data = pd.read_excel('Datatest.xlsx')
# Chiffre d'affaires
revenue = data['1st Year Revenue (Merged)'].sum() + data['Revenue Weightage (next year)'].sum()
# Filtrer les données pour l'année 2023
data_2023 = data[data['Created Date'].dt.year == 2023]
# Calculer le chiffre d'affaires en 2023
revenue_2023 = data_2023['1st Year Revenue (Merged)'].sum() + data_2023['Revenue Weightage (next year)'].sum()
# Nombre de projets reçus
projects_received = data['Opportunity Name'].nunique()
# Compter le nombre de projets pour chaque étape (stage)
project_count_by_stage = data.groupby('Stage')['Opportunity Name'].count().reset_index()
project_count_by_stage.columns = ['Stage', 'Number of Projects']
# Nombre de clients
clients = data['Account Name'].nunique()
# Années de fonctionnement
years_of_operation = data['Created Date'].dt.year.nunique()
# Nombre de régions d'équipes
regions_teams = data['Team Region'].nunique()
# Nombre de sous-régions
sub_regions = data['Team Sub-Region'].nunique()
# Nombre de responsables de projets
project_managers = data['Oppty Owner'].nunique()
st.markdown(f'<h1 style="font-size:30px; text-align: center;text-decoration: underline">{"Key numbers"}</h1>', unsafe_allow_html=True)

st.markdown(f'<h3 style="font-size:18px; text-align: center">Total income received since the operation of the company: {revenue}</h3>', unsafe_allow_html=True)
st.markdown(f'<h3 style="font-size:18px; text-align: center">{revenue_2023} Dollars of turnover achieved in 2023</h3>', unsafe_allow_html=True)
# Définir une colonne pour les visualisations
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<h3 style="font-size:18px; text-align: center">{projects_received} projects received including:</h3>', unsafe_allow_html=True)
with col2:
    st.markdown(project_count_by_stage['Stage'].to_frame().to_html(index=False), unsafe_allow_html=True)
with col3:
    st.markdown(project_count_by_stage['Number of Projects'].to_frame().to_html(index=False), unsafe_allow_html=True)
fig = px.pie(project_count_by_stage, values='Number of Projects', names='Stage', title='Percentage of each stage')
st.plotly_chart(fig)
st.markdown(f'<h3 style="font-size:18px; text-align: center">{clients} Customers received in total.</h3>', unsafe_allow_html=True)
st.markdown(f'<h3 style="font-size:18px; text-align: center">Company has {years_of_operation} years of Operation </h3>', unsafe_allow_html=True)
st.markdown(f'<h3 style="font-size:18px; text-align: center">{regions_teams} equipped Regions</h3>', unsafe_allow_html=True)
st.markdown(f'<h3 style="font-size:18px; text-align: center">{sub_regions} Sub regions</h3>', unsafe_allow_html=True)
st.markdown(f'<h3 style="font-size:18px; text-align: center">{project_managers} Project Manager</h3>', unsafe_allow_html=True)

st.markdown(f'<h1 style="color: blue; font-size:18px; text-align: center">{"Powerd by Orexine"}</h1>', unsafe_allow_html=True)
