import pygame
import colors
import utilities

NBLOCKS = 11

class GameBoard(pygame.sprite.Sprite):
    """
    The Game Board is a 10x10 grid of spaces which may contain sprite images
    Columns are indexed by number [0-9] and rows are indexed by letter [A-J]

        _|0|1|2|3|4|5|6|7|8|9|
        A|_|_|_|_|_|_|_|_|_|_|
        B|_|_|_|_|_|_|_|_|_|_|
        C|_|_|_|_|_|_|_|_|_|_|
        D|_|_|_|_|_|_|_|_|_|_|
        E|_|_|_|_|_|_|_|_|_|_|
        F|_|_|_|_|_|_|_|_|_|_|
        G|_|_|_|_|_|_|_|_|_|_|
        H|_|_|_|_|_|_|_|_|_|_|
        I|_|_|_|_|_|_|_|_|_|_|
        J|_|_|_|_|_|_|_|_|_|_|

    """
    def __init__(self, dimension):
        super().__init__()
        self.image = pygame.Surface(dimension)
        self.image.convert()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # helper variables for spacing sprite images
        self.x_step = self.width // NBLOCKS
        self.y_step = self.height // NBLOCKS

    def refresh(self):
        # Draw board background use color [board_bkgd]
        self.image.fill(colors.board_bkgd)

        # --------- BEGIN YOUR CODE ----------

        # Draw row and column header backgrounds
        #   Headers should be 1 block wide/tall and use color [header]
        pygame.draw.rect(self.image, colors.header, (0, 0, self.width, self.y_step))
        pygame.draw.rect(self.image, colors.header, (0, 0, self.x_step, self.height))

        # Draw grid lines use color [foreground]
        for n in range(1, NBLOCKS):
            pygame.draw.line(self.image, colors.foreground, (n*self.x_step, 0), (n*self.x_step, self.height))
            pygame.draw.line(self.image, colors.foreground, (0, n * self.y_step), (self.width, n * self.y_step))

        # Draw row labels [A-J] centered in each header block
        #    use color [foreground] and font
        letters = 'A B C D E F G H I J'.split(' ')

        for n in range(0, NBLOCKS - 1):
            text = utilities.create_text(letters[n], 24, colors.foreground)
            textImg = text.get_rect()
            textImg.centerx = 0.5 * self.x_step
            textImg.centery = (n * self.y_step) + (1.5 * self.y_step)
            self.image.blit(text, textImg)

        # Draw column labels [0-9] centered in each header block
        #    use color [foreground]

        for n in range(0, NBLOCKS - 1):
            text = utilities.create_text(str(n), 24, colors.foreground)
            textImg = text.get_rect()
            textImg.centerx = (n * self.x_step) + (1.5 * self.x_step)
            textImg.centery = 0.5 * self.y_step
            self.image.blit(text, textImg)

        # Draw border around the board use color [foreground]
            # far right and bottom side are one less than width/height
        pygame.draw.line(self.image, colors.foreground, (0, 0), (self.width - 1, 0))  # Top border
        pygame.draw.line(self.image, colors.foreground, (0, self.height - 1), (self.width - 1, self.height-1))  # Bottom border
        pygame.draw.line(self.image, colors.foreground, (self.width-1, 0), (self.width - 1, self.height - 1))  # Right border
        pygame.draw.line(self.image, colors.foreground, (0, 0), (0, self.height - 1))  # Left border

        # --------- END YOUR CODE ------------

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
