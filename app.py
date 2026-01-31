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

# 3. Abas com as Regras Oficiais do PDF
t1, t2, t3, t4, t5 = st.tabs(["📜 Regulamento", "🚫 Federados", "📊 Chaves", "🏆 Mata-Mata", "🏅 Premiação"])

with t1:
    st.markdown("### 📍 Informações Gerais")
    st.write("📅 **Data:** 22 de fevereiro de 2026")
    st.write("🏫 **Local:** Escola Sagrado - Torres/RS")
    st.write("🕗 **Início:** 08:00h (Tolerância 10 min na 1ª partida)")
    st.divider()
    st.markdown("### ⚙️ Regras Técnicas")
    st.write("• **Sets:** Único de 25 pontos (Classificatória, Quartas e Semis).")
    st.write("• **Final:** Melhor de 3 Sets (1º, 2º e 3º lugares).")
    st.write("• **Tempos:** 2 tempos técnicos por set.")
    st.write("• **Aquecimento:** 6 min na primeira partida (3' ponta, 2' saída, 1' saque).")

with t2:
    st.header("Regra para Atletas Federados
