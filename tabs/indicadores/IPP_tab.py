import streamlit as st
from tabs.tab import TabInterface


class AnaliseIndicadoresPorPedra(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[IPP – Indicador Psicopedagógico]", divider="blue")
            st.markdown(
                """
                    “Avaliação da equipe de educadores e psicopedagogos para caracterizar o desenvolvimento cognitivo, emocional, comportamental e de socialização do aluno no seu processo de aprendizado dentro do Programa de Aceleração do Conhecimento, dos Programas Educacionais e das Atividades Culturais promovidas pela Associação.” PEDE 2020 (Silva, 2021).
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
