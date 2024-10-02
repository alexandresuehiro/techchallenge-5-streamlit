import streamlit as st
from tabs.tab import TabInterface


class SobreIEG(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[IEG – Indicador de Engajamento]", divider="blue")
            st.markdown(
                """
                    “Mede o engajamento do aluno nas tarefas curriculares requeridas em cada uma das disciplinas oferecidas na Associação, e/ou seu engajamento em ações de voluntariado desenvolvidas pela Associação.” PEDE 2020 (Silva, 2021).
                    
                    O IEG expressa as entregas das atividades solicitadas para realização nos contraturnos das aulas do Programa de Aceleração do Conhecimento - a lição de casa dos estudantes das Fases 0 até a Fase 7. Para os estudantes da Fase 8, bolsistas universitários, essa é a medida do seu engajamento nas ações disponíveis de voluntariado. Seu valor é a transposição do percentual de entregas para uma base numérica comum (de 0 a 10 pontos).
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
