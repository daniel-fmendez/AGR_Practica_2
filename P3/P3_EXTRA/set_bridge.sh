#!/bin/bash

if [ "$#" -eq 1 ]; then
    name="$1"

    if ! ip link show "$name" >/dev/null 2>&1; then
        ip link add name "$name" type bridge
    fi

    ip link set "$name" up
    
fi
