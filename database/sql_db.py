import os
import sqlite3


class SqlDB:
    con = None  # Connection
    cur = None  # Cursor

    def __init__(self, path, is_relative=True):
        if is_relative:
            scriptdir = os.path.dirname(__file__)
            self.path = os.path.join(scriptdir, path)

            os.makedirs(os.path.dirname(self.path), exist_ok=True)
        else:
            self.path = path

        self._db_connect()

    def __del__(self):
        if self.con:
            self.db_close()

    def _db_connect(self):
        self.con = sqlite3.connect(self.path)
        self.con.row_factory = sqlite3.Row
        if self.con:
            self.cur = self.con.cursor()
        else:
            raise ConnectionError(f'Unable to connect to the database at -> {self.path}')

    def db_close(self):
        if self.con:
            self.con.close()

    def create_table(self, table_name, table_cols):
        """
        Create a table in the DB
        -> Name of table (String)
        -> Array of column statements (Array[String])
            ex. ["id integer PRIMARY KEY", "name text NOT NULL", ...]
        """
        create_statement = f'CREATE TABLE IF NOT EXISTS {table_name} ('

        num_rows = len(table_cols)
        index = 0
        for col in table_cols:
            index += 1
            if index == num_rows:
                create_statement += f' {col}'
            else:
                create_statement += f' {col},'

        create_statement += ')'

        self.cur.execute(create_statement)

    def add_column(self, table, new_col):
        """
        Add a column to a table in the DB
        -> Name of table (String)
        -> Name of the new column (String)
            ex. last_name text NOT NULL
        """
        create_statement = f'ALTER TABLE {table} ADD COLUMN {new_col}'
        self.cur.execute(create_statement)

    def select(self, statement, args=None):
        """
        Select data from the DB
        -> The SQL statment (String)
        -> A tuple of arguments to fill a prepared statement (tuple)
            Place ? where they go
            ex. "SELECT * FROM Users WHERE id=? and name=?", (id, name)
        """
        results = None
        if args:
            results = self.cur.execute(statement, args)
        else:
            results = self.cur.execute(statement)

        if results:
            return [dict(row) for row in results]
        else:
            return None

    def iud(self, statement, args=None):
        """
        Insert/Update/Delet data into the DB
        -> The SQL statment (String)
        -> A tuple of arguments to fill a prepared statement (tuple)
            Place ? where they go
            ex. "INSERT INTO Users (id, name) VALUES (?, ?)", (id, name)
        """

        if args:
            self.cur.execute(statement, args)
        else:
            self.cur.execute(statement)

        self.con.commit()

    def sql(self, statement, args=None, commit=False):
        """
        Execute arbitrary SQL
        -> The SQL statment (String)
        -> A tuple of arguments to fill a prepared statement (tuple)
            Place ? where they go
        -> Whether or not to commit to the DB (True/False)
        """
        if args:
            results = self.cur.execute(statement, args)
        else:
            results = self.cur.execute(statement)

        if commit:
            self.con.commit()

        return results
