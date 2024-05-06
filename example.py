import pygame
from background import BackgroundLayer

pygame.font.init()

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


def draw_window(window, *background_layers):
    for layer in background_layers:
        layer.draw(window)
    pygame.display.update()


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

# i mage_path, speed, window_width, window_height
    background_layers = [
        BackgroundLayer("background_layer.png", 2, WINDOW_WIDTH, WINDOW_HEIGHT),
        BackgroundLayer("midground_layer.png", 3, WINDOW_WIDTH, WINDOW_HEIGHT),
        BackgroundLayer("foreground_layer.png", 5, WINDOW_WIDTH, WINDOW_HEIGHT)
    ]

    run_game = True
    while run_game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        for layer in background_layers:
            layer.move()

        draw_window(window, *background_layers)

    pygame.quit()


if __name__ == '__main__':
    main()
