import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
from utils.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from utils.layout import output_layout, format_number


st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

df = pd.read_csv("assets/csv/petroleo-brent.csv")

with st.container():
    st.header(f":orange[{TITULO_ANALISE_EXPLORATORIA}]")

