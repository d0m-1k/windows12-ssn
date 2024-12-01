build-os:
	clear
	xorriso -as mkisofs -r -J -b isolinux/isolinux.bin -c isolinux/boot.cat -boot-load-size 4 -boot-info-table -o win13.iso ./HouseLinux
