## 🧭 Notion Roadmap: k8s-api-gateway-system

### 🟢 Phase 0: Setup GitHub repo - Initialize with the needed files 

### 🟢 Phase 1: Foundation Setup
[x] Install Docker, Kind, kubectl, helm on macOS Big Sur

[x] Create Kind cluster with port mappings

[x] Install NGINX Ingress Controller

[x] Deploy Kong Gateway via Helm

[x] Validate routing with dummy service (httpbin)


### 🟡 Phase 2: Microservices Scaffolding
[ ] Scaffold user-service with FastAPI + Dockerfile

[ ] Scaffold product-service and order-service

[ ] Add /health, /ready, /info endpoints to each

[ ] Create Kubernetes Deployment + Service YAMLs

[ ] Validate pod status and service exposure

### 🟠 Phase 3: Gateway Routing
[ ] Define Kong Ingress routes for each service

[ ] Test routing with curl and Postman

[ ] Add Kong plugins (rate limiting, logging, optional JWT auth)

[ ] Document routing logic in gateway/README.md

### 🔵 Phase 4: Observability (Optional)
[ ] Install Prometheus + Grafana via Helm

[ ] Configure scrape targets for services

[ ] Create basic Grafana dashboards

[ ] Document metrics setup in observability/README.md

### 🟣 Phase 5: CI/CD Integration
[ ] Create GitHub Actions workflow for Docker builds

[ ] Push images to GitHub Container Registry (GHCR)

[ ] Deploy to Kind via kubectl in CI

[ ] Document CI/CD flow in ci-cd/README.md

### 🟤 Phase 6: Cloud Portability (Optional)
[ ] Replicate setup on AWS EC2 with K3s

[ ] Explore EKS deployment via eksctl

[ ] Compare local vs cloud networking

[ ] Document cloud setup tradeoffs

### 🧾 Phase 7: Portfolio Polish
[ ] Finalize README.md with architecture diagram

[ ] Add CLI examples and YAML snippets

[ ] Highlight CKA-aligned skills and service communication

[ ] Share repo on LinkedIn with project summary

### THE END - You did it!! 
