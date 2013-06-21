%define		php_name	php%{?php_suffix}
%define		modname	Net_Gopher
%define		extname	gopher
%define		status	stable
Summary:	%{modname} - fopen wrapper for the gopher protocol
Summary(pl.UTF-8):	%{modname} - wrapper fopen dla protokołu gopher
Name:		%{php_name}-pecl-%{modname}
Version:	1.0.0
Release:	7
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	85435fc2d8f067558acc81c33a453d83
URL:		http://pecl.php.net/package/Net_Gopher/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fopen wrapper for retrieving documents via gopher protocol. Includes
additional function for parsing gopher directory entries.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Wrapper wokół funkcji fopen pozwalający na pobieranie dokumentów za
pomocą protokołu gopher. Zawiera dodatkową funkcję służącą parsowaniu
pozycji katalogu.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure \
	--enable-gopher
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{extname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{extname}.ini
; Enable %{modname} extension module
extension=%{extname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{extname}.ini
%attr(755,root,root) %{php_extensiondir}/%{extname}.so
