# README.md

# Cyberpunk Adventure Game

## Overview
This project is a text-based adventure game set in a cyberpunk universe. Players navigate through various rooms, interact with NPCs, collect items, and engage in combat. The game is built using Python and Flask, providing a web-based interface for players.

## Features
1. **Navigation**: Players can move between different rooms, each with unique ASCII art representations.
2. **Combat System**: Engage in battles with enemies using a turn-based combat system.
3. **Inventory Management**: Collect and manage items, with the ability to craft new items from existing ones.
4. **NPC Interactions**: Encounter non-player characters (NPCs) that players can interact with for quests or information.
5. **Dynamic Room Art**: ASCII art changes based on the player's current location, enhancing the visual experience.

## File Structure
- **assets.py**: Contains functions for retrieving ASCII art for different rooms.
- **fight.py**: Manages combat mechanics between players and enemies.
- **inventory.py**: Defines item and inventory management systems.
- **main.py**: Entry point for the Flask web application.
- **player_stats.py**: Defines player and enemy classes, including attributes and behaviors.
- **templates/index.html**: HTML template for the web application interface.
- **static/css/style.css**: CSS styles for the web application.
- **static/js/script.js**: JavaScript for enhancing interactivity.
- **.gitignore**: Specifies files and directories to ignore in version control.
- **README.md**: Documentation for the project.

## Getting Started
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application with `python main.py`.
4. Open your web browser and navigate to `http://127.0.0.1:5000` to start playing.

## Future Enhancements
- Implement a more complex room management system.
- Add more NPCs with unique dialogues and quests.
- Expand the crafting system to include more item combinations.
- Improve the combat system with different attack types and strategies.

## License
This project is licensed under the MIT License.