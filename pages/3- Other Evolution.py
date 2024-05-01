import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Opportunity",
    page_icon="📝",
)

data = pd.read_excel('Datatest.xlsx')
st.markdown(f'<h1 style="font-size:30px; text-align: center;text-decoration: underline">{"Evolution of income"}</h1>', unsafe_allow_html=True)


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

# Compter le nombre unique de projets et de clients pour chaque période de temps
projects_count = data.groupby('Time Granularity')['Opportunity Name'].nunique().reset_index()
clients_count = data.groupby('Time Granularity')['Account Name'].nunique().reset_index()

# Créer un graphique avec deux courbes (projets et clients)
fig = go.Figure()

# Ajouter la courbe pour le nombre de projets
fig.add_trace(go.Scatter(x=projects_count['Time Granularity'], y=projects_count['Opportunity Name'],
                         mode='lines+markers', name='Number of projects', line=dict(color='blue')))

# Ajouter la courbe pour le nombre de clients
fig.add_trace(go.Scatter(x=clients_count['Time Granularity'], y=clients_count['Account Name'],
                         mode='lines+markers', name='Number of clients', line=dict(color='red')))

# Mettre à jour les étiquettes de l'axe des x en fonction de la granularité
if selected_granularity == 'Per month':
    fig.update_xaxes(title_text='Month')
elif selected_granularity == 'Per quarter':
    fig.update_xaxes(title_text='Quarter')
elif selected_granularity == 'Per year':
    fig.update_xaxes(title_text='Year')

# Mettre à jour les étiquettes de l'axe des y
fig.update_yaxes(title_text='Number')

# Mettre à jour le titre du graphique
fig.update_layout(title='Evolution of the number of projects and clients')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)


st.markdown(f'<h1 style="color: blue; font-size:18px; text-align: center">{"Powerd by Orexine"}</h1>', unsafe_allow_html=True)
