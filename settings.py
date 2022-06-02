import pygame
import random


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
    'W90000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000X0X0X0000000000000W',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080505050Z00000000000W',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000X0X0X00000000000000000000000000000W',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000080505050Z000000C5050505050Y000000000W',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000C5050505050Y0000060505050700000000000W',
    'W0000X0X0X00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W0080505050Z000000000000000000000000000000000000000000000000000000000000000605050507000000000H0T0H0000000000000W',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000VB00000000000000000W',
    'W0060505050700000000000000000000000000000000000000000000000000000000000000000H0T0H0000000000000T000000000000000W',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
    'W0000H0T0H000000000000000000000000000000000000000000000000000000000000000000000T000000000000000T0B0N00000000000W',
    'W000VB0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000K0W',
    'W000000T0B0N0000000000000000000000000000000000000000000000000000000000000000000T0BB0N0000000000T000000000000000W',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000VB000000000000VB0B000000000000000224',
    'W000000T0000000000000000000000000000000000000000000000000000000000000E000000000T000000000000000T0000000000000D0R',
    'W00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000R',
    '2222222112222222224000003224000003222222222222222222222222222222222222222222222114000000000032211222222222222222',
    '111111111111111111R00000L11R00000L11111111111111111111111111111111111111111111111R0000000000L1111111111111111111'],
   ['W900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000W',
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
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000224',
    'W0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000D0R',
    'W000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000R',
    '22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222',
    '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111']]