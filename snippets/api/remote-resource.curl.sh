curl -H "Content-Type:application/json" \
     -H "Accept:application/json" \
     -H "X-Api-Key:$API_KEY" \
     --data '{"title": "my title", "description": "My description", "type": "main", filetype: "remote", "format": "csv",  "url": "https://url.to/ressource.csv"}' \
     -X POST $API/datasets/$DATASET/resources/
