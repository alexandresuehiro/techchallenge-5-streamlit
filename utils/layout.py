
import streamlit as st
from st_pages import show_pages, Page
import locale

from utils.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PASSOS, TITULO_INDICADORES, TITULO_INTRODUCAO, TITULO_MODELO, TITULO_REFLEXOES, TITULO_INSTRUCTIONS, TITULO_REFERENCIAS

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def output_layout():
    show_pages(
        [
            Page("./streamlit_app.py", "Tech Challenge 5", use_relative_hash=True),                 
            Page("./pages/intro.py", TITULO_INTRODUCAO, use_relative_hash=True),            
            Page("./pages/passos.py", TITULO_PASSOS, use_relative_hash=True),     
            Page("./pages/indicadores.py", TITULO_INDICADORES, use_relative_hash=True),         
            Page("./pages/analise.py", TITULO_ANALISE_EXPLORATORIA, use_relative_hash=True),
            Page("./pages/modelo.py", TITULO_MODELO, use_relative_hash=True),               
            Page("./pages/reflexoes.py", TITULO_REFLEXOES, use_relative_hash=True),         
            Page("./pages/instructions.py", TITULO_INSTRUCTIONS, use_relative_hash=True),         
            Page("./pages/ref_bibliografica.py", TITULO_REFERENCIAS, use_relative_hash=True)             
        ]
    )

    with st.sidebar:
        st.subheader("Aluno")
        st.text("Alexandre Suehiro de Paula e Silva")
        st.text("RM 352798 - 3DTAT")

        st.divider()

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/alexandresuehiro/techchallenge-5-streamlit",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
        st.link_button(
            "Repositório Jupyter Notebook, Análises e outros",
            "https://github.com/alexandresuehiro/Postgrad_FIAP_3DTAT/tree/main/techchallenge-5",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )