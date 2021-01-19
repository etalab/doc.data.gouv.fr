url = api_url('/datasets/{}/upload/'.format(DATASET))
response = requests.post(url, files={
    'file': open('/chemin/vers/le/fichier', 'rb'),
}, headers=HEADERS)
