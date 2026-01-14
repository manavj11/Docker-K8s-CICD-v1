from flask import Flask, jsonify

app = Flask(__name__)
visitor_count = 0

@app.route("/")
def home():
    global visitor_count
    visitor_count += 1
    return jsonify({
        "message": "Hello from Kubernetes (Python)!",
        "visitors": visitor_count
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
