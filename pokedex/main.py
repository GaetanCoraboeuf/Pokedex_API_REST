#####################################
#           Pokedex API             #
# Projet créé par Gaëtan et Embroaz #
#####################################

# depandances
import requests
import json
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

# fast API start
app = FastAPI()


# modèle de données pour les pokémons
class Pokemon(BaseModel):
    number: int = Field(ge=1)  # Numéro national du Pokémon
    name: str = Field(min_length=1)  # Nom utilisé par PokéAPI
    name_fr: str = Field(min_length=1)  # Nom français du Pokémon
    type: list[str] = Field(min_length=1)  # Types du Pokémon traduits en français
    image_url: str = Field(min_length=1)  # URL de l'image par defaut du Pokémon
    height: int = Field(ge=1)  # Taille du Pokémon en centimètres
    weight: int = Field(ge=1)  # Poids du Pokémon en grammes
    evolves_from_number: int = Field(
        ge=0
    )  # Numéro national du Pokémon dont il évolue (0 si pas d'évolution)


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
