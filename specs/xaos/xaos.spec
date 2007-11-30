# $Id$
# Authority: dries
# Upstream: xaos-devel@lists.sourceforge.net

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Fast, portable, real-time, and interactive fractal zoomer
Name: xaos
Version: 3.2.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://wmi.math.u-szeged.hu/xaos/doku.php

Source: http://dl.sf.net/xaos/XaoS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: aalib-devel
%{!?_without_modxorg:BuildRequires: libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
XaoS is a fast, portable, real-time, and interactive fractal zoomer. It 
displays the Mandelbrot set (among other escape time fractals) and allows 
you zoom smoothly into the fractal. Various coloring modes are provided 
for both the points inside and outside the selected set. In addition, 
switching between Julia and Mandelbrot fractal types and on-the-fly 
plane switching is provided.

%prep
%setup -n XaoS-%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=XaoS
Comment=Fractal zoomer
Exec=xaos
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Graphics;Scientific;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING doc/PROBLEMS README doc/SPONSORS TODO
%doc %{_mandir}/man6/xaos.6*
%doc %{_infodir}/xaos.info*
%{_bindir}/xaos
%{_datadir}/XaoS/
%{_datadir}/applications/*-xaos.desktop

%changelog
* Fri Nov 30 2007 Dries Verachtert <dries@ulyssis.org> - 3.2.3-1
- Updated to release 3.2.3.
