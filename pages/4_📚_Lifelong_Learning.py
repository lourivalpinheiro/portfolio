# Importing necessary libraries
import streamlit as st
from classes.footer import Footer
from classes.apiconnection import ApiConnecetion
from classes.hideelement import HideElement

# Hiding header
HideElement.hide_header()

# Header
st.markdown("# 📚 Lifelong Learning")
st.caption("Saiba mais sobre meus estudos.")
st.divider()

# Google Sheets Connection
lllData = ApiConnecetion.get_lifelong_learning()
st.dataframe(lllData, use_container_width=True)

Footer.footer()
