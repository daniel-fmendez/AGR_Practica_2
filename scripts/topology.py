# Definición de redes
config = {
    "servidor": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-servidor",
            "address": "10.100.0.10",
            "netmask": "255.255.255.0",
            "gateway": "10.100.0.1"
            }
        ],
        "routing": []
    },
    "rc1": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-rc1-rc2",
            "address": "10.100.0.1",
            "netmask": "255.255.255.252",
            "gateway": "10.100.0.2"
            },
            {
            "if": "eth1",
            "bridge": "br-rc1-rc2",
            "address": "10.1.0.1",
            "netmask": "255.255.255.252",
            "gateway": "10.1.0.2"
            }
        ],
        "routing": []
    },
    "rc2": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-rc1-rc2",
            "address": "10.1.0.2",
            "netmask": "255.255.255.252",
            "gateway": "10.1.0.1"
            }, 
            {
            "if": "eth1",
            "bridge": "br-rc1-rc2",
            "address": "10.2.0.1",
            "netmask": "255.255.255.252",
            "gateway": "10.1.0.1"
            },
            {
            "if": "eth2",
            "bridge": "br-rc1-rc2",
            "address": "10.3.0.1",
            "netmask": "255.255.255.252",
            "gateway": "10.1.0.1"
            }
        ],
        "routing": []
    },
    "ra": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-rc1-rc2",
            "address": "10.2.0.2",
            "netmask": "255.255.255.252",
            "gateway": "10.2.0.1"
            }, 
            {
            "if": "eth1",
            "bridge": "br-rc1-rc2",
            "address": "10.0.1.1",
            "netmask": "255.255.255.0",
            "gateway": "10.2.0.1"
            },
            {
            "if": "eth2",
            "bridge": "br-rc1-rc2",
            "address": "10.0.2.1",
            "netmask": "255.255.255.0",
            "gateway": "10.2.0.1"
            }
        ],
        "routing": []
    },
    "rb": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-rc1-rc2",
            "address": "10.3.0.2",
            "netmask": "255.255.255.252",
            "gateway": "10.3.0.1"
            }, 
            {
            "if": "eth1",
            "bridge": "br-rc1-rc2",
            "address": "10.0.3.1",
            "netmask": "255.255.255.0",
            "gateway": "10.3.0.1"
            },
            {
            "if": "eth2",
            "bridge": "br-rc1-rc2",
            "address": "10.0.4.1",
            "netmask": "255.255.255.0",
            "gateway": "10.3.0.1"
            }
        ],
        "routing": []
    },
    "host1": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-rc1-rc2",
            "address": "10.0.1.2",
            "netmask": "255.255.255.0",
            "gateway": "10.0.1.1"
            }
        ],
        "routing": []
    },
    "host2": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-rc1-rc2",
            "address": "10.0.2.2",
            "netmask": "255.255.255.0",
            "gateway": "10.0.2.1"
            }
        ],
        "routing": []
    },
    "host3": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-rc1-rc2",
            "address": "10.0.3.2",
            "netmask": "255.255.255.0",
            "gateway": "10.0.3.1"
            }
        ],
        "routing": []
    },
    "host4": {
        "ifs" : [
            {
            "if": "eth0",
            "bridge": "br-rc1-rc2",
            "address": "10.0.4.2",
            "netmask": "255.255.255.0",
            "gateway": "10.0.4.1"
            }
        ],
        "routing": []
    }
}

# Definición de máquinas virtuales
maquinas = {
    "servidor": {
        "nombre": "servidor",
        "interfaces": [
            {"mac": "52:54:00:10:00:01", "bridge": "br-servidor"}
        ]
    },
    "rc1": {
        "nombre": "rc1",
        "interfaces": [
            {"mac": "52:54:00:10:00:02", "bridge": "br-servidor"},
            {"mac": "52:54:00:11:00:01", "bridge": "br-rc1-rc2"}
        ]
    },
    "rc2": {
        "nombre": "rc2",
        "interfaces": [
            {"mac": "52:54:00:11:00:02", "bridge": "br-rc1-rc2"},
            {"mac": "52:54:00:12:00:01", "bridge": "br-rc2-ra"},
            {"mac": "52:54:00:13:00:01", "bridge": "br-rc2-rb"}
        ]
    },
    "ra": {
        "nombre": "ra",
        "interfaces": [
            {"mac": "52:54:00:12:00:02", "bridge": "br-rc2-ra"},
            {"mac": "52:54:00:01:01:01", "bridge": "br-red1"},
            {"mac": "52:54:00:02:02:01", "bridge": "br-red2"}
        ]
    },
    "rb": {
        "nombre": "rb",
        "interfaces": [
            {"mac": "52:54:00:13:00:02", "bridge": "br-rc2-rb"},
            {"mac": "52:54:00:03:03:01", "bridge": "br-red3"},
            {"mac": "52:54:00:04:04:01", "bridge": "br-red4"}
        ]
    },
    "host1": {
        "nombre": "host1",
        "interfaces": [
            {"mac": "52:54:00:01:01:02", "bridge": "br-red1"}
        ]
    },
    "host2": {
        "nombre": "host2",
        "interfaces": [
            {"mac": "52:54:00:02:02:02", "bridge": "br-red2"}
        ]
    },
    "host3": {
        "nombre": "host3",
        "interfaces": [
            {"mac": "52:54:00:03:03:02", "bridge": "br-red3"}
        ]
    },
    "host4": {
        "nombre": "host4",
        "interfaces": [
            {"mac": "52:54:00:04:04:02", "bridge": "br-red4"}
        ]
    }
}