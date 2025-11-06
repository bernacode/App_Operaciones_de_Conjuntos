import streamlit as st
import pandas as pd
import os

ruta_csv = "data/usuarios.csv"

def do_nothing():
    pass


def login():
    st.title("Login")
    usuario = st.text_input(
        "Usuario",
        key="login_usuario",
        on_change=do_nothing
    )
    password = st.text_input(
        "Contraseña",
        type="password",
        key="login_password", 
        on_change=do_nothing
    )

    if st.button("Entrar"):
        df_usuarios = pd.read_csv(ruta_csv)
        filtrar = df_usuarios[df_usuarios["usuario"] == usuario]

        if not filtrar.empty and filtrar.iloc[0]["password"] == password:
            st.session_state["logueado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["rol"] = filtrar.iloc[0]["rol"]
            st.success(f"Bienvenido {usuario}")

            st.rerun()

        else:
            st.error("Usuario o contraseña incorrectos")