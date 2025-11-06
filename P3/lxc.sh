#!/bin/bash

name="servidor-lxc"


if [ -d "/var/lib/lxc/$name" ]; then
    lxc-destroy -n "$name" --force
    rm -rf "/var/lib/lxc/$name"
    rm -f "/var/lib/lxc/$name.lock"
fi

if ! lxc-ls | grep -q "^$name$"; then
    echo "Creando contenedor $name..."
    lxc-create -n "$name" -t download -- --dist debian --release bookworm --arch amd64
fi

# Iniciar contenedor
echo "Iniciando contenedor..."
lxc-start -n "$name" -d

# Espera a que arranque
sleep 10


if ! lxc-info -n "$name" | grep -q "RUNNING"; then
    echo "El contenedor no se está ejecutando. Revisa los logs con:"
    echo "cat /var/log/lxc/$name.log"
    exit 1
fi

# Ejecutar comandos dentro del contenedor
lxc-attach -n "$name" -- bash -c '
apt-get update -y
apt-get install -y git curl
su - root -c "
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
export NVM_DIR=\"\$HOME/.nvm\"
source \$NVM_DIR/nvm.sh
nvm install 22
git clone https://github.com/Hsabaterl/agr.git
cd agr
npm install express
nohup node ./app.js >/root/app.log 2>&1 || sleep infinity &
"
'
