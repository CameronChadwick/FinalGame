import pygame
import sprites
from settings import *

# base elements
pygame.init()
pygame.display.set_caption("Game")

game_layout = sprites.Layout(LAYOUT)
layout_list = game_layout.get_layout()

player_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()


player = sprites.Player(225, 500, 25, layout_list, game_layout.enemies)
player_group.add(player)


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


def reset_level(new_level):
    global player, player_group, game_layout, layout_list
    # empty groups
    player_group.empty()
    game_layout.enemies.empty()
    player_bullet_group.empty()

    # create level
    game_layout.create(new_level)
    layout_list = game_layout.get_layout()
    player_group = pygame.sprite.Group()
    player = sprites.Player(800, 500, 25, layout_list, game_layout.enemies)
    player_group.add(player)

    return layout_list


def game_play():

    level = 1
    max_level = 2
    enemy_health = 3

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
            enemy_health -= 1

            if enemy_health <= 0:
                game_layout.enemy.kill()


            # door collision
        for tile in layout_lis:
            if tile[1].colliderect(player.rect.x + 3, player.rect.y,
                                   player.rect.width, player.rect.height) and len(tile) == 3:
                level += 1

                if level <= max_level:

                    layout_lis = reset_level(level)

                else:
                    running = False

        screen.fill(DARK_BLUE)

        player_group.update(screen)
        game_layout.update(screen)
        player_bullet_group.update()
        player_bullet_group.draw(screen)

        pygame.display.flip()

    pygame.quit()


playing = True
while playing:
    game_play()

pygame.quit()
