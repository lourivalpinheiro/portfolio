# Importing necessary libraries
import streamlit as st

from classes.footer import Footer
from classes.hideelement import HideElement

# PAge's main configuration
st.set_page_config("Projetos", page_icon="", layout="wide")
HideElement.hide_header()

# Projects
## Header
st.markdown("# 🗄️ Projetos")
st.caption("Saiba mais sobre meus projetos.")
st.divider()

tab1, tab2 = st.tabs(['Pessoais', 'Team Contabilidade'])

with tab1:
    ## Elements
    simpleCalculator, budgetCreator, roundpizza = st.columns(3, gap='small')
    
    # Simple Calculator
    with simpleCalculator:
        with st.expander(label="SIMPLE CALCULATOR"):
            st.markdown("### Simple Calculator")
            st.caption("Uma calculadora simples.")
            with st.popover("STATUS"):
                st.error("ARQUIVADO", icon="🗃️")
            st.divider()
            st.image(image="static/simplecalculator.png", width=210)
            st.link_button(
                label="BAIXAR",
                url="https://1drv.ms/u/c/1298dd6ed5ce46e7/ESxpIYzN8nRBid2lGl0o3zsBWjW6PYSFqUEjndf49iH6yQ?e=ncV9az",
                icon=":material/download:",
            )

    # BudgetCreator
    with budgetCreator:
        with st.expander(label="BUDGEN"):
            st.markdown("### Gerador de Orçamentos")
            st.caption("Cria um orçamento baseado em seu salário.")
            with st.popover("STATUS"):
                st.info("EM DESENVOLVIMENTO", icon="🚧")
            st.divider()
            st.image(image="static/budget-creator.png")
            st.link_button(
                label="ACESSAR",
                url="https://criadordeorcamentosltpneto.streamlit.app/",
                icon=":material/link:",
            )


    # Round Pizza
    with roundpizza:
        with st.expander(label="ROUND PIZZA"):
            st.markdown("### Modelo de Machine Learning")
            st.caption("Faz previsões de preços de pizzas com base no diâmetro.")
            with st.popover("STATUS"):
                st.info("ATIVO", icon="🏃‍♂")
            st.divider()
            st.image(image="static/roundpizza.png")
            st.link_button(
                label="ACESSAR",
                url="https://roundpizza.streamlit.app/",
                icon=":material/link:",
            )

with tab2:
    ## Elements
    teamOne, tributoSmartAnalytics = st.columns(2, gap='small')
    
    with teamOne:
        # Team One
        with st.expander(label="TEAM ONE"):
            st.markdown("### Team One")
            st.caption(
                "Um espaço seguro e integrado com ferramentas desenvolvidas para ajudar os setores no que concerne à comunicação, informação e automação de processos."
            )
            with st.popover("STATUS"):
                st.success("ATIVO", icon="🏃‍♂")
            st.divider()
            st.image(image="static/teamone.png")
            st.button(
                label="ACESSAR",
                disabled=True,
                help="Este app é privado."
            )
    
    with tributoSmartAnalytics:    
        # TributoSmart Analytics
        with st.expander(label="TRIBUTOSMART ANALYTICS"):
            st.markdown("### TributoSmart Analytics")
            st.caption(
                "Esboço de um app para acompanhamento e análise de recuperações tributárias."
            )
            with st.popover("STATUS"):
                st.success("ATIVO", icon="🏃‍♂")
            st.divider()
            st.image(image="static/tributoSmartAnalytics.png")
            st.markdown('''
                        #### CONTEXTO
                        ---
                        - Este projeto foi desenvolvido por mim, Neto Pinheiro, como elemento integrante da apresentação a ser feita aos responsáveis pelo setor Jurídico da Team Contabilidade, Tamires e Thiago, após ininterruptas terças-feiras de treinamento sobre Direito Empresarial e Recuperação Tributária durante o mês de maio.

                        #### OBJETIVO
                        ---
                        - O objetivo do app foi, com o conhecimento dos membros do projeto, Carlos, Marcos e eu, Neto Pinheiro, simularmos uma recuperação tributária de uma empresa fictícia. Para isso, eu resolvi criar esse app;

                        #### CARACTERÍSTICAS
                        ---
                        1. Apresentação dos dados brutos, fornecendo uma análise simples dos dados a fim de contextualizar o cliente a respeito do processo até o resultado de sua recuperação;
                        2. Área de análise mais aprofundada sobre os dados da recuperação, fornecendo ao cliente um dashboard, onde ele pode interagir com os gráficos que foram criados tendo como base atributos do conjunto de dados de sua recuperação tributária.

                        #### TECNOLOGIAS
                        ---
                        - Inteligência Artificial para criar o conjunto de dados que simulasse uma recuperação tributária;
                        - Python juntamente às bibliotecas:
                            1. Streamlit: criação da interface gráfica;
                            2. Pandas: análise exploratória de dados básica feita por mim a fim de praticar conteúdos absorvidos em meus estudos;
                            3. Plotly: criação de gráficos interativos.
                        - Paradigma de Programação orientada a objetos assim como princípios SOLID também foram aplicados ao projeto.

                        #### CONCLUSÃO
                        ---
                        - Não só fizemos um resumo do conteúdo prático que nos foi passado ao longo do mês de maio, mas também conseguimos criar o esboço de um projeto que, dado o interesse da liderança, pode vir a tornar-se uma ferramenta útil para os clientes participarem mais ativamente do processo de recuperação tributária.
                        ''')
            st.link_button(label="ACESSAR", url='https://teamcontabilidade-treinamentorecuperacaotributaria.streamlit.app/')
        

Footer.footer()
