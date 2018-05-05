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
        print("Noise: ", str(self.noise))
        print("Main_product: ", str(self.main_product))
        print("Add product: ", str(self.add_product))
        print("Meat yield: ", str(self.meat_yield()))


class Poultry(Pet):
    location = "coop"
    add_product = "eggs"
    color = "wight"
    weight = 5

    def __init__(self, coefficient, noise):
        self.coefficient = coefficient
        self.noise = noise


class DomesticCattle(Pet):
    location = "stable"

    def __init__(self, add_product, weight, noise):
        self.add_product = add_product
        self.weight = weight
        self.noise = noise


cow = DomesticCattle("milk", 50, "moo")
goat = DomesticCattle("milk", 20, "baa")
goat.color = "wight"
sheep = DomesticCattle("wool", 35, "baa")
pig = DomesticCattle("fat", 20, "oink")
duck = Poultry(0.5, "quack")
chicken = Poultry(0.7, "cluck")
chicken.color = "black"
goose = Poultry(0.8, "honk")
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
