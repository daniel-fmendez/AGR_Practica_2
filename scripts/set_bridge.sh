#!/bin/bash

if [ "$#" -eq 1 ]
then 
    name="$1"
    ip link add name "$name" type bridge
    ip link set "$name" up
fi