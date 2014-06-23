# $Id: smeserver-ajaxterm.spec,v 1.5 2013/06/27 16:03:48 unnilennium Exp $
# Authority: mweinber
# Name: Michael Weinberger

Summary: ajaxterm is a web-based terminal
%define realname smeserver-ajaxterm
%define version 1.0.5
%define release 6
Name: %{realname}
Version: %{version}
Release: %{release}%{?dist}
BuildArch: noarch
License: GPL
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.gz
Source1: Ajaxterm-0.10.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://antony.lesuisse.org/qweb/trac/wiki/AjaxTerm
Requires: smeserver-release > 7.1.3
BuildRequires: e-smith-devtools
BuildRequires: python2-devel python-setuptools

%changelog
* Thu Jun 27 2013 JP Pialasse <tests@pialasse.com> 1.0.5-6
- fix Allowoverride [SME: 7711]
- patch3

* Wed Jun 26 2013 JP Pialasse <tests@pialasse.com> 1.0.5-5
- fix lib64 issue to auth [SME: 7309 ]
- patch2

* Wed Feb 06 2013 JP Pialasse <tests@pialasse.com> 1.0.5-4
- fix user ajaxterm [SME: 6442]
- creating default database 

* Tue Feb 05 2013 JP Pialasse <tests@pialasse.com> 1.0.5-3
- import into SME8 tree [SME: 7309]
- fix brp-python in spec file

* Sat Mar 01 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.5-2
- Moved documentation from spec file
- Changed description (copied from http://antony.lesuisse.org/qweb/trac/wiki/AjaxTerm)
- Fixed whitelines in changelog between entries

* Fri Feb 29 2008 Michael Weinberger <mweinber@neddix.de> 1.0.5-1
  Fix spec file

* Thu Nov 15 2007 Michael Weinberger <mweinber@neddix.de>
  Version 1.0.5
  Bug fix: SysV start: do not fall back do user root if user ajaxterm does not exist
  added config properties 'width' and 'height'
  
* Thu Nov 15 2007 Michael Weinberger <mweinber@neddix.de>
  Version 1.0.4
  added config property basicAuthUsers

* Wed Nov 14 2007 Michael Weinberger <mweinber@neddix.de>
  Version 1.0.3
  added config properties allowOnlyLocalhost and servicePort
  login with 'su' when localhost, otherwise with ssh
  Promtps for SSHPort at ssh login

%description
Ajaxterm is a web based terminal. It was totally inspired and works almost exactly like http://anyterm.org/ except it's much easier to install (see comparaison with anyterm below).

%pre
if ! /usr/bin/id ajaxterm &>/dev/null; then
        /usr/sbin/useradd -c 'Ajaxterm User' -s /sbin/nologin -r -d /opt/ajaxterm ajaxterm &>/dev/null || \
                %logmsg "Unexpected error adding user \"ajaxterm\". Abort installation."
fi

%prep
%setup -n %{realname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
tar xzvf $RPM_SOURCE_DIR/Ajaxterm-0.10.tar.gz
mv Ajaxterm-0.10/* root/opt/ajaxterm
rm -rf Ajaxterm-0.10
ls root/opt/ajaxterm
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist  $RPM_BUILD_ROOT \
  --dir /opt/ajaxterm 'attr(0750,ajaxterm,www)' \
  --file /opt/ajaxterm/ 'attr(0640,ajaxterm,www)' \
  --file /opt/ajaxterm/ajaxterm.py 'attr(0550,ajaxterm,www)' \
  --file /opt/ajaxterm/login.pl 'attr(0550,ajaxterm,www)' \
  --dir /usr/share/doc/smeserver-ajaxterm-1.0.5  'attr(0755,root,root)' \
 >> %{name}-%{version}-filelist
find $RPM_BUILD_ROOT -depth -type l -print
# following make 4 files listed twice, and show no more
#find $RPM_BUILD_ROOT -depth -type l -print |\
# sed "s@^$RPM_BUILD_ROOT@@g" >> %{name}-%{version}-filelist
cat %{name}-%{version}-filelist
/usr/lib/rpm/brp-python-bytecompile

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && %{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
#following make folder listed twice
#%attr(0755,root,root)    %doc %dir          /usr/share/doc/smeserver-ajaxterm-1.0.5/


