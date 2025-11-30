import pygame
import defaults
import random
#list_enemies=[]
#Enemies - type,life,hit,collision,speed,size

class Enemie():
    def __init__(self,x,y):
        self.size = 125
        self.type = None

        self.position = pygame.Rect(x,y,self.size,self.size)

        self.sprite = pygame.image.load("./img/Zombie de fungo.png")
        self.sprite = pygame.transform.scale(self.sprite,(self.size, self.size))

    def sprite_enemie(self):
        defaults.screen.blit(self.sprite,(self.position.x,self.position.y))
        
def generate_enemies():
    x = random.randint(1, defaults.screen.get_width())
    y = random.randint(1, defaults.screen.get_height())
    new_enemie = Enemie(x,y)
    return new_enemie
#def hit():