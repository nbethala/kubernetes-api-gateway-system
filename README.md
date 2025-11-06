
# Kubernetes API Gateway System

This project demonstrates a Kubernetes-native API Gateway architecture using Kong Gateway, NGINX Ingress, and FastAPI microservices. It’s designed for CKA prep in mind.

## 🧱 Architecture Overview

- **Kind** cluster with multi-node setup
- **NGINX Ingress Controller** for external traffic
- **Kong Gateway** for routing and plugins
- **Microservices**: User, Product, Order (FastAPI)
- **Service Discovery** via Kubernetes DNS
- Optional: Prometheus + Grafana for observability

## 📦 Services

| Service        | Description                    | Port |
|----------------|--------------------------------|------|
| User Service   | CRUD for user profiles         | 8001 |
| Product Service| CRUD for product catalog       | 8002 |
| Order Service  | Create and track orders        | 8003 |

## 🚀 Setup Instructions

1. Install Docker, Kind, kubectl, helm
2. Create cluster: `kind create cluster --config kind-config.yaml`
3. Install Ingress + Kong
4. Deploy services and routes
5. Test with `curl` or Postman

## 📘 Learning Goals

- Understand API Gateway patterns
- Practice Kubernetes YAML and CLI
- Simulate service-to-service communication
- Build a portfolio-ready architecture

## 📎 Resources

- [Kong Gateway Docs](https://docs.konghq.com/)
- [CKA Curriculum](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)

## Folder Structure
```
k8s-api-gateway-system/
├── gateway/                    # Kong Gateway config and routing
│   ├── kong-ingress.yaml
│   ├── httpbin-route.yaml
│   └── README.md
├── services/                   # Microservices (FastAPI-based)
│   ├── user-service/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── README.md
│   ├── product-service/
│   └── order-service/
├── k8s-manifests/             # All Kubernetes YAMLs
│   ├── kind-config.yaml
│   ├── ingress-nginx.yaml
│   ├── kong-install.yaml
│   ├── httpbin-deployment.yaml
│   └── README.md
├── ci-cd/                     # GitHub Actions workflows (optional)
│   └── deploy.yaml
├── observability/             # Prometheus/Grafana setup (optional)
│   ├── prometheus-config.yaml
│   └── grafana-dashboards/
├── README.md                  # Main project overview
└── architecture.png           # Diagram (optional, add later)
```


