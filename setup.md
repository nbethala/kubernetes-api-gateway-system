## Follow the below instructions for detailed setup guidelines - 

### Phase 1: Foundation Setup
1.1 Install docker, kind, kubectl, helm locally 

Docker + CLI 	✅ Installed	Docker Desktop ≤ 4.3.x, Kind, kubectl, helm
Kind Cluster	✅ Created	Multi-node with port mappings for 80/443
NGINX Ingress	✅ Installed	Controller running in ingress-nginx namespace
Kong Gateway	✅ Deployed via Helm	Running in kong namespace
Dummy Service	✅ httpbin deployed	Routed via Kong using Ingress


1.2 Create a Kind cluster with port mappings (HTTP: 8080, HTTPS: 8443)
    - Create the cluster config file - Folder k8s-manifests/kind-config.yaml
    - Map -> Kong/Ingress HTTP → localhost:8080
    - Map -> Kong/Ingress HTTPS → localhost:8443
    - create cluster : 
    ```
    kind create cluster --name gateway-cluster --config k8s-manifests/kind-config.yaml
    ```
1.3 Install NGINX Ingress Controller 
```
https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.0/deploy/static/provider/kind/deploy.yaml

# check for controller pod to become ready
kubectl get pods -n ingress-nginx --watch

```
   - This YAML sets up the entry point for all HTTP/HTTPS traffic into your cluster.
   - The deploy.yaml file installs the NGINX Ingress Controller specifically configured for Kind clusters. 
   - It sets up the controller, RBAC permissions, services, and configmaps needed to route external HTTP/S traffic into your       Kubernetes cluster.
   - Key components : Namespace, ServiceAccount, ClusterRole, ClusterRoleBinding, ConfigMap, Deployment, Service (LoadBalancer), IngressClass.

1.4 Install Kong Gateway via Helm
```
helm repo add kong https://charts.konghq.com
helm repo update
kubectl create namespace kong
helm install kong kong/kong --namespace kong --set ingressController.installCRDs=false

# validate 
kubectl get all -n kong

# You should see:
#   Kong proxy pod running
#   Service exposing Kong on port 80/443 (mapped to localhost:9080/9443)
```

1.5 Deploy and Route httpbin via Kong Gateway
   Deploy the httpbin Service: 
    - This creates a simple HTTP service that echoes requests — perfect for testing.
   ```
   kubectl create deployment httpbin --image=kennethreitz/httpbin --port=80
   kubectl expose deployment httpbin --port=80 --target-port=80 --type=ClusterIP
    ```
   # create kong ingress resource - gateway/httpbin-route.yaml
   ```
   kubectl apply -f gateway/httpbin-route.yaml
   ```

   # Validate the route
   ```
   curl http://localhost:9080/httpbin/get
   ```

   ###  What You’ve Achieved : 
   - Bootstrapped a Kubernetes-native API Gateway system
   - Validated routing from Kong → Ingress → Service
   - Built a reusable foundation for microservices and observability