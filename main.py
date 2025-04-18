from flask import Flask, render_template, request
from assets import get_cyberpunk_art

app = Flask(__name__)

# Player class
class Player:
    def __init__(self, hp, items, holding_item):
        self.hp = hp
        self.items = items
        self.holding_item = holding_item

    def pick_item(self, item):
        self.items.append(item)

    def equip_item(self, item):
        if item in self.items:
            self.holding_item.append(item)
            return f"Equipped {item}!"
        return f"Item {item} not found in inventory."

player = Player(hp=100, items=[], holding_item=[])

@app.route("/")
def home():
    room = request.args.get("room", "menu")
    action = request.args.get("action", None)
    
    # Player interaction logic
    message = None
    if action == "explore":
        room = request.args.get("room", "home")
        art = get_cyberpunk_art(room)
        message = "You explore the area."
    elif action == "inventory":
        art = "Viewing inventory."
        message = f"Inventory: {player.items}, Equipped: {player.holding_item}"
    elif action == "craft":
        art = "Crafting unavailable yet."
        message = "Feature under development."
    elif action == "quit":
        art = "Goodbye, cyber-runner!"
        message = "Game Over."

    art = get_cyberpunk_art(room)
    return render_template("index.html", art=art, player=player, message=message)


if __name__ == "__main__":
    app.run(debug=True)
