#!/bin/bash

name="servidor-lxc"
address="10.0.3.100"

if [ -d "/var/lib/lxc/$name" ]; then
    lxc-destroy -n "$name" --force
    rm -rf "/var/lib/lxc/$name"
    rm -f "/var/lib/lxc/$name.lock"
fi

if ! lxc-ls | grep -q "^$name$"; then
    echo "Creando contenedor $name..."
    lxc-create -n "$name" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor..."
lxc-start -n "$name"

# Espera a que arranque
sleep 10

# Ejecutar comandos dentro del contenedor
lxc-attach -n "$name" -- bash -c '
apt-get update
apt-get install -y git curl
su - root -c "
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
export NVM_DIR=\"\$HOME/.nvm\"
source \$NVM_DIR/nvm.sh
nvm install 22
git clone https://github.com/Hsabaterl/agr.git
cd agr
npm install express

sleep 5
nohup node /root/agr/app.js >/root/app.log 2>&1 || sleep infinity &
"

'
cat >> /var/lib/lxc/servidor-lxc/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = lxcbr0
lxc.net.0.flags = up
lxc.net.0.ipv4.address = $address/24
lxc.net.0.ipv4.gateway = 10.0.3.1
# --- Fin configuración de red ---
EOF

iptables -t nat -A PREROUTING -p tcp --dport 3000 -j DNAT --to-destination $address:3000
iptables -t nat -A POSTROUTING -s $address -j MASQUERADE

lxc-stop -n $name
lxc-start -n $name -d

lxc-info -n servidor-lxc
