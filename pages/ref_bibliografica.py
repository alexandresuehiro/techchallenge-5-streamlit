import streamlit as st
from utils.constantes import TITULO_PRINCIPAL, TITULO_REFERENCIAS
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_REFERENCIAS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_REFERENCIAS}]")
    
    st.markdown(
        """
        1. Petróleo Brent em: https://en.wikipedia.org/wiki/Brent_Crude
        2. Sobre o IPEA em: https://www.ipea.gov.br/portal/coluna-3/institucional-sep/quem-somos
        3. Impactos da Guerra da Ucrania em: https://jornal.unesp.br/2022/07/25/guerra-da-ucrania-pode-provocar-uma-reestruturacao-do-comercio-energetico-global/
        4. Primavera Árabe e Petróleo em: https://www.chathamhouse.org/2011/02/arab-spring-and-oil-markets
        5. Meta Prophet Quick Start. Disponível em: https://facebook.github.io/prophet/docs/quick_start.html
        6. Precificação da Omicron e impacto na cotação do petróleo em: https://www.bloomberg.com/news/articles/2021-12-14/oil-is-pricing-in-omicron-impact-stock-market-should-be-next
        7. Serializing ARIMA models em: https://alkaline-ml.com/pmdarima/serialization.html
        8. Sobre ARIMA em: https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
        9. Sobre Meta Prophet em: https://facebook.github.io/prophet/docs/quick_start.html
        
    """
    )
