if [ -d "/var/lib/lxc/rc2" ]; then
    lxc-destroy -n "rc2" --force
    rm -rf "/var/lib/lxc/rc2"
    rm -f "/var/lib/lxc/rc2.lock"
fi

if ! lxc-ls | grep -q "^rc2$"; then
    echo "Creando contenedor rc2..."
    lxc-create -n "rc2" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor rc2"
lxc-start -n "rc2"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar

lxc-attach -n rc2 -- sysctl -w net.ipv4.ip_forward=1


# Para crear las conexiones

cat >> /var/lib/lxc/rc2/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-rc1-rc2
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.1.0.2/30
EOF
cat >> /var/lib/lxc/rc2/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.1.type = veth
lxc.net.1.link = br-rc2-ra
lxc.net.1.flags = up
lxc.net.1.ipv4.address = 10.2.0.1/30
EOF
cat >> /var/lib/lxc/rc2/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.2.type = veth
lxc.net.2.link = br-rc2-rb
lxc.net.2.flags = up
lxc.net.2.ipv4.address = 10.3.0.1/30
EOF

lxc-stop -n rc2
lxc-start -n rc2 -d

sudo lxc-attach -n rc2 -- ip route add 10.0.1.0/24 via 10.2.0.2
sudo lxc-attach -n rc2 -- ip route add 10.0.2.0/24 via 10.2.0.2
sudo lxc-attach -n rc2 -- ip route add 10.0.3.0/24 via 10.3.0.2
sudo lxc-attach -n rc2 -- ip route add 10.0.4.0/24 via 10.3.0.2
sudo lxc-attach -n rc2 -- ip route add default via 10.1.0.1

