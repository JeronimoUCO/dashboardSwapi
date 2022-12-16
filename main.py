import streamlit as st
import pandas as pd
import plotly.express as px

personajes=pd.read_csv("data.csv")

grafica_especies = px.pie(personajes, names='species', title='Especie de cada personaje')
grafica_alturas=px.line(personajes,x='name',y='height',title="Altura de cada personaje")
grafica_mass=px.scatter(personajes,x='name',y='mass',title="Peso de cada personaje")


st.title("Personajes de Star Wars")
#st.table(personajes)
st.plotly_chart(grafica_especies)
st.plotly_chart(grafica_alturas)
st.plotly_chart(grafica_mass)
