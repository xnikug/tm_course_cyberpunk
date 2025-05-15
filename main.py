from flask import Flask, render_template, request

from Game import Game
from Player import Player


from assets import get_cyberpunk_art
# from player_stats import

app = Flask(__name__)

def createGame():

    player = Player(100, [], None)

    return Game(
        player = player,
    )

if __name__ == "__main__":
    app.run(debug=True)



@app.route("/")
def home():
    return render_template("index.html", art=None, room=None)


if __name__ == "__main__":
    app.run(debug=True)