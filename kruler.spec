%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		kruler
Summary:	KDE Screen Ruler
Version:	19.08.3
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://www.kde.org/applications/graphics/kruler
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kruler-19.08.2-qt-5.14.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:  cmake(KF5DocTools)                                                             
BuildRequires:  cmake(KF5I18n)                                                                 
BuildRequires:  cmake(KF5Notifications)                                                        
BuildRequires:  cmake(KF5WindowSystem)                                                         
BuildRequires:  cmake(KF5XmlGui)  
BuildRequires:	cmake(X11)

%description
KRuler displays on screen a ruler measuring pixels.
Features :
    - Integrated color picker
    - Change the length of the ruler
    - Change the orientation of the ruler
    - Change the color, transparency and font of the ruler

%files -f %{name}.lang
%{_bindir}/kruler     
%{_datadir}/knotifications5/kruler.notifyrc
%{_datadir}/applications/org.kde.kruler.desktop                                                          
%{_iconsdir}/*/*/*/kruler*
%{_datadir}/kruler/sounds/move.wav
%{_datadir}/metainfo/*.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
