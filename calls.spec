%define libcalls_ver 0.1.4

Name:		calls
Version:	49.1.1
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

# Remove call-ui translations
rm %{buildroot}%{_datadir}/locale/ca/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pt_BR/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ro/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/uk/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fa/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fur/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/nl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pt/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sv/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/gl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/it/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fi/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/he/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ka/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/oc/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/sr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/tr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/el/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/hr/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/cs/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/eu/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/hi/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/hu/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/be/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/ht/LC_MESSAGES/call-ui.mo
rm %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/call-ui.mo

%find_lang %{name}

%files -f %{name}.lang
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
