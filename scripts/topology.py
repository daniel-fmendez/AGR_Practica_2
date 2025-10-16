# Definición de interfaces
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
        "routing": [
            {
                "dest" : "0.0.0.0/0",
                "next" : "10.1.0.2"
            }
        ]
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
        "routing": [
            {
                "dest" : "10.0.1.0/24",
                "next" : "10.2.0.2"
            },
            {
                "dest" : "10.0.2.0/24",
                "next" : "10.2.0.2"
            },
            {
                "dest" : "10.0.3.0/24",
                "next" : "10.3.0.2"
            },
            {
                "dest" : "10.0.4.0/24",
                "next" : "10.3.0.2"
            },
            {
                "dest" : "0.0.0.0/0",
                "next" : "10.1.0.1"
            }
        ]
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
        "routing": [
            {
                "dest" : "0.0.0.0/0",
                "next" : "10.2.0.1"
            }
        ]
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
        "routing": [
            {
                "dest" : "0.0.0.0/0",
                "next" : "10.3.0.1"
            }
        ]
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
# Definicion de redes
redes = {
    "red-servidor": {
        "nombre": "red-servidor",
        "bridge": "br-servidor",
        "network": "10.100.0.0/24",
        "gateway": "10.100.0.1",
        "hosts": [
            {"nombre": "servidor", "ip": "10.100.0.10", "mac": "52:54:00:10:00:01"},
            {"nombre": "rc1-lan", "ip": "10.100.0.1", "mac": "52:54:00:10:00:02"}
        ]
    },
    "red-troncal-rc1-rc2": {
        "nombre": "red-troncal-rc1-rc2",
        "bridge": "br-rc1-rc2",
        "network": "10.1.0.0/30",
        "gateway": "10.1.0.1",
        "hosts": [
            {"nombre": "rc1-wan", "ip": "10.1.0.1", "mac": "52:54:00:11:00:01"},
            {"nombre": "rc2-wan", "ip": "10.1.0.2", "mac": "52:54:00:11:00:02"}
        ]
    },
    "red-troncal-rc2-ra": {
        "nombre": "red-troncal-rc2-ra",
        "bridge": "br-rc2-ra",
        "network": "10.2.0.0/30",
        "gateway": "10.2.0.1",
        "hosts": [
            {"nombre": "rc2-if-ra", "ip": "10.2.0.1", "mac": "52:54:00:12:00:01"},
            {"nombre": "ra-wan", "ip": "10.2.0.2", "mac": "52:54:00:12:00:02"}
        ]
    },
    "red-troncal-rc2-rb": {
        "nombre": "red-troncal-rc2-rb",
        "bridge": "br-rc2-rb",
        "network": "10.3.0.0/30",
        "gateway": "10.3.0.1",
        "hosts": [
            {"nombre": "rc2-if-rb", "ip": "10.3.0.1", "mac": "52:54:00:13:00:01"},
            {"nombre": "rb-wan", "ip": "10.3.0.2", "mac": "52:54:00:13:00:02"}
        ]
    },
    "red1": {
        "nombre": "red1",
        "bridge": "br-red1",
        "network": "10.0.1.0/24",
        "gateway": "10.0.1.1",
        "hosts": [
            {"nombre": "ra-if-red1", "ip": "10.0.1.1", "mac": "52:54:00:01:01:01"},
            {"nombre": "host1", "ip": "10.0.1.2", "mac": "52:54:00:01:01:02"}
        ]
    },
    "red2": {
        "nombre": "red2",
        "bridge": "br-red2",
        "network": "10.0.2.0/24",
        "gateway": "10.0.2.1",
        "hosts": [
            {"nombre": "ra-if-red2", "ip": "10.0.2.1", "mac": "52:54:00:02:02:01"},
            {"nombre": "host2", "ip": "10.0.2.2", "mac": "52:54:00:02:02:02"}
        ]
    },
    "red3": {
        "nombre": "red3",
        "bridge": "br-red3",
        "network": "10.0.3.0/24",
        "gateway": "10.0.3.1",
        "hosts": [
            {"nombre": "rb-if-red3", "ip": "10.0.3.1", "mac": "52:54:00:03:03:01"},
            {"nombre": "host3", "ip": "10.0.3.2", "mac": "52:54:00:03:03:02"}
        ]
    },
    "red4": {
        "nombre": "red4",
        "bridge": "br-red4",
        "network": "10.0.4.0/24",
        "gateway": "10.0.4.1",
        "hosts": [
            {"nombre": "rb-if-red4", "ip": "10.0.4.1", "mac": "52:54:00:04:04:01"},
            {"nombre": "host4", "ip": "10.0.4.2", "mac": "52:54:00:04:04:02"}
        ]
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