#!/bin/bash

set -x

#sleep 5

export DISPLAY=:0
export WAYLAND_DISPLAY=/run/wayland-0
#export QT_QPA_PLATFORM=wayland-egl

mount --types proc /proc /alpine/proc 2>/dev/null
mount --rbind /sys /alpine/sys 2>/dev/null
mount --make-rslave /alpine/sys 2>/dev/null
mount --rbind /dev /alpine/dev 2>/dev/null
mount --make-rslave /alpine/dev 2>/dev/null
mount --bind /run /alpine/run 2>/dev/null
mount --make-slave /alpine/run 2>/dev/null
mount --bind /home/root /alpine/home/root 2>/dev/null

/home/root/skrypty/start.sh

