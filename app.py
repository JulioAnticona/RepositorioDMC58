import streamlit as st

st.title("Mi primera aplicacion en python")

st.sidebar.title("Parametros")

st.write("Elaborado por:Julio Anticona")

sesion = st.sidebar.selectbox("Selecione una sesión",[ "Sesión 1","Sesión 2", "Sesión 3", "Sesión 4"])
