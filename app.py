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

st.title("🏐 I Torneio RS/SC de Vôlei")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("🔐 Administração")
    senha = st.text_input("Senha para editar", type="password")
    admin_logado = (senha == "volei123")
    
    if admin_logado:
        st.success("Acesso Liberado!")
        novo_time = st.text_input("Nome do Time")
        if st.button("➕ Cadastrar"):
            if novo_time:
                st.session_state.times.append(novo_time)
                st.rerun()
    else:
        st.info("Apenas visualização pública.")

# --- ABAS ---
aba1, aba2, aba3 = st.tabs(["📜 Regulamento", "📊 Grupos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial")
    st.markdown("""
    **1. Organização:** Cristiano Delfino.  
    **2. Local:** Ginásio Municipal de Torres - RS.  
    **3. Regras:** Partidas em Set Único de 25 pontos. Categoria Mista.
    """)

with aba2:
    st.header("Distribuição dos Grupos")
    
    col_a, col_b = st.columns(2)
    
    # Exibição do Grupo A
    with col_a:
        st.markdown('<div style="background-color: #004a99; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">GRUPO A</div>', unsafe_allow_html=True)
        if st.session_state.chaves:
            for t in st.session_state.chaves["Grupo A"]:
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: white; color: black;">🏐 {t}</div>', unsafe_allow_html=True)
        else:
            for i in range(1, 5):
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: #f9f9f9; color: #999;">🏐 Aguardando Time {i}</div>', unsafe_allow_html=True)

    # Exibição do Grupo B
    with col_b:
        st.markdown('<div style="background-color: #d9534f; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">GRUPO B</div>', unsafe_allow_html=True)
        if st.session_state.chaves:
            for t in st.session_state.chaves["Grupo B"]:
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: white; color: black;">🏐 {t}</div>', unsafe_allow_html=True)
        else:
            for i in range(1, 5):
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: #f9f9f9; color: #999;">🏐 Aguardando Time {i}</div>', unsafe_allow_html=True)

    if admin_logado and st.session_state.chaves is None:
        st.divider()
        if st.button("🎲 REALIZAR SORTEIO AGORA"):
            if len(st.session_state.times) >= 4:
                lista = st.session_state.times.copy()
                random.shuffle(lista)
                meio = len(lista) // 2
                st.session_state.chaves = {"Grupo A": lista[:meio], "Grupo B": lista[meio:]}
                st.snow()
                st.rerun()
            else:
                st.error("Cadastre pelo menos 4 times primeiro!")

with aba3:
    st.header("Chaveamento Mata-Mata")
    st.markdown("""
    <div style="display: flex; justify-content: space-around; align-items: center; background-color: #f0f2f6; padding: 20px; border-radius: 10px; color: black;">
        <div style="text-align: center;">
            <div style="border: 2px solid #004a99; padding: 10px; margin: 5px; background: white;">1º Grupo A vs 2º Grupo B</div>
            <div style="border: 2px solid #004a99; padding: 10px; margin: 5px; background: white;">1º Grupo B vs 2º Grupo A</div>
        </div>
        <div style="font-size: 30px;">➡️</div>
        <div style="text-align: center;">
            <div style="border: 4px solid #ffd700; padding: 15px; background: white; font-weight: bold;">GRANDE FINAL</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
