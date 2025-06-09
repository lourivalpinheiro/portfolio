# Importing necessary modules
import streamlit as st
from classes.footer import Footer
from classes.hideelement import HideElement
from classes.apiconnection import ApiConnecetion
from classes.plots import Chart

# Login
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.set_page_config("Login Finanças", page_icon="💵", layout="centered")
    
    HideElement.hide_header()
    
    st.header(" 💵 Dashboard Financeiro")
    with st.form("financeLogin", enter_to_submit=False):
        username = st.text_input("USUÁRIO")
        password = st.text_input("SENHA", type="password")
        validate = st.form_submit_button("ENTRAR")

        if validate:
            credentialsSpreadsheet = ApiConnecetion.get_credentials()
            if not username or not password:
                st.warning("⚠️ Preencha todos os campos.")
            else:
                user_row = credentialsSpreadsheet[credentialsSpreadsheet["username"] == username]
                if not user_row.empty and password.strip() == str(user_row.iloc[0]["password"]).strip():
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    st.error("❌ Usuário ou senha inválidos.")
    Footer.footer()
    st.stop()

# Main page's configuration after logging in
st.set_page_config("Dashboard Financeiro", page_icon="💵", layout="wide")
HideElement.hide_header()

# Página principal (após login)
st.header(" 💵 Dashboard de Finanças")
st.divider()


df = ApiConnecetion.get_budget()

col1, col2 = st.columns(2)
with col1:
    st.dataframe(df)
with col2:
    st.plotly_chart(Chart.generate_chart())

with st.sidebar:
    if st.button("SAIR"):
        st.session_state["authenticated"] = False
        st.rerun()

Footer.footer()