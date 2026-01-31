import streamlit as st
import random
import time

# Configuração da página
st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

# Estilo para as bolinhas de vôlei caírem
def animacao_volei():
    # O Streamlit usa o 'snow' para flocos de neve, mas vamos usar emojis de vôlei no lugar
    st.markdown("""
        <style>
        .vball { font-size: 25px; }
        </style>
    """, unsafe_allow_html=True)
    st.snow() # Isso gera a animação de queda

# Inicialização do banco de dados temporário
if 'times' not in st.session_state:
    st.session_state.times = []
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

st.title("🏐 I Torneio RS/SC de Vôlei")
st.subheader("Sistema Oficial de Sorteio e Chaves")

# --- ÁREA LATERAL (SEGURANÇA) ---
with st.sidebar:
    st.header("🔐 Administração")
    # A senha que você vai usar. Pode mudar se quiser!
    senha = st.text_input("Senha do Organizador", type="password")
    
    admin_logado = (senha == "volei123")

    if admin_logado:
        st.success("Acesso Liberado!")
        st.divider()
        novo_time = st.text_input("Nome do Novo Time")
        if st.button("➕ Adicionar Time"):
            if novo_time and novo_time not in st.session_state.times:
                st.session_state.times.append(novo_time)
                st.rerun()
    else:
        if senha != "":
            st.error("Senha incorreta")
        st.info("Digite a senha para gerenciar os times.")

# --- TELA PRINCIPAL ---
col1, col2 = st.columns(2)

with col1:
    st.header("📋 Times Inscritos")
    if not st.session_state.times:
        st.write("Nenhum time cadastrado.")
    else:
        for i, time_nome in enumerate(st.session_state.times, 1):
            st.write(f"{i}. {time_nome}")

with col2:
    st.header("🎲 Sorteio das Chaves")
    
    if admin_logado:
        if len(st.session_state.times) >= 4:
            if st.button("REALIZAR SORTEIO AO VIVO!"):
                with st.spinner('Embaralhando os times...'):
                    time.sleep(2)
                    lista_sorteio = st.session_state.times.copy()
                    random.shuffle(lista_sorteio)
                    
                    # Divide em dois grupos (exemplo simples)
                    metade = len(lista_sorteio) // 2
                    st.session_state.chaves = {
                        "Grupo A": lista_sorteio[:metade],
                        "Grupo B": lista_sorteio[metade:]
                    }
                    animacao_volei() # Chama as bolinhas de vôlei!
                    st.success("Sorteio Realizado!")
        else:
            st.warning("Cadastre pelo menos 4 times para sortear.")
    else:
        st.info("Aguardando o organizador realizar o sorteio...")

# Exibição das Chaves
if st.session_state.chaves:
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🔥 Grupo A")
        for t in st.session_state.chaves["Grupo A"]:
            st.info(t)
    with c2:
        st.subheader("🔥 Grupo B")
        for t in st.session_state.chaves["Grupo B"]:
            st.info(t)

st.markdown("---")
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")
