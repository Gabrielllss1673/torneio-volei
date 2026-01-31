import streamlit as st
import random

# 1. Configuracoes Iniciais
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Secreto (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("I TORNEIO RS / SC de VOLEI")
st.subheader("Torneio Aberto Masculino de Quadra")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("Admin")
        nt = st.text_input("Nome da Equipe")
        if st.button("Adicionar") and nt:
            st.session_state.times.append(nt); st.rerun()
        if st.button("SORTEAR") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times); random.shuffle(lst)
            m = len(lst)//2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.snow(); st.rerun()
        if st.button("Reset"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas de Conteudo
t1, t2, t3, t4 = st.tabs(["Regulamento", "Atletas Federados", "Chaves", "Mata-Mata"])

with t1:
    st.markdown("### Informacoes Gerais")
    st.write("Data: 22/02/2026 | Local: Escola Sagrado (Torres/RS) | Inicio: 08:00h")
    st.write("Inscricao: R$ 400,00 | Pix: (51) 99881-6326 (Cristiano)")
    st.divider()
    st.markdown("### Regulamento Tecnico")
    st.write("- Fase Classificatoria, Quartas e Semis: Set unico de 25 pontos.")
    st.write("- Finais (1, 2 e 3 lugar): Melhor de 3 sets.")
    st.write("- Ate 12 atletas por equipe | 6 substituicoes por set.")
    st.write("- 2 tempos tecnicos por set | Aquecimento de 6 min no 1 jogo.")
    st.write("- Arbitragem decidira sobre pausa para almoco no dia.")

with t2:
    st.header("Regras para Federados")
    st.error("LIMITE: Apenas 1 (um) atleta federado por equipe.")
    st.write("O torneio e amador. Federado e quem possui registro ativo em federacoes.")
    st.warning("O descumprimento causa desclassificacao imediata (Item 1.5).")

with t3:
    st.header("Chaves de Classificacao")
    st.write("Os 4 melhores de cada chave avancam para as Quartas.")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("CHAVE A")
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in ta: st.info(t)
    with c2:
        st.markdown("CHAVE B")
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando..."]*4
        for t in tb: st.info(t)

with t4:
    st.header("Caminho ate a Final")
    st.subheader("QUARTAS DE FINAL")
    st.write("Jogo 1: 1A x 4B | Jogo 2: 2A x 3B")
    st.write("Jogo 3: 1B x 4A | Jogo 4: 2B x 3A")
    st.divider()
    st.subheader("SEMIFINAIS")
    st.write("Venc J1 x Venc J4 | Venc J2 x Venc J3")
    st.divider()
    st.subheader("FINAIS (Melhor de 3)")
    st.success("GRANDE FINAL: Vencedores das Semis")
    st.info("DISPUTA 3 LUGAR: Perdedores das Semis")

st.divider()
st.caption("Organizacao: Cristiano Delfino | Desenvolvido por Gabriel")
