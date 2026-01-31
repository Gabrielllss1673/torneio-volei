import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

# Estilo para garantir que o texto apareça sempre
st.markdown("<style>.stApp{background-color: #ffffff;} h1,h2,h3{color: #004A99 !important;}</style>", unsafe_allow_html=True)

# Inicialização da memória (Session State)
if 'times' not in st.session_state:
    st.session_state.times = []
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

# Verificação de Admin (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"

st.title("🏐 I TORNEIO RS / SC DE VÔLEI")

# 2. Painel Administrativo
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão Cristiano")
        with st.form("add_team", clear_on_submit=True):
            equipe = st.text_input("Nome da Equipe:")
            if st.form_submit_button("Adicionar"):
                if equipe:
                    st.session_state.times.append(equipe)
                    st.rerun()
        
        st.write(f"Inscritos: {len(st.session_state.times)}")
        
        if st.button("🎲 SORTEAR CHAVES"):
            if len(st.session_state.times) >= 4:
                lista = list(st.session_state.times)
                random.shuffle(lista)
                meio = len(lista) // 2
                st.session_state.chaves = {"A": lista[:meio], "B": lista[meio:]}
                st.rerun()
        
        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# 3. Conteúdo Fixo (Não depende de sorteio)
t1, t2, t3, t4 = st.tabs(["📜 REGULAMENTO", "🚫 FEDERADOS", "📊 CHAVES", "🏆 MATA-MATA"])

with t1:
    st.subheader("📍 Regulamento Oficial")
    st.write("**Data:** 22/02/2026 | **Local:** Escola Sagrado (Torres/RS)")
    st.write("**Início:** 08:00h | **Inscrição:** R$ 400,00")
    st.divider()
    st.write("• **Sets:** Único de 25 pontos até Semifinais.")
    st.write("• **Finais:** Melhor de 3 sets (1º, 2º e 3º lugares).")
    st.write("• **Aquecimento:** 6 minutos em quadra no primeiro jogo.")
    st.write("• **Equipe:** Máximo 12 atletas e 2 tempos por set.")

with t2:
    st.subheader("⚠️ Regra de Federados")
    st.error("Limite: Apenas 1 (um) atleta federado por equipe.")
    st.write("Federado é quem tem registro ativo em federações profissionais.")

with t3:
    st.subheader("📊 Grupos do Torneio")
    if st.session_state.chaves:
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("### GRUPO A")
            for t in st.session_state.chaves["A"]: st.write(f"🏐 {t}")
        with col_b:
            st.success("### GRUPO B")
            for t in st.session_state.chaves["B"]: st.write(f"🏐 {t}")
    else:
        st.warning("As chaves aparecerão aqui após o sorteio no painel admin.")

with t4:
    st.subheader("🏆 Chaveamento Mata-Mata")
    st.code("""
    QUARTAS (25 pts)        SEMIFINAIS           FINAL (MD3)
    
    1ºA vs 4ºB (J1) --.
                      |--- Venc J1 vs Venc J4 --.
    2ºB vs 3ºA (J4) --'                         |
                                                |--- FINALÍSSIMA
    1ºB vs 4ºA (J3) --.                         |
                      |--- Venc J3 vs Venc J2 --'
    2ºA vs 3ºB (J2) --'
    """)

st.divider()
st.caption("Organização: Cristiano Delfino | Torres-RS")
