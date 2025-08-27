import pytmx
import pygame
from .create_path import create_path

class Tilemap:
    def __init__(self, path_name: str):
        self.TILEMAP_PATH = create_path(path = f"assets/tilemaps/{path_name}")
        self.TILEMAP = pytmx.load_pygame(filename = self.TILEMAP_PATH)
        self.TILE_WIDTH = self.TILEMAP.tilewidth
        self.TILE_HEIGHT = self.TILEMAP.tileheight
        self.TILEMAP_WIDTH = self.TILEMAP.width * self.TILE_WIDTH
        
    def blit_map(self, screen: pygame.Surface, move: int):

        tile_layers = self.TILEMAP.visible_tile_layers
        self.MOVE = move
        
        for layer_id in tile_layers:
            layer = self.TILEMAP.layers[layer_id]
            
            for x, y, cell_id in layer:
                if cell_id:
                
                    image = self.TILEMAP.get_tile_image_by_gid(cell_id)
                    screen.blit(
                        source = image,
                        dest = (x * self.TILE_WIDTH - self.MOVE, y * self.TILE_HEIGHT)
                    )
    
    def create_rect_list(self, layer_name: str):
        collision_layer = self.TILEMAP.get_layer_by_name(layer_name)
        
        
        rect_list = []
        
        for collision_object in collision_layer:
            
            hitbox = pygame.Rect(
                collision_object.x - self.MOVE,
                collision_object.y,
                collision_object.width,
                collision_object.height
            )
            
            rect_list.append(hitbox)
        
        return rect_list

    def blit_map_rect(self, screen: pygame.Surface, layer_name: str):
        collision_layer = self.TILEMAP.get_layer_by_name(layer_name)

        for collision_object in collision_layer:
            hitbox = pygame.Rect(
                collision_object.x - self.MOVE,
                collision_object.y,
                collision_object.width,
                collision_object.height
            )
            
            pygame.draw.rect(
                surface = screen,
                color = (255, 0, 0),
                rect = hitbox,
                width = 1
            )

    def blit_decorations(self, screen: pygame.Surface):
        decorations_layer = self.TILEMAP.get_layer_by_name("Decorations layer")

        for decoration_object in decorations_layer:
            screen.blit(
                source = decoration_object.image,
                dest = (decoration_object.x - self.MOVE, decoration_object.y)
            )

game_map = Tilemap("2907_test/map.tmx")