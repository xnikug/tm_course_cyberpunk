from flask import Flask, render_template_string
from assets import get_cyberpunk_art

app = Flask(__name__)

CYBERPUNK_STYLE = """
    <style>
        body {
            background-color: #0f0f0f;
            color: #00ffea;
            font-family: monospace;
            padding: 2rem;
            white-space: pre-wrap;
            font-size: 12px;
        }
        .glow {
            text-shadow: 0 0 5px #00ffea, 0 0 10px #00ffea, 0 0 20px #00ffea;
        }
    </style>
"""

@app.route("/")
def cyberpunk():
    art = get_cyberpunk_art()
    return render_template_string(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cyberpunk Terminal</title>
            {CYBERPUNK_STYLE}
        </head>
        <body>
            <div class="glow">{{{{ art }}}}</div>
        </body>
        </html>
    """, art=art)

if __name__ == "__main__":
    app.run(debug=True)
