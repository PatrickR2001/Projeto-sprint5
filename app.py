import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('../datasets/vehicles.csv')




build_scatter_plot = st.checkbox("Criar gráfico de dispersão")

if build_scatter_plot:
    st.write(
        "Criando um gráfico de dispersão para comparar a relação odomometro X preço do veiculo")

    fig = px.scatter(df, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)


hist_button = st.button('Criar histograma')

if hist_button:
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            fig = px.histogram(df, x="odometer")
            st.plotly_chart(fig, use_container_width=True)