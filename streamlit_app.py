import streamlit as st
#<<<<<<< HEAD
#
#st.title("🎈 My new app")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)
#=======
from utils.constantes import TITULO_PRINCIPAL
from utils.layout import output_layout
import warnings



warnings.filterwarnings("ignore")

st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":orange[{TITULO_PRINCIPAL}]")

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    Este trabalho tem por finalidade analisar o desenvolvimento dos jovens da ONG Passos Mágicos, que recebem ajuda psicopedagógica, atividades e bolsas de estudo. Propomos a analisar termos e fontes de dados para implementar processos de Machine Learning que possam checar cenários de sucesso ou indicativos de um caminho. Com estes resultados, vamos exibi-los via Streamlit.
"""
)

st.subheader(
    ":blue[Sobre a Passos Mágicos]",
    divider="blue",
)
st.markdown(
    """
    Nossa história
    A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.

    A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.

    Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.
"""
)



st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    Usando a base de dados provida, referente ao período 2020-2022, fizemos uma análise inicial sobre o conteúdo para entender o que a Passos Mágicos observa em seus jovens. A partir desse ponto, consideramos o que ocorreu durante o período que poderia influenciar nos resultados achados.
    Deixamos como possibilidade considerar alguns indicadores como entrada para analisar os cenários e o que seria um "resultado esperado de sucesso do trabalho".
    Para facilitar as análises, deixamos a possibilidade de escolher alguns modelos de Machine Learning:
    1. Regressão Linear (Linear Regression);
    2. Árvore de Decisão por Classificação (Decision Tree - Classification)
    3. Random Forest por Classificação (Random Forest - Classification)
    4. Regressão Logística (Logistic Regression);
    5. Árvore de Decisão por Regressão (Decision Tree - Regression)
    6. Random Forest por Regressão (Random Forest - Regression)
 """
)
#>>>>>>> f36f782 (Initial commit)
