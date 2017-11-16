class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display_health(self):
        print("Health: ", self.health)
        print("")

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print("I am a Dragon")

Animal1 = Animal("Werewolf", 200)
Animal1.walk().walk().walk().run().run().display_health()

Dog1 = Dog("Winston")
Dog1.walk().walk().walk().run().run().pet().display_health()

Dragon1 = Dragon("Thor")
Dragon1.display_health()
