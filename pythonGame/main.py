import pygame
import random
from player import Perso
from enemie import Enemie
from sol import Sol
pygame.init()

ecran = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Survival")
p = Perso(ecran)
soList = []
enemies = []
# sol
soList.append(Sol(ecran,0,800,1000,900))
# mur droite
soList.append(Sol(ecran,950,00,50,1000))
# mur millieu
soList.append(Sol(ecran,random.randint(0,1000),750,50,60))
# mur gauche
soList.append(Sol(ecran,0,00,50,1000))
for i in range(6):
    soList.append(Sol(ecran,random.randint(0, 1000), random.randint(200,700), 120, 30))
for i in range(1):
    enemies.append(Enemie(ecran,random.randint(0, 1000), 0,"right"))
loop = True
getTicksLastFrame = 0
timerEnemie = 0
while loop:

    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    timerEnemie -= deltaTime
    if timerEnemie<=0:
        timerEnemie = 4
        enemies.append(Enemie(ecran,random.randint(0, 1000), 0, "right"))

    p.Update(deltaTime)
    for en in enemies:
        en.Update(deltaTime)
    for sol in soList:
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
        if event.type == pygame.QUIT:
            loop = False
    ecran.fill((0, 225, 255))

    for sol in soList:
        sol.Draw()
    p.Draw()

    for en in enemies:
        en.Draw()

    pygame.display.flip()

pygame.quit()