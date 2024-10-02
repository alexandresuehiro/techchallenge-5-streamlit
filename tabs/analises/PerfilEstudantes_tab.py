import streamlit as st
from tabs.tab import TabInterface


class PerfilEstudantes(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Perfil dos Estudantes]", divider="blue")
            tabela1 = [     
                        ["Status / Ano - Exercício",	"2020",	"2021",	"2022"]
                        ["Veterano",	"592",	"453",	"464"]
                        ["Ingressante",	"133",	"235",	"398"]
                        ["Total",	"725",	"688",	"862"]
                    ]
            st.markdown(
                """
                    Ingressantes e Veteranos
                    
                    De acordo com as informações obtidas da base de dados, havia cerca de 725 estudantes ao longo de 2020, 685 em 2021 e 862 em 2022:
                """)
            st.table(tabela1)
            st.markdown(
                """
                        Ano de Ingresso
Ainda analisando o tempo de início dos estudantes, temos o quadro abaixo:
	Ano - Exercício
Ano Ingresso	2020	2021	2022
2016	54	39	29
2017	78	45	40
2018	156	104	67
2019	304	187	139
2020	133	78	48
2021	-	235	141
2022	-	-	398
Total	725	688	862


Houve um acréscimo considerável em 2022, com o ingresso de 398 estudantes na associação (aumento de 200% em relação a 2020).
Escola Pública, Bolsistas e Universitários
Considerando todos aqueles do Ensino Fundamental e do Ensino Médio como alunos de Escola Pública ou Bolsistas, temos:
Quanto ao perfil estudantil, temos a seguinte composição:
Instituição de Ensino	2020	2021	2022
Escola Pública	596	559	733
Escola Privada	105	129	129
Universidade	24	0	0
 	725	688	862
Perfil por Fase
Quanto ao perfil por fase, temos a seguinte composição:
 	2020	2021	2022	Nível de Ensino
ALFA	80	120	190	2º e 3º Ensino Fundamental
1	172	136	192	4º Ensino Fundamental
2	155	162	155	5º e 6º Ensino Fundamental
3	122	115	148	7º e 8º Ensino Fundamental
4	55	59	76	9º Ensino Fundamental
5	54	50	60	1º Ensino Médio
6	30	23	18	2º Ensino Médio
7	33	19	23	3º Ensino Médio
8	24	0	0	Universitário

 
Perfil por Pedra / INDE
Na classificação do perfil dos estudantes pelo tipo de pedra, que é definida pela faixa de valor do INDE:
 	2020	2021	2022	Faixa de INDE
Quartzo	128	110	134	2,405 a 5,506 
Ágata	171	178	250	5,506 a 6,868 
Ametista	335	295	348	6,868 a 8,230 
Topázio	91	101	130	8,230 a 9,294 

 
A quantidade de estudantes nos perfis Ágata, Ametista e Topázio tiveram aumento maior que o Quartzo, ou seja, há maior porcentagem de estudantes com INDE de valores mais altos.

                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
