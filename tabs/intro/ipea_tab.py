import streamlit as st
from tabs.tab import TabInterface


class IntroIPEATab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":blue[Instituto de Pesquisa Econômica Aplicada (IPEA)]", divider="blue"
            )
            st.markdown(
                """
                A fundação Instituto de Pesquisa Econômica Aplicada (Ipea) é uma fundação pública federal vinculada ao Ministério do Planejamento e Orçamento (MPO) criada em 1964 como Epea (Escritório) e assumindo o nome atual em 1967.
                Suas atividades de pesquisa fornecem suporte técnico e institucional às ações do governo para a formulação e reformulação de políticas públicas e programas de desenvolvimento. Os trabalhos do Ipea são disponibilizados para a sociedade por meio de publicações (todas disponíveis gratuitamente em www.ipea.gov.br).
                <br/><br/>
            """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _ = st.columns([4, 2, 4])

                with col0:
                    st.image(
                        "assets/imgs/logo-ipea.png", width=128, caption="Logo do IPEA"
                    )
