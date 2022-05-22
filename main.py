
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional

@dataclass
class Player:
    """A player participating in the game.
    
    Instance Attributes:
      - designation: The category which is chosen by the player. (Will be the type 'VOID' if nothing is selected)
      - health: The amount of health each player has.
      - move: Determines which player's turn it is, 0 if it's the other players turn and 1 if it's the player's turn.
    """
    type: str
    health: int
    move: int

    def __init__(self, designation: str = 'void', move: int) -> None:
        """Initialize a new player of a given type.
        """
        self.designation = designation
        self.health = 50
        self.move = move

@dataclass
class Game:
    """Proceedings of the game."""

    def play(player1: Player, player2: Player, move: str) -> Any:
        """Plays one round after receiving the move from the next player."""
        if player1.move == 1
            if player1.designation == 'water':
                if player2.designation == 'fire':
                
