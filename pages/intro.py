import streamlit as st
from tabs.intro.passos_magicos import PassosMagicos
from tabs.intro.educacao_brasil import EducacaoBrasil
#from tabs.intro.educacao_local import EducacaoLocal
#from tabs.intro.decision_tree_classification_method import expDecisionTreeClassification
#from tabs.intro.random_forest_classification_method import expRandomForestClassification
from tabs.intro.linear_regression_method import expLinearRegression
from tabs.intro.logistic_regression_method import expLogisticRegression
from tabs.intro.decision_tree_method import expDecisionTree
from tabs.intro.random_forest_method import expRandomForest

from utils.constantes import TITULO_INTRODUCAO, TITULO_PRINCIPAL
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_INTRODUCAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_INTRODUCAO}]")

    st.write(
        """
        Nesta introdução, são descritos alguns tópicos importantes para entender:
         * Panorama da Educação Brasileira
         * Sobre a Passos Mágicos:
            <ol>
                <li>Nossa História</li>
                <li>O que fazemos</li>
                <li>Missão e Valores</li>
            </ol>
         * os modelos de Machine Learning usados: 
            <ol>
                <li>Regressão Linear (Linear Regression)</li>
                <li>Regressão Logística (Logistic Regression)</li>
                <li>Árvores de Decisão (Decision Trees)</li>
                <li>Florestas Aleatórias (Random Forest)</li>
            </ol>
    """
    )

    tab0, tab1, tab3, tab4, tab5, tab6 = st.tabs( #tab7, tab8  #tab2, 
    
        tabs=[
            "Passos Mágicos",
            "Educação no Brasil",
#            "Educação em Embu-Guaçú",
            "Regressão Linear",
            "Regressão Logística",
            "Decision Tree",
            "Random Forest"
        ]
    )

    PassosMagicos(tab0)
    EducacaoBrasil(tab1)
#    EducacaoLocal(tab2)
    expLinearRegression(tab3)
    expLogisticRegression(tab4)
    expDecisionTree(tab5)
    expRandomForest(tab6)
#    expDecisionTreeRegression(tab7)
#    expRandomForestRegression(tab8)
 
