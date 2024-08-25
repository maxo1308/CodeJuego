import pygame
from settings import *
from game_manager import GameManager

pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Party en Pygame")

# Instancia del GameManager
game_manager = GameManager()

# Bucle principal del juego
running = True
while running:s
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar y dibujar el estado del juego
    game_manager.update()
    game_manager.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
