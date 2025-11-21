import streamlit as st
import pandas as pd
import plotly.express as px



datos = pd.read_csv('data/vehicles_us.csv')

st.header('Análisis de anuncios de ventas de autos')

tabla_check = st.checkbox('Mostrar datos')
if tabla_check:
    st.write('EDA: tabla de datos')
    st.dataframe(datos)

hist_check = st.checkbox('Mostrar histograma')
if hist_check:
    st.write('Histograma: Distribución del odómetro de los autos en venta')

    min_odo = int(datos['odometer'].min())
    max_odo = int(datos['odometer'].max())

    rango = st.slider(
        'Selecciona el rango de odómetro',
        min_odo,
        max_odo,
        (min_odo, max_odo)
    )

    datos_filtrados = datos[
        (datos['odometer'] >= rango[0]) &
        (datos['odometer'] <= rango[1])
    ]

    hist = px.histogram(
        datos_filtrados,
        x='odometer',
        nbins=30,
        title='Distribución del odómetro'
    )
    st.plotly_chart(hist, use_container_width=True)

disp_check = st.checkbox('Mostrar gráfico de dispersión')
if disp_check:
    st.write('Relación entre odómetro y precio')
    fig = px.scatter(
        datos,
        x='odometer',
        y='price',
        title='Odómetro vs Precio',
        opacity=0.5
    )
    st.plotly_chart(fig, use_container_width=True)

scatter_check = st.checkbox('Mostrar gráfico de dispersión')

if scatter_check:
    st.write('Gráfico de dispersión: relación entre odómetro y precio')
    fig2 = px.scatter(datos, x='odometer', y='price', opacity=0.5)
    st.plotly_chart(fig2)