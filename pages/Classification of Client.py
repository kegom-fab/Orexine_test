import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Opportunity",
    page_icon="📝",
)

data = pd.read_excel('Datatest.xlsx')
st.markdown(f'<h1 style="font-size:30px; text-align: center;text-decoration: underline">{"Classification of clients"}</h1>', unsafe_allow_html=True)
# Ajouter une nouvelle colonne contenant la somme des revenus des deux colonnes
data['Total Revenue'] = data['1st Year Revenue (Merged)'] + data['Revenue Weightage (next year)']
# Regrouper les données par client et calculer le total des revenus générés par chaque client
revenue_by_client = data.groupby('Account Name')['Total Revenue'].sum().reset_index()

# Calculer l'année du dernier projet pour chaque client
last_project_year = data.groupby('Account Name')['Target Go-Live date'].max().reset_index()
last_project_year.columns = ['Account Name', 'Last Project Year']

# Calculer le nombre total de projets pour chaque client
projects_by_client = data.groupby('Account Name')['Opportunity Name'].nunique().reset_index()
projects_by_client.columns = ['Account Name', 'Number of Projects']

# Fusionner les données de revenus, d'année de dernier projet et de nombre de projets par client
merged_data = pd.merge(revenue_by_client, last_project_year, on='Account Name')
merged_data = pd.merge(merged_data, projects_by_client, on='Account Name')

# Trier les clients en fonction du montant total des revenus (du plus élevé au plus bas)
merged_data_sorted = merged_data.sort_values(by='Total Revenue', ascending=False)

# Widget de sélection du nombre de clients
selected_clients = st.slider('Sélectionnez le nombre de clients à afficher', min_value=1, max_value=min(20, merged_data_sorted.shape[0]), value=5)

# Sélectionner les premiers clients en fonction du nombre choisi
top_clients_filtered = merged_data_sorted.head(selected_clients)

# Tracer le diagramme en barres pour visualiser les revenus des clients
fig = px.bar(top_clients_filtered, x='Account Name', y='Total Revenue', hover_data={'Last Project Year': True, 'Number of Projects': True},
             color='Number of Projects', color_continuous_scale='viridis', labels={'Account Name': 'Client', 'Total Revenue': 'Revenus'})

# Mettre à jour le titre du graphique
fig.update_layout(title=f'Top {selected_clients} des clients avec les plus hauts revenus, leurs derniers projets et le nombre de projets')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)

# Ajouter une colonne pour l'unité de temps choisie par l'utilisateur (mois, trimestre ou année)
unit_of_time = st.selectbox("Sélectionnez l'unité de temps", ["Mois", "Trimestre", "Année"])

if unit_of_time == "Mois":
    data['Time Unit'] = data['Created Date'].dt.to_period('M').astype(str)
elif unit_of_time == "Trimestre":
    data['Time Unit'] = data['Created Date'].dt.to_period('Q').astype(str)
else:
    data['Time Unit'] = data['Created Date'].dt.to_period('Y').astype(str)

# Compter le nombre de clients par unité de temps
clients_by_time_unit = data.groupby('Time Unit')['Account Name'].nunique().reset_index()

# Tracer le graphique
fig = px.bar(clients_by_time_unit, x='Time Unit', y='Account Name', 
             labels={'Time Unit': f'{unit_of_time}', 'Account Name': 'Nombre de Clients'},
             title=f'Nombre de Clients par {unit_of_time}')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)
st.markdown(f'<h1 style="color: blue; font-size:18px; text-align: center">{"Powerd by Orexine"}</h1>', unsafe_allow_html=True)
