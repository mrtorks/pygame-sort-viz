import pygame
import math

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 40, 215, 154
    RED = 255, 0, 0
    BACKGROUND_COLOR = 215, 40, 101
    #BACKGROUND_COLOR = WHITE
    NUM_COLOR = WHITE
    GRADIENTS = [(40, 215, 154), (215, 65, 40), (215, 40, 190), (36, 194, 139), (32, 172, 123), (102, 215, 40), (28, 151, 108), (40, 102, 215),
                 (24, 129, 92), (190, 215, 40), (65, 40, 215), (172, 52, 32), (172, 32, 152), (82, 172, 32), (32, 82, 172), (152, 172, 32), (52, 32, 172)]

    SIDE_PAD = 100
    FONT = pygame.font.SysFont('Calibri', 20)
    LARGE_FONT = pygame.font.SysFont('Calibri', 40)

    VAL_FONT_NAME = "Calibri"
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Vizualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.low = 0
        self.list_size = len(self.lst)
        self.min_value = min(lst)
        self.max_value = max(lst)
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor(
            (self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2
