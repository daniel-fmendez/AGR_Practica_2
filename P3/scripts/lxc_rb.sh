if [ -d "/var/lib/lxc/rb" ]; then
    lxc-destroy -n "rb" --force
    rm -rf "/var/lib/lxc/rb"
    rm -f "/var/lib/lxc/rb.lock"
fi

if ! lxc-ls | grep -q "^rb$"; then
    echo "Creando contenedor rb..."
    lxc-create -n "rb" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor rb"
lxc-start -n "rb"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar

lxc-attach -n rb -- sysctl -w net.ipv4.ip_forward=1


# Para crear las conexiones

cat >> /var/lib/lxc/rb/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-rc2-rb
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.3.0.2/30
EOF
cat >> /var/lib/lxc/rb/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.1.type = veth
lxc.net.1.link = br-host3
lxc.net.1.flags = up
lxc.net.1.ipv4.address = 10.0.3.1/24
EOF
cat >> /var/lib/lxc/rb/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.2.type = veth
lxc.net.2.link = br-host4
lxc.net.2.flags = up
lxc.net.2.ipv4.address = 10.0.4.1/24
EOF

lxc-stop -n rb
lxc-start -n rb -d

sudo lxc-attach -n rb -- ip route add default via 10.3.0.1

