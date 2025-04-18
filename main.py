from flask import Flask, render_template
from assets import get_cyberpunk_art

app = Flask(__name__)

@app.route("/")
def home():
    art = get_cyberpunk_art()
    return render_template("index.html", art=art)

if __name__ == "__main__":
    app.run(debug=True)
