FROM fedora:33
MAINTAINER "Dávid Halász"

VOLUME /opt

RUN dnf install -y https://zfsonlinux.org/fedora/zfs-release$(rpm -E %dist).noarch.rpm flex bison && \
    dnf install -y $(dnf repoquery --requires --resolve zfs-dkms | grep -v kernel) && \
    dnf clean all

CMD dnf install -y kernel-modules kernel-devel && \
    dnf install -y zfs-dkms && \
    mkdir -p /opt/atomic-zfs/lib && \
    cp -rf /lib/modules /opt/atomic-zfs/lib/
