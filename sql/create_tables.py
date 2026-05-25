from config.db_config import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    with open("sql/schema.sql", "r") as file:
        sql_script = file.read()

    cursor.execute(sql_script)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Tables created successfully")