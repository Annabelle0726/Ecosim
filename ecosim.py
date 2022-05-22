#
# File: ecosim.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 14/11/2021
# Description: This is my program.
# This is my own work as defined by the University's
# Academic Misconduct policy
from animal import *
from plant import *
from game import *


class EcoSim(Game):
    """
    A class to represent the Ecosystem Simulator.
    Contains plants, animals, tile, and window
    Inherits from Game"""

    def __init__(self):
        """
        Constructing an object of this class will create Window,
        containing a grid of tiles, plants and animals at random locations.
        """
        super().__init__()
        self.tiles = []
        self.plant = []
        self.animal = []

        x = 0
        for tile in range(12):
            for y in range(12):
                random_tile = random.randint(0, 4)
                if random_tile == 0:
                    self.tiles.append(Sand(Vector2D(96 * x, 96 * y), 96, 96,
                                           ImageLibrary.get('sand_tile'), self))
                else:
                    dirt = Dirt(Vector2D(96 * x, 96 * y), 96, 96,
                                ImageLibrary.get('dirt_tile'), self)
                    self.tiles.append(dirt)
                    random_plant_grow = random.randint(0, 1)
                    if random_plant_grow == 1:
                        random_plant = random.randint(0, 1)
                        if random_plant == 0:
                            grass = Grass(Vector2D(96 * x, 96 * y), 96, 96,
                                          ImageLibrary.get('grass_tuft'), self)
                            dirt.set_plant(grass)
                            self.plant.append(grass)
                        else:

                            corn = Corn(Vector2D(96 * x, 96 * y), 96, 96,
                                        ImageLibrary.get('corn'), self)
                            dirt.set_plant(corn)
                            self.plant.append(corn)
                y += 1
            x += 1

        for i in range(10):
            random_animal_x = random.randint(1, 12)
            random_animal_y = random.randint(1, 10)
            self.animal.append(Wombat(Vector2D(96 * random_animal_x, 96 * random_animal_y), 96, 96,
                                      ImageLibrary.get('wombat1'), self, 10, 40))

        for i in range(6):
            random_animal_x = random.randint(1, 12)
            random_animal_y = random.randint(1, 10)
            self.animal.append(Chicken(Vector2D(96 * random_animal_x, 96 * random_animal_y), 96 * 2, 96 * 2,
                                       ImageLibrary.get('chicken'), self, 10, 40))

        for i in range(3):
            random_animal_x = random.randint(1, 12)
            random_animal_y = random.randint(1, 10)
            self.animal.append(Snake(Vector2D(96 * random_animal_x, 96 * random_animal_y), 96, 96,
                                     ImageLibrary.get('snake1'), self, 15, 55))


def main():
    """The start of the game"""
    ImageLibrary.load('images')
    ecosim = EcoSim()
    ecosim.run()


if __name__ == '__main__':
    main()
