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
    echo "$vm"
    virsh define "$vm"
done

for img in "$SCRIPT_DIR/../img/"*; do
    filename=$(basename "$img")

    img_name="${filename%.qcow2}"

    interface="$SCRIPT_DIR/../config/interfaces/interfaces_$img_name"
    cp "$interface" "$SCRIPT_DIR/../config/interfaces/interfaces"
    tmp_if="$SCRIPT_DIR/../config/interfaces/interfaces"

    virt-copy-in -a $img $tmp_if /etc/network/

    routes="$SCRIPT_DIR/../config/scripts/start_routes_$img_name"
    cp "$routes" "$SCRIPT_DIR/../config/scripts/start_routes.sh"
    tmp_routes="$SCRIPT_DIR/../config/scripts/start_routes.sh"

    virt-copy-in -a $img $tmp_routes /home/ubuntu/boot_config
done

for vm in "$SCRIPT_DIR/../xml/vms/"*; do
    vm_name=$(xmllint --xpath "string(//name)" "$vm")
    echo "$vm"
    virsh start "$vm_name"
done

echo "Defined VM":
virsh list --all