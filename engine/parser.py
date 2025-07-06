def parse_command(command, player, room):
    if command == "look":
        room.describe()
    elif command == "inventory":
        player.show_inventory()
    elif command == "attack":
        if room.enemies:
            enemy = room.enemies[0]
            player.attack(enemy)
            if enemy.is_alive():
                enemy.attack(player)
            else:
                print(f"{enemy.get_name()} has been defeated!")
                room.enemies.remove(enemy)
        else:
            print("No enemies here.")
    elif command == "use":
        if player.inventory:
            player.inventory[0].use(player)
        else:
            print("You have nothing to use.")
    elif command == "exit":
        print("Exiting the game...")
    else:
        print("Unknown command.")
