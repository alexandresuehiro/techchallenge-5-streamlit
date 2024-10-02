import streamlit as st
from tabs.tab import TabInterface


class AnaliseIndicadoresPorPedra(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[IDA – Indicador de Desempenho Acadêmico]", divider="blue")
            st.markdown(
                """
                    “Registra a proficiência do aluno nos exames padronizados de avaliação interna das disciplinas oferecidas pela Associação (os alunos das Fases 0 a 7). No caso dos alunos da Fase 8, esse indicador registra a nota média obtida pelos alunos em todas as disciplinas curriculares cursadas, nas respectivas instituições de ensino superior conveniadas ao programa de bolsas de estudo da Associação” PEDE 2020 (Silva, 2021)

                    O IDA expressa a proficiência dos estudantes da Fase 0 (alfabetização), até a Fase 7 (3° ano do ensino médio), nas provas aplicadas pela Associação Passos Mágicos, numa mesma base numérica (de 0 a 10 pontos). Para esses estudantes essa é uma medida uniforme de avaliação, pois essas provas se referem aos conteúdos, e às habilidades associadas a esses conteúdos, que foram desenvolvidos no contexto do Programa de Aceleração do Conhecimento. Para os estudantes da Fase 8, bolsistas universitários, esse indicador expressa a média anual das avaliações de cada disciplina cursada em seus respectivos cursos, na mesma base numérica (de 0 a 10 pontos).

                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
