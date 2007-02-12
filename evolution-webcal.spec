Summary:	Web calendar subscription utility for Evolution
Summary(pl.UTF-8):	Narzędzie do subskrypcji sieciowego kalendarza dla Evolution
Name:		evolution-webcal
Version:	2.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/evolution-webcal/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	6dd4821ce90e238acbd8a959fee1ee14
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.8.0
BuildRequires:	gtk+2-devel >= 2:2.10.3
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	libsoup-devel >= 2.2.96
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	evolution >= 2.8.0
Requires:	gtk+2 >= 2:2.10.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web calendar subscription utility for Evolution.

%description -l pl.UTF-8
Narzędzie do subskrypcji sieciowego kalendarza dla Evolution.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install evolution-webcal.schemas

%preun
%gconf_schema_uninstall evolution-webcal.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/evolution-webcal
%{_sysconfdir}/gconf/schemas/evolution-webcal.schemas
