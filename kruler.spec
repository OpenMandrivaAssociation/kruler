#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		kruler
Summary:	KDE Screen Ruler
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		https://www.kde.org/applications/graphics/kruler
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/kruler/-/archive/%{gitbranch}/kruler-%{gitbranchd}.tar.bz2#/kruler-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kruler-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(KF6DocTools)                                                             
BuildRequires:  cmake(KF6I18n)                                                                 
BuildRequires:  cmake(KF6Notifications)                                                        
BuildRequires:  cmake(KF6WindowSystem)                                                         
BuildRequires:  cmake(KF6XmlGui)  
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(X11)
BuildRequires:	pkgconfig(xkbcommon)

%rename plasma6-kruler

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KRuler displays on screen a ruler measuring pixels.
Features :
    - Integrated color picker
    - Change the length of the ruler
    - Change the orientation of the ruler
    - Change the color, transparency and font of the ruler

%files -f %{name}.lang
%{_bindir}/kruler     
%{_datadir}/knotifications6/kruler.notifyrc
%{_datadir}/applications/org.kde.kruler.desktop                                                          
%{_iconsdir}/*/*/*/kruler*
%{_datadir}/kruler/sounds/move.wav
%{_datadir}/metainfo/*.appdata.xml
