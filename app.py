from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>DevOps Pipeline Successful!</h1><p>My Flask app is running in Docker on EC2.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
