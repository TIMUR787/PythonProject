from TextObject import *


class Button(TextObject):
    """Create a button, then blit the surface in the while loop"""

    def change_text(self, row_text):
        """Change the text whe you click"""
        super().change_text(row_text)
        self.rect = pygame.Rect(self.x - self.size[0] // 2, self.y - self.size[1] // 2, self.size[0], self.size[1])

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True
        return False
