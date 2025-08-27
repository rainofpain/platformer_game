import pygame
from ..sprite import Sprite
from ..app import SCREEN_WIDTH
from ..tilemaps import game_map

class Player(Sprite):
    def __init__(self, ch_width: int,ch_height: int, ch_image_name: str, ch_x: int, ch_y: int, ch_step: int):
        Sprite.__init__(
            self, 
            ch_sprite_width = ch_width, 
            ch_sprite_height = ch_height, 
            ch_sprite_image_name = ch_image_name, 
            ch_sprite_x = ch_x, 
            ch_sprite_y = ch_y, 
            step = ch_step
            )
        
        self.HITBOX = pygame.Rect(
            self.X + 5, 
            self.Y + 10, 
            self.WIDTH - 7.5, 
            self.HEIGHT - 10
            )

        self.MAIN_PLAYER = True
        self.UNPRESS_JUMP = False
        self.MOVE_MAP = 0
        self.JUMP_END_POINT = 40
        self.JUMP_DURATION = self.JUMP_END_POINT
        self.IS_JUMP = False 
        self.FALL = True

    def move_left(self):
        if self.X > SCREEN_WIDTH / 2 and 0 <= self.MOVE_MAP <= game_map.TILEMAP_WIDTH - SCREEN_WIDTH or self.X < SCREEN_WIDTH / 2 and self.MOVE_MAP > 0:
            self.MOVE_MAP -= self.STEP
        else:
            self.X -= self.STEP
            self.HITBOX.x -= self.STEP

            if self.MOVE_MAP < 0:
                self.MOVE_MAP = 0

    def move_right(self):
        if self.X > SCREEN_WIDTH / 2 and 0 <= self.MOVE_MAP <= game_map.TILEMAP_WIDTH - SCREEN_WIDTH:
            self.MOVE_MAP += self.STEP
        else:
            self.X += self.STEP
            self.HITBOX.x += self.STEP

            if self.MOVE_MAP < 0:
                self.MOVE_MAP = 0

    def remove_chicken(self, chicken_list: list):
        for chicken in chicken_list:
            
            chicken_hitbox_top = pygame.Rect(
                chicken.HITBOX.x,
                chicken.HITBOX.y - 5,
                chicken.HITBOX.width,
                1
            )
            if self.HITBOX.bottom > chicken.HITBOX.y and self.FALL == True:
                if self.HITBOX.colliderect(chicken_hitbox_top):
                    chicken_list.remove(chicken)


    def jump(self):
        
        keys = pygame.key.get_pressed()
        
        if self.UNPRESS_JUMP == False:
            if self.COLLISION_UP == False:
                if keys[pygame.K_w] and self.JUMP_DURATION > 0:

                    self.IS_JUMP = True
                    self.FALL = False
                    self.Y -= 12
                    self.HITBOX.y -= 12
                    
                    self.IMAGE_NAME = "player/jump/0.png"

                    if self.DIRECTION == "R" and self.COLLISION_RIGHT == False:
                        
                        self.move_right()

                        self.CAN_MOVE = False

                    elif self.DIRECTION == "L" and self.COLLISION_LEFT == False:
                        
                        self.move_left()

                        self.CAN_MOVE = False
                
                    self.JUMP_DURATION -= 1
            else:
                self.UNPRESS_JUMP = True


    def movement(self):

        keys = pygame.key.get_pressed()
        
        #go right
        if keys[pygame.K_d]:
            
            if self.COLLISION_RIGHT == False and self.CAN_MOVE == True:
                self.IS_FLIP = False
                self.DIRECTION = "R"
                
                self.load_image(is_flip=False)
                
                self.animation(
                    image_folder = "run",
                    frame_amount = 6
                )

                self.move_right()
                
                

        #go left    
        elif keys[pygame.K_a]:
            
            if self.COLLISION_LEFT == False and self.CAN_MOVE == True:
                self.IS_FLIP = True
                self.DIRECTION = "L"
                
                self.load_image(is_flip=True)
                
                self.animation(
                    image_folder = "run",
                    frame_amount = 6
                )

                self.move_left()

        else:
            if self.IS_JUMP == False and self.DIRECTION == "":
                self.animation(
                    image_folder = "idle",
                    frame_amount = 4
                )

player = Player(
    ch_width = 50,
    ch_height = 50,
    ch_image_name = "player/idle/0.png",
    ch_x = 0,
    ch_y = 0,
    ch_step = 3
)
