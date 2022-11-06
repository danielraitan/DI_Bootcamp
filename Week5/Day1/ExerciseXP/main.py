# 1#
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat("jerry", 3)
# cat2 = Cat("jerr", 2)
# cat3 = Cat("je", 5)

# cats = [cat1, cat2, cat3]
# oldest_cat = cats[0]

# for cat in cats:
#     if oldest_cat.age < cat.age:
#         oldest_cat=cat

# print(cat.name)

# 2#
# class Dog:

#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} woof!")
    
#     def jump(self):
#         x =self.height * 2
#         print(f"{self.name} jumps {x} cm high!")

#     def __str__(self):
#         return f"{self.name}, {self.height}"

# davids_dog = Dog("rex", 50)

# print(davids_dog)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("teacup", 20)
# print(sarahs_dog)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if sarahs_dog.height > davids_dog.height:
#     print("sarahs dog is bigger")

# elif davids_dog.height > sarahs_dog.height:
#     print("davids dog is bigger")

# 3#
# class Song:

    # def __init__(self, lyrics):
    #     self.lyrics = lyrics

#     def __str__(self):
#         return f"{self.lyrics}"
    
#     def sing_me_a_song(self):
#         print(song1)
#         print(song2)
#         print(song3)

# song1 = Song("Theres a lady who's sure")
# song2 = Song("all that glitters is gold")
# song3 = Song("and shes buying a stairway to heaven")

# song1.sing_me_a_song()

# 4#
class Zoo:
    
    def __init__(self, zoo_name):
        self.animals = ["Bear", "lion", "deer"]
        self.zoo_name = zoo_name

    def add_animal(self, new_animal):
        self.new_animal = new_animal
        if new_animal not in self.animals:
             self.animals.append(new_animal)
             print(new_animal,  "added to the zoo")

    def get_animals(self):
        print(my_zoo.animals)

    def sell_animal(self, animal_sold):
        self.new_animal = animal_sold
        if animal_sold in self.animals:
             self.animals.remove(animal_sold)
             print(animal_sold,  "removed from zoo")

    def sort_animals(self):
        sorted(my_zoo.animals)
        print(sorted(my_zoo.animals))
        

my_zoo = Zoo("my_zoo")
my_zoo.add_animal("dog")
my_zoo.add_animal("cat")
my_zoo.sell_animal("dog")
my_zoo.get_animals()
my_zoo.sort_animals()
