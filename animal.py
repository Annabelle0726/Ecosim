#
# File: animal.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 14/12/2021
# Description: This is my program.
# This is my own work as defined by the University's
# Academic Misconduct policy
from exception import OutOfBoundsException
from plant import *
from game import *


class Animal(GameObject, metaclass=abc.ABCMeta):
    """Inherits from the GameObject class
    Contains position, width, height, sourceImage, game, speed, energy
    Moves around randomly when not hungry
    Finds closet food when hungry, Eats food
    Lives until it runs out of energy
    Creates a new animal if it lives long enough"""

    def __init__(self, position, width, height, sourceImage, game, speed, energy):
        """Constructing an Animal object"""
        super().__init__(position, width, height, sourceImage, game)
        self.speed = speed
        self.energy = energy
        self.target = Vector2D(random.randint(int(self.get_x()) - 50, int(self.get_x()) + 50),
                               random.randint(int(self.get_y()) - 50, int(self.get_y()) + 50))

    def find_closest_food(self, food_list):
        closest = food_list[0]
        distance = self.get_position().distance(closest.get_position())
        for food in food_list:
            if distance >= abs(self.get_position().distance(food.get_position())):
                closest = food
        return closest

    @abc.abstractmethod
    def eat(self, food_list):
        pass

    @abc.abstractmethod
    def destroyFood(self, food_list):
        pass

    def selectTarget(self):
        """Generates a random Vector2D target within a 100 pixel square around the Animal
        """
        self.target = Vector2D(random.randint(int(self.get_x()) - 50, int(self.get_x()) + 50),
                               random.randint(int(self.get_y()) - 50, int(self.get_y()) + 50))
        try:
            if self.target.x > 1152 or self.target.x < 0 or self.target.y > 960 or self.target.y < 0:
                raise OutOfBoundsException()
        except OutOfBoundsException as e:
            print(e)

    @abc.abstractmethod
    def set_speed(self):
        pass

    def die(self):
        self.get_game().animal.remove(self)

    def update(self, timeElapsed):
        """This update function is used to change the objects position"""

        self.energy -= timeElapsed
        if self.energy <= 0:
            self.destroy()
        else:
            self.reproduce(timeElapsed)
            self.set_speed()
            if self.energy <= 20:
                find_animal = self.find_closest_food(self.get_game().plant)
                if find_animal:
                    self.eat(find_animal)

            trajectory = self.target.subtract(self.get_position())
            trajectory = trajectory.normalize().scale(self.speed * timeElapsed)
            self.move_by(trajectory.x, trajectory.y)
            distance = self.get_position().distance(self.target)
            if distance < 10:
                self.selectTarget()

    @abc.abstractmethod
    def reproduce(self, timeElapsed):
        """Creates a new Animal object at the same location"""
        pass

    def __str__(self):
        """Returns a str representation of the Animal.
        Called automatically when the Animal is printed.
        """
        msg = f'Animal is in {self.get_position()}, has {self.get_width()} and {self.get_height()},' \
              f' moves at {self.speed} with {self.energy} energy'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()


class Wombat(Animal):
    """Inherits from the Animal class
    Contains position, width, height, sourceImage, game, speed, energy
    """

    def __init__(self, position, width, height, sourceImage, game, speed, energy):
        """Constructing a Wombat object"""
        super(Wombat, self).__init__(position, width, height, sourceImage, game, speed, energy)
        self.breed_time = 18

    def set_speed(self):
        """If Wombat is hungry, it moves fast at 80 pixels;
        If not it moves at 48 pixels per second"""
        if self.energy > 30:
            self.speed = 10
        else:
            self.speed = 12

    def reproduce(self, timeElapsed):
        """After 18 seconds, if the Wombat is still alive, it will create a new Wombat object at the same location"""
        self.breed_time -= timeElapsed
        if self.breed_time <= 0:
            wombat = Wombat(self.get_position(), self.get_width(), self.get_height(), self.get_image(),
                            self.get_game(), 10, 40)
            self.get_game().animal.append(wombat)
            self.breed_time = 18

    def find_closest_food(self, grass_list):
        """When a Wombat is low on energy, it finds the closest nearby grass"""
        super(Wombat, self).find_closest_food(grass_list)
        closest = grass_list[0]
        distance = self.get_position().distance(closest.get_position())
        for grass in grass_list:
            if type(grass) == Grass:
                if distance >= abs(self.get_position().distance(grass.get_position())):
                    closest = grass
                return closest

    def destroyFood(self, food):
        """When Wombat is within 48 pixels of the grass location, the grass is destroyed,
        """
        self.move_by(food.get_position().x, food.get_position().y)
        if self.get_position().distance(food.get_position()) <= 48:
            food.die()
            food.destroy()

    def eat(self, food):
        """Wombat eats grass as food and recovers 10 energy after it eats grass"""
        self.destroyFood(food)
        self.energy += 10

    def __str__(self):
        """Returns a str representation of the Wombat.
        Called automatically when the Wombat is printed.
        """
        msg = f'Wombat is in {self.get_position()}, has {self.get_width()} width and {self.get_height()} height,' \
              f' moves at {self.speed} speed with {self.energy} energy, a image of wombat'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()


class Snake(Animal):
    """Inherits from the Animal class
    Contains position, width, height, sourceImage, game, speed, energy
    """

    def __init__(self, position, width, height, sourceImage, game, speed, energy):
        """Constructing a Snake object"""
        super(Snake, self).__init__(position, width, height, sourceImage, game, speed, energy)
        self.breed_time = 32

    def reproduce(self, timeElapsed):
        """After 32 seconds, if the Snake is still alive, it will create a new Snake object at the same location"""
        self.breed_time -= timeElapsed
        if self.breed_time < 0:
            snake = Snake(self.get_position(), self.get_width(), self.get_height(), self.get_image(),
                          self.get_game(), 15, 55)
            self.get_game().animal.append(snake)
            self.breed_time = 32

    def update(self, timeElapsed):
        """This update function is used to change the objects position"""
        self.energy -= timeElapsed
        print(self.energy)
        if self.energy <= 0:
            self.destroy()
        else:
            self.reproduce(timeElapsed)
            self.set_speed()
            if self.energy <= 20:
                find_animal = self.find_closest_food(self.get_game().animal)
                if find_animal:
                    self.eat(find_animal)

            trajectory = self.target.subtract(self.get_position())
            trajectory = trajectory.normalize().scale(self.speed * timeElapsed)
            self.move_by(trajectory.x, trajectory.y)
            distance = self.get_position().distance(self.target)
            if distance < 10:
                self.selectTarget()

    def find_closest_food(self, animal_list):
        """When a Snake is low on energy, it finds the closest nearby animal"""
        if self.energy <= 12:
            super(Snake, self).find_closest_food(animal_list)
            closest = animal_list[0]
            distance = self.get_position().distance(closest.get_position())
            for animal in animal_list:
                if type(animal) == Wombat or type(animal) == Chicken:
                    if distance >= abs(self.get_position().distance(animal.get_position())):
                        closest = animal
            return closest

    def set_speed(self):
        """If Snake is hungry, it moves faster, at 45 pixels per second
        If not, it moves at 20 pixels per second"""
        if self.energy > 30:
            self.speed = 15
        else:
            self.speed = 30

    def destroyFood(self, food):
        """When Snake is within 48 pixels of its target, the target will be destroyed"""
        self.move_by(food.get_position().x, food.get_position().y)
        if self.get_position().distance(food.get_position()) <= 48:
            food.die()
            food.destory()

    def eat(self, food):
        """Snake eats other animal as food"""
        self.destroyFood(food)
        self.energy += 10

    def __str__(self):
        """Returns a str representation of the Snake.
        Called automatically when the Snake is printed.
        """
        msg = f'Snake is in {self.get_position()}, has {self.get_width()} width and {self.get_height()} height,' \
              f' moves at {self.speed} speed with {self.energy} energy, a image of snake'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()


class Chicken(Animal):
    """Inherits from the Animal class
    Contains position, width, height, sourceImage, game, speed, energy
    """

    def __init__(self, position, width, height, sourceImage, game, speed, energy):
        """Constructing a Chicken object"""
        super(Chicken, self).__init__(position, width, height, sourceImage, game, speed, energy)
        self.breed_time = 18

    def find_closest_food(self, corn_list):
        """When a Chicken is low on energy, it finds the closest nearby corn"""
        super(Chicken, self).find_closest_food(corn_list)
        if self.energy <= 20:
            closest = corn_list[0]
            distance = self.get_position().distance(closest.get_position())
            for corn in corn_list:
                if type(corn) == Corn:
                    if distance >= abs(self.get_position().distance(corn.get_position())):
                        closest = corn
            return closest

    def reproduce(self, timeElapsed):
        """After 18 seconds, if the Chicken is still alive, it will create a new Chicken object at the same location"""
        self.breed_time -= timeElapsed
        if self.breed_time < 0:
            chicken = Chicken(self.get_position(), self.get_width(), self.get_height(), self.get_image(),
                              self.get_game(), 10, 40)
            self.get_game().animal.append(chicken)
            self.breed_time = 18

    def set_speed(self):
        """If Chicken is hungry, it moves fast;
        If not it moves at 48 pixels per second"""
        if self.energy > 30:
            self.speed = 10
        else:
            self.speed = 12

    def destroyFood(self, food):
        """When Chicken is within 48 pixels of its target, the target will be destroyed"""
        self.move_by(food.get_position().x, food.get_position().y)
        if self.get_position().distance(food.get_position()) <= 48:
            food.die()
            food.destory()

    def eat(self, food):
        """Chicken eats corn as food and recovers 10 energy after it eats corn"""
        self.destroyFood(food)
        self.energy += 10

    def __str__(self):
        """Returns a str representation of the Chicken.
        Called automatically when the Chicken is printed.
        """
        msg = f'Chicken is in {self.get_position()}, has {self.get_width()} width and {self.get_height()} height,' \
              f' moves at {self.speed} speed with {self.energy} energy, a image of Chicken'
        return msg

    def __repr__(self):
        """Returns a printable representational string of the __str__ method."""
        return self.__str__()
