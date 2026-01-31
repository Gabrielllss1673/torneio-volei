import streamlit as st
import random

# 1. Configurações e Estilo Visual
st.set_page_config(page_title="I Torneio RS/SC de Vôlei", page_icon="🏐", layout="wide")

# CSS para colocar imagem de fundo e melhorar o visual
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
        url("https://images.unsplash.com/photo-1592656094267-764a45159577?q=80&w=2070&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
    }
    h1, h2, h3, p, span, label {
        color: white !important;
    }
    .stMarkdown div p {
        font-size: 1.1rem;
    }
    .st-expanderHeader {
        background-color: rgba(255, 255, 255, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.subheader("Unindo estados, celebrando o vôlei!")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão")
        nome_equipe = st.text_input("Nome da Equipe")
        if st.button("➕ Adicionar") and nome_equipe:
            st.session_state.times.append(nome_equipe); st.rerun()
        if st.button("🎲 SORTEAR") and len(st.session_state.times) >= 4:
            lista = list(st.session_state.times); random.shuffle(lista)
            m = len(lista) // 2
            st.session_state.chaves = {"A": lista[:m], "B": lista[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times = []; st.session_state.chaves = None; st.rerun()

# 3. Conteúdo das Abas
aba1, aba2, aba3, aba4 = st.tabs(["📜 Regulamento", "🚫 Federados", "📊 Chaves", "🏆 Mata-Mata"])

with aba1:
    st.markdown("### 📍 Informações Gerais")
    st.info("📅 Data: 22/02/2026 | 🏫 Escola Sagrado (Torres/RS) | 🕗 Início: 08:00h")
    st.write("• **Inscrição:** R$ 400,00 | **Pix:** (51) 99881-6326 (Cristiano)")
    st.write("• **Sets:** Único de 25 pts até Semis. Finais em Melhor de 3 Sets.")
    st.write("• **Equipes:** Até 12 atletas. 6 substituições e 2 tempos por set.")
    st.write("• **Aquecimento:** 6 min no primeiro jogo (3' ponta, 2' saída, 1' saque).")

with aba2:
    st.header("Regras para Federados")
    st.error("LIMITE: Apenas 1 (um) atleta federado por equipe.")
    st.write("O torneio possui caráter amador e recreativo conforme item 1.5.")
    st.write("Federado é quem possui registro ativo em federações profissionais.")

with aba3:
    st.header("Chaves de Classificação")
    st.write("Classificam-se os 4 melhores de cada chave.")
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown('<div style="background:#004a99;color:white;text-align:center;padding:10px;font-weight:bold;border-radius:5px;">CHAVE A</div>', unsafe_allow_html=True)
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in ta: st.info(f"🏐 {t}")
    with c_b:
        st.markdown('<div style="background:#d9534f;color:white;text-align:center;padding:10px;font-weight:bold;border-radius:5px;">CHAVE B</div>', unsafe_allow_html=True)
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in tb: st.info(f"🏐 {t}")

with aba4:
    st.header("Fase Eliminatória")
    st.subheader("1. Quartas de Final")
    st.write("• Jogo 1: 1ºA x 4ºB | Jogo 2: 2ºA x 3ºB")
    st.write("• Jogo 3: 1ºB x 4ºA | Jogo 4: 2ºB x 3ºA")
    st.divider()
    st.subheader("2. Semifinais e Final")
    st.write("• Venc. J1 x Venc. J4 | Venc. J2 x Venc. J3")
    st.success("🏆 Final e 3º Lugar em Melhor de 3 Sets")

st.divider()
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
