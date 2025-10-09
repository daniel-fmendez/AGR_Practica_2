#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "$0")")
# Networks
for n in $(virsh net-list --all --name | grep -v default); do
    virsh net-destroy "$n" 2>/dev/null
    virsh net-undefine "$n" 2>/dev/null
done

for network in "$SCRIPT_DIR/../xml/networks/"*; do
    net_name=$(xmllint --xpath "string(//name)" "$network")
    
    # Crear y arrancar la red de forma NO persistente
    if ! virsh net-info "$net_name" &>/dev/null; then
        virsh net-create "$network"
    fi
done

echo "Defined networks"
virsh net-list --all

# VM
for vm in "$SCRIPT_DIR/../xml/vms/"*; do
    vm_name=$(xmllint --xpath "string(//name)" "$vm")
    virsh create "$vm"
done

echo "Defined VM":
virsh list --all