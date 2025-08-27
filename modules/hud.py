import pygame
from .tilemaps import Tilemap
from .player import Player
from .create_path import create_path
pygame.init()

font = pygame.font.Font(None, 46)
egg =  pygame.image.load(create_path(path = "assets/hud/egg.png"))
meat = pygame.image.load(create_path(path = "assets/hud/meat.png"))
key = pygame.image.load(create_path(path = "assets/hud/key.png"))
heart = pygame.image.load(create_path(path = "assets/hud/heart.png"))
heart_list = [heart, heart, heart, heart, heart]

def blit_hud(map: Tilemap, player: Player, screen: pygame.Surface):

        heart_x = 21
        for heart_img in heart_list:
            screen.blit(
            source = heart_img,
            dest = (heart_x, 15)
            )
            heart_x += 24

        egg_counter = font.render(
            f"{player.EGG_COUNTER}",
            True,
            (255, 255, 255)
            )
        
        meat_counter = font.render(
            f"{player.MEAT_COUNTER}",
            True,
            (255, 255, 255)
            )
        
        key_counter = font.render(
            f"{player.KEY_COUNTER}",
            True,
            (255, 255, 255)
            )
        
        screen.blit(
            source = egg,
            dest = (183, 8)
        )
        screen.blit(
            source = egg_counter,
            dest = (212, 11)
        )
        screen.blit(
            source = key,
            dest = (277, 13)
        )
        screen.blit(
            source = key_counter,
            dest = (325, 11)
        )
        screen.blit(
            source = meat,
            dest = (387, 13)
        )
        screen.blit(
            source = meat_counter,
            dest = (443, 11)
        )