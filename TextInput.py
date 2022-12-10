import pygame

import TextObject

blue = (220, 220, 220)


class TextInput(TextObject.TextObject):
    def __init__(self, screen, row_text, pos, font_size, **kwargs):
        super().__init__(screen, row_text, pos, font_size, **kwargs)
        self.printed = 0

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
            if self.row_text[self.printed] == event.unicode:
                self.printed += 1
                self.change_text(self.row_text[self.printed:])
            # rect.size = img.get_size()


class DoubleTextInput:
    def __init__(self, screen, row_text, pos, font_size, **kwargs):
        self.size = kwargs['size']
        self.row_text = row_text
        self.ti1 = TextInput(screen, '', (pos[0] - self.size[0] // 2, pos[1]), font_size, color="gray",
                             bg=blue,
                             align='right', size=self.size)
        self.ti2 = TextInput(screen, row_text, (pos[0] + self.size[0] // 2, pos[1]), font_size, color="blue",
                             bg=kwargs['bg'], align='left', size=self.size)
        self.printed = 0
        self.mistakes = 0

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
            if self.printed < len(self.row_text):
                if self.row_text[self.printed] == event.unicode:
                    self.printed += 1
                    self.ti1.change_text(self.row_text[:self.printed][-TextObject.visible_size:])
                    self.ti2.change_text(self.row_text[self.printed:][:TextObject.visible_size])
                else:
                    self.mistakes += 1

    def show(self):
        self.ti1.show()
        self.ti2.show()
