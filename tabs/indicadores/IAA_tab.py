import streamlit as st
from tabs.tab import TabInterface


class SobreIAA(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[IAA – Indicador de Autoavaliação ]", divider="blue")
            st.markdown(
                """
                    “Registra por meio de um questionário padronizado e adaptado às distintas faixas etárias dos alunos a Associação, uma autoavaliação do aluno sobre como se sente consigo mesmo, sobre os estudos, sobre sua família, amigos e comunidade, e sobre como se sente a respeito da Associação Passos Mágicos.”  PEDE 2020 (Silva, 2021).
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
