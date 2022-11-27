import os
import re
import time

import pygame

from Button import Button
from TextInput import DoubleTextInput
from TextObject import TextObject

gray = (112, 128, 144)
button_size = (300, 400)
white = (135, 206, 250)
fps = 120
horizontal_shift = 400
vertical_shift = 150
vertical_names_shift = 208
text_size = 50
double_text_size = (900, 50)


class WindowMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.button1 = Button(screen, "Текст 1",
                              (screen.get_width() // 5, screen.get_height() // 2), text_size,
                              color="black",
                              bg=gray, size=button_size)
        self.button2 = Button(screen, "Текст 2",
                              (screen.get_width() // 5 * 2, screen.get_height() // 2), text_size,
                              color="black",
                              bg=gray, size=button_size)
        self.button3 = Button(screen, "Текст 3",
                              (screen.get_width() // 5 * 3, screen.get_height() // 2), text_size,
                              color="black",
                              bg=gray, size=button_size)
        self.button4 = Button(screen, "Ваш текст",
                              (screen.get_width() // 5 * 4, screen.get_height() // 2), text_size,
                              color="black",
                              bg=gray, size=button_size)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if self.button1.click(event):
                    window_print_text = WindowPrintText(self.screen, 'text1.txt')
                    window_print_text.run()
                if self.button2.click(event):
                    window_print_text = WindowPrintText(self.screen, 'text2.txt')
                    window_print_text.run()
                if self.button3.click(event):
                    window_print_text = WindowPrintText(self.screen, 'text3.txt')
                    window_print_text.run()
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

            self.screen.fill(white)
            self.button1.show()
            self.button2.show()
            self.button3.show()
            self.button4.show()

            pygame.display.flip()
            self.clock.tick(fps)


class WindowPrintText:
    def __init__(self, screen, file_name):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.end_time = time.time()
        self.objects = []
        path = os.path.join(os.path.dirname(__file__), 'app_texts', file_name)
        text = ' '.join(open(path).readlines())
        self.text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
        self.button_menu = Button(screen, "Меню",
                                  (screen.get_width() // 2, screen.get_height() // 15), text_size,
                                  color="black",
                                  bg=gray)
        self.ti = DoubleTextInput(screen, self.text, (screen.get_width() // 2, screen.get_height() // 2), text_size,
                                  bg=white,
                                  size=double_text_size)
        self.text_time = TextObject(screen, "{:.2f}".format(self.end_time - self.start_time),
                                    (screen.get_width() // 2 - horizontal_shift,
                                     screen.get_height() // 2 - vertical_shift), text_size,
                                    color="black",
                                    bg=white)
        self.text_speed = TextObject(screen, "0", (screen.get_width() // 2, screen.get_height() // 2 - vertical_shift),
                                     text_size,
                                     color="black",
                                     bg=white)
        self.text_mistakes = TextObject(screen, "0", (
            screen.get_width() // 2 + horizontal_shift, screen.get_height() // 2 - vertical_shift),
                                        text_size,
                                        color="black",
                                        bg=white)
        self.text_word_time = TextObject(screen, "Время",
                                         (screen.get_width() // 2 - horizontal_shift,
                                          screen.get_height() // 2 - vertical_names_shift), text_size,
                                         color="black",
                                         bg=white)
        self.text_word_speed = TextObject(screen, "Скорость",
                                          (screen.get_width() // 2, screen.get_height() // 2 - vertical_names_shift),
                                          text_size,
                                          color="black",
                                          bg=white)
        self.text_word_mistakes = TextObject(screen, "Точность",
                                             (screen.get_width() // 2 + horizontal_shift,
                                              screen.get_height() // 2 - vertical_names_shift),
                                             text_size,
                                             color="black",
                                             bg=white)

        self.start = False
        self.end = False

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                self.ti.update(event)
                self.press_key(event)
                if self.button_menu.click(event):
                    running = False
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

            self.screen.fill(white)
            self.ti.show()
            self.update_fields()

            self.button_menu.show()

            self.text_word_time.show()
            self.text_time.show()

            self.text_word_speed.show()
            self.text_speed.show()

            self.text_word_mistakes.show()
            self.text_mistakes.show()

            pygame.display.flip()
            self.clock.tick(fps)

    def press_key(self, event):
        if event.type == pygame.KEYDOWN:
            if self.ti.printed == 1 and not self.start:
                self.start = True
                self.start_time = time.time()
            if self.ti.printed == len(self.text) and not self.end:
                self.end = True
                self.end_time = time.time()

    def update_fields(self):
        if self.start and not self.end:
            print("{:.2f}".format(time.time() - self.start_time))
            self.text_time.change_text("{:.2f}".format(time.time() - self.start_time))
            self.text_speed.change_text("{:.0f}".format(self.ti.printed / (time.time() - self.start_time) * 60))
            self.text_mistakes.change_text("{:.2f}".format(1 - self.ti.mistakes / self.ti.printed))
        if self.end:
            self.text_time.change_text("{:.2f}".format(self.end_time - self.start_time))
            self.text_speed.change_text("{:.0f}".format(self.ti.printed / (self.end_time - self.start_time) * 60))
            self.text_mistakes.change_text("{:.2f}".format(1 - self.ti.mistakes / self.ti.printed))
