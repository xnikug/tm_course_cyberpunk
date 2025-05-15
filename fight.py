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
            if player.holding_item:
                item = player.holding_item[0]  # Use the first held item
                if item == "Sword":
                    damage = 20  # Sword attack damage
                    print("You equip the sword!")
                    enemy.hp -= damage
                    print(f"Dealt {damage} damage to {enemy.name} with the sword!")
                else:
                    print("You cannot use this item!")
            else:
                print("No usable items or sword already equipped!")
        
        # Enemy's turn (if still alive)
        if enemy.hp > 0:
            player.hp -= enemy.power
            print(f"\n{enemy.name} attacks! Dealt {enemy.power} damage to you.")

    # Fight outcome
    if player.hp <= 0:
        print("\nYou have been defeated!")
    elif enemy.hp <= 0:
        print(f"\nYou defeated the {enemy.name}!")
        # Optionally, add loot to player's inventory
        player.items.extend(enemy.loot_items)
        print(f"You found: {', '.join(enemy.loot_items)}")