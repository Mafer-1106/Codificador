import streamlit as st

# --- Funciones ---
def crear_tabla_sustitucion(palabra1, palabra2): 
    if len(palabra1) != len(palabra2):
        return None
    if len(set(palabra1.lower())) != len(palabra1) or len(set(palabra2.lower())) != len(palabra2):
        return None
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
            mensaje_codificado += letra
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
st.title(" 🕵️ Codificador de Mensajes 🕵️ ")

st.write("Selecciona la clave para codificar tu mensaje:")

clave_seleccionada = st.selectbox("Claves disponibles", claves)
palabra1 = "patron"
tabla = crear_tabla_sustitucion(palabra1, clave_seleccionada)

mensaje = st.text_input("Escribe el mensaje a codificar:")

if st.button("Codificar"):
    if tabla is None:
        st.error("ERROR: La clave seleccionada no es válida.")
    elif mensaje.strip() == "":
        st.warning("Por favor, escribe un mensaje.")
    else:
        mensaje_codificado = codificar_palabra(mensaje, tabla)
        st.success(f"Mensaje codificado: {mensaje_codificado}")
        
        # 🎉 Celebración con confeti y 'bombas'
        st.balloons()  # confeti
        st.snow()      # efecto extra de 'bombas'
