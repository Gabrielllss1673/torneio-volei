import streamlit as st
import random
import time

# 1. Configuração Inicial
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

# Inicialização de dados
if 'times' not in st.session_state:
    st.session_state.times = []
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

# 2. Sistema de Acesso Secreto (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"

# FORÇAR A BARRA LATERAL A SUMIR PARA O PÚBLICO
if not is_admin:
    st.markdown("""
        <style>
            [data-testid="stSidebar"], section[data-testid="stSidebar"] {
                display: none !important;
                width: 0px !important;
            }
        </style>
    """, unsafe_allow_html=True)

st.title("🏐 I Torneio RS/SC de Vôlei")

# 3. Painel do Organizador
if is_admin:
    with st.sidebar:
        st.header("🏁 Painel do Cristiano")
        novo_time = st.text_input("Nome do Time")
        if st.button("➕ Cadastrar Time"):
            if novo_time:
                st.session_state.times.append(novo_time)
                st.rerun()
        
        st.divider()
        if st.button("🎲 REALIZAR SORTEIO"):
            if len(st.session_state.times) >= 4:
                lista = st.session_state.times.copy()
                random.shuffle(lista)
                meio = len(lista) // 2
                st.session_state.chaves = {"A": lista[:meio], "B": lista[meio:]}
                st.snow()
                st.rerun()
        
        if st.button("🗑️ Resetar Tudo"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# 4. Conteúdo Público (Abas)
aba1, aba2, aba3 = st.tabs(["📜 Regulamento Detalhado", "📊 Grupos & Confrontos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial do Torneio")
    st.markdown("""
    ### 1. DA ORGANIZAÇÃO E OBJETIVO
    O **I Torneio RS/SC de Vôlei**, idealizado por **Cristiano Delfino**, busca integrar atletas e promover o esporte entre as regiões litorâneas dos dois estados.

    ### 2. DAS EQUIPES E INSCRIÇÕES
    * **Composição:** Mínimo de 6 e máximo de 12 atletas por equipe.
    * **Categoria Mista:** É obrigatória a manutenção de, no mínimo, 2 mulheres em quadra durante todos os ralis.
    * **Identificação:** Equipes devem, preferencialmente, utilizar uniformes de cores similares.

    ### 3. FORMATO DE DISPUTA
    * **Fase de Grupos:** As equipes serão divididas por sorteio em Grupo A e Grupo B.
    * **Partidas:** Set único de 25 pontos (com teto de 27). 
    * **Pontuação:** Vitória vale 3 pontos, derrota vale 0.
    * **Classificação:** Avançam para a semifinal os 2 melhores colocados de cada grupo.

    ### 4. CRITÉRIOS DE DESEMPATE
    1. Número de vitórias.
    2. Saldo de pontos (pontos feitos menos pontos sofridos).
    3. Confronto direto.
    4. Sorteio.

    ### 5. LOCAL E HORÁRIOS
    * **Data:** 29 de Março de 2026.
    * **Local:** Ginásio Municipal de Torres - RS.
    * **Abertura:** 07:30h para conferência de documentos.
    * **Início dos Jogos:** 08:00h pontualmente.
    """)

with aba2:
    st.header("Distribuição dos Grupos")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown('<div style="background-color:#004a99;color:white;padding:10px;border-radius:10px 10px 0 0;text-align:center;font-weight:bold;">GRUPO A</div>', unsafe_allow_html=True)
        times_a = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando Sorteio..."]*4
        for t in times_a:
            st.markdown(f'<div style="border:1px solid #ddd;padding:10px;background:white;color:black;">🏐 {t}</div>', unsafe_allow_html=
