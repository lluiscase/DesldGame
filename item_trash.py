import pygame
import defaults
import random
import time
enemies_list = []
start = time.time()
interval = 2
class Enemie():
    def __init__(self,x,y):
        self.size = 125
        self.type = None
        self.transf = False
        self.position = pygame.Rect(x,y,self.size,self.size)

        self.sprite = pygame.image.load("./img/Zombie de fungo.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite,(self.size, self.size))

    def sprite_enemie(self):
        defaults.screen.blit(self.sprite,self.position)
        
def generate_enemies():
    x = random.randint(1, defaults.screen.get_width())
    y = random.randint(1, defaults.screen.get_height())
    new_enemie = Enemie(x,y)
    return new_enemie

def spawn():
    global start
    elapsed = time.time() - start 
    if elapsed > interval:
        new = generate_enemies()
        enemies_list.append(new)
        start = time.time()
#def hit():