import sqlite3 

class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS todos(
                    id INTEGER PRIMERY KEY,
                    cause TEXT NOT NULL,
                    quantity INTEGER
                    )
        """)