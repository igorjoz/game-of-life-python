import pygame
from game import Game
from gui import Gui
from direction import Direction


FPS = 144


def main():
    gui = Gui()
    game = Game(gui)

    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left arrow key pressed")
                    game.move_player(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    print("right arrow key pressed")
                    game.move_player(Direction.RIGHT)
                elif event.key == pygame.K_UP:
                    print("up arrow key pressed")
                    game.move_player(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    print("down arrow key pressed")
                    game.move_player(Direction.DOWN)

        organisms_list = game.get_organisms_list()
        gui.update_window(organisms_list)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
