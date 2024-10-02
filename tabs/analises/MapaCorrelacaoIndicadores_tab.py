import streamlit as st
from tabs.tab import TabInterface
import pandas as pd


class MapaCorrelacaoIndicadores(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(":blue[Mapa de Correlação dos Indicadores]", divider="blue")
            st.markdown(
                """
                    Considerando os mapas, os indicadores psicológicos têm forte correlação entre si, além do indicador de engajamento. Pelo mapa, vemos que o IPP, IPV, IPS e IEG têm forte correlação, logo analisar o perfil dos estudantes pelas pedras e qual dos indicadores teriam maior peso poderia indicar um ponto a ser trabalhado.
                """)
            st.subheader('Mapa de Correlação dos Indicadores – 2020') 
            st.image('assets/imgs/01_mapa_correlacao_2020.png')
            st.markdown(
                """
                    Se olharmos o IPV como um fator crítico que determina a evolução do aprendizado e observamos as correlações maiores no seu entorno, podemos dizer que o IPP e o IPS têm peso considerável no ano de 2020.
                """)


            st.subheader('Mapa de Correlação dos Indicadores - 2021') 

            st.image('assets/imgs/01_mapa_correlacao_2021.png')

            st.markdown(
                """
                    O cenário em 2021 se repete ao de 2020, porém o IEG teve uma correlação maior (0.90  0.95), o que poderia implicar na compensação pela queda do IPP.
                """) 

            st.subheader('Mapa de Correlação dos Indicadores - 2022')                       
  
            st.image('assets/imgs/01_mapa_correlacao_2022.png')


            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
