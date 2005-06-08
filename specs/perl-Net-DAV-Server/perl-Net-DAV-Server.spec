# $Id$

# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define real_name Net-DAV-Server
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Provides a DAV Server
Name: perl-Net-DAV-Server
Version: 1.27
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DAV-Server/

Source: http://www.cpan.org/modules/by-module/Net/Net-DAV-Server-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides a WebDAV server. WebDAV stands for "Web-based
Distributed Authoring and Versioning". It is a set of extensions to the
HTTP protocol which allows users to collaboratively edit and manage
files on remote web servers.

Net::DAV::Server provides a WebDAV server and exports a filesystem for
you using the Filesys::Virtual suite of modules. If you simply want to
export a local filesystem, use Filesys::Virtual::Plain as above.

This module doesn't currently provide a full WebDAV implementation.
However, I am working through the WebDAV server protocol compliance test
suite (litmus, see http://www.webdav.org/neon/litmus/) and will provide
more compliance in future. The important thing is that it supports
cadaver and the Mac OS X Finder as clients.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DAV/Server.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Updated to release 1.27.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Initial package.