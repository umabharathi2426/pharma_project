from config.db_config import get_connection

class InventoryService:

    def get_inventory(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT m.name, i.quantity
            FROM inventory i
            JOIN medicines m ON i.medicine_id = m.medicine_id
        """)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data