# TODO:
# 	- add zsh and bash completions
#	- check python requirements for real
#	- maybe add some useful contrib scripts to the bindir?

%define	_snap	20050303

Summary:	Hierophant Build System - a simple packaging system
Summary(pl.UTF-8):	Hierophant Build System - prosty system pakietowania
Name:		hbs
Version:	%{_snap}
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://dobremiasto.net/~hoppke/yellow_brown/Hierophant-%{version}.tar.gz
# Source0-md5:	a69d337231e91d78cc8c981ef387d28b
URL:		http://dobremiasto.net/~hoppke/hbs/
BuildRequires:  python
%pyrequires_eq  python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple packaging system for LFS-like Linux distributions.

%description -l pl.UTF-8
Prosty system pakietowania dla dystrybucji Linuksa podobnych do LFS.

%prep
%setup -q -n Hierophant-%{version}

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/contrib

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -af contrib $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%attr(750,root,root) %dir /etc/hbs
%attr(750,root,root) %dir /var/lib/hbs
%attr(750,root,root) %dir /var/tmp/hbs
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/hbs/*
