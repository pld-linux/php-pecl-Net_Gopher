%define		_modname	Net_Gopher
%define		_smodname	gopher
%define		_status		beta
Summary:	%{_modname} - fopen wrapper for the gopher protocol
Summary(pl):	%{_modname} - wrapper fopen dla protoko³u gopher
Name:		php-pecl-%{_modname}
Version:	0.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	2bf3c726585b8eb754b4c43fef7c6079
URL:		http://pear.php.net/
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
fopen wrapper for retrieving documents via gopher protocol. Includes
additional function for parsing gopher directory entries.

This extension has in PEAR status: %{_status}.

%description -l pl
Wrapper wokó³ funkcji fopen pozwalaj±cy na pobieranie dokumentów za
pomoc± protoko³u gopher. Zawiera dodatkow± funkcjê s³u¿±c± parsowaniu
pozycji katalogu.

To rozszerzenie ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure --enable-gopher
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_smodname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_smodname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_smodname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_smodname}.so
