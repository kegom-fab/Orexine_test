import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Opportunity",
    page_icon="📝",
)

data = pd.read_excel('Datatest.xlsx')
st.markdown(f'<h1 style="font-size:30px; text-align: center;text-decoration: underline">{"Classification of opportunities"}</h1>', unsafe_allow_html=True)

# Ajouter une nouvelle colonne contenant la somme des revenus des deux colonnes
data['Total Revenue'] = data['1st Year Revenue (Merged)'] + data['Revenue Weightage (next year)']
# Tri des données par revenu total (du plus petit au plus grand)
data_sorted = data.sort_values(by='Total Revenue')
# Ajouter une colonne pour le trimestre (en tant que chaîne de caractères)
data['Quarter'] = data['Created Date'].dt.to_period('Q').astype(str)

# Demander à l'utilisateur le nombre de projets à afficher
chosen_option = st.number_input("Nombre de projets les plus rentables à afficher par trimestre: ", min_value=1, value=5)
# Trouver les projets les plus rentables pour chaque trimestre
top_profitable_per_quarter = data.groupby('Quarter').apply(lambda x: x.nlargest(chosen_option, 'Total Revenue')).reset_index(drop=True)
# Créer un graphique à barres
fig = px.bar(top_profitable_per_quarter, x='Quarter', y='Total Revenue', color='Opportunity Name', 
             title=f'{chosen_option} projets les plus rentables pour chaque trimestre', 
             labels={'Quarter': 'Trimestre', 'Total Revenue': 'Revenu total', 'Opportunity Name': 'Nom du projet'})

# Afficher le graphique
st.plotly_chart(fig)
st.markdown(f'<h2 style="font-size:30px; text-align: center;text-decoration: underline">{"Une vue globale sur lensemble des années"}</h2>', unsafe_allow_html=True)
# Sélectionner les projets les plus ou moins rentables selon le choix de l'utilisateur
option = st.selectbox("Choisissez de voir les projets les :", ['Plus rentables', 'Moins rentables'])
if option == 'Plus rentables':
    top_projects = data_sorted.tail(10)
    title = 'Les 10 projets les plus rentables'
else:
    top_projects = data_sorted.head(10)
    title = 'Les 10 projets les moins rentables (si rien ne saffiche ca veut dire que les revenus sont à 0)'
# Vérifier si tous les revenus sont à 0
if top_projects['Total Revenue'].sum() == 0:
    st.write("Aucune donnée à afficher car les revenus sont nuls, egale à 0.")
else:
    # Créer un graphique en camembert
    fig = px.pie(top_projects, values='Total Revenue', names='Opportunity Name', title=title)

    # Afficher le graphique
    st.plotly_chart(fig)
if option == 'Plus rentables':
    st.write("Top 10 of more profitable :")
    st.write(data_sorted.tail(10)[['Opportunity Name', 'Account Name','Created Date','Stage','1st Year Revenue (Merged)','Revenue Weightage (next year)', 'Total Revenue']].reset_index(drop=True))
elif option == 'Moins rentables':
    st.write("Top 10 of less profitable :")
    st.write(data_sorted.head(10)[['Opportunity Name', 'Account Name','Created Date','Stage','1st Year Revenue (Merged)','Revenue Weightage (next year)', 'Total Revenue']].reset_index(drop=True))


# Compter le nombre de projets par trimestre
projects_per_quarter = data.groupby('Quarter').size().reset_index(name='Number of Projects')
# Créer un graphe avec Plotly Express
fig = px.line(projects_per_quarter, x='Quarter', y='Number of Projects', title='Nombre de projets par trimestre')
# Afficher le graphe
st.plotly_chart(fig)

# Afficher la liste des projets pour le trimestre sélectionné
selected_quarter = st.selectbox("Sélectionner un trimestre", projects_per_quarter['Quarter'].unique())
projects_in_selected_quarter = data[data['Quarter'] == selected_quarter]
st.write("Liste des projets pour le trimestre sélectionné :")
st.write(projects_in_selected_quarter[['Opportunity Name', 'Account Name', 'Created Date', 'Stage']])
st.markdown(f'<h1 style="color: blue; font-size:18px; text-align: center">{"Powerd by Orexine"}</h1>', unsafe_allow_html=True)
