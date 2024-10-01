import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from utils.constantes import TITULO_HISTORIA, TITULO_PRINCIPAL
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_HISTORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()


# def plot_grafico_evolucao_preco_petroleo():
#     def add_ponto_interesse(fig, ponto, text_index, label):
#         fig.add_trace(
#             go.Scatter(
#                 x=[ponto.Data.values[0]],
#                 y=[ponto.Preco.values[0]],
#                 mode="markers",
#                 text=1,
#                 marker=dict(color="red", size=10, line=dict(color="white", width=1)),
#                 name=label,
#             )
#         )
#         fig.add_annotation(
#             x=ponto.Data.values[0],
#             y=ponto.Preco.values[0] + 4,
#             text=text_index,
#             showarrow=False,
#             font=dict(color="white", size=10),
#             bgcolor="red",
#             borderwidth=1,
#             bordercolor="white",
#         )

#     df = pd.read_csv("assets/csv/petroleo-brent.csv")

#     fig = go.Figure()
#     fig.add_trace(
#         go.Scatter(x=df.Data, y=df.Preco, mode="lines", name="Preço do barril de petróleo")
#     )
#     add_ponto_interesse(
#         fig, df.query('Data == "1990-08-02"'), 1, "1. Guerra do Golfo (1990-1991)"
#     )
#     add_ponto_interesse(
#         fig,
#         df.query('Data == "2001-09-11"'),
#         2,
#         "2. Atentados terroristas nos EUA (2001)",
#     )
#     add_ponto_interesse(
#         fig, df.query('Data == "2003-03-20"'), 3, "3. Guerra do Iraque (2003-2011)"
#     )
#     add_ponto_interesse(
#         fig, df.query('Data == "2007-08-01"'), 4, "4. Crise financeira global (2007-2008)"
#     )
#     add_ponto_interesse(
#         fig, df.query('Data == "2010-12-20"'), 5, "5. Primavera Árabe (2010-2012)"
#     )
#     add_ponto_interesse(
#         fig, df.query('Data == "2011-02-17"'), 6, "6. Guerra Civil na Líbia (2011)"
#     )
#     add_ponto_interesse(
#         fig,
#         df.query('Data == "2011-03-15"'),
#         7,
#         "7. Conflito na Síria (a partir de 2011)",
#     )
#     add_ponto_interesse(
#         fig,
#         df.query('Data == "2014-11-28"'),
#         8,
#         "8. OPEP mantém ritmo de produção (2014)",
#     )
#     add_ponto_interesse(
#         fig,
#         df.query('Data == "2015-01-02"'),
#         9,
#         "9. Grande produção e baixa demanda (2015)",
#     )
#     add_ponto_interesse(
#         fig, df.query('Data == "2020-01-30"'), 10, "10. Pandemia de COVID-19 (2020-2023)"
#     )
#     add_ponto_interesse(
#         fig,
#         df.query('Data == "2021-07-01"'),
#         11,
#         "11. Recuperação econômica pós-COVID (2021-presente)",
#     )
#     add_ponto_interesse(
#         fig,
#         df.query('Data == "2021-12-01"'),
#         12,
#         "12. Nova variante Omicron COVID-19 (2021)",
#     )
#     add_ponto_interesse(
#         fig,
#         df.query('Data == "2022-02-24"'),
#         13,
#         "13. Conflito Rússia-Ucrânia (2022-presente)",
#     )

#     fig.add_annotation(
#         x=0.5,
#         y=-0.15,
#         xref="paper",
#         yref="paper",
#         text="<b>Fonte: EIA, 2024</b>",
#         showarrow=False,
#         font=dict(color="black", size=10),
#         bgcolor="white",
#         borderwidth=1,
#         bordercolor="black",
#     )

#     fig.update_layout(
#         title="Evolução do preço do barril de petróleo Brent ao longo das decádas (1987 até hoje)",
#         xaxis_title="Data",
#         yaxis_title="Preço em US$",
#         height=640,
#     )

#     st.plotly_chart(fig, use_container_width=True)


# with st.container():
#     st.header(f":orange[{TITULO_HISTORIA}]")
#     st.markdown(
#         """
#         Ao longo das décadas, uma série de eventos significativos, como guerras e revoluções, moldaram o contexto geopolítico global de suas respectivas eras. Esses acontecimentos desempenharam um papel crucial na flutuação dos preços da commodity do petróleo, uma vez que é uma peça fundamental na economia mundial.\n
#         A seguir, serão detalhados 13 desses eventos cruciais, ordenados de forma cronológica, conforme a seguir:
#         * Guerra do Golfo (1990-1991)
#         * Atentados terroristas nos EUA (2001)
#         * Guerra do Iraque (2003-2011)
#         * Crise financeira global (2007-2008)
#         * Primavera Árabe (2010-2012)
#         * Guerra Civil na Líbia (2011)
#         * Conflito na Síria (2011~)
#         * OPEP mantém ritmo de produção (2014)
#         * Grande produção e baixa demanda (2015)
#         * Pandemia de COVID-19 (2020-2023)
#         * Nova variante Omicron COVID-19 (Dezembro 2021)
#         * Recuperação econômica pós-COVID (2021~)
#         * Conflito Rússia-Ucrânia (2022~)
#     """
#     )

#     plot_grafico_evolucao_preco_petroleo()
