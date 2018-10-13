url = api_url('/datasets/{}/'.format(DATASET))
response = requests.put(url, json={
    'title': 'Nouveau titre',
    'description': 'Nouvelle description',
}, headers=HEADERS)
