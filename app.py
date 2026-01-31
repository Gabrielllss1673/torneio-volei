import streamlit as st
import random
import time

# 1. Configuração e Estilo
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Texto do Regulamento Detalhado
TEXTO_REG = """
### 1. DA ORGANIZAÇÃO
Torneio organizado por **Cristiano Delfino** para integração RS/SC.

### 2. DAS EQUIPES
* Mínimo de 6 e máximo de 12 atletas.
* **Misto:** Pelo menos 2 mulheres em quadra.

### 3. DO FORMATO
* Set Único de 25 pontos (teto de 27).
* 2 melhores de cada grupo avançam.

### 4. CRITÉRIOS DE DESEMPATE
1º Vitórias | 2º Saldo de pontos | 3º Confronto direto.

### 5. LOCAL E HORÁRIO
* **Data:** 29 de Março de 2026.
* **Local:** Torres - RS.
* **Início:** 08:00h (Check-in 07:30h).
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
                lista = list(st.session_state.times)
                random.shuffle(lista)
                meio = len(lista)//2
                st.session_state.chaves = {"A": lista[:meio], "B": lista[meio:]}
                st.snow()
                st.rerun()
            else:
                st.error("Adicione pelo menos
