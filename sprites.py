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
        self.enemies = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.stopper = pygame.sprite.Group()
        self.trunk_group = pygame.sprite.Group()

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
                    image_rect = self.grass_top.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.grass_top, image_rect)
                    self.tile_list.append(tile)

                if col == "3":
                    image_rect = self.grass_l_c.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.grass_l_c, image_rect)
                    self.tile_list.append(tile)

                if col == "4":
                    image_rect = self.grass_r_c.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.grass_r_c, image_rect)
                    self.tile_list.append(tile)

                if col == "L":
                    image_rect = self.grass_l.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.grass_l, image_rect)
                    self.tile_list.append(tile)

                if col == "R":
                    image_rect = self.grass_r.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.grass_r, image_rect)
                    self.tile_list.append(tile)

                if col == "W":
                    image_rect = self.invwall.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.invwall, image_rect)
                    self.tile_list.append(tile)

                if col == "U":
                    image_rect = self.blue_up.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.blue_up, image_rect)
                    self.tile_list.append(tile)

                if col == "J":
                    image_rect = self.base_tile.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.base_tile, image_rect)
                    self.tile_list.append(tile)

                if col == "I":
                    image_rect = self.blue_up_r.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.blue_up_r, image_rect)
                    self.tile_list.append(tile)

                if col == "K":
                    image_rect = self.blue_r.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.blue_r, image_rect)
                    self.tile_list.append(tile)

                if col == "H":
                    image_rect = self.blue_l.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.blue_l, image_rect)
                    self.tile_list.append(tile)

                if col == "Y":
                    image_rect = self.blue_up_l.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.blue_up_l, image_rect)
                    self.tile_list.append(tile)

                if col == "B":
                    image_rect = self.tree_branch.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.tree_branch, image_rect)
                    self.tile_list.append(tile)

                if col == "N":
                    image_rect = self.branch_r.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.branch_r, image_rect)
                    self.tile_list.append(tile)

                if col == "V":
                    image_rect = self.branch_l.get_rect()
                    image_rect.x = x_val
                    image_rect.y = y_val
                    tile = (self.branch_l, image_rect)
                    self.tile_list.append(tile)

                if col == "T":
                    self.trunk = TreeTrunk(x_val, y_val)
                    self.trunk_group.add(self.trunk)

                if col == "D":
                    self.door = Door(x_val, y_val)
                    self.door_group.add(self.door)

                if col == "9":
                    self.stop = LeftStop(x_val, y_val)
                    self.stopper.add(self.stop)

                if col == "E":
                    self.enemy = EnemySold(x_val, y_val)
                    self.enemies.add(self.enemy)

    def update(self, display):
        for tile in self.tile_list:
            display.blit(tile[0], tile[1])
        for enemy in self.enemies:
            enemy.update(display)
        for door in self.door_group:
            door.update(display)
        for stop in self.stopper:
            stop.update(display)
        for trunk in self.trunk_group:
            trunk.update(display)

    def get_layout(self):
        return self.tile_list

    def images(self):
        inviswall = SpriteSheet("Assets/invisible wall colors.png")
        base_sheet = SpriteSheet("Assets/OpenGunnerStarterTiles.png")
        sheet1 = SpriteSheet("Assets/OpenGunnerForestTiles.png")

        # inside

        base_tile = base_sheet.image_at((75, 260, 50, 50))
        self.base_tile = pygame.transform.scale(base_tile, (TILE_SIZE, TILE_SIZE))

        blue_up = base_sheet.image_at((75, 206, 50, 50))
        self.blue_up = pygame.transform.scale(blue_up, (TILE_SIZE, TILE_SIZE))

        blue_up_r = base_sheet.image_at((129, 206, 50, 50))
        self.blue_up_r = pygame.transform.scale(blue_up_r, (TILE_SIZE, TILE_SIZE))

        blue_up_l = base_sheet.image_at((21, 206, 50, 50))
        self.blue_up_l = pygame.transform.scale(blue_up_l, (TILE_SIZE, TILE_SIZE))

        blue_r = base_sheet.image_at((129, 260, 50, 50))
        self.blue_r = pygame.transform.scale(blue_r, (TILE_SIZE, TILE_SIZE))

        blue_l = base_sheet.image_at((21, 260, 50, 50))
        self.blue_l = pygame.transform.scale(blue_l, (TILE_SIZE, TILE_SIZE))

        # outside

        dirt = sheet1.image_at((77, 255, 50, 50))
        self.dirt = pygame.transform.scale(dirt, (TILE_SIZE, TILE_SIZE))

        grass_top = sheet1.image_at((77, 201, 50, 50))
        self.grass_top = pygame.transform.scale(grass_top, (TILE_SIZE, TILE_SIZE))

        grass_l = sheet1.image_at((23, 255, 50, 50))
        self.grass_l = pygame.transform.scale(grass_l, (TILE_SIZE, TILE_SIZE))

        grass_r = sheet1.image_at((131, 255, 50, 50))
        self.grass_r = pygame.transform.scale(grass_r, (TILE_SIZE, TILE_SIZE))

        grass_r_c = sheet1.image_at((131, 201, 50, 50))
        self.grass_r_c = pygame.transform.scale(grass_r_c, (TILE_SIZE, TILE_SIZE))

        grass_l_c = sheet1.image_at((23, 201, 50, 50))
        self.grass_l_c = pygame.transform.scale(grass_l_c, (TILE_SIZE, TILE_SIZE))

        tree_branch = sheet1.image_at((1035, 297, 50, 24))
        self.tree_branch = pygame.transform.scale(tree_branch, (TILE_SIZE * 2, TILE_SIZE))

        branch_l = sheet1.image_at((1157, 297, 40, 24), -1)
        self.branch_l = pygame.transform.scale(branch_l, (TILE_SIZE, TILE_SIZE))

        self.branch_r = pygame.transform.flip(self.branch_l, True, False)

        invwall = inviswall.image_at((0, 0, 50, 50))
        self.invwall = pygame.transform.scale(invwall, (TILE_SIZE, TILE_SIZE))


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images()

        current_frame = 0
        card = False

        self.image = self.closed_door
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, display):
        display.blit(self.image, self.rect)

    def images(self):
        base_sheet = SpriteSheet("Assets/OpenGunnerStarterTiles.png")

        closed_door = base_sheet.image_at((24, 642, 50, 54))
        self.closed_door = pygame.transform.scale(closed_door, (TILE_SIZE * 2, TILE_SIZE * 2))


class LeftStop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        inviswall = SpriteSheet("Assets/invisible wall colors.png")
        stopper = inviswall.image_at((0, 0, 50, 50))
        self.stopper = pygame.transform.scale(stopper, (TILE_SIZE, TILE_SIZE))

        self.image = self.stopper
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, display):
        display.blit(self.image, self.rect)


class TreeTrunk(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        sheet1 = SpriteSheet("Assets/OpenGunnerForestTiles.png")
        tree_trunk = sheet1.image_at((646, 228, 44, 50))
        self.tree_trunk = pygame.transform.scale(tree_trunk, (TILE_SIZE * 2, TILE_SIZE * 2))
        self.image = self.tree_trunk
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, display):
        display.blit(self.image, self.rect)


class EnemyShoot(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, e_center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(BULLET_COLOR)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.e_center = e_center
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y, BULLET_WIDTH, BULLET_HEIGHT])

        self.x_velo = 12

    def directional(self):
        if self.rect.x > self.e_center:
            self.rect.x += self.x_velo
        if self.rect.x < self.e_center:
            self.rect.x -= self.x_velo

    def update(self):
        self.directional()


class EnemySold(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.images()
        self.image = self.e_idle_r
        self.rect = self.image.get_rect()
        self.image_delay = 100
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False
        self.last = pygame.time.get_ticks()
        self.current_frame = 0
        self.firing_timer = 0
        self.enemy_walk = 0
        self.enemy_bullet_group = pygame.sprite.Group()

    def enemy_firing(self):
        self.firing_timer += 1

        if self.firing_timer == 90:
            if self.left:
                bullet = EnemyShoot(self.rect.centerx - 16,
                               self.rect.top + 17, BULLET_WIDTH, BULLET_HEIGHT, self.rect.centerx)
                self.enemy_bullet_group.add(bullet)
            if self.right:
                bullet = EnemyShoot(self.rect.centerx + 12,
                                    self.rect.top + 17, BULLET_WIDTH, BULLET_HEIGHT, self.rect.centerx)
                self.enemy_bullet_group.add(bullet)
        if self.firing_timer == 130:
            self.enemy_bullet_group.empty()
            self.firing_timer = 0

    def enemy_movement(self):
        self.current_frame += 1

        if self.current_frame >= 1:
            self.right = True
            self.left = False

        if self.current_frame >= 120:
            self.left = True
            self.right = False

        if self.current_frame >= 240:
            self.current_frame = 0

        if self.right:
            self.rect.x += 1
            now = pygame.time.get_ticks()
            if now - self.last >= self.image_delay:
                self.last = now
                self.enemy_walk = (self.enemy_walk + 1) % len(self.run_rt)
                self.image = self.run_rt[self.enemy_walk]

        elif self.left:
            self.rect.x += -1
            now = pygame.time.get_ticks()
            if now - self.last >= self.image_delay:
                self.last = now
                self.enemy_walk = (self.enemy_walk + 1) % len(self.run_lft)
                self.image = self.run_lft[self.enemy_walk]

    def update(self, display):
        display.blit(self.image, self.rect)
        self.enemy_movement()
        self.enemy_firing()
        self.enemy_bullet_group.update()
        self.enemy_bullet_group.draw(display)

    def images(self):
        tile_sheet = SpriteSheet("Assets/OpenGunnerEnemySoldier.png")

        self.e_idle_r = tile_sheet.image_at((24, 129, 50, 50), -1)
        self.e_idle_l = tile_sheet.image_at((24, 186, 50, 50), -1)

        self.dmgr = tile_sheet.image_at((202, 129, 50, 50), -1)
        self.dmgl = tile_sheet.image_at((202, 186, 50, 50), -1)

        self.run_rt = []
        self.run_lft = []

        rr1 = tile_sheet.image_at((24, 286, 50, 50), -1)
        self.run_rt.append(rr1)
        rr2 = tile_sheet.image_at((75, 286, 50, 50), -1)
        self.run_rt.append(rr2)
        rr3 = tile_sheet.image_at((126, 286, 50, 50), -1)
        self.run_rt.append(rr3)
        rr4 = tile_sheet.image_at((177, 286, 50, 50), -1)
        self.run_rt.append(rr4)
        rr5 = tile_sheet.image_at((228, 286, 50, 50), -1)
        self.run_rt.append(rr5)
        rr6 = tile_sheet.image_at((279, 286, 50, 50), -1)
        self.run_rt.append(rr6)
        rr7 = tile_sheet.image_at((330, 286, 50, 50), -1)
        self.run_rt.append(rr7)
        rr8 = tile_sheet.image_at((381, 286, 50, 50), -1)
        self.run_rt.append(rr8)

        rl1 = tile_sheet.image_at((24, 346, 50, 50), -1)
        self.run_lft.append(rl1)
        rl2 = tile_sheet.image_at((75, 346, 50, 50), -1)
        self.run_lft.append(rl2)
        rl3 = tile_sheet.image_at((126, 346, 50, 50), -1)
        self.run_lft.append(rl3)
        rl4 = tile_sheet.image_at((177, 346, 50, 50), -1)
        self.run_lft.append(rl4)
        rl5 = tile_sheet.image_at((228, 346, 50, 50), -1)
        self.run_lft.append(rl5)
        rl6 = tile_sheet.image_at((279, 346, 50, 50), -1)
        self.run_lft.append(rl6)
        rl7 = tile_sheet.image_at((330, 346, 50, 50), -1)
        self.run_lft.append(rl7)
        rl8 = tile_sheet.image_at((381, 346, 50, 50), -1)
        self.run_lft.append(rl8)


class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        sheet = SpriteSheet("Assets/OpenGunnerBarsAndPanels.png")

        heart = sheet.image_at((349, 391, 9, 9), -1)
        self.heart = pygame.transform.scale(heart, (TILE_SIZE * 1.25, TILE_SIZE * 1.25))

        empty_heart = sheet.image_at((360, 391, 9, 9), -1)
        self.empty_heart = pygame.transform.scale(empty_heart, (TILE_SIZE * 1.25, TILE_SIZE * 1.25))

        self.image = self.heart
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, display):
        display.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size, tile_set, enemies, door, stop, trees):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = tile_size
        self.tile_set = tile_set
        self.enemies = enemies
        self.door = door
        self.stop = stop
        self.trees = trees
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
        for enemy in self.enemies:
            enemy.rect.x += self.camera_shift
        for door in self.door:
            door.rect.x += self.camera_shift
        for stop in self.stop:
            stop.rect.x += self.camera_shift
        for trunk in self.trees:
            trunk.rect.x += self.camera_shift

    def movement(self):
        self.dx = 0
        dy = 0

        # left and right movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.left = False
            self.right = True
            # right camera stopper
            for door in self.door:
                if door.rect.right + 22 > 800:
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
            # left camera stopper
            for stop in self.stop:
                if stop.rect.x - 25 < 0:
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
