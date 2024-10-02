import streamlit as st
from tabs.tab import TabInterface
import pandas as pd

data35 = pd.read_csv("data/35_ponto_de_Virada_2022.csv", header=0, sep=";")
data36 = pd.read_csv("data/36_cenario_ametista_topazio_topazio.csv", header=0, sep=";")
data37 = pd.read_csv("data/37_cenario_topazio_topazio_topazio.csv", header=0, sep=";")

class PontoVirada2022(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(":blue[Ponto de Virada – 2022]", divider="blue")
            st.markdown(
                """
						Agora vamos analisar um cenário que demonstra uma possível rota de sucesso para os estudantes, que seria o Ponto de Virada = Sim em 2022.
						Para isso, vamos considerar que o estudante está na associação regularmente no período 2020 a 2022.

                """)
            st.dataframe(data35)

            

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
