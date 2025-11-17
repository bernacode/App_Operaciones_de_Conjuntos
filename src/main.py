import os 
import sys

# BASE_DIR será la carpeta donde está main.py, incluso si ejecutas desde .bat o PyInstaller
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Archivos de datos
conjuntos_path = os.path.join(BASE_DIR, 'data', 'conjuntos.csv')
usuarios_path = os.path.join(BASE_DIR, 'data', 'usuarios.csv')

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="App de Conjuntos",
    page_icon="🧮",
)

defecto = {
    "logueado": False,
    "usuario": "",
    "rol": "",
    "conjunto_principal": None,
    "subconjuntos": None,
    "pagina": "Inicio",
}

for key, valores in defecto.items():
    if key not in st.session_state:
        st.session_state[key] = valores

from interfaces.login import login
from interfaces.establecer_subconjuntos import establecer_subconjuntos
from interfaces.principal import pagina_principal
from interfaces.resultados import resultados

# Login
if not st.session_state["logueado"]:
    login()
    st.stop()

rol = st.session_state["rol"]
usuario = st.session_state["usuario"]

st.sidebar.title(f"Bienvenido, {usuario}👋")
st.sidebar.write(f"**Rol:** {rol.capitalize()}")


opciones = [
    "Inicio", 
    "Establecer Subconjuntos",
    "Resultados",
    "Cerrar Sesion"]

if rol != "admin":
    opciones = ["Inicio", "Establecer Subconjuntos","Resultados","Cerrar Sesion"]


# Menu lateral con iconos 
with st.sidebar:
    pagina = option_menu(
        menu_title="Menu de navegacion",
        options=opciones,
        icons=["house", "folder", "bar-chart", "box-arrow-right"],
        menu_icon="app-indicator",
        default_index=0
    )

    st.session_state["pagina"] = pagina


# Mostrar la pagina seleccionada
match pagina:
    case "Inicio":
        pagina_principal()
    case "Establecer Subconjuntos":
        establecer_subconjuntos()
    case "Resultados":
        resultados()
    case "Cerrar Sesion":
        for key, valor in defecto.items():
            st.session_state[key] = valor
        st.rerun()

