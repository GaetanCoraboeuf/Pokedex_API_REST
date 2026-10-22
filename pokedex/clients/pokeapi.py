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
            donnees_evolves_from_species_tmp = response.json()["evolves_from_species"]
            if donnees_evolves_from_species_tmp != None:
                donnees_evolves_from_species = donnees_evolves_from_species_tmp["url"].split("/")[-2]
                if int(donnees_evolves_from_species) > 151:
                    donnees_evolves_from_species = "null" # Valeur par défaut si le Pokémon n'apartient pas à la première génération
            else:
                donnees_evolves_from_species = "null"
        else:
            donnees_nom_fr = {"name":"","language":{"name":"fr","url":""}}  # Valeur par défaut si la requête échoue
            donnees_evolves_from_species = "null"
            
        for name_entry in donnees_nom_fr.get("names", []):
            if name_entry["language"]["name"] == "fr":
                name_fr = name_entry["name"]
                break
        else:
            name_fr = ""  # Valeur par défaut si le nom français n'est pas trouvé
        
        type_fr_list = []
        for type_entry in donnees["types"]:
            type = type_entry["type"]["name"]
            url = f"https://pokeapi.co/api/v2/type/{type}"
            response = requests.get(url)
            if response.status_code == 200:
                donnees_nom_type_fr_tmp = response.json()
                for name_type_entry in donnees_nom_type_fr_tmp.get("names", []):
                    if name_type_entry["language"]["name"] == "fr":
                        type_fr_list.append(name_type_entry["name"])
                        break
                else:
                    type_fr_list.append("")  # Valeur par défaut si le nom français n'est pas trouvé
        
        donnees_pokemon = {
            "number": donnees["id"],
            "name": donnees["name"],
            "name_fr": name_fr,
            "type": type_fr_list,
            "image_url": donnees["sprites"]["front_default"],
            "height": donnees["height"],
            "weight": donnees["weight"],
            "evolves_from_number": donnees_evolves_from_species,
        }
        return donnees_pokemon
    else:
        return 0