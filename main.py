import pygame
import sprites
from settings import *

# base elements
pygame.init()
pygame.display.set_caption("Game")

game_layout = sprites.Layout(LAYOUT)
layout_list = game_layout.get_layout()

player_group = pygame.sprite.Group()
heart_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()


player = sprites.Player(225, 500, 25, layout_list, game_layout.enemies, game_layout.door_group,
                        game_layout.stopper, game_layout.trunk_group, game_layout.key_group)
player_group.add(player)

heart1 = sprites.Heart(25, 25)
heart_group.add(heart1)

heart2 = sprites.Heart(70, 25)
heart_group.add(heart2)

heart3 = sprites.Heart(115, 25)
heart_group.add(heart3)

SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)


class Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(BULLET_COLOR)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y, BULLET_WIDTH, BULLET_HEIGHT])

        self.x_velo = 12

    def directional_firing(self):
        if self.rect.x > player.rect.centerx:
            self.rect.x += self.x_velo
        if self.rect.x < player.rect.centerx:
            self.rect.x -= self.x_velo

    def update(self):
        self.directional_firing()


# def start_screen():
#     screen = pygame.display.set_mode(SIZE)
#     pygame.display.set_caption("Space Invaders")
#
#     clock = pygame.time.Clock()
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     running = False
#
#     screen.fill(BLACK)
#     pygame.display.flip()
#
#     clock.tick(FPS)


# def game_over():
#     screen = pygame.display.set_mode(SIZE)
#     pygame.display.set_caption("Space Invaders")
#
#     clock = pygame.time.Clock()
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     return False
#                 if event.key == pygame.K_RETURN:
#                     return True
#
#     screen.fill(BLACK)
#     pygame.display.flip()
#
#     clock.tick(FPS)


def reset_level(new_level):
    global player, player_group, game_layout, layout_list
    # empty groups
    player_group.empty()
    game_layout.enemies.empty()
    game_layout.door_group.empty()
    game_layout.stopper.empty()
    game_layout.trunk_group.empty()
    player_bullet_group.empty()

    # create level
    game_layout.create(new_level)
    layout_list = game_layout.get_layout()
    player_group = pygame.sprite.Group()
    player = sprites.Player(225, 500, 25, layout_list, game_layout.enemies, game_layout.door_group,
                            game_layout.stopper, game_layout.trunk_group, game_layout.key_group)
    player_group.add(player)

    return layout_list


def play():

    level = 1
    max_level = 2
    door_open = False

    layout_lis = reset_level(level)

    running = True

    clock = pygame.time.Clock()

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_e:
                    if player.left:
                        bullet = Shoot(player.rect.centerx - 16,
                                       player.rect.top + 17, BULLET_WIDTH, BULLET_HEIGHT)
                        player_bullet_group.add(bullet)
                    if player.right:
                        bullet = Shoot(player.rect.centerx + 12,
                                       player.rect.top + 17, BULLET_WIDTH, BULLET_HEIGHT)
                        player_bullet_group.add(bullet)
            if event.type == pygame.QUIT:
                running = False

            # enemy damage
        enemy_shot = pygame.sprite.groupcollide(game_layout.enemies, player_bullet_group, False, True)

        if enemy_shot:
            game_layout.enemy.enemy_health -= 1

        if game_layout.enemy.enemy_health <= 0:
            game_layout.enemy.kill()

            # player damage
        player_shot = pygame.sprite.groupcollide(game_layout.enemy.enemy_bullet_group, player_group, True, False)

        if player_shot:
            player.player_health -= 1

        if player.player_health == 3:
            heart1.image = heart1.heart
            heart2.image = heart2.heart
            heart3.image = heart3.heart

        if player.player_health < 3:
            heart3.image = heart3.empty_heart

        if player.player_health < 2:
            heart2.image = heart2.empty_heart

        if player.player_health == 0:
            running = False

        if player.rect.y > 900:
            running = False

            # door collision
        key_collision = pygame.sprite.groupcollide(game_layout.key_group, player_group, True, False)

        if key_collision:
            game_layout.door.keygrabbed = True
            game_layout.door.image = game_layout.door.door_open

        door_collision = pygame.sprite.groupcollide(game_layout.door_group, player_group, False, False)

        if door_collision and game_layout.door.keygrabbed:
            level += 1

            if level <= max_level:

                layout_lis = reset_level(level)

            else:
                running = False


        screen.fill(DARK_BLUE)

        game_layout.update(screen)
        player_group.update(screen)
        heart_group.update(screen)
        player_bullet_group.update()
        player_bullet_group.draw(screen)

        pygame.display.flip()

    pygame.quit()


# start_screen()
playing = True
while True:
    play()
    # game_over()
