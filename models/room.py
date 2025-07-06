class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.enemies = []

    def add_item(self, item):
        self.items.append(item)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def describe(self):
        print(f"\n📍 {self.name}")
        print(self.description)
        if self.items:
            print("Items in room:")
            for item in self.items:
                print(f"- {item.name}")
        if self.enemies:
            print("Enemies here:")
            for enemy in self.enemies:
                print(f"- {enemy.get_name()}")
