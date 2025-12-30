#!/bin/bash

# Build Docker image for Minikube
eval $(minikube docker-env)
docker build -t microservice:latest ./app/

kubectl apply -f k8s/namespace.yaml

helm upgrade --install microservice helm/microservice \
  --namespace devops-demo \
  --set image.repository=microservice \
  --set image.tag=latest \
  --set image.pullPolicy=Never
