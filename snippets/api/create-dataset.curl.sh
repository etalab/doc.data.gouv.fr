curl -H "Content-Type:application/json" \
     -H "Accept:application/json" \
     -H "X-Api-Key:$API_KEY" \
     --data '{"title": "my title", "description": "My description", "organization": "$ORG"}' \
     -X POST $API/datasets/
