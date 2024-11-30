import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os
import joblib

main_path = os.path.dirname(__file__).removesuffix('pages')
model_path = os.path.join(main_path, 'irrigation_automation_model_pipeline.joblib')

@st.cache_data
def load_model():
    return joblib.load(model_path)

model = load_model()

df_example = pd.DataFrame({
    "N": ['int64'],
    "P": ['int64'],
    "K": ['int64'],
    "temperature": ['float64'],
    "humidity": ['float64'],
    "ph": ['float64'],
    "rainfall": ['float64'],
    "culture": ['string']
})

st.subheader('Previsão dos dados sobre Irrigação Automática')
st.write('O modelo irá prever a necessidade de irrigação baseado nos fatores climáticos (temperatura, humidade e precipitação).')

st.write("O modelo a seguir aceita os seguintes dados para realizar a previsão: ")
st.write(df_example)

st.write("""
         Porém, como dito anteriormente, o modelo apenas irá considerar os dados sobre fatores climáticos, 
         demais dados não serão considerados neste momento.
         """)

# Planilha csv com os novos dados a serem previstos
up_file = st.file_uploader('Escolha um arquivo CSV para realizar a previsão.', type='csv')

# Processa o arquivo
if up_file is not None:
    df = pd.read_csv(up_file)

    # Exibe os 5 primeiros registros
    st.subheader('5 primeiros registros da planilha importada:')
    st.write(df.head())

    data = df[['temperature','humidity','rainfall']]

    predicts = model.predict(data)

    st.subheader('5 primeiros registros dos resultados:')
    st.write('Os valores previstos estão na coluna "irrigação_ligada".')
    df.insert(0, 'irrigacao_ligada', predicts)

    # Exibe os 5 primeiros resultados
    st.write(df.head())

    csv = df.to_csv(index=False)

    # Botão para realizar o download
    st.download_button(label='Baixar resultados',
                       data=csv,
                       file_name='produtos_agricolas_irrigação.csv',
                       mime='text/csv')
    
    # Gráfico para visualizar a importância de cada variável para a previsão dos valores
    st.subheader('Importância de cada variável na previsão:')
    fig, ax = plt.subplots(figsize=(12,6))
    ax.barh(data.columns, model.named_steps['estimator'].feature_importances_, color='skyblue')
    ax.set_xlabel("Importância Relativa")
    ax.set_ylabel("Atributos")
    ax.set_title('Importância das Variáveis para o problema de Irrigação Automática')

    st.pyplot(fig)