from config.db_config import get_connection
from models.sale import Sale

class SalesService:

    def add_sale(self, sale: Sale):
        conn = get_connection()
        cursor = conn.cursor()

        total_price = sale.calculate_total()

        cursor.execute("""
            INSERT INTO sales (medicine_id, quantity_sold, sale_date, total_price)
            VALUES (%s, %s, CURRENT_DATE, %s)
        """, (sale.medicine_id, sale.quantity, total_price))

        conn.commit()
        cursor.close()
        conn.close()

        print("Sale added successfully ✅")