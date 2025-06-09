# Importing necessary modules
import streamlit as st

class HideElement:
    @classmethod
    def hide_header(cls):
        # Hiding hamburguer menu
        hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_st_style, unsafe_allow_html=True)