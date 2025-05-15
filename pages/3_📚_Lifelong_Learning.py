# Importing necessary libraries
import streamlit as st 
from model import *

# Stay updated
st.markdown("# 📚 Lifelong Learning")
st.caption("Saiba mais sobre meus estudos.")
st.divider()
# Google Sheets Connection
lllData = apiConnect()
st.dataframe(lllData, use_container_width=True)
# Refreshind data
def refreshData():
    st.cache_data.clear()
    
st.button("ATUALIZAR", on_click=refreshData, help="Atualiza os dados da tabela.")

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Footer
footer = """
<style>
/* Hide default Streamlit footer */
footer {visibility: hidden;}

.footer-custom {
    position: relative;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: 14px;
    color: #ffff;
    padding: 10px 0;
    margin-top: auto;
}
</style>

<div class="footer-custom">
    © Developed by <strong>Neto Pinheiro<strong/>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)