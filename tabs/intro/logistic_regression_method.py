import streamlit as st
from tabs.tab import TabInterface


class expLogisticRegression(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Regressão Linear (Linear Regression)]", divider="blue")
            st.markdown(
                """
                    Uma média móvel integrada autoregressiva, ou ARIMA, é um modelo de análise estatística que usa dados de séries temporais para compreender melhor o conjunto de dados ou para prever tendências futuras.
                    Um modelo estatístico é autoregressivo se prever valores futuros com base em valores passados. Por exemplo, um modelo ARIMA pode procurar prever os preços futuros de uma ação com base no seu desempenho passado ou prever os lucros de uma empresa com base em períodos passados.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
