#
# File: plant.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 14/12/2021
# Description: This is my program.
# This is my own work as defined by the University's
# Academic Misconduct policy
import random
from tile import *
from game import *


class Plant(GameObject):
    """Inherits from the GameObject class
    Contains position, width, height, sourceImage, game
    """

    def __init__(self, position, width, height, sourceImage, game):
        """Constructing a Plant object"""
        super(Plant, self).__init__(position, width, height, sourceImage, game)
        self.grow_time = random.randint(5, 20)
        self.near_dirt = []

    def nearBy(self):
        """Check the game_object list append a new corn object's position"""
        for dirt in self.get_game().tiles:
            if type(dirt) == Dirt:
                if 96 <= self.get_position().distance(Vector2D(dirt.get_x(), dirt.get_y())) <= 192:
                    self.near_dirt.append(dirt)
        return self.near_dirt

    def die(self):
        self.get_game().plant.remove(self)

    @abc.abstractmethod
    def grow(self, location, timeElapsed):
        """Creates a new Plant object on adjacent dirt tile after a random number of seconds
        """
        pass

    def update(self, timeElapsed):
        """This update function is used to change the objects position"""
        if self.near_dirt is not None:
            pos = self.nearBy()
            new_plant_pos = random.choice(pos)
            if random.randint(1, 2) == 1:
                self.grow(new_plant_pos, timeElapsed)

    def __str__(self):
        """Returns a str representation of the Plant.
        Called automatically when the Plant is printed.
        """
        msg = f'Plant: is at position {self.get_position()}, has {self.get_height()} height' \
              f'and {self.get_width()} width, with an image of {self.get_image()}'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()


class Corn(Plant):
    """Inherits from the Plant class
    Contains position, width, height, sourceImage, game
    Corn is eaten by Chicken
    """

    def __init__(self, position, width, height, sourceImage, game):
        """Constructing a Corn object"""
        super(Corn, self).__init__(position, width, height, sourceImage, game)
        self.grow_time = random.randint(20, 40)
        self.near_dirt = []

    def update(self, timeElapsed):
        """This update function is used to change the objects position"""
        super(Corn, self).update(timeElapsed)
        if self.near_dirt is not None:
            pos = self.nearBy()
            new_plant_pos = random.choice(pos)
            self.grow(new_plant_pos, timeElapsed)

    def grow(self, dirt, timeElapsed):
        """Grow corn on the new location after several seconds between 5 and 20"""
        if dirt is not None:
            self.grow_time -= timeElapsed
            if dirt.plant is None:
                if self.grow_time <= 0:
                    new_corn = Corn(Vector2D(dirt.get_x(), dirt.get_y()), 96,
                                    96, self.get_image(), self.get_game())
                    self.get_game().plant.append(new_corn)
                    dirt.set_plant(new_corn)
                    self.grow_time = random.randint(20, 40)

    def __str__(self):
        """Returns a str representation of the Corn.
        Called automatically when the Corn is printed.
        """
        msg = f'Corn is in {self.get_position()}, has {self.get_width()} width and {self.get_height()} height,' \
              f' an image of Corn'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()


class Grass(Plant):
    """Inherits from the Plant class
    Contains position, width, height, sourceImage, game
    Grass is eaten by Wombat
    """

    def __init__(self, position, width, height, sourceImage, game):
        """Constructing a Grass object"""
        super(Grass, self).__init__(position, width, height, sourceImage, game)
        self.grow_time = random.randint(30, 40)
        self.locations = []

    def grow(self, dirt, timeElapsed):
        """Grow grass on the new location after several seconds between 5 and 20"""
        if dirt is not None:
            self.grow_time -= timeElapsed
            if dirt.plant is None:
                if self.grow_time <= 0:
                    new_grass = Grass(Vector2D(dirt.get_x(), dirt.get_y()), 96,
                                      96, self.get_image(), self.get_game())
                    self.get_game().plant.append(new_grass)
                    dirt.set_plant(new_grass)
                    self.grow_time = random.randint(30, 40)

    def __str__(self):
        """Returns a str representation of the Grass.
        Called automatically when the Grass is printed.
        """
        msg = f'Grass: is at position {self.get_position()}, has {self.get_height()} height' \
              f'and {self.get_width()} width, with an image of {self.get_image()}'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()
