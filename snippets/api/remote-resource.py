url = api_url('/datasets/{}/resources/'.format(DATASET))
response = requests.post(url, json={
    'title': 'Mon titre',
    'description': 'Ma description',
    'url': 'https://url.to/ressource.csv',
    'type': 'main',
    'filetype': 'remote',
    'format': 'csv',
}, headers=HEADERS)
