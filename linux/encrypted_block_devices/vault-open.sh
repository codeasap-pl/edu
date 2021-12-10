#!/bin/sh

FILE=${1:-A.disk}
VAULT=${2:-my-vault}
MOUNTPOINT=${3:-/mnt/disk}

echo "Using file: $FILE"

if mount | grep -qs /dev/mapper/$VAULT; then
    echo "Already mounted"
else
    sudo cryptsetup luksOpen $FILE $VAULT && \
	sudo mount /dev/mapper/$VAULT $MOUNTPOINT
    echo "Mounted $FILE at: $MOUNTPOINT"
fi
