from abstract_class import Animal


# example of python inheritance

class Dog(Animal):
    def make_sound(self):
        print("A dog barks like Woof! Woof!")

    def eat(self):
        print("The dof is eating pedigree")

    def sleep(self):
        print("Dog is sleeping")

    def move(self):
        print("Dog is running and walking")

    @staticmethod
    def _play():
        print("Dog is playing fetch")


class Cat(Animal):
    def make_sound(self):
        print("A cat meows like Meow!")

    def eat(self):
        print("The cat is eating fish")

    def sleep(self):
        print("Cat is sleeping")

    def move(self):
        print("Cat is running and walking")


class Fish(Animal):
    def make_sound(self):
        print("The fish makes sounds like Blub!")

    def eat(self):
        print("Fish is eating fish food")

    def sleep(self):
        print("Fish do not sleep")

    def move(self):
        print("Fish is swimming in the ocean")


animal_dog = Dog()
animal_dog.make_sound()
animal_dog.eat()
animal_dog.sleep()
animal_dog.move()
animal_dog._play()
print('-' * 20)

animal_cat = Cat()
animal_cat.make_sound()
animal_cat.eat()
animal_cat.sleep()
animal_cat.move()
print('-' * 20)

animal_fish = Fish()
animal_fish.make_sound()
animal_fish.eat()
animal_fish.sleep()
animal_fish.move()
print('-' * 20)
