%define ver 2.0.2
%define rev 743

Name: apparmor-utils
Summary: AppArmor userlevel utilities
Version: %ver
Release: %mkrel 1.%rev.1
License: GPL
Group: System/Base
Source0: apparmor-utils-%{ver}-%{rev}.tar.gz
URL: http://forge.novell.com/modules/xfmod/project/?apparmor
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
%config(noreplace) %{_sysconfdir}/apparmor/severity.db
%{_datadir}/locale/*/*/apparmor-utils.mo
%{_sbindir}/*
%{_libdir}/perl5/vendor_perl/Immunix
%{_var}/log/apparmor
%{_mandir}/man5/logprof.conf.5*
%{_mandir}/man8/aa-autodep.8*
%{_mandir}/man8/aa-complain.8*
%{_mandir}/man8/aa-enforce.8*
%{_mandir}/man8/aa-genprof.8*
%{_mandir}/man8/aa-logprof.8*
%{_mandir}/man8/aa-status.8*
%{_mandir}/man8/aa-unconfined.8*
%{_mandir}/man8/apparmor_status.8*
%{_mandir}/man8/autodep.8*
%{_mandir}/man8/complain.8*
%{_mandir}/man8/enforce.8*
%{_mandir}/man8/genprof.8*
%{_mandir}/man8/logprof.8*
%{_mandir}/man8/unconfined.8*

