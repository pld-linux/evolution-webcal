Summary:	Web calendar subscription utility for Evolution
Summary(pl):	Narzêdzie do subskrypcji sieciowego kalendarza dla Evolution
Name:		evolution-webcal
Version:	1.0.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	0121adfe452815e4ef52a7608b9c27db
Patch0:		%{name}-locale-names.patch
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 0.0.97
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libsoup-devel >= 2.1.12
Requires(post):	GConf2
Requires:	gtk+2 >= 2:2.4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web calendar subscription utility for Evolution.

%description -l pl
Narzêdzie do subskrypcji sieciowego kalendarza dla Evolution.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

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
