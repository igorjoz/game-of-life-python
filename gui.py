import tkinter as tk

import pygame

WIDTH = 800
HEIGHT = 800

ICON_WIDTH = 40
ICON_HEIGHT = 40

WHITE = (255, 255, 255)

FPS = 144

HUMAN_IMAGE = pygame.image.load("./assets/human.png")
HUMAN = pygame.transform.scale(HUMAN_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

WOLF_IMAGE = pygame.image.load("./assets/wolf.png")
WOLF = pygame.transform.scale(WOLF_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

FOX_IMAGE = pygame.image.load("./assets/fox.png")
FOX = pygame.transform.scale(FOX_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

SHEEP_IMAGE = pygame.image.load("./assets/sheep.png")
SHEEP = pygame.transform.scale(SHEEP_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

ANTELOPE_IMAGE = pygame.image.load("./assets/antelope.png")
ANTELOPE = pygame.transform.scale(ANTELOPE_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

TORTOISE_IMAGE = pygame.image.load("./assets/tortoise.png")
TORTOISE = pygame.transform.scale(TORTOISE_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

CYBER_SHEEP_IMAGE = pygame.image.load("./assets/cyber_sheep.png")
CYBER_SHEEP = pygame.transform.scale(CYBER_SHEEP_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

GRASS_IMAGE = pygame.image.load("./assets/grass.png")
GRASS = pygame.transform.scale(GRASS_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

DANDELION_IMAGE = pygame.image.load("./assets/dandelion.png")
DANDELION = pygame.transform.scale(DANDELION_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

GUARANA_IMAGE = pygame.image.load("./assets/guarana.png")
GUARANA = pygame.transform.scale(GUARANA_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

NIGHTSHADE_IMAGE = pygame.image.load("./assets/nightshade.png")
NIGHTSHADE = pygame.transform.scale(NIGHTSHADE_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

HOGWEED_IMAGE = pygame.image.load("./assets/hogweed.png")
HOGWEED = pygame.transform.scale(HOGWEED_IMAGE, (ICON_WIDTH, ICON_HEIGHT))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Game of Life - Igor Józefowicz")


class Gui:
    def __init__(self):
        self.context_menu_active = False
        pygame.init()

        self.world_size = 0

        self.window = tk.Tk()
        self.window.title("World Size Input")

        self.window.geometry("300x100")

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
            elif organism.symbol == "S":
                WINDOW.blit(SHEEP, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "C":
                WINDOW.blit(CYBER_SHEEP, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "A":
                WINDOW.blit(ANTELOPE, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "T":
                WINDOW.blit(TORTOISE, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "C":
                WINDOW.blit(CYBER_SHEEP, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "F":
                WINDOW.blit(FOX, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "G":
                WINDOW.blit(GRASS, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "U":
                WINDOW.blit(GUARANA, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "D":
                WINDOW.blit(DANDELION, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "N":
                WINDOW.blit(NIGHTSHADE, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))
            elif organism.symbol == "P":
                WINDOW.blit(HOGWEED, (organism.position.x * ICON_WIDTH, organism.position.y * ICON_HEIGHT))

        if self.context_menu_active:
            menu_font = pygame.font.Font(None, 24)  # You may need to choose a different font.
            menu_items = ["Wolf", "Sheep", "Antelope", "Tortoise", "CyberSheep", "Fox", "Grass", "Guarana", "Dandelion", "Nightshade", "Hogweed"]
            menu_height = len(menu_items) * menu_font.get_linesize()
            pygame.draw.rect(WINDOW, (200, 200, 200), (self.context_menu_position.left, self.context_menu_position.top, 150, menu_height))
            for i, item in enumerate(menu_items):
                text_surface = menu_font.render(item, True, (0, 0, 0))
                WINDOW.blit(text_surface, (self.context_menu_position.x, self.context_menu_position.y + i * menu_font.get_linesize()))

        pygame.display.update()

    def show_context_menu(self, position):
        self.context_menu_active = True
        self.context_menu_position = pygame.Rect(position[0], position[1], 0, 0)  # Convert tuple to Rect object
