import streamlit as st
import random

# 1. Configurações Iniciais conforme o PDF
st.set_page_config(page_title="I Torneio RS/SC de Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")
st.subheader("Unindo estados, celebrando o vôlei")

# 2. Painel Administrativo
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

# 3. Abas com Informações do PDF
t1, t2, t3, t4, t5 = st.tabs(["📜 Regulamento", "🚫 Atletas Federados", "📊 Chaves", "🏆 Mata-Mata", "🎁 Premiação"])

with t1:
    st.header("Informações Gerais")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Data:** 22 de fevereiro de 2026")
        st.info(f"**Local:** Escola Sagrado")
        st.write("**Endereço:** Rua Júlio de Castilhos, 875, Centro, Torres - RS")
    with col2:
        st.success("**Início:** 08h (Tolerância de 10 min na 1ª partida)")
        st.success("**Bola Oficial:** Penalty 8.0")
        st.write("**Inscrição:** R$ 400,00 por equipe")

    st.divider()
    st.header("Regulamento Técnico")
    st.markdown("""
    * **Equipes:** Até 12 atletas incluindo o líbero.
    * **Fases Iniciais:** Jogos em Set Único de 25 pontos (com 2 de diferença).
    * **Final:** Melhor de 3 sets.
    * **Substituições:** 6 por set.
    * **Tempos:** Dois tempos técnicos por set.
    * **Aquecimento:** 6 minutos na primeira partida de cada equipe.
    """)

with t2:
    st.header("Regra para Federados")
    st.warning("**Atenção:** Competição de caráter amador.")
    st.markdown("""
    * Atletas federados são bem-vindos.
    * **Limite:** Apenas **1 (um) atleta federado** por equipe.
    * O caráter recreativo deve ser respeitado.
    """)

with t3:
    st.header("Fase de Classificação")
    st.write("Classificam-se os 4 melhores de cada chave.")
    ca, cb = st.columns(2)
    with ca:
        st.markdown('<div style="background:#004a99;color:white;padding:5px;text-align:center;font-weight:bold;">CHAVE A</div>', unsafe_allow_html=True)
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in ta: st.info(f"🏐 {t}")
    with cb:
        st.markdown('<div style="background:#d9534f;color:white;padding:5px;text-align:center;font-weight:bold;">CHAVE B</div>', unsafe_allow_html=True)
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in tb: st.info(f"🏐 {t}")
    
    st.subheader("Critérios de Desempate")
    st.write("1. Confronto Direto (entre duas equipes)")
    st.write("2. Sets Average | 3. Pontos Average | 4. Saldo de Pontos (entre 3 ou mais)")

with t4:
    st.header("Fase Eliminatória")
    st.markdown("""
    **Quartas de Finais:**
    * Jogo 1: 1º Grupo A x 4º Grupo B
    * Jogo 2: 2º Grupo A x 3º Grupo B
    * Jogo 3: 1º Grupo B x 4º Grupo A
    * Jogo 4: 2º Grupo B x 3º Grupo A
    
    **Semifinais:**
    * Venc. Jogo 1 x Venc. Jogo 4
    * Venc. Jogo 2 x Venc. Jogo 3
    
    **Finais:**
    * Disputa de 3º lugar (perdedores das semis)
    * Grande Final (vencedores das semis)
    """)

with t5:
    st.header("Premiação")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Equipes")
        st.write("
