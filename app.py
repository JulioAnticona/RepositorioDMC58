import streamlit as st

st.title("Mi primera aplicacion en python")

st.sidebar.title("Parametros")

st.write("Elaborado por:Julio Anticona")

sesion = st.sidebar.selectbox("Selecione una sesión",[ "Sesión 1","Sesión 2", "Sesión 3", "Sesión 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido a la sesión 1")

if sesion == "Sesión 2":
  st.write("Bienvenido a la sesión 2")

if sesion == "Sesión 3":
  st.write("Bienvenido a la sesión 3")

if sesion == "Sesión 4":
  st.write("Bienvenido a la sesión 4")
