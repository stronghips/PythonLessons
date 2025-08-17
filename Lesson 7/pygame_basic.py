import pygame

def init_game():
    pygame.init()
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def move_rectangle(screen, rectangle):
    pygame.draw.rect(screen, (255, 0, 0), rectangle)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and rectangle.x > 0:
        rectangle.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] and rectangle.x < screen.get_width() - rectangle.width:
        rectangle.move_ip(1, 0)
    elif key[pygame.K_UP] and rectangle.y > 0:
        rectangle.move_ip(0, -1)
    elif key[pygame.K_DOWN] and rectangle.y < screen.get_height() - rectangle.height:
        rectangle.move_ip(0, 1)


def main_loop(screen):
    rectangle = pygame.Rect((300, 250, 50, 50))
    run = True
    while run:
        screen.fill((0, 0, 0))
        move_rectangle(screen, rectangle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    screen = init_game()
    main_loop(screen)
