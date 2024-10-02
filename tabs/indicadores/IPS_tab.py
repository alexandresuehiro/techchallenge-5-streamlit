import streamlit as st
from tabs.tab import TabInterface


class AnaliseIndicadoresPorPedra(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[IPS – Indicador Psicossocial]", divider="blue")
            st.markdown(
                """
                    “Avaliação da equipe de psicólogas para caracterizar o desenvolvimento do aluno nas suas interações familiares, no seu desenvolvimento emocional, comportamental e da sua socialização na vida comunitária. Esse indicador também caracteriza o tipo de atendimento psicológico oferecido pela Associação ao aluno.” PEDE 2020 (Silva, 2021).
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
