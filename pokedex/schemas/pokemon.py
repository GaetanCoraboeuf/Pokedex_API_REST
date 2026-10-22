from pydantic import BaseModel, Field, EmailStr

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
