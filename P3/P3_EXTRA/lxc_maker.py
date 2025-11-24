import os
import info
from netaddr import IPAddress
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.normpath(os.path.join(BASE_DIR, "scripts"))

template_path = os.path.join(os.path.dirname(__file__), "lxc_template.txt")
script_path = os.path.join(os.path.dirname(__file__), "set_bridge.sh")


network_text = """
cat >> /var/lib/lxc/{name}/config <<EOF
# --- Configuración de red estática añadida por script ---
lxc.net.{n}.type = veth
lxc.net.{n}.link = {bridge}
lxc.net.{n}.flags = up
lxc.net.{n}.ipv4.address = {address}/{mask}
"""

gateway_text = """
lxc.net.{n}.ipv4.gateway = {gateway}
"""

router_text = """
lxc-attach -n {name} -- sysctl -w net.ipv4.ip_forward=1
"""

routing_text = "sudo lxc-attach -n {name} -- ip route add {dest} via {exitIf}"

host_extra = """lxc-attach -n {name} -- bash -c '
apt-get update
apt-get install -y curl
'
"""

with open(template_path, encoding="utf-8") as f:
    template = f.read()

server_data = info.server_data
for nodo, info in info.config.items():
    #Extra        
    extra = ""
    if nodo == "servidor":
        extra = server_data
    if nodo in ["ra", "rb", "rc1", "rc2"]:
        extra = router_text.format(name = nodo)
    if nodo in ["host1", "host2", "host3", "host4"]:
        extra = host_extra.format(name = nodo)

    network = ""

    routing = ""
    for count, interface in  enumerate(info["ifs"]):
        if_if = interface["if"]
        if_address = interface["address"]
        if_netmask = interface["netmask"]
        if_gateway = interface["gateway"]
        if_bridge = interface["bridge"]

        mask = IPAddress(if_netmask).netmask_bits()

        #Network
        subprocess.run([script_path, if_bridge])
        network += network_text.format(name = nodo,n = count, bridge = if_bridge, address = if_address, mask = mask)
        if any(name in nodo for name in ["host","servidor"]):
            network+=gateway_text.format(n = count, gateway = if_gateway)

        network += "EOF"
        network += ""

    for route in info["routing"]:
        dest = route["dest"]
        next = route["next"]
        routing += routing_text.format(name = nodo, dest = dest, exitIf = next)
        routing += "\n"


    file_name = f"lxc_{nodo}.sh"
    out_path = os.path.join(out_dir,file_name)

    content = template.format(name = nodo, extra = extra, network = network, routing = routing)
    with open(out_path, "w") as f:
        f.write(content)           