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
    * O torneio é de categoria **Mista**. É obrigatória a presença de pelo menos 2 mulheres em quadra durante todo o tempo de jogo.
    * Uniformização: É recomendado o uso de camisetas da mesma cor para a equipe.

    ### 3. DO SISTEMA DE DISPUTA
    * **Fase de Grupos:** As equipes serão divididas em Grupo A e Grupo B. Jogam todos contra todos dentro do grupo em Set Único de 25 pontos (máximo 27 em caso de empate).
    * **Classificação:** Os 2 melhores de cada grupo avançam para as Semifinais.
    * **Critérios de Desempate:** 1º Vitórias, 2º Saldo de Pontos, 3º Confronto Direto.

    ### 4. PONTUAÇÃO E ARBITRAGEM
    * A arbitragem será composta por membros da organização e voluntários capacitados.
    * Discussões com a arbitragem podem acarretar em cartão amarelo (advertência) ou vermelho (expulsão do set).

    ### 5. LOCAL E HORÁRIO
    * **Endereço:** Ginásio Municipal de Torres - RS.
    * **Horário de Chegada:** 07:30h para confirmação de súmula.
    """)

with aba2:
    st.header("Distribuição dos Grupos")
    
    if admin_logado:
        if st.button("🎲 REALIZAR SORTEIO AGORA"):
            with st.spinner('Sorteando...'):
                time.sleep(2)
                lista = st.session_state.times.copy()
                random.shuffle(lista)
                # Divisão balanceada
                meio = len(lista) // 2
                st.session_state.chaves = {"Grupo A": lista[:meio], "Grupo B": lista[meio:]}
                st.snow()
    
    if st.session_state.chaves:
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("🔥 Grupo A")
            df_a = pd.DataFrame({"Equipe": st.session_state.chaves["Grupo A"]})
            st.table(df_a)
            st.markdown("**Possíveis Confrontos (Grupo A):**")
            for i in range(len(st.session_state.chaves["Grupo A"])):
                for j in range(i + 1, len(st.session_state.chaves["Grupo A"])):
                    st.write(f"🎮 {st.session_state.chaves['Grupo A'][i]} vs {st.session_state.chaves['Grupo A'][j]}")

        with col_b:
            st.subheader("🔥 Grupo B")
            df_b = pd.DataFrame({"Equipe": st.session_state.chaves["Grupo B"]})
            st.table(df_b)
            st.markdown("**Poss
