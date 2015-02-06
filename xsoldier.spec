Summary:	Shooting game on X Window System
Name:		xsoldier
Version:	1.8
Release:	2
License:	GPLv2
Group:		Games/Arcade
URL:		http://www.interq.or.jp/libra/oohara/xsoldier/
Source0:	http://www.interq.or.jp/libra/oohara/xsoldier/%{name}-%{version}.tar.gz
Source3:	%{name}-icons.tar.bz2
Patch0:		%{name}-1.5-mdv-fix-str-fmt.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	pkgconfig(x11)
Buildrequires:	pkgconfig(xpm)

%description
Great little shoot 'em up game in the style of galaga. Very neat graphics, but
there's no sound support yet.

%prep
%setup -q
%patch0 -p1 -b .strfmt

%build
%configure --bindir=%{_gamesbindir} --localstatedir=%{_localstatedir}/lib  --with-sdl
%make

%install
%__rm -fr %{buildroot}

%makeinstall bindir=%{buildroot}%{_gamesbindir} datadir=%{buildroot}%{_datadir} localstatedir=%{buildroot}%{_localstatedir}/lib mandir=%{buildroot}%{_mandir}

%__install -m 755 -d %{buildroot}/%{_menudir}
%__install -m 755 -d %{buildroot}/%{_iconsdir}

(cd  %{buildroot}/%{_iconsdir} ; bunzip2 -c %{SOURCE3} | tar xvf - )

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

%__chmod 777 %{buildroot}/%{_localstatedir}/lib/games/xsoldier
%__cp scorefile.txt %{buildroot}/%{_localstatedir}/lib/games/xsoldier/xsoldier.scores

%clean
%__rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README LICENSE INSTALL
%attr(0755, root, games) %{_gamesbindir}/*
%{_gamesdatadir}/*
%{_datadir}/applications/*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_mandir}/man6/*
%attr(664, games, games) %{_localstatedir}/lib/games/xsoldier/xsoldier.scores



%changelog
* Tue Apr 24 2012 Andrey Bondrov <abondrov@mandriva.org> 1.8-1mdv2011.0
+ Revision: 793132
- New version 1.8

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-2mdv2011.0
+ Revision: 615737
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Jérôme Brenier <incubusss@mandriva.org> 1.5-1mdv2010.1
+ Revision: 464479
- update to new version 1.5
- fix str fmt
- $RPM_BUILD_ROOT -> %%{buildroot}

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2009.0
+ Revision: 262717
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2009.0
+ Revision: 257773
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 1.4-3mdv2008.1
+ Revision: 140994
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-3mdv2008.0
+ Revision: 90387
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Apr 30 2007 Crispin Boylan <crisb@mandriva.org> 1.4-2mdv2008.0
+ Revision: 19452
- Fix menu name


* Tue Jan 23 2007 Crispin Boylan <crisb@mandriva.org> 1.4-1mdv2007.0
+ Revision: 112663
- New version, XDG menu
- Import xsoldier

* Thu Jan 05 2006 Lenny Cartier <lenny@mandriva.com> 1.3-5mdk
- rebuild

* Thu Jul 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3-4mdk
- rebuild

