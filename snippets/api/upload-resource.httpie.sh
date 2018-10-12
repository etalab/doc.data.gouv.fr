# Envoie d'une nouvelle ressource
# Create a dataset using HTTPie
http -f POST $API/datasets/5bc04b2cff66bd680e499f4a/upload
    X-Api-Key:$API_KEY \
    file@/chemin/vers/le/fichier
