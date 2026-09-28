from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Task is running successfully!"

@app.route("/status")
def status():
    return jsonify({
        "application": "DevOps Task",
        "status": "running",
        "platform": "AWS ECS Fargate"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
