#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Este script requiere de permisos su"
    exit 1
fi

# mkdir -p xml/networks
mkdir -p xml/vms
mkdir -p xml/networks
mkdir -p img
mkdir -p config/interfaces

python3 ./scripts/network_maker.py
python3 ./scripts/interfaces_maker.py
python3 ./scripts/vm_maker.py
sh ./scripts/define_start.sh