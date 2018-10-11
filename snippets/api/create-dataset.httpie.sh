# Create a dataset using HTTPie
http POST $API/datasets/
    Content-Type:application/json \
    Accept:application/json \
    X-Api-Key:$API_KEY \
    title="Mon titre" \
    description='Ma description"
