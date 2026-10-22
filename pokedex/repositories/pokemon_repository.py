import json

# Renvoie le Pokémon sous forme de dict (format du schéma Pokemon), ou None s'il n'est pas en base
def get_pokemon_by_number(db, number: int):
    row = db.execute("SELECT * FROM pokemon WHERE number = ?", (number,)).fetchone()
    if row is None:
        return None
    pokemon = dict(row)
    # SQLite stocke la liste des types en texte JSON
    pokemon["type"] = json.loads(pokemon.pop("types"))
    return pokemon

# Insère le Pokémon, ou le remplace s'il a déjà été scanné
def save_pokemon(db, pokemon: dict):
    db.execute(
        """
        INSERT OR REPLACE INTO pokemon
        (number, name, name_fr, types, image_url, height, weight, evolves_from_number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            pokemon["number"],
            pokemon["name"],
            pokemon["name_fr"],
            json.dumps(pokemon["type"], ensure_ascii=False),
            pokemon["image_url"],
            pokemon["height"],
            pokemon["weight"],
            pokemon["evolves_from_number"],
        ),
    )
    db.commit()
