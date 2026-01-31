import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.subheader("Unindo estados, celebrando o vôlei!")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão Cristiano")
        nt = st.text_input("Nome da Equipe")
        if st.button("➕ Adicionar Equipe") and nt:
            st.session_state.times.append(nt); st.rerun()
        st.divider()
        if st.button("🎲 SORTEAR CHAVES") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times); random.shuffle(lst)
            m = len(lst)//2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Resetar Dados"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas de Conteúdo
t1, t2, t3, t4 = st.tabs(["📜 Regulamento Completo", "🚫 Atletas Federados", "📊 Chaves", "🏆 Caminho da Glória"])

with t1:
    st.markdown("### 📋 Regulamento Técnico Oficial")
    c1, c2 = st.columns(2)
    with c1:
        st.info("📅 **DATA:** 22/02/2026\n\n🏫 **LOCAL:** Escola Sagrado\n\n🕗 **INÍCIO:** 08:00h")
    with c2:
        st.success("💰 **VALOR:** R$ 400,00\n\n🏐 **BOLA:** Penalty 8.0\n\n📝 **EQUIPES:** Até 12 atletas")
    
    st.markdown("---")
    st.write("**• Formato:** Set único de 25 pts (Classificatória até Semis).")
    st.write("**• Finais:** Melhor de 3 sets (Disputas de 1º, 2º e 3º).")
    st.write("**• Substituições:** 6 por set | **Tempos:** 2 tempos por set.")
    st.write("**• Aquecimento:** 6 min na 1ª partida de cada time (3' ponta, 2' saída, 1' saque).")
    st.write("**• Premiação:** Troféus e medalhas (1º ao 3º) + Destaques Individuais por posição.")

with t2:
    st.header("🛡️ Regra de Atletas Federados")
    st.warning("O torneio é amador e preza pelo equilíbrio técnico.")
    st.error("⚠️ LIMITE: Apenas 1 (um) atleta federado por equipe.")
    st.markdown("""
    * **Definição:** Atleta com registro ativo em federações profissionais.
    * **P
