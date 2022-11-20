import pygame


class TextObject:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, screen, row_text, pos, font_size, **kwargs):
        self.kwargs = kwargs
        self.row_text = row_text
        self.screen = screen
        self.x, self.y = pos
        self.font_size = font_size
        self.font = pygame.font.SysFont("Arial", font_size)
        self.change_text(row_text)

    def change_text(self, row_text):
        """Change the text whe you click"""
        self.text = self.font.render(row_text[:30], 1, pygame.Color(self.kwargs['color']))
        try:
            self.size = self.kwargs['size']
        except:
            self.size = max((300, self.font_size), self.text.get_size())
        self.size = (self.size[0], self.size[1] + 10)
        self.surface = pygame.Surface(self.size)
        text_rect = self.text.get_rect()
        try:
            if self.kwargs['align'] == 'left':
                text_rect.left = 0
            if self.kwargs['align'] == 'right':
                text_rect.right = self.size[0]
        except:
            text_rect.center = (self.size[0] // 2, self.size[1] // 2)

        self.surface.fill('black')
        self.surface.fill(self.kwargs['bg'], (2, 2, self.size[0] - 4, self.size[1] - 4))
        self.surface.blit(self.text, text_rect)
        # pygame.draw(self.surface, (255,0,0), pygame.Rect(10, 25, 200, 65), 4)
        # self.rect = pygame.Rect(self.x-self.size[0]//2, self.y-self.size[1]//2, self.size[0], self.size[1])

    def show(self):
        self.screen.blit(self.surface, (self.x - self.size[0] // 2, self.y - self.size[1] // 2))
