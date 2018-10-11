# All python snippets assume the following declarations

import requests  # Installed with `pip install requests`

API = 'https://www.data.gouv.fr/api/1'
API_KEY = 'my-api-key'
ORG = '5bbb6d6cff66bd4dc17bfd5a'


def api_url(path):
    return ''.join(API, path)
