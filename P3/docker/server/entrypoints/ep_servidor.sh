#!/bin/bash

ip route change default via 10.100.0.50             

cd app
npm start

/bin/sleep infinity