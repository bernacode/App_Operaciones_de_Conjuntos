import streamlit as st


def validar_usuario(usuario, password):
    return usuario == "admin" and password == "1234"

def login():
    st.title("Login")
    usuario = st.text_input("Usuario")
    password = st.text_input("Contrasena",type="password")

    if st.button("Entrar"):
        if validar_usuario(usuario,password):
            st.session_state["logueado"] = True
        else:
            st.error("Usuario o contrase;a incorrectos")


login()