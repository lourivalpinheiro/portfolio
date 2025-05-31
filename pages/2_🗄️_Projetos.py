# Importing necessary libraries
import streamlit as st

# PAge's main configuration
st.set_page_config("Projetos", page_icon="", layout="centered")
# Projects
## Header
st.markdown("# 🗄️ Projetos")
st.caption("Saiba mais sobre meus projetos.")
st.divider()

tab1, tab2 = st.tabs(['Pessoais', 'Team Contabilidade'])

with tab1:
    ## Elements
    simpleCalculator, budgetCreator = st.columns(2, gap='small')
    
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

with tab2:
    # PLanilhas NFSe
    with st.expander(label="TEAM ECOSYSTEM"):
        st.markdown("### Team Ecosystem")
        st.caption(
            "Um ecossistema com ferramentas desenvolvidas para ajudar os setores no que concerne à comunicação, informação e automação de processos."
        )
        with st.popover("STATUS"):
            st.success("ATIVO", icon="🏃‍♂")
        st.divider()
        st.image(image="static/teamEco.png")
        st.button(
            label="ACESSAR",
            disabled=True,
            help="Este app é privado."
        )

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
