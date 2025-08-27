import pygame
from .settings import Settings
from .app import SCREEN_WIDTH
from .running import game_map

class Sprite(Settings):
    def __init__(self, ch_sprite_width: int,ch_sprite_height: int, ch_sprite_image_name: str, ch_sprite_x: int, ch_sprite_y: int, step: int):
        Settings.__init__(
            self, 
            width = ch_sprite_width, 
            height = ch_sprite_height, 
            image_name = ch_sprite_image_name, 
            x = ch_sprite_x, 
            y = ch_sprite_y, 
            )
    
        self.FRAME = 0
        self.ANIMATION_SPEED = 0
        self.IS_FLIP = False
        
        self.GRAVITY = 6
        
        self.KEY_PRESSED = False
        self.DIRECTION = ""
        
        self.COLLISION_ITEM = False

        self.GROUND = False
        self.COLLISION_LEFT = False
        self.COLLISION_RIGHT = False
        self.COLLISION_UP = False
        
        self.CAN_MOVE = True
        
        self.STEP = step
        
        self.EGG_COUNTER = 0
        self.MEAT_COUNTER = 0
        self.KEY_COUNTER = 0
        self.LIFE_COUNTER = 5
    
    def animation(self, image_folder: str, frame_amount: int):
        
        self.ANIMATION_SPEED += 1
        
        if frame_amount > self.FRAME:
            if self.ANIMATION_SPEED % frame_amount == 0:
                self.IMAGE_NAME = f"player/{image_folder}/{self.FRAME}.png"
                
                self.FRAME += 1
        else:
            self.FRAME = 0

    def image_direction(self):
        if  self.DIRECTION == "R":
            self.IS_FLIP = False
        if self.DIRECTION == "L":
            self.IS_FLIP = True

    def draw_rect(self, screen: pygame.Surface):
        
        pygame.draw.rect(
            surface = screen,
            color = (0, 0, 255),
            rect = self.HITBOX,
            width = 2
        )
    
    def collision_item(self, block_list: list, item_name: str):
        
        for item in block_list:

            if self.HITBOX.colliderect(item):
                collision_layer = game_map.TILEMAP.get_layer_by_name(f"{item_name} collision layer")
                tile_layer = game_map.TILEMAP.get_layer_by_name(f"{item_name} tile layer")
                
                for collision_object in collision_layer:
                    
                    col_x = collision_object.x - self.MOVE_MAP
                    col_y = collision_object.y

                    if -self.STEP <= col_x - item.x <= self.STEP and col_y == item.y :
                        row = col_y // 50
                        col = (col_x + self.MOVE_MAP)// 50
                        tile_layer.data[int(row)][int(col)] = 0
                        if item_name == "Egg":
                            self.EGG_COUNTER += 1
                        collision_layer.remove(collision_object)
                        break
                break
            
    def collision_left(self, block_list: list):
        for hitbox in block_list:
            if self.HITBOX.left < 0 and self.MAIN_PLAYER == True:
                self.COLLISION_LEFT = True
                    
                self.CAN_MOVE = False
                break

            if self.HITBOX.bottom - 10 < hitbox.bottom and self.HITBOX.bottom - 10 > hitbox.top:
                if hitbox.right > self.HITBOX.left and hitbox.right < self.HITBOX.right:
                    
                    self.COLLISION_LEFT = True
                    
                    self.CAN_MOVE = False
                    break
                else:
                    self.COLLISION_LEFT = False
                    self.CAN_MOVE = True
    
    def collision_right(self, block_list: list):
        for hitbox in block_list:

            if self.HITBOX.right > SCREEN_WIDTH and self.MAIN_PLAYER == True:
                self.COLLISION_RIGHT = True
                    
                self.CAN_MOVE = False
                break

            if self.HITBOX.bottom - 10 < hitbox.bottom and self.HITBOX.bottom - 10 > hitbox.top:
                
                if self.HITBOX.right > hitbox.left and self.HITBOX.left < hitbox.left:
    
                    self.COLLISION_RIGHT = True
                    
                    self.CAN_MOVE = False
                    break
                else:
                    self.COLLISION_RIGHT = False
                    self.CAN_MOVE = True

    def collision_down(self, block_list: list):
        for hitbox in block_list:
            hitbox_top = pygame.Rect(
                hitbox.x,
                hitbox.y,
                hitbox.width,
                1
            )
            
            if self.HITBOX.colliderect(hitbox_top):
                self.GROUND = True

                if self.KEY_PRESSED == False:
                    self.DIRECTION = ""

                self.FALL = False

                self.IS_JUMP = False

                self.JUMP_DURATION = 40

                self.UNPRESS_JUMP = False

                self.CAN_MOVE = True
            
                break
            else:
                self.GROUND = False
                

    def collision_up(self, block_list: list):
        for hitbox in block_list:
            hitbox_bottom = pygame.Rect(
                hitbox.x,
                hitbox.bottom,
                hitbox.width,
                1
            )
            
            if self.HITBOX.colliderect(hitbox_bottom):
                self.COLLISION_UP = True
                break
            else:
                self.COLLISION_UP = False

    def object_fall(self, block_list: list):
        
        self.collision_down(block_list = block_list)
        
        if self.DIRECTION == "R" and self.COLLISION_RIGHT == False:
            self.move_right()

            self.CAN_MOVE = False
        
        elif self.DIRECTION == "L" and self.COLLISION_LEFT == False:
            self.move_left()

            self.CAN_MOVE = False
        
        if not self.GROUND:
            self.IMAGE_NAME = "player/gravity/0.png"
            self.Y += self.GRAVITY
            self.HITBOX.y += self.GRAVITY
            self.FALL = True
        
    def object_unstuck(self):
        if self.COLLISION_LEFT == True and self.GROUND == True:
            if self.X > SCREEN_WIDTH / 2 and 0 <= self.MOVE_MAP <= game_map.TILEMAP_WIDTH - SCREEN_WIDTH:
                self.MOVE_MAP += self.STEP
            else:
                self.X += self.STEP
                self.HITBOX.x += self.STEP
        
        if self.COLLISION_RIGHT == True and self.GROUND == True:
            if self.X > SCREEN_WIDTH / 2 and 0 <= self.MOVE_MAP <= game_map.TILEMAP_WIDTH - SCREEN_WIDTH:
                self.MOVE_MAP -= self.STEP
            else:
                self.X -= self.STEP
                self.HITBOX.x -= self.STEP