%define debug_package %{nil}

Name:           atomic-zfs
Version:        0.0.1
Release:        1%{?dist}
Summary:        atomic-zfs, builds the ZFS kernel module for Fedora Atomic/Silverblue
ExclusiveArch:  x86_64

Group:          System Environment/Kernel
License:        MIT
URL:            https://github.com/skateman/atomic-zfs
Source0:        atomic-zfs
Source1:        atomic-zfs.service
Source2:        LICENSE

BuildRequires: systemd-rpm-macros

Requires(pre):  shadow-utils
Requires:       systemd podman

%description
This package is responsible for building and loading the ZFS kernel module in an rpm-ostree
based Fedora installation using a regular rpm-based Fedora container.

%prep

%build

%install

install -D %{SOURCE0} %{buildroot}%{_bindir}/atomic-zfs
install -D %{SOURCE1} %{buildroot}%{_unitdir}/atomic-zfs.service
install -D %{SOURCE2} %{buildroot}%{_docdir}/atomic-zfs/LICENSE
install --directory %{buildroot}%{_localstatedir}/atomic-zfs

%post
%systemd_post atomic-zfs.service
semanage fcontext -a -t container_file_t %{_localstatedir}/atomic-zfs
restorecon -R %{_localstatedir}/atomic-zfs

%preun
%systemd_preun atomic-zfs.service

%postun
%systemd_postun_with_restart %{name}.service

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/atomic-zfs
%attr(644, root, root) %{_unitdir}/atomic-zfs.service
%dir %{_localstatedir}/atomic-zfs

%doc %{_docdir}/%{name}/LICENSE

%changelog
* Sun Apr 18 2021 Dávid Halász <rpm@skateman.eu> - 0.0.1
- initial version: v0.0.1
