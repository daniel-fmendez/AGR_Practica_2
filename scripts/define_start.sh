#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "$0")")

: 'for network in "$SCRIPT_DIR/../xml/networks/"*; do
    net_name=$(xmllint --xpath "string(//name)" "$network")
    echo " - Creando red: $net_name"
    virsh net-create "$network"
done

echo
echo "Redes activas actualmente:"
virsh net-list
'
# VM
for vm in "$SCRIPT_DIR/../xml/vms/"*; do
    vm_name=$(xmllint --xpath "string(//name)" "$vm")
    virsh create "$vm"
done

echo "Defined VM":
virsh list --all