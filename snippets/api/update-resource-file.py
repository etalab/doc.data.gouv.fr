url = api_url('/datasets/{}/resources/{}/upload/'.format(DATASET, RESOURCE))
response = requests.post(url, files={
    'file': open('/chemin/vers/le/nouveau/fichier', 'rb'),
}, headers=HEADERS)
