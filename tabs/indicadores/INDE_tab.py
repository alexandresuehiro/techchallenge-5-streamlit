import streamlit as st
from tabs.tab import TabInterface


class SobreINDE(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[INDE - Índice de Desenvolvimento Educacional]", divider="blue")
            st.markdown(
                """
                    Este índice é composto a partir dos índices citados anteriormente, porém a função varia de acordo com a fase do estudante.

                    Fases 0 a 7
                    
                    Para estudantes das fases 0 a 7 (estudantes do Ensino Fundamental e Médio), temos a seguinte função:

                        INDE = IAN x 0,1 + IDA x 0,2 + IEG x 0,2 + IAA x 0,1 + IPS x 0,1 + IPP x 0,1 + IPV x 0,2

                    Notar que todos os índices têm seu percentual de importância, com maior peso para o IDA (Índice de Desempenho Acadêmico), IEG (Índice de Engajamento) e o IPV (Índice de Ponto de Virada). 

                    
                    Fase 8
                    
                    Para estudantes da fase 8 (universitários, estudantes de curso técnico, tecnólogos), temos a seguinte função:

                        INDE = IAN x 0,1 + IDA x 0,4 + IEG x 0,2 + IAA x 0,1 + IPS x 0,2

                    Para os estudantes dessa fase, o mais crítico é o IDA (Índice de Desempenho Acadêmico). Nesta avaliação do INDE não considera o IPP (Índice psicopedagógico) e o IPV (Índice de Ponto de Virada). 
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
