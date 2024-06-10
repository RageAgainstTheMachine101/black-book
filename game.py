from constants import WELCOME_MESSAGE


class character:
    def __init__(self, name):
        self.name = input("Enter your name: ")
        self.hp = 100
        self.mp = 100
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

    def attack(self, enemy):
        pass

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.mp += 10
        self.xp_to_next_level += 50

    def gain_xp(self, xp):
        self.xp += xp
        if self.xp >= self.xp_to_next_level:
            self.level_up()

    def __str__(self):
        return f"{self.name} (Level {self.level})"

class game:
    def __init__(self):
        self.character = None

    def run(self):
        print(WELCOME_MESSAGE)

        # create a character
        self.character = character()

        # create a deck

        # generate an enemy

        # start a battle
