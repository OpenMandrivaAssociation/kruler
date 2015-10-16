Name:		kruler
Summary:	KDE Screen Ruler
Version:	15.08.2
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://www.kde.org/applications/graphics/kruler
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:  cmake(KF5DocTools)                                                             
BuildRequires:  cmake(KF5I18n)                                                                 
BuildRequires:  cmake(KF5Notifications)                                                        
BuildRequires:  cmake(KF5WindowSystem)                                                         
BuildRequires:  cmake(KF5XmlGui)  


%description
KRuler displays on screen a ruler measuring pixels.
Features :
    - Integrated color picker
    - Change the length of the ruler
    - Change the orientation of the ruler
    - Change the color, transparency and font of the ruler

%files
%doc %{_docdir}/HTML/en/%{name}                                                                        
%{_bindir}/kruler     
%{_datadir}/knotifications5/kruler.notifyrc
%{_datadir}/applications/org.kde.kruler.desktop                                                          
%{_iconsdir}/*/*/*/kruler*
%{_datadir}/kruler/sounds/move.wav

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
