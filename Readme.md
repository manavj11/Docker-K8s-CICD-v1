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
- kubectl

## Build Docker Image
```bash
docker build -t flask-k8s-demo .
