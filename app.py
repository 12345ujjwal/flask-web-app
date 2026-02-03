from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Students, Welcome to Skill Lab Cloud and DevOps Training Program'

@app.route('/health')
def health():
    return 'Server is up and running'
