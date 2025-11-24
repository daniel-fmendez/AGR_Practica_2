if [ -d "/var/lib/lxc/host3" ]; then
    lxc-destroy -n "host3" --force
    rm -rf "/var/lib/lxc/host3"
    rm -f "/var/lib/lxc/host3.lock"
fi

if ! lxc-ls | grep -q "^host3$"; then
    echo "Creando contenedor host3..."
    lxc-create -n "host3" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor host3"
lxc-start -n "host3"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar
lxc-attach -n host3 -- bash -c '
apt-get update
apt-get install -y curl
'


# Para crear las conexiones

cat >> /var/lib/lxc/host3/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-host3
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.0.3.2/24

lxc.net.0.ipv4.gateway = 10.0.3.1
EOF

lxc-stop -n host3
lxc-start -n host3 -d


