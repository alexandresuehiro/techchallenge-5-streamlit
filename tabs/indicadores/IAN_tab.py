import streamlit as st
from tabs.tab import TabInterface


class SobreIAN(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[IAN – Indicador de Adequação de Nível]", divider="blue")
            st.markdown(
                """
                    “Registra a defasagem da aprendizagem do aluno por meio da comparação da Fase atual do aluno na Associação com a equivalência das Fases de ensino da Associação e a divisão dos anos escolares do ensino formal (por idade).” PEDE 2020 (Silva, 2021)

                    “O IAN capta a correspondência entre a Fase de Ensino, do Programa de Aceleração do Conhecimento, a qual o estudante estava vinculado no ano corrente, com o ano escolar equivalente e adequado a sua idade. Essa equivalência é determinada pela resolução número 6 do Conselho Nacional de Educação do Ministério da Educação (BRASIL, 2010), que regulamenta a indicação da idade escolar em cada etapa da vida escolar dos estudantes no Brasil.” PEDE 2020 (Silva, 2021)

                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
