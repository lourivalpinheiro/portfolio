# Importing necessary libraries
import streamlit as st
from streamlit import switch_page
from model import *

# Page's main configuration
st.set_page_config("Login Finanças", page_icon="💵")
st.header(" 💵 Dashboard Financeiro")

# Login form
with st.form("financeLogin"):
    username = st.text_input("USUÁRIO")
    password = st.text_input("SENHA", type="password")
    validate = st.form_submit_button("ENTRAR")

    if validate:
            if not username or not password:
                st.warning("⚠️ Preencha todos os campos.")
            else:
                # Verifying if user exists within the spreadsheet
                user_row = credentialsSpreadsheet[credentialsSpreadsheet['username'] == username]
                
                if not user_row.empty:
                    # Strip to remove extra spaces
                    senha_digitada = password.strip()
                    senha_salva = str(user_row.iloc[0]['password']).strip()

                    # Now that I've minimized the potential errors, I validate it.
                    if senha_digitada == senha_salva:
                        st.session_state['authenticated'] = True
                        switch_page("pages/5_💵_Dashboard_Financeiro.py")
                    else:
                        st.error(" ❌ Senha incorreta.")
                else:
                    st.error("❌ Usuário não encontrado.")
            