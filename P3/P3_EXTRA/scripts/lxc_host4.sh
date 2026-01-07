if [ -d "/var/lib/lxc/host4" ]; then
    lxc-destroy -n "host4" --force
    rm -rf "/var/lib/lxc/host4"
    rm -f "/var/lib/lxc/host4.lock"
fi

if ! lxc-ls | grep -q "^host4$"; then
    echo "Creando contenedor host4..."
    lxc-create -n "host4" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor host4"
lxc-start -n "host4"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar
lxc-attach -n host4 -- bash -c '
apt-get update
apt-get install -y curl
'


# Para crear las conexiones

cat >> /var/lib/lxc/host4/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-host4
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.0.4.2/24

lxc.net.0.ipv4.gateway = 10.0.4.1
EOF

lxc-stop -n host4
lxc-start -n host4 -d


