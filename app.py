from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kivo CI/CD Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .card {
                background: #1e293b;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 0 20px rgba(0,0,0,0.3);
                text-align: center;
                width: 500px;
            }

            .status {
                color: #22c55e;
                font-size: 24px;
                font-weight: bold;
            }

            h1 {
                margin-bottom: 20px;
            }

            .info {
                margin-top: 20px;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Kivo CI/CD Pipeline Demo</h1>

            <div class="status">
                Application Running Successfully
            </div>

            <div class="info">
                <p>Source Control: GitHub</p>
                <p>CI/CD Tool: Jenkins</p>
                <p>Container: Docker</p>
                <p>Registry: Artifact Registry</p>
                <p>Deployment: Cloud Run</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)