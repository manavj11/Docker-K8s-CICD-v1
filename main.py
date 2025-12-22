import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

# Use environment variables for configuration
# 'redis-service' is the name we will give our Redis service in Kubernetes
redis_host = os.getenv("REDIS_HOST", "localhost")
redis = Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    try:
        count = redis.incr('hits')
        return f"<h1>Hello!</h1><p>This page has been viewed <b>{count}</b> times.</p>"
    except Exception as e:
        return f"<h1>Error</h1><p>Could not connect to Redis: {str(e)}</p>"

if __name__ == "__main__":
    # In production, we'd use a real server like Gunicorn, 
    # but for a POC, the Flask dev server is fine.
    app.run(host="0.0.0.0", port=8080)