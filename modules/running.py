import pygame
from .app import screen
from .events import event_quit, unpress_w
from .tilemaps import game_map
from .player import player
from .create_path import create_path
from .chicken import chicken
from .hud import blit_hud

pygame.init()

chicken_list = [chicken]

def run():
    running = True

    while running:
        screen.fill(color = (0, 0, 0))
        clock = pygame.time.Clock()
        events = pygame.event.get()

        for event in events:
            if event_quit(event = event):
                running = False
                pygame.quit()
            if unpress_w(event = event):
                player.UNPRESS_JUMP = True

        blit_hud(
            map = game_map, 
            player = player, 
            screen = screen
        )
        game_map.blit_map(screen = screen, move = player.MOVE_MAP)

        block_hitboxes_list = game_map.create_rect_list(layer_name = "Blocks collision layer")
        egg_hitboxes_list = game_map.create_rect_list(layer_name = "Egg collision layer")

        # game_map.blit_map_rect(screen = screen, layer_name = "Blocks collision layer")
        game_map.blit_decorations(screen = screen)

        for chicken_obj in chicken_list:

            chicken_obj.load_image(is_flip = chicken_obj.IS_FLIP)
            chicken_obj.blit_image(screen = screen, move_map = player.MOVE_MAP)
            # chicken_obj.draw_rect(screen = screen)

            chicken_obj.collision_right(block_list = block_hitboxes_list)
            chicken_obj.collision_left(block_list = block_hitboxes_list)

            chicken_obj.run(max_distance = 500)
        
        player.image_direction()

        player.load_image(is_flip = player.IS_FLIP)
        player.blit_image(screen = screen, move_map = 0)
        # player.draw_rect(screen = screen)

        
        player.movement()
        
        player.collision_item(block_list = egg_hitboxes_list, item_name = "Egg")

        player.remove_chicken(chicken_list = chicken_list)
       
        player.object_fall(block_list = block_hitboxes_list)
        player.collision_left(block_list = block_hitboxes_list)
        player.collision_right(block_list = block_hitboxes_list)
        player.collision_up(block_list = block_hitboxes_list)

        player.jump()

        player.object_unstuck()
    
        clock.tick(60)
        pygame.display.flip()