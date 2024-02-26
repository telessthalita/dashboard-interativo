import streamlit as st
import pandas as pd
import plotly.express as px

# Configurando a página para um layout amplo
st.set_page_config(layout="wide")

# Carregando os dados
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Adicionando uma coluna para o mês
df["Month"] = df["Date"].dt.to_period('M')

# Sidebar para seleção do mês
month = st.sidebar.selectbox("Selecione o Mês", df["Month"].unique())

# Filtrando os dados pelo mês selecionado
df_filtered = df[df["Month"] == month]

# Dividindo a tela em colunas
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia", color_discrete_sequence=px.colors.qualitative.Vivid)
col1.plotly_chart(fig_date, use_container_width=True)

# Gráfico de faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Date", y="Product line", 
                  color="City", title="Faturamento por tipo de produto",
                  orientation="h", color_discrete_sequence=px.colors.qualitative.Vivid)
col2.plotly_chart(fig_prod, use_container_width=True)

# Faturamento total por filial
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total",
                   title="Faturamento por filial", color="City", color_discrete_sequence=px.colors.qualitative.Vivid)
col3.plotly_chart(fig_city, use_container_width=True)

# Gráfico de distribuição do tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                   title="Distribuição do faturamento por tipo de pagamento", color_discrete_sequence=px.colors.qualitative.Vivid)
col4.plotly_chart(fig_kind, use_container_width=True)

# Avaliação média por filial
city_avg_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_avg_rating, x="City", y="Rating",
                    title="Avaliação Média por Filial", color="City", color_discrete_sequence=px.colors.qualitative.Vivid)
col5.plotly_chart(fig_rating, use_container_width=True)
