import random

class Item:
    def __init__(self, name, bonus_type, bonus_value):
        self.name = name
        self.bonus_type = bonus_type  # 'attack' or 'defense'
        self.bonus_value = bonus_value

    def __str__(self):
        if self.bonus_type == 'attack':
            return f"{self.name} (+{self.bonus_value} {self.bonus_type})"
        else:
            return f"{self.name} (-{round(self.bonus_value * 100)}% damage taken)"

class Inventory:
    def __init__(self):
        self.slots = [None for _ in range(9)]

    def show(self):
        for idx, item in enumerate(self.slots):
            print(f"Slot {idx + 1}: {item if item else 'Empty'}")

    def add_item(self, item):
        for i in range(9):
            if self.slots[i] is None:
                self.slots[i] = item
                print(f"Picked up: {item}")
                return True
        print("Inventory full! Cannot pick up new item.")
        return False

    def combine(self, index1, index2):
        i1, i2 = self.slots[index1], self.slots[index2]
        if not i1 or not i2:
            print("Cannot craft: One or both slots are empty.")
            return
        key = tuple(sorted([i1.name, i2.name]))
        if key in crafting_recipes:
            result = crafting_recipes[key]
            print(f"{i1.name} + {i2.name} crafted into {result.name}!")
            self.slots[index1] = result
            self.slots[index2] = None
        else:
            print(f"{i1.name} + {i2.name} cannot be crafted together.")

# Define Cyberpunk Items
cyberpunk_items = [
    Item("Neural Spike Driver", "attack", 3),
    Item("Smart Ammo Rounds", "attack", 4),
    Item("Nano-edge Blade Kit", "attack", 2),
    Item("Optical Targeting AI", "attack", 5),
    Item("Stimulant Injector", "attack", 1),
    Item("Carbon Weave Jacket", "defense", 0.2),
    Item("EMP Shield Cloak", "defense", 0.3),
    Item("Dermal Plating Mk.II", "defense", 0.4),
    Item("Kinetic Pulse Shell", "defense", 0.5),
    Item("Liquid Armor Vest", "defense", 0.1),
]

# Example Crafting Results
crafted_items = {
    ("Neural Spike Driver", "Optical Targeting AI"): Item("Neural Sniper System", "attack", 6),
    ("Smart Ammo Rounds", "Nano-edge Blade Kit"): Item("Smart Melee Hybrid", "attack", 5),
    ("EMP Shield Cloak", "Kinetic Pulse Shell"): Item("Adaptive Barrier System", "defense", 0.6),
    ("Carbon Weave Jacket", "Liquid Armor Vest"): Item("Advanced Hybrid Vest", "defense", 0.4),
}

crafting_recipes = {tuple(sorted(k)): v for k, v in crafted_items.items()}

# Setup empty inventory and item pickup index
inv = Inventory()
pickup_index = 0  # Tracks which item to give next

# Main loop
while True:
    cmd = input("\nCommand (e=inventory, c=craft, p=pickup item, q=quit): ").strip().lower()

    if cmd == "e":
        print("\n--- Inventory ---")
        inv.show()

    elif cmd == "c":
        print("\n--- Crafting Mode ---")
        inv.show()
        combo = input("Enter combination (e.g., 1+2): ")
        if '+' in combo:
            try:
                a, b = map(int, combo.split('+'))
                inv.combine(a - 1, b - 1)
            except:
                print("Invalid input format.")
        else:
            print("Invalid format. Use x+y to craft.")

    elif cmd == "p":
        if pickup_index < len(cyberpunk_items):
            item = cyberpunk_items[pickup_index]
            inv.add_item(item)
            pickup_index += 1
        else:
            print("No more items left to pick up.")

    elif cmd == "q":
        print("Goodbye, cyber-runner!")
        break

    else:
        print("Unknown command.")
