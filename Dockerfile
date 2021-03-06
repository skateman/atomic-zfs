FROM fedora:36
MAINTAINER "Dávid Halász"

VOLUME /var/atomic-zfs

RUN dnf install -y https://zfsonlinux.org/fedora/zfs-release$(rpm -E %dist).noarch.rpm flex bison && \
    dnf install -y $(dnf repoquery --requires --resolve zfs-dkms | grep -v kernel) && \
    dnf clean all

CMD dnf install -y kernel-modules-$(uname -r) kernel-devel-$(uname -r) && \
    dnf install -y zfs-dkms && \
    mkdir -p /var/atomic-zfs/lib && \
    cp -rf /lib/modules /var/atomic-zfs/lib/
