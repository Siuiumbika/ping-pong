import pygame

win_x, win_y = 700, 500
win = pygame.display.set_mode((win_x, win_y))
clock = pygame.time.Clock()
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    win.fill((250, 10, 100))
    pygame.display.update()
    clock.tick(60)