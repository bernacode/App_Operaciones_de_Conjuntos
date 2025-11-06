import streamlit as st

st.title("Prueba de menu de navegacion")

pagina = st.sidebar.selectbox("Ir a:", ["Inicio","Parametros","Resultados"])
if pagina == "Inicio":
    st.write("Bienvenido a la pagina de inicio")
elif pagina == "Parametros":
    st.write("Aqui se seleccionan los parametros")