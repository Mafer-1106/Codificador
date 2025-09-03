import streamlit as st

# --- Funciones ---
def crear_tabla_sustitucion(palabra1, palabra2): 
    # Verificar que tengan la misma longitud y letras únicas
    if len(palabra1) != len(palabra2):
        return None
    if len(set(palabra1.lower())) != len(palabra1) or len(set(palabra2.lower())) != len(palabra2):
        return None

    # Crear tabla de sustitución
    tabla = {}
    for l1, l2 in zip(palabra1.lower(), palabra2.upper()):
        tabla[l1] = l2
    return tabla


def codificar_palabra(palabra, tabla):
    mensaje_codificado = ""
    for letra in palabra.lower():
        if letra in tabla:
            mensaje_codificado += tabla[letra]
        else:
            mensaje_codificado += letra  # deja igual lo que no esté en la clave
    return mensaje_codificado


# --- Lista de claves ---
claves = [
    "camino",
    "tiempo",
    "bronce",
    "cuerpo",
    "frugal",
    "piedra",
    "muerto",
    "silbar",
    "dentro",
    "justan"
]

# --- Streamlit ---
st.title("Codificador de Mensajes")

st.write("Selecciona la clave para codificar tu mensaje:")

# Menú desplegable de claves
clave_seleccionada = st.selectbox("Claves disponibles", claves)

# Palabra base
palabra1 = "patron"

# Crear tabla de sustitución
tabla = crear_tabla_sustitucion(palabra1, clave_seleccionada)

# Ingreso de mensaje
mensaje = st.text_input("Escribe el mensaje a codificar:")

# Botón para codificar
if st.button("Codificar"):
    if tabla is None:
        st.error("ERROR: La clave seleccionada no es válida.")
    elif mensaje.strip() == "":
        st.warning("Por favor, escribe un mensaje.")
    else:
        mensaje_codificado = codificar_palabra(mensaje, tabla)
        st.success(f"Mensaje codificado: {mensaje_codificado}")
