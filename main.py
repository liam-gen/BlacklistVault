"""
main.py
--------
Point d'entrée principal de l'application.

Auteur: Liam CHARPENTIER (liam-gen)
Contributeurs:
    - liam-gen
Date: 2025-09-07
Version: 1.0

Description:
    Ce fichier contient le code principal de l'application. 
    Il initialise le serveur FastAPI, configure les routes et 
    gère les endpoints REST pour la vérification des utilisateurs 
    et IP dans les différentes blacklists.
    
Repository:
    https://github.com/liam-gen/BlacklistVault

Website:
    https://liamcharpentier.fr

Licence:
    MIT License
"""

from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException
import httpx
import json
import re
import os


app = FastAPI()

load_dotenv()

with open("services.json") as f:
    BLACKLIST_SERVICES = json.load(f)


"""
Exemple sur le root du site web
"""
@app.get("/")
def read_root():
    return {"Hello": "World"}
    
    
def get_from_path(data, path):
    """
    Convertis une string en JSON réel et l'applique à data
    
    Exemple :
        data = {"foo": {"header": [ "azerty", "hello world" ]}}
        path = foo.header.1
        sortie = "hello world"

    Args:
        data: Valeur sur laquelle on applique la recherche JSON
        path: Chaîne de caractère à compiler

    Returns:
        N'importe quel type de variable

    Raises:
        KeyError: Rien pour l'instant
    """
    
    keys = path.split(".")
    for k in keys:
        if isinstance(data, list) and k.isdigit():
            data = data[int(k)]
        elif isinstance(data, dict):
            data = data.get(k, None)
            if data is None:
                return None
        else:
            return None
    return data




#TODO : Checker si ENV[x] existe avant
def load_from_env(name):

    """
    Récupérer la valeur d'une variable ENV

    Args:
        name: Nom de la variable

    Returns:
        La valeur de la variable d'environnement si il s'agit d'une variable d'environnement 
        sinon on retourne la valeur de name

    Raises:
        KeyError: Rien pour l'instant
    """

    pattern = r"%_(.*?)_%"
    match = re.search(pattern, name)
    
    if match:
        name = os.environ.get(match.group(1), name)
    
    return name


async def check_service(service, value):
    
    """
    Aller sur ce services pour voir si l'élément est blacklisté

    Args:
        service: SERVICE (JSON)
        value: Element qu'on cherche (valeur de l'adresse ip, ...)

    Returns:
        Résultats

    Raises:
        KeyError: Rien pour l'instant
    """

    url = service["base_url"] % value
    auth = None
    if service.get("auth", {}).get("type") == "credentials":
        auth = (load_from_env(service["auth"]["username"]), load_from_env(service["auth"]["password"]))

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, auth=auth)
            resp.raise_for_status()
            
            data = None
            
            match service["type"]:
                case "dict":
                    data = resp.json()
                    result = get_from_path(data, service["scheme"])
                    
                case "regexp":
                    data = resp.text
                    matches = re.findall(service["pattern"], data)
                    result = {key: int(value) for key, value in matches}
                
            print(data)

            return {"service": service["name"], "lists": result}
        except Exception as e:
            return {"service": service["name"], "error": str(e)}
        
        
        

@app.get("/blacklist/{type}/{value}")
async def read_blacklist(type: str, value: str):
    
    """
    Lancer la recherche dans toutes les blacklists répertoriées

    Args:
        service: Type de service (ip, email, domaine, ...)
        value: Element qu'on cherche (valeur de l'adresse ip, ...)

    Returns:
        Une liste de sites JSON

    Raises:
        KeyError: Rien pour l'instant
    """
    
    type = type.lower()
    if type not in BLACKLIST_SERVICES:
        raise HTTPException(status_code=400, detail=f"Type {type} non supporté")
    
    services = BLACKLIST_SERVICES[type]
    results = []
    for service in services:
        res = await check_service(service, value)
        results.append(res)
    
    return {"type": type, "value": value, "results": results}