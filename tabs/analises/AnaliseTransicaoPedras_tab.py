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

data21 = pd.read_csv("data/21_ieg_transicao_ametista_ametista_ametista.csv", header=0, sep=";")
data22 = pd.read_csv("data/22_ieg_transicao_ametista_ametista_agata.csv", header=0, sep=";")
data23 = pd.read_csv("data/23_ieg_transicao_topazio_topazio_topazio.csv", header=0, sep=";")
data24 = pd.read_csv("data/24_ieg_transicao_topazio_ametista_ametista.csv", header=0, sep=";")
data25 = pd.read_csv("data/25_ieg_transicao_ametista_agata_agata.csv", header=0, sep=";")
data26 = pd.read_csv("data/26_ieg_transicao_ametista_agata_ametista.csv", header=0, sep=";")
data27 = pd.read_csv("data/27_ieg_transicao_ametista_topazio_topazio.csv", header=0, sep=";")

data28 = pd.read_csv("data/28_ipv_transicao_ametista_ametista_ametista.csv", header=0, sep=";")
data29 = pd.read_csv("data/29_ipv_transicao_ametista_ametista_agata.csv", header=0, sep=";")
data30 = pd.read_csv("data/30_ipv_topazio_topazio_topazio.csv", header=0, sep=";")
data31 = pd.read_csv("data/31_ipv_topazio_ametista_ametista.csv", header=0, sep=";")
data32 = pd.read_csv("data/32_ipv_ametista_agata_agata.csv", header=0, sep=";")
data33 = pd.read_csv("data/33_ipv_ametista_agata_ametista.csv", header=0, sep=";")
data34 = pd.read_csv("data/34_ipv_ametista_topazio_topazio.csv", header=0, sep=";")                 

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
                    De acordo com as informações obtidas da base de dados, havia cerca de 725 estudantes ao longo de 2020, 685 em 2021 e 862 em 2022: Pelo quadro obtido, a maioria das situações mostra estabilidade no perfil, seguido de queda com estabilidade como outro cenário mais plausível de ocorrer. Ocorreram também casos pontuais em que o estudante apresentou ascensão depois de uma queda ou um período estável. 
                    
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

            st.subheader('Análise de IEG na Transição Ametista - Ametista - Ametista') 
            st.markdown(
                """
						Vamos considerar o Indicador de Engajamento como ponto a analisar em mais detalhes o cenário Ametista  Ametista  Ametista. 
                """)
            st.dataframe(data21)
            st.markdown(
                """
                        Vemos a presença maior de casos em que o IEG melhorou em 2021 para 2022. Apesar de ter um número considerável de saldo negativo do período 2020-2022, a quantidade de melhoras para o perfil Ametista condiz com o gráfico do Indicador IEG em relação às pedras.
                """)
            st.subheader('Análise de IEG na Transição Ametista - Ametista - Ágata')                       

  
            st.dataframe(data22)
            st.markdown(
                """
                        O que vemos aqui é um número de casos em que houve queda no Indicador Psicopedagógico em 2021  2022, com muitos casos com menos de 7.5 pontos, o que afeta o INDE. Se considerarmos que este Indicador mede bem a situação mental do estudante, este cenário mostra que algo afetou muito a capacidade dos estudantes.
                """)

            st.subheader('Análise de IEG na Transição Topázio - Topázio - Topázio')
            st.markdown(
                """ 
						Vamos considerar o Indicador de Engajamento como ponto a analisar em mais detalhes o cenário Topázio  Topázio  Topázio. O diferencial desse cenário é que seria o indicativo de alto INDE. 
                """)
            st.dataframe(data23)

            st.markdown(
                """ 
						Ao analisar a quantidade de ascensão e queda nos números, podemos ver que o Indicador de Engajamento para essas pessoas já é considerado alto. As quedas ocorridas não são consideráveis e o IEG não impactou como em outros cenários.
                """)
            

            st.subheader('Análise de IEG na Transição Topázio - Ametista - Ametista')
            st.markdown(
                """ 
                    Vamos considerar o Indicador de Engajamento como ponto a analisar em mais detalhes o cenário Topázio - Ametista - Ametista. 
                """)
            st.dataframe(data24)

            st.markdown(
                """ 
                    Vemos aqui um alto engajamento em 2020, porém uma queda considerável em 2021, com muitos casos com perdas de mais de um ponto, porém muitos desses casos que tiveram queda em 2020-2021 apresentaram recuperação em 2021-2022.
                """)
            

            st.subheader('Análise de IEG na Transição Ametista - Ágata - Ágata')
            st.markdown(
                """ 
					Vamos considerar o Indicador de Engajamento como ponto a analisar em mais detalhes o cenário Ametista - Ágata - Ágata. 
                """)
            st.dataframe(data25)

            st.markdown(
                """ 
                    Este cenário é bem simbólico sobre a mudança do padrão da nota. Praticamente todos tiveram queda em 2020-2021, porém conseguiram recuperar boa parte da nota em 2021-2022.
                """)
            

            st.subheader('Análise de IEG na Transição Ametista - Ágata - Ametista')
            st.markdown(
                """ 
                    Vamos considerar o Indicador de Engajamento como ponto a analisar em mais detalhes o cenário Ametista - Ágata - Ametista. 
                """)
            st.dataframe(data26)

            st.markdown(
                """ 
                    Este cenário foi similar ao anterior, com somente uma ascensão no período 2020-2021. Houve recuperação do IEG em 2021-2022, quase revertendo a queda no período anterior.
                """)
            


            st.subheader('Análise de IEG na Transição Ametista - Topázio - Topázio')
            st.markdown(
                """ 
					Este cenário a ser analisado é considerado importante pois mostra estudantes em tendência de ascensão e mantiveram o ritmo.
                """)
            st.dataframe(data27)

            st.markdown(
                """ 
                    Pela quantidade de melhoria e queda nas avaliações, vemos que o Engajamento foi recuperado no período 2021-2022.
                """)


            st.subheader('Conclusão da Análise de IEG')
            st.markdown(
                """ 
                    O Indicador de Engajamento mostrou que as atividades realizadas pela Passos Mágicos durante o ano de 2021, se comparado a 2020, teve uma queda considerável e isso afetou a avaliação dos alunos. Em 2022, o cenário mudou muito, o que mostra que as atividades conseguiram puxar mais os estudantes para o ambiente da associação.
                """)




            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
