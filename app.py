import streamlit as st
import random

# 1. Configurações e Estilo
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

st.markdown("<style>.stApp{background-color: #ffffff;} h1,h2,h3{color: #004A99;}</style>", unsafe_allow_html=True)

# Inicialização segura das variáveis
if 'times' not in st.session_state:
    st.session_state.times = []
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

# Acesso Admin
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC DE VÔLEI")

# 2. Painel Administrativo
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão")
        with st.form("form_add", clear_on_submit=True):
            equipe = st.text_input("Nome da Equipe:")
            if st.form_submit_button("➕ Adicionar"):
                if equipe:
                    st.session_state.times.append(equipe)
                    st.rerun()
        
        st.write(f"Inscritos: {len(st.session_state.times)}")
        
        if st.button("🎲 SORTEAR AGORA"):
            if len(st.session_state.times) >= 4:
                lista = list(st.session_state.times)
                random.shuffle(lista)
                m = len(lista) // 2
                st.session_state.chaves = {"A": lista[:m], "B": lista[m:]}
                st.rerun()
            else:
                st.error("Mínimo de 4 equipes!")

        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# 3. Abas
t1, t2, t3, t4 = st.tabs(["📜 REGULAMENTO", "🚫 FEDERADOS", "📊 CHAVES", "🏆 MATA-MATA"])

with t1:
    st.subheader("📍 Informações Gerais")
    st.write("**Data:** 22/02/2026 | **Escola Sagrado**")
    st.write("**Inscrição:** R$ 400,00 | **Início:** 08:00h")
    st.divider()
    st.write("- Set único de 25 pts (Classificatória e Semis).")
    st.write("- Finais (1º e 3º): Melhor de 3 sets.")
    st.write("- Aquecimento: 6 min no primeiro jogo de cada equipe.")

with t2:
    st.subheader("Regra de Federados")
    st.error("Limite: Apenas 1 (um) atleta federado por equipe.")
    st.write("O descumprimento gera desclassificação imediata.")

with t3:
    st.subheader("Distribuição dos Grupos")
    if st.session_state.chaves:
        st.markdown("### 🔹 GRUPO A")
        for t in st.session_state.chaves["A"]:
            st.info(t)
        
        st.divider()
        
        st.markdown("### 🔸 GRUPO B")
        for t in st.session_state.chaves["B"]:
            st.success(t)
    else:
        st.info("Aguardando o sorteio das equipes...")

with t4:
    st.subheader("Fase Eliminatória")
    st.code("""
    QUARTAS DE FINAL          SEMIFINAIS              FINAL (MD3)
    
    (J1) 1ºA vs 4ºB ----.
                        |--- Venc J1 vs Venc J4 ----.
    (J4) 2ºB vs 3ºA ----'                           |
                                                    |--- [ CAMPEÃO ]
    (J3) 1ºB vs 4ºA ----.                           |
                        |--- Venc J3 vs Venc J2 ----'
    (J2) 2ºA vs 3ºB ----'
    """)
    

st.divider()
st.caption("Organização: Cristiano Delfino | Site Oficial")
