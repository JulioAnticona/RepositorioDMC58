import streamlit as st

st.title("Mi primera aplicacion en python")

st.sidebar.title("Parametros")

st.write("Elaborado por:Julio Anticona")

st.sidebar.image("DMC.png")

sesion = st.sidebar.selectbox("Selecione una sesión",[ "Sesión 1","Sesión 2", "Sesión 3", "Sesión 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido a la sesión 1")
  st.image("PYTHON.jfif")

if sesion == "Sesión 2":
  st.write("Bienvenido a la sesión 2")

  st.number_input("Ingrese el precio del producto")
  descuento = st.number_input("Ingrese el descuento del producto")

  precio_final_producto = precio - (precio*descuento)

  st.write ("El precio del producto es:" , precio_final_producto)

if sesion == "Sesión 3":
  st.write("Bienvenido a la sesión 3")

if sesion == "Sesión 4":
  st.write("Bienvenido a la sesión 4")
