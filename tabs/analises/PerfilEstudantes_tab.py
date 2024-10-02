import streamlit as st
from tabs.tab import TabInterface
import pandas as pd


data1 = pd.read_csv("data/01_ingressantes_veteranos.csv", header=0, sep=";")
data2 = pd.read_csv("data/02_ano_ingresso.csv", header=0, sep=";")
data3 = pd.read_csv("data/03_instituicao_ensino.csv", header=0, sep=";")
data4 = pd.read_csv("data/04_perfil_fase.csv", header=0, sep=";")
data5 = pd.read_csv("data/05_perfil_pedra_INDE.csv", header=0, sep=";")

class PerfilEstudantes(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(":blue[Perfil dos Estudantes]", divider="blue")
            st.subheader('Ingressantes e Veteranos') 
            st.markdown(
                """
                    De acordo com as informações obtidas da base de dados, havia cerca de 725 estudantes ao longo de 2020, 685 em 2021 e 862 em 2022:
                """)
            st.dataframe(data1)
            st.subheader('Ano de Ingresso') 
            st.markdown(
                """
                        Ainda analisando o tempo de início dos estudantes, temos o quadro abaixo:
                """)
            st.dataframe(data2)
            st.image('assets/imgs/01_qtde_veteranos.png')
            st.markdown(
                """
                        Houve um acréscimo considerável em 2022, com o ingresso de 398 estudantes na associação (aumento de 200% em relação a 2020).
                """) 
            st.subheader('Escola Pública, Bolsistas e Universitários')                       
            st.markdown(
                """     
                        Considerando todos aqueles do Ensino Fundamental e do Ensino Médio como alunos de Escola Pública ou Bolsistas, temos:

                """)    
                                
            st.markdown(
                """     
                        Quanto ao perfil estudantil, temos a seguinte composição:
                """)
            st.dataframe(data3)
            st.subheader('Perfil por Fase')
            st.markdown(
                """
                        Quanto ao perfil por fase, temos a seguinte composição:
                """)
            st.dataframe(data4)
            st.image('assets/imgs/02_qtde_estudantes_fase.png')
            st.subheader('Perfil por Pedra / INDE')

            st.dataframe(data5)
            st.image('assets/imgs/quantidade_perfis_pedras_2020_2022.png')
            st.markdown(
                """ 
A quantidade de estudantes nos perfis Ágata, Ametista e Topázio tiveram aumento maior que o Quartzo, ou seja, há maior porcentagem de estudantes com INDE de valores mais altos.

                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
