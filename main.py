import pygame

# import game class
from game import Game

WIDTH = 900
HEIGHT = 700

ICON_WIDTH = 64
ICON_HEIGHT = 64

WHITE = (255, 255, 255)

FPS = 144

HUMAN_IMAGE = pygame.image.load("assets/human.png")
HUMAN = pygame.transform.scale(HUMAN_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Game of Life - Igor Józefowicz")


def draw_window():
    WINDOW.fill(WHITE)
    WINDOW.blit(HUMAN, (0, 0))
    pygame.display.update()


def main():
    game = Game()

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            pass
        # if enter is pressed, draw red square
        if keys_pressed[pygame.K_RETURN]:
            pass

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
