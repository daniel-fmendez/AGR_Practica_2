#!/bin/bash

for c in $(sudo lxc-ls); do
    echo "Destruyendo contenedor $c..."
    sudo lxc-stop -n "$c"
    sudo lxc-destroy -n "$c" --force
done