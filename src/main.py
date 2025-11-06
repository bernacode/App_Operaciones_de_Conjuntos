import streamlit as st


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

def cargar_css(ruta_archivo):
    with open(ruta_archivo,"r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

cargar_css("assets/style.css")

# Login
if not st.session_state["logueado"]:
    login()
    st.stop()

rol = st.session_state["rol"]
usuario = st.session_state["usuario"]

st.sidebar.title(f"Bienvenido, {usuario}👋")
st.sidebar.write(f"**Rol:** {rol.capitalize()}")


opciones = ["Inicio", "Establecer Subconjuntos","Resultados","Cerrar Sesion"]
if rol != "admin":
    opciones = ["Inicio", "Establecer Subconjuntos","Resultados","Cerrar Sesion"]

pagina = st.sidebar.radio("Menu de navegacion", opciones)
st.session_state["pagina"] = pagina

match pagina:
    case "Inicio":
        pagina_principal()
    case "Establecer Subconjuntos":
        establecer_subconjuntos()
    case "Resultados":
        print("Por establecer")
    case "Cerrar Sesion":
        for key, valor in defecto.items():
            st.session_state[key] = valor
        st.rerun()

