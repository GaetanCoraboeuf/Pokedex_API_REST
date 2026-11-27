from repositories.pokemon_repository import get_pokemon_by_number, save_pokemon
from clients.pokeapi import get_pokemon_from_api
def services_metier(db,number: int):
    # Vérifie si le Pokémon est déjà en base
    pokemon = get_pokemon_by_number(db, number)
    if pokemon is None:
        pokemon = get_pokemon_from_api(number)
        save_pokemon(db, pokemon)
    db.close()
    return 1