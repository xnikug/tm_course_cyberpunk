from flask import Flask, render_template, request
from assets import get_cyberpunk_art

app = Flask(__name__)


@app.route("/")
def home():
    room = request.args.get("room", "home")
    art = get_cyberpunk_art(room)
    return render_template("index.html", art=art)

from player_stats import Player

if __name__ == "__main__":
    player = Player(hp=100, holding_item=[]) 

    app.run(debug=True)
