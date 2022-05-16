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
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W00000000000000000000000000000E000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000D',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '32222222222222222240000032222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222',
    'L11111111111111111R00000L1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'],
   ['W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000D0W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    '22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222',
    '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111']]