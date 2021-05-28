 
 
 
echo $GKE_SA_KEY > .gcloud-api-key.json
docker login -u _json_key --password-stdin https://gcr.io < .gcloud-api-key.json
gcloud auth activate-service-account --key-file .gcloud-api-key.json
gcloud container clusters get-credentials $GKE_CLUSTER --region=$GKE_ZONE --project $GKE_PROJECT