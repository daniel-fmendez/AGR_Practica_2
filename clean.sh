#!/bin/bash
# Limpieza de máquinas virtuales y redes en virsh

echo "Eliminando redes (excepto default)..."
for n in $(virsh net-list --all --name | grep -v '^default$'); do
    echo " - Borrando red: $n"
    virsh net-destroy "$n" 2>/dev/null
    virsh net-undefine "$n" 2>/dev/null
done

echo "Eliminando máquinas virtuales (excepto default)..."
for vm in $(virsh list --all --name | grep -v '^default$'); do
    echo " - Borrando VM: $vm"
    virsh destroy "$vm" 2>/dev/null
    virsh undefine "$vm" --remove-all-storage 2>/dev/null
done


echo "=== Eliminando bridges huérfanos (los que no gestiona libvirt) ==="
for br in $(brctl show | awk 'NR>1 {print $1}' | grep -v '^virbr0$'); do
    echo " - Borrando bridge: $br"
    ip link set "$br" down 2>/dev/null
    brctl delbr "$br" 2>/dev/null
done


echo "Limpieza completada."
