import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC de Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.subheader("Unindo estados, celebrando o vôlei!")

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

# 3. Abas Detalhadas
t1, t2, t3, t4, t5 = st.tabs(["📜 Regulamento Completo", "🚫 Atletas Federados", "📊 Chaves", "🏆 Caminho da Glória", "🎁 Premiação VIP"])

with t1:
    st.markdown("### 📋 Regulamento Técnico Oficial")
    col1, col2 = st.columns(2)
    with col1:
        st.info("📅 **DATA:** 22 de fevereiro de 2026\n\n🏫 **LOCAL:** Escola Sagrado (Torres/RS)\n\n🕗 **INÍCIO:** 08:00h (Tolerância 10 min na 1ª partida)")
    with col2:
        st.success("💰 **INSCRIÇÃO:** R$ 400,00 (PIX: 51 99881-6326)\n\n🏐 **BOLA:** Penalty 8.0\n\n📝 **EQUIPES:** Até 12 atletas (inc. Líbero)")

    st.markdown("""
    **1. Formato das Partidas:**
    * Fase Classificatória, Quartas e Semis: **Set Único de 25 pontos**.
    * Grande Final e 3º Lugar: **Melhor de 3 Sets**.
    
    **2. Dinâmica de Jogo:**
    * Regras oficiais da CBV com adaptações.
    * 6 substituições por set e 2 tempos técnicos por set.
    * Aquecimento: 6 minutos em quadra para o primeiro jogo de cada time.
    * Início com 6 atletas em quadra (sistema 3x3 ou 6x0 conforme nível).
    """)

with t2:
    st.header("🛡️ Política de Atletas Federados")
    st.warning("O I Torneio RS/SC preza pelo equilíbrio técnico e o espírito recreativo.")
    st.markdown("""
    **Conforme o item 1.5 do regulamento:**
    * **O que é federado?** Atleta com registro ativo em federações profissionais.
    * **Limite:** É permitido apenas **1 (um) atleta federado** por equipe.
    * **Objetivo:** Garantir que o torneio continue sendo uma celebração amadora, onde todos tenham chances reais de disputa.
    * **Fiscalização:** A escalação de mais de um federado implica em desclassificação imediata.
    """)

with t3:
    st.header("📊 Chaves de Classificação")
