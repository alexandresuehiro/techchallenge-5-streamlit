import streamlit as st
from tabs.modelo.machine_learning_models_tab import ModelosMachineLearningTab
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
        Prever sucesso é algo complexo e depende de muitos fatores, principalmente sobre a jornada de um ser humano.
        O que define sucesso? Ou o que define indicativos de sucesso?

        Para essa situação, chegar à faculdade? Um curso técnico? Concluir o Ensino Médio e ter um projeto de vida?
        Por isso deixamos em aberto o que podemos considerar como marca de sucesso ao avaliar os jovens...

        Importante notar que estamos considerando os alunos que possuem três anos consecutivos na Passos Mágicos para realizar a avaliação.
    """
    )

    tab0 = st.tabs(tabs=["Previsões"])

    ModelosMachineLearningTab(tab0)