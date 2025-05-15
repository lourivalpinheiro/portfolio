# Importing necessary libraries
import streamlit as st
from model import *

# Page's main configuration
st.set_page_config(page_title="A arte de aprender", page_icon="🧠", layout="centered")
st.header("🧠 A arte de aprender")
st.divider()

# Page's content
st.markdown('''
            Desde pequeno, eu sempre gostei de estudar. Algumas matérias da escola captavam meu interesse com muita facilidade como o Inglês, por exemplo. Meus pais sempre exigiram muito de mim quanto aos estudos e não demorou muito para que isso se tornasse uma forma de ser validado por eles.
            
            Cresci e levei um tempo para lidar com isso de forma saudável, mas acabou que algo não tão positivo veio a formar um dos principais pilares de minha personalidade na idade adulta: a constante necessidade de aprender. Não me entenda mal, isso não é, nem de longe, algo bom... pelo contrário, coloca sobre mim o peso de nunca chegar até determinado nível de conhecimento e me sentir satisfeito, ou até mesmo não conseguir me elogiar nem ficar feliz por conquistas que muitas vezes quis com todas as minhas forças. Entretanto, é algo que me dá um próposito na vida: saber que há um Deus cujo conhecimento é infinito e que, talvez, se eu me esforçar, eu venha a ter pelo menos um glimpse dele.
            
            Trabalhei como Professor de Inglês dos 17 aos 24 anos, mas resolvi me desafiar com algo novo, algo que me tirasse da zona de conforto, que me fizesse voltar a ter contato com assuntos nos quais cresci ouvindo pessoas dizerem que eu era ruim como: matemática, raciocínio lógico, etc.; optei então pela área de Contabilidade e, após meu primeiro mês de experiência, tive contato direto com Python, uma linguagem de programação. Esse seria o encontro que mudaria minha vida para sempre.
            
            Hoje, graças ao encontro dessas duas áreas, consegui aprender coisas que jamais sonhei conseguir. Me interessei por assuntos que antes eram totalmente chatos por não saber absolutamente nada sobre. Tenho, agora, uma carreira a percorrer: tornar-me um ***Cientista de Dados*** especializado na área de Contabilidade e Finanças; e sei que todo o caminho percorrido até aqui foi necessário para que eu estivesse exatamente onde estou.
            
            Jamais deixe alguém dizer o que você é ou não capaz de ser ou fazer, tudo é uma questão de aprendizado contínuo, repetição, prática, porém, acima de tudo, uma nova oportunidade para construir uma versão melhor de si mesmo.
            ''')
st.code(
    body='''
        opportunity = "life"
        for opportunity in range(40):
            print('Nailing it!')
    ''',
    language='python')


# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


