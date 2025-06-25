import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Sabores Lost Mary", layout="wide", page_icon="🍓")

# ==== CARGA DE IMÁGENES ====
lostmary_img = Image.open("assets/lostmary.png")
relx_img = Image.open("assets/relx.png")
capsula_img = Image.open("assets/capsulas/mango.png")  # Puedes cambiar esto por rotación de sabores

# ==== ESTADO DEL JUEGO ====
if 'player_pos' not in st.session_state:
    st.session_state.player_pos = [1, 1]
if 'enemy_pos' not in st.session_state:
    st.session_state.enemy_pos = [5, 5]
if 'capsulas' not in st.session_state:
    st.session_state.capsulas = [[3, 2], [6, 1], [2, 4]]
if 'score' not in st.session_state:
    st.session_state.score = 0

# ==== MAPA DEL JUEGO ====
MAP_WIDTH, MAP_HEIGHT = 7, 7

def draw_grid():
    grid = ""
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if [x, y] == st.session_state.player_pos:
                grid += "🟥"  # Personaje Lost Mary
            elif [x, y] == st.session_state.enemy_pos:
                grid += "🟦"  # Enemigo RELX
            elif [x, y] in st.session_state.capsulas:
                grid += "🟡"  # Cápsula
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

    # Recolectar cápsula
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
    st.image(lostmary_img, width=100)
    st.write("Puntaje:", st.session_state.score)
    st.button("⬅️", on_click=lambda: move("left"))
    st.button("➡️", on_click=lambda: move("right"))
    st.button("⬆️", on_click=lambda: move("up"))
    st.button("⬇️", on_click=lambda: move("down"))
