import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.subheader("Unindo estados, celebrando o vôlei!")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão Cristiano")
        nt = st.text_input("Nome da Equipe")
        if st.button("➕ Adicionar") and nt:
            st.session_state.times.append(nt); st.rerun()
        st.divider()
        if st.button("🎲 SORTEAR") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times); random.shuffle(lst)
            m = len(lst)//2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas de Conteúdo
t1, t2, t3, t4 = st.tabs(["📜 Regulamento", "🚫 Federados", "📊 Chaves", "🏆 Mata-Mata"])

with t1:
    st.markdown("### 📋 Informações Gerais (PDF)")
    st.info("📅 22/02/2026 | 🏫 Escola Sagrado (Torres/RS) | 🕗 08:00h")
    st.write("**• Valor:** R$ 400,00 (PIX: 51 99881-6326)")
    st.write("**• Formato:** Set único de 25 pts até a Semi. Final em Melhor de 3 Sets.")
    st.write("**• Equipes:** Até 12 atletas. 6 substituições e 2 tempos por set.")
    st.write("**• Aquecimento:** 6 min na primeira partida de cada time.")
    st.write("**• Prêmios:** Troféus e medalhas (1º ao 3º) + Destaques Individuais.")

with t2:
    st.header("🛡
