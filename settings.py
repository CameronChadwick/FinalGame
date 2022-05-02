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
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    '22222222222222222222220000222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222',
    '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'],
   ['11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002220000002220000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000222000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000002220000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000022222000000000000000000000000000000001000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000000000000000000020001000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000002220000000000000000000000000000000000000000001000000000000000000000000000000000002000001',
    '10000000000000000022220000000000000000000000000000000000000000000100000000220000001000000000000000000000000000000000000000001',
    '10000000000000000000000000000000000000000000000000000000000000001100000000000000001000000000000000000000000000000000000000D01',
    '10000000000000000000000000000000000000000000000000000000000000011100000000000000001000000000000000000000000000000000000000001',
    '11111111111111100000000000011111111111100001111111000011111111111100000111111111111000000000000000000000000000000001111111111']]
