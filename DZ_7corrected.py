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

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def meat_yield(self):
        return round(self.weight * self.coefficient)

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
    coefficient = 0.6


class DomesticCattle(Pet):
    location = "stable"


class Cow(DomesticCattle):
    noise = "moo"
    add_product = "milk"


class Goat(DomesticCattle):
    noise = "baa"
    add_product = "milk"


class Sheep(DomesticCattle):
    noise = "baa"
    add_product = "wool"


class Pig(DomesticCattle):
    noise = "oink"
    add_product = "fat"


class Duck(Poultry):
    noise = "quack"


class Chicken(Poultry):
    noise = "cluck"


class Goose(Poultry):
    noise = "honk"


cow1 = Cow(40, "wight")
cow2 = Cow(48, "brown")
goat1 = Goat(15, "black")
sheep1 = Sheep(22, "wight")
pig1 = Pig(5, "pink")
duck1 = Duck(7, "brown")
chicken1 = Chicken(3, "wight")
goose1 = Goose(8, "wight")

print("Domestic_cattle - Cow")
print(cow1.inf())
print(cow2.inf())
print("Domestic_cattle - Goat")
print(goat1.inf())
print("Domestic_cattle - Sheep")
print(sheep1.inf())
print("Domestic_cattle - Pig")
print(pig1.inf())
print("Poultry - Duck")
print(duck1.inf())
print("Poultry - Chicken")
print(chicken1.inf())
print("Poultry - Goose")
print(goose1.inf())