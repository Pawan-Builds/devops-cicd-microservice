from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps CI/CD Pipeline</title>
        <style>
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                text-align: center;
                padding: 3rem;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                max-width: 800px;
                margin: 2rem;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                background: linear-gradient(90deg, #00d2ff, #3a7bd5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .subtitle {
                font-size: 1.2rem;
                opacity: 0.9;
                margin-bottom: 2rem;
            }
            .pipeline {
                display: flex;
                justify-content: space-between;
                margin: 3rem 0;
                position: relative;
            }
            .pipeline:before {
                content: '';
                position: absolute;
                top: 50%;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #00d2ff, #3a7bd5);
                transform: translateY(-50%);
                z-index: 1;
            }
            .stage {
                background: rgba(0, 0, 0, 0.3);
                padding: 1rem 1.5rem;
                border-radius: 10px;
                z-index: 2;
                position: relative;
                min-width: 120px;
                border: 2px solid rgba(0, 210, 255, 0.3);
            }
            .stage-icon {
                font-size: 2rem;
                margin-bottom: 0.5rem;
            }
            .status {
                margin-top: 2rem;
                padding: 1rem;
                background: rgba(46, 204, 113, 0.2);
                border-radius: 10px;
                display: inline-block;
                border: 2px solid #2ecc71;
            }
            .version {
                position: absolute;
                top: 1rem;
                right: 1rem;
                background: rgba(255, 255, 255, 0.1);
                padding: 0.5rem 1rem;
                border-radius: 20px;
                font-size: 0.9rem;
            }
            .deploy-count {
                margin-top: 2rem;
                font-size: 1.5rem;
                color: #00d2ff;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="version">v1.0.0</div>
            <h1>🚀 DevOps CI/CD Pipeline</h1>
            <div class="subtitle">Automated Deployment System | Built with Flask & Docker</div>
            
            <div class="pipeline">
                <div class="stage">
                    <div class="stage-icon">📦</div>
                    <div>Code Commit</div>
                </div>
                <div class="stage">
                    <div class="stage-icon">⚙️</div>
                    <div>Build</div>
                </div>
                <div class="stage">
                    <div class="stage-icon">🧪</div>
                    <div>Test</div>
                </div>
                <div class="stage">
                    <div class="stage-icon">🐳</div>
                    <div>Deploy</div>
                </div>
                <div class="stage">
                    <div class="stage-icon">📊</div>
                    <div>Monitor</div>
                </div>
            </div>
            
            <div class="status">
                ✅ System Status: <strong>OPERATIONAL</strong>
            </div>
            
            <div class="deploy-count">
                Latest Deployment: Successful
            </div>
            
            <div style="margin-top: 3rem; font-size: 0.9rem; opacity: 0.7;">
                <p>✨ Automated pipeline running | Real-time monitoring enabled</p>
                <p>🛠️ Tools: Flask • Docker • Jenkins/GitHub Actions • Kubernetes</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
