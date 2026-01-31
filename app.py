import streamlit as st
import random

# 1. Configurações Iniciais
st.set_page_config(page_title="I Torneio RS/SC de Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state: st.session_state.times = []
if 'chaves' not in st.session_state: st.session_state.chaves = None

# Acesso Administrativo (?modo=cristiano)
is_admin = st.query_params.get("modo") == "cristiano"
if not is_admin:
    st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)

st.title("🏐 I TORNEIO RS / SC de VÔLEI")
st.subheader("Unindo estados, celebrando o vôlei!")

# 2. Painel Administrativo
if is_admin:
    with st.sidebar:
        st.header("🏁 Gestão do Torneio")
        nome_equipe = st.text_input("Nome da Equipe")
        if st.button("➕ Adicionar Equipe") and nome_equipe:
            st.session_state.times.append(nome_equipe)
            st.rerun()
        st.divider()
        if st.button("🎲 REALIZAR SORTEIO") and len(st.session_state.times) >= 4:
            lista_sorteio = list(st.session_state.times)
            random.shuffle(lista_sorteio)
            meio = len(lista_sorteio) // 2
            st.session_state.chaves = {"A": lista_sorteio[:meio], "B": lista_sorteio[meio:]}
            st.snow()
            st.rerun()
        if st.button("🗑️ Limpar Todos os Dados"):
            st.session_state.times = []
            st.session_state.chaves = None
            st.rerun()

# 3. Abas de Informação
aba1, aba2, aba3, aba4 = st.tabs(["📜 Regulamento", "🚫 Atletas Federados", "📊 Chaves", "🏆 Mata-Mata"])

with aba1:
    st.markdown("### 📍 Informações Gerais")
    st.info("Data: 22 de Fevereiro de 2026 | Local: Escola Sagrado (Torres/RS) | Início: 08:00h")
    st.write("• Inscrição: R$ 400,00 | Pix: (51) 99881-6326 (Cristiano Delfino)")
    st.write("• Bola Oficial: Penalty 8.0")
    st.divider()
    st.markdown("### ⚙️ Regulamento Técnico")
    st.write("• Fase Classificatória, Quartas e Semifinais: Set único de 25 pontos.")
    st.write("• Finais (1º, 2º e 3º lugares): Melhor de 3 Sets.")
    st.write("• Equipes: Até 12 atletas | 6 substituições e 2 tempos por set.")
    st.write("• Aquecimento: 6 min na primeira partida (3' ponta, 2' saída, 1' saque).")

with aba2:
    st.header("Regras para Atletas Federados")
    st.error("LIMITE: É permitido apenas 1 (um) atleta federado por equipe.")
    st.write("O torneio possui caráter amador e recreativo.")
    st.write("Considera-se federado o atleta com registro ativo em federações profissionais.")
    st.warning("O descumprimento resultará na desclassificação imediata (Item 1.5).")

with aba3:
    st.header("Chaves de Classificação")
    st.write("Classificam-se os 4 melhores de cada chave para as Quartas de Final.")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<p style="background:#004a99;color:white;text-align:center;padding:10px;font-weight:bold;border-radius:5px;">CHAVE A</p>', unsafe_allow_html=True)
        times_a = st.session_state.chaves["A"] if st.session_state.chaves else ["Aguardando sorteio..."]*4
        for t in times_a: st.info(f"🏐 {t}")
    with col_b:
        st.markdown('<p style="background:#d9534f;color:white;text-align:center;padding:10px;font-weight:bold;border-radius:5px;">CHAVE B</p>', unsafe_allow_html=True)
        times_b = st.session_state.chaves["B"] if st.session_state.chaves else ["Aguardando sorteio..."]*4
        for t in times_b: st.info(f"🏐 {t}")

with aba4:
    st.header("Fase Eliminatória (Mata-Mata)")
    st.subheader("1. Quartas de Final")
    st.write("• Jogo 1: 1º Grupo A x 4º Grupo B")
    st.write("• Jogo 2: 2º Grupo A x 3º Grupo B")
    st.write("• Jogo 3: 1º Grupo B x 4º Grupo A")
    st.write("• Jogo 4: 2º Grupo B x 3º Grupo A")
    
    st.divider()
    st.subheader("2. Semifinais")
    st.write("• Vencedor Jogo 1 x Vencedor Jogo 4")
    st.write("• Vencedor Jogo 2 x Vencedor Jogo 3")
    
    st.divider()
    st.subheader("3. Finais")
    st.success("🏆 Finalíssima: Vencedores das semis (Melhor de 3 Sets)")
    st.info("🥉 Terceiro Lugar: Perdedores das semis (Melhor de 3 Sets)")

st.divider()
st.caption("Organização: Cristiano Delfino | Desenvolvido por Gabriel")

