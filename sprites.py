import pygame
from settings import *


class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        """rectangle is a tuple with (x, y, x+offset, y+offset)"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

    def load_grid_images(self, num_rows, num_cols, x_margin=0, x_padding=0,
            y_margin=0, y_padding=0, width=None, height=None, colorkey = None):
        """Load a grid of images.
        x_margin is the space between the top of the sheet and top of the first
        row. x_padding is space between rows. Assumes symmetrical padding on
        left and right.  Same reasoning for y. Calls self.images_at() to get a
        list of images.
        """

        sheet_rect = self.sheet.get_rect()
        sheet_width, sheet_height = sheet_rect.size

        # To calculate the size of each sprite, subtract the two margins,
        #   and the padding between each row, then divide by num_cols.
        # Same reasoning for y.
        if width and height:
            x_sprite_size = width
            y_sprite_size = height
        else:
            x_sprite_size = (sheet_width - 2 * x_margin
                    - (num_cols - 1) * x_padding) / num_cols
            y_sprite_size = (sheet_height - 2 * y_margin
                    - (num_rows - 1) * y_padding) / num_rows

        sprite_rects = []
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                # Position of sprite rect is margin + one sprite size
                #   and one padding size for each row. Same for y.
                x = x_margin + col_num * (x_sprite_size + x_padding)
                y = y_margin + row_num * (y_sprite_size + y_padding)
                sprite_rect = (x, y, x_sprite_size, y_sprite_size)
                sprite_rects.append(sprite_rect)

        return self.images_at(sprite_rects, colorkey)


class Layout():
    def __init__(self, layout):
        self.images()

        self.layout = layout
        self.tile_list = []

    def create(self, level):
        self.tile_list = []
        level_num = self.layout[level - 1]
        for i, row in enumerate(level_num):
            for j, col in enumerate(row):
                x_val = j * TILE_SIZE
                y_val = i * TILE_SIZE

                if col == "1":
                    image_rect = self.dirt.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.dirt, image_rect)
                    self.tile_list.append(tile)

                if col == "2":
                    image_rect = self.grass.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.grass, image_rect)
                    self.tile_list.append(tile)

                if col == "W":
                    image_rect = self.invwall.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.invwall, image_rect)
                    self.tile_list.append(tile)

                if col == "D":
                    image_rect = self.door.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.door, image_rect, 1)
                    self.tile_list.append(tile)

    def update(self, display):
        for tile in self.tile_list:
            display.blit(tile[0], tile[1])

    def get_layout(self):
        return self.tile_list

    def images(self):
        inviswall = SpriteSheet("Assets/invisible wall colors.png")
        base_sheet = SpriteSheet("Assets/OpenGunnerStarterTiles.png")
        sheet1 = SpriteSheet("Assets/OpenGunnerForestTiles.png")

        dirt = sheet1.image_at((77, 255, 50, 50))
        self.dirt = pygame.transform.scale(dirt, (TILE_SIZE, TILE_SIZE))

        grass = sheet1.image_at((77, 201, 50, 50))
        self.grass = pygame.transform.scale(grass, (TILE_SIZE, TILE_SIZE))

        invwall = inviswall.image_at((0, 0, 50, 50))
        self.invwall = pygame.transform.scale(invwall, (TILE_SIZE, TILE_SIZE))

        door = base_sheet.image_at((448, 581, 50, 54))
        self.door = pygame.transform.scale(door, (TILE_SIZE * 2, TILE_SIZE * 2))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size, tile_set):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        self.tile_set = tile_set
        self.images()
        self.image = self.stand_r
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last = pygame.time.get_ticks()
        self.image_delay = 100
        self.current_frame = 0
        self.right = True
        self.left = False
        self.jumping = False
        self.falling = False
        self.velo_y = 0
        self.camera_shift = 0
        self.jumpspeed = 0
        self.dx = 0

    def camera(self):
        left_edge = DISPLAY_WIDTH // 4
        right_edge = DISPLAY_WIDTH - left_edge
        if self.rect.left <= left_edge and self.left:
            self.camera_shift = 4
            self.rect.left = left_edge
            self.dx = 0
        elif self.rect.right >= right_edge and self.right:
            self.camera_shift = -4
            self.rect.right = right_edge
            self.dx = 0
        else:
            self.camera_shift = 0

        for tile in self.tile_set:
            tile[1].x += self.camera_shift

    def movement(self):
        self.dx = 0
        dy = 0

        # left and right movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.left = False
            self.right = True
            self.camera()
            self.dx = 4
            now = pygame.time.get_ticks()
            if now - self.last >= self.image_delay:
                self.last = now
                self.current_frame = (self.current_frame + 1) % len(self.run_rt)
                self.image = self.run_rt[self.current_frame]

        elif keys[pygame.K_a]:
            self.left = True
            self.right = False
            self.camera()
            self.dx = -4
            now = pygame.time.get_ticks()
            if now - self.last >= self.image_delay:
                self.last = now
                self.current_frame = (self.current_frame + 1) % len(self.run_lft)
                self.image = self.run_lft[self.current_frame]

        else:
            self.current_frame = 0
            self.dx = 0
            if self.right:
                self.image = self.stand_r
            elif self.left:
                self.image = self.stand_l

        if self.jumping or self.falling:
            if self.right:
                self.image = self.jump_r
            elif self.left:
                self.image = self.jump_l
            else:
                if self.right:
                    self.image = self.stand_r
                elif self.left:
                    self.image = self.stand_l

        # jumping
        if keys[pygame.K_SPACE] and not self.falling:
            self.jumping = True
            self.jumpspeed -= 3
            dy += self.jumpspeed

        if not keys[pygame.K_SPACE]:
            self.falling = True

        if self.jumpspeed < -11:
            self.jumping = False
            self.falling = True
            dy += self.jumpspeed

        # gravity
        self.jumpspeed += 1
        if self.jumpspeed > 10:
            self.jumpspeed = 10
        dy = self.jumpspeed

        # collision
        for tile in self.tile_set:
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y,
                                   self.rect.width, self.rect.height):
                self.dx = 0
                self.camera_shift = 0
                if self.right:
                    self.rect.x -= 1
                elif self.left:
                    self.rect.x += 1
            if tile[1].colliderect(self.rect.x, self.rect.y + dy,
                                   self.rect.width, self.rect.height):
                if dy < 0:
                    dy = tile[1].bottom - self.rect.top
                elif dy > 0:
                    dy = tile[1].top - self.rect.bottom
                    self.falling = False

        # update position
        self.rect.x += self.dx
        self.rect.y += dy

    def update(self, display):
        self.movement()
        # draw to screen
        display.blit(self.image, self.rect)

    def images(self):
        tile_sheet = SpriteSheet("Assets/OpenGunnerHeroVer2.png")

        self.stand_r = tile_sheet.image_at((24, 143, 50, 50), -1)
        self.stand_l = tile_sheet.image_at((24, 200, 50, 50), -1)

        self.jump_r = tile_sheet.image_at((126, 143, 50, 50), -1)
        self.jump_l = tile_sheet.image_at((126, 200, 50, 50), -1)

        self.run_rt = []
        self.run_lft = []

        rt1 = tile_sheet.image_at((24, 315, 50, 50), -1)
        self.run_rt.append(rt1)
        rt2 = tile_sheet.image_at((75, 315, 50, 50), -1)
        self.run_rt.append(rt2)
        rt3 = tile_sheet.image_at((126, 315, 50, 50), -1)
        self.run_rt.append(rt3)
        rt4 = tile_sheet.image_at((177, 315, 50, 50), -1)
        self.run_rt.append(rt4)
        rt5 = tile_sheet.image_at((228, 315, 50, 50), -1)
        self.run_rt.append(rt5)
        rt6 = tile_sheet.image_at((279, 315, 50, 50), -1)
        self.run_rt.append(rt6)
        rt7 = tile_sheet.image_at((330, 315, 50, 50), -1)
        self.run_rt.append(rt7)
        rt8 = tile_sheet.image_at((381, 315, 50, 50), -1)
        self.run_rt.append(rt8)

        lft1 = tile_sheet.image_at((24, 375, 50, 50), -1)
        self.run_lft.append(lft1)
        lft2 = tile_sheet.image_at((75, 375, 50, 50), -1)
        self.run_lft.append(lft2)
        lft3 = tile_sheet.image_at((126, 375, 50, 50), -1)
        self.run_lft.append(lft3)
        lft4 = tile_sheet.image_at((177, 375, 50, 50), -1)
        self.run_lft.append(lft4)
        lft5 = tile_sheet.image_at((228, 375, 50, 50), -1)
        self.run_lft.append(lft5)
        lft6 = tile_sheet.image_at((279, 375, 50, 50), -1)
        self.run_lft.append(lft6)
        lft7 = tile_sheet.image_at((330, 375, 50, 50), -1)
        self.run_lft.append(lft7)
        lft8 = tile_sheet.image_at((381, 375, 50, 50), -1)
        self.run_lft.append(lft8)
