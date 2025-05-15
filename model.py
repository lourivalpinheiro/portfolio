# Importing necessary libraries
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Credentials
connCredentials = st.connection("gsheets", type=GSheetsConnection)
credentialsSpreadsheet = connCredentials.read(
    spreadsheet=st.secrets['database']['spreadsheet'],
    worksheet=st.secrets['database']['credentialsWorksheet']
    )

# Google sheets api connection
st.cache_data(show_spinner=True)
def apiConnect():
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(
        spreadsheet=st.secrets['database']['spreadsheet'])
    return df  # ← Returning the dataframe so I can display it in the app.

# Budget
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(
    spreadsheet=st.secrets['database']['spreadsheet'],
    worksheet=st.secrets['database']['budgetWorksheet']
    )

# VISUALIZATIONS
## DF ANALYSIS
df['VALOR'] = pd.to_numeric(
    df['VALOR']
    .astype(str)
    .str.replace(',', '.')
    .str.replace('R\$', '', regex=True)
    .str.strip(),
    errors='coerce'
)
incomeXexpenseAnalysis = df.groupby("TIPO")["VALOR"].sum().reset_index()

## Plotly bar chart
incomeXexpenseAnalysisFig = px.bar(incomeXexpenseAnalysis, x='TIPO', y='VALOR', color_continuous_scale='GREEN')