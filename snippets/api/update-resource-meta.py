url = api_url('/datasets/{}/resources/{}/'.format(DATASET, RESOUCE))
response = requests.put(url, json={
    'title': 'Nouveau titre',
    'description': 'Nouvelle description',
}, headers=HEADERS)
