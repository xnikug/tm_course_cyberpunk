from assets import get_room_art

def init_fight(enemy, player):
    print("\n=== FIGHT STARTED ===")
    print(get_room_art())  # Display dungeon room as battle background
    
    while enemy.hp > 0 and player.hp > 0:
        # Player's turn
        print(f"\nPlayer HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
        print("1. Attack")
        print("2. Use Item")
        action = input("Choose action (1-2): ")

        if action == "1":
            damage = 10
            print("\nYou attack!")
            enemy.hp -= damage
            print(f"Dealt {damage} damage to {enemy.name}.")
        
        elif action == "2":
            if "Sword" in player.items and "Sword" not in player.holding_item:
                player.holding_item.append("Sword")
                print("You equip the sword!")
                damage = 20  # Sword attack damage
                enemy.hp -= damage
                print(f"Dealt {damage} damage to {enemy.name} with the sword!")
            else:
                print("No usable items or sword already equipped!")
        
        # Enemy's turn (if still alive)
        if enemy.hp > 0:
            player.hp -= enemy.damage
            print(f"\n{enemy.name} attacks! Dealt {enemy.damage} damage to you.")

    # Fight outcome
    if player.hp <= 0:
        print("\nYou have been defeated!")
    elif enemy.hp <= 0:
        print(f"\nYou defeated the {enemy.name}!")