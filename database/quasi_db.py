import sqlite3 as sl


class MySQL:
    def __init__(self, db_name):
        self.connection = sl.connect(rf'database/{db_name}')

        with self.connection as conn:
            conn.cursor().execute("CREATE TABLE IF NOT EXISTS users ("
                                  "telegram_id INTEGER PRIMARY KEY,"
                                  "username VARCHAR(20),"
                                  "role INTEGER);")
            conn.commit()

    def add_user(self, telegram_id, username, role):
        _sql = 'INSERT OR IGNORE INTO users (telegram_id, username, role) values(?, ?, ?)'
        _data = [
            (telegram_id, username, role),
        ]
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.executemany(_sql, _data)
            conn.commit()

    def del_user(self, telegram_id):
        _sql = f"DELETE FROM users WHERE telegram_id = ?"
        _data = (telegram_id,)
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(_sql, _data)
            conn.commit()

    def get_all_users(self):
        _sql = "SELECT * FROM users;"
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(_sql)

            return cursor.fetchall()

    def get_all_admins(self):
        _sql = "SELECT * FROM users WHERE role = ?"
        _data = (1,)
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(_sql, _data)

            return cursor.fetchall()

    def availability_user(self, telegram_id):
        _sql = "SELECT telegram_id FROM users WHERE telegram_id=?"
        _data = (telegram_id,)
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(_sql, _data)

            data = cursor.fetchall()
            if not data:
                return False
            return True

    def __del__(self):
        self.connection.close()
