import pygame
from .create_path import create_path

class Settings:
    def __init__(self, width: int, height: int, image_name: str, x: int, y: int):
        self.WIDTH = width
        self.HEIGHT = height
        self.IMAGE_NAME = image_name
        self.X = x
        self.Y = y
        
        

    def load_image(self, is_flip: bool = False):
        self.IMAGE_LOAD = pygame.image.load(create_path(path = f"assets/{self.IMAGE_NAME}"))
        
        self.IMAGE_LOAD = pygame.transform.scale(
            surface = self.IMAGE_LOAD,
            size = (self.WIDTH, self.HEIGHT)
        )
        
        self.IMAGE_LOAD = pygame.transform.flip(
            surface = self.IMAGE_LOAD,
            flip_x = is_flip,
            flip_y = False
        )

    def blit_image(self, screen: pygame.Surface, move_map: int):
        screen.blit(
            source = self.IMAGE_LOAD, 
            dest = (self.X - move_map, self.Y)
        )


    
