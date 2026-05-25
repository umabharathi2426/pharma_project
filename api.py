# ✅ IMPORTS
from fastapi import FastAPI
from config.db_config import get_connection

# ✅ CREATE APP FIRST (IMPORTANT)
app = FastAPI()


# ✅ ADD SALE (ONLY DATABASE — no CSV)
@app.post("/add-sale")
def add_sale(medicine_id: int, quantity: int, price: float):

    conn = get_connection()
    cursor = conn.cursor()

    total_price = quantity * price

    cursor.execute("""
        INSERT INTO sales (medicine_id, quantity_sold, sale_date, total_price)
        VALUES (%s, %s, CURRENT_DATE, %s)
    """, (medicine_id, quantity, total_price))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Sale added to DB ✅"}
