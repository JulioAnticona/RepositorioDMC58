import streamlit as st
import numpy as nt

st.title("Mi primera aplicacion en python")

st.sidebar.title("Parametros")

st.write("Elaborado por:Julio Anticona")

st.sidebar.image("DMC.png")

sesion = st.sidebar.selectbox("Selecione una sesión",[ "Sesión 1","Sesión 2", "Sesión 3", "Sesión 4"])

if sesion == "Sesión 1":
  st.write("Bienvenido a la sesión 1")
  st.image("PYTHON.jfif")

elif sesion == "Sesión 2":

  st.write("Bienvenido la sesión 2")
 
  precio = st.number_input("Ingrese el precio del producto", min_value = 0 , max_value = 5000 , value = 1200)
  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100% ", min_value = 0 , max_value = 100 )
  precio_final_producto = precio - (precio*(descuento/100))
  st.write("El precio final del producto es: ", precio_final_producto  )

if sesion == "Sesión 3":
  st.write("Bienvenido a la sesión 3")
  
  fin_rango = st.slider("Selecione un valor", min_value=0, max_value=20, value=7)

  arreglo = np.arange (0, fin_rango)

  st.write (arreglo)

if sesion == "Sesión 4":
  st.write("Bienvenido a la sesión 4")
