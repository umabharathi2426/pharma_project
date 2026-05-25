from config.db_config import get_connection
import pandas as pd

def display_all_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema='public';
    """)

    tables = cursor.fetchall()

    print("\n📊 DATABASE TABLES:")
    for t in tables:
        print("✔", t[0])

    cursor.close()

    for t in tables:
        df = pd.read_sql(f"SELECT * FROM {t[0]};", conn)

        print(f"\n==============================")
        print(f"TABLE: {t[0].upper()}")
        print(f"==============================")

        if df.empty:
            print("No Data Available")
        else:
            print(df.to_string(index=False))

    conn.close()

