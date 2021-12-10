#!/bin/sh

VAULT=${1:-my-vault}

if mount | grep -qs /dev/mapper/my-vault; then
	sudo umount /dev/mapper/my-vault
	sudo cryptsetup luksClose my-vault
	echo "Closed my-vault."
else
    echo "Not mounted"
fi
	
