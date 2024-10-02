import streamlit as st
from tabs.tab import TabInterface


class EducacaoBrasil(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Panorama da Qualidade da Educação Brasileira: Um Desafio Contínuo]", divider="blue")
            st.markdown(
                """
                    A qualidade da educação brasileira é um tema complexo e multifacetado, com avanços e desafios que se entrelaçam. Embora tenhamos visto progressos em alguns indicadores, como a expansão do acesso ao ensino fundamental, ainda há muito a ser feito para garantir uma educação de qualidade para todos os brasileiros.
                                    """)

            st.subheader(":blue[Principais Desafios]", divider="blue")
            st.markdown(
                """
                    * Desigualdade: A qualidade da educação varia significativamente entre as regiões, redes públicas e privadas, e entre as diferentes classes sociais.
                    * Infraestrutura: Muitas escolas, especialmente nas regiões mais carentes, enfrentam problemas de infraestrutura, como falta de materiais didáticos, laboratórios e espaços adequados.
                    * Formação de professores: A formação inicial e continuada dos professores é um ponto crucial para a melhoria da qualidade do ensino, mas ainda há desafios nesse aspecto.
                    * Avaliação: Os sistemas de avaliação da aprendizagem, embora importantes, precisam ser aprimorados para fornecer informações mais precisas sobre o desempenho dos alunos e das escolas.
                    * Financiamento: A educação brasileira enfrenta desafios de financiamento, com recursos muitas vezes insuficientes para atender às demandas.
                                    """)

            st.subheader(":blue[Pontos Positivos e Avanços]", divider="blue")
            st.markdown(
                """
                    * Expansão do acesso: O Brasil tem feito progressos na expansão do acesso à educação, com altas taxas de matrícula no ensino fundamental.
                    * Programas de inclusão: Programas como o Bolsa Família e o ProUni contribuíram para a inclusão social e o acesso à educação superior.
                    * Inovação: A utilização de novas tecnologias e metodologias pedagógicas tem se expandido em algumas escolas.
                    * Discussão e políticas públicas: A educação tem sido tema de debates e políticas públicas, com a busca por soluções para os desafios enfrentados.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
