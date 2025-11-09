# API Gateway System Architetcure : gateway routing 

Diagram showing how everything connects inside your Kind cluster.

##  Nginx Ingress routing 

<Diagram>

This image illustrates:

🧭 Postman/curl sending requests to localhost:8082

🚦 NGINX Ingress receiving traffic via port 31080 (mapped to 8082)

🔁 Routing to the internal httpbin service via ClusterIP

🧱 Kong Gateway shown as a parallel ingress controller 

🧩 All components aligned inside the Kind cluster


## Kong Gateway Routing 

Kong Gateway fully exposed and routing traffic to your microservices inside the Kind cluster.

<Diagram >

This visual illustrates:

🧭 Postman/curl sending requests to localhost:8080 (mapped from Kong’s NodePort 30080)

🔷 Kong Gateway receiving traffic and routing to the three microservices 

 - user service

 - product service

 - order service

🔁 Each service connected to its pod via ClusterIP

🔹 NGINX Ingress shown as a parallel controller on localhost:8082 (mapped from 31080)

🧩 All components aligned inside the Kind cluster

## Dual Ingress Gateway 
This is a great project that uses dual ingress - Nginx and Kong . By building it this way you can learn ports, mapping, routes and your kubernetes cluster communication through the Kong gateway and to the Microservices .

NGINX Ingress : It is Lightweight, simple path-based routing, fast for testing your local connectivity to the pods .

Kong Gateway : Full-featured API gateway, with Advanced routing, plugins (rate limiting, logging, JWT) - Production grade setup. 