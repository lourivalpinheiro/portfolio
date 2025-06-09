# Importing necessary modules
import streamlit as st

class Footer:
    @classmethod
    def footer(cls):
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