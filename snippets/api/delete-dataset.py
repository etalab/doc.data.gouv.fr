url = api_url('/datasets/{}/'.format(DATASET))
response = requests.delete(url, headers=HEADERS)
