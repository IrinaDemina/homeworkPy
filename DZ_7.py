
# =============================================================================
# Необходимо реализовать классы животных на ферме:
# 
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.
# =============================================================================

class Pet:
    color = "not defined"
    position = "farm"
    main_product = "meat"
    coefficient = 0.8

    def meat_yield(self):
        return self.weight * self.coefficient
           
    def inf(self):
       print("Color: ", str(self.color))
       print("Position: ", str(self.position))
       print("Location: ", str(self.location))
       print("Main_product: ", str(self.main_product))
       print("Add product: ", str(self.add_product))
       print("Meat yield: ", str(self.meat_yield()))

class Poultry(Pet):
    location = "coop"
    add_product = "eggs"
    color = "wight"
    weight = 5
    
    def __init__(self, coefficient):
       self.coefficient = coefficient

class Domestic_cattle(Pet):
    location = "stable"

    def __init__(self, add_product, weight):
       self.add_product = add_product
       self.weight = weight


cow = Domestic_cattle("milk", 50)
goat = Domestic_cattle("milk", 20)
goat.color = "wight"
sheep = Domestic_cattle("wool", 35)
pig = Domestic_cattle("fat", 20)
duck = Poultry(0.5)
chicken = Poultry(0.7)
chicken.color = "black"
goose = Poultry(0.8)
goose.weight = 10

print("Domestic_cattle - cow")
print(cow.inf())
print("Domestic_cattle - goat")
print(goat.inf())
print("Domestic_cattle - sheep")
print(sheep.inf())
print("Domestic_cattle - pig")
print(pig.inf())
print("Poultry - duck")
print(duck.inf())
print("Poultry - chicken")
print(chicken.inf())
print("Poultry - goose")
print(goose.inf())