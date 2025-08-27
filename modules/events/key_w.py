import pygame

def unpress_w(event: pygame.event) -> bool:
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            return True