url = api_url('/datasets/{}/resources/{}/'.format(DATASET, RESOURCE))
response = requests.delete(url, headers=HEADERS)
