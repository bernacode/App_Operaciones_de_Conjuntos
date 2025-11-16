import streamlit as st
import random
import pandas as pd

from logic.operaciones import realizar_operacion,concepto_clave

def resultados():

    operaciones_list  = [
        "Unión",
        "Intersección",
        "Diferencia",
        "Complemento"
    ]

    st.title("🧩 Resultados de Operaciones de Conjuntos")
    st.markdown("Aquí se muestran los resultados de las operaciones aplicadas a tus subconjuntos de forma aleatoria.")

    if "subconjuntos" not in st.session_state or st.session_state["subconjuntos"] is None or "conjunto_principal" not in st.session_state or st.session_state["conjunto_principal"] is None:
        st.warning("Aún no has ingresado los subconjuntos y/o el conjunto principal. Ve a la página de 'Establecer Subconjuntos'.")
        st.stop()


    subconjuntos = st.session_state["subconjuntos"]
    conjunto_principal = st.session_state["conjunto_principal"]

    indices_seleccionados = random.sample(range(len(subconjuntos)), 3)
    s1_idx, s2_idx, s3_idx = indices_seleccionados

    s1 = subconjuntos[s1_idx]
    s2 = subconjuntos[s2_idx]
    s3 = subconjuntos[s3_idx]

    st.markdown("### Subconjuntos seleccionados para las operaciones:")
    st.write(f"SubConjunto {s1_idx + 1}: {s1}")
    st.write(f"SubConjunto {s2_idx + 1}: {s2}")
    st.write(f"SubConjunto {s3_idx + 1}: {s3}")

    resultados = []
    conceptos = []

    for op in operaciones_list:
        resultado = realizar_operacion(s1, s2, s3, conjunto_principal, op)
        resultados.append(resultado)
        conceptos.append(concepto_clave(op))

        st.markdown("---")
        if op != "Complemento":

            st.write(f"Operacion: **{op}**")
            st.write(f"SubConjunto {s1_idx + 1}: **{s1}**")
            st.write(f"SubConjunto {s2_idx + 1}: **{s2}**")
            st.write(f"SubConjunto {s3_idx + 1}: **{s3}**")
            st.markdown(f"**Resultado:** :blue[{resultado}]")           

        else: # Complemento
            st.write(f"Operacion: **{op}**")
            st.write(f"Universal: **{conjunto_principal}**")
            st.write(f"SubConjunto {s1_idx + 1}: **{s1}**")
            st.markdown(f"**Resultado (Complemento):** :green[{resultado}]")

    informacion = {
        "Operacion": operaciones_list,
        "Resultados": resultados,
        "Concepto Clave": conceptos
    }

    st.markdown("---")
    df_resultados = pd.DataFrame(informacion)
    st.dataframe(df_resultados)