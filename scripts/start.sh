#!/bin/bash

#export LC_ALL=pl_PL.UTF-8
#export LANG=pl_PL.UTF-8
#export DISPLAY=:0
#export QT_QPA_PLATFORM=wayland-egl
#timedatectl set-timezone Europe/Warsaw
#echo 1 > /proc/sys/net/ipv4/ip_forward
#if ! pgrep udhcpc; then
#	udhcpc -b -i eth0 > /dev/null 2>&1 &
#fi
#ip addr del 192.168.10.90/24 dev eth0 label eth0:1
#ip addr add 192.168.10.90/24 dev eth0 label eth0:1
#ip route replace 192.168.10.0/24 via 192.168.10.90 dev eth0:1
#iptables -A FORWARD -i eth0:1 -o eth0 -j ACCEPT
#iptables -A FORWARD -i eth0 -o eth0:1 -m state --state ESTABLISHED,RELATED -j ACCEPT
#iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -o eth0 -j MASQUERADE

cd /home/root/skrypty
./cmd_balaton 05 01
./cmd_balaton 03 255

sleep 3
echo "MERA-SYSTEMY"
echo "Demo TVM"
 

cd /home/root/fela.swiss
python3 main.py
