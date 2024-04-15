#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		plasma6-kruler
Summary:	KDE Screen Ruler
Version:	24.02.2
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://www.kde.org/applications/graphics/kruler
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
BuildRequires:	cmake(X11)

%description
KRuler displays on screen a ruler measuring pixels.
Features :
    - Integrated color picker
    - Change the length of the ruler
    - Change the orientation of the ruler
    - Change the color, transparency and font of the ruler

%files -f kruler.lang
%{_bindir}/kruler     
%{_datadir}/knotifications6/kruler.notifyrc
%{_datadir}/applications/org.kde.kruler.desktop                                                          
%{_iconsdir}/*/*/*/kruler*
%{_datadir}/kruler/sounds/move.wav
%{_datadir}/metainfo/*.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kruler-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kruler --with-html
