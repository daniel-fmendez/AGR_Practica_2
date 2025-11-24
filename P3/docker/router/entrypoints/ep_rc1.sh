#!/bin/bash

service syslog-ng start
service frr start

vtysh << EOF
conf t
log file /shared-volume/frr/frr1.log
router ospf

end
EOF



/bin/sleep infinity