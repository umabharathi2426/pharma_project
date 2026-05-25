from config.db_config import get_connection

def insert_sample_data():
    conn = get_connection()
    cursor = conn.cursor()

    # ✅ Clear old data (THIS SOLVES YOUR PROBLEM)
    cursor.execute("""
        DELETE FROM sales;
        DELETE FROM inventory;
        DELETE FROM suppliers;
        DELETE FROM medicines;
    """)

    # ✅ Reset IDs (optional but clean)
    cursor.execute("""
        ALTER SEQUENCE sales_sale_id_seq RESTART WITH 1;
        ALTER SEQUENCE inventory_inventory_id_seq RESTART WITH 1;
        ALTER SEQUENCE suppliers_supplier_id_seq RESTART WITH 1;
        ALTER SEQUENCE medicines_medicine_id_seq RESTART WITH 1;
    """)

    # ✅ Insert fresh data
    with open("sql/sample_data.sql", "r") as file:
        cursor.execute(file.read())

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Fresh data inserted (no duplicates)")