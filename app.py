import streamlit as st
import random
import time

# 1. Configuração e Estilo
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Esconder barra lateral para o público
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar'] {display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")

# 2. Painel Administrativo
if is_admin:
    with st.sidebar:
        st.header("🏁 Organizador")
        nt = st.text_input("Novo Time")
        if st.button("➕ Adicionar") and nt:
            st.session_state.times.append(nt)
            st.rerun()
        if st.button("🎲 SORTEAR") and len(st.session_state.times) >= 4:
            lista = st.session_state.times.copy()
            random.shuffle(lista)
            m = len(lista)//2
            st.session_state.chaves = {"A": lista[:m], "B": lista[m:]}
            st.snow()
            st.rerun()
        if st.button("🗑️ Resetar"):
            st.session_state.times = []; st.session_state.chaves = None; st.rerun()

# 3. Conteúdo das Abas
aba1, aba2, aba3 = st.tabs(["📜 Regulamento", "📊 Grupos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial")
    st.markdown("""
    **Organização:** Cristiano Delfino | **Local:** Torres - RS
    
    1. **Misto:** Mínimo de 2 mulheres em quadra.
    2. **Jogos:** Set único de 25 pontos.
    3. **Classificação:** Top 2 de cada grupo avançam.
    4. **Horário:** Chegada às 07:30h, início às 08:00h.
    """)

with aba2:
    st.header("Distribuição dos Grupos")
    ca, cb = st.columns(2)
    with ca:
        st.markdown('<div style="background:#004a99;color:white;padding:10px;text-align:center;font-weight:bold;">GRUPO A</div>', unsafe_allow_html=True)
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in ta:
            st.markdown(f'<div style="border:1px solid #ddd;padding:10px;background:white;color:black;">🏐 {t}</div>', unsafe_allow_html=True)
    with cb:
        st.markdown('<div style="background:#d9534f;color:white;padding:10px;text-align:center;font-weight:bold;">GRUPO B</div>', unsafe_allow_html=True)
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in tb:
            st.markdown(f'<div style="border:1px solid #ddd;padding:10px;background:white;color:black;">🏐 {t}</div>', unsafe_allow_html=True)

with aba3:
    st.header("Chaveamento Final")
    st.markdown("""
    <div style="display:flex;justify-content:space-around;align-items:center;background:#f0f2f6;padding:20px;border-radius:10px;color:black;">
        <div style="text-align:center;"><b>SEMIFINAIS</b>
            <div style="border:1px solid #004a99;padding:10px;margin:5px;background:white;">1º A vs 2º B</div>
            <div style="border:1px solid #004a99;padding:10px;margin:5px;background:white;">1º B vs 2º A</div>
        </div>
        <div style="font-size:30px;">➡️</div>
        <div style="text-align:center;"><b>FINAL</b>
            <div style="border:3px solid #ffd700;padding:15px;background:white;font-weight:bold;">🏆 GRANDE FINAL</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
