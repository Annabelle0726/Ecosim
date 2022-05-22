#
# File: tile.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 14/12/2021
# Description: This is my program.
# This is my own work as defined by the University's
# Academic Misconduct policy
import random

from game import *


class Tile(GameObject):
    """Inherits from the GameObject class
    Contains position, width, height, sourceImage, game
    """

    def __init__(self, position, width, height, sourceImage, game):
        """Constructing a tile object"""
        super().__init__(position, width, height, sourceImage, game)

    def update(self, timeElapsed):
        """This update function is used to change the objects position"""
        # print('Time Elapsed =', timeElapsed)
        pass

    def __str__(self):
        """Returns a str representation of the Tile.
        Called automatically when the Tile is printed.
        """
        msg = f'Tile: is at position {self.get_position()}, has {self.get_height()} height' \
              f'and {self.get_width()} width, with an image of {self.get_image()}'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()


class Dirt(Tile):
    """Inherits from the GameObject class
    Contains position, width, height, sourceImage, game
    Randomly generated in a grid along with sand tiles.
    Has a 50% chance to spawn with a grass or corn on top.
    """

    def __init__(self, position, width, height, sourceImage, game):
        """Constructing a Dirt object"""
        super().__init__(position, width, height, sourceImage, game)
        self.plant = None

    def __str__(self):
        """Returns a str representation of the Dirt.
        Called automatically when the Dirt is printed.
        """
        msg = f'Dirt: is at position {self.get_position()}, has {self.get_height()} height' \
              f'and {self.get_width()} width, with an image of {self.get_image()}'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()

    def set_plant(self, plant):
        """Spawn with a plant on top"""
        if self.plant is None:
            self.plant = plant


class Sand(Tile):
    """Inherits from the Tile class
    Contains position, width, height, sourceImage, game
    Randomly generated in a grid along with dirt tiles."""

    def __init__(self, position, width, height, sourceImage, game):
        """Constructing a Sand object"""
        super().__init__(position, width, height, sourceImage, game)

    def __str__(self):
        """Returns a str representation of the Sand.
        Called automatically when the Sand is printed.
        """
        msg = f'Sand: is at position {self.get_position()}, has {self.get_height()} height' \
              f'and {self.get_width()} width, with an image of {self.get_image()}'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()
