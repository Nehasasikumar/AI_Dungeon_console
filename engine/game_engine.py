from database.db_connection import get_connection

def add_player():
    print("\n🎮 Create a New Player 🎮")
    name = input("Enter player name: ")

    # ✅ Step 1: Show available roles
    roles = ["Warrior", "Mage", "Healer", "Rogue", "Paladin"]
    print("\nAvailable Roles:")
    for idx, role in enumerate(roles, start=1):
        print(f"{idx}. {role}")

    # ✅ Step 2: Let user pick by number
    try:
        role_choice = int(input("Choose a role (number): "))
        if 1 <= role_choice <= len(roles):
            role = roles[role_choice - 1]
        else:
            print("❌ Invalid role selected.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    # ✅ Step 3: Get other details
    try:
        health = int(input("Enter player health: "))
    except ValueError:
        print("❌ Invalid health value. Please enter an integer.")
        return

    inventory = input("Enter inventory items (comma-separated): ")

    # ✅ Step 4: Save to DB
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO players (name, role, health, inventory) VALUES (%s, %s, %s, %s)"
    values = (name, role, health, inventory)

    cursor.execute(query, values)
    conn.commit()

    print(f"\n✅ Player '{name}' the {role} added successfully!\n")

    cursor.close()
    conn.close()
