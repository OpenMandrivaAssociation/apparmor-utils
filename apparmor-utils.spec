%define ver 2.3.1
%define rev 1357

Name: apparmor-utils
Summary: AppArmor userlevel utilities
Version: %ver
Release: %mkrel 1.%rev.4
License: GPL
Group: System/Base
Source0: apparmor-utils-%{ver}-%{rev}.tar.gz
URL: http://forge.novell.com/modules/xfmod/project/?apparmor
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
%{makeinstall_std} PERLDIR=%{buildroot}%{perl_vendorlib}/Immunix

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/apparmor
%config(noreplace) %{_sysconfdir}/apparmor/logprof.conf
%config(noreplace) %{_sysconfdir}/apparmor/severity.db
%{_datadir}/locale/*/*/apparmor-utils.mo
%{_sbindir}/*
%{perl_vendorlib}/Immunix
%{_var}/log/apparmor
%{_mandir}/man5/logprof.conf.5*
%{_mandir}/man8/aa-audit.8*
%{_mandir}/man8/aa-autodep.8*
%{_mandir}/man8/aa-complain.8*
%{_mandir}/man8/aa-enforce.8*
%{_mandir}/man8/aa-genprof.8*
%{_mandir}/man8/aa-logprof.8*
%{_mandir}/man8/aa-status.8*
%{_mandir}/man8/aa-unconfined.8*
%{_mandir}/man8/apparmor_status.8*
%{_mandir}/man8/autodep.8*
%{_mandir}/man8/audit.8*
%{_mandir}/man8/complain.8*
%{_mandir}/man8/enforce.8*
%{_mandir}/man8/genprof.8*
%{_mandir}/man8/logprof.8*
%{_mandir}/man8/unconfined.8*


%changelog
* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.1-1.1357.4mdv2010.1
+ Revision: 521354
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3.1-1.1357.3mdv2010.0
+ Revision: 413035
- rebuild

* Sat Jan 03 2009 Eugeni Dodonov <eugeni@mandriva.com> 2.3.1-1.1357.2mdv2009.1
+ Revision: 323498
- Updated to 2.3.1-1357 (as shipped by SuSE 11.1).

* Wed Dec 03 2008 Michael Scherer <misc@mandriva.org> 2.3-1.1269.2mdv2009.1
+ Revision: 309843
- add Patch 0, fix bug 45936, by removing useless and buggy perl code ( since a undefined variable
  value is 0 if we use it for most operations )

* Wed Aug 06 2008 Luiz Fernando Capitulino <lcapitulino@mandriva.com> 2.3-1.1269.1mdv2009.0
+ Revision: 264683
- updated to version 2.3 svnrev 1269
- dropped apparmor-utils-2.1.2-1089-pt_BR.patch as messages have changed
  and the patch does not seen needed anymore

* Wed Mar 05 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1089.4mdv2008.1
+ Revision: 180005
- fix perl module installation path

* Mon Mar 03 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1089.3mdv2008.1
+ Revision: 178069
- one more important pt_BR i18n fix

* Mon Mar 03 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1089.2mdv2008.1
+ Revision: 178033
- fix duplicate shortcut key in translations (#38290)

* Wed Feb 27 2008 Andreas Hasenack <andreas@mandriva.com> 2.1.2-1.1089.1mdv2008.1
+ Revision: 175848
- updated apparmor-utils to 2.1.2-1089

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 15 2007 Andreas Hasenack <andreas@mandriva.com> 2.0.2-1.743.1mdv2008.0
+ Revision: 40166
- updated to version 2.0.2-743

* Wed Jun 13 2007 Andreas Hasenack <andreas@mandriva.com> 2.0.1-1.449.1mdv2008.0
+ Revision: 38732
- updated URL
- Import apparmor-utils

