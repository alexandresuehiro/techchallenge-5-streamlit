import streamlit as st
from tabs.tab import TabInterface


class expLinearRegression(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(f":orange[Regressão Linear (Linear Regression)]")
            st.subheader(":blue[Uma Analogia e Uma Explicação Detalhada]", divider="blue")
            st.markdown(
                """
                     Imagine ajustar uma linha reta em um gráfico. Essa linha representa a melhor relação possível entre duas variáveis. Essa é a ideia central da regressão linear.
                    
                    A regressão linear é um método estatístico que busca modelar a relação linear entre uma variável dependente (aquela que queremos prever) e uma ou mais variáveis independentes (aquelas que usamos para fazer a previsão).
                """),
            st.subheader(":blue[Vamos usar uma analogia para entender melhor]", divider="blue")
            st.markdown(
                """  
                    Imagine que você quer prever o preço de um apartamento baseado em sua área. Você coleta dados de diversos apartamentos, anotando a área e o preço de cada um. Ao plotar esses dados em um gráfico, você provavelmente verá que, em média, quanto maior a área, maior o preço. A regressão linear busca encontrar a reta que melhor se ajusta a esses pontos, ou seja, a reta que minimiza a distância entre os pontos e a reta.
                    
                    A equação da reta é dada por:
                    
                        y = mx + b

                    Onde:

                        y: é a variável dependente (o preço do apartamento, no nosso exemplo)
                        x: é a variável independente (a área do apartamento)
                        m: é a inclinação da reta (indica como y varia em relação a x)
                        b: é o coeficiente linear (o valor de y quando x é igual a zero)
                    A regressão linear busca encontrar os valores de m e b que minimizam a soma dos quadrados dos resíduos, ou seja, a diferença entre os valores reais de y e os valores previstos pela reta.
                """),
            st.subheader(":blue[Comparando com a Floresta Aleatória]", divider="blue")
            st.markdown(
                """  
                    Enquanto a Floresta Aleatória é um método de ensemble que combina múltiplas árvores de decisão, a regressão linear é um modelo linear que busca encontrar uma única relação linear entre as variáveis.

                    Floresta Aleatória:
                        - Múltiplas árvores de decisão.
                        - Captura relações não lineares.
                        - Alta precisão em diversos problemas.
                        - Pode ser mais difícil de interpretar.
                    
                    
                    Regressão Linear:
                        - Uma única reta.
                        - Captura apenas relações lineares.
                        - Mais simples de entender e interpretar.
                        - Pode não ser adequada para dados com relações não lineares.
                    
                    Quando usar a Regressão Linear:
                        - Relações lineares: Quando você acredita que existe uma relação linear entre as variáveis.
                        - Interpretabilidade: Quando a interpretação dos coeficientes é importante.
                        - Dados simples: Quando os dados são relativamente simples e sem muitos outliers.
                """),
            st.subheader(":blue[Em resumo...", divider="blue")
            st.markdown(
                """  
                    A regressão linear é uma ferramenta poderosa e fácil de usar para modelar relações lineares entre variáveis. No entanto, é importante lembrar que nem todos os problemas podem ser resolvidos com uma simples reta. Em muitos casos, modelos mais complexos, como a Floresta Aleatória, podem ser mais adequados.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
