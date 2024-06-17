## 🚀 ML Model Deployment on Docker and Kubernetes

## 📁 1. Navigate to `kubernetes_notes`

Move to the 'kubernetes_notes' directory:

```sh
cd Deploying-ML-with-FastAPI-on-Docker-Kubernetes
```

##🐋 2. Deploy on Docker

## 🔨 2.1. Build Image

## Set Docker environment to Minikube
eval $(minikube docker-env)

## Build the Docker image
```sh
docker image build -t ml-prediction-with-fastapi:1.0 .
```
## ▶️ 2.2. Run Container

## Run the container
```sh
docker run --rm \
  --name ml-prediction \
  -p 8002:8000 -d ml-prediction-with-fastapi:1.0
```
## 🔍 2.3. Prediction

## Make a prediction

```sh
curl -X 'POST' \
  'http://127.0.0.1:8002/prediction/iris' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "SepalLengthCm": 5.1,
  "SepalWidthCm": 3.5,
  "PetalLengthCm": 1.4,
  "PetalWidthCm": 0.2
}'
```
## Expected output: "Iris-setosa"

## 🛑 2.4. Stop Docker Container
```sh
# Stop the running Docker container
docker container stop ml-prediction
```
## More information: https://fastapi.tiangolo.com/deployment/docker/

## ☸️ 3. Minikube

## Apply Kubernetes deployment configuration
```sh
kubectl apply -f ml-prediction-deployment.yaml
```
## 🔧 3.1. Create Service

## Create a NodePort service for the deployment
```sh
kubectl create service nodeport ml-prediction --tcp=8000:8000
kubectl get services
```
## Expected output:
  NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
  kubernetes      ClusterIP   10.96.0.1      <none>        443/TCP          6h24m
  ml-prediction   NodePort    10.99.159.87   <none>        8000:31647/TCP   72s

## 🌐 4. Prediction on Minikube NodePort
```sh
### Make a prediction using the Minikube NodePort service
curl -X 'POST' \
  'http://192.168.49.2:30833/prediction/iris' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "SepalLengthCm": 5.1,
  "SepalWidthCm": 3.5,
  "PetalLengthCm": 1.4,
  "PetalWidthCm": 0.2
}'
```
### Expected output: "Iris-setosa"

## 🌐 5. Ingress

## Enable Ingress addon in Minikube
```sh
minikube addons enable ingress
```
## Apply the Ingress resource
```sh
kubectl apply -f ingress-ml-prediction.yaml
```

## Add the following line to /etc/hosts
```sh
sudo vim /etc/hosts

#### 192.168.49.2    ml.prediction.vbo.local
```
### Test the prediction through Ingress
```sh
curl -X 'POST' \
  'http://ml.prediction.vbo.local/prediction/iris' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "SepalLengthCm": 5.1,
  "SepalWidthCm": 3.5,
  "PetalLengthCm": 1.4,
  "PetalWidthCm": 0.2
}'
```
