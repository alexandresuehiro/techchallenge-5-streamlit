import streamlit as st
from utils.constantes import TITULO_PRINCIPAL, TITULO_INSTRUCTIONS
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_INSTRUCTIONS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st._main:

        st.subheader("Como construir o app?")
        st.text("Do zero, no site do streamlit")
        st.text("Acessar o 'Create app' - 'Blank App'")
        
        st.subheader("Como construir o app (localmente)?")
        st.text("Criar ambiente com Virtualenv")
        st.code(body="python -m venv venv", language="shell")
        st.code(body="source venv/Scripts/activate", language="shell")
        st.code(body="pip install -r requirements.txt", language="shell")
        st.subheader("Executar localmente")
        st.code(body="streamlit run main.py", language="shell")

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/alexandresuehiro/techchallenge4_Streamlit_from_zero",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
        st.link_button(
            "Repositório Jupyter Notebook",
            "https://github.com/alexandresuehiro/Postgrad_FIAP_3DTAT/tree/main/techchallenge-4",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )