from .character import Character

class Zombie(Character):
    def __init__(self):
        super().__init__("Zombie", 50)

    def attack(self, target):
        print(f"{self._name} bites you!")
        target.take_damage(10)
