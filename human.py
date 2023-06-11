from enum import Enum
from typing import Tuple
import random

from animal import Animal
from organism import Organism
from point import Point
from world import World


class PlayerAction(Enum):
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    NONE = 5


class Human(Animal):
    STRENGTH = 5
    INITIATIVE = 4
    SYMBOL = 'H'

    def __init__(self, position: Point, world: World):
        super().__init__(self.STRENGTH, self.INITIATIVE, self.SYMBOL, position, world)
        self.player_action = PlayerAction.NONE
        self.species = 'HUMAN'
        self.is_alive = True

    def action(self):
        x = self.position.x
        y = self.position.y

        special_ability_duration = self.world.get_game().get_special_ability_duration()
        random_number = random.choice([0, 1])

        if special_ability_duration > 2 or (special_ability_duration > 0 and random_number == 1):
            if self.player_action == PlayerAction.MOVE_UP:
                y -= 2
            elif self.player_action == PlayerAction.MOVE_DOWN:
                y += 2
            elif self.player_action == PlayerAction.MOVE_LEFT:
                x -= 2
            elif self.player_action == PlayerAction.MOVE_RIGHT:
                x += 2
        else:
            if self.player_action == PlayerAction.MOVE_UP:
                y -= 1
            elif self.player_action == PlayerAction.MOVE_DOWN:
                y += 1
            elif self.player_action == PlayerAction.MOVE_LEFT:
                x -= 1
            elif self.player_action == PlayerAction.MOVE_RIGHT:
                x += 1

        destination = Point(x, y)

        if not self.world.is_within_board_boundaries(destination):
            return

        if self.world.is_occupied(destination):
            other = self.world.get_organism_at(destination)
            self.collision(other)

        if self.can_move_to(destination):
            self.move(destination)

    def collision(self, other: Organism):
        if self.can_kill(other):
            self.kill(other)
            return True

        return False

    def die(self):
        self.is_alive = False
        super().die()

    def reproduce(self, position: Point):
        pass

    def get_player_action(self):
        return self.player_action

    def get_is_alive(self):
        return self.is_alive

    def set_player_action(self, player_action: PlayerAction):
        self.player_action = player_action
