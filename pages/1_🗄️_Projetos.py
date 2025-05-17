# Importing necessary libraries
import streamlit as st

# PAge's main configuration
st.set_page_config("Projetos", page_icon="", layout="centered")
# Projects
## Header
st.markdown("# 🗄️ Projetos")
st.caption("Saiba mais sobre meus projetos.")
st.divider()

## Elements
simpleCalculator, budgetCreator, planilhasNfse = st.columns(3, gap="small")

with simpleCalculator:
    with st.expander(label="Simple Calculator"):
        st.markdown("### Simple Calculator")
        st.caption("Uma calculadora simples.")
        with st.popover("STATUS"):
            st.error("ARQUIVADO", icon="🗃️")
        st.divider()
        st.image(image="static/simplecalculator.png", width=210)
        st.link_button(label="BAIXAR", url="https://1drv.ms/u/c/1298dd6ed5ce46e7/ESxpIYzN8nRBid2lGl0o3zsBWjW6PYSFqUEjndf49iH6yQ?e=ncV9az", icon=":material/download:")

with budgetCreator:
    with st.expander(label="BUDGEN"):
        st.markdown("### Gerador de Orçamentos")
        st.caption("Cria um orçamento baseado em seu salário.")
        with st.popover("STATUS"):
            st.info("EM DESENVOLVIMENTO", icon="🚧")
        st.divider()
        st.image(image="static/budget-creator.png")
        st.link_button(label="ACESSAR", url="https://criadordeorcamentosltpneto.streamlit.app/", icon=":material/link:")

with planilhasNfse:
    with st.expander(label="Planilhas Nfse"):
        st.markdown("### Planilhas Nfse")
        st.caption("Cria um modelo de importação de planilhas de notas de serviço para o sistema [Domínio](https://www.dominiosistemas.com.br/).")
        with st.popover("STATUS"):
            st.success("ATIVO", icon="🏃‍♂")
        st.divider()
        st.image(image="static/planilhasnfse.png")
        st.button(label="ACESSAR", disabled=True, help="No momento, este app é privado. Uma versão pública será lançada em breve.")

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
