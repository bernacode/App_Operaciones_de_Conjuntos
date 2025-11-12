import streamlit as st

def pagina_principal():
    st.title(" 🏠 Ventana Principal")
    st.caption("👇 Bienvenido a la app de operaciones de conjuntos")
    st.markdown("""Esta aplicación permite trabajar con conjuntos y subconjuntos. 
    Funciona de la siguiente manera:
    
    - **Admin**: puede definir y modificar el conjunto principal.
    - **Usuario**: puede ver el conjunto principal y establecer los subconjuntos.
    
    Puedes navegar por las distintas páginas usando la barra lateral.""")

    conjunto = st.session_state.get("conjunto_principal")
    if conjunto is not None:
        st.write(f"Conjunto principal: {conjunto}")