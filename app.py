import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC", page_icon="🏐", layout="wide")

# Estilo para manter o site limpo e profissional
st.markdown("<style>.stApp{background-color: #ffffff;} h1,h2,h3{color: #004A99;}</style>", unsafe_allow_html=True)

# Inicialização do Banco de Dados Temporário
if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Admin (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC DE VÔLEI")

# 2. Painel Administrativo (BOTÃO CORRIGIDO COM FORMULÁRIO)
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão Cristiano")
        
        with st.form("add_team_form", clear_on_submit=True):
            nome_equipe = st.text_input("Nome da Equipe:")
            submit_button = st.form_submit_button("➕ Adicionar Equipe")
            
            if submit_button and nome_equipe:
                st.session_state.times.append(nome_equipe)
                st.toast(f"{nome_equipe} adicionada!")
        
        st.write(f"Equipes cadastradas: **{len(st.session_state.times)}**")
        
        st.divider()
        
        if st.button("🎲 REALIZAR SORTEIO"):
            if len(st.session_state.times) >= 4:
                lista_sorteio = list(st.session_state.times)
                random.shuffle(lista_sorteio)
                meio = len(lista_sorteio) // 2
                st.session_state.chaves = {
                    "A": lista_sorteio[:meio], 
                    "B": lista_sorteio[meio:]
                }
                st.balloons()
                st.rerun()
            else:
                st.error("Adicione pelo menos 4 equipes!")

        if st.button("🗑️ Limpar Tudo"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# 3. Abas Detalhadas
t1, t2, t3, t4 = st.tabs(["📜 REGULAMENTO", "🚫 FEDERADOS", "📊 CHAVES", "🏆 MATA-MATA"])

with t1:
    st.subheader("📍 Disposições Gerais")
    st.write("**Data:** 22 de Fevereiro de 2026 | **Local:** Escola Sagrado - Torres/RS")
    st.write("**Início:** 08:00h | **Inscrição:** R$ 400,00 | **Bola:** Penalty 8.0")
    
    st.divider()
    st.subheader("⚙️ Regras Técnicas")
    st.write("1. **Sets:** Único de 25 pts até Semis. Finais em Melhor de 3 sets.")
    st.write("2. **Dinâmica:** Máximo 12 atletas, 6 substituições e 2 tempos por set.")
    st.write("3. **Aquecimento:** 6 min (3' ponta, 2' saída, 1' saque) no primeiro jogo.")

with t2:
    st.header("🚫 Regra de Atletas Federados")
    st.error("⚠️ LIMITE: Apenas 1 (um) atleta federado por equipe.")
    st.write("Federado é quem possui registro ativo em federações profissionais (Item 1.5).")
    st.warning("O descumprimento implica em desclassificação imediata.")

with t3:
    st.header("📊 Chaves do Torneio")
    c1
