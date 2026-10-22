import requests

def get_pokemon_from_api(number: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url)
    if response.status_code == 200:
        donnees = response.json()
        url = f"https://pokeapi.co/api/v2/pokemon-species/{number}"
        response = requests.get(url)
        if response.status_code == 200:
            donnees_nom_fr = response.json()
        else:
            donnees_nom_fr = {"names": [{"name": ""}]}  # Valeur par défaut si la requête échoue
            
        donnees_pokemon = {
            "number": donnees["id"],
            "name": donnees["name"],
            "name_fr": donnees_nom_fr["names"][4]["name"],
            "type": [t["type"]["name"] for t in donnees["types"]],
            "image_url": donnees["sprites"]["front_default"],
            "height": donnees["height"],
            "weight": donnees["weight"],
            "evolves_from_number": 0,  # À remplir si nécessaire
        }
        return donnees_pokemon
    else:
        return 0