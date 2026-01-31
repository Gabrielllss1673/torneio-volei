import streamlit as st
import random
import time

# 1. Configuração e Estilo
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Texto do Regulamento (Separado para não quebrar o código)
TEXTO_REGULAMENTO = """
### 1. DA ORGANIZAÇÃO
O **I Torneio RS/SC de Vôlei** é organizado por **Cristiano Delfino**, visando integrar atletas do RS e SC.

### 2. DAS EQUIPES E ATLETAS
* **Misto:** Mínimo de 2 mulheres em quadra o tempo todo.
* **Inscritos:** Mínimo 6 e máximo 12 atletas por equipe.

### 3. DO FORMATO DE DISPUTA
* **Fase de Grupos:** Set Único de 25 pontos (máximo 27).
* **Classificação:** Os 2 melhores de cada grupo avançam.

### 4. CRITÉRIOS DE DESEMPATE
1. Vitórias | 2. Saldo de pontos | 3. Confronto direto.

### 5. LOCAL E HORÁRIO
* **Data:** 29 de Março de 2026.
* **Local:** Ginásio Municipal de Torres - RS.
* **Início:** 08:00h pontualmente (Check-in 07:30h).
"""

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
                random.shuffle(
