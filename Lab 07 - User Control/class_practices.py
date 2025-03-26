class Cat:
    def __init__(self, name, weight, color):
        self.name = str(input("What is the name of your cat? "))
        self.weight = int(input("How much does your cat weigh? (Number in pounds) "))
        self.color = str(input("What color is your cat? "))

    def meow(self):
        print(self.name, "is", self.color, "and he weighs", self.weight, "pounds. He says meow\n")


class Monster:
    def __init__(self, name, health):
        self.name = str(input("What is the name of the monster? "))
        self.health = int(input("How much health does he have? (Enter a number) "))

    def decrease_health(self):
        self.health -= 4
        print(self.name, "took 4 damage.")
        if self.health < 1:
            print(self.name, "has been defeated\n")
        else:
            print(self.name, "has", self.health, "health remaining.\n")


class Star:
    def __init__(self, name, star):
        self.name = str(input("What is the name of your star? "))  # gonna be a string
        self.star = star  # gonna be a string

    def birth(self):
        print("A star has been born! It's name is", self.name, "and it's a", self.star)


def main():
    new_cat = Cat("Giggleshitter", 8, "brown")
    new_cat.meow()

    new_monster = Monster("Godzilla", 13)
    new_monster.decrease_health()

    new_star = Star("Kirby", "red supergiant")
    new_star.birth()

main()
