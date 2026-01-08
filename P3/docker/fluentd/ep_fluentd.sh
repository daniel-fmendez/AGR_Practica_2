#!/bin/bash

ip route change default via 10.100.0.50

/usr/local/bundle/gems/fluentd-1.17.0/bin/fluentd -c /fluentd/etc/fluent.conf & 

/bin/sleep infinity