if [ -d "/var/lib/lxc/servidor" ]; then
    lxc-destroy -n "servidor" --force
    rm -rf "/var/lib/lxc/servidor"
    rm -f "/var/lib/lxc/servidor.lock"
fi

if ! lxc-ls | grep -q "^servidor$"; then
    echo "Creando contenedor servidor..."
    lxc-create -n "servidor" -t download -- --dist ubuntu --release jammy --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor servidor"
lxc-start -n "servidor"

# Espera a que arranque
sleep 5

# Extras a ejecutar antes de inicar
lxc-attach -n servidor -- bash -c '
apt-get update
apt-get install -y git curl

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
export NVM_DIR="$HOME/.nvm"
source $NVM_DIR/nvm.sh

nvm install 22
git clone https://github.com/Hsabaterl/agr.git
cd agr
npm install express

nohup node /root/agr/app.js >/root/app.log 2>&1 &
'


# Para crear las conexiones

cat >> /var/lib/lxc/servidor/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.0.type = veth
lxc.net.0.link = br-servidor
lxc.net.0.flags = up
lxc.net.0.ipv4.address = 10.100.0.10/24

lxc.net.0.ipv4.gateway = 10.100.0.1
EOF

lxc-stop -n servidor
lxc-start -n servidor -d


