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
        self.equipped_attack = None
        self.equipped_defense = None

    def show(self):
        print("\n--- Inventory ---")
        for idx, item in enumerate(self.slots):
            print(f"Slot {idx + 1}: {item if item else 'Empty'}")
        print("\n--- Equipped ---")
        print(f"Weapon: {self.equipped_attack if self.equipped_attack else 'None'}")
        print(f"Armor : {self.equipped_defense if self.equipped_defense else 'None'}")

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

    def equip(self, slot, slot_type):
        if slot < 0 or slot >= len(self.slots):
            print("Invalid slot.")
            return
        item = self.slots[slot]
        if not item:
            print("Slot is empty.")
            return
        if slot_type == 'a' and item.bonus_type == 'attack':
            if self.equipped_attack:
                print(f"Unequipped {self.equipped_attack.name}")
            self.equipped_attack = item
            self.slots[slot] = None
            print(f"Equipped {item.name} as weapon.")
        elif slot_type == 'd' and item.bonus_type == 'defense':
            if self.equipped_defense:
                print(f"Unequipped {self.equipped_defense.name}")
            self.equipped_defense = item
            self.slots[slot] = None
            print(f"Equipped {item.name} as armor.")
        else:
            print("Item cannot be equipped in that slot type.")

    def unequip(self, slot_type):
        if slot_type == 'a' and self.equipped_attack:
            if self.add_item(self.equipped_attack):
                print(f"Unequipped {self.equipped_attack.name}")
                self.equipped_attack = None
        elif slot_type == 'd' and self.equipped_defense:
            if self.add_item(self.equipped_defense):
                print(f"Unequipped {self.equipped_defense.name}")
                self.equipped_defense = None
        else:
            print("Nothing to unequip or inventory is full.")

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

# Crafting recipes
crafted_items = {
    ("Neural Spike Driver", "Optical Targeting AI"): Item("Neural Sniper System", "attack", 6),
    ("Smart Ammo Rounds", "Nano-edge Blade Kit"): Item("Smart Melee Hybrid", "attack", 5),
    ("EMP Shield Cloak", "Kinetic Pulse Shell"): Item("Adaptive Barrier System", "defense", 0.6),
    ("Carbon Weave Jacket", "Liquid Armor Vest"): Item("Advanced Hybrid Vest", "defense", 0.4),
}
crafting_recipes = {tuple(sorted(k)): v for k, v in crafted_items.items()}

# Setup
inv = Inventory()
pickup_index = 0

# Main loop
while True:
    cmd = input("\nCommand (e=inventory, c=craft, p=pickup, eq a/d <slot>, uneq a/d, q=quit): ").strip().lower()

    if cmd == "e":
        inv.show()

    elif cmd == "c":
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

    elif cmd.startswith("eq "):
        parts = cmd.split()
        if len(parts) == 3 and parts[1] in ['a', 'd']:
            try:
                slot = int(parts[2]) - 1
                inv.equip(slot, parts[1])
            except:
                print("Invalid slot number.")
        else:
            print("Use format: eq a 3 or eq d 5")

    elif cmd.startswith("uneq "):
        parts = cmd.split()
        if len(parts) == 2 and parts[1] in ['a', 'd']:
            inv.unequip(parts[1])
        else:
            print("Use format: uneq a or uneq d")

    elif cmd == "q":
        print("Goodbye, cyber-runner!")
        break

    else:
        print("Unknown command.")