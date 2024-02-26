# Dashboard de Análise de Vendas em Supermercado

Este é um aplicativo Streamlit que oferece uma análise interativa das vendas de um supermercado, utilizando dados de vendas fornecidos em um arquivo CSV.

## Como Executar

1. Certifique-se de ter o Python instalado em seu ambiente.
2. Instale os requisitos do projeto utilizando o seguinte comando:
    ```
    pip install -r requirements.txt
    ```
3. Execute o aplicativo Streamlit com o seguinte comando:
    ```
    streamlit run app.py
    ```

## Recursos

### Análise de Vendas

- **Faturamento por Dia**: Visualize o faturamento diário por cidade em um gráfico de barras.
- **Faturamento por Tipo de Produto**: Explore o faturamento por tipo de produto ao longo do tempo em um gráfico de barras horizontal.
- **Faturamento Total por Filial**: Veja o faturamento total por filial em um gráfico de barras.
- **Distribuição do Tipo de Pagamento**: Analise a distribuição do faturamento por tipo de pagamento em um gráfico de pizza.
- **Avaliação Média por Filial**: Observe a avaliação média por filial em um gráfico de barras.


## Fontes de Dados

Os dados de vendas utilizados neste aplicativo são provenientes do arquivo CSV `supermarket_sales.csv`.

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/): Framework para criação de aplicativos da web interativos com Python.
- [Pandas](https://pandas.pydata.org/): Biblioteca para manipulação e análise de dados.
- [Plotly Express](https://plotly.com/python/plotly-express/): Biblioteca para visualização de dados interativos.
