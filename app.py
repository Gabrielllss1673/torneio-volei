import streamlit as st
import random

# 1. Configurações
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.write("Torneio Aberto Masculino de Quadra - Realização: Cristiano Delfino")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("🏁 Painel Admin")
        nt = st.text_input("Nome do Time")
        if st.button("➕ Adicionar") and nt:
            st.session_state.times.append(nt); st.rerun()
        if st.button("🎲 SORTEAR") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times); random.shuffle(lst)
            m = len(lst)//2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Resetar"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas Fixas (Informações do PDF)
t1, t2, t3, t4, t5 = st.tabs(["📜 Regras", "🚫 Federados", "📊 Chaves", "🏆 Mata-Mata", "🏅 Prêmios"])

with t1:
    st.info("📅 22/02/2026 | 🏫 Escola Sagrado | 🕗 08:00h")
    st.markdown("**Regulamento:**")
    st.write("- Set único de 25 pontos (Classificatória até Semis).")
    st.write("- Finais (1º, 2º e 3º) em Melhor de 3 Sets.")
    st.write("- Inscrição: R$ 400,00 | Bola: Penalty 8.0")

with t2:
    st.header("Atletas Federados")
    st.warning("⚠️ LIMITE: Apenas 1 (um) atleta federado por equipe.")
    st.write("O torneio mantém caráter amador e recreativo conforme item 1.5.")

with t3:
    st.header("Chaves do Torneio")
    ca, cb = st.columns(2)
    with ca:
        st.markdown('<p style="background:#004a99;color:white;text-align:center;">CHAVE A</p>', unsafe_allow_html=True)
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando Sorteio..."]*4
        for t in ta: st.info(t)
    with cb:
        st.markdown('<p style="background:#d9534f;color:white;text-align:center;">CHAVE B</p>', unsafe_allow_html=True)
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando Sorteio..."]*4
        for t in tb: st.info(t)

with t4:
    st.header("Mata-Mata (Quartas de Final)")
    st.write("1º Chave A x 4º Chave B")
    st.write("2º Chave A x 3º Chave B")
    st.write("1º Chave B x 4º Chave A")
    st.write("2º Chave B x 3º Chave A")
    

with t5:
    st.header("Premiação")
    st.write("🥇 1º, 🥈 2º e 🥉 3º: Troféus e Medalhas.")
    st.divider()
    st.write("🏅 Destaques: Levantador, Oposto, Ponteiro, Central e Líbero.")

st.caption("Org: Cristiano Delfino | Desenvolvido por Gabriel")
