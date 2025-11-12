import streamlit as st
import numpy as np
import pandas as pd
import os 

def establecer_subconjuntos():

    # Ruta absoluta del archivo csv.
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_csv = os.path.join(BASE_DIR,"data","conjuntos.csv")
    os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)


    st.title("Establecer Subconjuntos")

    usuario = st.session_state["usuario"]
    rol = st.session_state.get("rol","usuario")

    # Conjunto_Principal 
    if "conjunto_principal" not in st.session_state or st.session_state["conjunto_principal"] is None:
        if rol == "admin":
            st.session_state["conjunto_principal"] = []
        else:
            st.session_state["conjunto_principal"] = np.random.choice(np.arange(1,100),size=50,replace=False)

    if rol == "admin":
        st.write("Admin: puedes modificar el conjunto principal")
        
        conjunto = st.session_state.get("conjunto_principal")
        if conjunto is None:
            conjunto = []
        elif isinstance(conjunto,np.ndarray):
            conjunto = conjunto.tolist()

        conjunto_input = st.text_input(
            "conjunto principal (separado por comas)",
            value =",".join(map(str,conjunto)),
            key ="input_conjunto"
        )
        try:
            conjunto = np.array([ int(x.strip()) for x in conjunto_input.split(",") if x.strip() != ""])
            st.session_state["conjunto_principal"] = conjunto 
        except ValueError:
            st.error("El conjunto principal tiene elementos no validos")
            return
    
    conjunto = st.session_state["conjunto_principal"]
    st.write(f"Conjunto principal: {conjunto}")
    st.write("Ingresa tus 4 subconjuntos (separa los elementos con comas)")

    sub1 = st.text_input("Subconjunto 1", key="sub1")
    sub2 = st.text_input("Subconjunto 2", key="sub2")
    sub3 = st.text_input("Subconjunto 3", key="sub3")
    sub4 = st.text_input("Subconjunto 4", key="sub4")

    if st.button("Guardar Subconjuntos"):
        subconjuntos = []
        errores = []

        for idx, s in enumerate([sub1,sub2,sub3,sub4],start=1):
            try:
                arr = np.array([int(x.strip()) for x in s.split(",") if x.strip() !=""])
                if not np.all(np.isin(arr,conjunto)):
                    errores.append(f"Subconjunto {idx} contiene elementos que no están en el conjunto principal.")
                else:
                    subconjuntos.append(arr)
            except ValueError:
                errores.append(f"Subconjunto {idx} tiene elementos no válidos.")
        
        if errores:
            for e in errores:
                st.error(e)
        else:
            st.session_state["subconjuntos"] = subconjuntos

            data = {
                "Usuario": [usuario]*4,
                "ConjuntoPrincipal": [",".join(map(str,conjunto))]*4,
                "SubConjunto": [f"S{i+1}" for i in range(4)],
                "Elementos": [",".join(map(str,arr)) for arr in subconjuntos]
            }

            df = pd.DataFrame(data)
            df.to_csv(ruta_csv,index=False,mode="a", header=not os.path.exists(ruta_csv))
            st.success(f"SubConjuntos guardados correctamente en '{ruta_csv}'!")
            st.dataframe(df)