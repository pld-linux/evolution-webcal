Summary:	Web calendar subscription utility for Evolution
Summary(pl.UTF-8):	Narzędzie do subskrypcji sieciowego kalendarza dla Evolution
Name:		evolution-webcal
Version:	2.32.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-webcal/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	eec3c2464b18853fd03ebb4da1a69031
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 2.26.0
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	evolution >= 2.26.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web calendar subscription utility for Evolution.

%description -l pl.UTF-8
Narzędzie do subskrypcji sieciowego kalendarza dla Evolution.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
