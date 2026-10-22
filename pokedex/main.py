#####################################
#           Pokedex API             #
# Projet créé par Gaëtan et Embroaz #
#####################################

# depandances
import requests
import json
from fastapi import FastAPI
from schemas.pokemon import Pokemon
from db.database import get_connection
from repositories.pokemon_repository import get_pokemon_by_number
# depends:db  

# fast API start
app = FastAPI()

# help
def main():
    print("Bienvenue dans le Pokedex API !")
    print("Pour lancer le serveur, utilisez la commande : fastapi dev main.py")


# Route GET pour vérifier que l'API fonctionne
@app.get("/health")
def health_check():
    return {"status": "ok"}


# Route GET pour récupérer les informations d'un Pokémon par son numéro
@app.get("/pokemons/{number}", response_model=Pokemon)
def get_pokemon(number: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url)
    if response.status_code == 200:
        donnees = response.json()
        donnees_pokemon = {
            "number": donnees["id"],
            "name": donnees["name"],
            "name_fr": donnees["species"]["name"],
            "type": [t["type"]["name"] for t in donnees["types"]],
            "image_url": donnees["sprites"]["front_default"],
            "height": donnees["height"],
            "weight": donnees["weight"],
            "evolves_from_number": 0,  # À remplir si nécessaire
        }
        return donnees_pokemon
    else:
        return {"error": "Pokémon non trouvé"}
