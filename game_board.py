import pygame
import colors

NBLOCKS = 11


class GameBoard(pygame.sprite.Sprite):

    def __init__(self, dimension):
        super().__init__()
        self.image = pygame.Surface(dimension)
        self.image.convert()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x_step = self.width // NBLOCKS
        self.y_step = self.height // NBLOCKS

    def refresh(self):
        # Draw board background use color [board_bkgd]
        self.image.fill(colors.board_bkgd)

        # Draw row and column header backgrounds use color [header]

        # Draw grid and add row and column labels use color [foreground]

        # Add a border around the entire game board use color [foreground]

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

