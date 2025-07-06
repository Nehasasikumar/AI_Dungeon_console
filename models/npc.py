class NPC:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def interact(self):
        print(f"{self.name} the {self.role} has nothing to say right now.")
