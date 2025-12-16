#!/bin/bash
minikube start

# 2. Copiar el plugin static al nodo
echo "Instalando plugin static CNI..."
minikube cp ./cni-plugins/static /home/docker/static
minikube ssh "sudo mv /home/docker/static /opt/cni/bin/static && sudo chmod +x /opt/cni/bin/static"

# 3. Limpiar restos de redes previas por si acaso
minikube ssh "sudo rm -rf /var/lib/cni/networks/*"

echo "Plugin static listo."