import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")

# 2. Painel Administrativo
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

# 3. Abas de Conteúdo
t1, t2, t3, t4 = st.tabs(["📜 Regulamento", "❓ Dúvidas (FAQ)", "📊 Grupos", "🏆 Mata-Mata"])

with t1:
    st.header("Regulamento Oficial")
    st.markdown("""
    **1. ORGANIZAÇÃO** Organizado por **Cristiano Delfino** para integração entre RS e SC.
    
    **2. EQUIPES E ATLETAS** * Mínimo 6 e máximo 12 atletas por equipe.
    * **Misto:** Obrigatório mínimo de 2 mulheres em quadra.
    
    **3. FORMATO DE JOGO** * Set Único de 25 pontos (com teto de 27).
    * Vitória: 3 pts | Derrota: 0 pts.
    * Avançam os 2 melhores de cada grupo.
    
    **4. DATA E LOCAL** * **Data:** 29 de Março de 2026.
    * **Local:** Ginásio Municipal de Torres - RS.
    * **Início:** 08:00h (Check-in às 07:30h).
    """)

with t2:
    st.header("Dúvidas Frequentes")
    with st.expander("Pode jogar com mais de 2 mulheres?"):
        st.write("Sim! O regulamento exige o *mínimo* de 2. O time pode ser todo feminino se desejarem.")
    with st.expander("O que acontece em caso de atraso?"):
        st.write("Tolerância de 10 minutos apenas para o primeiro jogo. Atrasos maiores resultam em W.O. (25x0).")
    with st.expander("Como funciona o desempate no grupo?"):
        st.write("1º Vitórias, 2º Saldo de Pontos, 3º Confronto Direto, 4º Sorteio.")
    with st.expander("Pode trocar jogador durante o dia?"):
        st.write("Não. Apenas atletas que assinaram a súmula no início do torneio podem jogar.")

with t3:
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

with t4:
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
