import streamlit as st
from utils.constantes import TITULO_PRINCIPAL, TITULO_REFLEXOES
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_REFLEXOES} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_REFLEXOES}]")

    st.markdown(
        """
        Após a análise dos resultados, considerando o histórico de mudanças no valor do Petróleo, podemos afirmar que alguns eventos futuros poderão ter impacto no seu valor:
        1) Eleição nos EUA: devido ao impacto de uma eventual mudança na Casa Branca, o mundo poderá reagir e o preço do petróleo mudar.
        2) Fim da guerra da Ucrânia: caso ocorra um final de conflito, o mercado pode reagir melhor e suspendar as sanções contra a Rússia, o que pode impactar até mesmo a nossa balança comercial.
        3) Preço de commodities: se a produção de commodities acelerar, a demanda por petróleo aumentará, o que beneficia os países produtores, como a Rússia e os países do Oriente Médio.
                - Impacto direto: muitos países da Europa, cuja matriz energética depende do petróleo, sofrerão impactos nos gastos com importações e isso pode causar atritos políticos com muitas consequências.
                - Impacto direto: isso pode beneficiar os países que já produzem commodities e aumentar a produção das mesmas, o que pode causar excesso e derrubar os preços das mesmas.
    """
    )

