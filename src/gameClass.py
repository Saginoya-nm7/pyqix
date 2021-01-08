import pygame
import pygame.locals as pgConst
import src.const as const
from .field import Field


class Game:

    def __init__(self):
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode(size=const.Screen.Size)
        pygame.display.set_caption(const.Screen.Title)
        self.field = Field(self.screen)

    def run(self):
        continueFlag = True
        while continueFlag:
            self.screen.fill(color=(0, 0, 0))

            self.draw()

            pygame.display.update()

            for event in pygame.event.get():
                # 終了検出
                continueFlag = not (continueFlag and event.type == pgConst.QUIT)

        self.exit()

    def draw(self):
        self.field.draw()

    @staticmethod
    def exit():
        pygame.quit()
