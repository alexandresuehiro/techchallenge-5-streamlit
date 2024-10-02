import streamlit as st
from tabs.tab import TabInterface
import pandas as pd



data6 = pd.read_csv("data/06_ian_pedras.csv", header=0, sep=";")
data7 = pd.read_csv("data/07_ida_pedras.csv", header=0, sep=";")
data8 = pd.read_csv("data/08_ieg_pedras.csv", header=0, sep=";")
data9 = pd.read_csv("data/09_iaa_pedras.csv", header=0, sep=";")
data10 = pd.read_csv("data/10_ips_pedras.csv", header=0, sep=";")
data11 = pd.read_csv("data/11_ipp_pedras.csv", header=0, sep=";")
data12 = pd.read_csv("data/12_ipv_pedras.csv", header=0, sep=";")


class AnaliseIndicadoresPorPedra(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(":blue[Análise dos Indicadores por Pedra]", divider="blue")
            st.markdown(
                """
                    Como vimos anteriormente, a ampla maioria se enquadra na faixa de 5,506 até 9,294. Resta verificar quais componentes ajudaram no INDE ser tão alto em muitos casos, o que poderia indicar um caminho para o sucesso do estudante e, em contrapartida, quais pontos precisam ser discutidos para pensar em melhoras.
                """)
            st.subheader('Análise do Indicador IAN em relação ao perfil de Pedras') 
            st.image('assets/imgs/qtde_pedras_IAN.png')
            st.dataframe(data6)
            st.markdown(
                """
                    Na composição do INDE, o IAN possui peso 0,1. Ao analisar o perfil de pedras ao longo dos anos, vemos que as médias ao longo dos anos tiveram uma variação considerável, com decréscimo para todos os perfis e que houve muita concentração das notas entre 4.96 e 5.60. Logo, o Indicador de Adequação de Nível mostra que há muitos estudantes defasados em relação ao seu ano ideal (isto é, há defasagem de anos escolares em relação ao ano ideal). 
                """)


            st.subheader('Análise do Indicador IDA em relação ao perfil de Pedras') 

            st.image('assets/imgs/qtde_pedras_IDA.png')
            st.dataframe(data7)
            st.markdown(
                """
                    Pelo Indicador de Desempenho Acadêmico, vemos que ao longo dos anos, o perfil Quartzo teve melhora significativa na sua média. Em contrapartida, os demais perfis tiveram uma queda em 2021 se comparado a 2020 e apresentou recuperação parcial em 2022. Para os estudantes da Fase 8, o peso do Indicador de Desempenho Acadêmico é maior, com peso de 0,4 na composição do INDE. Pode ser um fator que ajude a impulsionar a vontade de esforçar para mostrar resultado ou o fato de ter uma bolsa impulsiona a vontade de estudar.
                """) 

            st.subheader('Análise do Indicador IEG em relação ao perfil de Pedras')                       
  
            st.image('assets/imgs/qtde_pedras_IEG.png')
            st.dataframe(data8)              
            st.markdown(
                """     
                    Pelo Indicador de Engajamento, vemos que praticamente todos os perfis tiveram aumento ao longo do período mensurado, com destaque para o período de 2021, que foi um ano de pandemia e os estudantes se engajaram em atividades. O peso do IEG na composição do INDE é de 0,2, logo as médias que ficaram acima do limite inferior do perfil de cada pedra mostram que ajudaram positivamente neste cálculo.
                """)

            st.subheader('Análise do Indicador IAA em relação ao perfil de Pedras')                       
  
            st.image('assets/imgs/qtde_pedras_IAA.png')
            st.dataframe(data9)              
            st.markdown(
                """     
                    O Indicador de Autoavaliação mostra que aqueles no grupo Quartzo tendem a se avaliar com uma nota menor que o restante. A variação ao longo dos anos para os grupos Ágata, Ametista e Topázio foi mínima e não foi um fator que influenciou no INDE global. O interessante do Indicador de Autoavaliação é que mostra um certo grau de confiança do estudante em si próprio e que evolui ao longo do tempo ao evoluir de INDE e, por consequência, de pedras.
                """)
            
            st.subheader('Análise do Indicador IPS em relação ao perfil de Pedras')                       
  
            st.image('assets/imgs/qtde_pedras_IPS.png')
            st.dataframe(data10)
            st.markdown(
                """
                    O Indicador Psicossocial é uma avaliação realizada pelo time de psicólogos da associação sobre as interações familiares, de comunidade e dentro da associação. Para o grupo Quartzo, a nota teve um crescimento substancial em 2022 comparado com 2021.
                """)

            st.subheader('Análise do Indicador IPP em relação ao perfil de Pedras')                       
  
            st.image('assets/imgs/qtde_pedras_IPP.png')
            st.dataframe(data11)
            st.markdown(
                """
                    Este indicador é resultado da avaliação da equipe de educadores e psicopedagogos para caracterizar o desenvolvimento cognitivo, emocional, comportamental e de socialização do aluno no seu processo de aprendizado.
                    O Indicador Psicopedagógico é o que mostrou considerável queda nas médias para todos os perfis de pedras no ano de 2022 em comparação com os anos anteriores. Pode ser que este seja um dos fatores que mais contribuíram para a queda do INDE global. Ao mesmo tempo, é importante notar que historicamente esses valores sempre foram altos

                """)

            st.subheader('Análise do Indicador IPV em relação ao perfil de Pedras')                       
  
            st.image('assets/imgs/qtde_pedras_IPV.png')
            st.dataframe(data12)
            st.markdown(
                """
                    Pelo histórico acima, houve uma queda para aqueles do perfil Topázio, mas dentro da faixa que define este perfil. Para os outros perfis de pedra, não houve grandes mudanças que justifiquem algum alerta. Como houve um aumento considerável no perfil Topázio, será necessário ficar atento aos resultados de 2023 para ver se há persistência de ausência de recuperação do Indicador.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
