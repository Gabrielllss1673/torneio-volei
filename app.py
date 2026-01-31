import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC de Vôlei", page_icon="🏐", layout="wide")

# CSS para o fundo com imagem da Seleção e cores do Brasil
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
        url("https://images.unsplash.com/photo-1592656094267-764a45159577?auto=format&fit=crop&q=80&w=2000");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    /* Estilização das Abas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(0, 155, 58, 0.3); /* Verde Brasil */
        padding: 10px;
        border-radius: 15px;
        border: 1px solid #FFDF00; /* Amarelo Brasil */
    }
    /* Títulos e textos em branco para leitura */
    h1, h2, h3, p, span, label {
        color: white !important;
        font-family: 'sans-serif';
    }
    /* Estilo dos quadros de informação */
    .stInfo, .stSuccess, .stError, .stWarning {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True)

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.write("### Ouro, Prata e Bronze: A disputa começa aqui!")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão Cristiano")
        nome = st.text_input("Nome da Equipe")
        if st.button("➕ Adicionar") and nome:
            st.session_state.times.append(nome); st.rerun()
        if st.button("🎲 SORTEAR") and len(st.session_state.times) >= 4:
            lista = list(st.session_state.times); random.shuffle(lista)
            m = len(lista) // 2
            st.session_state.chaves = {"A": lista[:m], "B": lista[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Conteúdo das Abas
t1, t2, t3, t4 = st.tabs(["📜 Regulamento", "🚫 Federados", "📊 Chaves", "🏆 Mata-Mata"])

with t1:
    st.markdown("### 📋 Informações Oficiais")
    st.write("📅 **Data:** 22/02/2026 | 🏫 **Local:** Escola Sagrado | 🕗 **Início:** 08:00h")
    st.write("💰 **Inscrição:** R$ 400,00 | **Pix:** (51) 99881-6326 (Cristiano Delfino)")
    st.divider()
    st.write("• **Sets:** Único de 25 pts até Semis. Finais em Melhor de 3 Sets.")
    st.write("• **Equipe:** Até 12 atletas. 6 substituições e 2 tempos por set.")
    st.write("• **Aquecimento:** 6 min no 1º jogo (3' ponta, 2' saída, 1' saque).")
    st.write("• **Bola:** Penalty 8.0 Oficial.")

with t2:
    st.header("🛡️ Atletas Federados")
    st.warning("⚠️ LIMITE: Apenas 1 (um) atleta federado por equipe.")
    st.write("O torneio é amador. Federado é quem possui registro ativo em federações profissionais.")
    st.write("O uso de mais de 1 federado causa desclassificação imediata (Item 1.5).")

with t3:
    st.header("📊 Chaves de Classificação")
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown('<div style="background:#004a99;color:white;text-align:center;padding:10px;font-weight:bold;border-radius:10px;border:2px solid #FFDF00;">CHAVE A</div>', unsafe_allow_html=True)
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in ta: st.info(f"🏐 {t}")
    with c_b:
        st.markdown('<div style="background:#009b3a;color:white;text-align:center;padding:10px;font-weight:bold;border-radius:10px;border:2px solid #FFDF00;">CHAVE B</div>', unsafe_allow_html=True)
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in tb: st.info(f"🏐 {t}")

with t4:
    st.header("⚡ Cruzamentos Eliminatórios")
    st.subheader("Quartas de Final")
    st.write("• J1: 1ºA x 4ºB | J2: 2ºA x 3ºB")
    st.write("• J3: 1ºB x 4ºA | J4: 2ºB x 3ºA")
    st.divider()
    st.subheader
