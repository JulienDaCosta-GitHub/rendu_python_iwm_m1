import pygame
class Perso:
    def __init__(self,ecran):
        self.x = 50
        self.y = 600
        self.vit = 300
        self.ecran = ecran
        self.canjump = True
        self.sautForce = 0
        self.maxSautForce = 500

    def Draw(self):
        pygame.draw.circle(self.ecran, ( 0, 0, 255), (self.x, self.y), 20)
    def Update(self,deltatime):
        if pygame.key.get_pressed()[pygame.K_d]:
                self.x += deltatime * self.vit
        if pygame.key.get_pressed()[pygame.K_q]:
                self.x += -deltatime * self.vit
        self.y += deltatime* 200
        self.jump(deltatime)

    def jump(self,deltatime):
        self.y -= deltatime* self.sautForce
        self.sautForce -= deltatime * 400
        if self.sautForce< 0 : self.sautForce = 0