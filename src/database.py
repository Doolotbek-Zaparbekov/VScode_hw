import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expense (
                    id INTEGER PRIMARY KEY,
                    cause TEXT NOT NULL,
                    quantity INTEGER
                )
            """)

    def add_expense(self, cause: str, quantity: int):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO expense (cause, quantity) VALUES (?, ?)
                """,
                (cause, quantity)
            )
            conn.commit()

    def delete_expense(self, expense_id: int):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "DELETE FROM expense WHERE id = ?",
                (expense_id,)
            )
            conn.commit()

    def get_all_expenses(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.execute("SELECT id, cause, quantity FROM expense")
            return cursor.fetchall()

    def get_total_expense(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.execute("SELECT SUM(quantity) FROM expense")
            result = cursor.fetchone()[0]
            return result if result else 0