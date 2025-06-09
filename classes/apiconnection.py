# importing necessary modules
from streamlit_gsheets import GSheetsConnection
import streamlit as st

class ApiConnecetion:
    @staticmethod
    @st.cache_data
    def get_lifelong_learning():
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(spreadsheet=st.secrets["database"]["spreadsheet"])
        return df  # ← Returning the dataframe so I can display it in the app.

    @staticmethod
    @st.cache_data
    def get_credentials():
        # Credentials
        conn_credentials = st.connection("gsheets", type=GSheetsConnection)
        credentials_content = conn_credentials.read(
            spreadsheet=st.secrets["database"]["spreadsheet"],
            worksheet=st.secrets["database"]["credentialsWorksheet"],
        )
        return credentials_content

    @staticmethod
    @st.cache_data
    def get_budget():
        # Budget
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(
            spreadsheet=st.secrets["database"]["spreadsheet"],
            worksheet=st.secrets["database"]["budgetWorksheet"],
        )
        return df
