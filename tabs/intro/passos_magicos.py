import streamlit as st
from tabs.tab import TabInterface


class PassosMagicos(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Passos Mágicos]", divider="blue")
            st.markdown(
                """
                    Um pouco mais sobre a Metodologia da Passos Magicos.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
