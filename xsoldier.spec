%define name	xsoldier
%define version 1.5
%define release %mkrel 1

Summary:	Shooting game on X Window System
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
BuildRequires:	libx11-devel
BuildRequires:	libSDL-devel
BuildRequires:	libSDL_image-devel
Source:		http://www.interq.or.jp/libra/oohara/xsoldier/%{name}-%{version}.tar.gz
Source3:	%{name}-icons.tar.bz2
Patch0:		%{name}-1.5-mdv-fix-str-fmt.patch
URL:		http://www.interq.or.jp/libra/oohara/xsoldier/
Buildrequires:	libxpm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
rm -fr %{buildroot}

%makeinstall bindir=%{buildroot}%{_gamesbindir} datadir=%{buildroot}%{_datadir} localstatedir=%{buildroot}%{_localstatedir}/lib mandir=%{buildroot}%{_mandir}

install -m 755 -d %{buildroot}/%{_menudir}
install -m 755 -d %{buildroot}/%{_iconsdir}

(cd  %{buildroot}/%{_iconsdir} ; bunzip2 -c %{SOURCE3} | tar xvf - ) 

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{_gamesbindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

chmod 777 %{buildroot}/%{_localstatedir}/lib/games/xsoldier
cp scorefile.txt %{buildroot}/%{_localstatedir}/lib/games/xsoldier/xsoldier.scores

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -fr %{buildroot}

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


