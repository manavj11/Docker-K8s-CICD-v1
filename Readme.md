# Flask Kubernetes Demo

A minimal Flask app deployed using Docker and Kubernetes.

## Features
- Python Flask API
- Dockerized application
- Deployed to Kubernetes
- Health check endpoint

## Endpoints
- `/` – returns a greeting and visitor count
- `/health` – health check

## Requirements
- Docker
- Kubernetes (Docker Desktop)
  - Install and run Docker as normal
- kubectl

## Build Docker Image
docker build -t flask-k8s-demo .

## Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

## Check service details:
kubectl get svc
kubectl get pods

## Access Application

- Open the main endpoint - Open your browser and go to: http://localhost:30007
  - If everything is working, you should see a greeting message and a visitor count.

- Open the health endpoint - In the same browser, go to: http://localhost:30007/health
  - You should see a simple health message (for example “OK” or “healthy”).

Happy testing!