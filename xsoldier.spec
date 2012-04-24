Summary:	Shooting game on X Window System
Name:		xsoldier
Version:	1.8
Release:	%mkrel 1
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

