#!/usr/bin/env bash


while :; do
  chroot /alpine \
    /usr/bin/chromium \
      --no-sandbox \
      --kiosk \
      --start-fullscreen \
      --suppress-message-center-popups \
      --block-new-web-contents \
      --ozone-platform=wayland \
      "$1" \
      && break # Break from "endless" reopen loop if ? = 0
done
