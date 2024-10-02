import streamlit as st
from tabs.tab import TabInterface


class expLogisticRegression(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Regressão Linear (Linear Regression)]", divider="blue")
            st.markdown(
                """
                    Regressão Logística: Uma Explicação Intuitiva
Imagine um modelo que tenta prever se um e-mail é spam ou não. Ao invés de prever um valor numérico contínuo (como o preço de uma casa), aqui queremos prever uma categoria (spam ou não spam). A regressão logística é ideal para esse tipo de problema.

A regressão logística é um tipo de modelo estatístico utilizado para modelar a probabilidade de uma determinada classe ou evento ocorrer. Ao contrário da regressão linear, que prevê um valor numérico contínuo, a regressão logística prevê a probabilidade de um evento pertencer a uma determinada categoria.

Uma analogia:

Imagine que você está tentando prever se um aluno será aprovado ou reprovado em um exame, baseado em sua nota. A regressão logística criaria uma curva em "S" (conhecida como curva logística) que se aproxima de 0 (probabilidade de reprovação) ou 1 (probabilidade de aprovação) à medida que a nota aumenta.

Como funciona:

Função logística: A regressão logística utiliza uma função matemática chamada função logística para transformar a saída linear em uma probabilidade entre 0 e 1.
Limiar: Um limiar é definido para classificar as observações. Por exemplo, se a probabilidade for maior que 0.5, a observação é classificada como positiva (spam, aprovado, etc.), caso contrário, é classificada como negativa.
Comparando com a Regressão Linear:

Regressão Linear: Prediz um valor numérico contínuo.
Regressão Logística: Prediz a probabilidade de uma classe.
Saída: A saída da regressão linear é um número real, enquanto a saída da regressão logística é uma probabilidade entre 0 e 1.
Quando usar a Regressão Logística:

Problemas de classificação: Quando você quer prever se uma observação pertence a uma determinada categoria.
Variável dependente binária: Quando a variável que você quer prever tem apenas dois possíveis valores (sim/não, 0/1).
Relação não linear: A função logística permite modelar relações não lineares entre as variáveis.

Em resumo:

A regressão logística é uma ferramenta poderosa para resolver problemas de classificação. Ela é especialmente útil quando a variável dependente é binária e a relação entre as variáveis não é necessariamente linear.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
