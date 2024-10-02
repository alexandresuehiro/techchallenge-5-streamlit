import streamlit as st
from tabs.tab import TabInterface

import pandas as pd

data35 = pd.read_csv("data/35_ponto_de_Virada_2022.csv", header=0, sep=";")
data36 = pd.read_csv("data/36_cenario_ametista_topazio_topazio.csv", header=0, sep=";")
data37 = pd.read_csv("data/37_cenario_topazio_topazio_topazio.csv", header=0, sep=";")

class AnalisePontoVirada2022Sim(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(":blue[Análise de Indicadores para Ponto de Virada 2022 = Sim]", divider="blue")    
			
            st.subheader('Cenário Ametista - Topázio - Topázio')                       
            st.markdown(
                """
						Para esses casos, vamos olhar diretamente nos Indicadores IPP, IEG e IPV para o cenário Ametista  Topázio  Topázio e fazermos uma média de todos os Indicadores nos três anos:
                """)
  
            st.dataframe(data36)
            st.markdown(
                """
						Observando os Indicadores ano a ano e agrupados, vemos que há quedas entre anos para um indicador, porém outro indicador do trio compensa essa queda. Vale observar que na penúltima linha há um caso de alguém que se recuperou de um IPP baixo em 2020 e compensou na média com Indicador de Engajamento igual a dez durante os três anos.
                """)

            st.subheader('Cenário Topázio - Topázio - Topázio')
            st.markdown(
                """ 
						Para esses casos, vamos olhar diretamente nos Indicadores IPP, IEG e IPV para o cenário Topázio - Topázio - Topázio e fazermos uma média de todos os Indicadores nos três anos:
                """)
            st.dataframe(data37)

            st.markdown(
                """ 
						Este cenário vale a pena analisar com um pouco mais de atenção por ser um quadro muito estável ao longo de três anos. Apesar terem certos períodos de queda num indicador como queda no IPP, porém há compensação no IPV.
                """)
            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
