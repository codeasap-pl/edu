#!/bin/sh

FILE=${1:-A.disk}

echo "Using file: $FILE"

if mount | grep -qs /dev/mapper/my-vault; then
    echo "Already mounted"
else
    sudo cryptsetup luksOpen $FILE my-vault && \
	sudo mount /dev/mapper/my-vault /mnt/disk
    echo "Mounted $FILE at: /mnt/disk"
fi
