import streamlit as st
import random

# 1. Configurações de Estilo Profissional
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

# Estilo para deixar o site bonito e legível
st.markdown("<style>.stApp{background-color: #F8F9FA;} h1,h2,h3{color: #004A99;}</style>", unsafe_allow_html=True)

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Admin (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC DE VÔLEI")
st.write("Torneio Aberto Masculino | Torres - RS")

# 2. Painel Administrativo
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão")
        equipe = st.text_input("Nome da Equipe:")
        if st.button("Adicionar") and equipe:
            st.session_state.times.append(equipe)
            st.rerun()
        if st.button("SORTEAR CHAVES") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times)
            random.shuffle(lst)
            m = len(lst) // 2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.rerun()
        if st.button("Limpar Tudo"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# 3. Abas com Informações do PDF
t1, t2, t3, t4 = st.tabs(["📜 REGULAMENTO", "🚫 FEDERADOS", "📊 CHAVES", "🏆 MATA-MATA"])

with t1:
    st.subheader("📍 Informações Gerais")
    st.write("**Data:** 22/02/2026 | **Local:** Escola Sagrado | **Início:** 08:00h")
    st.write("**Inscrição:** R$ 400,00 | **Pix:** (51) 99881-6326")
    st.divider()
    st.subheader("⚙️ Regras Técnicas")
    st.write("- Fase Classificatória até Semifinais: Set único de 25 pontos.")
    st.write("- Finais (1º, 2º e 3º lugares): Melhor de 3 sets.")
    st.write("- Aquecimento: 6 min na primeira partida (3' ponta, 2' saída, 1' saque).")
    st.write("- Máximo de 12 atletas por equipe.")

with t2:
    st.header("🚫 Regra de Federados")
    st.error("LIMITE: Máximo de 1 (um) atleta federado por equipe.")
    st.write("O torneio é amador. Federado é o atleta com registro ativo em federações.")
    st.warning("O descumprimento causa desclassificação imediata (Item 1.5).")

with t3:
    st.header("📊 Chaves")
    c1, c2 = st.columns(2)
    ch = st.session_state.chaves
    with c1:
        st.markdown("**GRUPO A**")
        ta = ch["A"] if ch else []
        for t in ta: st.info(t)
    with c2:
        st.markdown("**GRUPO B**")
        tb = ch["B"] if ch else []
        for t in tb: st.info(t)

with t4:
    st.header("🏆 Fase Eliminatória")
    st.subheader("Quartas de Final")
    st.write("J1: 1A x 4B | J2: 2A x 3B | J3: 1B x 4A | J4: 2B x 3A")
    st.divider()
    st.subheader("Semifinais e Final")
    st.write("Venc. J1 x Venc. J4 | Venc. J2 x Venc. J3")
    st.success("Final e 3º lugar em Melhor de 3 Sets")

st.divider()
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
