from pygame import *
from pygame import sprite
from random import randint
import random

font.init()

lost = 0
FPS = 30
speed_x = 5
speed_y = 5
win_height = 500
win_width = 700
clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('window.jpg'), (700, 500))
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)
font3 = font.Font(None, 50)
font4 = font.Font(None, 50)

class GameSprite(sprite.Sprite):
    def __init__(self, imag, speed, x, y, width, length):
        super().__init__()
        self.image = transform.scale(image.load(imag), (width, length))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 635:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_z] and self.rect.y < 635:
            self.rect.y += self.speed
        if keys_pressed[K_x] and self.rect.y > 0:
            self.rect.y -= self.speed
class Ball(GameSprite):
    pass

lost = 0
plat = Player('plat.jpg', 8, 25, 250, 20, 100)
plat2 = Player('plat.jpg', 8, 650, 250, 20, 100)
ball = Ball('ball1.png', 5, 350, 250, 40, 40)

text_player1 = font1.render('Player 1 win!! ', 100, (255, 255, 0))
text_player2 = font2.render('Player 2 win!! ', 100, (250, 0, 0))

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        text_plat1 = font3.render('Player 1', 100, (0, 0, 0))
        text_plat2 = font4.render('Player 2', 100, (0, 0, 0))

        window.blit(background, (0, 0))
        window.blit(text_plat1, (90, 10))
        window.blit(text_plat2, (470, 10))

        plat.update()
        plat.reset()

        plat2.update2()
        plat2.reset()

        ball.update()
        ball.reset()

        if ball.rect.y > win_height -50:
            speed_y *= -1

        if ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > win_width -10:
            finish = True
            window.blit(text_player1, (270,200))

        if ball.rect.x < -50:
            finish = True
            window.blit(text_player2, (270,200))

     
        if sprite.collide_rect(ball, plat2):
            speed_x *= -1
        
        if sprite.collide_rect(ball, plat):
            speed_x *= -1

    display.update()
    clock.tick(FPS)