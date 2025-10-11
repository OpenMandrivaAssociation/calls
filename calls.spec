%define libcalls_ver 0.1.4

Name:		calls
Version:	49.1
Release:	1
Summary:	A phone dialer and call handler
Group:		Applications/Communications
License:	GPLv3+ and MIT
URL:		https://gitlab.gnome.org/GNOME/calls
Source0   https://download.gnome.org/sources/calls/49/calls-%{version}.tar.xz
#Source0:	https://gitlab.gnome.org/GNOME/calls/-/archive/%{version}/%{name}-v%{version}.tar.bz2
#Source1:  https://gitlab.gnome.org/World/Phosh/libcall-ui/-/archive/v%{libcalls_ver}/libcall-ui-v%{libcalls_ver}.tar.bz2

BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	pkgconfig(libcallaudio-0.1)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libhandy-1) >= 1.0.0
BuildRequires:	pkgconfig(gsound)
BuildRequires:  pkgconfig(libgdata)
BuildRequires:	pkgconfig(libpeas-2)
BuildRequires:	pkgconfig(gom-1.0)
BuildRequires:	pkgconfig(libebook-contacts-1.2)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(mm-glib)
BuildRequires:	pkgconfig(libfeedback-0.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	gstreamer1.0-plugins-good
BuildRequires:	pkgconfig(sofia-sip-ua)
BuildRequires:	pkgconfig(sofia-sip-ua-glib)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  dbus
BuildRequires:  dbus-daemon
BuildRequires:	desktop-file-utils
BuildRequires:	x11-server-xvfb
BuildRequires:	xauth
BuildRequires:	appstream-util
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  python-docutils

Requires: hicolor-icon-theme

%description
A phone dialer and call handler.

%prep
%autosetup -n %{name}-%{version} -p1

#mv libcall-ui-v%{libcalls_ver}/* subprojects/libcall-ui/

%build
%meson -Dtests=false
%meson_build

%install
%meson_install

%find_lang %{name}
%find_lang %{name}-ui

%files -f %{name}.lang -f %{name}-ui.lang
%{_sysconfdir}/xdg/autostart/org.gnome.Calls-daemon.desktop
%{_bindir}/gnome-%{name}
%{_prefix}/lib/systemd/user/calls-daemon.service
%dir %{_libdir}/calls
%{_libdir}/calls/plugins/
%{_datadir}/glib-2.0/schemas/org.gnome.Calls.gschema.xml
%{_datadir}/applications/org.gnome.Calls.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Calls.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calls-symbolic.svg
%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.Calls.service
%{_mandir}/man1/gnome-calls.1.*
%doc README.md
%license COPYING
