import pygame
import sprites
from settings import *

# base elements
pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Game")

game_layout = sprites.Layout(LAYOUT)
layout_list = game_layout.get_layout()

player_group = pygame.sprite.Group()


player = sprites.Player(225, 500, 25, layout_list)
player_group.add(player)


def reset_level(new_level):
    global player, player_group, game_layout, layout_list
    # empty groups
    player_group.empty()

    # create level
    game_layout.create(new_level)
    layout_list = game_layout.get_layout()
    player_group = pygame.sprite.Group()
    player = sprites.Player(225, 500, 25, layout_list)
    player_group.add(player)

    return layout_list


def game_play():

    level = 1
    max_level = 2

    layout_lis = reset_level(level)

    running = True

    clock = pygame.time.Clock()

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.QUIT:
                running = False

        screen.fill(DARK_BLUE)

        player_group.update(screen)
        game_layout.update(screen)

        pygame.display.flip()

    pygame.quit()


playing = True
while playing:
    game_play()

pygame.quit()
