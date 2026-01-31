import streamlit as st
import random
import time
import pandas as pd

st.set_page_config(page_title="Torneio RS/SC Vôlei", page_icon="🏐", layout="wide")

if 'times' not in st.session_state:
    st.session_state.times = []
if 'chaves' not in st.session_state:
    st.session_state.chaves = None

st.title("🏐 I Torneio RS/SC de Vôlei")

with st.sidebar:
    st.header("🔐 Administração")
    senha = st.text_input("Senha do Organizador", type="password")
    admin_logado = (senha == "volei123")
    if admin_logado:
        st.success("Acesso Liberado!")
        novo_time = st.text_input("Nome do Time")
        if st.button("➕ Cadastrar"):
            if novo_time: st.session_state.times.append(novo_time); st.rerun()
    else:
        st.info("Apenas visualização.")

aba1, aba2, aba3 = st.tabs(["📜 Regulamento Detalhado", "📊 Grupos & Confrontos", "🏆 Mata-Mata"])

with aba1:
    st.header("Regulamento Oficial")
    st.write("O I Torneio RS/SC de Vôlei é organizado por Cristiano Delfino...")

with aba2:
    st.header("Distribuição dos Grupos")
    
    # Se ainda não sorteou, cria uma visualização de "Espelho"
    if st.session_state.chaves is None:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div style="background-color: #004a99; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">GRUPO A (Aguardando Sorteio)</div>', unsafe_allow_html=True)
            for i in range(1, 5):
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: #f9f9f9; color: #999;">🏐 Time {i}</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div style="background-color: #d9534f; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">GRUPO B (Aguardando Sorteio)</div>', unsafe_allow_html=True)
            for i in range(1, 5):
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: #f9f9f9; color: #999;">🏐 Time {i}</div>', unsafe_allow_html=True)
        
        if admin_logado:
            st.divider()
            if st.button("🎲 REALIZAR SORTEIO AGORA"):
                if len(st.session_state.times) >= 4:
                    lista = st.session_state.times.copy()
                    random.shuffle(lista)
                    meio = len(lista) // 2
                    st.session_state.chaves = {"Grupo A": lista[:meio], "Grupo B": lista[meio:]}
                    st.snow()
                    st.rerun()
                else:
                    st.error("Cadastre pelo menos 4 times antes de sortear!")
    
    else:
        # Se já sorteou, mostra os times reais
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div style="background-color: #004a99; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">GRUPO A</div>', unsafe_allow_html=True)
            for t in st.session_state.chaves["Grupo A"]:
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: white; color: black;">🏐 {t}</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div style="background-color: #d9534f; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold;">GRUPO B</div>', unsafe_allow_html=True)
            for t in st.session_state.chaves["Grupo B"]:
                st.markdown(f'<div style="border: 1px solid #ddd; padding: 10px; border-top: none; background-color: white; color: black;">🏐 {t}</div>', unsafe_allow_html=True)

with aba3:
    st.header("Caminho até o Título (Mata-Mata)")
    st.markdown("""
    <div style="display: flex; justify-content: space-around; align-items: center; background-color: #f0f2f6; padding: 20px; border-radius: 10px; color: black;">
        <div style="flex: 1; text-align: center;">
            <h4 style="color: #333;">SEMIFINAIS</h4>
            <div style="border: 2px solid #004a99; padding: 10px; margin: 10px; background: white; border-radius: 5px;">1º Grupo A vs 2º Grupo B</div>
