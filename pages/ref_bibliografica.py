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
        1. Sobre a Passos Mágicos em: https://passosmagicos.org.br/quem-somos/
        2. Sobre o PEDE 2022 - SILVA, Dario Rodrigues da. Pesquisa Extensiva do Desenvolvimento Educacional - PEDE 2022.
                                Associação Passos Mágicos. São Paulo
        3. Sobre Jornada do Herói em: https://rockcontent.com/br/talent-blog/jornada-do-heroi/
        4. Sobre piora de níveis educacionais na pandemia em: https://www.cnnbrasil.com.br/nacional/inep-aponta-piora-em-todos-os-niveis-da-educacao-basica-devido-a-pandemia/
        5. Sobre desempenho escolar durante a pandemia em: https://www.correiobraziliense.com.br/brasil/2022/09/5037496-apos-pandemia-aprendizado-no-brasil-piora-em-todos-os-niveis-escolares.html
        6. Sobre Linear Regression em: https://www.geeksforgeeks.org/ml-linear-regression/
        7. Sobre Logistic Regression: https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
        8. Sobre Decision Tree em: https://scikit-learn.org/stable/modules/tree.html
        9. Sobre Random Forest em: https://scikit-learn.org/stable/modules/ensemble.html#forest
        
    """
    )
