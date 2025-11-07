## use the troubleshooting guide if you run into issues - if you can't troubleshoot at all call Jesus !

### Docker : The beast dosen't start
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

Solution : Open Docker Desktop from your Applications folder to re-start the daemon - You should see both Client and Server sections.

### ingress-nginx-controller pod failed to schedule 
error: The nodeSelector constraint in the deployment that was too strict for the Kind node.
```
0/1 nodes are available: 1 node(s) didn't match Pod's node affinity/selector.
```

solution : Patch the deployment to remove node Selector 
```
kubectl patch deployment ingress-nginx-controller -n ingress-nginx --type=json \
  -p='[{"op": "remove", "path": "/spec/template/spec/nodeSelector"}]'

 # Restart the pod 
 kubectl delete pod -n ingress-nginx --all
 
```

### Why curl localhost:9080 Fails - Kong Proxy not reachable 
Kong’s proxy service is of type LoadBalancer. Kind doesn’t support LoadBalancer natively.

Solution : Patch Kong Proxy to NodePort (Modular + Cloud-Ready)

```
kubectl patch svc kong-kong-proxy -n kong \
  -p '{"spec": {"type": "NodePort"}}'
```
Later on AWS cloud you can easily switch to - type: LoadBalancer

### If Nodeport dosent work use below option : 
Use kubectl port-forward to Expose Kong Proxy
This bypasses NodePort and directly maps Kong’s internal port to your local machine:

```
kubectl port-forward -n kong service/kong-kong-proxy 9080:80
```

This maps Kong’s internal port 80 → your local port 9080

🔍 Test the Route
Now run:

```
curl http://localhost:9080/httpbin/get
```
You should get a JSON response from the httpbin pod.


