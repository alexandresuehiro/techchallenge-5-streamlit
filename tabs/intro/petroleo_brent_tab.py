import streamlit as st
from tabs.tab import TabInterface

class IntroPetroleoBrentTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Petróleo Brent]', divider='blue')
            st.markdown('''
                        Brent é uma sigla, que normalmente acompanha a cotação do petróleo e indica a origem do óleo e o mercado onde ele é negociado. O petróleo Brent foi batizado assim porque era extraído de uma base da Shell chamada Brent. Atualmente, a palavra Brent designa todo o petróleo extraído no Mar do Norte e comercializado na Bolsa de Londres.
                        A cotação do mercado nos afeta diretamente, influenciando no preço de seus derivados como óleo diesel e a gasolina. Impactando o preço do transporte, afetando todas as mercadorias e amplamente negociado nos mercados internacionais de commodities. Seu preço é influenciado por uma série de fatores, incluindo a oferta e demanda globais, eventos geopolíticos, políticas de produção da OPEP e condições econômicas mundiais.
            ''')