# Tous les examples Python sont executés avec cette convention

import requests  # installé avec `pip install requests`

API = 'https://www.data.gouv.fr/api/1'
API_KEY = 'my-api-key'
ORG = '5bbb6d6cff66bd4dc17bfd5a'
DATASET = '5bc04b2cff66bd680e499f4a'
RESOURCE = '54d47250-1daf-483b-965a-3013f8c76617'
HEADERS = {
    'X-API-KEY': API_KEY,
}


def api_url(path):
    return ''.join(API, path)
