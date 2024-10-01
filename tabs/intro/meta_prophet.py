import streamlit as st
from tabs.tab import TabInterface


class IntroMetaProphet(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":blue[Meta Prophet]", divider="blue"
            )
            st.markdown(
                """
                Devido a necessidade de realizar previsões, a empresa Facebook criou em 2017 o Prophet, um framework para previsões de séries temporais, acessível através de API tanto em R quanto em Python e que segue o princípio de uma série temporal poder ser decomposta em 4 componentes: tendência, sazonalidade, uma componente que comporte as variações devido a feriados, e os erro como quarta.
                <br/><br/>
            """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])

                with col0:
                    st.image(
                        "assets/imgs/logo-meta.png", width=220, caption="Logo do Meta"
                    )
