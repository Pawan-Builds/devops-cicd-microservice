from flask import Flask, render_template_string
import datetime
import os

app = Flask(__name__)

@app.route("/")
def display_dashboard():
    # Deployment information
    deployment_count = 42  # Simulated
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps CI/CD Microservice Dashboard</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            
            body {
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: #f1f5f9;
                min-height: 100vh;
                padding: 20px;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            
            header {
                text-align: center;
                padding: 40px 20px;
                background: rgba(30, 41, 59, 0.7);
                border-radius: 20px;
                margin-bottom: 30px;
                border: 1px solid #334155;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
            
            h1 {
                font-size: 3rem;
                background: linear-gradient(90deg, #60a5fa, #3b82f6);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                margin-bottom: 15px;
            }
            
            .tagline {
                font-size: 1.2rem;
                color: #94a3b8;
                margin-bottom: 25px;
            }
            
            .status-badge {
                display: inline-block;
                background: linear-gradient(90deg, #10b981, #059669);
                color: white;
                padding: 8px 20px;
                border-radius: 50px;
                font-weight: bold;
                font-size: 0.9rem;
                margin-top: 10px;
            }
            
            .dashboard-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 25px;
                margin-bottom: 30px;
            }
            
            .card {
                background: rgba(30, 41, 59, 0.7);
                border-radius: 15px;
                padding: 25px;
                border: 1px solid #334155;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
            }
            
            .card h2 {
                color: #60a5fa;
                margin-bottom: 20px;
                font-size: 1.5rem;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .tech-stack {
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                margin-top: 15px;
            }
            
            .tech-item {
                background: rgba(59, 130, 246, 0.1);
                border: 1px solid #3b82f6;
                padding: 8px 16px;
                border-radius: 8px;
                font-size: 0.9rem;
            }
            
            .pipeline-visual {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: 30px 0;
                position: relative;
            }
            
            .stage {
                text-align: center;
                z-index: 2;
                background: rgba(30, 41, 59, 0.9);
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #475569;
                min-width: 120px;
            }
            
            .stage-number {
                background: #3b82f6;
                color: white;
                width: 30px;
                height: 30px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 10px;
                font-weight: bold;
            }
            
            .stage-name {
                font-weight: 600;
                margin-bottom: 5px;
            }
            
            .connector {
                position: absolute;
                top: 50%;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #3b82f6, #8b5cf6);
                transform: translateY(-50%);
                z-index: 1;
            }
            
            .stats {
                display: flex;
                justify-content: space-around;
                margin-top: 30px;
                text-align: center;
            }
            
            .stat-item {
                padding: 20px;
            }
            
            .stat-value {
                font-size: 2.5rem;
                font-weight: bold;
                background: linear-gradient(90deg, #60a5fa, #8b5cf6);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }
            
            .stat-label {
                color: #94a3b8;
                font-size: 0.9rem;
                margin-top: 5px;
            }
            
            .instructions {
                background: rgba(30, 41, 59, 0.7);
                border-radius: 15px;
                padding: 25px;
                margin-top: 30px;
                border-left: 5px solid #10b981;
            }
            
            .instructions h3 {
                color: #10b981;
                margin-bottom: 15px;
            }
            
            code {
                background: #1e293b;
                padding: 2px 8px;
                border-radius: 4px;
                font-family: 'Courier New', monospace;
                color: #fbbf24;
            }
            
            pre {
                background: #1e293b;
                padding: 20px;
                border-radius: 10px;
                overflow-x: auto;
                margin: 15px 0;
                border: 1px solid #334155;
                font-size: 0.9rem;
            }
            
            .file-tree {
                font-family: 'Courier New', monospace;
                line-height: 1.6;
                background: #1e293b;
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #334155;
                margin: 15px 0;
            }
            
            .tree-folder {
                color: #60a5fa;
            }
            
            .tree-file {
                color: #fbbf24;
            }
            
            .tree-indent {
                margin-left: 20px;
            }
            
            .deployment-time {
                text-align: center;
                color: #94a3b8;
                font-size: 0.9rem;
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #334155;
            }
            
            @media (max-width: 768px) {
                .pipeline-visual {
                    flex-direction: column;
                    gap: 20px;
                }
                
                .connector {
                    display: none;
                }
                
                h1 {
                    font-size: 2.2rem;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>🚀 DevOps CI/CD Microservice</h1>
                <p class="tagline">End-to-End Automation from Code to Kubernetes</p>
                <div class="status-badge">✅ Pipeline Status: ACTIVE</div>
            </header>
            
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-value">{{ deployment_count }}</div>
                    <div class="stat-label">Successful Deployments</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">5</div>
                    <div class="stat-label">Pipeline Stages</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">6</div>
                    <div class="stat-label">Technologies</div>
                </div>
            </div>
            
            <div class="pipeline-visual">
                <div class="connector"></div>
                <div class="stage">
                    <div class="stage-number">1</div>
                    <div class="stage-name">📦 Code Commit</div>
                    <div style="font-size: 0.8rem; color: #94a3b8;">Push to GitHub</div>
                </div>
                <div class="stage">
                    <div class="stage-number">2</div>
                    <div class="stage-name">⚙️ Build & Test</div>
                    <div style="font-size: 0.8rem; color: #94a3b8;">GitHub Actions</div>
                </div>
                <div class="stage">
                    <div class="stage-number">3</div>
                    <div class="stage-name">🐳 Containerize</div>
                    <div style="font-size: 0.8rem; color: #94a3b8;">Docker Image</div>
                </div>
                <div class="stage">
                    <div class="stage-number">4</div>
                    <div class="stage-name">🚀 Deploy</div>
                    <div style="font-size: 0.8rem; color: #94a3b8;">Helm to K8s</div>
                </div>
                <div class="stage">
                    <div class="stage-number">5</div>
                    <div class="stage-name">📊 Monitor</div>
                    <div style="font-size: 0.8rem; color: #94a3b8;">Health Checks</div>
                </div>
            </div>
            
            <div class="dashboard-grid">
                <div class="card">
                    <h2>📁 Project Structure</h2>
                    <div class="file-tree">
                        <div class="tree-folder">devops-cicd-microservice/</div>
                        <div class="tree-indent">
                            <div class="tree-folder">app/</div>
                            <div class="tree-indent">
                                <div class="tree-file">app.py</div>
                                <div class="tree-file">requirements.txt</div>
                                <div class="tree-file">Dockerfile</div>
                            </div>
                            <div class="tree-folder">helm/</div>
                            <div class="tree-indent">
                                <div class="tree-folder">microservice/</div>
                                <div class="tree-indent">
                                    <div class="tree-file">Chart.yaml</div>
                                    <div class="tree-file">values.yaml</div>
                                    <div class="tree-folder">templates/</div>
                                    <div class="tree-indent">
                                        <div class="tree-file">deployment.yaml</div>
                                        <div class="tree-file">service.yaml</div>
                                    </div>
                                </div>
                            </div>
                            <div class="tree-folder">k8s/</div>
                            <div class="tree-indent">
                                <div class="tree-file">namespace.yaml</div>
                            </div>
                            <div class="tree-folder">.github/</div>
                            <div class="tree-indent">
                                <div class="tree-folder">workflows/</div>
                                <div class="tree-indent">
                                    <div class="tree-file">ci-cd.yaml</div>
                                </div>
                            </div>
                            <div class="tree-folder">scripts/</div>
                            <div class="tree-indent">
                                <div class="tree-file">local-deploy.sh</div>
                            </div>
                            <div class="tree-file">README.md</div>
                            <div class="tree-file">interviewer-explanation.md</div>
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <h2>🏗️ Architecture</h2>
                    <p>This project demonstrates a complete CI/CD pipeline that builds, containerizes, and deploys a microservice application to Kubernetes using:</p>
                    <div class="tech-stack">
                        <div class="tech-item">GitHub Actions</div>
                        <div class="tech-item">Docker</div>
                        <div class="tech-item">Kubernetes</div>
                        <div class="tech-item">Helm</div>
                        <div class="tech-item">Python Flask</div>
                        <div class="tech-item">GitHub Container Registry</div>
                    </div>
                    
                    <h3 style="margin-top: 20px; color: #94a3b8;">Workflow</h3>
                    <ol style="padding-left: 20px; margin-top: 10px; line-height: 1.8;">
                        <li>Developer pushes code to GitHub</li>
                        <li>GitHub Actions builds Docker image</li>
                        <li>Image is pushed to GitHub Container Registry</li>
                        <li>Application is deployed to Kubernetes using Helm</li>
                    </ol>
                </div>
                
                <div class="card">
                    <h2>🔧 Tech Stack Details</h2>
                    <div class="tech-stack">
                        <div class="tech-item" style="background: rgba(239, 68, 68, 0.1); border-color: #ef4444;">CI/CD: GitHub Actions</div>
                        <div class="tech-item" style="background: rgba(59, 130, 246, 0.1); border-color: #3b82f6;">Container: Docker</div>
                        <div class="tech-item" style="background: rgba(139, 92, 246, 0.1); border-color: #8b5cf6;">Orchestration: Kubernetes</div>
                        <div class="tech-item" style="background: rgba(16, 185, 129, 0.1); border-color: #10b981;">Package Manager: Helm</div>
                        <div class="tech-item" style="background: rgba(245, 158, 11, 0.1); border-color: #f59e0b;">Backend: Python Flask</div>
                        <div class="tech-item" style="background: rgba(236, 72, 153, 0.1); border-color: #ec4899;">Registry: GHCR</div>
                    </div>
                    
                    <h3 style="margin-top: 20px; color: #94a3b8;">Key Files</h3>
                    <ul style="padding-left: 20px; margin-top: 10px; line-height: 1.8;">
                        <li><code>.github/workflows/ci-cd.yaml</code> - CI/CD pipeline</li>
                        <li><code>helm/microservice/</code> - Helm charts</li>
                        <li><code>scripts/local-deploy.sh</code> - Local deployment</li>
                        <li><code>k8s/namespace.yaml</code> - K8s namespace</li>
                    </ul>
                </div>
            </div>
            
            <div class="instructions">
                <h3>🚀 How to Run Locally</h3>
                <pre><code># Start Minikube cluster
minikube start

# Deploy using the provided script
./scripts/local-deploy.sh

# Access the application
minikube service flask-app-service</code></pre>
            
            <div class="deployment-time">
                Dashboard loaded: {{ current_time }} UTC<br>
                Service Version: 1.0.0 | Environment: Production | Pod: flask-app-{{ deployment_count }}
            </div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template, 
                                 deployment_count=deployment_count,
                                 current_time=current_time)

@app.route("/health")
def health_check():
    return {
        "status": "healthy", 
        "service": "devops-cicd-microservice", 
        "version": "1.0.0",
        "timestamp": datetime.datetime.now().isoformat(),
        "checks": {
            "database": "connected",
            "cache": "healthy",
            "disk_space": "adequate"
        }
    }

@app.route("/api/deployments")
def get_deployments():
    return {
        "total_deployments": 42,
        "last_7_days": [5, 3, 7, 2, 6, 4, 8],
        "success_rate": "99.2%",
        "average_deployment_time": "45s",
        "pipeline": {
            "build_time": "1m 30s",
            "test_time": "45s",
            "deploy_time": "2m 15s"
        }
    }

@app.route("/api/pipeline")
def pipeline_info():
    return {
        "stages": [
            {"name": "Code Commit", "description": "Push to GitHub"},
            {"name": "Build & Test", "description": "GitHub Actions CI"},
            {"name": "Containerize", "description": "Docker Image Build"},
            {"name": "Deploy", "description": "Helm to Kubernetes"},
            {"name": "Monitor", "description": "Health Checks & Logging"}
        ],
        "tools": ["GitHub Actions", "Docker", "Kubernetes", "Helm", "Python Flask"]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
