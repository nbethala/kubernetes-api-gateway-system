
# Kubernetes API Gateway Architecture 

This project demonstrates a Kubernetes-native API Gateway architecture using Kong Gateway, NGINX Ingress for quick local testing, and FastAPI microservices. 

## 🧱 Architecture Overview

<img width="778" height="479" alt="API-architecture drawio (1)" src="https://github.com/user-attachments/assets/196de481-4d61-4212-8d26-3a0a2bf47299" />


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

## 📎 Resources

- [Kong Gateway Docs](https://docs.konghq.com/)

## Folder Structure
```
k8s-api-gateway-system/
├── gateway/                    # Kong Gateway config and routing
│   ├── kong-ingress.yaml
│   ├── httpbin-route.yaml
│   ├── httpbin-deployment.yaml
│   ├── httpbin-service.yaml
│   └── README.md
├── services/                   # Microservices (FastAPI-based)
│   │   └── README.md
│   ├── user-service/
│   │   ├── app.py
│   │   ├── Dockerfile
│   ├── product-service/
│   │   ├── app.py
│   │   ├── Dockerfile
│   └── order-service/
│   │   ├── app.py
│   │   ├── Dockerfile
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


