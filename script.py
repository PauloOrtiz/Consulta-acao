import streamlit as st
import yfinance as yf
import pandas as pd

# Título da aplicação
st.title('Visualizador de Ações')

# Input do usuário para o ticker da ação
ticker = st.text_input('Digite o ticker da ação (ex: PETR4.SA, AAPL):')

# Botão para buscar as informações
if st.button('Buscar Informações'):
    # Verifica se o ticker não está vazio

    st.write(ticker)
    if ticker:
        # Busca os dados da ação
        acao = yf.Ticker(ticker)
        st.write(acao)
        # Pega as informações
        info = acao.info
        if 'companyOfficers' in info:
            del info['companyOfficers']
        st.write(info)
        dataframe = pd.DataFrame([info])

        st.dataframe(dataframe)
        
    else:
        st.error("Por favor, digite um ticker.")
