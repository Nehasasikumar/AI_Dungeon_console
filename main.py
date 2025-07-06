from engine.game_engine import add_player

def main():
    while True:
        print("====== AI Dungeon Menu ======")
        print("1. Add New Player")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
