import streamlit as st
import pandas as pd
from model import credentialsSpreadsheet, incomeXexpenseAnalysisFig, df



# Login
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.set_page_config("Login Finanças", page_icon="💵", layout="centered")
    
    # Ocultar menus
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    st.header(" 💵 Dashboard Financeiro")
    with st.form("financeLogin"):
        username = st.text_input("USUÁRIO")
        password = st.text_input("SENHA", type="password")
        validate = st.form_submit_button("ENTRAR")

        if validate:
            if not username or not password:
                st.warning("⚠️ Preencha todos os campos.")
            else:
                user_row = credentialsSpreadsheet[credentialsSpreadsheet["username"] == username]
                if not user_row.empty and password.strip() == str(user_row.iloc[0]["password"]).strip():
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    st.error("❌ Usuário ou senha inválidos.")
    st.stop()

# Main page's configuration after logging in
st.set_page_config("Dashboard Financeiro", page_icon="💵", layout="wide")

# Ocultar menus
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Página principal (após login)
st.header(" 💵 Dashboard de Finanças")
st.divider()

tab1, tab2 = st.tabs(["ORÇAMENTO", "LIVRO DIÁRIO"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(df)
    with col2:
        st.plotly_chart(incomeXexpenseAnalysisFig)

with tab2:
    subtab1, subtab2 = st.tabs(["REGISTRO", "VISUALIZAÇÕES"])
    with subtab1:
        with st.form("financeTrackerForm", clear_on_submit=True):
            operation = st.text_input("OPERAÇÃO")
            factDate = st.date_input("DATA")
            category = st.selectbox("TIPO", ["RECEITA", "DESPESA"], index=None)
            amount = st.number_input("VALOR", min_value=0.0)
            submited = st.form_submit_button("REGISTRAR")

            if submited:
                if not operation or not factDate or not category or not amount:
                    st.warning("⚠️ Preencha todos os campos.")
                else:
                    st.success("Operação registrada!")  # Aqui você pode registrar os dados

        st.dataframe(pd.DataFrame({"TESTE": []}))
    with subtab2:
        st.write("Vazio")

with st.sidebar:
    if st.button("SAIR"):
        st.session_state["authenticated"] = False
        st.rerun()
