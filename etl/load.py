from config.db_config import get_connection

def load(med, sup, inv, sales):

    conn = get_connection()
    cursor = conn.cursor()

    # ✅ CLEAN TABLES PROPERLY
    cursor.execute("""
        TRUNCATE TABLE sales, inventory, suppliers, medicines RESTART IDENTITY CASCADE;
    """)

    # ✅ INSERT MEDICINES FIRST
    print("Inserting medicines...")
    for _, row in med.iterrows():
        cursor.execute("""
            INSERT INTO medicines (name, category, price)
            VALUES (%s, %s, %s)
        """, (row["name"], row["category"], float(row["price"])))

    # ✅ COMMIT (VERY IMPORTANT)
    conn.commit()

    # ✅ INSERT SUPPLIERS
    print("Inserting suppliers...")
    for _, row in sup.iterrows():
        cursor.execute("""
            INSERT INTO suppliers (name, contact)
            VALUES (%s, %s)
        """, (row["name"], row["contact"]))

    conn.commit()

    # ✅ INSERT INVENTORY
    print("Inserting inventory...")
    for _, row in inv.iterrows():
        cursor.execute("""
            INSERT INTO inventory (medicine_id, supplier_id, quantity, last_updated)
            VALUES (%s, %s, %s, CURRENT_DATE)
        """, (
            int(row["medicine_id"]),
            int(row["supplier_id"]),
            int(row["quantity"])
        ))

    conn.commit()

    # ✅ INSERT SALES
    print("Inserting sales...")
    for _, row in sales.iterrows():
        cursor.execute("""
            INSERT INTO sales (medicine_id, quantity_sold, sale_date, total_price)
            VALUES (%s, %s, CURRENT_DATE, %s)
        """, (
            int(row["medicine_id"]),
            int(row["quantity"]),
            float(row["total_price"])
        ))

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Data Loaded Successfully (No FK errors)")