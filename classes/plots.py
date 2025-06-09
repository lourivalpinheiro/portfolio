# Importing necessary modules
import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_gsheets import GSheetsConnection

class Chart():
    @staticmethod
    @st.cache_data
    def generate_chart():
        # Budget
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(
            spreadsheet=st.secrets["database"]["spreadsheet"],
            worksheet=st.secrets["database"]["budgetWorksheet"],
        )

        # VISUALIZATIONS
        ## DF ANALYSIS
        df["VALOR"] = pd.to_numeric(
            df["VALOR"]
            .astype(str)
            .str.replace(",", ".")
            .str.replace("R\$", "", regex=True)
            .str.strip(),
            errors="coerce",
        )

        incomeXexpenseAnalysis = df.groupby("TIPO")["VALOR"].sum().reset_index()

        ## Plotly bar chart
        incomeXexpenseAnalysisFig = px.bar(
            incomeXexpenseAnalysis, x="TIPO", y="VALOR", color_discrete_sequence=['green'], text_auto=True
        )
        return incomeXexpenseAnalysisFig