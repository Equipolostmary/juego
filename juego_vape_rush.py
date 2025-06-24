
import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configurar pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Vape Rush - Sabor Piña Mango")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 200, 255)

# Jugador (vape)
jugador = pygame.Rect(100, 300, 50, 50)
velocidad = 5

# Objetos que dan puntos (sabores)
sabores = [pygame.Rect(random.randint(400, 750), random.randint(50, 550), 30, 30) for _ in range(5)]
puntos = 0

# Fuente
fuente = pygame.font.SysFont(None, 36)

# Bucle principal
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    pantalla.fill(BLANCO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.top > 0:
        jugador.move_ip(0, -velocidad)
    if teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
        jugador.move_ip(0, velocidad)
    
    # Detección de colisiones
    for sabor in sabores[:]:
        if jugador.colliderect(sabor):
            sabores.remove(sabor)
            sabores.append(pygame.Rect(random.randint(400, 750), random.randint(50, 550), 30, 30))
            puntos += 10

    # Dibujar jugador
    pygame.draw.rect(pantalla, AZUL, jugador)
    
    # Dibujar sabores
    for sabor in sabores:
        pygame.draw.rect(pantalla, (255, 200, 0), sabor)

    # Mostrar puntos
    texto_puntos = fuente.render(f"Puntos: {puntos}", True, NEGRO)
    pantalla.blit(texto_puntos, (10, 10))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
