Summary:	Main Menu Editor for LXDE. Written in Java
Summary(de.UTF-8):	Main Menu Editor für LXDE. Geschrieben in Java.
Name:		lxmed
Version:	20120515
Release:	0.1
License:	GPL v3
Group:		X11/Applications
URL:		http://sourceforge.net/projects/lxmed
Source0:	http://downloads.sourceforge.net/lxmed/%{name}-%{version}.tar.gz
# Source0-md5:	dfbda46aad608d32f28ffdf44a3b1ac3
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	jpackage-utils
Requires:	jre
Requires:	desktop-file-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxmed is a small, simple, free, open source, easy to use application
that allows you to customize the LXDE menu.

lxmed is very useful for people that want to create their own,
customized menus for LXDE.

lxmed is written in the Java programming language.

%description -l de.UTF-8
lxmed ist ein kleines, einfaches, kostenloses, Open Source, Anwendung,
mit dem Sie das LXDE-Menü anpassen können.

lxmed ist sehr nützlich für Leute, die ihre eigene, individuelle Menüs
für LXDE erstellen möchten.

lxmed ist in der Programmiersprache Java geschrieben.

%prep
%setup -q -n %{name}

cat > %{name}.sh << 'EOF'
#!/bin/sh
exec java -jar %{_datadir}/%{name}/LXMenuEditor.jar "$@"
EOF

cat > %{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Exec=lxmed
Icon=lxmed
Type=Application
Terminal=false
Name=Main Menu Editor
GenericName=Main Menu Editor
StartupNotify=false
Categories=Settings;DesktopSettings;X-LXDE-Settings;
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir}}
install -p %{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

cp -p content/LXMenuEditor.jar $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p content/lxmed.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}


%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
