import pygame

class Block:
    sum = 0

    def __init__(self, x, y, scl, is_bomb):
        self.x = x * scl
        self.y = y * scl
        self.scl = scl
        self.is_bomb = is_bomb
        self.is_press = False
        self.flagged = False
        self.value = 0

    def init(self, blocks, width, height):
        if not self.is_bomb:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= self.y + i * self.scl < height * self.scl and 0 <= self.x + j * self.scl < width * self.scl:
                        if not (j == 0 and i == 0):
                            if blocks[self.y // self.scl + i][self.x // self.scl + j].is_bomb:
                                self.value += 1
        else:
            Block.sum += 1

    def open(self, blocks, width, height):
        self.is_press = True
        if self.is_bomb:
            return False
        if self.value == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= self.y + i * self.scl < height * self.scl and 0 <= self.x + j * self.scl < width * self.scl:
                        if not (j == 0 and i == 0):
                            if not blocks[self.y // self.scl + i][self.x // self.scl + j].is_press:
                                blocks[self.y // self.scl + i][self.x // self.scl + j].open(blocks, width, height)
        return True

    def show(self, window):
        if not self.is_press:
            pygame.draw.rect(window, (150, 150, 150), (self.x, self.y, self.scl, self.scl))
        else:
            pygame.draw.rect(window, (100, 100, 100), (self.x, self.y, self.scl, self.scl))
            if self.is_bomb:
                pygame.draw.circle(window, (150, 150, 150), (self.x+self.scl//2, self.y+self.scl//2), 10)
            else:
                if self.value != 0:
                    myfont = pygame.font.SysFont('Comic Sans MS', 10)
                    textsurface = myfont.render(f'{self.value}', False, (0, 0, 0))
                    window.blit(textsurface, (self.x+self.scl/3, self.y+self.scl/3))

        if self.flagged and not self.is_press:
            pygame.draw.circle(window, (0, 255, 0), (self.x + self.scl // 2, self.y + self.scl // 2), 10)