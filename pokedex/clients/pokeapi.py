import requests

BASE_URL = "https://pokeapi.co/api/v2"

# Renvoie le nom français d'une entrée "names" de PokéAPI, ou le nom de secours s'il n'y en a pas
def _nom_fr(names: list, secours: str) -> str:
    for entry in names:
        if entry["language"]["name"] == "fr":
            return entry["name"]
    return secours

def _type_fr(type_name: str) -> str:
    response = requests.get(f"{BASE_URL}/type/{type_name}")
    if response.status_code != 200:
        return type_name
    return _nom_fr(response.json().get("names", []), type_name)

# Renvoie la fiche normalisée du Pokémon, ou 0 s'il est introuvable
def get_pokemon_from_api(number: int):
    response = requests.get(f"{BASE_URL}/pokemon/{number}")
    if response.status_code != 200:
        return 0
    donnees = response.json()

    name_fr = donnees["name"]
    evolves_from_number = 0
    response = requests.get(f"{BASE_URL}/pokemon-species/{number}")
    if response.status_code == 200:
        espece = response.json()
        name_fr = _nom_fr(espece.get("names", []), donnees["name"])
        parent = espece.get("evolves_from_species")
        if parent is not None:
            numero_parent = int(parent["url"].rstrip("/").split("/")[-1])
            # le projet ne garde que les évolutions internes à la génération 1
            if numero_parent <= 151:
                evolves_from_number = numero_parent

    return {
        "number": donnees["id"],
        "name": donnees["name"],
        "name_fr": name_fr,
        "type": [_type_fr(t["type"]["name"]) for t in donnees["types"]],
        "image_url": donnees["sprites"]["front_default"],
        "height": donnees["height"],
        "weight": donnees["weight"],
        "evolves_from_number": evolves_from_number,
    }
