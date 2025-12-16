

echo "Borrando puentes"
sudo ip link delete br-ra-r1 --force
sudo ip link delete br-ra-r2 --force
sudo ip link delete br-rb-r3 --force
sudo ip link delete br-rb-r4 --force
sudo ip link delete br-rc1-rc2 --force
sudo ip link delete br-rc2-ra --force
sudo ip link delete br-rc2-rb --force
sudo ip link delete br-servidor-rc1 --force

echo "Borrando pots"
kubectl delete pod host1 host2 host3 host4 ra rb rc1 rc2 server --force

echo "Borrando redes"
kubectl delete network-attachment-definition bridge-ra-h1
kubectl delete network-attachment-definition bridge-ra-h2
kubectl delete network-attachment-definition bridge-rb-h3
kubectl delete network-attachment-definition bridge-rb-h4
kubectl delete network-attachment-definition bridge-rc1-rc2
kubectl delete network-attachment-definition bridge-rc2-ra
kubectl delete network-attachment-definition bridge-rc2-rb
kubectl delete network-attachment-definition bridge-serv-rc1

minikube ssh "sudo rm -rf ls /var/lib/cni/networks/*"