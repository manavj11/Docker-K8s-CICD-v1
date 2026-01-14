# Kubernetes + Docker Visitor Counter

A minimal Python web app that counts visitors, exposes a health check, and is designed to run in Docker and Kubernetes.

This project is beginner-friendly and perfect for learning Docker & Kubernetes using GitHub Codespaces.

---

## 🚀 What You’ll Learn

- Build a small Python web service
- Containerize it with Docker
- Deploy to Kubernetes with Deployment & Service
- Use `/health` checks
- Use GitHub Codespaces for development

---

## 📦 Project Structure

k8s-python-visitor-counter/
├── app/
│ ├── main.py
│ └── requirements.txt
├── Dockerfile
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
└── README.md

## 🐍 Python Application

### `app/requirements.txt`

🚀 Running in GitHub Codespaces
Open this repo in GitHub Codespaces (VS Code in the cloud)
Build the Docker image:
docker build -t python-visitor-counter .
Apply Kubernetes resources:
kubectl apply -f k8s/
Forward the service port:
kubectl port-forward svc/python-visitor-counter-svc 8080:80
Visit:
http://localhost:8080/ ⇒ visitor count
http://localhost:8080/health ⇒ health
💡 Notes
Each pod has its own counter — demonstrates stateless scaling
Health checks help Kubernetes restart bad pods

