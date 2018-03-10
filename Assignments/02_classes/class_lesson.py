class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def say_species(self):
        print "I am a %s!" % self.species

    def say_name(self):
        print "My name is %s!" % self.name

bear = Animal("tiger", "bear", "roar")

bear.make_sound()

bear.say_name()

bear.say_species()

babboon = Animal("chris", "babboon", "chitters")

babboon.make_sound()

babboon.say_name()

babboon.say_species()

