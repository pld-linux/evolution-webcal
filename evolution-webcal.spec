Summary:	Web calendar subscription utility for Evolution
Name:		evolution-webcal
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gnome.org/~dobey/%{name}-%{version}.tar.bz2
# Source0-md5:	08d818efdb21a880015f89077556ac5d
Patch0:		%{name}-paths.patch
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 0.0.90
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libsoup-devel >= 2.1.8
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web calendar subscription utility for Evolution.

%prep
%setup -q
%patch0 -p1

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
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/evolution-webcal
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/application-registry/*
