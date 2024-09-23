# Kubernetes YAML for Rick and Morty API

This directory contains Kubernetes manifests (YAML files) for deploying the Rick and Morty Flask API to a Kubernetes cluster. The Docker image is publicly available and is fetched from my personal Docker Hub repository, making it accessible to everyone.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/tomernos/rick-and-morty-restful-api.git
```
###  2. Apply the Kubernetes YAML Files

#### **a. Apply the Deployment:**

```bash
kubectl apply -f deployment.yaml
```

#### **b. Apply the Service:**

```bash
kubectl apply -f service.yaml
```

#### **c. Apply the Ingress:**

```bash
kubectl apply -f ingress.yaml
```

### 3. Fetching Characters from the Rick and Morty API

After deploying all the Kubernetes manifests, you can access the Rick and Morty API to fetch character information. Follow these steps to interact with the API.

#### **a. Get the Minikube IP or NodePort IP:**

```bash
minikube ip
```

#### **b. Fetch All Characters:**

```bash
curl http://<minikube-ip>:<nodeport>/characters
```

