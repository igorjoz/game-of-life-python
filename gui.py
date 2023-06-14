import tkinter as tk

import pygame

WIDTH = 900
HEIGHT = 700

ICON_WIDTH = 64
ICON_HEIGHT = 64

WHITE = (255, 255, 255)

FPS = 144

HUMAN_IMAGE = pygame.image.load("./assets/human.png")
HUMAN = pygame.transform.scale(HUMAN_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

WOLF_IMAGE = pygame.image.load("./assets/wolf.png")
WOLF = pygame.transform.scale(WOLF_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

SHEEP_IMAGE = pygame.image.load("./assets/sheep.png")
SHEEP = pygame.transform.scale(SHEEP_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

FOX_IMAGE = pygame.image.load("./assets/fox.png")
FOX = pygame.transform.scale(FOX_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

TORTOISE_IMAGE = pygame.image.load("./assets/tortoise.png")
TORTOISE = pygame.transform.scale(TORTOISE_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

ANTELOPE_IMAGE = pygame.image.load("./assets/antelope.png")
ANTELOPE = pygame.transform.scale(ANTELOPE_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

GRASS_IMAGE = pygame.image.load("./assets/grass.png")
GRASS = pygame.transform.scale(GRASS_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

DANDELION_IMAGE = pygame.image.load("./assets/dandelion.png")
DANDELION = pygame.transform.scale(DANDELION_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

GUARANA_IMAGE = pygame.image.load("./assets/guarana.png")
GUARANA = pygame.transform.scale(GUARANA_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

NIGHTSHADE_IMAGE = pygame.image.load("./assets/nightshade.png")
NIGHTSHADE = pygame.transform.scale(NIGHTSHADE_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

HOGWEED_IMAGE = pygame.image.load("./assets/hogweed.jpg")
HOGWEED = pygame.transform.scale(HOGWEED_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Game of Life - Igor Józefowicz")


class Gui:
    def __init__(self):
        self.world_size = 0

        self.window = tk.Tk()
        self.window.title("World Size Input")

        self.size_label = tk.Label(self.window, text="Enter world size:")
        self.size_label.pack()

        self.size_entry = tk.Entry(self.window)
        self.size_entry.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        self.world_size = int(self.size_entry.get())
        print(f"World size: {self.world_size}")
        self.window.destroy()

    def get_board_size(self):
        self.window.mainloop()
        return self.world_size

    def update_window(self, organisms_list):
        WINDOW.fill(WHITE)

        for i in range(0, self.world_size):
            for j in range(0, self.world_size):
                pygame.draw.rect(WINDOW, (0, 0, 0), (i * ICON_WIDTH, j * ICON_HEIGHT, ICON_WIDTH, ICON_HEIGHT), 1)

        for organism in organisms_list:
            if organism.symbol == "H":
                WINDOW.blit(HUMAN, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "W":
                WINDOW.blit(WOLF, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))

        pygame.display.update()
