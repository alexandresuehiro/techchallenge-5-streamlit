import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from utils.constantes import TITULO_INDICADORES, TITULO_PRINCIPAL
from utils.layout import output_layout, format_number

from tabs.indicadores.IAN_tab import SobreIAN
from tabs.indicadores.IDA_tab import SobreIDA
from tabs.indicadores.IEG_tab import SobreIEG
from tabs.indicadores.IAA_tab import SobreIAA
from tabs.indicadores.IPS_tab import SobreIPS
from tabs.indicadores.IPP_tab import SobreIPP
from tabs.indicadores.IPV_tab import SobreIPV
from tabs.indicadores.INDE_tab import SobreINDE
from tabs.tab import TabInterface


st.set_page_config(
    page_title=f"{TITULO_INDICADORES} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()


class SobreIndicadoresAvaliacao(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        st.header(f":orange[{TITULO_INDICADORES}]")

        st.markdown(
            """
            Nesta sessão de análise, detalharemos sobre os Indicadores de Avaliação que compõem o INDE:

            Dimensão acadêmica: 
            *	IAN: Indicador de Adequação de Nível (Indicador de Avaliação)
            *	IDA: Indicador de Desempenho Acadêmico (Indicador de Avaliação)
            *   IEG: Indicador de Engajamento (Indicador de Avaliação)

            
            Dimensão psicossocial:
            *   IAA: Indicador de Autoavaliação (Indicador de Avaliação)
            *   IPS: Indicador Psicossocial (Indicador de Conselho)

            Dimensão psicopedagógica:
            *   IPP: Indicador Psicopedagógico (Indicador de Conselho)
            *   IPV: Indicador de Ponto de Virada (Indicador de Conselho)
        """
        )
        # Criando 8 expanders

        # Se você tiver muitas seções, pode utilizar um loop for para simplificar:
        for i in range(1, 9):
            with st.expander(f"INDE"):
                chamarINDE = SobreINDE()
                st.write(chamarINDE)
            with st.expander(f"IAA"):
                chamarIAA = SobreIAA()
            with st.expander(f"IAN"):
                chamarIAN = SobreIAN()
                st.write(chamarIAN)
            with st.expander(f"IDA"):
                chamarIDA = SobreIDA()
                st.write(chamarIDA)
            with st.expander(f"IEG"):
                chamarIEG = SobreIEG()
                st.write(chamarIEG)
            with st.expander(f"IPS"):
                chamarIPS = SobreIPS()
                st.write(chamarIPS)
            with st.expander(f"IPP"):
                chamarIPP = SobreIPP()
                st.write(chamarIPP)
            with st.expander(f"IPV"):
                chamarIPV = SobreIPV()
                st.write(chamarIPV)


        # tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        #     tabs=[
        #         "INDE",
        #         "IAA",
        #         "IAN",
        #         "IDA",
        #         "IEG",
        #         "IPS",
        #         "IPP",
        #         "IPV"
        #     ]
        # )

        # SobreINDE(tab0)
        # SobreIAA(tab1)
        # SobreIAN(tab2)
        # SobreIDA(tab3)
        # SobreIEG(tab4)
        # SobreIPS(tab5)
        # SobreIPP(tab6)
        # SobreIPV(tab7)
    
