import streamlit as st
import random
import time
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

# Inicialização
if 'times' not in st.session_state:
    st.session_state.times = []
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

st.title("🏐 I Torneio RS/SC de Vôlei")

# --- SENHA NA BARRA LATERAL ---
with st.sidebar:
    st.header("🔐 Administração")
    senha = st.text_input("Senha do Organizador", type="password")
    admin_logado = (senha == "volei123")
    
    if admin_logado:
        st.success("Acesso Liberado!")
        st.divider()
        novo_time = st.text_input("Nome do Time")
        if st.button("➕ Cadastrar"):
            if novo_time and novo_time not in st.session_state.times:
                st.session_state.times.append(novo_time)
                st.rerun()
    else:
        st.info("Visualização Pública")

# --- ABAS ---
aba1, aba2, aba3 = st.tabs(["📜 Regulamento Detalhado", "📊 Grupos & Confrontos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial")
    st.markdown("""
    ### 1. DA ORGANIZAÇÃO
    O I Torneio RS/SC de Vôlei é organizado por **Cristiano Delfino**.
    ### 2. DAS EQUIPES E ATLETAS
    * Mínimo 6 e máximo 12 atletas por equipe. Categoria Mista (mínimo 2 mulheres).
    ### 3. DO SISTEMA DE DISPUTA
    * Fase de Grupos: Set Único de 25 pontos. 2 melhores de cada grupo avançam.
    """)

with aba2:
    st.header("Distribuição dos Grupos")
    
    if admin_logado:
        if st.button("🎲 REALIZAR SORTEIO AGORA"):
            with st.spinner('Sorteando...'):
                time.sleep(2)
                lista = st.session_state.times.copy()
                random.shuffle(lista)
                meio = len(lista) // 2
                st.session_state.chaves = {"Grupo A": lista[:meio], "Grupo B": lista[meio:]}
                st.snow()
    
    if st.session_state.chaves:
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("""
                <div style="background-color: #004a99; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">
                    GRUPO A
                </div>
            """, unsafe_allow_html=True)
            for t in st.session_state.chaves["Grupo A"]:
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: white; color: black;">
                        🏐 {t}
                    </div>
                """, unsafe_allow_html=True)
            
            st.write("---")
            st.write("**🎮 Jogos do Grupo A:**")
            equipes_a = st.session_state.chaves["Grupo A"]
            for i in range(len(equipes_a)):
                for j in range(i + 1, len(equipes_a)):
                    st.code(f"{equipes_a[i]} vs {equipes_a[j]}")

        with col_b:
            st.markdown("""
                <div style="background-color: #d9534f; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">
                    GRUPO B
                </div>
            """, unsafe_allow_html=True)
            for t in st.session_state.chaves["Grupo B"]:
                st.markdown(f"""
                    <div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: white; color: black;">
                        🏐 {t}
                    </div>
                """, unsafe_allow_html=True)
            
            st.write("---")
            st.write("**🎮 Jogos do Grupo B:**")
            equipes_b = st.session_state.chaves["Grupo B"]
            for i in range(len(equipes_b)):
                for j in range(i + 1, len(equipes_b)):
                    st.code(f"{equipes_b[i]} vs {equipes_b[j]}")
    else:
        st.warning("O sorteio ainda não foi realizado.")

with aba3:
    st.header("Caminho até o Título (Mata-Mata)")
    st.markdown("""
    <div style="display: flex; justify-content: space-around; align-items: center; background-color: #f0f2f6; padding: 20px; border-radius: 10px; color: black;">
        <div style="flex: 1; text-align: center;">
            <h4 style="color: #333;">SEMIFINAIS</h4>
            <div style="border: 2px solid #004a99; padding: 10px; margin: 10px; background: white; border-radius: 5px;">1º Grupo A<br>vs<br>2º Grupo B</div>
            <div style="border: 2px solid #004a99; padding: 10px; margin: 10px; background: white; border-radius: 5px;">1º Grupo B<br>vs<br>2º Grupo A</div>
        </div>
        <div style="font-size: 40px; color: #333;">➡️</div>
        <div style="flex: 1; text-align: center;">
            <h4 style="color: #333;">FINAL</h4>
            <div style="border: 4px solid #ffd700; padding: 20px; background: white; font-weight: bold; border-radius: 10px;">🏆 VENCEDORES SEMI</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
