%define ver 2.0.1
%define rev 449

Name: apparmor-utils
Summary: AppArmor userlevel utilities
Version: %ver
Release: %mkrel 1.%rev.1
License: GPL
Group: System/Base
Source0: apparmor-utils-%{ver}-%{rev}.tar.gz
URL: http://developer.novell.com/wiki/index.php/Novell_AppArmor
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildArch: noarch

%description
This package contains programs to help create and manage AppArmor
profiles.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} PERLDIR=%{buildroot}%{_libdir}/perl5/vendor_perl/Immunix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/apparmor
%config(noreplace) %{_sysconfdir}/apparmor/logprof.conf
# XXX db? config?
%config(noreplace) %{_sysconfdir}/apparmor/severity.db
%{_datadir}/locale/*/*/apparmor-utils.mo
%{_sbindir}/*
%{_libdir}/perl5/vendor_perl/Immunix
%{_var}/log/apparmor
