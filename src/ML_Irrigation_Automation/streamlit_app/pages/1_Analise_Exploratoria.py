import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd
import os

main_path = os.path.dirname(__file__).removesuffix('pages')
data_path = os.path.join(main_path, 'produtos_agricolas.csv')

@st.cache_data
def load_data():
    data = pd.read_csv(data_path)
    return data

df = load_data()

st.write('Caso quiser, você pode baixar a base de dados que serão utilizados para a visualização abaixo:')

csv = df.to_csv()
st.download_button(label="Baixar csv com dados",
                   data=csv,
                   file_name='produtos_agricolas.csv',
                   mime='text/csv')

# Exibe as 5 primeiras linhas
st.subheader("5 primeiras linhas do dataset:")
st.write(df.head())

# Matriz de Correlação
st.subheader("Matriz de Correlação entre as variáveis")
corr = df.select_dtypes(include=['int64', 'float64', 'bool']).corr()
fig_corr, ax_corr = plt.subplots(figsize=(12,6))
sns.heatmap(data=corr, annot=True, cmap='coolwarm', ax=ax_corr)
st.pyplot(fig_corr)

# Gráfico de Dispersão interativo
st.subheader("Gráfico de dispersão interativo")
col1, col2 = st.columns(2)
with col1:
    x_axis = st.selectbox("Selecione o eixo X", df.select_dtypes(include=['int64','float64']).columns)
with col2:
    y_axis = st.selectbox("Selecione o eixo Y", df.select_dtypes(include=['int64','float64']).columns)
cultures = st.multiselect("Selecione as culturas que deseja visualizar no gráfico de dispersão", df['culture'].unique())

if cultures:
    df_filtered = df[df['culture'].isin(cultures)]
else:
    df_filtered = df

fig_scatter = px.scatter(
    df_filtered,
    x=x_axis,
    y=y_axis,
    color='culture',
    title=f'Relação entre {x_axis} e {y_axis}',
    labels={x_axis: x_axis, y_axis: y_axis},
    template="plotly_white"
)
st.plotly_chart(fig_scatter)