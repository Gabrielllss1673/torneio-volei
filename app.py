import streamlit as st
import random
import time
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

# Inicialização do banco de dados temporário
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
        if senha != "":
            st.error("Senha incorreta")
        st.info("Visualização Pública")

# --- CRIAÇÃO DAS ABAS ---
aba1, aba2, aba3 = st.tabs(["📜 Regulamento Detalhado", "📊 Grupos & Confrontos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial")
    st.markdown("""
    ### 1. DA ORGANIZAÇÃO
    O I Torneio RS/SC de Vôlei é organizado por **Cristiano Delfino**, visando a integração entre atletas dos estados do Rio Grande do Sul e Santa Catarina.

    ### 2. DAS EQUIPES E ATLETAS
    * Cada equipe deve inscrever no mínimo 6 e no máximo 12 atletas.
    * O torneio é de categoria **Mista**. É obrigatória a presença de pelo menos 2 mulheres em quadra.
    * Uniformização: É recomendado o uso de camisetas da mesma cor.

    ### 3. DO SISTEMA DE DISPUTA
    * **Fase de Grupos:** Equipes divididas em Grupo A e Grupo B. Jogam todos contra todos dentro do grupo em Set Único de 25 pontos.
    * **Classificação:** Os 2 melhores de cada grupo avançam para as Semifinais.
    * **Critérios de Desempate:** 1º Vitórias, 2º Saldo de Pontos, 3º Confronto Direto.
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
            st.subheader("🔥 Grupo A")
            st.table(pd.DataFrame({"Equipe": st.session_state.chaves["Grupo A"]}))
            st.write("**Confrontos sugeridos:**")
            equipes_a = st.session_state.chaves["Grupo A"]
            for i in range(len(equipes_a)):
                for j in range(i + 1, len(equipes_a)):
                    st.write(f"🎮 {equipes_a[i]} vs {equipes_a[j]}")

        with col_b:
            st.subheader("🔥 Grupo B")
            st.table(pd.DataFrame({"Equipe": st.session_state.chaves["Grupo B"]}))
            st.write("**Confrontos sugeridos:**")
            equipes_b = st.session_state.chaves["Grupo B"]
            for i in range(len(equipes_b)):
                for j in range(i + 1, len(equipes_b)):
                    st.write(f"🎮 {equipes_b[i]} vs {equipes_b[j]}")
    else:
        st.warning("O sorteio ainda não foi realizado.")

with aba3:
    st.header("Caminho até o Título (Mata-Mata)")
    st.markdown("""
    <div style="display: flex; justify-content: space-around; align-items: center; background-color: #f0f2f6; padding: 20px; border-radius: 10px; color: black;">
        <div>
            <h4>SEMIFINAIS</h4>
            <div style="border: 2px solid #004a99; padding: 10px; margin: 10px; background: white;">1º Grupo A vs 2º Grupo B</div>
            <div style="border: 2px solid #004a99; padding: 10px; margin: 10px; background: white;">1º Grupo B vs 2º Grupo A</div>
        </div>
        <div style="font-size: 30px;">➡️</div>
        <div>
            <h4>FINAL</h4>
            <div style="border: 3px solid #ffd700; padding: 10px; background: white; font-weight: bold;">Vencedores Semi</div>
        </div>
        <div style="font-size: 30px;">🏆</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
