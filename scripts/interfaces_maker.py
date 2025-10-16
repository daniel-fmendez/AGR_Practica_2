import os
import topology

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.normpath(os.path.join(BASE_DIR, "..", "config", "interfaces"))

loopback = """
auto lo
iface lo inet static

"""

for nodo, info in topology.config.items():
    result_string = loopback
    for interface in info["ifs"]:
        if_if = interface["if"]
        if_address = interface["address"]
        if_netmask = interface["netmask"]
        if_gateway = interface["gateway"]

        interface_string = f"""
auto {if_if}
iface {if_if} inet static
    address {if_address}
    netmask {if_netmask}
    gateway {if_gateway}

"""
        result_string += interface_string

    file_name = f"interfaces_{nodo}"
    out_path = os.path.join(out_dir,file_name)
    with open(out_path, "w") as text_file:
        text_file.write(result_string)

            