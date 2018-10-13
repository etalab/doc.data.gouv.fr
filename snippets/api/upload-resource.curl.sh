curl -H "Accept:application/json" \
     -H "X-Api-Key:$API_KEY" \
     -F "file=/chemin/vers/le/fichier" \
     -X POST $API/datasets/5bc04b2cff66bd680e499f4a/upload
