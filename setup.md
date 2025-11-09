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
1.3 Install NGINX Ingress Controller - two methods
```
# Installation via static manifest yaml 
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.0/deploy/static/provider/kind/deploy.yaml

# Installation via helm - which will be consistent with kong and does port mapping 
helm install nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx --create-namespace \
  --set controller.service.type=NodePort \
  --set controller.service.nodePorts.http=31080 \
  --set controller.service.nodePorts.https=31443 \
  --set controller.resources.requests.cpu=100m \
  --set controller.resources.requests.memory=128Mi \
  --set controller.affinity=null \
  --set controller.nodeSelector=null

```
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
   kubectl apply -f gateway/httpbin-deployment.yaml
   kubectl apply -f gateway/httpbin-service.yaml
   kubectl apply -f gateway/httpbin-route.yaml
   
   ```

   # Validate the route
   ```
   curl http://localhost:8082/httpbin/get
   curl -i http://localhost:8082/httpbin/status/200
   ```


   # Validate the route via POSTMAN -Test httpbin via NGINX Ingress
   ```
    Target URL: http://localhost:8082/httpbin/status/200 
    This hits NGINX → rewrites path → routes to httpbin → returns 200 OK.
   ```
      
###  What You've Achieved : 
   - Bootstrapped a Kubernetes-native API Gateway system
   - Validated routing from Kong → Ingress → Service
   - Built a reusable foundation for microservices and observability


### Phase 2: Microservices Scaffolding
2.1  setup services with FastAPI + Dockerfile
      - services/user-service/app.py
      - services/order-service/app.py
      - services/product-service/app.py
      - services/user-service/Dockerfile
      - services/order-service/Dockerfile
      - services/product-service/Dockerfile

2.2 Create Kubernetes Deployment + Service YAMLs (both will be in the same yaml file for ease of tracking and service)
     - k8s-manifests/user-service.yaml
     - k8s-manifests/order-service.yaml
     - k8s-manifests/product-service.yaml

2.3 Apply and Validate yaml files 
```
kubectl apply -f k8s-manifests/user-service.yaml
kubectl apply -f k8s-manifests/product-service.yaml
kubectl apply -f k8s-manifests/order-service.yaml

kubectl get pods
kubectl get svc
```

###  You should see all three services running and exposed internally.
NOTE : You will see ImagePullBackOff and ErrImagePull errors because Kubernetes is unable to fetch the container image for your microservices.

Reason - Kubernetes expects this image to exist in a registry or be preloaded into the Kind cluster. But by default, Kind can't pull from your local Docker daemon. Since this project is been built locally - lets load images locally into the kind cluster.

✅ Fix: Load Local Images into Kind
```
# build image locally 
docker build -t user-service:latest services/user-service/
docker build -t product-service:latest services/product-service/
docker build -t order-service:latest services/order-service/

# Load each image into kind
kind load docker-image user-service:latest
kind load docker-image product-service:latest
kind load docker-image order-service:latest

# restart the deployments (optional)
kubectl rollout restart deployment user-service
kubectl rollout restart deployment product-service
kubectl rollout restart deployment order-service
```

### Phase 3: Gateway Routing
3.1 Define Kong Ingress Routes for Microservices

 # setup yaml files 
  gateway/user-kong-route.yaml
  gateway/product-kong-route.yaml
  gateway/order-kong-route.yaml
```
kubectl apply -f gateway/user-kong-route.yaml
kubectl apply -f gateway/product-kong-route.yaml
kubectl apply -f gateway/order-kong-route.yaml
```

3.2 Test routing with curl and Postman 
#validate that Kong is correctly forwarding external requests to internal services.
