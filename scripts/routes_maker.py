import os
import topology
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.normpath(os.path.join(BASE_DIR, "..", "config", "scripts"))

for nodo, info in topology.config.items():
    file_name = "start_routes_"+nodo
    out_path = os.path.join(out_dir,file_name)
    with open(out_path, "w") as text_file:       
        for route in info["routing"]:
            rout_dest = route["dest"]
            rout_next = route["next"]

            command_line = f"ip route ${rout_dest} ${rout_next}\n"
            text_file.write(command_line)

       
            
