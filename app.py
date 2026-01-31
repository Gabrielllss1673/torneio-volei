import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

# Estilo para melhorar as cores
st.markdown("<style>.stApp{background-color: #Fdfdfd;} h1,h2,h3{color: #004A99;}</style>", unsafe_allow_html=True)

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Admin (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC DE VÔLEI")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("Admin")
        equipe = st.text_input("Nova Equipe:")
        if st.button("Adicionar") and equipe:
            st.session_state.times.append(equipe)
            st.rerun()
        if st.button("SORTEAR") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times)
            random.shuffle(lst)
            m = len(lst) // 2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.rerun()
        if st.button("Limpar"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas
t1, t2, t3, t4 = st.tabs(["📜 Regulamento", "🚫 Federados", "📊 Chaves", "🏆 Mata-Mata"])

with t1:
    st.subheader("Informações Gerais")
    st.write("Data: 22/02/2026 | Local: Escola Sagrado | Início: 08:00h")
    st.write("Inscrição: R$ 400,00 | Pix: (51) 99881-6326")
    st.divider()
    st.write("- Set único de 25 pts (até Semifinais).")
    st.write("- Finais e 3º lugar em Melhor de 3 sets.")
    st.write("- Aquecimento: 6 minutos em quadra por time.")

with t2:
    st.subheader("Regra de Federados")
    st.error("Limite: Apenas 1 (um) atleta federado por equipe.")
    st.write("Torneio amador/recreativo conforme item 1.5.")

with t3:
    st.header("Chaves dos Grupos")
    c1, c2 = st.columns(2)
    ch = st.session_state.chaves
    with c1:
        st.markdown("<p style='background:#004A99;color:white;text-align:center;padding:5px;border-radius:5px'>GRUPO A</p>", unsafe_allow_html=True)
        ta = ch["A"] if ch else ["Aguardando..."]*4
        for t in ta: st.info(t)
    with c2:
        st.markdown("<p style='background:#009b3a;color:white;text-align:center;padding:5px;border-radius:5px'>GRUPO B</p>", unsafe_allow_html=True)
        tb = ch["B"] if ch else ["Aguardando..."]*4
        for t in tb: st.info(t)

with t4:
    st.header("Diagrama do Mata-Mata")
    st.write("Abaixo o caminho oficial até o título:")
    
    st.code("""
    QUARTAS (25 pts)           SEMIFINAIS             FINAL (MD3)
    
    [1ºA] vs [4ºB] (J1) --.
                          |--- [Venc J1 x Venc J4] --.
    [2ºB] vs [3ºA] (J4) --'                          |
                                                     |--- [ CAMPEÃO ]
    [1ºB] vs [4ºA] (J3) --.                          |
                          |--- [Venc J3 x Venc J2] --'
    [2ºA] vs [3ºB] (J2) --'
    """)

    

st.divider()
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
