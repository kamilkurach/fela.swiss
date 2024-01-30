#!/bin/bash 

export RenLogFile=/home/root/skrypty/render.log

touch $RenLogFile
/opt/imx-gpu-sdk/GLES2/Bloom/GLES2.Bloom_Wayland >> $RenLogFile &
sleep 60
killall GLES2.Bloom_Wayland
exit 1