class Player:
    def __init__(self, hp, items, holding_item):
        self.hp = hp
        self.items = items  # List of items in inventory
        self.holding_item = holding_item  # List of currently held items