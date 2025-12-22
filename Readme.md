# Visitor Counter POC

A minimal DevOps project demonstrating a Python/Redis stack running on Kubernetes.

## 🚀 Local Development
1. **Install requirements:** `pip install -r requirements.txt`
2. **Run App:** `python main.py` (Note: requires local Redis or it will error gracefully)

## 🐳 Docker Instructions
1. **Build:** `docker build -t your-username/visitor-app .`
2. **Push:** `docker push your-username/visitor-app`

## ☸️ Kubernetes Deployment
1. **Apply manifests:** `kubectl apply -f k8s-all-in-one.yaml`
2. **Port-forward to view:** `kubectl port-forward svc/web-service 8080:80`
3. **Open:** [http://localhost:8080](http://localhost:8080)