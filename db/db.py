import sqlite3

from sqlite3 import Connection


class Database:
    def __init__(self):
        self.conexion: Connection | None = None
        self.initialize_conexion()
        self.initialize_tables()

    def get_conexion(self):
        return self.conexion

    def initialize_conexion(self):
        if self.conexion is None:
            self.conexion = sqlite3.connect('../productos.db')

    def initialize_tables(self):
        query = '''CREATE TABLE IF NOT EXISTS productos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                descripcion TEXT NOT NULL,
                                precio REAL NOT NULL,
                                cantidad INTEGER NOT NULL)'''

        self.execute(query, ())

    def close_conexion(self):
        self.conexion.close()
        self.conexion = None

    def fetch_many(self, query, params=()):
        self.initialize_conexion()
        conexion = self.get_conexion()
        data = conexion.execute(query, params).fetchall()
        self.close_conexion()
        return data

    def execute(self, query, params=()):
        self.initialize_conexion()
        conexion = self.get_conexion()
        conexion.execute(query, params)
        conexion.commit()
        self.close_conexion()

    def fetch_one(self, query, params=()):
        self.initialize_conexion()
        conexion = self.get_conexion()
        data = conexion.execute(query, params).fetchone()
        self.close_conexion()
        return data


db = Database()
