import pygame
import random
import os

W = 800
H = 600
SILVER = (192, 192, 192)
WHITE = (255, 255, 255)
run = True
w = 380
h = 180
k = 40 

pygame.init()
pygame.display.set_caption('Текст ')
screen = pygame.display.set_mode((W, H))
screen.fill((0, 0, 255))

font = pygame.font.SysFont('Arial', 36, True, False)
font2 = pygame.font.SysFont('Arial', 18, False, True)


text1 = font.render("Все привет ", 1, WHITE)
text2 = font2.render('Задание на урок ', 1, (220, 220, 0))

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
    screen.blit(text1, (300, 240))
    screen.blit(text2, (300, 280))
    pygame.draw.rect(screen, (0, 0, 255), (w, h, k, 40))
    w += 0.05
    if w > W:
        w = -k
    pygame.draw.rect(screen, (255, 0, 0), (w, h, k, 40))
    pygame.display.update()
