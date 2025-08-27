import pygame

def event_quit(event: pygame.event) -> bool:
    if event.type == pygame.QUIT:
        return True