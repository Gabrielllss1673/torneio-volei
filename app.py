import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC de Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.subheader("Torneio Aberto Masculino de Quadra")

# 2. Painel Administrativo
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão Cristiano")
        nt = st.text_input("Nome da Equipe")
        if st.button("➕ Adicionar Equipe") and nt:
            st.session_state.times.append(nt); st.rerun()
        st.divider()
        if st.button("🎲 SORTEAR CHAVES") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times); random.shuffle(lst)
            m = len(lst)//2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas com as Regras do PDF
t1, t2, t3, t4 = st.tabs(["📜 Regulamento Técnico", "🚫 Federados", "📊 Chaves e Jogos", "🏆 Premiação"])

with t1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**🗓 DATA:** 22 de fevereiro de 2026\n\n**📍 LOCAL:** Escola Sagrado\n\n**🕗 INÍCIO:** 08:00h")
    with col2:
        st.markdown(f"**💰 INSCRIÇÃO:** R$ 400,00\n\n**🏐 BOLA:** Penalty 8.0\n\n**👤 ORGANIZAÇÃO:** Cristiano Delfino")
    
    st.divider()
    st.markdown("""
    ### Principais Regras:
    * **Equipes:** Até 12 atletas inscritos.
    * **Fases:** Classificatória, Quartas e Semis em **Set Único de 25 pontos**.
    * **F
