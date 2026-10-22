import sqlite3

def get_connection():
    connexion = sqlite3.connect("database.db")
    connexion.row_factory = sqlite3.Row
    return connexion

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1
    );
    ''')
    connection.commit()