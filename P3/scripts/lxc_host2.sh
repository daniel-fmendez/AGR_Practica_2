if [ -d "/var/lib/lxc/host2" ]; then
    lxc-destroy -n "host2" --force
    rm -rf "/var/lib/lxc/host2"
    rm -f "/var/lib/lxc/host2.lock"
fi

if ! lxc-ls | grep -q "^host2$"; then
    echo "Creando contenedor host2..."
    lxc-create -n "host2" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor host2"
lxc-start -n "host2"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar
lxc-attach -n host2 -- bash -c '
apt-get update
apt-get install -y curl
'


# Para crear las conexiones

cat >> /var/lib/lxc/host2/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-host2
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.0.2.2/24

lxc.net.0.ipv4.gateway = 10.0.2.1
EOF

lxc-stop -n host2
lxc-start -n host2 -d


