# Importing necessary modules
import streamlit as st

# Page's main configuration
st.set_page_config(page_title='PyCharm', page_icon='🐍', layout='wide')

# Page's header
st.title('📰 Blog')
st.divider()

with st.expander('PyCharm Professional'):
    # Hiding humburguer menu
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Page's content

    ## Definition
    st.markdown("""
    # 🐍 Por que escolhi o **PyCharm** como minha IDE profissional de desenvolvimento Python?
    
    Ao longo da minha jornada com Python, explorei diversas opções de ambientes de desenvolvimento integrados (IDEs). Após avaliar criteriosamente fatores como produtividade, recursos integrados, suporte a projetos complexos e experiência do usuário, optei por adotar o **PyCharm** como minha IDE principal. Abaixo, explico as razões por trás dessa escolha.
    
    ---
    
    ## 🔍 O que é o PyCharm?
    
    O **PyCharm** é uma IDE (Ambiente de Desenvolvimento Integrado) totalmente focada na linguagem **Python**. Desenvolvido pela JetBrains, ele foi projetado para oferecer suporte completo ao ciclo de vida do desenvolvimento Python — desde projetos simples até aplicações complexas em áreas como **Data Science**, **desenvolvimento web**, automação e muito mais.
    
    Sua interface intuitiva e os diversos recursos nativos tornam o desenvolvimento mais fluido, produtivo e organizado.
    
    ---
    
    ## ✅ Principais Motivos da Escolha
    
    1. **Ambientes virtuais integrados de forma eficiente:**  
       Assim como o VS Code, o PyCharm permite criar e gerenciar ambientes virtuais por projeto. Porém, sua interface oferece uma visualização mais clara e organizada da estrutura de pastas e arquivos, o que facilita o gerenciamento de dependências e configurações específicas de cada projeto.
    
    2. **Ferramentas nativas poderosas:**  
       O PyCharm possui recursos robustos como **debugger visual**, **testes automatizados**, **autoimportação de bibliotecas**, **refatoração inteligente**, **complementação de código** e **integração com bancos de dados** — tudo isso sem a necessidade de instalar dezenas de extensões, como ocorre em outras IDEs.
    
    3. **Foco total em Python:**  
       Por ser especializado em Python, o PyCharm oferece suporte superior para frameworks como Django, Flask e FastAPI, além de bibliotecas populares de ciência de dados, como NumPy, Pandas, Matplotlib e Scikit-Learn.
    
    4. **Integração com controle de versão (Git):**  
       O controle de versões com Git é totalmente integrado e facilita a visualização de alterações, commits e gerenciamento de branches diretamente pela interface.
    
    5. **Confiabilidade e estabilidade:**  
       Como ferramenta madura e consolidada no mercado, o PyCharm proporciona uma experiência estável, com atualizações frequentes e suporte técnico sólido da JetBrains.
    
    ---
    
    ## 🧩 Conclusão
    
    Em resumo, escolhi o **PyCharm** porque ele me proporciona um ambiente de trabalho mais completo, organizado e eficiente. Com ele, consigo manter um alto padrão de qualidade nos meus projetos Python e garantir maior produtividade no meu dia a dia profissional.    
    """)
