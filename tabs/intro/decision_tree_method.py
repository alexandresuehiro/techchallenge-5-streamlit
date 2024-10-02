import streamlit as st
from tabs.tab import TabInterface


class expDecisionTree(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Árvore de Decisão - Classificação (Decision Tree - Classification)]", divider="blue")
            st.markdown(
                """
                    Árvore de Decisão: Uma Ferramenta Versátil para Classificação e Regressão
Imagine tomar decisões como um fluxograma. A cada decisão, você segue um caminho específico baseado em algumas condições. Uma árvore de decisão funciona de forma similar, mas usando dados para tomar decisões de forma automatizada.

Uma árvore de decisão é um algoritmo de aprendizado de máquina que cria uma estrutura em forma de árvore para tomar decisões. Cada nó interno da árvore representa um teste em um atributo (por exemplo, "idade > 30"), e cada ramo representa o resultado do teste. As folhas da árvore representam as classes (em problemas de classificação) ou os valores (em problemas de regressão) que queremos prever.

Como a Árvore de Decisão Funciona:
Construção: A árvore é construída de forma recursiva, dividindo os dados em subconjuntos mais puros a cada nível.
Critério de divisão: Um critério de divisão (como a entropia ou o índice de Gini) é utilizado para escolher o melhor atributo para dividir os dados em cada nó.
Parada: A construção da árvore para quando um nó atinge um determinado nível de pureza ou quando o número de exemplos em um nó é muito pequeno.
Árvore de Decisão em Problemas de Classificação e Regressão:
Classificação:
Objetivo: Prever a classe a qual um dado pertence.
Exemplo: Classificar um e-mail como spam ou não spam.
Saída: Uma classe (spam ou não spam).
Regressão:
Objetivo: Prever um valor numérico contínuo.
Exemplo: Prever o preço de uma casa.
Saída: Um número real (preço).
Em ambos os casos, a árvore de decisão segue o mesmo princípio: fazer perguntas sobre os dados para chegar a uma conclusão. A diferença está na natureza da conclusão: em classificação, a conclusão é uma categoria, enquanto em regressão, é um número.

Vantagens da Árvore de Decisão:
Fácil de entender e interpretar: A estrutura da árvore é intuitiva e pode ser visualizada.
Capacidade de lidar com dados numéricos e categóricos: Não requer pré-processamento extenso dos dados.
Identificação de features importantes: As árvores de decisão podem ajudar a identificar quais atributos são mais importantes para a previsão.
Desvantagens da Árvore de Decisão:
Propensa a overfitting: Pode se ajustar demais aos dados de treinamento, prejudicando a generalização para novos dados.
Instável: Pequenas mudanças nos dados podem levar a árvores de decisão completamente diferentes.
Dificuldade em lidar com dados faltantes: Existem técnicas para lidar com dados faltantes, mas podem complicar a interpretação da árvore.
Resumo:
A árvore de decisão é uma ferramenta versátil que pode ser aplicada tanto em problemas de classificação quanto de regressão. Sua simplicidade e interpretabilidade a tornam uma excelente escolha para muitos problemas de aprendizado de máquina. No entanto, é importante estar atento às suas limitações e utilizar técnicas como poda e random forest para melhorar sua performance.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
