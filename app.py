from flask import Flask, render_template_string

app = Flask(__name__)

HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Skill Lab | Cloud & DevOps</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #1d2671, #c33764);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            max-width: 500px;
        }
        h1 {
            margin-bottom: 15px;
            font-size: 28px;
        }
        p {
            font-size: 18px;
            line-height: 1.6;
        }
        .badge {
            margin-top: 20px;
            display: inline-block;
            padding: 8px 16px;
            background: #00ffcc;
            color: #000;
            border-radius: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Welcome Students</h1>
        <p>
            Welcome to the <b>Skill Lab Cloud & DevOps Training Program</b><br>
            Learn Docker, AWS, Kubernetes & real-world DevOps skills.
        </p>
        <div class="badge">Server Running Successfully ✅</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_PAGE)

@app.route('/health')
def health():
    return {
        "status": "UP",
        "message": "Server is healthy and running"
    }
