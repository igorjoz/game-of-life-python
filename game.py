from typing import Union, List
from enum import Enum
import numpy as np

from human import Human
from wolf import Wolf
from world import World

from direction import Direction
from point import Point
from player_action import PlayerAction


class Game:
    SPECIAL_ABILITY_COOLDOWN = 5

    def __init__(self, gui):
        self.gui = gui
        self.world = None
        self.size = 0
        self.turn = 0
        self.special_ability_cooldown = self.SPECIAL_ABILITY_COOLDOWN
        self.special_ability_duration = 0

        self.initialize_game()

    def initialize_game(self):
        self.size = self.gui.get_board_size()

        self.world = World(self, self.size)
        self.turn = 0

        self.special_ability_cooldown = self.SPECIAL_ABILITY_COOLDOWN
        self.special_ability_duration = 0

        self.spawn_initial_organisms()

    def spawn_initial_organisms(self):
        self.create_human()
        self.spawn_wolves()

    def create_human(self):
        position = Point(0, 0)

        human = Human(position, self.world)
        self.world.create_human(human)

    def spawn_wolves(self):
        for _ in range(Wolf.INITIAL_QUANTITY):
            wolf = Wolf(self.world)
            self.world.spawn_organism(wolf)

    def move_player(self, direction: Direction):
        human = self.world.get_human()

        if direction == Direction.UP:
            human.set_player_action(PlayerAction.MOVE_UP)
        elif direction == Direction.DOWN:
            human.set_player_action(PlayerAction.MOVE_DOWN)
        elif direction == Direction.LEFT:
            human.set_player_action(PlayerAction.MOVE_LEFT)
        elif direction == Direction.RIGHT:
            human.set_player_action(PlayerAction.MOVE_RIGHT)

        self.world.take_turn()
        self.increment_organisms_age()
        self.turn += 1
        #
        # if self.special_ability_cooldown > 0:
        #     self.special_ability_cooldown -= 1
        #
        # if self.special_ability_duration > 0:
        #     self.special_ability_duration -= 1
        #
        #     if self.special_ability_duration == 0:
        #         self.special_ability_cooldown = self.SPECIAL_ABILITY_COOLDOWN
        #
        # for i in range(self.size):
        #     for j in range(self.size):
        #         if self.world.get_organisms()[j][i] is None:
        #             print("- ", end='')
        #         else:
        #             print(self.world.get_organisms()[j][i].get_symbol(), " ", end='')
        #     print()

    def increment_organisms_age(self):
        for organism in self.world.get_organisms_list():
            organism.age = organism.age + 1

    def activate_special_ability(self):
        if self.special_ability_cooldown > 0:
            print("Special ability is on cooldown!")
            return

        self.special_ability_duration = 5
        self.special_ability_cooldown = 0

    def get_special_ability_duration(self):
        return self.special_ability_duration

    def get_special_ability_cooldown(self):
        return self.special_ability_cooldown

    def get_organisms_list(self):
        return self.world.get_organisms_list()

    def save_to_file(self):
        with open("save.txt", "w") as file:
            # Add saving mechanism here, e.g.:
            file.write(str(self.turn) + "\n")
            # ...

    # def load_from_file(self):
    #     try:
    #         with open("save.txt", "r")
