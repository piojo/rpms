# $Id$

# Authority: dries
# Upstream: Manuel Valente <mvalente$ripe,net>

%define real_name Net-IP
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl extension for manipulating IPv4/IPv6 addresses
Name: perl-Net-IP
Version: 1.23
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IP/

Source: http://www.cpan.org/modules/by-module/Net/Net-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl extension for manipulating IPv4/IPv6 addresses.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes COPYING
%doc %{_mandir}/man3/*
%{_bindir}/*
%{perl_vendorlib}/Net/IP.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
