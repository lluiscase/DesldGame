import pygame
import defaults
import player
#list_enemies=[]
#Enemies - type,life,hit,collision,speed,size

class Enemie():
    def __init__(self):
        self.life = 3
        self.size = 25
        self.hit = 1
        self.type = None
        self.speed = 5
        self.position = pygame.Vector2(defaults.screen.get_width() / 4 ,defaults.screen.get_height() / 4)
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
        dist = max(1, (dx**2 + dy**2) ** 0.5)
        self.position.x += self.speed - dx /dist
        self.position.y += self.speed - dy /dist
        
#def generate_enemies():
#def hit():