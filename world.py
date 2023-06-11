from typing import Optional

from game import Game as Gam
from human import Human as Hum
from organism import Organism
from point import Point


class World:
    def __init__(self, game: Gam, size: int):
        self.game = game
        self.size = size
        self.organisms = [[None for _ in range(size)] for _ in range(size)]
        self.organisms_list = []
        self.turn_summary_messages = []
        # self.human: Optional[Human] = None
        self.human: Optional[Hum] = None

    def take_turn(self):
        if not self.human.get_is_alive():
            print("You died!")
            exit(0)

        self.organisms_list.sort(key=lambda organism: (organism.get_initiative(), organism.get_age()), reverse=True)

        for organism in self.organisms_list.copy():
            organism.action()

    def spawn_organism(self, organism: Organism):
        position = self.get_random_position()

        if self.is_occupied(position):
            return

        organism.set_position(position)
        self.organisms_list.append(organism)
        self.organisms[position.x][position.y] = organism

    def get_random_position(self):
        import random
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)

        return Point(x, y)
