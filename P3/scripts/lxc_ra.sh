if [ -d "/var/lib/lxc/ra" ]; then
    lxc-destroy -n "ra" --force
    rm -rf "/var/lib/lxc/ra"
    rm -f "/var/lib/lxc/ra.lock"
fi

if ! lxc-ls | grep -q "^ra$"; then
    echo "Creando contenedor ra..."
    lxc-create -n "ra" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor ra"
lxc-start -n "ra"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar

lxc-attach -n ra -- sysctl -w net.ipv4.ip_forward=1


# Para crear las conexiones

cat >> /var/lib/lxc/ra/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-rc2-ra
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.2.0.2/30
EOF
cat >> /var/lib/lxc/ra/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.1.type = veth
lxc.net.1.link = br-host1
lxc.net.1.flags = up
lxc.net.1.ipv4.address = 10.0.1.1/24
EOF
cat >> /var/lib/lxc/ra/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.2.type = veth
lxc.net.2.link = br-host2
lxc.net.2.flags = up
lxc.net.2.ipv4.address = 10.0.2.1/24
EOF

lxc-stop -n ra
lxc-start -n ra -d

sudo lxc-attach -n ra -- ip route add default via 10.2.0.1

