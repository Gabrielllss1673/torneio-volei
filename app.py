import streamlit as st
import random
import time

# 1. Configuração e Estilo
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Esconder barra lateral para o público
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar'] {display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")

# 2. Painel Administrativo
if is_admin:
    with st.sidebar:
        st.header("🏁 Painel do Cristiano")
        nt = st.text_input("Nome do Novo Time")
        if st.button("➕ Adicionar Time") and nt:
            st.session_state.times.append(nt)
            st.rerun()
        st.divider()
        if st.button("🎲 REALIZAR SORTEIO"):
            if len(st.session_state.times) >= 4:
                lista = st.session_state.times.copy()
                random.shuffle(lista)
                m = len(lista)//2
                st.session_state.chaves = {"A": lista[:m], "B": lista[m:]}
                st.snow()
                st.rerun()
            else:
                st.error("Adicione pelo menos 4 times!")
        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times = []; st.session_state.chaves = None; st.rerun()

# 3. Conteúdo das Abas
aba1, aba2, aba3 = st.tabs(["📜 Regulamento Detalhado", "📊 Grupos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial do Torneio")
    st.markdown("""
    ### 1. DA ORGANIZAÇÃO
    O **I Torneio RS/SC de Vôlei** é organizado por **Cristiano Delfino**, com o objetivo de promover a integração esportiva entre atletas dos estados do Rio Grande do Sul e Santa Catarina.
    
    ### 2. DAS EQUIPES E ATLETAS
    * **Composição:** Mínimo de 6 e máximo de 12 atletas inscritos por equipe.
    * **Categoria Mista:** É obrigatória a presença de, no mínimo, 2 mulheres em quadra durante todo o tempo de jogo.
    * **Uniformes:** Recomenda-se o uso de camisetas de cores idênticas ou similares para identificação.
    
    ### 3. DO FORMATO DE DISPUTA
    * **Fase de Grupos:** As equipes serão divididas em Grupo A e Grupo B. Jogam todos contra todos dentro do grupo.
    * **Partidas:** Realizadas em **Set Único de 25 pontos** (com vantagem mínima de 2 pontos, teto de 27).
    * **Classificação:** Os 2 melhores colocados de cada grupo avançam para as Semifinais.
    
    ### 4. CRITÉRIOS DE DESEMPATE
    1. Maior número de vitórias.
    2. Melhor saldo de pontos (pontos pró menos pontos contra).
    3. Confronto direto (em caso de empate entre duas equipes).
    4. Sorteio.
    
    ### 5. LOCAL E HORÁRIOS
    * **Data:** 29 de Março de 2026.
    * **Local:** Ginásio Municipal de Torres - RS.
    * **Check-in:** 07:30h (conferência de súmulas).
    * **Início dos Jogos:** 08:00h pontualmente. Atrasos superiores a 10 minutos resultarão em W.O.
    """)

with aba2:
    st.header("Distribuição dos Grupos")
    ca, cb = st.columns(2)
    with ca:
        st.markdown('<div style="background:#004a99;color:white;padding:10px;text-align:center;font-weight:bold;border-radius:5px 5px 0 0;">GRUPO A</div>', unsafe_allow_html=True)
        ta = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando Sorteio..."]*4
        for t in ta:
            st.markdown(f'<div style="border:1px solid #ddd;padding:10px;background:white;color:black;border-top:none;">🏐 {t}</div>', unsafe_allow_html=True)
    with cb:
        st.markdown('<div style="background:#d9534f;color:white;padding:10px;text-align:center;font-weight:bold;border-radius:5px 5px 0 0;">GRUPO B</div>', unsafe_allow_html=True)
        tb = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando Sorteio..."]*4
        for t in tb:
            st.markdown(f'<div style="border:1px solid #ddd;padding:10px;background:white;color:black;border-top:none;">🏐 {t}</div>', unsafe_allow_html=True)

with aba3:
    st.header("Chaveamento Final")
    st.markdown("""
    <div style="display:flex;justify-content:space-around;align-items:center;background:#f0f2f6;padding:20px;border-radius:10px;color:black;">
        <div style="text-align:center;"><b>SEMIFINAIS</b>
            <div style="border:1px solid #004a99;padding:10px;margin:5px;background:white;border-radius:5px;">1º Grupo A vs 2º Grupo B</div>
            <div style="border:1px solid #004a99;padding:10px;margin:5px;background:white;border-radius:5px;">1º Grupo B vs 2º Grupo A</div>
        </div>
        <div style="font-size:30px;">➡️</div>
        <div style="text-align:center;"><b>FINAL</b>
            <div style="border:3px solid #ffd700;padding:15px
