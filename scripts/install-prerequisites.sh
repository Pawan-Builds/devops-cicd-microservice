#!/bin/bash

set -e

echo "🔧 Installing DevOps CI/CD Microservice Prerequisites"
echo "====================================================="

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
else
    echo "❌ Unsupported OS: $OSTYPE"
    exit 1
fi

echo "📦 Checking and installing prerequisites..."

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install Docker
if ! command_exists docker; then
    echo "🐳 Installing Docker..."
    if [ "$OS" = "linux" ]; then
        # For Ubuntu/Debian
        sudo apt-get update
        sudo apt-get install -y docker.io
        sudo systemctl start docker
        sudo systemctl enable docker
        sudo usermod -aG docker $USER
        echo "✅ Docker installed. Please log out and log back in for group changes to take effect."
    elif [ "$OS" = "macos" ]; then
        echo "📱 Please install Docker Desktop from: https://docs.docker.com/desktop/install/mac-install/"
        echo "Then run this script again."
        exit 1
    fi
else
    echo "✅ Docker is already installed"
fi

# Install Minikube
if ! command_exists minikube; then
    echo "⚙️  Installing Minikube..."
    if [ "$OS" = "linux" ]; then
        curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
        sudo install minikube-linux-amd64 /usr/local/bin/minikube
        rm minikube-linux-amd64
    elif [ "$OS" = "macos" ]; then
        brew install minikube
    fi
    echo "✅ Minikube installed"
else
    echo "✅ Minikube is already installed"
fi

# Install kubectl
if ! command_exists kubectl; then
    echo "📦 Installing kubectl..."
    if [ "$OS" = "linux" ]; then
        curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
        sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
        rm kubectl
    elif [ "$OS" = "macos" ]; then
        brew install kubectl
    fi
    echo "✅ kubectl installed"
else
    echo "✅ kubectl is already installed"
fi

# Install Helm
if ! command_exists helm; then
    echo "📊 Installing Helm..."
    if [ "$OS" = "linux" ]; then
        curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
    elif [ "$OS" = "macos" ]; then
        brew install helm
    fi
    echo "✅ Helm installed"
else
    echo "✅ Helm is already installed"
fi

echo ""
echo "🎉 All prerequisites installed successfully!"
echo ""
echo "Next steps:"
echo "1. Log out and log back in (if Docker was just installed)"
echo "2. Run: ./scripts/local-deploy.sh"
echo ""

# Verify installations
echo "🔍 Verifying installations..."
docker --version
minikube version
kubectl version --client
helm version
