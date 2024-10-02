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
        DISCUSSÃO SOBRE AS ANÁLISES REALIZADAS

        * **Quais indicadores cooperaram mais para o atual cenário?**
        Pelas análises realizadas, podemos dizer que o Indicador Psicopedagógico (IPP) e o Indicador de Engajamento (IEG) tiveram maior influência do que os outros indicadores no INDE. Se olharmos o mapa de correlação, uma mudança nesses dois pontos pode afetar justamente a avaliação do Indicador do Ponto de Virada (IPV). Como o fator de saúde mental e a realização de atividades afetam diretamente a capacidade de aprendizado, isso pode ter influenciado o Indicador de Desempenho Acadêmico e, por consequência, o Indicador de Ponto de Virada.
        
        * **Seria algum fator psicológico ou acadêmico muito relevante? Algum fator de engajamento?**
        O que sabemos por pesquisa e notícias referentes ao período da Pandemia é que o aprendizado foi afetado pela política de isolamento e ausência de aulas presenciais. Por conta desse isolamento, o convívio social e as atividades em grupo foram afetadas e isso afetou diretamente o desenvolvimento e o aprendizado. Para recuperar desse cenário, é muito provável que muitas atividades foram propostas para os estudantes como forma de manter a saúde mental. Ou seja, engajar em atividades pode ser um ponto inicial muito bom para que os outros indicadores melhorem. Sobre o perfil daqueles que apresentaram Ponto de Virada igual a “sim” em 2022, podemos notar que há certas oscilações entre os indicadores, com um apresentando queda e o outro compensando essa queda, como se fosse uma mudança de foco nos períodos, como uma revisão de prioridade.


        * **O que poderia ser feito para melhorar isso?**
        De acordo com as conversas em “Lives” que tivemos com o senhor Dimitri, da Passos Mágicos, o trabalho psicopedagógico tem tido papel crítico para a melhoria depois dos impactos da Pandemia, como fomentar nos estudantes um cenário de desafio, que a vida pode mostrar muito mais do que eles enxergam no atual momento e que essa jornada pode ser um ponto importante para o ponto de virada na vida. 
        Outro ponto também que notamos durante a análise dos dados e das outras bases fornecidas é que algumas pessoas conseguem ir bem academicamente, porém tem certos problemas sociais. Poderia ser um indicativo de autismo? Sim, como foi comentado nas conversas das “Lives”, tanto que há estudantes que fazem tratamento para autismo. Podemos considerar ainda algum trauma complexo que necessita um trabalho mais pormenorizado.
        

        * **O que poderia ser feito para adequar comparações entre a Passos Mágicos e outros índices públicos de educação?**
        Este foi um questionamento feito na primeira “Live” sobre o Datathon e desde então pensamos em algumas possibilidades sobre o público que precisaria ver esses resultados. É notório que o projeto da Passos Mágicos funciona e muito bem, porém são necessárias comparações para ver em que pontos se sobressai em relação a muitas escolas ou associações.
        Logo, se for possível, obter as notas de provas como o Saeb dos estudantes, vestibulares e outros possíveis testes que mostrem a capacidade desses estudantes seria um claro indicativo para variados públicos que, sim, este projeto funciona.
        Também, se possível, comparar o desempenho de bolsistas com os estudantes regulares de escolas privadas, para mostrar que o trabalho psicológico da associação tem grande peso na formação do estudante.
        Outro ponto a considerar também seria o caminho para os estudantes chegarem na fase 8 (Ensino Superior ou Técnico), que ficou carente neste trabalho por falta de mais informações de universitários nos anos 2021 e 2022.

    """
    )

