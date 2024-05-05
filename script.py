import streamlit as st
import yfinance as yf
import pandas as pd
import io

# Título da aplicação
st.title('Visualizador de Ações')

# Input do usuário para o ticker da ação
ticker = st.text_input('Digite o ticker da ação (ex: PETR4.SA, AAPL):')

# Botão para buscar as informações
if st.button('Buscar Informações'):
    if ticker:  # Verifica se o ticker não está vazio
        # Busca os dados da ação
        acao = yf.Ticker(ticker)
        # Pega as informações
        info = acao.info

        # Remove a chave 'companyOfficers' se presente
        if 'companyOfficers' in info:
            del info['companyOfficers']

        # Cria um DataFrame com uma lista contendo o dicionário
        dataframe = pd.DataFrame([info])

        # Mostra o DataFrame no Streamlit
        st.dataframe(dataframe)

        # Cria um objeto BytesIO para salvar o DataFrame como Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            dataframe.to_excel(writer, index=False)

        # Prepara o botão de download
        st.download_button(
            label="Baixar dados em formato Excel",
            data=output.getvalue(),
            file_name="dados_acao.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.error("Por favor, digite um ticker.")