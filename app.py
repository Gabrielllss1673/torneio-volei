import streamlit as st
import random
import time

# Configuração da página
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

# Inicialização de dados
if 'times' not in st.session_state:
    st.session_state.times = []
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

# --- O SEGREDO DO ORGANIZADOR ---
# Agora usamos o novo formato do Streamlit para ler o link
is_admin = st.query_params.get("modo") == "cristiano"

# Se NÃO for admin, escondemos a barra lateral completamente via CSS
if not is_admin:
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {display: none !important;}
            [data-testid="stSidebarNav"] {display: none !important;}
        </style>
    """, unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")

# Só criamos os botões de controle se o link tiver "?modo=cristiano"
if is_admin:
    with st.sidebar:
        st.header("🏁 Painel do Cristiano")
        st.success("Modo Editor Ativo")
        
        novo_time = st.text_input("Nome do Time")
        if st.button("➕ Cadastrar Time"):
            if novo_time:
                st.session_state.times.append(novo_time)
                st.rerun()
        
        st.divider()
        
        if st.button("🎲 REALIZAR SORTEIO"):
            if len(st.session_state.times) >= 4:
                lista = st.session_state.times.copy()
                random.shuffle(lista)
                meio = len(lista) // 2
                st.session_state.chaves = {"Grupo A": lista[:meio], "Grupo B": lista[meio:]}
                st.snow()
                st.rerun()
            else:
                st.error("Precisa de 4 times!")

        if st.button("🗑️ Resetar Torneio"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# --- ABAS PÚBLICAS ---
aba1, aba2, aba3 = st.tabs(["📜 Regulamento Detalhado", "📊 Grupos & Confrontos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial")
    st.markdown("""
    ### Informações Principais
    * **Organização:** Cristiano Delfino.
    * **Data:** 29 de Março de 2026.
    * **Local:** Ginásio Municipal de Torres - RS.
    
    ### Regras de Jogo
    1. Partidas em Set Único de 25 pontos.
    2. Cada equipe deve ter pelo menos 2 mulheres em quadra (Misto).
    3. Os dois melhores de cada grupo avançam para o mata-mata.
    """)

with aba2:
    st.header("Distribuição dos Grupos")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown('<div style="background-color: #004a99; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">GRUPO A</div>', unsafe_allow_html=True)
        if st.session_state.chaves:
            for t in st.session_state.chaves["Grupo A"]:
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: white; color: black;">🏐 {t}</div>', unsafe_allow_html=True)
        else:
            for i in range(1, 5):
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: #f9f9f9; color: #999;">🏐 Aguardando Sorteio...</div>', unsafe_allow_html=True)

    with col_b:
        st.
