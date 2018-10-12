# Create a dataset with python requests

url = api_url('/datasets/')
response = requests.post(url, json={
    'title': 'Mon titre',
    'description': 'Ma description',
    'organization': ORG,
})
