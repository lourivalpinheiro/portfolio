# Importing necessary libraries
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Google sheets api connection
st.cache_data(show_spinner=True)
def apiConnect():
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(
        spreadsheet=st.secrets['database']['spreadsheet'])
    return df  # ← Returning the dataframe so I can display it in the app.
