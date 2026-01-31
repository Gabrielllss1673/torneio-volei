import streamlit as st
import random

st.set_page_config(page_title="Torneio RS/SC", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")

if is_admin:
    with st.sidebar:
        st.header("🏁 Admin")
        nt = st.text_input("Time")
        if st.button("➕ Add") and nt:
            st.session_state.times.append(nt); st.rerun()
        if st.button("🎲 SORTEAR") and len(st.session_state.times) >= 2:
            lst = list(st.session_state.times); random.shuffle(lst)
            m = len(lst)//2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.snow(); st.rerun()
        if st.button("🗑️ Reset"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

tab1, tab2, tab3 = st.tabs(["📜 Regulamento", "📊 Grupos", "🏆 Mata-Mata"])

with tab1:
    st.markdown("""
    ### Regulamento Detalhado
    **1. Organização:** Cristiano Delfino.
    **2. Local:** Torres - RS | **Data:** 29/03/2026.
    **3. Regras:** Misto (min. 2 mulheres). Set único de 25 pts.
    **4. Avançam:** Os 2 melhores de cada grupo para a semi.
    """)

with tab2:
    ca, cb = st.columns(2)
    with ca:
        st.markdown('<div style="background:#004a99;color:white;padding:5px;text-align:center;">GRUPO A</div>', unsafe_allow_html=True)
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in ta: st.info(f"🏐 {t}")
    with cb:
        st.markdown('<div style="background:#d9534f;color:white;padding:5px;text-align:center;">GRUPO B</div>', unsafe_allow_html=True)
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in tb: st.info(f"🏐 {t}")

with tab3:
    st.markdown("""
    <div style="background:#f0f2f6;padding:20px;border-radius:10px;text-align:center;color:black;">
    <h4>SEMIFINAIS</h4>
    <p>1º A vs 2º B  |  1º B vs 2º A</p>
    <hr>
    <h4>🏆 FINAL</h4>
    <p>Vencedores das Semis</p>
    </div>
    """, unsafe_allow_html=True)

st.caption("Org: Cristiano Delfino | Desenvolvido por Gabriel")
