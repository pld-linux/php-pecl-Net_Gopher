%define		_modname	Net_Gopher
%define		_smodname	gopher
%define		_status		stable
Summary:	%{_modname} - fopen wrapper for the gopher protocol
Summary(pl):	%{_modname} - wrapper fopen dla protoko³u gopher
Name:		php-pecl-%{_modname}
Version:	1.0.0
Release:	6
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	85435fc2d8f067558acc81c33a453d83
URL:		http://pecl.php.net/package/Net_Gopher/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fopen wrapper for retrieving documents via gopher protocol. Includes
additional function for parsing gopher directory entries.

In PECL status of this package is: %{_status}.

%description -l pl
Wrapper wokó³ funkcji fopen pozwalaj±cy na pobieranie dokumentów za
pomoc± protoko³u gopher. Zawiera dodatkow± funkcjê s³u¿±c± parsowaniu
pozycji katalogu.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure --enable-gopher
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_smodname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_smodname}.ini
; Enable %{_modname} extension module
extension=%{_smodname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_smodname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_smodname}.so
