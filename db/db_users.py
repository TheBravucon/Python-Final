import sqlite3

from queries_users import *


class DatabaseUsers:
    def __init__(self):
        self.conexion_users = self.get_conexion_users()
        self.initialize_tables_users()

    def get_conexion_users(self):
        self.connect = sqlite3.connect('usuarios.db')
        return self.connect

    def initialize_conexion_users(self):
        self.connect = sqlite3.connect('usuarios.db')

    def initialize_tables_users(self):
        cursor = self.connect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                usuario TEXT NOT NULL,
                                contrasenia TEXT NOT NULL)''')
        self.connect.commit()

    def close_conexion_users(self):
        self.connect.close()
        self.connect = None

    def fetch_many_users(self, query, params=()):
        self.get_conexion_users()
        self.execute_users(BUSCAR_TODOS_USERS, params)
        self.initialize_conexion_users()
        self.close_conexion_users()

    def execute_users(self, query, params=()):
        self.connect = self.get_conexion_users()
        self.connect.execute(query, params)
        self.initialize_conexion_users()
        self.close_conexion_users()

    def fetch_one_user(self, query, params=()):
        self.get_conexion_users()
        self.execute_users(FETCH_USERS, params)
        self.initialize_conexion_users()
        self.close_conexion_users()