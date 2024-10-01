import streamlit as st
from tabs.modelo.arima_tab import ModeloARIMATab
from tabs.modelo.prophet_tab import ModeloProphetTab
from utils.constantes import TITULO_MODELO, TITULO_PRINCIPAL
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_MODELO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_MODELO}]")

    st.markdown(
        """
        Prever o preço do barril de petróleo é um desafio crítico para muitos setores, e tanto o :blue[Prophet] quanto a :blue[ARIMA] são ferramentas valiosas nessa tarefa. O que torna complexa é a capacidade de um algoritmo prever sazonalidades ou eventos incomuns, como pandemias ou atentados, por isso uma análise mais profunda pode ser necessária além do escopo oferecido até aqui.
    """
    )

    tab0, tab1 = st.tabs(tabs=["Meta Prophet", "ARIMA"])

    ModeloProphetTab(tab0)
    ModeloARIMATab(tab1)
