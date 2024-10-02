import streamlit as st
from tabs.tab import TabInterface


class expRandomForestRegression(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Floresta Aleatória Regressiva (Random Forest - Regression)]", divider="blue")
            st.markdown(
                """
                    O que é floresta aleatória?
                    Floresta aleatória é um algoritmo de machine learning comumente usado, com marca registrada por Leo Breiman e Adele Cutler, que combina a saída de várias árvores de decisão para alcançar um único resultado. Sua facilidade de uso e flexibilidade incentivaram a sua adoção, pois lida tanto com problemas de classificação quanto de regressão.

                    Como funciona?
                    Os algoritmos de floresta aleatória possuem três hiperparâmetros principais, os quais devem ser definidos antes do treinamento. Estes incluem o tamanho do nó, o número de árvores e o número de recursos amostrados. A partir daí, o classificador de floresta aleatória pode ser usado para resolver problemas de regressão ou classificação.

                    O algoritmo de floresta aleatória é composto por uma coleção de árvores de decisão, sendo que cada árvore na combinação é composta por uma amostra de dados extraída de um conjunto de treinamento com substituição, chamada de amostra bootstrap. Dessa amostra de treinamento, um terço dela é separado como dados de teste, conhecida como amostra out-of-bag (OOB), a qual iremos abordar mais tarde. Outra instância de aleatoriedade é então injetada por meio do bagging de recursos, incluindo mais diversidade ao conjunto de dados e reduzindo a correlação entre as árvores de decisão. Dependendo do tipo de problema, a determinação da previsão irá variar. Para uma tarefa de regressão, as árvores de decisão individuais terão suas médias calculadas, e para uma tarefa de classificação, um voto da maioria, ou seja, a variável categórica mais frequente, produzirá a classe prevista. Por fim, a amostra OOB é então utilizada para validação cruzada, finalizando esse previsão.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
