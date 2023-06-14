import pygame
import sys
import random
from pygame import*
from pygame import mixer

pygame.init()
mixer.init()

size = (800,700)

score_point = 0
health_point = 100

screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("Arial", 50)

Score_text = font.render("SCORE:"+str(score_point), True, (0, 255, 0))

x1 = 260
y1 = 590

bx = 260
by = 600

bg_pic = pygame.image.load("bg2.jpg")
ship = pygame.image.load("spaceship.png")
bullet = pygame.image.load("bullet.png")
pygame.display.set_caption("SPACE İNVADERS")
clock = pygame.time.Clock()

class Enemy:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.speed = random.randrange(2,4)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += self.speed
        
        if self.x <= 0 or self.x >= 720:
            self.speed *= -1
            self.y += 25

enemy_images = ["enemy1.png" , "enemy2.png" , "enemy3.png"]

enemies = []

for i in range(5):
    x = random.randrange(0,550,50)
    y = random.randrange(50,250,50)
    image = random.choice(enemy_images)
    enemy = Enemy(x, y, image)
    enemies.append(enemy)

move_BOOL = 0
FİRE_İNFO = False

game_music = "gamesong.mp3"
mixer.music.load(game_music)
mixer.music.play()

while True:

    by -= (5 * move_BOOL)
    
    clock.tick(144)
    screen.fill((0,0,0))
    screen.blit(bg_pic,(0,0))
    screen.blit(Score_text,(0,0))

    if by < -40:
        by = 600
        move_BOOL = 0
        bx = x1
        FİRE_İNFO = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_BOOL = 1
                FİRE_İNFO = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        x1 += 3
        if FİRE_İNFO == False:
            bx = x1
        if x1 > 710:
            x1 = 710

    if keys[pygame.K_a]:
        x1 -= 3
        if FİRE_İNFO == False:
            bx = x1
        if x1 < 0:
            x1 = 0

    screen.blit(ship,(x1,y1))
    screen.blit(bullet,(bx,by))

    for enemy in enemies:
        enemy.update()
        enemy_x = enemy.x
        enemy_y = enemy.y
        enemy.draw(screen)
        if by == enemy_y:
            if  (enemy_x - 40) < bx < (enemy_x + 40):
                KS = mixer.Sound("explotion.wav")
                KS.play()
                enemies.remove(enemy)
                score_point += 10
                Score_text = font.render("SCORE:"+str(score_point), True, (0, 255, 0))
                x = random.randrange(0, 550, 50)
                y = random.randrange(50, 250, 50)
                image = random.choice(enemy_images)
                enemy = Enemy(x, y, image)
                enemies.append(enemy)

                
    pygame.display.update()
