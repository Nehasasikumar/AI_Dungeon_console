from .character import Character

class Player(Character):
    def __init__(self, name, role):
        super().__init__(name, 100)
        self.role = role
        self.inventory = []

    def attack(self, target):
        print(f"{self._name} slashes with their sword!")
        target.take_damage(15)

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if self.inventory:
            print("🎒 Inventory:")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print("Your inventory is empty.")
