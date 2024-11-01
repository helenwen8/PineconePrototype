import sqlite3

def initialize_db(db_path="pinecone.db"):
    with open("schema.sql") as f:
        schema = f.read()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

def insert_test_data(db_path="pinecone.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    with open("test_data.sql", "r") as f:
        sql_script = f.read()
    
    try:
        cursor.executescript(sql_script)
        conn.commit()
        print("Test data inserted successfully.")
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        conn.close()


if __name__ == "__main__":
    initialize_db()
    insert_test_data()
