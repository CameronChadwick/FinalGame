import pygame


DARK_BLUE = (9, 60, 143)
# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (242, 235, 31)
GREEN = (31, 242, 137)
RED = (255, 0, 0)
BLUE = (69, 91, 255)
BULLET_COLOR = (255, 196, 0)


FPS = 60

BULLET_WIDTH = 7
BULLET_HEIGHT = 3

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

TILE_SIZE = 25


LAYOUT = [[
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000D0',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222',
    '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'],
   ['W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '22222222222222222222222222222222222222000000222222222222222222222222222222222222222222222222222222222222222222222222222222222',
    '11111111111111111111111111111111111111000000111111111111111111111111111111111111111111111111111111111111111111111111111111111']]
