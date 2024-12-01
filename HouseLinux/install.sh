#!/bin/bash

ARCH=amd64 # i386 or amd64

OS=debian
DISTRO=stable

TARGET=/data/data/com.termux/files/home/windows13-ssn/HouseLinux

## в качестве источника можно использовать примонтированный cdrom с системой:
#debootstrap --include=sudo,nano,wget --arch $ARCH $DISTRO $TARGET file:/media/cdrom

## а можно и зеркало в интернете
debootstrap --include=sudo,nano,wget --arch $ARCH $DISTRO $TARGET http://$OS.mirror.vu.lt/$OS/

## строчки ниже трогать не нужно, они монтируют системные директории в новый /
#mount -o bind /dev $TARGET/dev
#mount -o bind /sys $TARGET/sys
