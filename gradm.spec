#
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution 
%define 	grsec_version	2.0-rc3
Summary:	GrSecurity ACL Administration
Summary(pl):	Administracja ACL GrSecurity
Name:		gradm
Version:	2.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.grsecurity.net/%{name}-%{grsec_version}.tar.gz
# Source0-md5:	9758bd7407b034bf464c72c9aef27bad
Source1:	http://www.grsecurity.net/gracldoc.htm
# Source1-md5:	010802958eaed78e4c370f4f5ce142b5
URL:		http://www.grsecurity.net/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	glibc-static
BuildRequires:	texinfo
%{?with_dist_kernel:BuildRequires:	kernel-headers(grsecurity) = %{grsec_version}}
%{?with_dist_kernel:Requires:	kernel(grsecurity) > 1.9.8}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
GrSecurity ACL Administration.

%description -l pl
Administracja ACL GrSecurity.

%prep
%setup -q -n %{name}2

cp -f %{SOURCE1} .

%build
%{__make} \
	CC=%{__cc} \
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
