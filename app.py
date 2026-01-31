import streamlit as st
import random

# 1. Configurações de Estilo Premium
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

st.markdown("""
    <style>
    /* Fundo Escuro Profissional */
    .stApp {
        background-color: #0E1117;
    }
    /* Estilização dos Cards de Chaves */
    .stInfo {
        background-color: #1E2129 !important;
        border: 1px solid #30363D !important;
        border-radius: 10px !important;
    }
    /* Cores do Brasil discretas nos títulos */
    h1 {
        color: #FFDF00 !important; /* Amarelo */
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    h3 {
        color: #009b3a !important; /* Verde */
    }
    /* Esconder o menu lateral para usuários */
    [data-testid="stSidebar"] {
        background-color: #161B22;
    }
    </style>
    """, unsafe_allow_html=True)

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Admin
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC DE VÔLEI")
st.markdown("<p style='text-align: center; color: #8B949E;'>Torneio Aberto Masculino de Quadra | Torres - RS</p>", unsafe_allow_html=True)

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("⚙️ Painel do Cristiano")
        nome = st.text_input("Nome da Equipe")
        if st.button("➕ Adicionar") and nome:
            st.session_state.times.append(nome); st.rerun()
        st.divider()
        if st.button("🎲 GERAR CHAVES") and len(st.session_state.times) >= 4:
            lista = list(st.session_state.times); random.shuffle(lista)
            m = len(lista) // 2
            st.session_state.chaves = {"A": lista[:m], "B": lista[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Limpar Tudo"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas Organizadas
t1, t2, t3, t4 = st.tabs(["📋 REGULAMENTO", "🚫 FEDERADOS", "📊 CHAVES", "🏆 MATA-MATA"])

with t1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 Local e Data")
        st.write("📅 **Data:** 22/02/2026")
        st.write("🏫 **Local:** Escola Sagrado")
        st.write("🕗 **Início:** 08:00h (10 min de tolerância)")
    with col2:
        st.subheader("💰 Inscrição")
        st.write("✅ **Valor:** R$ 400,00 por equipe")
        st.write("🔑 **Pix:** (51) 99881-6326 (Cristiano Delfino)")
    
    st.divider()
    st.subheader("
