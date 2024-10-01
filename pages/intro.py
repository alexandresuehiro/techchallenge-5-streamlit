import streamlit as st
from tabs.intro.passos_magicos import PassosMagicos
from tabs.intro.educacao_brasil import EducacaoBrasil
from tabs.intro.educacao_local import EducacaoLocal
from tabs.intro.decision_tree_classification_method import expDecisionTreeClassification
from tabs.intro.random_forest_classification_method import expRandomForestClassification
from tabs.intro.linear_regression_method import expLinearRegression
from tabs.intro.logistic_regression_method import expLogisticRegression
from tabs.intro.decision_tree_regression_method import expDecisionTreeRegression
from tabs.intro.random_forest_regression_method import expRandomForestRegression

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

    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
        tabs=[
            "Passos Mágicos",
            "Educação no Brasil",
            "Educação em Embu-Guaçú",
            "Regressão Linear",
            "Regressão Logística",
            "Decision Tree - Classification",
            "Random Forest - Classification",
            "Decision Tree - Regression",
            "Random Forest - Regression"
        ]
    )

    PassosMagicos(tab0)
    EducacaoBrasil(tab1)
    EducacaoLocal(tab2)
    expLinearRegression(tab3)
    expLogisticRegression(tab4)
    expDecisionTreeClassification(tab5)
    expRandomForestClassification(tab6)
    expDecisionTreeRegression(tab7)
    expRandomForestRegression(tab8)
 
