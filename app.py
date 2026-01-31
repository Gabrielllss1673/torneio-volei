import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

# Estilo para manter o site limpo e profissional
st.markdown("<style>.stApp{background-color: #ffffff;} h1,h2,h3{color: #004A99;}</style>", unsafe_allow_html=True)

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Admin (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC DE VÔLEI")

# 2. Painel Admin
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão Cristiano")
        equipe = st.text_input("Nome da Equipe:")
        if st.button("Adicionar") and equipe:
            st.session_state.times.append(equipe)
            st.rerun()
        if st.button("SORTEAR CHAVES") and len(st.session_state.times) >= 4:
            lst = list(st.session_state.times)
            random.shuffle(lst)
            m = len(lst) // 2
            st.session_state.chaves = {"A": lst[:m], "B": lst[m:]}
            st.rerun()
        if st.button("Resetar Tudo"):
            st.session_state.times=[]; st.session_state.chaves=None; st.rerun()

# 3. Abas Detalhadas
t1, t2, t3, t4 = st.tabs(["📜 REGULAMENTO COMPLETO", "🚫 ATLETAS FEDERADOS", "📊 CHAVES", "🏆 MATA-MATA"])

with t1:
    st.subheader("📍 Disposições Gerais")
    st.write("**Data:** 22 de Fevereiro de 2026")
    st.write("**Local:** Escola Sagrado - Torres/RS")
    st.write("**Início:** 08:00h (Tolerância de 10 min apenas no primeiro jogo)")
    st.write("**Inscrição:** R$ 400,00 | **Bola Oficial:** Penalty 8.0")
    
    st.divider()
    st.subheader("⚙️ Regras Técnicas do Torneio")
    st.write("1. **Formato dos Sets:**")
    st.write("- Fase classificatória, quartas e semifinais: Set único de 25 pontos.")
    st.write("- Finais (1º, 2º e 3º lugares): Melhor de 3 sets (2 sets de 25 e tie-break de 15).")
    
    st.write("2. **Dinâmica de Jogo:**")
    st.write("- Máximo de 12 atletas por equipe.")
    st.write("- 06 substituições permitidas por set.")
    st.write("- 02 tempos técnicos de 30 segundos por set para cada equipe.")
    st.write("- O sistema de jogo e arbitragem seguirá as normas da CBV, com as adaptações deste regulamento.")
    
    st.write("3. **Aquecimento:**")
    st.write("- 06 minutos de aquecimento em quadra para a primeira partida de cada equipe.")
    st.write("- Tempo dividido em: 3 min rede (ponta), 2 min rede (saída) e 1 min saque.")
    
    st.write("4. **Uniformidade:**")
    st.write("- Equipes devem jogar com camisetas de cores iguais e numeradas.")

with t2:
    st.header("🚫 Regra de Atletas Federados")
    st.error("⚠️ LIMITE RÍGIDO: Apenas 1 (um) atleta federado por equipe.")
    st.write("**O que define um atleta federado?**")
    st.write("Todo atleta que possua registro ativo em federações profissionais no ano vigente.")
    st.info("Esta regra (Item 1.5) visa manter o equilíbrio e o caráter amador do torneio.")
    st.warning("A identificação de mais de um federado implica em desclassificação imediata.")

with t3:
    st.header("📊 Chaves do Torneio")
    st.write("Classificam-se os 4 melhores de cada grupo para as Quartas de Final.")
    c1, c2 = st.columns(2)
    ch = st.session_state.chaves
    with c1:
        st.markdown("<p style='background:#004A99;color:white;text-align:center;padding:10px;border-radius:5px'>GRUPO A</p>", unsafe_allow_html=True)
        ta = ch["A"] if ch else ["Aguardando..."]*4
        for t in ta: st.info(t)
    with c2:
        st.markdown("<p style='background:#009b3a;color:white;text-align:center;padding:10px;border-radius:5px'>GRUPO B</p>", unsafe_allow_html=True)
        tb = ch["B"] if ch else ["Aguardando..."]*4
        for t in tb: st.info(t)

with t4:
    st.header("🏆 Caminho para o Título")
    st.write("Cruzamento Olímpico conforme Item 3.3 do Regulamento:")
    
    st.code("""
    QUARTAS DE FINAL          SEMIFINAIS              FINAL (MD3)
    
    (J1) 1ºA vs 4ºB ----.
                        |--- Venc J1 vs Venc J4 ----.
    (J4) 2ºB vs 3ºA ----'                           |
                                                    |--- [ CAMPEÃO ]
    (J3) 1ºB vs 4ºA ----.                           |
                        |--- Venc J3 vs Venc J2 ----'
    (J2) 2ºA vs 3ºB ----'
    """)

    
    
    st.divider()
    st.subheader("🏅 Premiação Individual")
    st.write("Além dos troféus por equipe (1º, 2º e 3º), teremos destaques para:")
    st.write("• Melhor Levantador | Oposto | Ponteiro | Central | Líbero")

st.divider()
st.caption("Organização: Cristiano Delfino | Site Oficial do Torneio")
