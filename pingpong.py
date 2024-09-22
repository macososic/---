from pygame import *
from random import randint
 
 
WIDTH = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 10
RESTART_TIME = 3000
 
BACKGROUND = (randint(0, 255), randint(0, 255), randint(0, 255))
WHITE = (255, 255, 255)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
 
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("PING-PONG")
clock = time.Clock()
 
class GameSprite(sprite.Sprite):
    def __init__(self, img: str, x: int, y: int, w: int, h: int):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
run = True
finish = False
 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
 
    if not finish:
        window.fill(BACKGROUND)
 
    display.update()
    clock.tick(FPS)