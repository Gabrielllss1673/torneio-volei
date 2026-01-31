import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC de Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Administrativo (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.subheader("Torneio Aberto Masculino de Quadra")

# 2. Painel Administrativo
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão do Torneio")
        nome_equipe = st.text_input("Nome da Equipe")
        if st.button("➕ Adicionar Equipe") and nome_equipe:
            st.session_state.times.append(nome_equipe)
            st.rerun()
        st.divider()
        if st.button("🎲 REALIZAR SORTEIO") and len(st.session_state.times) >= 4:
            lista_sorteio = list(st.session_state.times)
            random.shuffle(lista_sorteio)
            meio = len(lista_sorteio) // 2
            st.session_state.chaves = {"A": lista_sorteio[:meio], "B": lista_sorteio[meio:]}
            st.snow()
            st.rerun()
        if st.button("🗑️ Limpar Todos os Dados"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# 3. Abas de Informação (Conteúdo Extraído do PDF)
aba1, aba2, aba3, aba4 = st.tabs(["📜 Regulamento", "🚫 Atletas Federados", "📊 Chaves", "🏆 Mata-Mata"])

with aba1:
    st.markdown("### 📍 Informações Gerais")
    st.info("📅 **Data:** 22 de Fevereiro de 2026 | 🏫 **Local:** Escola Sagrado (Torres/RS) | 🕗 **Início:** 08:00h")
    st.write("**• Inscrição:** R$ 400,00 | **Pix:** (51) 99881-6326 (Cristiano Delfino)")
    st.write("**• Bola Oficial:** Penalty 8.0 (Não disponibilizamos bolas para aquecimento)")
    
    st.divider()
    st.markdown("### ⚙️ Regulamento Técnico")
    st.write("**• Formato:** Set único de 25 pontos (Fase Classificatória, Quartas e Semifinais).")
    st.write("**• Finais:**
