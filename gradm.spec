Summary:	GrSecurity ACL Administration
Summary(pl):	Administracja ACL GrSecurity
Name:		gradm
Version:	1.1c
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.grsecurity.net/%{name}-%{version}.tar.gz
Source1:	http://www.grsecurity.net/obvdoc.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.grsecurity.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
GrSecurity ACL Administration.

%description -l pl
Administracja ACL GrSecurity.

%prep
%setup -q -a1
%patch -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install gradm.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf ChangeLog config/README config/Setup

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz config/*.gz config/*.acl config/rc.grsec
%attr(755,root,root) %{_sbindir}/gradm
%{_sysconfdir}/grsec
%{_mandir}/man8/*
