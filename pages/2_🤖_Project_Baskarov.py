# Importing necessary libraries
import streamlit as st
from classes.hideelement import HideElement

# Page's main configuration
st.set_page_config('Project Baskarov', page_icon='🤖', layout='centered')
HideElement.hide_header()

# Page's content
st.header('🤖 Project Baskarov')
st.divider()

# Chatbot
chatbot =  st.chat_input(placeholder='Pergunte ao Baskarov...')
if chatbot:
    with st.chat_message(name='ai', avatar='static/chatbot.png'):
            st.write("Olá! Me chamo Baskarov, Inteligência Artificial que deve ser uma cópia da mente de Neto Pinheiro, meu criador. Eu não sei muita coisa sobre ele, no momento, porque estou em desenvolvimento, mas vai ser um prazer ver você por aqui uma vez que eu esteja finalizado. See you later!")

