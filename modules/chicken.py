import pygame
from .sprite import Sprite
from .player import player

class Chicken(Sprite):

    def __init__(self, ch_chicken_width: int, ch_chicken_height: int, ch_chicken_image_name: str, ch_chicken_x: int, ch_chicken_y: int, ch_chicken_step: int):
        Sprite.__init__(
            self,
            ch_sprite_width = ch_chicken_width, 
            ch_sprite_height = ch_chicken_height, 
            ch_sprite_image_name = ch_chicken_image_name, 
            ch_sprite_x = ch_chicken_x, 
            ch_sprite_y = ch_chicken_y, 
            step = ch_chicken_step
        )

        self.HITBOX = pygame.Rect(
            self.X, 
            self.Y + 10, 
            self.WIDTH - 6, 
            self.HEIGHT - 10
            )
        
        self.MAIN_PLAYER = False
        self.DIST_COUNT = 0
        
    def run(self, max_distance):
        if self.DIST_COUNT % max_distance == 0 or self.COLLISION_RIGHT == True or self.COLLISION_LEFT == True:
            self.IS_FLIP = not self.IS_FLIP
        if self.IS_FLIP == False:
            self.X += self.STEP
            self.HITBOX.x += self.STEP
        elif self.IS_FLIP == True:
            self.X -= self.STEP
            self.HITBOX.x -= self.STEP
        self.HITBOX.x = self.X - player.MOVE_MAP
        self.DIST_COUNT += 1
        
    
chicken = Chicken(
            ch_chicken_width = 50,
            ch_chicken_height = 50,
            ch_chicken_image_name = "npc/chicken/idle/0.png",
            ch_chicken_x = 640,
            ch_chicken_y = 654,
            ch_chicken_step = 1
        )