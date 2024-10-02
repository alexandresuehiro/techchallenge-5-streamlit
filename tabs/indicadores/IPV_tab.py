import streamlit as st
from tabs.tab import TabInterface


class SobreIPV(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[IPV: Indicador de Ponto de Virada]", divider="blue")
            st.markdown(
                """
                    Avaliação da equipe de educadores e psicopedagogos a respeito do desenvolvimento do aluno das aptidões necessárias para iniciar a transformação da sua vida por meio da Educação, avaliando a integração do aluno à Associação, o seu desenvolvimento emocional, e o seu potencial acadêmico.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
