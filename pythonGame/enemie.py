import pygame, math

class Enemie:
    def __init__(self,ecran,x,y,direction,vit,couleur):
        self.x = x
        self.y = y
        self.vit = vit
        self.dir = direction
        self.ecran = ecran
        self.couleur = couleur

    def Draw(self):
        pygame.draw.circle(self.ecran, self.couleur, (self.x,self.y), 20)
    def Update(self,deltatime):
        if self.dir == "right":
            self.x += deltatime* self.vit
        elif self.dir == "left":
            self.x -= deltatime* self.vit
        self.y += deltatime* 300

    def Collision(self,player):
        if math.sqrt((player.x-self.x)**2+(player.y - self.y)**2) <= 40:
            pygame.quit()