import sqlite3
from pathlib import Path

# chemin absolu : la base est trouvée quel que soit le dossier de lancement
DB_PATH = Path(__file__).resolve().parent.parent / "pokedex.db"

def get_connection():
    connexion = sqlite3.connect(DB_PATH)
    connexion.row_factory = sqlite3.Row
    return connexion

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon (
    number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    name_fr TEXT NOT NULL,
    types TEXT NOT NULL,
    image_url TEXT NOT NULL,
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    evolves_from_number INTEGER
    );
    ''')
    connection.commit()
