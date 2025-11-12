import sqlite3

from db.queries import BUSCAR_TODOS_PRODUCTOS, FETCH_PRODUCTOS


class Database:
    def __init__(self):
        self.conexion = self.get_conexion()
        self.initialize_tables()

    def get_conexion(self):
        self.conexion = sqlite3.connect('../productos.db')
        return self.conexion

    def initialize_conexion(self):
        self.conexion = sqlite3.connect('../productos.db')

    def initialize_tables(self):
        cursor = self.conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                descripcion TEXT NOT NULL,
                                precio REAL NOT NULL,
                                cantidad INTEGER NOT NULL)''')
        self.conexion.commit()

    def close_conexion(self):
        self.conexion.close()
        self.conexion = None

    def fetch_many(self, query, params=()):
        self.get_conexion()
        self.execute(BUSCAR_TODOS_PRODUCTOS, params)
        self.initialize_conexion()
        self.close_conexion()

    def execute(self, query, params=()):
        self.conexion = self.get_conexion()
        self.conexion.execute(query, params)
        self.initialize_conexion()
        self.close_conexion()

    def fetch_one(self, query, params=()):
        self.get_conexion()
        self.execute(FETCH_PRODUCTOS, params)
        self.initialize_conexion()
        self.close_conexion()

db = Database()