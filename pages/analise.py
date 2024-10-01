import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from utils.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from utils.layout import output_layout, format_number

from tabs.analises.SobreIndicadoresAvaliacao_tab import SobreIndicadoresAvaliacao
from tabs.analises.PerfilEstudantes_tab import PerfilEstudantes
from tabs.analises.AnaliseIndicadoresPorPedra_tab import AnaliseIndicadoresPorPedra
from tabs.analises.MapaCorrelacaoIndicadores_tab import MapaCorrelacaoIndicadores
from tabs.analises.AnaliseTransicaoPedras_tab import AnaliseTransicaoPedras
from tabs.analises.PontoVirada2022_tab import PontoVirada2022
from tabs.analises.AnalisePontoVirada2022Sim_tab import AnalisePontoVirada2022Sim


st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()


with st.container():
    st.header(f":orange[{TITULO_ANALISE_EXPLORATORIA}]")

    st.markdown(
        """
        Nesta sessão de análise, detalharemos um pouco sobre: 
            1 - Sobre Indicadores de Avaliação: indicadores internos sobre o perfil de cada jovem
            2 - Perfil dos Estudantes: análise de idade, tipo de escola, valor de INDE etc
            3 - Análise dos Indicadores por Pedra: um escrutínio sobre a relevância de cada Indicador e o peso sobre o perfil das pedras
            4 - 
    """
    )

    tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        tabs=[
            "Sobre Indicadores de Avaliação",
            "Perfil dos Estudantes",
            "Análise dos Indicadores por Pedra",
            "Mapa de Correlação de Indicadores",
            "Análise de Transição de Pedras",
            "Ponto de Virada 2022",
            "Análise do Ponto de Virada 2022 = Sim"
        ]
    )

    SobreIndicadoresAvaliacao(tab0)
    PerfilEstudantes(tab1)
    AnaliseIndicadoresPorPedra(tab2)
    MapaCorrelacaoIndicadores(tab3)
    AnaliseTransicaoPedras(tab4)
    PontoVirada2022(tab5)
    AnalisePontoVirada2022Sim(tab6)

 
