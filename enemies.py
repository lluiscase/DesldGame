import pygame
import defaults
import player
import random
#list_enemies=[]
#Enemies - type,life,hit,collision,speed,size

class Enemie():
    def __init__(self,x,y):
        self.life = 3
        self.size = 25
        self.hit = 1
        self.type = None
        self.speed = 1.5
        self.position = pygame.Vector2(x,y)
        self.sprite_enemie()
        self.move()
    def sprite_enemie(self):
        square=[
        (self.position.x,self.position.y),
        (self.position.x + self.size,self.position.y + self.size),
        (self.position.x + self.size, self.position.y),
        (self.position.x, self.position.y +self.size),
        ]
        pygame.draw.polygon(defaults.screen, "green", square, self.size)
    def move(self):
        dx = player.initial_pos.x - self.position.x
        dy = player.initial_pos.y - self.position.y
        dist = (dx ** 2 + dy ** 2) ** .5 + 1
        x_vel = dx / dist * self.speed
        y_vel = dy / dist * self.speed

        self.position.x += x_vel
        self.position.y += y_vel
        
def generate_enemies():
    x = random.randint(1, defaults.screen.get_width())
    y = random.randint(1, defaults.screen.get_height())
    new_enemie = Enemie(x,y)
    return new_enemie
#def hit():