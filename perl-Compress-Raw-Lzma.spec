%define	modname	Compress-Raw-Lzma
%define	modver	2.059

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Low-Level Interface to the liblzma compression library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	pkgconfig(liblzma)

%description
Low-Level Interface to the liblzma compression library.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Compress
%{perl_vendorarch}/auto/Compress

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.59.0-1
- cleanups
- new version

* Tue Mar 13 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.49.0-1
+ Revision: 784856
- imported package perl-Compress-Raw-Lzma

* Mon Mar 13 2012 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.49.0-1
- initial release
