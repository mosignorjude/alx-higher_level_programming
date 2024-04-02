#!/usr/bin/python3
class Robots:
    """ Represents a robot, with a name."""
    # A class variable counting the  number of robots
    population = 0

    def __init__(self, name):
        """ Initializes the data. """
        self.name = name
        print("initializing {}".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robots.population += 1

    def die(self):
            """I am dying"""
            print("{} is being destroyed!".format(self.name))
            Robots.population -= 1
            if Robots.population == 0:
                print("{} was the last one.".format(self.name))
            else:
                print("There is still {:d} robots working."
                      .format(Robots.population))

    def say_hi(self):
            """Greeting by the robot"""
            print("Greeting, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """prints the current popolation"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robots("g120")
droid1.say_hi()
Robots.how_many()

driod2 = Robots("f340")
driod2.say_hi()
Robots.how_many()

print("\nRobots can do some work here\n")
print("Robots have finised their work. so lets destroy them")
droid1.die()
Robots.how_many()
driod2.die()
Robots.how_many()
