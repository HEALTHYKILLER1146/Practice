class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def say_species(self):
        print "I am a %s!" % self.species

class Canine(Animal):
    def howl(self):
        print "AWWWWWOOOOOOOOOOOO"
    

dog = Canine("fido","dog","woof")

dog.make_sound()
dog.howl()



babboon = Animal("chris", "babboon", "chitters")

babboon.make_sound()

babboon.say_species()

babboon.howl()
