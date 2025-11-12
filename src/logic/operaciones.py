
def realizar_operacion(s1,s2,s3, u,op):

    set1, set2, set3, universo = set(map(int, s1)), set(map(int, s2)), set(map(int, s3)), set(map(int, u))
    match op:
        case "Unión":
            return set1 | set2 | set3
        case "Intersección":
            return set1 & set2 & set3
        case "Diferencia":
            return (set1 - set2) - set3
        case "Complemento":
            return universo - set1


def concepto_clave(operacion):
    """
    Devuelve una breve descripción teórica de la operación de conjuntos.
    """
    conceptos = {
        "Unión": "🔗Reúne todos los elementos que pertenecen a cualquiera de los conjuntos.",
        "Intersección": "🔘Contiene solo los elementos comunes entre los conjuntos.",
        "Diferencia": "➖Contiene los elementos que están en el primer conjunto pero no en los otros.",
        "Complemento": "🌌Contiene los elementos del conjunto universal que no están en el subconjunto."
    }
    return conceptos.get(operacion, "Operación no reconocida.")