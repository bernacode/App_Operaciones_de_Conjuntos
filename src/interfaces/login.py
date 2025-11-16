import streamlit as st
import pandas as pd
import os
import sys


# Definir la carpeta base, funcione incluso desde .bat o PyInstaller
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Ruta absoluta al CSV de usuarios
usuarios_path = os.path.join(BASE_DIR, '..', 'data', 'usuarios.csv')  # '..' porque login.py está en interfaces/

def do_nothing():
    pass


def login():
    st.title("🔐 Login")
    st.caption("Accede a la aplicación para gestionar tus conjuntos y operaciones.")

    usuario = st.text_input(
        "👤 Usuario",
        key="login_usuario",
        on_change=do_nothing
    )
    password = st.text_input(
        "🔑 Contraseña",
        type="password",
        key="login_password", 
        on_change=do_nothing
    )

    if st.button("🚪 Iniciar sesion"):
        df_usuarios = pd.read_csv(usuarios_path)
        filtrar = df_usuarios[df_usuarios["usuario"] == usuario]

        if not filtrar.empty and filtrar.iloc[0]["password"] == password:
            st.session_state["logueado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["rol"] = filtrar.iloc[0]["rol"]
            st.success(f"✅ Acceso concedido. Bienvenido a la aplicación {usuario}.")

            st.rerun()

        else:
            st.error("❌ Usuario o contraseña incorrectos. Intenta de nuevo.")