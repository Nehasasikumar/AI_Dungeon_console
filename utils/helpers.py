from database.db_connection import get_connection

def save_player_to_db(player):
    conn = get_connection()
    cursor = conn.cursor()

    inventory_str = ",".join([item.name for item in player.inventory])
    cursor.execute("""
        INSERT INTO players (name, role, health, inventory)
        VALUES (%s, %s, %s, %s)
    """, (player.get_name(), player.role, player.get_health(), inventory_str))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Player saved to database.")
