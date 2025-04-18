from flask import Flask, render_template_string, request, jsonify
import traceback

app = Flask(__name__)

# Define the Room class and GameState logic
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}  # Dictionary to store direction -> Room

    def add_connection(self, direction, room):
        self.connections[direction] = room

    def get_connected_rooms(self):
        return self.connections


class GameState:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.previous_room = None  # Track the last room

    def create_rooms(self):
        # Define rooms
        self.rooms["entrance"] = Room("Entrance", "The entrance of the neon-lit cyberpunk district. Flashing signs illuminate the night.")
        self.rooms["alley"] = Room("Alley", "A narrow alleyway covered in neon graffiti. It's eerily quiet.")
        self.rooms["market"] = Room("Market", "A bustling market with vendors selling high-tech gear and gadgets.")
        self.rooms["rooftop"] = Room("Rooftop", "A rooftop overlooking the cyberpunk cityscape. Neon lights flicker below.")
        self.rooms["underground_lab"] = Room("Underground Lab", "A dark, abandoned laboratory with malfunctioning machines.")
        self.rooms["neon_park"] = Room("Neon Park", "A park with glowing, futuristic trees. It's strangely peaceful.")
        self.rooms["hacker_den"] = Room("Hacker Den", "A cluttered room filled with computer screens and digital chaos.")
        self.rooms["cyber_bar"] = Room("Cyber Bar", "A neon-lit bar thick with tension and whispered deals.")
        self.rooms["abandoned_subway"] = Room("Abandoned Subway", "A dim, eerie subway station with graffiti-covered walls.")
        self.rooms["secret_room"] = Room("Secret Room", "A hidden room with walls of encrypted data, long forgotten.")
        self.rooms["sky_lounge"] = Room("Sky Lounge", "A luxurious lounge atop a skyscraper with a breathtaking city view.")

        # Define connections
        self.rooms["entrance"].add_connection("e", self.rooms["alley"])
        self.rooms["alley"].add_connection("w", self.rooms["entrance"])
        self.rooms["alley"].add_connection("s", self.rooms["market"])
        self.rooms["market"].add_connection("n", self.rooms["alley"])
        self.rooms["market"].add_connection("e", self.rooms["underground_lab"])
        self.rooms["underground_lab"].add_connection("w", self.rooms["market"])
        self.rooms["underground_lab"].add_connection("n", self.rooms["neon_park"])
        self.rooms["neon_park"].add_connection("s", self.rooms["underground_lab"])
        self.rooms["neon_park"].add_connection("e", self.rooms["hacker_den"])
        self.rooms["hacker_den"].add_connection("w", self.rooms["neon_park"])
        self.rooms["hacker_den"].add_connection("n", self.rooms["cyber_bar"])
        self.rooms["cyber_bar"].add_connection("s", self.rooms["hacker_den"])
        self.rooms["cyber_bar"].add_connection("e", self.rooms["abandoned_subway"])
        self.rooms["abandoned_subway"].add_connection("w", self.rooms["cyber_bar"])
        self.rooms["abandoned_subway"].add_connection("n", self.rooms["secret_room"])
        self.rooms["secret_room"].add_connection("s", self.rooms["abandoned_subway"])
        self.rooms["secret_room"].add_connection("e", self.rooms["sky_lounge"])
        self.rooms["sky_lounge"].add_connection("w", self.rooms["secret_room"])

        # Starting point
        self.current_room = self.rooms["entrance"]
        self.previous_room = None

    def get_current_room(self):
        return self.current_room

    def move(self, direction):
        if not self.current_room:
            print("Error: Current room is None")
            return False
        if direction in self.current_room.connections:
            self.previous_room = self.current_room
            self.current_room = self.current_room.connections[direction]
            print(f"Moved to {self.current_room.name}")
            return True
        print(f"Invalid direction '{direction}' from {self.current_room.name}")
        return False

    def move_back(self):
        if not self.current_room:
            print("Error: Current room is None")
            return False
        if self.previous_room:
            self.current_room = self.previous_room
            self.previous_room = None
            print(f"Moved back to {self.current_room.name}")
            return True
        print("No previous room to move back to")
        return False


# Initialize the game state
game = GameState()
game.create_rooms()


# Entry page template (index.html)
index_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cyberpunk Terminal</title>
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
    <script>
        // Listen for Enter key to start the game
        document.addEventListener("keydown", function(event) {
            if (event.key === "Enter") {
                // Redirect to the game
                window.location.href = "/game";
            }
        });
    </script>
</head>
<body>
    <div class="cyberpunk-glow">
        <pre>{{ art }}</pre>
    </div>
    <p style="text-align: center;">Press "Enter" to start the game.</p>
</body>
</html>
'''

# Game interface template
game_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyberpunk Tokyo Dungeon</title>
    <style>
        body {
            font-family: monospace;
            text-align: center;
            background-color: #101010;
            color: #00ffcc;
            margin: 0;
            padding: 20px;
        }
        h1 {
            font-size: 2.5em;
            color: #ff00ff;
            text-shadow: 0 0 10px #ff00ff;
        }
        .room-description {
            margin: 20px auto;
            padding: 15px;
            border: 2px solid #ff00ff;
            border-radius: 10px;
            max-width: 600px;
            background-color: #1a1a1a;
        }
        .controls {
            margin-top: 20px;
            font-size: 1.1em;
        }
        p {
            margin: 10px 0;
        }
    </style>
    <script>
        document.addEventListener("keydown", function(event) {
            let direction = null;
            if (event.key === "w") {
                direction = "n";
            } else if (event.key === "a") {
                direction = "w";
            } else if (event.key === "s") {
                direction = "s";
            } else if (event.key === "d") {
                direction = "e";
            } else if (event.key === "b") {
                direction = "b";
            } else if (event.key === "Enter") {
                direction = "enter";
            }

            if (direction) {
                console.log("Sending direction: " + direction);
                fetch('/move', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({ direction: direction }) // Properly encoding the data
                })
                .then(response => response.json()) // Always expect JSON response
                .then(data => {
                    console.log("Response data:", data);
                    if (data.status === "success") {
                        window.location.reload(); // Reload the page if the move was successful
                    } else {
                        alert("Error: " + data.error); // Show error message if move fails
                    }
                })
                .catch(error => {
                    console.error("Fetch error:", error);
                    alert("Network error occurred");
                });
            }
        });
    </script>
</head>
<body>
    <h1>Cyberpunk Tokyo Dungeon</h1>
    <div class="room-description">
        <h2>{{ room.name }}</h2>
        <p>{{ room.description }}</p>
    </div>
    <div class="controls">
        <p>Use WASD to navigate:</p>
        <p><strong>W</strong>: North | <strong>A</strong>: West | <strong>S</strong>: South | <strong>D</strong>: East | <strong>B</strong>: Back</p>
    </div>
</body>
</html>
'''

# Route for the entry page
@app.route('/')
def index():
    return render_template_string(index_template)

# Route for the game interface
@app.route('/game')
def game_route():
    current_room = game.get_current_room()
    if not current_room:
        return jsonify({"error": "Game state error: No current room"}), 500
    return render_template_string(game_template, room=current_room)

# Route for moving between rooms
@app.route('/move', methods=['POST'])
def move():
    direction = request.form.get('direction')
    print(f"Received direction: {direction}")

    try:
        if not direction:
            return jsonify({"error": "No direction provided"}), 400

        if direction == 'b':
            if game.move_back():
                return jsonify({"status": "success"}), 200
            return jsonify({"error": "Cannot move back"}), 400

        if direction in ['n', 's', 'e', 'w']:
            if game.move(direction):
                return jsonify({"status": "success"}), 200
            return jsonify({"error": f"Cannot move {direction}"}), 400

        if direction == 'enter':
            print("Enter key pressed")
            return jsonify({"status": "enter"}), 200

        return jsonify({"error": f"Invalid direction: {direction}"}), 400

    except Exception as e:
        print(f"Error in move route: {str(e)}\n{traceback.format_exc()}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
