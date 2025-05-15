# Importing necessary libraries
import streamlit as st
from model import *

# Page's main configuration
st.set_page_config(page_title="Currículo", layout="centered")

# Page's Content 
st.image(image="static/netopinheiro.jpeg", width=150)

st.markdown("# Neto Pinheiro")
st.link_button(label="LINKEDIN", url="https://www.linkedin.com/in/lourival-pinheiro-7a8744254?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BTA0WPmJVRV%2BjYt8Fi0ALJw%3D%3D", icon=":material/badge:")

tab1, tab2, tab3, tab4 = st.tabs(["SOBRE", "EDUCAÇÃO", "COMPETÊNCIAS", "EXPERIÊNCIA"])
with tab1:
    st.markdown("#### Cientista de Dados")
    st.caption("Apaixonado por transformar dados em soluções reais para negócios.")
    st.divider()
    st.markdown('''
                Olá! Meu nome é Neto Pinheiro, tenho 25 anos e sou natural de Palmares, Pernambuco, Brasil.

                Atualmente, estou desenvolvendo meu Domínio de Negócio em Contabilidade com objetivo de projetar soluções de dados robustas, escaláveis e orientadas a resultados, que contribuam diretamente para a resolução de problemas e a melhoria de processos nas empresas. Acredito no poder dos dados como ferramenta estratégica, capaz de gerar valor e inovação em diferentes setores.

                Estou sempre em busca de novos aprendizados, desafios e conexões que me ajudem a crescer como profissional e a contribuir de forma significativa com a área de Ciência de Dados.

                📌 Principais interesses:
                
                - Software Engineering;
                
                - Machine Learning;
                
                - Inteligência Artificial;
                
                - Desenvolvimento de dashboards e relatórios interativos;
                
                - Tomada de decisão orientada por dados;
                
                - Automação de processos.
                
        
''')

with tab2:
    st.markdown("#### Cebrac Anápolis")
    st.caption("Auxiliar Administrativo Financeiro")
with tab3:
    softSkills, hardSkills = st.columns(2)
    with softSkills:
        st.markdown("#### Soft Skills")
        st.divider()
        st.markdown('''
            - Comunicação;
            - Inteligência Emocional;
            - Liderança;
            - Proatividade;
            - Trabalho em equipe.
        ''')

    with hardSkills:
        st.markdown("#### Hard Skills")
        st.divider()
        st.markdown('''
            - Contabilidade: Básico;
            - Django: básico;
            - Excel: avançado;
            - Estatística: básico;
            - Github: intermediário;
            - Machine Learning: básico;
            - Matématica: básico;
            - Modelagem de Dados: básico;
            - Plotly: básico;
            - Power BI: intermediário;
            - Python: básico;
            - SQL: básico;
            - Streamlit: intermediário.
        ''')


with tab4:
    st.markdown("### Team Contabilidade")
    st.caption("Junho de 2024 - Presente momento")
    st.divider()
    st.markdown("📍 Assistente Contábil Jr.")
    st.caption("mar de 2025 - Presente momento")
    st.caption('''Agora, minha jornada consiste em aprimorar a execução de todos os processos que me foram ensinados, além de aprender os procedimentos de conferência restantes. Mesmo tendo dominado todos os processos de conferências, precisarei me aprofundar na lógica de como as coisas funcionam para questões nas quais ainda não tenho o conhecimento contábil necessário, afinal, não adianta realizar processos sem antes compreender aquilo que está sendo feito. Só após todas essas etapas, espero ser preparado para iniciar os fechamentos de Balancete e DRE.''')
    st.markdown("⬆️ Auxiliar Administrativo")
    st.caption("jun de 2024 - mar de 2025")
    st.caption(" Minha responsabilidade é organizar a documentação enviada pelos clientes, assegurando que esteja em conformidade com o período de competência e estruturada corretamente para o devido registro dos fatos contábeis no sistema Domínio. Adicionalmente, realizo a conferência de relatórios cruciais que, em conjunto, irão compor as demonstrações contábeis.")

# Hiding humburguer menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


