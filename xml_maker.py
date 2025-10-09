import xml.etree.ElementTree as ET
import uuid
import os

# Img and template
source_file = "/home/daniel/Documents/AGR/originals/plantilla-vm.xml"
xml_template_path = "/home/daniel/Documents/AGR/originals/plantilla-vm.xml"
xml_template = ET.parse(xml_template_path)

root = xml_template.getroot()

xml_string = ET.tostring(root, encoding='utf-8').decode('utf-8')
print(xml_string)
