if [ -d "/var/lib/lxc/rc1" ]; then
    lxc-destroy -n "rc1" --force
    rm -rf "/var/lib/lxc/rc1"
    rm -f "/var/lib/lxc/rc1.lock"
fi

if ! lxc-ls | grep -q "^rc1$"; then
    echo "Creando contenedor rc1..."
    lxc-create -n "rc1" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor rc1"
lxc-start -n "rc1"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar

lxc-attach -n rc1 -- sysctl -w net.ipv4.ip_forward=1


# Para crear las conexiones

cat >> /var/lib/lxc/rc1/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-servidor
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.100.0.1/24
EOF
cat >> /var/lib/lxc/rc1/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.1.type = veth
lxc.net.1.link = br-rc1-rc2
lxc.net.1.flags = up
lxc.net.1.ipv4.address = 10.1.0.1/30
EOF

lxc-stop -n rc1
lxc-start -n rc1 -d

sudo lxc-attach -n rc1 -- ip route add default via 10.1.0.2

