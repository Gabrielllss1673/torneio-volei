import streamlit as st
import random

st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")

if is_admin:
    with st.sidebar:
        st.header("🏁 Admin")
        nt = st.text_input("Nome do Time")
        if st.button("➕ Adicionar") and nt:
            st.session_state.times.append(nt); st.rerun()
        st.divider()
        if st.button("🎲 SORTEAR") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times); random.shuffle(lst)
            m = len(lst)//2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Reset"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas de Conteúdo (Adicionada aba Federados)
t1, t2, t3, t4, t5 = st.tabs(["📜 Regulamento", "🚫 Federados", "❓ Dúvidas", "📊 Grupos", "🏆 Mata-Mata"])

with t1:
    st.header("Regulamento Oficial")
    st.markdown("""
    **Organização:** Cristiano Delfino | **Local:** Torres - RS.
    * **Misto:** Mínimo de 2 mulheres em quadra.
    * **Jogos:** Set Único de 25 pontos (teto de 27).
    * **Início:** 08:00h pontualmente.
    """)

with t2:
    st.header("Regras para Atletas Federados")
    st.warning("Para garantir o nível amador do torneio, aplicam-se as seguintes regras:")
    st.markdown("""
    * **Definição:** Considera-se 'Federado' o atleta que disputou campeonatos oficiais por federações estaduais nos últimos 2 anos.
    * **Limite por Equipe:** Cada equipe poderá ter no máximo **2 atletas federados** inscritos.
    * **Em Quadra:** Apenas **1 atleta federado** pode estar em quadra por vez (não podem jogar dois federados juntos).
    * **Penalidade:** O uso de atletas federados acima do limite resultará em desclassificação imediata da equipe.
    """)
    st.info("Caso haja dúvida sobre a condição de um atleta, a organização deve ser consultada antes do início do torneio.")

with t3:
    st.header("Dúvidas Frequentes")
    with st.expander("Pode jogar com mais de 2 mulheres?"):
        st.write("Sim! O mínimo é 2, mas pode jogar com 3, 4 ou mais.")
    with st.expander("O que acontece em caso de atraso?"):
        st.write("Tolerância de 10 minutos apenas no primeiro jogo. Depois é W.O.")
    with st.expander("Substituição de atletas?"):
        st.write("Somente atletas que assinaram a súmula no início do dia podem participar.")

with t4:
    st.header("Distribuição dos Grupos")
    ca, cb = st.columns(2)
    with ca:
        st.markdown('<div style="background:#004a99;color:white;padding:5px;text-align:center;font-weight:bold;">GRUPO A</div>', unsafe_allow_html=True)
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in ta: st.info(f"🏐 {t}")
    with cb:
        st.markdown('<div style="background:#d9534f;color:white;padding:5px;text-align:center;font-weight:bold;">GRUPO B</div>', unsafe_allow_html=True)
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in tb: st.info(f"🏐 {t}")

with t5:
    st.header("Chaveamento Mata-Mata")
    st.markdown("""
    <div style="background:#f0f2f6;padding:20px;border-radius:10px;text-align:center;color:black;">
    <h4>SEMIFINAIS</h4>
    <p>1º A vs 2º B  |  1º B vs 2º A</p>
    <hr>
    <h4>🏆 FINAL</h4>
    <p>Vencedores das Semis</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Org: Cristiano Delfino | Desenvolvido por Gabriel")
