Name: kruler
Summary: KDE Screen Ruler
Version: 4.7.95
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://www.kde.org/applications/graphics/kruler
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
KRuler displays on screen a ruler measuring pixels.
Features :
    - Integrated color picker
    - Change the length of the ruler
    - Change the orientation of the ruler
    - Change the color, transparency and font of the ruler

%files
%_kde_bindir/kruler
%_kde_applicationsdir/kruler.desktop
%_kde_appsdir/kruler
%_kde_iconsdir/*/*/*/kruler*
%doc %_kde_docdir/HTML/en/%name

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

