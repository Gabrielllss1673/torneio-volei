import streamlit as st
import random

# 1. Configurações de Estilo (Fundo Claro e Moderno)
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #004a99 !important;
        font-family: 'Arial';
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 10px;
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
st.write("Torneio Aberto Masculino de Quadra - Torres/RS")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("🏁 Painel Admin")
        nome = st.text_input("Nome da Equipe:")
        if st.button("➕ Adicionar") and nome:
            st.session_state.times.append(nome)
            st.rerun()
        st.divider()
        if st.button("🎲 SORTEAR") and len(st.session_state.times) >= 4:
            lista = list(st.session_state.times)
            random.shuffle(lista)
            m = len(lista) // 2
            st.session_state.chaves = {"A": lista[:m], "B": lista[m:]}
            st.rerun()
        if st.button("🗑️ Resetar"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas
t1, t2, t3, t4 = st.tabs(["📜 REGULAMENTO", "🚫 FEDERADOS", "📊 CHAVES", "🏆 MATA-MATA"])

with t1:
    st.markdown("### 📍 Informações Gerais")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Data:** 22/02/2026")
        st.write("**Local:** Escola Sagrado")
        st.write("**Início:** 08:00h")
    with col2:
        st.write("**Inscrição:** R$ 400,00")
        st.write("**Pix:** (51) 99881-6326")
        st.write("**Bola:** Penalty 8.0")
    
    st.divider()
    st.markdown("### ⚙️ Regras Técnicas")
    st.write("- Set único de 25 pontos até a semifinal.")
    st.write("- Finais (1º, 2º e 3º) em melhor de 3 sets.")
    st.write("- Até 12 atletas por equipe.")
    st.write("- 6 substituições e 2 tempos por set.")

with t2:
    st.header("🚫 Regra de Federados")
    st.warning("Limite: Apenas 1 (um) atleta federado por equipe.")
    st.write("O torneio é amador. Considera-se federado o atleta com registro ativo.")
    st.info("O descumprimento gera desclassificação imediata (Item 1.5).")

with t3:
    st.header("📊 Chaves")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**GRUPO A**")
        ta = st.session_state.chaves["A"] if st.session_state.chaves else []
        for t in ta: st.info(t)
    with c2:
        st.markdown("**GRUPO B**")
        tb = st.session_state.
