
import streamlit as st
import random
import time

st.set_page_config(page_title="Vapea con LostMary", page_icon="💨", layout="centered")

# --- Assets ---
st.image("assets/logo.png", width=200)
st.title("💨 Vapea con LostMary")
st.caption("Recolecta sabores, evoluciona y derrota al monstruo RELX")

# --- Sonido (simple) ---
st.audio("assets/pop_music.mp3")

# --- Inicialización de estado ---
if "fase" not in st.session_state:
    st.session_state.fase = 1
if "sabores" not in st.session_state:
    st.session_state.sabores = 0
if "capsulas" not in st.session_state:
    st.session_state.capsulas = 0
if "muerto" not in st.session_state:
    st.session_state.muerto = False

# --- Juego Fase 1 ---
if st.session_state.fase == 1:
    st.subheader("🎯 Recolecta 12 sabores de Lost Mary")
    if st.button("🚀 Inhalar sabor"):
        resultado = random.choices(["bueno", "malo"], weights=[0.8, 0.2])[0]
        if resultado == "malo":
            st.image("assets/relx_monstruo.png", width=150)
            st.error("¡Has inhalado un sabor no original! 💀")
            st.session_state.muerto = True
        else:
            st.session_state.sabores += 1
            st.image(f"assets/sabores/sabor{random.randint(1,3)}.png", width=100)
            st.success(f"Llevas {st.session_state.sabores}/12 sabores")
            if st.session_state.sabores >= 12:
                st.session_state.fase = 2
                st.balloons()

# --- Fase 2 ---
elif st.session_state.fase == 2:
    st.subheader("⚡ Eres un Tappo Air. Recolecta 10 cápsulas")
    st.image("assets/tappo_air.png", width=150)
    if st.button("🎯 Recoger cápsula"):
        st.session_state.capsulas += 1
        st.image(f"assets/capsulas/capsula{random.randint(1,2)}.png", width=80)
        st.success(f"{st.session_state.capsulas}/10 cápsulas recolectadas")
        if st.session_state.capsulas >= 10:
            st.session_state.fase = 3
            st.balloons()

# --- Fase 3 ---
elif st.session_state.fase == 3:
    st.subheader("👾 Lucha final contra RELX")
    st.image("assets/relx_monstruo.png", width=150)
    if st.button("🔥 Lanzar cápsula de sabor"):
        for i in range(3):
            st.write("¡Impacto!")
            time.sleep(0.5)
        st.success("RELX no soportó tanto sabor. ¡Has ganado! 🏆")
        st.image("assets/tappo_air.png", width=150)
        st.balloons()

# --- Reinicio ---
if st.session_state.muerto:
    if st.button("🔁 Reintentar"):
        for key in ["fase", "sabores", "capsulas", "muerto"]:
            st.session_state[key] = 0 if key != "muerto" else False
