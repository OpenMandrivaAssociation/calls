Name:		calls
Version:	41.1
Release:	1%{?dist}
Summary:	A phone dialer and call handler

License:	GPLv3+ and MIT
URL:		https://gitlab.gnome.org/GNOME/calls
Source0:	https://gitlab.gnome.org/GNOME/calls/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	gcc-c++

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

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Calls.desktop

# Some tests are failing in the build environment, so we manually just run a handful for now.
LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test manager plugins
SH


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

%changelog
* Sat Oct 30 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41.1-1
- Update to 41.1

* Mon Sep 20 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41.0-1
- Update to 41.0

* Fri Sep 10 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41.rc-1
- Update to 41.rc

* Sat Aug 14 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41~.beta-1
- Update to 41.beta

* Sat Aug 07 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 41~.alpha-1
- Change source to new upstream location https://gitlab.gnome.org/GNOME/calls
- Update to 41.alpha

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Thu May 20 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.3-1
- Update version 0.3.3

* Mon May 03 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.2-1
- Update version 0.3.2

* Tue Feb 16 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-1
- Update version 0.3.1

* Sat Feb 13 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.0-1
- Update version 0.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-3
- Patch for callaudiod-0.1

* Tue Jan 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-2
- Bump for libcallaudio-0.1.so

* Wed Jan 06 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-1
- Update version 0.2.0

* Sun Nov 08 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.9-1
- Update version 0.1.9

* Fri Sep 18 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.8-1
- Update version 0.1.8

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.7-1
- Update version 0.1.7

* Wed Jun 24 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.6-2
- Rebuild for broken libebook-contacts

* Fri Jun 12 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.6-1
- Update version 0.1.6

* Mon May 18 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.5-1
- Owning the directories for calls, plugins, and mm.
- Update version 0.1.5.
- Adding MIT to License
- Upstream changed "appdata" to "metainfo"

* Fri Apr 24 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.4-1
- Updating version 0.1.4. Fixing comments from review regarding ofono and appdata.

* Fri Mar 27 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.3-1 
- Updating version 0.1.3. Adding tests

* Wed Mar 25 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.2-2
- Adding license and meson_test. Remove buildid

* Sun Mar 08 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.2-1
- Initial packaging
