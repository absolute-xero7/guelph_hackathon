"""
Ye Old Game
"""
from __future__ import annotations
import random

physical_damage = 3
max_health = 10
max_shield = 5
shield_regen = 1
strength_modifier = 1
transformation_modifier = 1
types = {'void': 0, 'fire': 1, 'air': 2, 'earth': 3, 'water': 4, 'electricity': 5, 'ice': 6}
# magic_dictionary = {'void': ['Dead Inside', 10, 12, 15 , 16, 16, ], 'fire': ['Inferno Breath', 10], 'air': ['Whirlwind', 10], 'earth': ['Earthquake', 10], 'water': ['Whirlpool', 10], 'electricity': ['Thunder', 10]
# , 'ice': ['Frostbite', 10]}
magic_dictionary = {
    'void': ['Dead Inside', random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
             random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
             random.randint(1, 2)],
    'fire': ['Inferno Breath', random.randint(1, 2), random.randint(2, 3), random.randint(2, 4),
             random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
             random.randint(2, 4)],
    'air': ['Whirlwind', random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
            random.randint(1, 2), random.randint(1, 2), random.randint(1, 2), random.randint(1, 2)],
    'earth': ['Earthquake', random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
              random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
              random.randint(1, 2)],
    'water': ['Whirlpool', random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
              random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
              random.randint(1, 2)],
    'electricity': ['Thunder', random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
                    random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
                    random.randint(1, 2)],
    'ice': ['Absolute Xero', random.randint(1, 2), random.randint(1, 2), random.randint(1, 2),
            random.randint(1, 2), random.randint(1, 2), random.randint(1, 2), random.randint(1, 2)]}


class Player:
    """A player participating in the game.

    Instance Attributes:
      - designation: The category which is chosen by the player. (Will be the type 'VOID' if nothing is selected)
      - health: The amount of health each player has.
      - move: Determines which player's turn it is, 0 if it's the other players turn and 1 if it's the player's turn.
      - transform_turn: The number of turns left in the current transformation. (0 if not in a transformation)
    """
    type: str
    health: int
    mana: int
    shield: int
    transform_turn: int
    strength_turn: int

    def __init__(self, designation: str = 'void') -> None:
        """Initialize a new player of a given type.
        """
        self.type = designation
        self.health = max_health  # 50 - 100
        self.shield = 0
        self.transform_turn = 0
        self.strength_turn = 0

    def heal_potion(self) -> None:
        """Heals the player by a random amount between 5 and 10.
        """
        heal = random.randint(1, 5)
        if heal + self.health > max_health:
            self.health = max_health
        else:
            self.health += heal

    def strength_potion(self: Player) -> None:
        """Gives the player strength for a certain amount of turns."""
        self.strength_turn = strength_modifier

    def add_shield(self) -> None:
        """Adds a shield to the player."""
        if self.shield + shield_regen > max_shield:
            self.shield = max_shield
        else:
            self.shield += shield_regen

    def take_damage(self, damage: int) -> None:
        """Takes damage from the other player."""
        if self.shield < damage:
            self.shield = 0
            self.health -= (damage - self.shield)
        else:
            self.shield -= damage

    def transform(self, designation: str) -> None:
        """Transforms the player into a different type for a certain amount of turns."""
        self.type = designation
        self.transform_turn = transformation_modifier

    def magical_attack(self, opponent: Player) -> int:
        """Returns the damage of a magical attack."""
        type_n2 = types[opponent.type]
        return magic_dictionary[self.type][type_n2 + 1]

    def make_move(self, move: list, opponent: Player) -> None:
        """Makes a move for a player."""
        if move[0] == 'attack':
            if move[1] == 'physical':
                opponent.take_damage(physical_damage)
            elif move[1] == 'magic':
                opponent.take_damage(self.magical_attack(opponent))
            elif move[0] == 'transform':
                self.transform(move[1])
            else:
                raise ValueError('Invalid move')
        elif move[0] == 'potion':
            if move[1] == 'heal':
                self.heal_potion()
            elif move[1] == 'strength':
                self.strength_potion()
            else:
                raise ValueError('Invalid move')
        elif move[0] == 'shield':
            self.add_shield()
        else:
            raise ValueError('Invalid move')


class Game:
    """Proceedings of the game."""

    def __init__(self, player1: Player, player2: Player) -> None:
        """Initialize a new game.
        """
        self.player1 = player1
        self.player2 = player2
        self.turn = 0

    def play_turn(self, move) -> None:
        """Plays one round with given moves.
        """
        if self.turn % 2 == 0:
            self.player1.make_move(move, self.player2)
        else:
            self.player2.make_move(move, self.player1)
        self.turn += 1

    def run_game(self) -> None:
        """Runs the game until one player has no health left."""
        while self.player1.health > 0 and self.player2.health > 0:
            move = input("Enter your move:")
            self.play_turn(move)
            self.turn += 1
            if self.player1.health <= 0:
                print('You Lose >:(')
            if self.player2.health <= 0:
                print("You Win! Congrats! :D")


if __name__ == 'name':
    player1 = Player()
    player2 = Player()

