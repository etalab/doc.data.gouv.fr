# Create a dataset using CURL
curl -H "Content-Type:application/json" \
     -H "Accept:application/json" \
     -H "X-Api-Key:$API_KEY" \
     --data '{"title": "my title", "description": "My description"}' \
     -X POST $API/datasets/
