Summary:	Web calendar subscription utility for Evolution
Summary(pl):	Narzêdzie do subskrypcji sieciowego kalendarza dla Evolution
Name:		evolution-webcal
Version:	2.1.91
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
# Source0-md5:	7c51c5a432439f673553be86c3d7a5dd
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.1.4
BuildRequires:	gtk+2-devel >= 2:2.6.2
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libsoup-devel >= 2.2.2
Requires(post):	GConf2
Requires:	gtk+2 >= 2:2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web calendar subscription utility for Evolution.

%description -l pl
Narzêdzie do subskrypcji sieciowego kalendarza dla Evolution.

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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
