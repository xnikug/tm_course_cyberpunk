
class Enemy:
    def __init__(self, name, strength, weakness, hp, power, loot_items):
        self.name = name
        self.strength = strength
        self.weakness = weakness
        self.hp = hp  # Enemy's health points
        self.power = power  # Enemy's attack power
        self.loot_items = loot_items  # List of items dropped upon defeat

class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue  # Dialogue that the NPC can say

    def speak(self):
        return f"{self.name} says: {self.dialogue}"

class GameObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description  # Description of the object

    def inspect(self):
        return f"{self.name}: {self.description}"