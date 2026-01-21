# Flask Kubernetes Demo

A minimal Flask application containerized with Docker and deployed to Kubernetes.  
This project demonstrates a simple end-to-end workflow for building, deploying, and accessing a Python web service in a Kubernetes cluster.

---

## 🚀 Features

- Python Flask REST API
- Dockerized application
- Kubernetes deployment and service
- Health check endpoint
- Visitor counter example

---

## 📡 API Endpoints

| Endpoint   | Description                                   |
|-----------|-----------------------------------------------|
| `/`       | Returns a greeting and visitor count           |
| `/health` | Health check endpoint                          |

---

## 🧰 Requirements

- **Docker**
- **Kubernetes** (Docker Desktop Kubernetes is sufficient)
- **kubectl**

Ensure Docker and Kubernetes are installed and running before proceeding.

---

## 🏗️ Build the Docker Image
docker build -t flask-k8s-demo .

## ☸️ Deploy to Kubernetes
Apply the Kubernetes deployment and service manifests:\
kubectl apply -f k8s/deployment.yaml\
kubectl apply -f k8s/service.yaml

## 🔍 Verify Deployment
Check the status of the running pods and services:\
kubectl get svc\
kubectl get pods

## 🌐 Access the Application

Main Endpoint\
Open your browser and navigate to:\
http://localhost:30007\
You should see a greeting message along with a visitor count.

Health Check Endpoint\
Navigate to:\
http://localhost:30007/health\
You should receive a simple health response such as OK or healthy.

Happy testing!
