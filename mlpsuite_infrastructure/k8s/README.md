## Kubernetes
- `minikube start --mount-string="C:\projects\mlpsuite\mlpsuite_infrastructure:/mnt/root" --mount`
- `helm upgrade --install my-release spark-operator/spark-operator --namespace spark-operator --set webhook.enable=true --set serviceAccounts.spark.name=spark --create-namespace`

https://github.com/GoogleCloudPlatform/spark-on-k8s-operator

