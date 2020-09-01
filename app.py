import random
import pygame
pygame.init()
pygame.font.init()

from Block import *

width, height = 800, 600

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (0, 0, 0)
BLACK = (0, 0, 0)

scl = 50
rand = [False for i in range(9)]
rand.append(True)
blocks = [[Block(j, i, scl, random.choice(rand)) for j in range(width // scl)] for i in range(height // scl)]

for i in blocks:
    for j in i:
        j.init(blocks, width // scl, height // scl)

print(Block.sum)
must_opens = (width // scl) * (height // scl) - Block.sum
opens = 0
print(must_opens)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minespaper")

clock = pygame.time.Clock()
oyun_bitti = False
kazandin = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not oyun_bitti:
                if pygame.mouse.get_pressed()[0] == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in blocks:
                        for j in i:
                            if j.x < mouse_x < j.x + j.scl and j.y < mouse_y < j.y + j.scl:
                                if not j.flagged:
                                    if not j.open(blocks, width // scl, height // scl):
                                        oyun_bitti = True
                elif pygame.mouse.get_pressed()[2] == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in blocks:
                        for j in i:
                            if j.x < mouse_x < j.x + j.scl and j.y < mouse_y < j.y + j.scl:
                                if not j.flagged:
                                    j.flagged = True
                                else:
                                    j.flagged = False

    opens = 0
    for i in blocks:
        for j in i:
            if j.is_press:
                opens += 1
            j.show(window)

    if must_opens == opens:
        oyun_bitti = True
        kazandin = True

    for i in range(height // scl):
        pygame.draw.line(window, BLACK, (0, i * scl), (width, i * scl))
    for i in range(width // scl):
        pygame.draw.line(window, BLACK, (i * scl, 0), (i * scl, height))

    if oyun_bitti:
        for i in blocks:
            for j in i:
                j.is_press = True
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        if kazandin:
            textsurface = myfont.render('Yendin !', False, (255, 0, 0))
            window.blit(textsurface, (width // 3, height // 3))
        else:
            textsurface = myfont.render('Yenildin !', False, (255, 0, 0))
            window.blit(textsurface, (width // 3, height // 3))

    pygame.display.update()

    clock.tick(60)
pygame.quit()