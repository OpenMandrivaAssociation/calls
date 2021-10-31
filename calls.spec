Name:		calls
Version:	41.1
Release:	1
Summary:	A phone dialer and call handler
License:	GPLv3+ and MIT
URL:		https://gitlab.gnome.org/GNOME/calls
Source0:	https://gitlab.gnome.org/GNOME/calls/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	meson
BuildRequires:	cmake

BuildRequires:	pkgconfig(libcallaudio-0.1)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libhandy-1) >= 1.0.0
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(gom-1.0)
BuildRequires:	pkgconfig(libebook-contacts-1.2)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(mm-glib)
BuildRequires:	pkgconfig(libfeedback-0.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	gstreamer1-plugins-good-gtk
BuildRequires:	sofia-sip-glib-devel

BuildRequires:	desktop-file-utils
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	/usr/bin/xauth
BuildRequires:	libappstream-glib

Requires: hicolor-icon-theme

%description
A phone dialer and call handler.

%prep
%setup -q -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}


%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/org.gnome.Calls-daemon.desktop
%{_bindir}/gnome-%{name}

%dir %{_libdir}/calls
%dir %{_libdir}/calls/plugins
%dir %{_libdir}/calls/plugins/mm
%dir %{_libdir}/calls/plugins/dummy
%dir %{_libdir}/calls/plugins/sip

%{_libdir}/calls/plugins/mm/libmm.so
%{_libdir}/calls/plugins/mm/mm.plugin
%{_libdir}/calls/plugins/dummy/dummy.plugin
%{_libdir}/calls/plugins/dummy/libdummy.so
%{_libdir}/calls/plugins/sip/libsip.so
%{_libdir}/calls/plugins/sip/sip.plugin

# ofono is retired so we exclude the plugins 4/24/2020
%exclude %{_libdir}/calls/plugins/ofono/libofono.so
%exclude %{_libdir}/calls/plugins/ofono/ofono.plugin

%{_datadir}/glib-2.0/schemas/org.gnome.Calls.gschema.xml
%{_datadir}/applications/org.gnome.Calls.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Calls.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calls-symbolic.svg
%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml

%doc README.md
%license COPYING
