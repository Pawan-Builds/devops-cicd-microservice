# DevOps CI/CD Microservice Project

## Overview
This project demonstrates a complete CI/CD pipeline that builds, containerizes,
and deploys a microservice application to Kubernetes using GitHub Actions, Docker,
and Helm.

## Tech Stack
- GitHub Actions
- Docker
- Kubernetes
- Helm
- Python (Flask)

## Workflow
1. Developer pushes code to GitHub
2. GitHub Actions builds Docker image
3. Image is pushed to GitHub Container Registry
4. Application is deployed to Kubernetes using Helm

## How to Run Locally
```bash
minikube start
./scripts/local-deploy.sh
