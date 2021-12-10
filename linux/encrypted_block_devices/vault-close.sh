#!/bin/sh

VAULT=${1:-my-vault}

if mount | grep -qs /dev/mapper/$VAULT; then
	sudo umount /dev/mapper/$VAULT
	sudo cryptsetup luksClose $VAULT
	echo "Closed $VAULT."
else
    echo "Not mounted"
fi
