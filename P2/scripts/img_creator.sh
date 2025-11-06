#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "$0")")

original_img="$SCRIPT_DIR/../originals/agr-vm-base.qcow2"
new_img="$SCRIPT_DIR/../img/$1.qcow2"

qemu-img create -f qcow2 -b "$original_img" -F qcow2 "$new_img"