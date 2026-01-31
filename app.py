import streamlit as st
import random

# 1. Configurações de Estilo
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

# CSS Minimalista para evitar erros de renderizacao
st.markdown("<style>h1{color: #FFDF00;} h3{color: #009b3a;} .stApp{background-color: #0E1117;}</style>", unsafe_allow_html=True)

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Admin
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC DE VOLEI")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("Admin")
        nome = st.text_input("Equipe:")
        if st.button("Adicionar") and nome:
            st.session_state.times.append(nome)
            st.rerun()
        if st.button("SORTEAR") and len(st.session_state.times) >= 4:
            lista = list(st.session_state.times)
            random.shuffle(lista)
            m = len(lista) // 2
            st.session_state.chaves = {"A": lista[:m], "B": lista[m:]}
            st.rerun()
        if st.button("Resetar"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Conteudo em Abas
t1, t2, t3, t4 = st.tabs(["Regulamento", "Federados", "Chaves", "Mata-Mata"])

with t1:
    st.subheader("Informacoes Gerais")
    st.write("Data: 22/02/2026 | Local: Escola Sagrado | Inicio: 08:00h")
    st.write("Inscricao: R$ 400,00 | Pix: (51) 99881-6326")
    st.divider()
    st.subheader("Regras Tecnicas")
    st.write("- Set unico de 25 pts (Classificatoria ate Semis)")
    st.write("- Final e 3 lugar: Melhor de 3 sets")
    st.write("- Ate 12 atletas por equipe | 6 substituicoes por set")
    st.write("- Aquecimento: 6 min no primeiro jogo de cada time")

with t2:
    st.subheader("Atletas Federados")
    st.error("Limite: Apenas 1 (um) atleta federado por equipe.")
    st.write("O torneio e amador e recreativo. Federado e quem tem registro ativo.")
    st.warning("O descumprimento gera desclassificacao imediata (Item 1.5).")

with t3:
    st.subheader("Chaves")
    c1, c2 = st.columns(2)
    with c1:
        st.write("GRUPO A")
