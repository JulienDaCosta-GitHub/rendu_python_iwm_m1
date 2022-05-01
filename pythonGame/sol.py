import pygame
from player import Perso
from enemie import Enemie
class Sol:
    def __init__(self,ecran,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ecran = ecran

    def Draw(self):
        pygame.draw.rect(self.ecran, (80, 150, 0), pygame.Rect(self.x, self.y, self.width, self.height))

    def Collision(self, player):
        if self.y <= player.y +20 and player.x +20 >= self.x:
            if player.x-20 <= self.x+self.width and player.y-20 <= self.y+self.height:

                x = self.x + self.width/2
                y = self.y + self.height/2

                if player.y>self.y and player.y<self.y+self.height:
                    if player.x < x:
                        player.x = self.x - 20
                        if type(player) == Enemie:
                            player.dir = 'left'
                    if player.x > x:
                        if type(player) == Enemie:
                            player.dir = 'right'
                        player.x = self.x+self.width+20
                if player.x>self.x and player.x<self.x+self.width:
                    if player.y < y:
                        player.y = self.y - 20
                        if type(player) == Perso:
                            player.canjump = True
                    if player.y > y:
                        player.y = self.y + 20
