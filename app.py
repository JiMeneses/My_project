import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv(
    'vehicles_us.csv')  # cargar datos

st.header('Anuncios de ventas de autos')  # crear encabezado

hist_checkbox = st.checkbox('Construir histograma')  # crear checkbox
scatter_checkbox = st.checkbox(
    'Construir gráfico de dispersión')  # crear checkbox

if hist_checkbox:

    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')

    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:

    st.write(
        'Creación de gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')

    fig = px.scatter(car_data, y='price', x='odometer')
    st.plotly_chart(fig, use_container_width=True)
