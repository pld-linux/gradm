Summary:	GrSecurity ACL Administration
Summary(pl):	Administracja ACL GrSecurity
Name:		gradm
Version:	1.7b
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.grsecurity.net/%{name}-%{version}.tar.gz
Source1:	http://www.grsecurity.net/gracldoc.htm
URL:		http://www.grsecurity.net/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	glibc-static
BuildRequires:  texinfo
%{!?_without_dist_kernel:BuildRequires:	kernel(grsecurity) > 1.9.8}
%{!?_without_dist_kernel:BuildRequires:	kernel-headers >= 2.4}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
GrSecurity ACL Administration.

%description -l pl
Administracja ACL GrSecurity.

%prep
%setup -q -n %{name}

cp -f %{SOURCE1} .

%build
%{__make} \
	YACC=/usr/bin/bison \
	CFLAGS="%{rpmcflags} -static"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/grsec}

install gradm $RPM_BUILD_ROOT%{_sbindir}
install gradm.8 $RPM_BUILD_ROOT%{_mandir}/man8
install acl $RPM_BUILD_ROOT%{_sysconfdir}/grsec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc gracldoc.htm
%attr(755,root,root) %{_sbindir}/gradm
%dir %{_sysconfdir}/grsec
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/grsec/acl
%{_mandir}/man8/*
