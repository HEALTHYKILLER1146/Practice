class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def say_species(self):
        print "I am a %s!" % self.species

dog = Animal("fido","dog","woof")

dog.make_sound()
dog.say_species()
