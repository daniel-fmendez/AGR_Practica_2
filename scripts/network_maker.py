import xml.etree.ElementTree as ET
import os
import topology
import ipaddress
import subprocess


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
xml_dir = os.path.normpath(os.path.join(BASE_DIR, "..", "xml", "networks"))

script_path = os.path.join(os.path.dirname(__file__), "set_bridge.sh")

def generateXML(name, bridge, address, mask, macs, names, ips):
    file_name = str(f"{name}_net.xml")
    output_path = os.path.join(xml_dir, file_name)

    root = ET.Element("network")

    name_element = ET.SubElement(root, "name")
    name_element.text = name

    bridge_element = ET.SubElement(root, "bridge", attrib={"name": bridge})

    ip_element = ET.SubElement(root, "ip", attrib={"address": address, "netmask": mask})

    dhcp = ET.SubElement(ip_element, "dhcp")
    for name, mac, ip in zip(names, macs, ips):
        host = ET.SubElement(dhcp, "host", attrib={"mac": mac, "name":name, "ip":ip})

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    xml_str = ET.tostring(root, encoding="unicode")
    
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    subprocess.run([script_path, bridge])

subprocess.run(["chmod", "+x", script_path])
for nodo, info in topology.redes.items():
    print(f"Nodo: {nodo}")
    name = info["nombre"]
    bridge = info["bridge"]
    network = ipaddress.ip_network(info["network"])
    ip = str(network.network_address)
    mask = str(network.netmask)

    macs = []
    names = []
    ips = []
    for host in info["hosts"]:
        mac = host["mac"]
        name = host["nombre"]
        ip = host["ip"]

        macs.append(mac)
        names.append(name)
        ips.append(ip)

    generateXML(name, bridge, ip, mask, macs, names, ips)




