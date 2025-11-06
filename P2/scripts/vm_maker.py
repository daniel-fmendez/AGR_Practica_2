import xml.etree.ElementTree as ET
import uuid
import os
import topology
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Img and template
source_img_path = os.path.normpath(os.path.join(BASE_DIR, "..", "img"))
xml_template_path = os.path.normpath(os.path.join(BASE_DIR, "..", "originals", "plantilla-vm.xml"))
xml_dir = os.path.normpath(os.path.join(BASE_DIR, "..", "xml", "vms"))
script_path = os.path.join(os.path.dirname(__file__), "img_creator.sh")
subprocess.run(["chmod", "+x", script_path])
for nodo, info in topology.maquinas.items():
    subprocess.run([script_path, nodo])
    source_name = str(f"{nodo}.qcow2")
    source_img = os.path.join(source_img_path,source_name)

    xml_template = ET.parse(xml_template_path)
    root = xml_template.getroot()

    name = info["nombre"]

    hostname_element = root.find('name')
    if hostname_element is not None:
        hostname_element.text = name

    uuid_element = root.find('uuid')
    if uuid_element is not None:
        uuid_element.text = str(uuid.uuid4())
    else:
        uuid_element = ET.Element('uuid')
        uuid_element.text = str(uuid.uuid4())

        parent = root
        name_index = list(parent).index(hostname_element)
        parent.insert(name_index + 1, uuid_element)
    
    for disk in root.findall(".//devices/disk"):
        source = disk.find("source")
        if source is not None:
            source.set("file", source_img)

    devices = root.find(".//devices")
    for interface in info["interfaces"]:
        mac = interface["mac"]
        bridge = interface["bridge"]

        interface_element = ET.Element("interface", type="bridge")
        ET.SubElement(interface_element, "mac", address=mac)
        ET.SubElement(interface_element, "source", bridge=bridge)
        ET.SubElement(interface_element, "model", type="virtio")
        devices.append(interface_element)

    ET.indent(xml_template, space="  ")
    filename = str(f"{nodo}_vm.xml")
    out_path = os.path.join(xml_dir,filename)

    xml_template.write(out_path, encoding="utf-8", xml_declaration=True)