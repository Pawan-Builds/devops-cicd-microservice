#!/bin/bash

set -e  # Exit on any error

echo "🚀 DevOps CI/CD Microservice - Local Deployment"
echo "=============================================="

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to display error and help
show_error() {
    echo "❌ $1 is not installed or not in PATH"
    echo ""
    echo "📝 Installation instructions for $1:"
    case "$1" in
        docker)
            echo "   Linux (Ubuntu/Debian): sudo apt-get update && sudo apt-get install -y docker.io"
            echo "   macOS: Download Docker Desktop from https://docs.docker.com/desktop/install/mac-install/"
            echo "   Windows: Download Docker Desktop from https://docs.docker.com/desktop/install/windows-install/"
            ;;
        minikube)
            echo "   Linux:"
            echo "     curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"
            echo "     sudo install minikube-linux-amd64 /usr/local/bin/minikube"
            echo "   macOS: brew install minikube"
            echo "   Windows: choco install minikube"
            ;;
        kubectl)
            echo "   Linux:"
            echo "     curl -LO 'https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl'"
            echo "     sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl"
            echo "   macOS: brew install kubectl"
            echo "   Windows: choco install kubernetes-cli"
            ;;
        helm)
            echo "   Linux/Mac:"
            echo "     curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash"
            echo "   macOS: brew install helm"
            echo "   Windows: choco install kubernetes-helm"
            ;;
    esac
    echo ""
    exit 1
}

# Check prerequisites
echo "🔍 Checking prerequisites..."
PREREQUISITES=("docker" "minikube" "kubectl" "helm")

for cmd in "${PREREQUISITES[@]}"; do
    if command_exists "$cmd"; then
        echo "✅ $cmd is installed"
    else
        show_error "$cmd"
    fi
done

# Check if Minikube is running
echo "🔍 Checking Minikube status..."
if ! minikube status | grep -q "Running"; then
    echo "⚙️  Minikube is not running. Starting Minikube..."
    minikube start
    
    # Wait for Minikube to be ready
    echo "⏳ Waiting for Minikube to be ready..."
    sleep 10
else
    echo "✅ Minikube is already running"
fi

# Set Docker to use Minikube's daemon
echo "🐳 Configuring Docker to use Minikube..."
eval $(minikube docker-env)

# Build Docker image
echo "🏗️  Building Docker image..."
docker build -t microservice:latest ./app/
echo "✅ Docker image built successfully"

# Apply Kubernetes namespace
echo "📦 Creating Kubernetes namespace..."
kubectl apply -f k8s/namespace.yaml
echo "✅ Namespace created"

# Deploy with Helm
echo "🚀 Deploying with Helm..."
helm upgrade --install microservice helm/microservice \
  --namespace devops-demo \
  --set image.repository=microservice \
  --set image.tag=latest \
  --set image.pullPolicy=Never \
  --wait
echo "✅ Helm deployment completed"

# Wait for pods to be ready
echo "⏳ Waiting for pods to be ready..."
kubectl wait --for=condition=ready pod -l app=microservice -n devops-demo --timeout=120s

# Display status
echo ""
echo "📊 Deployment Status:"
echo "===================="
kubectl get pods -n devops-demo
kubectl get svc -n devops-demo

echo ""
echo "🎉 Deployment successful!"
echo ""
echo "🔗 To access the application, run:"
echo "   minikube service microservice -n devops-demo"
echo ""
echo "📝 Useful commands:"
echo "   kubectl logs -l app=microservice -n devops-demo --follow"
echo "   kubectl describe pod -l app=microservice -n devops-demo"
echo "   kubectl get all -n devops-demo"
echo ""
echo "🗑️  To clean up:"
echo "   helm uninstall microservice -n devops-demo"
echo "   kubectl delete namespace devops-demo"
