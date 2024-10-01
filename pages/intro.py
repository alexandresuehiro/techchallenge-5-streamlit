import streamlit as st
from tabs.intro.ipea_tab import IntroIPEATab
from tabs.intro.meta_prophet import IntroMetaProphet
from tabs.intro.petroleo_brent_tab import IntroPetroleoBrentTab
from tabs.intro.arima_method import IntroARIMA
from utils.constantes import TITULO_INTRODUCAO, TITULO_PRINCIPAL
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_INTRODUCAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_INTRODUCAO}]")

    st.markdown(
        """
        Nesta introdução, são descritos alguns tópicos importantes para entender a missão da Passos Mágicos e os modelos de Machine Learning usados: o Meta Prophet e o ARIMA.
    """
    )

    tab0, tab1, tab2, tab3 = st.tabs(
        tabs=[
            "Passos Mágicos",
            "Educação no Brasil x Educação em Embu-Guaçú",
            "Regressão Linear",
            "Decision Tree - Classification",
            "Random Forest - Classification",
            "Decision Tree - Regression",
            "Random Forest - Regression",
            "Regressão Linear",
        ]
    )

    IntroPetroleoBrentTab(tab0)
    IntroIPEATab(tab1)
    IntroMetaProphet(tab2)
    IntroARIMA(tab3)
