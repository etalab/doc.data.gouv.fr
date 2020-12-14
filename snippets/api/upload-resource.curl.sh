curl -H "Accept:application/json" \
     -H "X-Api-Key:$API_KEY" \
     -F "file=@/chemin/vers/le/fichier" \
     -X POST $API/datasets/$DATASET/upload/
