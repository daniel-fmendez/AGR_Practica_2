#!/bin/bash

service syslog-ng start
service frr start

vtysh << EOF
conf t
log file /shared-volume/frr/frr1.log
router ospf
network 10.2.0.0/30 area 0
network 10.0.1.0/24 area 0
network 10.0.2.0/24 area 0
end
EOF



/bin/sleep infinity