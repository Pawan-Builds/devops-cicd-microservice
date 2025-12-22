#!/bin/bash

kubectl apply -f k8s/namespace.yaml

helm upgrade --install microservice helm/microservice \
  --namespace devops-demo \
  --set image.repository=ghcr.io/YOUR_GITHUB_USERNAME/devops-cicd-microservice
