# Importing necessary libraries
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Lifelong Learning Data
_dataframe = {
    "TECNOLOGIA": ["Django", "Flet", "Langchain"],
    "PROFIÊNCIA": ["NOVATO", "SEM CONTATO", "SEM CONTATO"]
}

# Creating dataframe
df  = pd.DataFrame(_dataframe)

# Google sheets api connection
st.cache_data()
def apiConnect():
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(
        spreadsheet=st.secrets['database']['spreadsheet'])
    return df  # ← Returning the dataframe so I can display it in the app.
