#!/bin/bash

for c in $(sudo lxc-ls); do
    echo "Destruyendo contenedor $c..."
    lxc-stop -n "$c"
    lxc-destroy -n "$c" --force
done
rm -rf "/var/lib/lxc/*"

mkdir -p scripts

echo "Creando los scripts de inicialización de LXC"
python3 ./lxc_maker.py

sleep 1

echo "Ejecutando las maquinas creadas"


for file in scripts/*.sh; do
    echo "Ejecutando $file"
    bash "$file"
done

echo "Finalizado el proceso de creación"