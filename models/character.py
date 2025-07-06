from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health):
        self._name = name
        self._health = health

    @abstractmethod
    def attack(self, target):
        pass

    def take_damage(self, amount):
        self._health -= amount
        print(f"{self._name} takes {amount} damage. Health: {self._health}")

    def is_alive(self):
        return self._health > 0

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health
