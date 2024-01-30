#!/bin/bash
ifconfig eth0 | grep "inet" | cut -d: -f2 | awk '{print $2}'