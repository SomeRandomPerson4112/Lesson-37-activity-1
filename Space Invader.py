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
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load("bg invader.png")
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
bullet_state="ready"
score_value=0
font=pygame.font.Font("freesansbold.ttf")
text_y=10
text_x=10
over_font=pygame.font.Font("freesansbold.ttf")
def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER ",True,(255,255,255))
    screen.blit(over_text(200,250))
def player(x,y):
    screen.blit(playerIMG,(x,y))
def enemy(x,y,i):
    screen.blit(enemyIMG[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletIMG,(x+16,y+10))
def isCollison(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return distance<collision_distance
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
for event in pygame.event.get():
    if event.type==pygame.QUIT:
        running=False
    if event.type==pygame.KEYDOWN:
        if event.type==pygame.K_LEFT:
            playerx_change=-5
        if event.type==pygame.K_RIGHT:
            playerx_change=5
        if event.type==pygame.K_SPACE and bullet_state=="ready":
            bullet_x=player_y
            fire_bullet(bullet_x,bullet_y)
    if event.type==pygame.KEYUP and event.key in pygame[pygame.K_LEFT,pygame.K_RIGHT]:
        playerx_change=0
player_x+=playerx_change
player_x=max(0,min(player_x,screen_width-64))
