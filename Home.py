import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Opportunity",
    page_icon="📝",
)

st.title("Welcome 😀")
st.markdown(f'<h1 style="font-size:25px; text-align: center">{"Monitoring the evolution of income over time"}</h1>', unsafe_allow_html=True)

data = pd.read_excel('Datatest.xlsx')

# Ajouter une colonne pour le total des revenus
data['Total Revenue'] = data['1st Year Revenue (Merged)'] + data['Revenue Weightage (next year)']

# Ajouter une colonne pour la granularité temporelle sélectionnée par l'utilisateur (par défaut par mois)
data['Time Granularity'] = data['Created Date'].dt.to_period('M').astype(str)

# Créer une liste des granularités disponibles
granularities = ['Per month', 'Per quarter', 'Per year']

# Demander à l'utilisateur de choisir la granularité temporelle
selected_granularity = st.selectbox('Choose the temporal granularity :', granularities)

# Regrouper les données en fonction de la granularité sélectionnée par l'utilisateur
if selected_granularity == 'Per quarter':
    data['Time Granularity'] = data['Created Date'].dt.to_period('Q').astype(str)
elif selected_granularity == 'Per year':
    data['Time Granularity'] = data['Created Date'].dt.to_period('Y').astype(str)

# Regrouper les données par granularité temporelle et calculer le total des revenus
revenue_by_time = data.groupby('Time Granularity')['Total Revenue'].sum().reset_index()

# Créer le graphique avec Plotly Express
fig = px.line(revenue_by_time, x='Time Granularity', y='Total Revenue', title='Evolution of total revenue')

# Mettre à jour les étiquettes de l'axe des x en fonction de la granularité
if selected_granularity == 'Per month':
    fig.update_xaxes(title_text='Month')
elif selected_granularity == 'Per quarter':
    fig.update_xaxes(title_text='Quarter')
elif selected_granularity == 'Per year':
    fig.update_xaxes(title_text='Year')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)




st.markdown(f'<h1 style="color: blue; font-size:18px; text-align: center">{"Powerd by Orexine"}</h1>', unsafe_allow_html=True)
