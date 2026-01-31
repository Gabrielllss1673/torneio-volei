import streamlit as st
import random
import time

# 1. Configuração Inicial
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state:
    st.session_state.times = []
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

# 2. Sistema de Acesso Secreto
# Use ?modo=cristiano no final da URL para abrir o painel
is_admin = st.query_params.get("modo") == "cristiano"

if not is_admin:
    st.markdown("<style>[data-testid='stSidebar'] {display: none !important;}</style>", unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")

# 3. Painel do Organizador (Só aparece com o link secreto)
if is_admin:
    with st.sidebar:
        st.header("🏁 Painel do Cristiano")
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
                st.session_state.chaves = {"A": lista[:meio], "B": lista[meio:]}
                st.snow()
                st.rerun()
        
        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# 4. Conteúdo Público (Abas)
aba1, aba2, aba3 = st.tabs(["📜 Regulamento", "📊 Grupos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial")
    st.markdown("""
    **Organização:** Cristiano Delfino  
    **Data:** 29 de Março de 2026  
    **Local:** Ginásio Municipal de Torres - RS  
    
    * Partidas em Set Único de 25 pontos.
    * Mínimo 2 mulheres em quadra (Misto).
    """)

with aba2:
    st.header("Distribuição dos Grupos")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown('<div style="background-color:#004a99;color:white;padding:10px;border-radius:10px 10px 0 0;text-align:center;font-weight:bold;">GRUPO A</div>', unsafe_allow_html=True)
        times_a = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in times_a:
            st.markdown(f'<div style="border:1px solid #ddd;padding:10px;background:white;color:black;">🏐 {t}</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div style="background-color:#d9534f;color:white;padding:10px;border-radius:10px 10px 0 0;text-align:center;font-weight:bold;">GRUPO B</div>', unsafe_allow_html=True)
        times_b = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando..."]*4
        for
