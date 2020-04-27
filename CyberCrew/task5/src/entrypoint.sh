#!/bin/sh

mount -o remount,rw,hidepid=2 /proc/
mount --bind /dev /code/dev/
mount --bind /proc /code/proc/
mount --bind /etc/resolv.conf /code/etc/resolv.conf

echo "[*] Mounted!"

echo "[*] Chrooting"
chroot /code/ flask run -h 0.0.0.0 -p 7171