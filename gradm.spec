#
# TODO: - add Provides: ...(grsecurity) in the kernel.spec /LINUX_2_6 should
#	  provide grsecurity/ and uncomment the Reqs
#
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution 
%bcond_with	static		# build static version
%bcond_with	debug		# build debug version
#
%define 	grsec_version	2.1.14
%define		snap		200907110111
%define		rel		1
Summary:	GrSecurity ACL Administration
Summary(pl.UTF-8):	Administracja ACL GrSecurity
Name:		gradm
Version:	%{grsec_version}
Release:	%{snap}.%{rel}
License:	GPL
Group:		Applications/System
#Source0:	http://www.grsecurity.net/%{name}-%{version}-%{snap}.tar.gz
Source0:	http://www.grsecurity.net/~spender/%{name}-%{version}-%{snap}.tar.gz
# Source0-md5:	84d356657f11b6c2eea0ced387cbc6c7
Source1:	http://www.grsecurity.net/gracldoc.htm
# Source1-md5:	010802958eaed78e4c370f4f5ce142b5
Patch0:		%{name}-caps.patch
Patch1:		%{name}-num-ugid.patch
Patch2:		%{name}-num-protocols.patch
Patch3:		%{name}-show-trans.patch
Patch4:		%{name}-symlink_depth.patch
URL:		http://www.grsecurity.net/
BuildRequires:	bison
BuildRequires:	flex
%if %{with static}
BuildRequires:	glibc-static
BuildRequires:	pam-static
BuildRequires:	sed > 4.0
%endif
BuildRequires:	pam-devel
BuildRequires:	texinfo
#{?with_dist_kernel:Requires:	kernel(grsecurity) = %{grsec_version}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
GrSecurity ACL Administration.

%description -l pl.UTF-8
Administracja ACL GrSecurity.

%prep
%setup -q -n %{name}2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
cp -f %{SOURCE1} .

%build
%{?with_static:sed -i 's/LDFLAGS=/LDFLAGS=-static -ldl/' Makefile}
%{__make} \
	CC="%{__cc}" \
	YACC=/usr/bin/bison \
	OPT_FLAGS="%{rpmcflags} %{?with_debug:-DGRADM_DEBUG}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/grsec}

install gradm $RPM_BUILD_ROOT%{_sbindir}
install gradm_pam $RPM_BUILD_ROOT%{_sbindir}
install grlearn $RPM_BUILD_ROOT%{_sbindir}
install gradm.8 $RPM_BUILD_ROOT%{_mandir}/man8
install policy $RPM_BUILD_ROOT%{_sysconfdir}/grsec
install learn_config $RPM_BUILD_ROOT%{_sysconfdir}/grsec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc gracldoc.htm
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/grsec
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/grsec/policy
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/grsec/learn_config
%{_mandir}/man8/*
