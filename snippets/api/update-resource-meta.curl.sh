curl -H "Content-Type:application/json" \
     -H "Accept:application/json" \
     -H "X-Api-Key:$API_KEY" \
     --data '{"title": "Nouveau titre", "description": "Nouvelle description"}' \
     -X PUT $API/datasets/$DATASET/resources/$RESOURCE/
