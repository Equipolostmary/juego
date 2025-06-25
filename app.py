import streamlit as st
import random
from PIL import Image
import os

st.set_page_config(page_title="Sabores Lost Mary", layout="wide", page_icon="🍓")

# ==== PRUEBA DE EXISTENCIA DE ARCHIVOS ====
st.write("🔍 Verificando archivos...")
st.write("assets/lostmary.png:", os.path.exists("assets/lostmary.png"))
st.write("assets/relx.png:", os.path.exists("assets/relx.png"))
st.write("assets/capsulas/mango.png:", os.path.exists("assets/capsulas/mango.png"))

# ==== CARGA DE IMÁGENES CON CONTROL DE ERRORES ====
try:
    lostmary_img = Image.open("assets/lostmary.png")
except Exception as e:
    st.error(f"❌ Error cargando 'lostmary.png': {e}")

try:
    relx_img = Image.open("assets/relx.png")
except Exception as e:
    st.error(f"❌ Error cargando 'relx.png': {e}")

try:
    capsula_img = Image.open("assets/capsulas/mango.png")
except Exception as e:
    st.error(f"❌ Error cargando cápsula mango.png: {e}")

# ==== ESTADO DEL JUEGO ====
if 'player_pos' not in st.session_state:
    st.session_state.player_pos = [1, 1]
if 'enemy_pos' not in st.session_state:
    st.session_state.enemy_pos = [5, 5]
if 'capsulas' not in st.session_state:
    st.session_state.capsulas = [[3, 2], [6, 1], [2, 4]]
if 'score' not in st.session_state:
    st.session_state.score = 0

# ==== MAPA ====
MAP_WIDTH, MAP_HEIGHT = 7, 7

def draw_grid():
    grid = ""
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if [x, y] == st.session_state.player_pos:
                grid += "🟥"
            elif [x, y] == st.session_state.enemy_pos:
                grid += "🟦"
            elif [x, y] in st.session_state.capsulas:
                grid += "🟡"
            else:
                grid += "⬜"
        grid += "\n"
    return grid

# ==== MOVIMIENTO ====
def move(direction):
    x, y = st.session_state.player_pos
    if direction == "up" and y > 0:
        y -= 1
    elif direction == "down" and y < MAP_HEIGHT - 1:
        y += 1
    elif direction == "left" and x > 0:
        x -= 1
    elif direction == "right" and x < MAP_WIDTH - 1:
        x += 1
    st.session_state.player_pos = [x, y]

    if [x, y] in st.session_state.capsulas:
        st.session_state.capsulas.remove([x, y])
        st.session_state.score += 1

# ==== UI ====
st.markdown("## 🎮 Sabores Lost Mary")
st.markdown("**Recoge las cápsulas sin que el RELX te atrape.**")

col1, col2 = st.columns([2, 1])
with col1:
    st.text(draw_grid())
with col2:
    if 'lostmary_img' in locals():
        st.image(lostmary_img, width=100)
    st.write("Puntaje:", st.session_state.score)
    st.button("⬅️", on_click=lambda: move("left"))
    st.button("➡️", on_click=lambda: move("right"))
    st.button("⬆️", on_click=lambda: move("up"))
    st.button("⬇️", on_click=lambda: move("down"))
