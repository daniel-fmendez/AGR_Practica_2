if [ -d "/var/lib/lxc/host1" ]; then
    lxc-destroy -n "host1" --force
    rm -rf "/var/lib/lxc/host1"
    rm -f "/var/lib/lxc/host1.lock"
fi

if ! lxc-ls | grep -q "^host1$"; then
    echo "Creando contenedor host1..."
    lxc-create -n "host1" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor host1"
lxc-start -n "host1"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar
lxc-attach -n host1 -- bash -c '
apt-get update
apt-get install -y curl
'


# Para crear las conexiones

cat >> /var/lib/lxc/host1/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-host1
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.0.1.2/24

lxc.net.0.ipv4.gateway = 10.0.1.1
EOF

lxc-stop -n host1
lxc-start -n host1 -d


