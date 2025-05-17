# Importing necessary libraries
import streamlit as st
from streamlit import switch_page
from model import *

# Page's main configuration
st.set_page_config("Login Finanças", page_icon="💵", layout="wide")

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Checking login state
if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
    st.image("static/loginImage.svg")
    st.warning("Por favor, faça o login para continuar.")
    st.stop()

st.header(" 💵 Dashboard de Finanças")
st.divider()

# Page's content
tab1, tab2 = st.tabs(["ORÇAMENTO", "LIVRO DIÁRIO"])
with tab1:
    dataFrame, visualization = st.columns(2, gap="large")
    
    with dataFrame:
        st.dataframe(df)
    
    with visualization:
        st.plotly_chart(incomeXexpenseAnalysisFig)
    
        
with tab2:
    tab1, tab2 = st.tabs(["REGISTRO", "VISUALIZAÇÕES"])
    with tab1:
        with st.form("financeTrackerForm", clear_on_submit=True, enter_to_submit=False):
            operation = st.text_input("OPERAÇÃO", placeholder="Insira o nome da operação...")
            factDate = st.date_input("DATA", format="DD/MM/YYYY", value="today")
            category = st.selectbox("TIPO", placeholder="Selecione um tipo de operação...", options=["RECEITA", "DESPESA"], index=None)
            amount = st.number_input("VALOR")
            submited = st.form_submit_button("REGISTRAR")
            
            if submited:
                if not operation or factDate or category or amount:
                    st.warning("Preencha todos os campos")
                else:
                    pass
            
        emptyData = {
        "TESTE": [],
        }
        emptyDataFrame = pd.DataFrame(emptyData)
        st.dataframe(emptyDataFrame)
    
    with tab2:
        st.write("Vazio")

with st.sidebar:
    logoutButton = st.button("SAIR")
    if logoutButton:
        st.session_state['authenticated'] = False
        switch_page('pages/3_💵_Login_Dashboard_Financeiro.py')


# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
