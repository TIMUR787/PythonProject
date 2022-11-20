from Windows import *

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)

window_menu = WindowMenu(screen)
while True:
    window_menu.run()

pygame.quit()
exit()
