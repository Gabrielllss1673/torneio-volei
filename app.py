import streamlit as st
import random
import time

st.set_page_config(page_title="Torneio RS/SC Vôlei", layout="wide", page_icon="🏐")

# --- MEMÓRIA DO APP ---
if 'inscritos' not in st.session_state:
    st.session_state.inscritos = []
if 'chave_a' not in st.session_state:
    st.session_state.chave_a = []
if 'chave_b' not in st.session_state:
    st.session_state.chave_b = []

# --- CABEÇALHO ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🏐 I TORNEIO RS / SC DE VÔLEI</h1>", unsafe_allow_html=True)
st.write("---")

aba = st.sidebar.radio("Navegação", ["Inscrições", "Sorteio ao Vivo", "Regulamento Completo"])

if aba == "Inscrições":
    st.header("📝 Cadastro de Equipes")
    with st.form("cadastro", clear_on_submit=True):
        nome = st.text_input("Nome da Equipe:")
        if st.form_submit_button("✅ Confirmar"):
            if nome:
                st.session_state.inscritos.append(nome)
                st.toast(f"{nome} inscrito!", icon="🏐")

    st.subheader("📋 Lista de Confirmados")
    for i, t in enumerate(st.session_state.inscritos):
        c1, c2 = st.columns([5, 1])
        c1.markdown(f"**{i+1}.** {t}")
        if c2.button("🗑️", key=f"del_{i}"):
            st.session_state.inscritos.pop(i)
            st.rerun()

elif aba == "Sorteio ao Vivo":
    st.header("🎲 Sorteio de Chaves")
    if len(st.session_state.inscritos) < 2:
        st.warning("Adicione times para sortear.")
    else:
        if st.button("🔥 INICIAR SORTEIO"):
            lista = st.session_state.inscritos.copy()
            random.shuffle(lista)
            meio = len(lista) // 2
            st.session_state.chave_a = lista[:meio]
            st.session_state.chave_b = lista[meio:]
            st.balloons()
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.success("🟡 CHAVE A")
        for t in st.session_state.chave_a: st.write(f"🏐 {t}")
    with col_b:
        st.info("🔵 CHAVE B")
        for t in st.session_state.chave_b: st.write(f"🏐 {t}")

elif aba == "Regulamento Completo":
    st.header("📜 Regulamento Oficial 2026")
    
    col_reg1, col_reg2 = st.columns(2)
    
    with col_reg1:
        st.subheader("📍 Informações Gerais")
        st.write("🗓️ **Data:** 29 de Março de 2026")
        st.write("⏰ **Início:** 08:30h")
        st.write("📍 **Local:** Escola Sagrado - Torres/RS")
        st.write("💰 **Inscrição:** R$ 400,00 por equipe")
        st.write("📞 **Organização:** Cristiano Delfino")
        
    with col_reg2:
        st.subheader("🏐 Formato da Competição")
        st.markdown("""
        * **Equipes:** Máximo de 12 atletas inscritos.
        * **Chaves:** 2 Grupos (A e B) sorteados ao vivo.
        * **Classificação:** Os 4 melhores de cada chave avançam.
        * **Bola Oficial:** Penalty 8.0.
        """)

    st.write("---")
    st.subheader("⏱️ Regras de Jogo (Sets e Pontuação)")
    
    # Criando uma tabela para ficar bem visual
    dados_regras = {
        "Fase": ["Classificatória", "Quartas de Final", "Semifinais", "Grande Final"],
        "Formato": ["Set Único", "Set Único", "Set Único", "Melhor de 3 Sets"],
        "Pontuação": ["25 pontos", "25 pontos", "25 pontos", "21/21/15 pontos"],
        "Observação": ["Mínimo 2 pts de diferença", "Mínimo 2 pts de diferença", "Mínimo 2 pts de diferença", "Tie-break se necessário"]
    }
    st.table(dados_regras)

    with st.expander("🔍 Detalhes sobre Substituições e Líbero"):
        st.write("""
        * **Substituições:** Até 6 substituições por set.
        * **Líbero:** Cada equipe pode atuar com até 2 líberos inscritos.
        * **Atrasos:** Tolerância de 15 minutos apenas para o primeiro jogo do dia.
        * **Uniformes:** Equipes devem estar devidamente uniformizadas e numeradas.
        """)

st.sidebar.markdown("---")
st.sidebar.caption("🚀 I Torneio RS/SC de Vôlei")