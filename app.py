import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header('Análisis Exploratorio de Datos de Vehículos')

car_data = pd.read_csv('vehicles_us.csv')

hist_checkbox = st.checkbox('Construir Histograma')

if hist_checkbox:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear histográma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # demos título al gráfico
    fig.update_layout(title_text='Distribución del Odómetro',
                      xaxis_title='Lectura del Odómetro', yaxis_title='Cantidad de Anuncios')

    # Mostrar gráfico interactivo en Streamlit
    st.plotly_chart(fig, use_container_width=True)


scatt_checkbox = st.checkbox('Construir Diagrama de Dispersión')

if scatt_checkbox:
    st.write('Construir un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = go.Figure(data=go.Scatter(
        x=car_data['odometer'], y=car_data['price'], mode='markers'))

    fig.update_layout(
        title_text='Diagrama de Dispersión del Precio vs Odómetro', xaxis_title='Odómetro', yaxis_title='Precio')

    st.plotly_chart(fig, use_container_width=True)
