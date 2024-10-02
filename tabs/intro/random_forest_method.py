import streamlit as st
from tabs.tab import TabInterface


class expRandomForest(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(f":orange[Floresta Aleatória - Classificação (Random Forest - Classification)]")
            st.subheader(":blue[Uma Explicação Intuitiva]", divider="blue")
            st.markdown(
                """
                Imagine plantar uma floresta. Em vez de plantar árvores de uma única espécie, você planta diversas espécies, cada uma com suas características únicas. Essa diversidade faz com que a floresta seja mais resistente a pragas e doenças, e capaz de se adaptar a diferentes condições climáticas.

                A Floresta Aleatória funciona de forma similar. Em vez de árvores, temos árvores de decisão. Cada árvore de decisão é um modelo simples que "aprende" a classificar dados ou fazer previsões. Ao invés de plantar uma única árvore, criamos uma floresta com muitas árvores, cada uma construída com um subconjunto aleatório dos dados e considerando apenas um subconjunto aleatório das características.

                A força da Floresta Aleatória está na diversidade. Cada árvore "opina" sobre a classificação ou previsão, e a decisão final é tomada por votação. Essa abordagem reduz o risco de overfitting (quando o modelo se ajusta demais aos dados de treinamento e perde a capacidade de generalizar para novos dados) e aumenta a precisão do modelo.
                """)
            st.subheader(":blue[Classificador vs. Regressor: Qual a diferença?]", divider="blue")
            st.markdown(
                """  

                Classificador: Um classificador é usado para prever a classe a qual um determinado exemplo pertence. Por exemplo, um classificador de e-mails pode determinar se um e-mail é spam ou não spam. A saída de um classificador é geralmente uma categoria (por exemplo, "spam", "não spam", "gato", "cachorro").

                Regressor: Um regressor é usado para prever um valor numérico contínuo. Por exemplo, um regressor pode ser usado para prever a temperatura máxima de amanhã, o preço de uma casa ou a idade de uma pessoa. A saída de um regressor é um número real (por exemplo, 25°C, R$ 500.000, 35 anos).
                """),
            st.subheader(":blue[Em resumo...]", divider="blue")
            st.markdown(
                """  
                * Classificação: Prever a classe a qual um exemplo pertence.
                * Regressão: Prever um valor numérico contínuo.
                * Florestas Aleatórias podem ser usadas tanto para classificação quanto para regressão. A diferença está no tipo de problema que queremos resolver e no tipo de saída que esperamos do modelo.

                Exemplo:

                * Classificação: Prever se um cliente irá comprar um produto (sim ou não).
                * Regressão: Prever o valor que um cliente irá gastar na próxima compra.

                Em ambos os casos, a Floresta Aleatória cria múltiplas árvores de decisão e combina suas previsões para obter um resultado mais preciso e robusto.

                Vantagens da Floresta Aleatória:

                * Alta precisão: Geralmente obtém resultados muito bons em diversos tipos de problemas.
                * Robustez: É pouco sensível a outliers e ruídos nos dados.
                * Capacidade de lidar com diferentes tipos de dados: Funciona bem com dados numéricos e categóricos.
                * Fácil de interpretar: A importância de cada característica pode ser avaliada.


                Em resumo, a Floresta Aleatória é um algoritmo de aprendizado de máquina versátil e poderoso, amplamente utilizado em diversas áreas, como:
                * Análise de dados: Para encontrar padrões e fazer previsões.
                * Reconhecimento de padrões: Para identificar objetos em imagens ou sons.
                * Bioinformática: Para analisar dados genéticos.
                * Finanças: Para prever o valor de ações.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
