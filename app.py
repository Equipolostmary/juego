
import streamlit as st
import time

st.set_page_config(page_title="Vapea con LostMary", layout="centered")

st.markdown("# 🌈 Vapea con LostMary")
st.image("assets/logo.png")
st.markdown("Recolecta sabores 🍓, evita los malos 🚫 y derrota a RELX 💀")

# Reproductor de música
audio_file = open('assets/pop_music.mp3', 'rb')
st.audio(audio_file.read(), format='audio/mp3')

if "sabores" not in st.session_state:
    st.session_state.sabores = 0
    st.session_state.capsulas = 0
    st.session_state.transformado = False
    st.session_state.enemigo = False

if st.button("🎮 Empezar"):
    st.session_state.sabores = 0
    st.session_state.capsulas = 0
    st.session_state.transformado = False
    st.session_state.enemigo = False

if st.session_state.sabores < 12:
    if st.button("🍓 Recolectar sabor"):
        st.session_state.sabores += 1
        st.image(f"assets/sabores/sabor{st.session_state.sabores}.png")
        st.success(f"Sabor {st.session_state.sabores} conseguido!")
        if st.session_state.sabores == 12:
            st.balloons()
            st.session_state.transformado = True

if st.session_state.transformado:
    st.image("assets/personaje.png", caption="¡Eres un Tappo Air!")
    if st.session_state.capsulas < 10:
        if st.button("💊 Recolectar cápsula"):
            st.session_state.capsulas += 1
            st.image(f"assets/capsulas/capsula{st.session_state.capsulas}.png")
            if st.session_state.capsulas == 10:
                st.session_state.enemigo = True

if st.session_state.enemigo:
    st.image("assets/relx.png", caption="RELX el Monstruo")
    st.markdown("Le lanzas tus sabores frutales 🌈✨")
    st.success("¡RELX ha sido derrotado por el sabor superior! 🎉")
