import streamlit as st
import random
import time

# Configuração da página
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

# Inicialização do banco de dados temporário
if 'times' not in st.session_state:
    st.session_state.times = ["Time A", "Time B", "Time C", "Time D", "Time E", "Time F", "Time G", "Time H"]
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

# Título e Cabeçalho
st.title("🏐 I Torneio RS/SC de Vôlei")

# --- SENHA NA BARRA LATERAL ---
with st.sidebar:
    st.header("🔐 Admin")
    senha = st.text_input("Senha para editar", type="password")
    admin_logado = (senha == "volei123")
    
    if admin_logado:
        st.success("Modo Edição Ativo")
        novo_time = st.text_input("Nome do Time")
        if st.button("➕ Cadastrar"):
            st.session_state.times.append(novo_time)
            st.rerun()
    else:
        st.info("Visualização Pública")

# --- CRIAÇÃO DAS ABAS ---
aba1, aba2, aba3 = st.tabs(["📜 Regulamento", "🎲 Sorteio & Grupos", "🏆 Mata-Mata"])

with aba1:
    st.header("Informações Gerais")
    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.markdown(f"""
        **📅 Data:** 29 de Março de 2026  
        **📍 Local:** Ginásio Municipal de Torres - RS  
        **⏰ Início:** 08:00h
        """)
    with col_inf2:
        st.markdown("""
        **🏐 Modalidade:** Vôlei Misto  
        **🏆 Premiação:** Troféu + Medalhas
        """)
    
    st.divider()
    st.header("📋 Regulamento Resumido")
    st.write("""
    1. Cada equipe deve ter no mínimo 6 jogadores em quadra.
    2. Partidas da primeira fase: Set único de 25 pontos.
    3. Semifinais e Final: Melhor de 3 sets (25, 25, tie-break 15).
    4. Tolerância de atraso: 10 minutos.
    """)

with aba2:
    st.header("Chaveamento da Primeira Fase")
    
    if admin_logado:
        if st.button("🎲 REALIZAR SORTEIO AGORA"):
            with st.spinner('Sorteando...'):
                time.sleep(2)
                lista = st.session_state.times.copy()
                random.shuffle(lista)
                metade = len(lista) // 2
                st.session_state.chaves = {"Grupo A": lista[:metade], "Grupo B": lista[metade:]}
                st.snow()
    
    if st.session_state.chaves:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("🔥 Grupo A")
            for t in st.session_state.chaves["Grupo A"]:
                st.info(f"🏐 {t}")
        with c2:
            st.subheader("🔥 Grupo B")
            for t in st.session_state.chaves["Grupo B"]:
                st.info(f"🏐 {t}")
    else:
        st.warning("As chaves ainda não foram sorteadas pelo organizador.")

with aba3:
    st.header("Fase Final (Mata-Mata)")
    if st.session_state.chaves:
        st.write("O cruzamento será entre os melhores de cada grupo.")
        
        # Desenho visual do Mata-Mata
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.subheader("Semifinais")
            st.code(f"1º Grupo A  vs  2º Grupo B")
            st.code(f"1º Grupo B  vs  2º Grupo A")
        
        with col_m2:
            st.subheader("Final")
            st.code("Vencedor Semi 1\n      vs\nVencedor Semi 2")
            
        with col_m3:
            st.subheader("🏆 Campeão")
            st.write("❓ Aguardando jogos...")
    else:
        st.info("O mata-mata será liberado após a definição dos grupos.")

st.markdown("---")
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
