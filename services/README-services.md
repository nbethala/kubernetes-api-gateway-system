# Kubernetes API Gateway System - Services 

## Microservices : 
Here we are creating three microservices as part of this project. The architecture is cloud-native, 
multi-services designed for scalability, service orchestration and routing via Kong Gateway.

## Service description 
A FASTAPI-based microservice exposes three endpoints: 
 - /health - liveness check 
 - /ready - readiness probe for kubernetes 
 - /info - service metadata (name, version)

Each service is containerized with a lightweight Dockerfile and deployed to kubernetes via Deployment and Service YAMLs.

## Architecture Role
 - user-service: Handles user-related data and identity logic
 - product-service: Manages product catalog and metadata
 - order-service: Coordinates order placement and status

 ## Communication 
 These services communicate internally via Kubernetes DNS and are externally accessible through Kong Gateway routes.

 ## Key Files
  - app.py – FastAPI app with health,ready and info endpoints
  - Dockerfile – container definition
  - k8s-manifests/<service>.yaml – Kubernetes deployment and service 
  - gateway/<service>-route.yaml – Kong Ingress route