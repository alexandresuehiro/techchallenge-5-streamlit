import streamlit as st
from tabs.tab import TabInterface


class PassosMagicos(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(f":orange[Passos Mágicos]")
            st.subheader(":blue[Nossa história]", divider="blue")
            st.markdown(
                """
A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.

A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.

Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.
                """)

            st.subheader(":blue[O que fazemos?]", divider="blue")
            st.markdown(
                """
                    Oferecemos um programa de educação de qualidade para crianças e jovens do município de Embu-Guaçu.
                """),

            unsafe_allow_html=True,
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                    st.subheader(f"Aceleração do Conhecimento")
                    st.markdown(
                """
                    Educação de qualidade, programas educacionais, assistência psicológica e ampliação da visão de mundo. Conheça mais sobre nosso trabalho.

                    https://passosmagicos.org.br/aceleracao-do-conhecimento/
                """)
            with col2:
                    st.subheader(f"Programas Especiais")
                    st.markdown(
                """
                    Conheça nosso projeto de apadrinhamento e de intercâmbio, visando uma maior integração dos alunos com diferentes ambientes e culturas.

                    https://passosmagicos.org.br/programas-especiais/
                """)
            with col3:
                    st.subheader(f"Eventos e Ações Sociais")
                    st.markdown(
                """
                    Anualmente, em prol dos alunos, são promovidas campanhas de arrecadação para presentear as centenas de crianças e adolescentes Passos Mágicos.

                    https://passosmagicos.org.br/eventos-e-acoes-sociais/
                """)
            with col4:
                    st.subheader(f"Parceiros e Apoiadores")
                    st.markdown(
                """
                    Conheça nossas empresas parceiras e apoiadoras que nos ajudam a dar vida aos nossos projetos de transformação.

                    https://passosmagicos.org.br/parceiros-e-apoiadores/
                """)     
            st.subheader(":blue[Missão e Valores]", divider="blue")
            st.markdown(
                """
                    Nossa missão é transformar a vida de jovens e crianças, oferecendo ferramentas para levá-los a melhores oportunidades de vida.

                    Nossa visão é viver em um Brasil no qual todas as crianças e jovens têm iguais oportunidades para realizarem seus sonhos e são agentes transformadores de suas próprias vidas.

                    
                """),
              
            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
