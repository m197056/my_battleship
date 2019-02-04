import pygame

"""
 'cut out' sprites from the sprite sheet
 the first sprite is provided as an example
"""

# sprites are 30x30 tiles separated by 1 pixel margins
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 30
SPRITE_MARGIN = 1

# an array of all the game sprites
sprites = []

# load the sprite sheet
sprite_sheet = pygame.image.load('assets/sprite_sheet.png')

# ---ship_top (30x30)---
#     create an empty surface for the sprite
ship_top = pygame.Surface((30, 30))
#     see blit documentation at
#     https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
ship_top.blit(sprite_sheet, (0, 0), pygame.Rect(0, 0, 30, 30))
#     add the sprite to the array
sprites.append(ship_top)

# --------- BEGIN YOUR CODE ----------

# ---ship_left (30x30)---
ship_left = pygame.Surface((30, 30))
ship_left.blit(sprite_sheet, (0, 0), pygame.Rect(31, 0, 30, 30))
sprites.append(ship_left)

# ---ship_bottom (30x30)---
ship_bottom = pygame.Surface((30, 30))
ship_bottom.blit(sprite_sheet, (0, 0), pygame.Rect(62, 0, 30, 30))
sprites.append(ship_bottom)

# ---ship_right (30x30)---
ship_right = pygame.Surface((30, 30))
ship_right.blit(sprite_sheet, (0, 0), pygame.Rect(93, 0, 30, 30))
sprites.append(ship_right)

# ---ship_horizontal (30x30)---
ship_horizontal = pygame.Surface((30, 30))
ship_horizontal.blit(sprite_sheet, (0, 0), pygame.Rect(0, 31, 30, 30))
sprites.append(ship_horizontal)

# ---ship_vertical (30x30)---

# ---hit (30x30)---

# ---miss (30x30)---

# ---ship_sunk (30x30)---

# ---turn (40x20)---

# ---msg_box (250x122)---

# --------- END YOUR CODE ------------


# set alpha on all sprites to enable transparency
def initialize():
    for sprite in sprites:
        sprite.set_colorkey((255, 0, 255))
        sprite.convert_alpha()