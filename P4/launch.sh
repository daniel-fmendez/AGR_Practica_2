#!/bin/bash

echo "Lanzando redes...."
for file in networks/*.yaml; do
    kubectl apply -f $file --validate=false
done

echo "Creando pods...."
for file in pods/*.yaml; do
    kubectl apply -f $file --validate=false
done