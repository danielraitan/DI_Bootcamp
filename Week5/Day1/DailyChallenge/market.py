class Farm:

    def __init__(self, macdonald):
        self.animals = []
        self.macdonald = macdonald
      
    def add_animal(self, new_animal):
         self.new_animal = new_animal
         if new_animal not in self.animals:
              self.animals.append(new_animal)

    def get_info(self):
        print(f"{self.macdonald}'s farm")
        for self in self.animals: 
          print(self)
        print("E-I-E-I-0!")

    def get_animal_types(self):
        for self in self.animals: 
          print(self)

    def get_short_info(self):
        print(f"McDonalds farm has {self.animals[0]}, {self.animals[1]} and {self.animals[2]}.")

macdonald = Farm("McDonald")
macdonald.add_animal('cow')
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat')
macdonald.get_info()

macdonald.get_animal_types()
macdonald.get_short_info()