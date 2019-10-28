curl -H "Accept:application/json" \
     -H "X-Api-Key:$API_KEY" \
     -F "file=@/chemin/vers/le/nouveau/fichier" \
     -X POST $API/datasets/$DATASET/resources/$RESOURCE/upload/
