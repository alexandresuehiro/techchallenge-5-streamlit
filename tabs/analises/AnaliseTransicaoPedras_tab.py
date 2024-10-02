import streamlit as st
from tabs.tab import TabInterface
import pandas as pd


data13 = pd.read_csv("data/13_transicao_pedras.csv", header=0, sep=";")
data14 = pd.read_csv("data/14_ipp_transicao_pedras.csv", header=0, sep=";")
data14a = pd.read_csv("data/14a_ipp_transicao_pedras_ametista_ametista_ametista.csv", header=0, sep=";")
data15 = pd.read_csv("data/15_ipp_transicao_pedras_ametista_ametista_agata.csv", header=0, sep=";")
data16 = pd.read_csv("data/16_ipp_transicao_pedras_topazio_topazio_topazio.csv", header=0, sep=";")
data17 = pd.read_csv("data/17_ipp_transicao_topazio_ametista_ametista.csv", header=0, sep=";")
data18 = pd.read_csv("data/18_ipp_transicao_ametista_agata_agata.csv", header=0, sep=";")
data19 = pd.read_csv("data/19_ipp_transicao_ametista_agata_ametista.csv", header=0, sep=";")
data20 = pd.read_csv("data/20_ipp_transicao_ametista_topazio_topazio.csv", header=0, sep=";")
                     

class AnaliseTransicaoPedras(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.header(":blue[Análise de Transição entre Pedras]", divider="blue")
            st.markdown(
                """
                    Sobre as transições entre perfis de Pedras, essa análise contempla os veteranos que estão na Passo Mágicos há três anos consecutivos, no período de 2020 a 2022.
                """)
            st.dataframe(data13)
            st.markdown(
                """
                    De acordo com as informações obtidas da base de dados, havia cerca de 725 estudantes ao longo de 2020, 685 em 2021 e 862 em 2022:Pelo quadro obtido, a maioria das situações mostra estabilidade no perfil, seguido de queda com estabilidade como outro cenário mais plausível de ocorrer. Ocorreram também casos pontuais em que o estudante apresentou ascensão depois de uma queda ou um período estável. 
                    
                    A vantagem de considerarmos esse cenário é que temos estudantes com bom tempo de casa e com perfil relativamente conhecido pela própria associação. Também pode ser interessante observar os indicadores em alguns casos de estudo como faremos a seguir.

                    O ponto importante também é observar a evolução ao longo do tempo, sem considerar o Ponto de Virada, que pode ser um sinal de sucesso, porém há possibilidade de retroceder em termos de fase.
                """)

            st.subheader('Análise de IPP na Transição Ametista - Ametista - Ametista') 
            st.markdown(
                """
                    Vamos considerar o Indicador Psicopedagógico como ponto a comparar em mais detalhes em relação à transição de maior frequência, que foi o cenário Ametista - Ametista - Ametista. 
                """)
            st.dataframe(data14a)
            st.markdown(
                """
                        O que vemos aqui é um número de casos em que houve queda no Indicador Psicopedagógico em 2021  2022, com muitos casos com menos de 7.0 pontos, o que afeta o INDE. Se considerarmos que este Indicador mede bem a situação mental do estudante, este cenário mostra que algo afetou muito a capacidade dos estudantes. Como se mantiveram estável no mesmo perfil ao longo do tempo, é provável que algum outro indicador compensou essa queda para manter o INDE dentro da faixa para Ametista.
                """)
            st.subheader('Análise de IPP na Transição Ametista - Ametista - Ágata')                       
            st.markdown(
                """     
                        Neste próximo cenário, com transição Ametista - Ametista - Ágata, verificaremos também o quanto o Indicador Psicopedagógico foi afetado.
                """)    
            st.dataframe(data15)
            st.markdown(
                """
                        O que vemos aqui é um número de casos em que houve queda no Indicador Psicopedagógico em 2021  2022, com muitos casos com menos de 7.5 pontos, o que afeta o INDE. Se considerarmos que este Indicador mede bem a situação mental do estudante, este cenário mostra que algo afetou muito a capacidade dos estudantes.
                """)

            st.subheader('Análise de IPP na Transição Topázio - Topázio - Topázio')
            st.markdown(
                """ 
                    Neste próximo cenário, com transição Topázio  Topázio  Topázio, verificaremos também o quanto o Indicador Psicopedagógico foi afetado.
                """)
            st.dataframe(data16)

            st.markdown(
                """ 
                    O mesmo ocorreu para este cenário, com queda de mais de um ponto no acumulado entre 2020-2022.
                """)
            

            st.subheader('Análise de IPP na Transição Topázio - Ametista - Ametista')
            st.markdown(
                """ 
                    Neste próximo cenário, com transição Topázio - Topázio - Topázio, verificaremos também o quanto o Indicador Psicopedagógico foi afetado.
                """)
            st.dataframe(data17)

            st.markdown(
                """ 
                    Apesar de ter apresentado uma boa quantidade de aumento de IPP entre 2020 e 2021, houve uma grande quantidade de quedas em 2021 e 2022, com muitos caso com perda acumulada de mais de um ponto.
                """)
            

            st.subheader('Análise de IPP na Transição Ametista - Ágata - Ágata')
            st.markdown(
                """ 
                    Neste próximo cenário, com transição Ametista  Ágata  Ágata, verificaremos também o quanto o Indicador Psicopedagógico foi afetado.
                """)
            st.dataframe(data18)

            st.markdown(
                """ 
                    Apesar de ter apresentado uma boa quantidade de aumento de IPP entre 2020 e 2021, houve uma grande quantidade de quedas em 2021 e 2022, com muitos caso com perda acumulada de mais de um ponto.
                """)
            

            st.subheader('Análise de IPP na Transição Ametista - Ágata - Ametista')
            st.markdown(
                """ 
                    Este cenário é um pouco diferente dos anteriores, por ter ocorrido uma recuperação no perfil ao longo do tempo.
                """)
            st.dataframe(data19)

            st.markdown(
                """ 
                    Mesmo neste caso, o padrão de um número considerável de ascensão na pontuação em 2020-2021 e uma queda maior em 2021-2022 se repetiu.
                """)
            


            st.subheader('Análise de IPP na Transição Ametista - Topázio - Topázio')
            st.markdown(
                """ 
                    Neste próximo cenário, com transição Ametista  Topázio  Topázio, verificaremos também o quanto o Indicador Psicopedagógico foi afetado.
                """)
            st.dataframe(data20)

            st.markdown(
                """ 
                    Este cenário foi diferente do restante. Mesmo que tenha ocorrido um número considerável de quedas no período 2021-2022, a perda de mais de um ponto ocorreu para poucos casos.
                """)


            st.subheader('Conclusão da Análise de IPP')
            st.markdown(
                """ 
                    Pelos cenários analisados, o IPP influenciou negativamente no INDE, o que fez com o Ponto de Virada fosse atribuído a outros Indicadores.
                """)

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
