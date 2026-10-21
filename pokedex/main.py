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

# help
def main():
    print("Bienvenue dans le Pokedex API !")
    print("Pour lancer le serveur, utilisez la commande : fastapi dev main.py")

# Route GET pour vérifier que l'API fonctionne
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Route GET pour récupérer les informations d'un Pokémon par son numéro
@app.get("/pokemons/{number}")
def get_pokemon(number: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url)
    if response.status_code == 200:
        donnees = response.json()

        return donnees
    else:
        return {"error": "Pokémon non trouvé"}