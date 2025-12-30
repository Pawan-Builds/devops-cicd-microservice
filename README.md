# 🚀 DevOps CI/CD Microservice (End-to-End Pipeline)

![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-blue)
![Helm](https://img.shields.io/badge/Packaging-Helm-blue)
![Registry](https://img.shields.io/badge/Registry-GHCR-blue)

---

## 📌 Overview

This project demonstrates a **production-style DevOps CI/CD pipeline** that automatically builds, containerizes, and deploys a **Python Flask microservice** to **Kubernetes** using **GitHub Actions**, **Docker**, **Helm**, and **GitHub Container Registry (GHCR)**.

The entire setup is **reproducible**, **immutable**, and **observable**, closely mirroring real-world DevOps practices used in modern engineering teams.

---

## 🧠 What This Project Demonstrates

* ✅ CI/CD pipeline using **GitHub Actions**
* ✅ Docker image build & push to **GHCR**
* ✅ **SHA-based image tagging** (immutable deployments)
* ✅ Kubernetes deployment using **Helm**
* ✅ **Liveness & Readiness probes**
* ✅ Service exposure via **Minikube**
* ✅ Full environment reproducibility from a Git clone

---

## 🏗️ Architecture

```
Developer → GitHub → GitHub Actions
                ↓
          Docker Build
                ↓
     GitHub Container Registry
                ↓
          Helm Deployment
                ↓
        Kubernetes (Minikube)
```

---

## 🔁 CI/CD Workflow

1. Developer pushes code to GitHub
2. GitHub Actions pipeline:

   * Builds Docker image
   * Tags image with **commit SHA**
   * Pushes image to GHCR
3. Helm deploys the exact image version to Kubernetes
4. Kubernetes health checks validate the deployment

---

## 🚀 How to Run Locally (From Scratch)

> Even if the entire project folder is deleted, this setup will work.

```bash
# Clone the repository
git clone https://github.com/Pawan-Builds/devops-cicd-microservice.git
cd devops-cicd-microservice

# Start Kubernetes cluster
minikube start

# Deploy the application
./scripts/local-deploy.sh

# Access the service
minikube service microservice -n devops-demo
```

---

## 🔍 Health Checks

The application exposes the following endpoint:

```
/health
```

Used by Kubernetes for:

* **Readiness Probe** – controls traffic routing
* **Liveness Probe** – enables self-healing

---

## 📦 Docker Images

Docker images are published to **GitHub Container Registry** using **immutable commit SHA tags**:

```
ghcr.io/pawan-builds/devops-cicd-microservice:<commit-sha>
```

This guarantees:

* Reproducible deployments
* Easy rollbacks
* Clear traceability from code → container → pod

---

## 🎯 Why This Project Matters

This is not a toy project or tutorial demo.

It demonstrates:

* Ownership of CI/CD pipelines
* Kubernetes deployment best practices
* Production-grade DevOps thinking
* Debugging and observability awareness

---

## 🖼️ Application Output

<img width="1879" height="911" alt="Screenshot 2025-12-23 205722" src="https://github.com/user-attachments/assets/168c70b4-c012-4cc8-99e3-2dc39be4aecf" />

<img width="1879" height="952" alt="Screenshot 2025-12-23 205745" src="https://github.com/user-attachments/assets/fc3c6e87-4255-4f99-a20d-9b85016edfa7" />

<img width="1879" height="611" alt="Screenshot 2025-12-23 205801" src="https://github.com/user-attachments/assets/6cb4a2ad-dc7c-4f6a-b7fa-c75a063524a4" />

---

## 👤 Author

**Pawan Singh M**
GitHub: [https://github.com/Pawan-Builds](https://github.com/Pawan-Builds)

