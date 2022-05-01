import pygame
import random
from player import Perso
from enemie import Enemie
from sol import Sol
pygame.init()

clock = pygame.time.Clock()
ecran = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Survival")
p = Perso(ecran)

font = pygame.font.Font('freesansbold.ttf',32)
victory = font.render("VICTOIRE ! Tu as survécu !", True, (0, 0, 0))

counter, text = 25, '25'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font('freesansbold.ttf', 30)
showVictory = False

solList = []
enemies = []
solList.append(Sol(ecran,0,800,1000,900))
solList.append(Sol(ecran,950,00,50,1000))
solList.append(Sol(ecran,random.randint(0,1000),750,50,60))
solList.append(Sol(ecran,0,00,50,1000))
for i in range(6):
    solList.append(Sol(ecran,random.randint(0, 1000), random.randint(200,700), 120, 30))
for i in range(1):
    enemies.append(Enemie(ecran,random.randint(0, 1000), 0,"right", 50, (255, 0, 0)))
loop = True
getTicksLastFrame = 0
timerEnemie = 0

sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')

while loop:

    ecran.blit(bg_img, (0,0))
    ecran.blit(sun_img, (300,100))

    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    timerEnemie -= deltaTime
    if timerEnemie<=0:
        timerEnemie = 5
        enemies.append(Enemie(ecran,random.randint(0, 1000), 0, "right", 50, (255, 0, 0)))
        enemies.append(Enemie(ecran,random.randint(0, 1000), 0, "right", 100, (0, 0, 0)))

    p.Update(deltaTime)
    for en in enemies:
        en.Update(deltaTime)
    for sol in solList:
        sol.Collision(p)
        for en in enemies:
            sol.Collision(en)
    for en in enemies:
        en.Collision(p)
        en.Update(deltaTime)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                if p.canjump:
                    p.canjump = False
                    p.sautForce = p.maxSautForce
        if event.type == pygame.USEREVENT:
            if counter > 0:
                counter -= 1
                text = str(counter).rjust(3)
            else:
                showVictory = True
        if event.type == pygame.QUIT:
            loop = False
    else:
        ecran.blit(font.render(text, True, (0, 0, 0)), (500, 20))

    for sol in solList:
        sol.Draw()
    p.Draw()

    for en in enemies:
        en.Draw()

    if showVictory == True:
        ecran.fill((255,255,255))
        ecran.blit(victory, (300, 480))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()