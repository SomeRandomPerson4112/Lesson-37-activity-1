import math
import pygame
import random
screen_width=800
screen_height=500
player_x_start=370
player_y_start=380
enemy_start_min=50
enemy_start_max=150
enemy_speedx=4
enemy_speedy=40
bullet_speed=10
collision_distance=27
pygame.init()
pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerIMG=pygame.image.load("rocket.png")
player_x=player_x_start
player_y=player_y_start
playerx_change=0
enemyIMG=[]
enemy_y=[]
enemy_x=[]
enemy_x_change=[]
enemy_y_change=[]
num_of_enemy=6
for _i in range(num_of_enemy):
    enemyIMG.append(pygame.image.load("enemy.png"))
    enemy_y.append(random.randint(enemy_start_min,enemy_start_max))
    enemy_x.append(random.randint(0,screen_width-64))
    enemy_x_change.append(enemy_speedx)
    enemy_y_change.append(enemy_speedy)
bulletIMG=pygame.image.load("bullet.png")
bullet_x=0
bullet_y=player_y_start
bullet_x_change=0
bullet_y_change=bullet_speed
