import pygame

GREEN = (50, 150, 50)
BLUE = (50, 50, 150)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, speed, wight, height):
        super().__init__()
        self.image = pygame.Surface((wight, height)) #вместе 55,55 - параметры
        self.image.fill(color=color)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_UP] and self.rect.y > 4:
           self.rect.y -= self.speed
       if keys[pygame.K_DOWN] and self.rect.y < win_y - self.rect.height:
           self.rect.y += self.speed
class Player2(GameSprite):
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_s] and self.rect.y < win_y - self.rect.height:
           self.rect.y += self.speed

win_x, win_y = 700, 500
win = pygame.display.set_mode((win_x, win_y))

clock = pygame.time.Clock()

racket2 = Player2(color=GREEN, x=15, y=200, speed=4, wight=25, height=150) 
racket1 = Player1(BLUE, win_x - 40, 200, 4, 25, 150)

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    win.fill((250, 10, 100))
    racket1.update()
    racket2.update()
    racket1.reset()
    racket2.reset()
    pygame.display.update()
    clock.tick(60)